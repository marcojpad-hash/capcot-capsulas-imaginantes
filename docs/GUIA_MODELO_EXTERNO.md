# Guía para ChatGPT y modelos externos

Tu función es investigar y entregar preproducción textual. **No generes imágenes, frames, audio, voz, video o renders. No publiques ni programes.** Grok conserva selección editorial final, producción audiovisual, QA oficial y publicación.

## Lectura
Lee primero \`docs/PLAN_MAESTRO_AUTOMATICO.md\`; después \`docs/RECETA_CAPSULA.md\`, \`docs/ESTILOS_VISUALES.md\`, \`scripts/estilos.json\`, \`data/temas_del_dia.json\`, \`data/rotacion.json\`, \`data/publicaciones.json\` si existe, \`docs/LINEAS_TEMATICAS.md\`, \`docs/FLUJO_EXTERNO.md\`, \`docs/CONTINUIDAD_AUDIOVISUAL.md\`, \`docs/INVESTIGACION_API_META_Y_GOOGLE_TRENDS.md\`, briefs recientes y storyboards de cola/proyectos/salidas.

Los JSON de datos pueden estar incompletos. Contrástalos con storyboards históricos; no declares unicidad si faltan registros.

## Investigación
Consultar RSS científicos y Google Trends RSS México. Registrar fallos exactos y usar Trending Now oficial si Trends RSS falla. Reunir 3–5 candidatos recientes (≤7 días), priorizar estudio original, verificar DOI/URL y respaldar cada afirmación. Separar tendencia, relevancia científica y oportunidad editorial. Distinguir observado, cálculo, inferencia y recomendación.

## Storyboard
Desarrollar un candidato principal con la receta y plantilla vigentes. Serie exacta «Datos y ociosidades» y cierre hablado «Esto fue Datos y ociosidades.». Elegir un estilo del catálogo, copiar \`prompt_base\` literalmente y no repetir el estilo anterior. Incluir mapa, dato/gráfico, fuentes por escena, biblia visual/tipográfica, voz prevista, ambiente y SFX.

## Entrega
Crear exactamente:
- \`docs/briefs/YYYY-MM-DD_RADAR_CAPCOT.md\`
- \`cola/entrada/YYYY-MM-DD_slug.json\`

Fuentes y verificación van dentro del JSON. No crear \`_fuentes.md\`. El JSON de cola no incluye \`asset_filename\`, \`asset_type\`, rutas de medios ni \`export.filename\`; \`approved_assets=[]\` y \`render_status=NOT_GENERATED\`.

Volver a leer desde GitHub, parsear, contar palabras/duración, comprobar arcos, gancho, cierre, voz, estilo, mapa, dato/gráfico, source_ids y ausencia de placeholders. Registrar commits reales. No declarar QA ni aceptación de Grok.
