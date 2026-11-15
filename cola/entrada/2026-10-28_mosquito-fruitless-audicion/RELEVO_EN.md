# RELEVO_EN — 2026-10-28_mosquito-fruitless-audicion (English version)

- Fecha: 2026-11-14 (America/Mexico_City).
- Fuente: cápsula en español `~/workspace/capcot-entregas/2026-11-18_mosquito/`
  (capsula.mp4 87.30 s, 8 frames, storyboard.json, capsula.srt ES).
- Título EN: "The gene that tunes the male mosquito's hearing" | hook: "The mosquito that listens".
- Traducción: guion completo ES → EN desde el storyboard narrado (192 palabras EN).
  Cierre: "That was Datos y ociosidades." Fuentes y DOI sin cambios (3 fuentes,
  DOI 10.1371/journal.pbio.3004041). Números hablados escritos en palabras
  (four hundred fifty / seven hundred fifty / October twenty-seventh / one sixth).
- Pronunciación (verificado en frase aislada ANTES de narrar):
  "fruitless" se oye correcto; "Johnston's organ" se oye correcto;
  "Aedes aegypti" se oye "ee-deez ee-jip-tee" (variante válida) y el ASR lo
  transcribe "eats Egypti" (artefacto de nombre propio, como Palumbi→Palembeye
  en corales). Respelling "AY-deez AY-jip-tee" probado aislado y salió PEOR
  ("AYD's AYGIPT"), así que NO se aplica corrección: narración y subtítulo
  quedan "Aedes aegypti".
- Voz: Kokoro am_adam (en-us), speed 0.817 calibrada (pasadas: 1.0 → ~82 s,
  0.850 → 75.7 s, 0.817 → 78.9 s; necesaria 78.7 s = target 85 − cortinilla 6 − lead 0.3).
- Montaje: mismo pipeline build_en.py de las 6 (ffmpeg, 1080×1920 30 fps,
  mismos 8 frames del español, título EN en caja amarilla + subrayado rojo
  en escena 1, on_screen_text EN por escena 2–8, subtítulos EN DejaVu Sans 72
  bold Outline 6, cortinilla "Sources" 6 s con firma
  "Datos y ociosidades · @datosyociosidadesEN", cama sintetizada arpegio,
  loudness −14.95 LUFS, TP 0.0 dB tras trim).
  Nota: como en las otras 6 versiones EN, las capas informativas del español
  (mapa Nagoya, gráfico 450/750 Hz, dato 1/6) no se re-renderizan: el pipeline
  EN usa solo on_screen_text por escena.
- Duración real: 85.25 s (target 85 s, diff +0.25 s). Tamaño: 7.8 MB.
- QA: PASA (ver qa.txt). Verificado en cuadros: título t=1 s, on-screen +
  subtítulo t=40 s, cortinilla t=84 s. Transcripción faster-whisper base:
  ratio 0.921; únicas diferencias: Aedes aegypti (nombre propio),
  posesivos female's/male's, normalización de números del ASR y la marca
  en español (todo en las clases aceptadas).
- Archivos: `capsula_en.mp4` (local, 7.8 MB), `capsula_en.srt`,
  `storyboard_en.json`, `subs_en.ass`, `qa.txt`, este archivo,
  `build_en_mosquito.py` (adaptación de build_en.py con frames del español).
- NO programado en YouTube/TikTok/Facebook: lo programa el agente principal.
- No se tocó el paquete en español ni su capsula.mp4.
