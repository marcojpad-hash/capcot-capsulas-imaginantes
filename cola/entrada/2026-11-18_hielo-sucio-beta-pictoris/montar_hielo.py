"""Relevo de Pecas: monta la cápsula Hielo sucio Beta Pictoris (dato del día 18-nov-2026) con Kokoro (voz local) + faster-whisper
para los tiempos de subtítulos, reutilizando montar_capsula.py como motor de video.

Espejo de montar_capsula.main(), con dos sustituciones:
  - edge-tts (inaccesible: websocket bloqueado por el proxy de salida) -> Kokoro ONNX
    em_santa, modelo local ~/workspace/capcot-entregas/_models/kokoro-v1.0.onnx.
  - WordBoundary de edge-tts -> faster-whisper (base, CPU int8) con word_timestamps,
    alineado por orden con los tokens del guion; los números se expanden a palabras
    (1943 -> mil novecientos cuarenta y tres) antes de alinear.
El resto (escena_video, cortinilla, cama_sonora, licencias, SRT/ASS, mezcla final,
loudnorm -14, CRF 20) es idéntico al pipeline oficial.
Uso: python montar_hielo.py <storyboard.json> -o <capsula.mp4>
"""
import json
import os
import re
import sys
import tempfile

PKG = os.path.dirname(os.path.abspath(__file__))  # se ejecuta desde el paquete
SCRIPTS = "/home/hatch/workspace/capcot-entregas/_repo/scripts"
sys.path.insert(0, SCRIPTS)
import montar_capsula as mc  # noqa: E402

KOKORO_MODEL = "/home/hatch/workspace/capcot-entregas/_models/kokoro-v1.0.onnx"
KOKORO_VOICES = "/home/hatch/workspace/capcot-entregas/_models/voices-v1.0.bin"


