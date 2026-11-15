# RELEVO_EN — 2026-11-09_dato-robot-ensambla-orbita (English version)

- Fecha: 2026-11-15 (America/Mexico_City).
- Fuente: release `semana-2026-11-15_21-en`, carpeta `2026-11-09_dato-robot-ensambla-orbita`
  (frames limpios, storyboard.json, guion.txt narrado de verdad, capsula.srt ES).
- Título EN: "A robot assembles a structure in orbit" | hook: "A robot built in orbit".
- Traducción: guion completo ES → EN desde el guion narrado (185 palabras EN).
  Cierre: "That was Datos y ociosidades." Fuentes y DOIs sin cambios (3 fuentes).
  Correccion fonetica: escena 7 dice "CAP-ton" (no "Kapton": Kokoro am_adam decia "captain", verificado por transcripcion; el subtitulo muestra "Kapton"). Loudness: el primer montaje quedo en -15.59 LUFS (0.09 fuera del gate) por el trim de TP a 0.0 dB; correccion +1.0 dB -> -14.61 LUFS, TP 0.84 dB (dentro del margen de overshoot AAC <=+1.0 dB del pipeline). La cita SRC-003 de NASA conserva "(pin aproximado de Vandenberg)" textual del storyboard en espanol.
- Voz: Kokoro am_adam (en-us), speed 0.878 calibrada (68.3 s @1.0 → 74.0 s @0.878;
  necesaria 74.7 s = target 88 − cortinilla 13 − lead 0.3).
- Montaje: ffmpeg, 1080×1920 30 fps, mismos frames, título EN en caja amarilla +
  subrayado rojo (escena 1), on_screen_text EN por escena (2–9), subtítulos EN
  (DejaVu Sans 72 bold, Outline 6, baseline 1300 px), cortinilla "Sources" 13 s
  con firma "Datos y ociosidades · @datosyociosidadesEN", cama musical sintetizada
  (arpegio suave), loudness -14.61 LUFS, TP 0.84 dB (tras correccion +1.0 dB).
- Duración real: 87.30s (target 88 s). Tamaño: 7.1 MB.
- QA: PASA (ver qa.txt). Verificado en cuadros: título t=1 s, on-screen +
  subtítulo t=45 s, cortinilla t=84 s. Transcripción faster-whisper base:
  ratio 0.968 (187 palabras guion / 187 oidas); unicas diferencias: "Caltech's"->"Coltex" (artefacto ASR), "CAP-ton"->"CAP-tun" (vocal reducida; en frase aislada se oye "CAP-ton" exacto), "eleven"->"11" (digitos), "Datos"->"Dato's", "ociosidades"->"Oceosidades" (marca en espanol, esperado).
- Archivos: `capsula_en.mp4` (local, 7.1 MB), `capsula_en.srt`,
  `storyboard_en.json`, `subs_en.ass`, `qa.txt`, este archivo.
- NO programado en YouTube/TikTok/Facebook: lo programa el agente principal.
- No se tocó el paquete en español ni su capsula.mp4.
