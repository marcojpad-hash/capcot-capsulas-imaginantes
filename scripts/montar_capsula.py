#!/usr/bin/env python3
"""Monta una cápsula vertical 9:16 desde un storyboard con frames PNG locales.
Uso: python3 montar_capsula.py proyectos/x/storyboard.json -o salida.mp4
Requiere: ffmpeg/ffprobe, edge-tts (pip), Pillow.
Pasos: TTS por escena (edge-tts, WordBoundary) -> SRT por palabras -> Ken Burns
(zoompan) por frame -> cortinilla de fuentes (Pillow) -> concat + subtítulos
quemados + música opcional con ducking -> MP4 1080x1920 30 fps."""
import argparse, asyncio, json, os, subprocess, sys, tempfile
from PIL import Image, ImageDraw, ImageFont

W, H, FPS = 1080, 1920, 30
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_R = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def run(cmd):
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)

def dur(path):
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                          "-of", "csv=p=0", path]).decode().strip())

async def tts(text, voice, out_mp3, rate="+0%", pitch="+0Hz"):
    import edge_tts
    c = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch, boundary="WordBoundary")
    words = []
    with open(out_mp3, "wb") as f:
        async for ch in c.stream():
            if ch["type"] == "audio": f.write(ch["data"])
            elif ch["type"] == "WordBoundary":
                words.append((ch["offset"] / 1e7, (ch["offset"] + ch["duration"]) / 1e7, ch["text"]))
    return words