# ---- números a palabras (español) para alinear la narración hablada ----
_U = ["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
_D10 = ["diez", "once", "doce", "trece", "catorce", "quince", "dieciséis",
        "diecisiete", "dieciocho", "diecinueve"]
_D = ["", "", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta",
      "setenta", "ochenta", "noventa"]
_C = ["", "ciento", "doscientos", "trescientos", "cuatrocientos", "quinientos",
      "seiscientos", "setecientos", "ochocientos", "novecientos"]


def num_es(n):
    if n < 10:
        return _U[n]
    if n < 20:
        return _D10[n - 10]
    if n < 30:
        return "veinte" if n == 20 else "veinti" + _U[n - 20]
    if n < 100:
        d, u = divmod(n, 10)
        return _D[d] if u == 0 else _D[d] + " y " + _U[u]
    if n < 1000:
        if n == 100:
            return "cien"
        c, r = divmod(n, 100)
        return _C[c] + ("" if r == 0 else " " + num_es(r))
    if n < 10000:
        m, r = divmod(n, 1000)
        miles = "mil" if m == 1 else _U[m] + " mil"
        return miles + ("" if r == 0 else " " + num_es(r))
    raise ValueError(n)


def expandir_tokens(toks):
    """Devuelve la lista de palabras habladas: cada token del guion aporta una
    palabra, salvo los números, que aportan su expansión (1943 -> 4 palabras).
    También devuelve, por cada token, el rango [i0, i1) en la lista expandida."""
    habladas, rangos = [], []
    for tok in toks:
        core = tok.strip(".,;:!?¿¡…\"'()")
        if core.isdigit():
            exp = num_es(int(core)).split()
            rangos.append((len(habladas), len(habladas) + len(exp)))
            habladas.extend(exp)
        else:
            rangos.append((len(habladas), len(habladas) + 1))
            habladas.append(tok)
    return habladas, rangos


def whisper_words(wav16k):
    """Tiempos por palabra con faster-whisper (entrada como array numpy 16 kHz,
    porque el decodificador av de este venv no acepta archivos directamente)."""
    import soundfile as sf
    from faster_whisper import WhisperModel
    samples, sr = sf.read(wav16k, dtype="float32")
    assert sr == 16000, sr
    model = whisper_words._model
    segs, _ = model.transcribe(samples, language="es", word_timestamps=True)
    out = []
    for s in segs:
        for w in (s.words or []):
            out.append((float(w.start), float(w.end), w.word.strip()))
    return out


whisper_words._model = None


import difflib
import re
import unicodedata


def _norm1(w):
    """Una palabra normalizada para comparar whisper con guion: minúsculas,
    sin acentos ni puntuación."""
    w = unicodedata.normalize("NFKD", w.lower())
    w = "".join(c for c in w if not unicodedata.combining(c))
    return re.sub(r"[^\w]", "", w)


def alinear(toks, wwords, adur):
    """Alinea las palabras de whisper (por orden) con los tokens del guion.
    Whisper no siempre devuelve la misma segmentación: los números hablados
    vuelven como dígitos ("1943" = 1 palabra en vez de 5), "tu disfraz" se
    funde en una ("Tudisfraz") y los nombres propios se parten ("Gjermundbu"
    -> "Heger Mundo"). Por eso se alinea con difflib sobre las palabras
    normalizadas: los bloques iguales toman el tiempo real de whisper y las
    regiones desalineadas reparten su tramo entre las palabras que cubren.
    Devuelve [(inicio, fin, token)] con los tiempos de whisper; si el
    alineado cubre menos del 60% de las palabras, reparte de forma
    proporcional sobre adur."""
    habladas, rangos = expandir_tokens(toks)
    wn = [_norm1(w) for _, _, w in wwords]
    hn = [_norm1(w) for w in habladas]
    sm = difflib.SequenceMatcher(a=wn, b=hn, autojunk=False)
    times = [None] * len(habladas)
    iguales = 0
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            iguales += i2 - i1
            for k in range(i2 - i1):
                times[j1 + k] = (wwords[i1 + k][0], wwords[i1 + k][1])
        else:
            if i2 > i1:
                t0, t1 = wwords[i1][0], wwords[i2 - 1][1]
            else:
                t0 = wwords[i1 - 1][1] if i1 > 0 else 0.0
                t1 = wwords[i1][0] if i1 < len(wwords) else adur
            n = j2 - j1
            for k in range(n):
                times[j1 + k] = (t0 + (t1 - t0) * k / n, t0 + (t1 - t0) * (k + 1) / n)
    if iguales < 0.6 * len(habladas) or any(x is None for x in times):
        print(f"AVISO: alineado débil ({iguales}/{len(habladas)}) -> tiempos proporcionales",
              file=sys.stderr)
        n = len(toks)
        return [(i * adur / n, (i + 1) * adur / n, tok) for i, tok in enumerate(toks)], "proporcional"
    words = []
    for tok, (i0, i1) in zip(toks, rangos):
        s = times[i0][0]
        e = times[i1 - 1][1]
        words.append((s, e, tok))
    return words, f"whisper+alineado ({iguales}/{len(habladas)})"


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("storyboard")
    ap.add_argument("-o", "--out", required=True)
    a = ap.parse_args()
    sb = json.load(open(a.storyboard, encoding="utf-8"))
    # relevo: normalizar sfx/ambiente a nombres válidos del motor (cama_sonora.SINTETICOS)
    SFX_MAP = {"viento": "viento_fuerte", "olas": "oceano", "reloj": "silencio",
               "pluma": "silencio", "campanas": "silencio"}
    for _sc in sb["scenes"]:
        if _sc.get("sfx"):
            _sc["sfx"] = [SFX_MAP.get(x, x) for x in _sc["sfx"]]
        if _sc.get("ambiente"):
            _sc["ambiente"] = SFX_MAP.get(_sc["ambiente"], _sc["ambiente"])
    base = os.path.dirname(os.path.abspath(a.storyboard))
    v = sb["voice"]
    tempfile.tempdir = os.path.join(base, "_tmp")
    os.makedirs(tempfile.tempdir, exist_ok=True)
    tmp = tempfile.mkdtemp(prefix="capcot_hielo_")
    continuo = v.get("modo_pausas", "continuo") == "continuo"
    pad = float(v.get("pad_seconds", 0.3))
    speed = 0.93  # relevo: a 1.0 la narración total es ~49 s y el video queda <60 s
    voice_id = "em_santa"  # relevo: storyboard pide es-MX-JorgeNeural (edge-tts), bloqueado por proxy; Kokoro local em_santa

    from kokoro_onnx import Kokoro
    import soundfile as sf
    from faster_whisper import WhisperModel
    kok = Kokoro(KOKORO_MODEL, KOKORO_VOICES)
    whisper_words._model = WhisperModel("base", device="cpu", compute_type="int8")

    clips, audio_parts, all_words, t, durs = [], [], [], 0.0, []
    for i, sc in enumerate(sb["scenes"]):
        narration = sc["narration"]
        toks = narration.split()
        raw = os.path.join(tmp, f"{sc['id']}_raw.wav")
        samples, sr = kok.create(narration, voice=voice_id, speed=speed, lang="es")
        sf.write(raw, samples, sr)
        adur = len(samples) / sr
        # whisper necesita 16 kHz mono
        w16 = os.path.join(tmp, f"{sc['id']}_16k.wav")
        mc.run(["ffmpeg", "-y", "-v", "error", "-i", raw, "-ar", "16000", "-ac", "1", w16])
        wwords = whisper_words(w16)
        words, modo = alinear(toks, wwords, adur)
        if continuo and words:
            sdur = adur + 0.25 + pad
        elif continuo:
            sdur = float(sc.get("duration_seconds", 3))
        else:
            sdur = max(float(sc["duration_seconds"]), adur + pad)
        all_words += [(s + t + 0.25, e + t + 0.25, w) for s, e, w in words]
        wav = os.path.join(tmp, f"{sc['id']}.wav")
        mc.run(["ffmpeg", "-y", "-i", raw, "-af", "adelay=250,apad", "-t", f"{sdur:.3f}",
                "-ar", "48000", "-ac", "2", wav])
        audio_parts.append(wav)
        mp4 = os.path.join(tmp, f"{sc['id']}.mp4")
        titulo = sb.get("titulo") or sb["scenes"][0].get("on_screen_text", "")
        mc.escena_video(os.path.join(base, sc["asset_filename"]), sdur, mp4, i,
                        titulo if i == 0 else sc.get("on_screen_text", ""),
                        float(sb.get("export", {}).get("plano_seconds", 2.5)),
                        gancho=(i == 0), capa=sc.get("capa"),
                        titulo_estilo=sb.get("titulo_estilo"))
        clips.append(mp4)
        ps = float(sb.get("export", {}).get("plano_seconds", 2.5))
        n = mc.n_planos(sdur, ps, sc.get("capa"))
        sfx = sc.get("sfx") or [sc.get("ambiente") or "olas"]
        durs += [(sfx[min(k, len(sfx) - 1)], sdur / n) for k in range(n)]
        print(f"{sc['id']}: voz {adur:.1f}s, escena {sdur:.1f}s, "
              f"palabras whisper {len(wwords)}/{len(toks)} tokens ({modo})")
        t += sdur

    cd = float(sb["cortinilla_fuentes"].get("duration_seconds", 5))
    cpng = os.path.join(tmp, "cortinilla.png")
    mc.cortinilla(sb, cpng)
    cmp4 = os.path.join(tmp, "cortinilla.mp4")
    mc.run(["ffmpeg", "-y", "-loop", "1", "-i", cpng, "-t", f"{cd}", "-r", str(mc.FPS),
            "-vf", "format=yuv420p", "-c:v", "libx264", "-preset", "veryfast", cmp4])
    clips.append(cmp4)
    cwav = os.path.join(tmp, "cortinilla.wav")
    mc.run(["ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
            "-t", f"{cd}", cwav])
    audio_parts.append(cwav)
    with open(os.path.join(tmp, "v.txt"), "w") as f:
        f.writelines(f"file '{c}'\n" for c in clips)
    with open(os.path.join(tmp, "a.txt"), "w") as f:
        f.writelines(f"file '{c}'\n" for c in audio_parts)
    vcat, acat = os.path.join(tmp, "v.mp4"), os.path.join(tmp, "voz.wav")
    mc.run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", os.path.join(tmp, "v.txt"),
            "-c", "copy", vcat])
    mc.run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", os.path.join(tmp, "a.txt"),
            "-c", "copy", acat])
    srt = os.path.splitext(a.out)[0] + ".srt"
    open(srt, "w", encoding="utf-8").write(
        mc.srt_from_words(all_words, sb["export"].get("subtitle_max_words", 3)))
    ass = os.path.splitext(a.out)[0] + ".ass"
    mc.ass_from_srt(open(srt, encoding="utf-8").read(), ass)
    vf = f"ass={ass}"
    durs.append(("silencio", cd))
    camas = mc.cama_sonora(sb.get("audio", {}), base, mc.dur(acat), tmp, durs)
    cmd = ["ffmpeg", "-y", "-i", vcat, "-i", acat]
    if camas:
        for c in camas:
            cmd += ["-i", c]
        n = len(camas)
        ins = "".join(f"[{k + 2}:a]" for k in range(n))
        fc = (f"[1:a]loudnorm=I=-16:TP=-2,asplit=2[v][sc];{ins}amix=inputs={n}:normalize=0[bed];"
              f"[bed][sc]sidechaincompress=threshold=0.015:ratio=8:attack=15:release=350:makeup=1[duck];"
              f"[v][duck]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5[aout];[0:v]{vf}[vout]")
        cmd += ["-filter_complex", fc, "-map", "[vout]", "-map", "[aout]"]
    else:
        cmd += ["-vf", vf, "-af", "loudnorm=I=-14:TP=-1.5", "-map", "0:v", "-map", "1:a"]
    cmd += ["-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
            "-r", str(mc.FPS), "-c:a", "aac", "-b:a", "160k", "-ar", "48000",
            "-shortest", "-movflags", "+faststart", a.out]
    mc.run(cmd)
    d = mc.dur(a.out)
    print(f"OK {a.out} duración {d:.2f}s")
    lic_path = os.path.join(os.path.dirname(os.path.abspath(a.out)), "licencias.json")
    mc.licencias(sb, lic_path)
    # la voz NO es Edge TTS en este relevo: corregir el registro
    lic = json.load(open(lic_path, encoding="utf-8"))
    lic["voz"] = {"motor": "Kokoro ONNX (local, modelo kokoro-v1.0.onnx)",
                  "voz": voice_id,
                  "nota": "voz sintética; no imita a una persona real"}
    json.dump(lic, open(lic_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    if not 60 <= d <= 120:
        print("ERROR: duración fuera de 60-120 s", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
