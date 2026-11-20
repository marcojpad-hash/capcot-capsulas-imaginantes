# Estado de ejecución — 2026-10-30_arqueas-origen-eucariotas

## Resultado
Paquete candidato externo preparado: storyboard, 8 frames, mapa de Yokosuka, gráfico de dato con fuente, cortinilla, bloques de subtítulos y registro preliminar de licencias. **No hay MP4, voz, música renderizada, ASS/SRT temporizado, QA oficial ni publicación.**

## Entorno
- /workspace/capcot: AUSENTE.
- ffmpeg y ffprobe: presentes.
- edge_tts: ModuleNotFoundError; falta la voz obligatoria es-MX-JorgeNeural.
- No se sustituyó la voz ni se montó un MP4 incompleto.
- Las 8 imágenes se generaron manualmente con OpenAI ImageGen y se normalizaron a 1080×1920; no es una ejecución del proveedor de imágenes del pipeline.
- El gráfico y la cortinilla se generaron localmente. El mapa usa coastlines GSHHG incluidos en Basemap; licencia LGPL-3.0-or-later. El punto es aproximado y representa la sede institucional JAMSTEC, no el sitio de muestreo.
- Crossref REST falló por resolución DNS. El DOI resuelve en la página editorial de Nature y el comunicado de JAMSTEC confirma el estudio. No se afirma que el validador automático DOI haya pasado.
- No se ejecutaron procesar_cola.py, validar_storyboard.py --check-doi, capsula_diaria.py ni qa_capsula.py. No se declara QA oficial.

## Registros diarios
- data/temas_del_dia.json: fechas hasta 2026-10-28; no hay entrada del 29 ni del 30.
- data/rotacion.json: 22 registros hasta 2026-10-28; no hay registro del 29 ni del 30.
- data/publicaciones.json: 17 registros hasta 2026-10-26; no hay registro del 30.
- data/cola.json está vacío.
- No existe data/horario_2026-10-30.json ni hay proyectos 2026-10-30_* en el árbol consultado.
- Por eso **no puede certificarse la unicidad frente a cápsulas no registradas del 30-oct**. El tema no aparece en los temas registrados. Se eligen estructura pregunta, estilo microscopio_psicodelico y música sintetico:pizzicato; difieren de la última cápsula documentada del 29-oct (sabias_que, mosaico_piedra, menor_calma) y de la última rotación del 28-oct (historia, ukiyo_e, arpegio). Esta comparación no sustituye los registros diarios faltantes.
- scripts/rotacion.py fija máximo 3 cápsulas por día (2 propias + 1 externa). No se forzó ni simuló cupo.

## Handoff operativo
salidas/_ops/2026-10-28_HANDOFF_TOTAL_grok_principal.md asigna temporalmente la producción integral a Grok principal. Esta carpeta se preparó por la instrucción explícita recibida; no se presenta como ejecución de Grok Bot ni del pipeline oficial.

## Integridad y alcance
- 8 escenas; 176 palabras; 80 s de escenas + 6 s de cortinilla = 86 s; 61 bloques de subtítulos, máximo 3 palabras.
- Objetivo: 9:16, 1080×1920, 30 fps, H.264/AAC, −14 LUFS.
- Capas: mapa con fuente oficial; gráfico 100 % vs 142 % con DOI; dato de dos cepas.
- Los subtítulos no tienen timecodes; deben sincronizarse con WordBoundary del TTS oficial.
- No se modificaron temas, rotación, publicaciones, cola, horarios ni motor U6. No se publicó nada.


## Corrección de auditoría — 2026-11-20

**Estado de preproducción:** `BORRADOR_EN_PROYECTOS_NO_APTO_PARA_PROMOCION`. **Clasificación de producción:** `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`. **Recepción Grok:** `RECEPCION_GROK_NO_CONFIRMADA`. **Medios:** `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`.

- La afirmación anterior de que no había publicación queda contradicha por `salidas/2026-10-30_arqueas-origen-eucariotas/publicacion.json`: YouTube ID `bICGA3kIBcU`, privacidad `private`, `publishAt=2026-11-02T01:00:00Z` (1-nov, 19:00 CDMX). No se afirma que haya llegado a público.
- El mismo registro conserva `historial_youtube` con `i2l4BkMvHp0` y `9XflXdWDM0A` todavía descritos como programados. Riesgo de duplicado; no borrar ni cancelar.
- `salidas/.../qa.json` es QA audiovisual (21/21, 81.80 s), no narrative_qa. El storyboard no contiene narrative_qa independiente.
- `SHA256SUMS.json` declara `media_committed_to_github=false`; no hay MP4/frames verificables en el árbol. No reabrir ni redispatchar el proyecto.
