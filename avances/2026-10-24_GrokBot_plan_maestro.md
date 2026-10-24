# 2026-10-24 — Grok Bot — Plan maestro automático + prototipo probado

Commit base: 05dec303974cb533f1cee7f534956c12334efb58. Hashes = `git hash-object` (blob SHA-1).

## Antes → ahora (por archivo)
- docs/PLAN_MAESTRO_AUTOMATICO.md — no existía → fuente única de verdad: 14 conflictos resueltos (16:9→9:16; 1–3 min→60–90 s; universitario→público general; clicks Flow/Kling→frames por API + Ken Burns; TTS edge-tts/Chirp; subtítulos por WordBoundary; compuertas automáticas; publicación YT automática / TikTok borrador; métricas semanales con una variable). SHA después: fd93e5aa65c2c8a1835c518f508aaa998fdb39d9
- templates/storyboard_vertical.template.json — no existía → plantilla 9:16 con arc, trend_source, voice, cortinilla_fuentes, publicacion. SHA: 99e7ef0164ed4d43243767932154cf6f8116cd14. (La plantilla 16:9 de ChatGPT se conserva sin cambios: 776b0896240a0942872eecab2c7621832007f26a).
- scripts/validar_storyboard.py — no existía → validador stdlib (arco, 60–90 s, 9:16, fuentes, DOI vía Crossref). SHA: 0ad161ff9b24642a73c4e4c21d3d0efa075444de
- scripts/montar_capsula.py — no existía → TTS edge-tts + SRT por palabra + Ken Burns + cortinilla + loudnorm → MP4 1080×1920. SHA: 4c1d7c6cbdae40ab931998feb735e6e57a0d943c
- proyectos/demo-001/storyboard.json, generar_placeholders.py — nuevos (Tunguska 1908). SHA: 96505111ce6640abf699aabddcb0aa950d8304a4, a8a643ea2b4165eaee61e54ffe9ba0b530b2c3ad
- .gitignore — no existía → excluye mp4/wav/mp3/srt/frames. SHA: aecef56846bf89d61d1895371bbc22d385c04aa1
- README.md — antes e42914d7e1a45fe7fe5d4269ee8caa3b6e15c1c8 → después de2972654fd1c92a77b33d26898ce3377cdcceec (descripción 9:16 y enlace al plan maestro).
- Ningún archivo de otros modelos borrado. salidas/ (de otro agente) no se tocó.

## Pruebas: 4 passed, 0 skipped, 0 failed
1. validar_storyboard.py --check-doi sobre demo-001: OK (3 DOI resuelven en Crossref).
2. Compuerta de duración: primer render 91.67 s → rechazado (exit 2) ✔; ajustado rate +4 % → 84.37 s.
3. ffprobe: h264 1080×1920 30/1 + aac, 84.366667 s.
4. Loudness integrada −14.1 LUFS; inspección visual de frames: subtítulos en zona segura, cortinilla legible.
Render: /workspace/imaginantes/demo-001.mp4 (no versionado).
