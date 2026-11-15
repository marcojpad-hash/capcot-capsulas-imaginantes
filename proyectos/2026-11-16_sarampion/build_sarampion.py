#!/usr/bin/env python3
"""Montaje relevo Sarampión (CAPCOT, dato del día lun 16-nov-2026 07:00 CST).

Reutiliza las funciones oficiales de montar_capsula.py (zoompan, cortinilla,
subtítulos ASS estilo oficial, loudnorm -14 LUFS) con la narración Kokoro
ef_dora pregrabada (edge-tts está bloqueado en la VM).

Voz: Kokoro ef_dora (narradora_es), speed 0.73 (133.4 ppm, rango 120-140
para público 65+; a 0.9 daba 177 ppm, demasiado rápido).
Narración medida: 85.0 s; escenas = voz + 0.25 lead + 0.3 pad; total
esperado 94.3 s (target 94 en storyboard.json).
Cama: viento + arpegio sintetizados con cama_sonora.py.
Planos: 4.0 s (movimientos suaves, modo pausado).
"""
import json, os, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import montar_capsula as mc
import cama_sonora as cs

SB = json.load(open(os.path.join(HERE, "storyboard.json"), encoding="utf-8"))
AUDIO = os.path.join(HERE, "audio")
FRAMES = os.path.join(HERE, "frames")
OUT = os.path.join(HERE, "capsula.mp4")
PLANO_S = 4.0
PAD = 0.3
LEAD = 0.25

def dur(path):
    return float(subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", path]).decode().strip())

def main():
    tmp = tempfile.mkdtemp(prefix="apagon_build_")
    clips, audio_parts, all_words, t, durs = [], [], [], 0.0, []
    for i, sc in enumerate(SB["scenes"]):
        wav_in = os.path.join(AUDIO, f"escena_{i+1:02d}.wav")
        adur = dur(wav_in)
        sdur = adur + LEAD + PAD
        toks = sc["narration"].split()
        step = adur / max(len(toks), 1)
        words = [(t + LEAD + k * step, t + LEAD + (k + 1) * step, w)
                 for k, w in enumerate(toks)]
        all_words += words
        wav = os.path.join(tmp, f"{sc['id']}.wav")
        mc.run(["ffmpeg", "-y", "-i", wav_in, "-af",
                f"adelay={int(LEAD*1000)}:all=1,apad", "-t", f"{sdur:.3f}",
                "-ar", "48000", "-ac", "2", wav])
        audio_parts.append(wav)
        mp4 = os.path.join(tmp, f"{sc['id']}.mp4")
        titulo = SB.get("titulo") or SB["scenes"][0].get("on_screen_text", "")
        mc.escena_video(os.path.join(FRAMES, f"scene_{i+1:03d}.jpg"), sdur, mp4, i,
                        titulo if i == 0 else sc.get("on_screen_text", ""),
                        PLANO_S, gancho=(i == 0), capa=sc.get("capa"),
                        titulo_estilo=SB.get("titulo_estilo"))
        ps = PLANO_S
        n = mc.n_planos(sdur, ps, sc.get("capa"))
        sfx = sc.get("sfx") or [sc.get("ambiente") or "viento"]
        durs += [(sfx[min(k, len(sfx) - 1)], sdur / n) for k in range(n)]
        print(f"{sc['id']}: voz {adur:.1f}s, escena {sdur:.1f}s", flush=True)
        clips.append(mp4)
        t += sdur
    cd = float(SB["cortinilla_fuentes"].get("duration_seconds", 6))
    cpng = os.path.join(tmp, "cortinilla.png")
    mc.cortinilla(SB, cpng)
    cmp4 = os.path.join(tmp, "cortinilla.mp4")
    mc.run(["ffmpeg", "-y", "-loop", "1", "-i", cpng, "-t", f"{cd}", "-r", "30",
            "-vf", "format=yuv420p", "-c:v", "libx264", "-preset", "veryfast", cmp4])
    clips.append(cmp4)
    cwav = os.path.join(tmp, "cortinilla.wav")
    mc.run(["ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
            "-t", f"{cd}", cwav])
    audio_parts.append(cwav)
    total = t + cd
    print(f"total escenas {t:.2f}s + cortinilla {cd}s = {total:.2f}s "
          f"(target {SB['target_duration_seconds']}s)", flush=True)
    with open(os.path.join(tmp, "v.txt"), "w") as f:
        f.writelines(f"file '{c}'\n" for c in clips)
    with open(os.path.join(tmp, "a.txt"), "w") as f:
        f.writelines(f"file '{c}'\n" for c in audio_parts)
    vcat, acat = os.path.join(tmp, "v.mp4"), os.path.join(tmp, "voz.wav")
    mc.run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i",
            os.path.join(tmp, "v.txt"), "-c", "copy", vcat])
    mc.run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i",
            os.path.join(tmp, "a.txt"), "-c", "copy", acat])
    srt = os.path.join(HERE, "capsula.srt")
    open(srt, "w", encoding="utf-8").write(
        mc.srt_from_words(all_words, SB["export"].get("subtitle_max_words", 3)))
    ass = os.path.join(HERE, "capsula.ass")
    mc.ass_from_srt(open(srt, encoding="utf-8").read(), ass)
    aud = SB.get("audio", {})
    amb_raw = os.path.join(tmp, "amb_raw.wav")
    cs.guardar(cs.ambiente(aud.get("ambiente", "viento"), total), amb_raw)
    amb = os.path.join(tmp, "amb.wav")
    mc.run(["ffmpeg", "-y", "-i", amb_raw, "-af",
            f"loudnorm=I={aud.get('ambiente_lufs', -28)}:TP=-3",
            "-ar", "48000", amb])
    mus_raw = os.path.join(tmp, "mus_raw.wav")
    cs.guardar(cs.musica(total, int(aud.get("music_bpm", 92)),
                         aud.get("cama_musical") or "pizzicato"), mus_raw)
    mus = os.path.join(tmp, "mus.wav")
    mc.run(["ffmpeg", "-y", "-i", mus_raw, "-af",
            f"loudnorm=I={aud.get('music_lufs', -27)}:TP=-3",
            "-ac", "2", "-ar", "48000", mus])
    vf = f"ass={ass}"
    fc = (f"[1:a]loudnorm=I=-16:TP=-2,asplit=2[v][sc];"
          f"[2:a][3:a]amix=inputs=2:normalize=0[bed];"
          f"[bed][sc]sidechaincompress=threshold=0.015:ratio=8:attack=15:release=350:makeup=1[duck];"
          f"[v][duck]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5[aout];[0:v]{vf}[vout]")
    cmd = ["ffmpeg", "-y", "-i", vcat, "-i", acat, "-i", amb, "-i", mus,
           "-filter_complex", fc, "-map", "[vout]", "-map", "[aout]",
           "-c:v", "libx264", "-preset", "medium", "-crf", "20",
           "-pix_fmt", "yuv420p", "-r", "30", "-c:a", "aac", "-b:a", "160k",
           "-ar", "48000", "-shortest", "-movflags", "+faststart", OUT]
    mc.run(cmd)
    print(f"OK {OUT} duración {dur(OUT):.2f}s", flush=True)

if __name__ == "__main__":
    main()
