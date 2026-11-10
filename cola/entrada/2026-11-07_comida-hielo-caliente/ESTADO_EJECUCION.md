# ESTADO_EJECUCION — 2026-11-07_comida-hielo-caliente

Project: 2026-11-07_comida-hielo-caliente
Serie: Datos y ociosidades
Estructura: mito_vs_dato
Estilo: linea_fina
Voz: es-MX-JorgeNeural +7%, pitch −2 Hz
Título (pantalla): ¿Caliente se congela antes?
Título YT: ¿El agua caliente se congela antes? #Shorts

## Hecho (2026-11-10, Imaginantes)

- Storyboard ampliado de 6 a 9 escenas sin afirmaciones nuevas (solo SRC-001 y SRC-002).
- 9 frames PNG 1080×1920, estilo linea_fina, sin texto en la imagen; encuadres: general, cenital, medio, macro, contrapicado, detalle.
- Montaje oficial con `scripts/montar_capsula.py` (JorgeNeural, plano_seconds=5, cama `pulso`).
- MP4: `salidas/2026-11-07_comida-hielo-caliente/capsula.mp4` y copia en `/workspace/entregas/2026-11-11_mpemba/capsula.mp4`
- Portada: `portada.jpg` extraída a 0.5 s (título en caja crema y subrayado rojo).
- QA oficial `scripts/qa_capsula.py`: PASA (duración 89.83 s, 1080×1920, −14.4 LUFS, 217 palabras, cierre scene_009 13.2 s).
- SRC-002: DOI verificado 2026-11-10 (10.1088/0031-9120/4/3/312).
- Slot programado (autorizado por Mj, cápsula extra): **2026-11-11 13:30 hora CDMX (America/Mexico_City) = 2026-11-11T19:30:00Z**.

## Pendiente

- YouTube PROGRAMADO: videoId `HSgrnejAcaI` — https://youtube.com/shorts/HSgrnejAcaI — private, publishAt 2026-11-11T19:30:00Z (13:30 hora CDMX). Miniatura: thumbnails.set OK (portada a 0.5 s, maxres presente). Confirmado por videos.list. containsSyntheticMedia=false (ilustración no realista, mismo criterio que cápsulas anteriores del pipeline).
- TikTok y Facebook: no hay vía automática de programación usada en este repo (TT del script queda en buzón de borradores y está desactivado). Programar a mano a la misma hora, eligiendo la portada como cover. Archivos y caption en `/workspace/entregas/2026-11-11_mpemba/`.

## Qué NO se hizo

- No se borró ni movió material publicado previo.
- No se subieron binarios pesados al repo (mp4/png/jpg gitignored).
