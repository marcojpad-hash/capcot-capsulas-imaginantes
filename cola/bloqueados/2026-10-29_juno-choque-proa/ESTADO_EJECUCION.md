# Estado de ejecución — 2026-10-29_juno-choque-proa

## Resultado
Paquete candidato preparado con storyboard, ocho frames, mapa esquemático, dos capas de datos/gráficos, cortinilla, fuentes, registro preliminar de licencias y bloques de subtítulos de hasta tres palabras. **No hay MP4 final, voz, SRT/ASS temporizado, QA oficial ni publicación.**

## Entorno comprobado en esta sesión
- `test -d /workspace/capcot`: `false`; el runtime oficial no está disponible.
- `python3 -c 'import edge_tts'`: `ModuleNotFoundError: No module named 'edge_tts'`.
- `ffmpeg` sí existe en `/usr/bin/ffmpeg`, pero no sustituye el TTS obligatorio ni el pipeline oficial.
- No se ejecutaron `scripts/validar_storyboard.py --check-doi`, `scripts/capsula_diaria.py`, `scripts/procesar_cola.py` ni `scripts/qa_capsula.py`. No se presenta validación local como QA oficial.
- Ocho frames se generaron con OpenAI ImageGen y se normalizaron a 1080×1920. No se generaron audio, música ni MP4. Los overlays se diseñaron localmente como referencias para montaje manual.
- Las llamadas de generación usaron prompts visualmente compatibles con el estilo Art Déco; no copiaron literalmente el campo `image_prompt` completo en cada llamada. El storyboard sí conserva el `prompt_base` exacto del catálogo para reproducibilidad. Revisión estética de Grok pendiente.
- El handoff operativo `salidas/_ops/2026-10-28_HANDOFF_TOTAL_grok_principal.md` asigna temporalmente la producción integral a Grok principal mientras se recuperan créditos. Este paquete se preparó por la instrucción directa de esta conversación; no se presenta como ejecución de Grok Bot ni sustituye su revisión.
- El DOI resuelve en la página editorial de Nature Communications. La API Crossref no pudo consultarse desde esta sesión; no se afirma que se haya pasado la compuerta Crossref.

## Actualidad y precisión de la fuente
- La noticia de ScienceDaily está fechada el 28-oct-2026.
- El artículo primario de *Nature Communications* se publicó el 31-jul-2026. La cápsula se presenta como cobertura de actualidad publicada hoy, **no** como un artículo primario recién publicado esta semana.
- Los resultados se basan en dos cruces del choque de proa de Júpiter observados por Juno el 10–11-dic-2024. La extrapolación a restos de supernovas es una posible aplicación, no una observación de Juno en una supernova.

## Rotación y conflictos de la parrilla
- `data/temas_del_dia.json` llega hasta 2026-10-28; no hay entrada para 2026-10-29. El tema Juno/choque de proa no aparece en los temas registrados del 24 al 28-oct.
- `data/rotacion.json` tiene cero registros del 29-oct. `data/publicaciones.json` también tiene cero registros del 29-oct.
- `data/estilos_usados.json` termina con los estilos del 28-oct (`papel_infantil`, `fieltro_stop_motion`, `grafiti_colorido`, `bordado`, `ukiyo_e`). `art_deco_poster` no aparece en los últimos cinco registros.
- La cama `pizzicato` no aparece en las cinco cápsulas registradas del 28-oct (`pulso`, `circuito_neural`, `tambor`, `marimba`, `arpegio`).
- La estructura `sabias_que` no aparece en las estructuras registradas el 28-oct (`historia`, `pregunta`, `mito_vs_dato`, `comparacion`, `historia`).
- `data/horario_2026-10-29.json` no existe y `data/cola.json` está vacío. Un handoff de operaciones menciona una propuesta para 29-oct 19:00 sobre Machu Picchu/fallas vs. Pisa, pero el storyboard referenciado no existe en el path indicado. Por tanto, **no puede certificarse la unicidad frente a todas las cápsulas que pudieran estar planificadas hoy**. Esta candidata es distinta de todos los registros consultables, pero no se inventaron datos para completar el horario.
- La estructura, el estilo y la música de la candidata son `sabias_que`, `art_deco_poster` y `sintetico:pizzicato`, respectivamente. El estilo encaja con astronomía/tecnología del catálogo; no repite los estilos de ayer.

## Integridad y alcance
- 8 escenas; duración de escenas 79 s + cortinilla 6 s = 85 s previstos.
- Narración dentro del rango 170–235 palabras; 9:16, 1080×1920, 30 fps como objetivo de exportación.
- Incluye capa `mapa` con ubicación aproximada de University of Iowa y capas `grafico`/`dato` con fuente.
- `subtitulos_bloques.json` contiene bloques de 1–3 palabras, sin marcas de tiempo. El TTS oficial debe generar WordBoundary.
- El mapa local es un esquema de ubicación; la capa `mapa` del storyboard contiene coordenadas para que el pipeline oficial la renderice con Natural Earth.
- No se modificaron `data/temas_del_dia.json`, `data/rotacion.json`, `data/publicaciones.json`, `data/cola.json`, `data/estilos_usados.json` ni el motor U6.
