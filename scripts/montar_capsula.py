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

async def _tts_one(text, voice, out_mp3, rate, pitch):
    import edge_tts
    c = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch, boundary="WordBoundary")
    words = []
    with open(out_mp3, "wb") as f:
        async for ch in c.stream():
            if ch["type"] == "audio": f.write(ch["data"])
            elif ch["type"] == "WordBoundary":
                words.append((ch["offset"] / 1e7, (ch["offset"] + ch["duration"]) / 1e7, ch["text"]))
    return words

# Pausas naturales: edge-tts no acepta SSML <break>, así que se sintetiza frase por
# frase y se insertan silencios según la puntuación final (".", "?", "…", ":").
# Regla de pausas (feedback Mj 2026-10-24): narración casi continua, pausas 0.3–0.6 s.
PAUSAS = {".": 0.45, "?": 0.55, "!": 0.5, "…": 0.6, ":": 0.3, ";": 0.3}

def _frases(text):
    import re
    partes = re.findall(r"[^.?!…:;]+(?:\.\.\.|[.?!…:;]+)?", text)
    return [p.strip() for p in partes if p.strip()]

async def tts(text, voice, out_mp3, rate="+0%", pitch="+0Hz"):
    tmpd = tempfile.mkdtemp(prefix="tts_"); parts, words, t = [], [], 0.0
    frases = _frases(text)
    for k, fr in enumerate(frases):
        mp = os.path.join(tmpd, f"{k}.mp3")
        ws = await _tts_one(fr, voice, mp, rate, pitch)
        # recortar el silencio que edge-tts deja al inicio/final de cada frase (si no, las pausas se duplican ~1 s)
        a0 = max(ws[0][0] - 0.05, 0) if ws else 0.0
        a1 = min(ws[-1][1] + 0.15, dur(mp)) if ws else dur(mp)
        d = a1 - a0
        words += [(s - a0 + t, e - a0 + t, w) for s, e, w in ws]
        wav = os.path.join(tmpd, f"{k}.wav")
        fin = "…" if fr.endswith("...") else fr[-1]
        gap = PAUSAS.get(fin, 0.15) if k < len(frases) - 1 else 0.0
        run(["ffmpeg", "-y", "-i", mp, "-af", f"atrim={a0:.3f}:{a1:.3f},asetpts=PTS-STARTPTS,afade=t=out:st={max(d-0.04,0):.3f}:d=0.04,apad=pad_dur={gap}",
             "-ar", "48000", "-ac", "1", wav])
        parts.append(wav); t += d + gap
    lst = os.path.join(tmpd, "l.txt")
    with open(lst, "w") as f: f.writelines(f"file '{p}'\n" for p in parts)
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c:a", "libmp3lame", "-q:a", "2", out_mp3])
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
    if c.get("firma") or sb.get("canal"):  # end card del canal (sin números en nombres/handles)
        f = c.get("firma") or f"{sb['canal']['nombre']} · {sb['canal']['handle']}"
        y += 70
        for ln in f.split(" · "):
            d.text((x0, y), ln, font=ImageFont.truetype(FONT, 46), fill=(240, 200, 120)); y += 62
    if y > H * .80: print("AVISO: la cortinilla invade la zona segura inferior", file=sys.stderr)
    img.save(out_png)

# ---- Cama sonora sintética (ambiente + música), generada con ffmpeg: sin derechos de terceros ----
NOTAS = {"A2": 110.0, "C3": 130.81, "D3": 146.83, "E3": 164.81, "F2": 87.31, "F3": 174.61, "G2": 98.0,
         "G3": 196.0, "A3": 220.0, "B3": 246.94, "C4": 261.63, "D4": 293.66, "E4": 329.63, "G4": 392.0}
PROGRESIONES = {"menor_calma": [["A2", "E3", "A3", "C4"], ["F2", "C3", "A3", "C4"], ["C3", "G3", "C4", "E4"], ["G2", "D3", "G3", "B3"]]}

def _pad(dst, total, prog="menor_calma", acorde_s=6.0):
    tmpd = tempfile.mkdtemp(prefix="pad_"); parts = []
    for k, ch in enumerate(PROGRESIONES[prog]):
        expr = "+".join(f"{0.18/(1+j*0.5):.3f}*sin(2*PI*{NOTAS[n]}*t)*(1+0.3*sin(2*PI*{0.2+0.07*j:.2f}*t))"
                        for j, n in enumerate(ch))
        pp = os.path.join(tmpd, f"{k}.wav")
        run(["ffmpeg", "-y", "-f", "lavfi", "-i", f"aevalsrc='{expr}':s=48000:d={acorde_s}",
             "-af", f"afade=t=in:d=1.5,afade=t=out:st={acorde_s-1.5}:d=1.5", pp]); parts.append(pp)
    lst = os.path.join(tmpd, "l.txt"); open(lst, "w").writelines(f"file '{p}'\n" for p in parts)
    run(["ffmpeg", "-y", "-stream_loop", "-1", "-f", "concat", "-safe", "0", "-i", lst, "-t", f"{total:.2f}",
         "-af", "lowpass=f=1800,aecho=0.8:0.7:120|260:0.35|0.25,afade=t=in:d=2,"
                f"afade=t=out:st={max(total-3,0):.2f}:d=3,loudnorm=I=-40:TP=-2", "-ac", "2", "-ar", "48000", dst])

