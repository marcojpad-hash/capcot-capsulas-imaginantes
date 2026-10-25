# CAPCOT — 25 de octubre de 2026: recuperación de corales blanqueados

**Estado:** paquete editorial y visual preparado; no renderizado; no publicado.

## Contenido
- `storyboard.json`: 9 escenas, arco `historia`, 222 palabras, 82 s de escenas + 6 s de cortinilla (88 s previstos), voz obligatoria `es-MX-JorgeNeural`, mapa y capa de dato con fuente.
- `frames/scene_001.png` … `frames/scene_009.png`: ilustraciones generadas con IA, normalizadas a 1080×1920.
- `fuentes.md`: estudio original DOI, comunicado institucional, noticia dentro de la ventana de siete días y fuente de ubicación del mapa.
- `licencias.json`: registro preliminar de imágenes, voz, música, SFX, mapa y datos.
- `subtitulos_plan.json`: bloques de texto de máximo tres palabras; no contiene tiempos.
- `ESTADO_EJECUCION.md`: limitaciones comprobadas, conflicto de cupo y elementos pendientes.
- `contact_sheet.png`: hoja de revisión de los nueve frames; no usar como frame del video.
- `SHA256SUMS.json`: tamaños y SHA-256 de los archivos incluidos.

## Uso previsto
Importar el paquete en `cola/entrada/2026-10-25_corales-contacto/` para que Grok Bot ejecute el pipeline oficial cuando el entorno y el cupo estén resueltos. No se debe marcar como publicado ni aprobado por QA con este paquete solamente.

## Importante
El entorno de esta ejecución no contiene `/workspace/capcot` ni el módulo `edge_tts`. Por tanto, no existe MP4, voz, SRT/ASS temporizado ni resultado de QA oficial. La entrada no se añadió a `data/cola.json`, y no se modificaron los registros de temas, rotación o publicaciones.

Los `image_prompt` del storyboard están normalizados al formato exacto `prompt_base + " + " + descripción de escena` del catálogo `ukiyo_e`. Los PNG adjuntos se generaron con briefs visuales ampliados y coherentes con ese estilo; no fueron producidos por `scripts/generar_frames.py` ni por una corrida oficial.
