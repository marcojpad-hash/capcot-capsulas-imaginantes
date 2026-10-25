# Estado de ejecución — 2026-10-25_corales-contacto

## Estado real
- Paquete editorial preparado con storyboard, fuentes, registro preliminar de licencias, plan de bloques de subtítulos y nueve frames ilustrados.
- **No se generó MP4. No se generó voz ni SRT/ASS temporizado. No se ejecutó el QA oficial. No se publicó.**
- No se escribió en `data/temas_del_dia.json`, `data/rotacion.json`, `data/publicaciones.json` ni `data/cola.json`.
- En GitHub se versionaron únicamente storyboard y documentación. Los PNG permanecen en el ZIP; la carpeta de cola no está lista para montaje hasta extraer esos medios.

## Bloqueos comprobados en este entorno
1. `/workspace/capcot` no existe en este entorno; por ello no estaba disponible la cola local oficial (`scripts/procesar_cola.py` → `scripts/capsula_diaria.py` → `scripts/qa_capsula.py`).
2. El módulo Python `edge_tts` no está instalado. La receta prohíbe sustituir `es-MX-JorgeNeural` por otra voz o montar con una voz distinta; por eso se entrega sin montar.
3. El pipeline de imágenes/capas, la cama musical, la cortinilla de fuentes y el QA oficial no se ejecutaron. Los nueve PNG se normalizaron localmente a 1080×1920; esto **no** equivale a una corrida oficial ni a aprobación de QA.

## Conflicto de cupo detectado en los datos existentes
`data/publicaciones.json` contiene cuatro `project_id` distintos con fecha `2026-10-25`: `2026-10-25_sueno-electricidad-qom`, `2026-10-25_ave-jurasica-sin-vuelo`, `2026-10-25_reina-olor` y `2026-10-24_lote01-04-tardigrado` (este último anotado como placeholder). `scripts/rotacion.py` establece un máximo duro de tres cápsulas por fecha. La corrida oficial probablemente rechazará esta entrada por cupo hasta que el proceso responsable reconcilie los registros existentes. No se alteraron esos registros manualmente.

## Diferenciación del día
- Tema: recuperación del coral blanqueado por contacto entre clones; no aparece en los temas del 25-octubre.
- Estructura: `historia`; las estructuras registradas hoy son `comparacion` y `pregunta`.
- Estilo: `ukiyo_e`; no aparece entre los estilos registrados hoy (`van_gogh`, `linograbado`).
- Música propuesta: `arpegio`; difiere de las camas registradas hoy (`marimba`, `pulso`) y de la cama `pizzicato` especificada en el storyboard de Yuezhuornis. `data/publicaciones.json` no registra la cama musical de `2026-10-25_reina-olor`, así que no es posible certificar que también difiera de esa cápsula.

## Alcance científico
El experimento se hizo en laboratorio, con muestras pequeñas y corales del mismo genotipo. El resultado no equivale a una técnica ya aplicable a la restauración masiva de arrecifes. La ubicación del mapa es la estación de laboratorio de Pacific Grove; el estudio no documenta el lugar de recolección original de los corales.

## Procedencia de los frames
Los `image_prompt` del storyboard están normalizados al formato exacto `prompt_base + " + " + descripción de escena` del catálogo `ukiyo_e`. Los PNG adjuntos se generaron con briefs visuales ampliados y coherentes con ese estilo; no fueron producidos por `scripts/generar_frames.py` ni por una corrida oficial.