def _ambiente(tipo, dst, total):
    if tipo == "oceano":   # oleaje: ruido marrón con vaivén lento (~9 s por ola)
        src, af = "anoisesrc=c=brown:r=48000:a=0.5", "lowpass=f=900,highpass=f=60,volume='0.45+0.55*pow(sin(PI*0.11*t),2)':eval=frame"
    elif tipo == "viento":  # viento: ruido rosa en banda media con ráfagas lentas
        src, af = "anoisesrc=c=pink:r=48000:a=0.5", "bandpass=f=600:w=500,volume='0.5+0.5*sin(2*PI*0.07*t)':eval=frame"
    else: raise SystemExit(f"ambiente desconocido: {tipo}")
    run(["ffmpeg", "-y", "-f", "lavfi", "-i", src, "-t", f"{total:.2f}", "-af",
         f"{af},afade=t=in:d=2,afade=t=out:st={max(total-3,0):.2f}:d=3,loudnorm=I=-38:TP=-2", "-ac", "2", dst])

def cama_sonora(aud, base, total, tmp):
    """aud = sb['audio']: ambiente: oceano|viento|oceano+viento|<archivo>; music_asset: <archivo> | 'sintetico:menor_calma'.
    Devuelve lista de wavs (cada uno ya normalizado ~-38/-40 LUFS: ≥22 dB bajo la voz a -16)."""
    out = []
    amb = aud.get("ambiente", "")
    for k, a in enumerate([x for x in amb.split("+") if x]):
        dst = os.path.join(tmp, f"amb{k}.wav")
        if a in ("oceano", "viento"): _ambiente(a, dst, total)
        else: run(["ffmpeg", "-y", "-stream_loop", "-1", "-i", os.path.join(base, a), "-t", f"{total:.2f}",
                   "-af", "loudnorm=I=-38:TP=-2", "-ac", "2", "-ar", "48000", dst])
        out.append(dst)
    m = aud.get("music_asset", "")
    if m:
        dst = os.path.join(tmp, "musica.wav")
        if m.startswith("sintetico"): _pad(dst, total, m.split(":", 1)[1] if ":" in m else "menor_calma")
        else: run(["ffmpeg", "-y", "-stream_loop", "-1", "-i", os.path.join(base, m), "-t", f"{total:.2f}",
                   "-af", f"loudnorm=I={aud.get('music_lufs', -40)}:TP=-2", "-ac", "2", "-ar", "48000", dst])
        out.append(dst)
    return out

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
    continuo = v.get("modo_pausas", "continuo") == "continuo"
    pad = float(v.get("pad_seconds", 0.35 if continuo else 0.6))
    clips, audio_parts, all_words, t = [], [], [], 0.0
    for i, sc in enumerate(sb["scenes"]):
        mp3 = os.path.join(tmp, f"{sc['id']}.mp3")
        words = asyncio.run(tts(sc["narration"], v["voice_id"], mp3, v.get("rate", "+11%"), v.get("pitch", "-2Hz"))) if sc["narration"].strip() else []
        adur = dur(mp3) if words else 0.0
        if continuo and words: sdur = adur + 0.25 + pad   # la escena dura lo que su voz: sin huecos
        elif continuo: sdur = float(sc.get("duration_seconds", 3))
        else: sdur = max(float(sc["duration_seconds"]), adur + pad)
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
    camas = cama_sonora(sb.get("audio", {}), base, dur(acat), tmp)
    cmd = ["ffmpeg", "-y", "-i", vcat, "-i", acat]
    if camas:
        for c in camas: cmd += ["-i", c]
        n = len(camas); ins = "".join(f"[{k+2}:a]" for k in range(n))
        fc = (f"[1:a]loudnorm=I=-16:TP=-2,asplit=2[v][sc];{ins}amix=inputs={n}:normalize=0[bed];"
              f"[bed][sc]sidechaincompress=threshold=0.02:ratio=6:attack=20:release=500:makeup=1[duck];"
              f"[v][duck]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5[aout];[0:v]{vf}[vout]")
        cmd += ["-filter_complex", fc, "-map", "[vout]", "-map", "[aout]"]
    else:
        cmd += ["-vf", vf, "-af", "loudnorm=I=-14:TP=-1.5", "-map", "0:v", "-map", "1:a"]
    cmd += ["-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p", "-r", str(FPS),
            "-c:a", "aac", "-b:a", "160k", "-ar", "48000", "-shortest", "-movflags", "+faststart", a.out]
    run(cmd)
    d = dur(a.out); print(f"OK {a.out} duración {d:.2f}s")
    if not 60 <= d <= 95: print("ERROR: duración fuera de 60-95 s", file=sys.stderr); sys.exit(2)

if __name__ == "__main__":
    main()
