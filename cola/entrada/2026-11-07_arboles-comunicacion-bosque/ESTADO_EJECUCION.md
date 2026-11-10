# ESTADO_EJECUCION — 2026-11-07_arboles-comunicacion-bosque

Project: 2026-11-07_arboles-comunicacion-bosque
Serie: Datos y ociosidades
Estructura: mito_vs_dato
Estilo: papel_rasgado_capas
Voz: es-MX-JorgeNeural +7%, pitch −2 Hz
Cama: pizzicato
Título (pantalla): ¿Los árboles hablan?
Título YT: ¿Los árboles hablan bajo tierra? #Shorts

## Hecho (2026-11-10, Imaginantes)

- Storyboard ampliado de 5 a 9 escenas / 228 palabras. Se descartó el DOI falso `10.1126/example` del paquete. Fuentes usadas: Simard et al. 1997 (Nature, DOI 10.1038/41557) y Karst, Jones & Hoeksema 2023 (Nat Ecol Evol, DOI 10.1038/s41559-023-01986-1). No se repitió la afirmación no sustentada de que un árbol atacado «avisa a los vecinos».
- 9 frames PNG 1080×1920, estilo papel_rasgado_capas, sin texto en la imagen; paleta teal/verde/ocre/crema.
- Montaje oficial con `scripts/montar_capsula.py` (JorgeNeural, plano_seconds=5, cama `pizzicato`). Escenas con sfx `redes` pasaron a `silencio` (el sfx redes depende de `madera`, ausente).
- MP4: `salidas/2026-11-07_arboles-comunicacion-bosque/capsula.mp4` y copia en `/workspace/entregas/2026-11-13_arboles/capsula.mp4`
- Portada: `portada.jpg` extraída a 0.5 s (título en caja crema y subrayado rojo).
- QA oficial `scripts/qa_capsula.py`: PASA (duración 87.50 s, 1080×1920, −14.3 LUFS, 228 palabras, cierre scene_009 11.2 s).
- Slot programado (autorizado por Mj, cápsula extra): **2026-11-13 13:30 hora CDMX (America/Mexico_City) = 2026-11-13T19:30:00Z**.

## Pendiente

- YouTube PROGRAMADO: videoId `EX0W3q-yKRw` — https://youtube.com/shorts/EX0W3q-yKRw — private, publishAt 2026-11-13T19:30:00Z (13:30 hora CDMX). Miniatura: thumbnails.set OK (portada a 0.5 s, maxres presente). Confirmado por videos.list. containsSyntheticMedia=false (ilustración no realista).
- TikTok y Facebook: no programados por API. Programar a mano a la misma hora, eligiendo la portada como cover. Archivos y caption en `/workspace/entregas/2026-11-13_arboles/`.

## Qué NO se hizo

- No se borró ni movió material publicado previo.
- No se subieron binarios pesados al repo (mp4/png/jpg gitignored).
- No se tocó TikTok ni Facebook.
