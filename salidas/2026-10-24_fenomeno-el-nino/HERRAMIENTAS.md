# Herramientas y costo
- Tema: Google Trends RSS MX (24-oct-2026) → fenómeno El Niño
- Guion: redactado por agente (sin API LLM); fuentes verificadas vía Crossref + climate.gov
- Imágenes: GenerateImage (Grok Bot, incluido) 576x1024 → escalado 1080x1920; estilo linograbado
- Voz: edge-tts es-MX-JorgeNeural (gratis); SRT por WordBoundary
- Montaje: scripts/montar_capsula.py (ffmpeg zoompan, subs abajo ≤3 palabras, loudnorm −14 LUFS)
- QA: scripts/qa_capsula.py → 11/11 PASA
- Costo: US$0

## v2 (feedback Mj, 2026-10-24)
- Guion reescrito (215 palabras), estructura Imaginantes; hechos solo de SRC-001..003 (climate.gov re-leído hoy).
- Voz es-MX-JorgeNeural (misma del demo v1), rate +8 %, pitch −2 Hz; silencio de edge-tts recortado por frase; pausas 0.3–0.6 s.
- Ambiente: océano (ruido marrón con vaivén de ~9 s) + viento (ruido rosa en banda con ráfagas), sintetizados con ffmpeg anoisesrc.
- Música: pad sintético en La menor (Am–F–C–G, aevalsrc + eco), generado por montar_capsula.py.
- Licencia: todo el audio de fondo es generado por el pipeline (obra propia, sin derechos de terceros); no se usó audio externo.
- Mezcla: voz −16 LUFS, camas −38/−40 LUFS (22–24 dB abajo) + sidechaincompress (ratio 6) → master −14 LUFS.
  Medido: tramo con voz −14.4 LUFS; cama sola (cortinilla) −23.9 LUFS.
- Resultado: capsula_v2.mp4, 87.8 s, QA 11/11.