def ts(t):
    ms = int(round(t * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"

def srt_from_words(words, max_words=3):
    out, i, n = [], 0, 1
    while i < len(words):
        chunk = words[i:i + max_words]
        # cortar en puntuación fuerte
        for j, w in enumerate(chunk):
            if w[2][-1:] in ".,;:?!" and j < len(chunk) - 1:
                chunk = chunk[:j + 1]; break
        nxt = words[i + len(chunk)][0] if i + len(chunk) < len(words) else 1e9
        end = min(chunk[-1][1] + 0.3, nxt - 0.01)
        out.append(f"{n}\n{ts(chunk[0][0])} --> {ts(end)}\n{' '.join(w[2] for w in chunk)}\n")
        i += len(chunk); n += 1
    return "\n".join(out)

def wrap(draw, text, font, maxw):
    lines, cur = [], ""
    toks = []
    for w in text.split():  # partir tokens largos (URLs/DOIs) que no caben
        while draw.textlength(w, font=font) > maxw and len(w) > 1:
            k = len(w)
            while k > 1 and draw.textlength(w[:k], font=font) > maxw: k -= 1
            toks.append(w[:k]); w = w[k:]
        toks.append(w)
    for w in toks:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=font) <= maxw: cur = t
        else: lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines

def cortinilla(sb, out_png):
    c = sb["cortinilla_fuentes"]
    img = Image.new("RGB", (W, H), tuple(c.get("bg_rgb", [18, 16, 14])))
    d = ImageDraw.Draw(img)
    ft, fs, fn = ImageFont.truetype(FONT, 64), ImageFont.truetype(FONT_R, 40), ImageFont.truetype(FONT_R, 34)
    # zona segura: 10% arriba, 20% abajo, 15% derecha (botones TikTok)
    x0, maxw, y = int(W * .08), int(W * .77), int(H * .14)
    d.text((x0, y), c.get("titulo", "Fuentes"), font=ft, fill=(240, 200, 120)); y += 120
    for s in sb["sources"]:
        for ln in wrap(d, s["cita_corta"], fs, maxw):
            d.text((x0, y), ln, font=fs, fill=(235, 235, 235)); y += 52
        ref = s.get("ref_display") or ("doi.org/" + s["doi"] if s.get("doi") else s["url"])
        for ln in wrap(d, ref, fn, maxw):
            d.text((x0, y), ln, font=fn, fill=(160, 190, 230)); y += 46
        y += 40
    for ln in wrap(d, c.get("aviso", ""), fn, maxw):
        d.text((x0, y + 20), ln, font=fn, fill=(170, 170, 170)); y += 46
    if y > H * .80: print("AVISO: la cortinilla invade la zona segura inferior", file=sys.stderr)
    img.save(out_png)

def kenburns(png, seconds, out_mp4, idx):
    frames = int(round(seconds * FPS))
    zin = idx % 2 == 0
    z = f"min(1+0.12*on/{frames},1.12)" if zin else f"max(1.12-0.12*on/{frames},1)"
    vf = (f"scale={W*2}:{H*2}:force_original_aspect_ratio=increase,crop={W*2}:{H*2},"
          f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={frames}:s={W}x{H}:fps={FPS},"
          f"format=yuv420p")
    run(["ffmpeg", "-y", "-loop", "1", "-i", png, "-vf", vf, "-frames:v", str(frames),
         "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", out_mp4])

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("storyboard"); ap.add_argument("-o", "--out", required=True)
    a = ap.parse_args()
    sb = json.load(open(a.storyboard, encoding="utf-8")); base = os.path.dirname(os.path.abspath(a.storyboard))
    v = sb["voice"]; tmp = tempfile.mkdtemp(prefix="capcot_")
    pad = float(v.get("pad_seconds", 0.6))
    clips, audio_parts, all_words, t = [], [], [], 0.0
    for i, sc in enumerate(sb["scenes"]):
        mp3 = os.path.join(tmp, f"{sc['id']}.mp3")
        words = asyncio.run(tts(sc["narration"], v["voice_id"], mp3, v.get("rate", "+0%"), v.get("pitch", "+0Hz"))) if sc["narration"].strip() else []
        adur = dur(mp3) if words else 0.0
        sdur = max(float(sc["duration_seconds"]), adur + pad)
        toks = sc["narration"].split()  # recuperar puntuación del guion (edge-tts la omite)
        if len(toks) == len(words): words = [(s, e, tok) for (s, e, _), tok in zip(words, toks)]
        all_words += [(s + t + 0.25, e + t + 0.25, w) for s, e, w in words]
        wav = os.path.join(tmp, f"{sc['id']}.wav")
        src = ["-i", mp3] if words else ["-f", "lavfi", "-i", "anullsrc=r=48000:cl=mono"]
        run(["ffmpeg", "-y", *src, "-af", f"adelay=250,apad", "-t", f"{sdur:.3f}", "-ar", "48000", "-ac", "2", wav])
        audio_parts.append(wav)
        mp4 = os.path.join(tmp, f"{sc['id']}.mp4")
        kenburns(os.path.join(base, sc["asset_filename"]), sdur, mp4, i); clips.append(mp4)
        print(f"{sc['id']}: voz {adur:.1f}s, escena {sdur:.1f}s"); t += sdur
    cd = float(sb["cortinilla_fuentes"].get("duration_seconds", 6))
    cpng = os.path.join(tmp, "cortinilla.png"); cortinilla(sb, cpng)
    cmp4 = os.path.join(tmp, "cortinilla.mp4")
    run(["ffmpeg", "-y", "-loop", "1", "-i", cpng, "-t", f"{cd}", "-r", str(FPS), "-vf", "format=yuv420p",
         "-c:v", "libx264", "-preset", "veryfast", cmp4]); clips.append(cmp4)
    cwav = os.path.join(tmp, "cortinilla.wav")
    run(["ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo", "-t", f"{cd}", cwav]); audio_parts.append(cwav)
    with open(os.path.join(tmp, "v.txt"), "w") as f: f.writelines(f"file '{c}'\n" for c in clips)
    with open(os.path.join(tmp, "a.txt"), "w") as f: f.writelines(f"file '{c}'\n" for c in audio_parts)
    vcat, acat = os.path.join(tmp, "v.mp4"), os.path.join(tmp, "voz.wav")
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", os.path.join(tmp, "v.txt"), "-c", "copy", vcat])
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", os.path.join(tmp, "a.txt"), "-c", "copy", acat])
    srt = os.path.splitext(a.out)[0] + ".srt"
    open(srt, "w", encoding="utf-8").write(srt_from_words(all_words, sb["export"].get("subtitle_max_words", 3)))
    style = ("FontName=DejaVu Sans,FontSize=16,Bold=1,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,"
             "BorderStyle=1,Outline=3,Shadow=0,Alignment=2,MarginV=70")
    vf = f"subtitles={srt}:original_size={W}x{H}:force_style='{style}'"
    music = sb.get("audio", {}).get("music_asset")
    cmd = ["ffmpeg", "-y", "-i", vcat, "-i", acat]
    if music:
        cmd += ["-stream_loop", "-1", "-i", os.path.join(base, music),
                "-filter_complex", f"[2:a]volume={sb['audio'].get('music_volume',0.25)}[m];"
                f"[m][1:a]sidechaincompress=threshold=0.03:ratio=8[md];[1:a][md]amix=inputs=2:duration=first,"
                f"loudnorm=I=-14:TP=-1.5[aout];[0:v]{vf}[vout]", "-map", "[vout]", "-map", "[aout]"]
    else:
        cmd += ["-vf", vf, "-af", "loudnorm=I=-14:TP=-1.5", "-map", "0:v", "-map", "1:a"]
    cmd += ["-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p", "-r", str(FPS),
            "-c:a", "aac", "-b:a", "160k", "-ar", "48000", "-shortest", "-movflags", "+faststart", a.out]
    run(cmd)
    d = dur(a.out); print(f"OK {a.out} duración {d:.2f}s")
    if not 60 <= d <= 90: print("ERROR: duración fuera de 60-90 s", file=sys.stderr); sys.exit(2)

if __name__ == "__main__":
    main()
