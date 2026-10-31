# Plan maestro operativo CAPCOT — vigente 2026-10-31

> Autoridad de investigación, preproducción y rotación. La autoridad superior para responsabilidades entre agentes, cupos y handoff es \`docs/CONTRATO_OPERATIVO_UNIFICADO.md\`; este Plan rige los detalles editoriales y técnicos de ChatGPT. Las instrucciones de producción integral anteriores, archivadas en \`docs/obsoleto/2026-10-31/\`, son legado.

## Precedencia y capacidad reconciliada

Consultar primero `docs/CONTRATO_OPERATIVO_UNIFICADO.md`. En esta rama, `scripts/rotacion.py` permite hasta cinco cápsulas por fecha (máximo dos propias y cinco externas, con tope global de cinco); `scripts/procesar_cola.py` procesa múltiples entradas de la fecha y conserva la entrada original cuando falla producción. La asignación horaria dispone de cinco ventanas, alineadas con los slots 07:00, 13:30, 17:00, 19:00 y 23:30 CDMX. Capacidad de código y programación no equivalen a publicaciones efectivas: cada publicación requiere QA y evidencia de plataforma. ChatGPT conserva el alcance textual descrito en este Plan; Imaginantes opera producción audiovisual, QA y publicación.

## Objetivo y alcance
CAPCOT / **Datos y ociosidades** produce cápsulas científicas y de naturaleza. ChatGPT es responsable de investigación, documentación y preproducción textual. Su entrega normal es un brief y un storyboard JSON verificables en GitHub.

ChatGPT no genera imágenes, frames, audio, voz, video ni renders; no ejecuta QA audiovisual oficial; no decide la publicación final ni publica. No consume créditos.

## Responsabilidades
| Responsable | Función |
|---|---|
| ChatGPT | Investigación, verificación de fuentes, radar, clasificación temática, brief y storyboard textual; mantenimiento de documentación y validadores. |
| Grok | Selección editorial final; adaptación del storyboard; generación/edición audiovisual; QA oficial; decisión y ejecución de publicación. |
| Usuario | Objetivos, prioridades y decisiones que requieren autorización personal. |
| GitHub | Fuente de verdad, historial, cola y evidencia. |

No atribuir a Grok revisión, aceptación o publicación que no esté registrada.

## Fuente de verdad
Repositorio: \`marcojpad-hash/capcot-capsulas-imaginantes\`. Rama de trabajo: \`feature/capcot-video-discovery-continuity\`.

Antes de cada ejecución leer, en este orden:
1. \`docs/CONTRATO_OPERATIVO_UNIFICADO.md\`
2. \`docs/PLAN_MAESTRO_AUTOMATICO.md\`
3. \`docs/RECETA_CAPSULA.md\`
4. \`docs/GUIA_MODELO_EXTERNO.md\`
5. \`docs/ESTILOS_VISUALES.md\`
6. \`scripts/estilos.json\`
7. \`data/temas_del_dia.json\`
8. \`data/rotacion.json\`
9. \`data/publicaciones.json\`, si existe
10. \`docs/LINEAS_TEMATICAS.md\`
11. \`docs/FLUJO_EXTERNO.md\`
12. \`docs/CONTINUIDAD_AUDIOVISUAL.md\`
13. \`docs/INVESTIGACION_API_META_Y_GOOGLE_TRENDS.md\`
14. Briefs recientes y storyboards relevantes de \`cola/entrada/\`, \`proyectos/\` y \`salidas/\`.

El catálogo canónico de estilos es \`scripts/estilos.json\`; el Markdown es una vista derivada.

## Investigación
1. Consultar los RSS científicos definidos en \`scripts/tendencias.py\` y Google Trends RSS México.
2. Si una fuente falla, registrar el error exacto. Si Trends RSS no se puede leer, consultar Trending Now oficial. Nunca afirmar que se parseó XML si no se obtuvo y procesó.
3. Reunir 3–5 candidatos publicados en los últimos siete días, priorizando el estudio original.
4. Verificar DOI mediante Crossref o resolvedor y contrastar afirmaciones en el paper o comunicado oficial. Si no se completa, marcar pendiente; no presentar el DOI como validado.
5. Clasificar por las líneas reales de \`docs/LINEAS_TEMATICAS.md\`; separar tendencia, relevancia científica y oportunidad editorial.
6. Registrar novedad, fuente primaria, DOI/URL, fecha, público/ocasión, riesgos y verificación.
7. Separar observado, cálculo, inferencia y recomendación. No inventar métricas, causalidad, resultados ni precisión geográfica.

## Rotación y memoria editorial
Los JSON de \`data/\` son registros operativos y pueden estar incompletos. No declarar unicidad usando solo esos archivos.
- Reconciliar \`data/temas_del_dia.json\`, \`data/rotacion.json\` y \`data/publicaciones.json\` con storyboards de \`cola/entrada/\`, \`proyectos/\` y \`salidas/\`.
- \`scripts/registro_editorial.py\` ofrece una vista de lectura combinada; no escribe ni modifica \`data/*.json\`.
- Una entrada de cola o proyecto preparado es evidencia de tema/estilo propuesto, no prueba de publicación.
- Distinguir propuesta, paquete preparado, producción audiovisual, QA oficial y publicación.
- No repetir el estilo de la cápsula anterior ni estilo/estructura ya usado el mismo día.
- Si no se reconstruye la secuencia, marcar la unicidad como no certificable e indicar las fechas faltantes.
- ChatGPT no modifica, completa ni inventa registros en \`data/*.json\`.

## Storyboard diario
Desarrollar un candidato principal para Grok:
- 9:16; 75–90 s totales, incluidos seis segundos de cortinilla.
- 170–235 palabras de narración; 7–9 escenas.
- Arco \`hook_medias_res\` → \`desarrollo\` → \`cierre_historia\` → \`reflexion_o_pregunta\`.
- \`titulo\` es el gancho y no supera seis palabras.
- Cada afirmación verificable lleva \`source_ids\`.
- Capa de mapa con coordenadas reales, fuente y nota de precisión.
- Capa de dato/gráfico con fuente primaria.
- Voz declarada: edge-tts, \`es-MX-JorgeNeural\`, rate \`+7%\`, pitch \`-2Hz\`.
- Ambiente y SFX por escena; biblia visual y tipográfica coherente.
- Serie exacta \`Datos y ociosidades\`; cierre hablado exacto \`Esto fue Datos y ociosidades.\`.

## Estilo
Elegir un solo estilo del catálogo por tema. Copiar literalmente \`prompt_base\` desde \`scripts/estilos.json\`; cada \`image_prompt\` debe comenzar con él. No inventar, mezclar ni renombrar estilos. No usar el estilo de la cápsula anterior. Si el Markdown difiere del JSON, prevalece el JSON.

## Entregables por ejecución
Crear exactamente:
1. \`docs/briefs/YYYY-MM-DD_RADAR_CAPCOT.md\`: 3–5 candidatos, Trends, fallos/fallbacks, límites y recomendación.
2. \`cola/entrada/YYYY-MM-DD_slug.json\`: storyboard completo con fuentes incorporadas en el propio JSON.

No crear un archivo de fuentes separado salvo petición expresa.

## Prohibición de assets en preproducción
En el JSON de cola no incluir \`asset_filename\`, \`asset_type\`, rutas de frames/audio/video ni \`export.filename\`. \`approved_assets\` debe ser \`[]\`; \`export.render_status\` debe ser \`NOT_GENERATED\`; \`publicacion.status\` queda pendiente de Grok. Los prompts son instrucciones futuras, no evidencia de imágenes existentes.

## Validación y entrega
Confirmar ambos archivos en la rama; volver a leerlos desde GitHub; parsear JSON; comprobar palabras, escenas, duración, arco, gancho, cierre, voz, estilo, fuentes, source_ids, mapa, dato/gráfico y ausencia de rutas de assets; registrar commits reales. No declarar QA ni aceptación de Grok.

No tocar \`main\`, no hacer merge, no modificar Motor U6 ni motores canónicos, no modificar \`data/*.json\`, no publicar/programar ni consumir créditos.

## Seguimiento técnico
Revisar documentación oficial/changelogs de Meta Graph API, Instagram Insights, Facebook Pages Insights y Google Trends API alfa. Comparar con \`docs/INVESTIGACION_API_META_Y_GOOGLE_TRENDS.md\`; actualizar solo si hay cambio nuevo relevante y sustentado. No solicitar ni guardar secretos. Si una integración requiere OAuth/permiso del titular, documentar el bloqueo y mantener la ruta pública disponible.

## Confirmación de recepción por Grok
Leer cola/estado/YYYY-MM-DD_slug.json si existe. Su ausencia significa que la recepción no está confirmada. Grok es el único responsable de crear/actualizar ese archivo; ChatGPT solo lo lee. Ver docs/GROK_STATUS_CONTRACT.md.

## Handoff optimizado para Grok Bot
Aplicar `docs/PROTOCOLO_DESCARGA_CARGA_GROK.md`: ChatGPT no entrega solo un tema o una idea, sino investigación verificada y paquete textual completo listo para producir (guion, storyboard, prompts por escena, audio/SFX, fuentes y metadata). Bot no debe repetir research ni redactar de nuevo por defecto; debe concentrarse en producción audiovisual, montaje, render y QA. Las devoluciones se hacen por campo/escena y ChatGPT resuelve investigación faltante con un parche. Las correcciones consumen tokens, por lo que no se solicitan reescrituras ni regeneraciones integrales sin defecto justificado.
