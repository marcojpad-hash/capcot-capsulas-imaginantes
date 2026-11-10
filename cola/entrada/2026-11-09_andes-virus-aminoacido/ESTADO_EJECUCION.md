# ESTADO_EJECUCION — 2026-11-09_andes-virus-aminoacido

Project: 2026-11-09_andes-virus-aminoacido
Serie: Datos y ociosidades
Estructura: pregunta
Estilo: oleo_expresivo
Voz: es-MX-JorgeNeural +7%, pitch −2 Hz
Cama: tambor
Título (pantalla): Un solo aminoácido
Título YT: Un aminoácido cambia el virus Andes #Shorts

## Hecho (2026-11-10, Imaginantes)

- Se usó este paquete (fuentes suficientes para 9 escenas). Narración alineada al paper de Vidal-Freire et al. 2026 (Science Advances, DOI 10.1126/sciadv.aek2522), no a la paráfrasis invertida del paquete: el aislado humano tiene I641; I641T (volver a T de roedor) reduce la retención en Golgi y acelera la salida de VLP, así que T641I se asocia con más retención y salida más lenta. Se documentó en `fuentes.md` (Nota de precisión 2026-11-10). Se plantea como posibilidad; no hay genética reversa para probarlo en virus completo.
- 9 frames PNG 1080×1920, estilo oleo_expresivo, sin texto en la imagen ni científica recurrente.
- Montaje oficial con `scripts/montar_capsula.py` (JorgeNeural, plano_seconds=5, cama `tambor`). Cortinilla de fuentes recortada a 2.0 s para entrar en 85–90 s (primera pasada: 93.93 s).
- MP4: `salidas/2026-11-09_andes-virus-aminoacido/capsula.mp4` y copia en `/workspace/entregas/2026-11-14_andes/capsula.mp4`
- Portada: `portada.jpg` extraída a 0.15 s (título en caja crema y subrayado rojo, sin subtítulo quemado). Miniatura de YouTube re-fijada con esta portada limpia (el extracto automático de `publicar.py` era a 0.5 s y traía el subtítulo).
- QA oficial `scripts/qa_capsula.py`: PASA (duración 89.93 s, 1080×1920, −14.2 LUFS, 239 palabras, cierre scene_009 12.3 s).
- Slot programado (autorizado por Mj, cápsula extra): **2026-11-14 13:30 hora CDMX (America/Mexico_City) = 2026-11-14T19:30:00Z**.

## Pendiente

- YouTube PROGRAMADO: videoId `8EcFyXTcSdM` — https://youtube.com/shorts/8EcFyXTcSdM — private, publishAt 2026-11-14T19:30:00Z (13:30 hora CDMX). Miniatura: thumbnails.set OK (portada a 0.15 s, maxres/qhd presentes). Confirmado por videos.list. containsSyntheticMedia=false (ilustración no realista).
- TikTok y Facebook: no programados por API. Programar a mano a la misma hora, eligiendo la portada como cover. Archivos y caption en `/workspace/entregas/2026-11-14_andes/`.

## Qué NO se hizo

- No se borró ni movió material publicado previo.
- No se subieron binarios pesados al repo (mp4/png/jpg gitignored).
- No se tocó TikTok ni Facebook.
