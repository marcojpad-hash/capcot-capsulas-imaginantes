#!/usr/bin/env python3
"""Monta una cápsula vertical 9:16 desde un storyboard con frames PNG locales.
Uso: python3 montar_capsula.py proyectos/x/storyboard.json -o salida.mp4
Requiere: ffmpeg/ffprobe, edge-tts (pip), Pillow.
Pasos: TTS por escena (edge-tts, WordBoundary) -> SRT por palabras -> planos ~2.5 s con cortes secos
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
# Regla de pausas (feedback Mj 2026-10-24 10:53): pausa ligera entre frases 0.25–0.35 s, sin huecos largos.
PAUSAS = {".": 0.32, "?": 0.35, "!": 0.35, "…": 0.35, ":": 0.25, ";": 0.25}

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

# Subtítulos ASS con PlayRes = resolución real (con SRT, libass usa PlayResY=288 y un MarginV grande
# empujaba el texto fuera de cuadro: bug de v5, se veían solo palabras sueltas).
SUB_Y_BASE = 1300  # línea base inferior del subtítulo (px): debajo del texto clave (12-35 %), arriba del 20 % inferior
def ass_from_srt(srt_txt, out_ass):
    head = ("[Script Info]\nScriptType: v4.00+\nPlayResX: 1080\nPlayResY: 1920\nWrapStyle: 0\nScaledBorderAndShadow: yes\n\n"
            "[V4+ Styles]\nFormat: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, "
            "Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\n"
            f"Style: Sub,DejaVu Sans,72,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,6,2,2,90,170,{1920-SUB_Y_BASE},1\n\n"
            "[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n")
    ev = []
    for b in srt_txt.strip().split("\n\n"):
        l = b.split("\n"); a, z = l[1].split(" --> ")
        f = lambda x: (lambda h, m, r: f"{int(h)}:{m}:{r.replace(',', '.')[:-1]}")(*x.split(":"))
        ev.append(f"Dialogue: 0,{f(a)},{f(z)},Sub,,0,0,0,,{' '.join(l[2:])}")
    open(out_ass, "w", encoding="utf-8").write(head + "\n".join(ev) + "\n")

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

def cama_sonora(aud, base, total, tmp, durs=None):
    """Plantilla base (feedback Mj 10:55): ambiente POR ESCENA (campo scenes[].ambiente) + música con
    pulso suave sintetizada (scripts/cama_sonora.py). Niveles: ambiente -30 LUFS, música -27 LUFS,
    voz -16 LUFS; la cama se agacha con sidechain cuando habla la voz.
    Compatibles: audio.ambiente global (oceano|viento|archivo) y music_asset=<archivo CC0>."""
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import cama_sonora as cs
    out = []
    if durs:
        dst = os.path.join(tmp, "amb.wav"); cs.guardar(cs.pista_sfx(durs, total, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "sfx")), dst)
        n = os.path.join(tmp, "amb_n.wav")
        run(["ffmpeg", "-y", "-i", dst, "-af", f"loudnorm=I={aud.get('ambiente_lufs', -26)}:TP=-3", "-ar", "48000", n]); out.append(n)
    m = aud.get("music_asset", "sintetico:pulso")
    if m:
        dst = os.path.join(tmp, "musica_raw.wav")
        if m.startswith("sintetico"): cs.guardar(cs.musica(total, int(aud.get("music_bpm", 92)), aud.get("cama_musical") or (m.split(":", 1)[1] if ":" in m else "pulso")), dst)
        else: run(["ffmpeg", "-y", "-stream_loop", "-1", "-i", os.path.join(base, m), "-t", f"{total:.2f}", dst])
        n = os.path.join(tmp, "musica.wav")
        run(["ffmpeg", "-y", "-i", dst, "-af", f"loudnorm=I={aud.get('music_lufs', -27)}:TP=-3", "-ac", "2", "-ar", "48000", n]); out.append(n)
    return out

# ---- Estructura visual (docs/ESTRUCTURA_VISUAL_TRENDS.md): planos de ~2.5 s con cortes secos ----
# Cada escena se parte en planos; cada plano usa un movimiento distinto sobre el mismo frame
# (zoom in, zoom out, paneo, punch-in) para que haya un cambio visual cada 2-3 s sin transiciones.
MOVS = ["zin", "pan_d", "punch", "zout", "pan_i", "punch_b"]

def texto_png(text, out_png, gancho=False, estilo=None):
    # estilo (opcional, solo gancho): storyboard["titulo_estilo"] = {"font": ruta_ttf, "size": 92,
    #   "caja_rgb": [r,g,b], "texto_rgb": [r,g,b], "subrayado_rgb": [r,g,b]} -> tipografía/subrayado por cápsula
    e = (estilo or {}) if gancho else {}
    fpath = e.get("font") if e.get("font") and os.path.exists(e.get("font")) else FONT
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    f = ImageFont.truetype(fpath, int(e.get("size", 92)) if gancho else 64); maxw = int(W * .78)
    caja = tuple(e.get("caja_rgb", (240, 200, 120))) + (235,); tcol = tuple(e.get("texto_rgb", (20, 18, 16)))
    sub = tuple(e.get("subrayado_rgb", (200, 40, 40))) + (245,)
    lines = wrap(d, text.upper() if gancho else text, f, maxw); lh = 108 if gancho else 78
    y = int(H * (.15 if gancho else .12))  # zona segura superior
    for ln in lines:
        x = int(W * .08); tw = d.textlength(ln, font=f); bx = (x - 18, y - 10, x + tw + 18, y + lh - 8)
        d.rounded_rectangle(bx, 14, fill=(0, 0, 0, 170) if not gancho else caja)
        d.text((x, y), ln, font=f, fill=tcol if gancho else (255, 255, 255)); y += lh + 6
    if gancho and lines:  # título-gancho subrayado (trazo de acento bajo la última línea)
        tw = d.textlength(lines[-1], font=f); x = int(W * .08); d.rounded_rectangle((x, y + 4, x + tw, y + 22), 8, fill=sub)
    img.save(out_png)

def _plano(png, seconds, out_mp4, mov, overlay=None, ov_hasta=None):
    fr = max(int(round(seconds * FPS)), 1)
    c = "iw/2-(iw/zoom/2)"; m = "ih/2-(ih/zoom/2)"
    z, x, y = {"zin": (f"1+0.10*on/{fr}", c, m), "zout": (f"1.10-0.10*on/{fr}", c, m),
               "pan_d": ("1.15", f"(iw-iw/zoom)*on/{fr}", m), "pan_i": ("1.15", f"(iw-iw/zoom)*(1-on/{fr})", m),
               "punch": (f"1.30+0.05*on/{fr}", c, "ih*0.38-(ih/zoom/2)"),
               "punch_b": (f"1.30+0.05*on/{fr}", c, "ih*0.62-(ih/zoom/2)")}[mov]
    base = (f"[0:v]scale={W*2}:{H*2}:force_original_aspect_ratio=increase,crop={W*2}:{H*2},"
            f"zoompan=z='{z}':x='{x}':y='{y}':d={fr}:s={W}x{H}:fps={FPS}")
    if overlay:
        en = f":enable='lt(t,{ov_hasta:.2f})'" if ov_hasta else ""
        fc = f"{base}[b];[b][1:v]overlay=0:0{en},format=yuv420p[o]"; ins = ["-loop", "1", "-i", overlay]
    else: fc = f"{base},format=yuv420p[o]"; ins = []
    run(["ffmpeg", "-y", "-loop", "1", "-i", png, *ins, "-filter_complex", fc, "-map", "[o]", "-frames:v", str(fr),
         "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-r", str(FPS), out_mp4])

def n_planos(seconds, plano_s=2.5): return max(1, round(seconds / plano_s))

def escena_video(png, seconds, out_mp4, idx, texto="", plano_s=2.5, gancho=False, capa=None, titulo_estilo=None):
    tmpd = tempfile.mkdtemp(prefix="pl_"); n = n_planos(seconds, plano_s); parts = []
    ov = None
    if texto:
        ov = os.path.join(tmpd, "t.png"); texto_png(texto, ov, gancho, titulo_estilo)
    for k in range(n):
        d = seconds / n; mp = os.path.join(tmpd, f"{k}.mp4")
        # el texto en pantalla vive en el primer plano de la escena (en el gancho, los 2 primeros)
        con_txt = ov if (k == 0 or (gancho and k == 1)) else None
        if capa and k == min(int(capa.get("plano", n - 1)), n - 1):  # capa informativa (mapa/gráfico/dato), no Ken Burns
            sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import capas_datos
            capas_datos.render_capa(capa, d, mp); parts.append(mp); continue
        _plano(png, d, mp, MOVS[(idx * 2 + k) % len(MOVS)], con_txt); parts.append(mp)
    lst = os.path.join(tmpd, "l.txt"); open(lst, "w").writelines(f"file '{p}'\n" for p in parts)
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", out_mp4])

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("storyboard"); ap.add_argument("-o", "--out", required=True)
    a = ap.parse_args()
    sb = json.load(open(a.storyboard, encoding="utf-8")); base = os.path.dirname(os.path.abspath(a.storyboard))
    v = sb["voice"]; tmp = tempfile.mkdtemp(prefix="capcot_")
    continuo = v.get("modo_pausas", "continuo") == "continuo"
    pad = float(v.get("pad_seconds", 0.35 if continuo else 0.6))
    clips, audio_parts, all_words, t, durs = [], [], [], 0.0, []
    for i, sc in enumerate(sb["scenes"]):
        mp3 = os.path.join(tmp, f"{sc['id']}.mp3")
        words = asyncio.run(tts(sc["narration"], v["voice_id"], mp3, v.get("rate", "+7%"), v.get("pitch", "-2Hz"))) if sc["narration"].strip() else []
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
        titulo = sb.get("titulo") or sb["scenes"][0].get("on_screen_text", "")
        escena_video(os.path.join(base, sc["asset_filename"]), sdur, mp4, i, titulo if i == 0 else sc.get("on_screen_text", ""),
                     float(sb.get("export", {}).get("plano_seconds", 2.5)), gancho=(i == 0), capa=sc.get("capa"),
                     titulo_estilo=sb.get("titulo_estilo")); clips.append(mp4)
        ps = float(sb.get("export", {}).get("plano_seconds", 2.5)); n = n_planos(sdur, ps)
        sfx = sc.get("sfx") or [sc.get("ambiente") or "olas"]  # lista por plano; el último se repite
        durs += [(sfx[min(k, len(sfx) - 1)], sdur / n) for k in range(n)]
        print(f"{sc['id']}: voz {adur:.1f}s, escena {sdur:.1f}s"); t += sdur
    cd = float(sb["cortinilla_fuentes"].get("duration_seconds", 5))
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
    ass = os.path.splitext(a.out)[0] + ".ass"; ass_from_srt(open(srt, encoding="utf-8").read(), ass)
    vf = f"ass={ass}"
    durs.append(("silencio", cd))  # cortinilla: solo música
    camas = cama_sonora(sb.get("audio", {}), base, dur(acat), tmp, durs)
    cmd = ["ffmpeg", "-y", "-i", vcat, "-i", acat]
    if camas:
        for c in camas: cmd += ["-i", c]
        n = len(camas); ins = "".join(f"[{k+2}:a]" for k in range(n))
        fc = (f"[1:a]loudnorm=I=-16:TP=-2,asplit=2[v][sc];{ins}amix=inputs={n}:normalize=0[bed];"
              f"[bed][sc]sidechaincompress=threshold=0.015:ratio=8:attack=15:release=350:makeup=1[duck];"
              f"[v][duck]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5[aout];[0:v]{vf}[vout]")
        cmd += ["-filter_complex", fc, "-map", "[vout]", "-map", "[aout]"]
    else:
        cmd += ["-vf", vf, "-af", "loudnorm=I=-14:TP=-1.5", "-map", "0:v", "-map", "1:a"]
    cmd += ["-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p", "-r", str(FPS),
            "-c:a", "aac", "-b:a", "160k", "-ar", "48000", "-shortest", "-movflags", "+faststart", a.out]
    run(cmd)
    d = dur(a.out); print(f"OK {a.out} duración {d:.2f}s")
    licencias(sb, os.path.join(os.path.dirname(os.path.abspath(a.out)), "licencias.json"))
    # Regla 1 anti 'en serie': duración variable por tema (60-90+ s), nunca <60; techo 120 s
    if not 60 <= d <= 120: print("ERROR: duración fuera de 60-120 s", file=sys.stderr); sys.exit(2)

def licencias(sb, path):
    """Registro de licencias por cápsula (música, SFX, imágenes, voz, mapas)."""
    R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    aud = sb.get("audio", {}); m = aud.get("music_asset", "sintetico:pulso")
    lic_sfx = {}
    lp = os.path.join(R, "assets", "sfx", "LICENCIAS.json")
    if os.path.exists(lp): lic_sfx = json.load(open(lp, encoding="utf-8"))
    usados = sorted({x for sc in sb["scenes"] for y in (sc.get("sfx") or [sc.get("ambiente") or "olas"]) for x in y.split("+")})
    if m.startswith("sintetico"):
        mus = {"cama": aud.get("cama_musical") or (m.split(":", 1)[1] if ":" in m else "pulso"), "origen": "síntesis propia (scripts/cama_sonora.py, numpy)", "licencia": "obra propia de Datos y ociosidades", "generada_por_ia": False}
    else:
        mus = {"archivo": m, "origen": aud.get("music_origen", "YouTube Audio Library (descarga manual de Mj)"), "licencia": aud.get("music_licencia", "PENDIENTE: anotar licencia/atribución"), "generada_por_ia": bool(aud.get("music_ia", False))}
    capas = [sc["capa"]["tipo"] for sc in sb["scenes"] if sc.get("capa")]
    rec = {"project_id": sb.get("project_id"), "musica": mus,
           "sfx": {k: (lic_sfx.get(k) or {"origen": "síntesis propia (cama_sonora.py)", "licencia": "obra propia"}) for k in usados},
           "imagenes": {"origen": sb.get("proveedor_imagenes", "generadas con IA (ilustración no realista)"), "estilo": sb.get("estilo_id"), "realista": bool(sb.get("parece_real", False))},
           "voz": {"motor": "Microsoft Edge TTS", "voz": sb.get("voice", {}).get("voice_id"), "nota": "voz sintética; no imita a una persona real"},
           "capas_datos": {"tipos": capas, "mapa_base": "Natural Earth 110m (dominio público)" if "mapa" in capas else None, "render": "matplotlib (propio)"},
           "fuentes_datos": [s.get("url") for s in sb.get("sources", [])]}
    json.dump(rec, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

if __name__ == "__main__":
    main()
