# Estado de ejecución — 2026-10-27_corneja-decision-rapida

## Resultado

Paquete candidato preparado: storyboard, 8 frames, música original, fuentes, registro de licencias y plan de bloques de subtítulos. **No hay MP4 final, audio de voz, SRT temporizado ni QA oficial. No publicado.**

## Comprobaciones del entorno

- `test -d /workspace/capcot`: falso; el runtime oficial no está disponible en esta sesión.
- `python3 -c 'import edge_tts'`: `ModuleNotFoundError: No module named 'edge_tts'`.
- `ffmpeg` y `ffprobe`: presentes.
- La receta exige `edge-tts`, voz `es-MX-JorgeNeural`, +7 %, pitch −2 Hz. No se sustituyó por otra voz y no se montó un MP4 parcial.
- La música original se entrega como MP3 dentro del ZIP. El `music_asset` del storyboard apunta a la ruta esperada si el paquete se extrae en `/workspace/capcot/cola/entrada/2026-10-27_corneja-decision-rapida/`.

## Conflictos del estado editorial de hoy

- Tema: la decisión visual ultrarrápida de cornejas negras no aparece en `data/temas_del_dia.json` del 27-oct.
- Estilo: `microscopio_psicodelico` pertenece a `scripts/estilos.json`; no aparece entre los estilos de las cápsulas programadas de hoy ni coincide con el último estilo de rotación (`dibujo_cientifico_scratchboard`).
- Música: se creó una composición original propia, 7/8, cama `cognicion_7_8`, distinta de las camas registradas o programadas hoy. Es un archivo, no una cama nombrada del selector `CAMAS`.
- **Estructura no puede ser única sin cambiar el esquema:** las cinco estructuras permitidas están usadas hoy en el conjunto registrado/programado: `historia`, `pregunta`, `mito_vs_dato`, `comparacion` y `sabias_que` (esta última en el proyecto muralismo programado para hoy). Se conserva `sabias_que` para mantener compatibilidad con el validador, pero la unicidad formal queda **NO RESUELTA**. No se inventó una sexta estructura ni se modificó el pipeline.
- **Cupo externo bloqueado:** `data/rotacion.json` contiene siete entradas fechadas 2026-10-27, todas `origen: propia`, aunque el procedimiento establece un máximo de tres cápsulas por día (dos propias + una externa). `data/cola.json` está vacío y `data/publicaciones.json` no contiene registros del día, mientras `data/horario_2026-10-27.json` lista seis slots programados. El pipeline oficial probablemente rechazará la entrada por el cupo/estado incoherente. No se corrigieron ni fabricaron registros.

## Integridad y límites

- JSON de storyboard parseable; 8 escenas, 208 palabras narradas, 85.5 s planificados incluida la cortinilla, formato objetivo 1080×1920/30 fps.
- Cada escena declara `source_ids`, `ambiente`, `sfx`; hay capa mapa y capas de dato con fuente.
- Los bloques de referencia de subtítulos tienen como máximo tres palabras, pero **no llevan timecodes**. El SRT/ASS definitivo debe generarlo el pipeline a partir de WordBoundary de la voz.
- No se ejecutó `procesar_cola.py`, `capsula_diaria.py`, `validar_storyboard.py` ni `qa_capsula.py`: no están disponibles en este entorno. No se afirma QA aprobado.
- No se modificaron `data/temas_del_dia.json`, `data/rotacion.json`, `data/publicaciones.json`, `data/cola.json`, ni motor U6.
