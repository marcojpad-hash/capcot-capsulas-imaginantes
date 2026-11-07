# ESTADO_EJECUCION — 2026-11-07_comida-hielo-caliente

Project: 2026-11-07_comida-hielo-caliente
Slot propuesto: 2026-11-07 13:30, comida_familia
Serie: Datos y ociosidades
Estructura: mito_vs_dato
Estilo: linea_fina (catálogo, temas química / cocina; no es el último estilo usado, ukiyo_e, ni los prohibidos grafiti_colorido, bordado, ukiyo_e, litografia_azul_dorado)
Voz: es-MX-JorgeNeural +7%, pitch -2Hz (solo en storyboard; Pecas NO montó MP4 final con otra voz)
Duración borrador: 60 s, 6 escenas, ~115 palabras de narración

## Qué hay en este paquete
- storyboard.json — 6 escenas completas, en español, con source_ids
- fuentes.md — SRC-001 con DOI verificado, SRC-002 sin DOI inventado
- ESTADO_EJECUCION.md — este archivo

## Qué falta / pendientes para Imaginantes
- Frames: NO hay frames JPG en el repo. Pecas generó 6 clips de video de prueba en español (~10 s c/u) en su espacio de trabajo, no subidos como MP4 al repo por la regla de no subir mp4 / medios pesados. Los image_prompt de cada escena en storyboard.json permiten generar los frames con scripts/generar_frames.py.
- Capas mapa y dato/gráfico: borrador listo 2026-11-07 con Gemini (conector directo custom.gemini): `capas_dato_mapa_borrador.json`. Verificación de las 6 narraciones contra SRC-001 y SRC-002: todas "ok", sin datos inventados. Capas propuestas: scene_001 mapa "Tanzania, África" (SRC-002), scene_002 dato "Erasto Mpemba, estudiante" (SRC-002), scene_003 dato "Mpemba y Osborne, 1969" (SRC-002), scene_004 sin capa (premisa lógica, sin dato respaldado), scene_005 dato "Burridge y Linden, 2016" (SRC-001), scene_006 dato "Efecto aún en disputa" (SRC-001). Imaginantes decide si las usa tal cual o las genera con scripts/capas_datos.py.
- Duración ideal: 75-90 s y 170-235 palabras según RECETA. Este borrador es de 60 s, mínimo aceptado por QA (60-95 s). Para llegar a 75-90 s faltan 2 escenas.
- Ambiente/SFX por escena: no fijados en este borrador; que los ponga el pipeline sin repetir cama de hoy.
- QA oficial: pendiente. Este borrador NO es un QA propio aprobado; solo cuenta scripts/qa_capsula.py corrido por Imaginantes.

## Qué NO se hizo
- No se publicó nada en YouTube, TikTok ni Facebook.
- No se editó data/horario_*.json, data/publicaciones.json ni data/rotacion.json.
- No se montó MP4 final.

## Siguiente paso para Imaginantes
1. git pull --rebase
2. python3 scripts/procesar_cola.py
3. Generar frames, capas mapa/dato, montar con scripts/montar_capsula.py (JorgeNeural)
4. python3 scripts/qa_capsula.py
5. Programar / publicar solo si QA pasa, slot 2026-11-07 13:30
