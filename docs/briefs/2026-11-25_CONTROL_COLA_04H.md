# CAPCOT — control de cola y auditoría
**Corte:** 2026-11-25 04:06, hora de Ciudad de México  
**Rama de trabajo:** `feature/capcot-video-discovery-continuity` — HEAD observado `a4df507`  
**Referencia de producción:** `main` — HEAD observado `7b50235`

## 1. Cambios desde el control anterior

La rama de trabajo no recibió storyboards nuevos para el 25 de noviembre. El árbol de `feature/capcot-video-discovery-continuity` conserva 90 storyboards y una sola entrada anidada en cola; no contiene los nueve reworks del 25–29, que están únicamente en `main`.

La comparación de `main` desde el control de las 22:00 hasta el HEAD actual muestra cambios en `data/cierre_diario/2026-11-24.md` y `data/endscreens_rotacion.json`; no hubo cambios de storyboard. Por tanto, no hay un borrador nuevo que justifique repetir QA narrativo.

## 2. Ocupación y colisiones de publicación

La conciliación de `data/miniaturas_auditoria_2026-11-21.json`, `data/rehechos_2026-11-22.json` y `data/horarios.json` confirma:

| Fecha | Programaciones | Límite diario | Estado |
|---|---:|---:|---|
| 25 nov | 7 | 5 | Sobre el límite |
| 26 nov | 7 | 5 | Sobre el límite |
| 27 nov | 7 | 5 | Sobre el límite |
| 28 nov | 7 | 5 | Sobre el límite |
| 29 nov | 5 | 5 | En el límite |

El 25 de noviembre hay dos videos distintos programados a las 07:00. También se mantienen dos reworks diarios a las 10:00 y 15:00 del 25 al 28, y uno a las 10:00 el día 29. Los reworks tienen identificadores de YouTube y estados de programación para TikTok/Facebook en el registro de reworks. No se canceló, reprogramó ni duplicó ninguna publicación.

Las ventanas vigentes son 06:30–07:30 y 16:30–18:00. Los horarios 10:00, 13:30, 15:00 y 19:00 quedan fuera de esas ventanas. La ocupación no deja un slot autorizado para un storyboard nuevo.

## 3. Reworks preexistentes en main

Se inspeccionaron los nueve proyectos de rework y sus archivos de storyboard, metadatos y render log. Los nueve ya tienen programación o identificador de video; se clasifican como `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`.

Hallazgos comunes:
- Siete escenas y entre 215 y 229 palabras por storyboard.
- Referencias de asset en las escenas y `export.filename` presente.
- `narrative_qa`, `approved_assets` y `export.render_status` ausentes.
- Los logs registran duraciones de 86.47–88.80 s, pero los MP4 referenciados no están en el árbol Git; no se puede medir ni verificar el medio desde el repositorio.
- Los nueve `cola/estado/<project_id>.json` devuelven 404: `RECEPCION_GROK_NO_CONFIRMADA`.
- `historial_youtube.json` devuelve 404, por lo que no se pudo conciliar el historial completo.

Clasificación: `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`, `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO` y `RECEPCION_GROK_NO_CONFIRMADA`. No se promovieron copias ni se alteró main.

## 4. QA narrativo y continuidad de auditoría

La auditoría fría del corte de las 14:00 registró 6 PASS y 3 FAIL para los nueve reworks. El control de las 22:00 reportó 8 PASS y 1 FAIL, pero la comparación de commits entre ambos cortes confirma que no cambió ningún storyboard: solo cambiaron datos de rotación y un reporte del orquestador. En aplicación de la regla de no repetir PASS cuando la narración no cambió, el resultado de las 22:00 no se usa para elevar los tres FAIL anteriores. Se conserva como discrepancia de auditoría, no como una nueva revisión válida.

Los 12 IDs del lote del 5–7 de noviembre conservan 2 PASS y 10 FAIL según la última auditoría disponible; no se repitieron sus PASS. El issue #11 de Cuásares continúa abierto con etiqueta `hecho`, pero su estado narrativo sigue FAIL/0 por ausencia de revisión independiente válida.

## 5. Cola y ruta de despacho

- `main/cola/entrada`: 32 storyboards anidados y `.gitkeep`; cero JSON planos.
- `feature/cola/entrada`: una entrada anidada (magnetismo) y `.gitkeep`; cero JSON planos.
- `data/cola.json` está vacío.
- `capcot-grok-dispatch.yml` filtra `cola/entrada/*.json` y selecciona con profundidad máxima 1. Las entradas anidadas no son despachables por ese workflow, aunque el procesador Python pueda recorrer carpetas.
- Magnetismo conserva seis escenas y 138 palabras; su estado Grok devuelve 404, carece de QA narrativo y no tiene el medio referenciado en el árbol. Se mantiene `NOT_DISPATCHABLE` y `RECEPCION_GROK_NO_CONFIRMADA`.

El trabajador de cola terminó SUCCESS, pero su log dice literalmente que no había trabajo en cola. No se disparó `capcot-grok-dispatch`, no se envió payload y no se inspeccionaron valores de secretos.

## 6. Actions, CI e issues

- Run `45530346824` — trabajador de cola: SUCCESS, sin trabajo en cola.
- Run `45578768822` — CodeQL programado: SUCCESS; no es un despacho Grok.
- Run `45560255843` — CodeQL en PR #3: SUCCESS; no acredita el validador estructural ni una prueba de storyboard.
- Run `45553710984` — Semgrep: FAILURE, 37 hallazgos bloqueantes; además omitió 37 archivos mayores de 1 MB. No se atribuyen los hallazgos a los archivos omitidos sin evidencia.
- Run `45553711043` — Gitleaks: SUCCESS.
- PR #15 permanece abierto. No se fusionó ni se disparó ningún workflow.

## 7. Feeds, tendencias y fuentes

Reintento de los diez feeds científicos y Google Trends RSS. Errores exactos observados:
- `curl: (6) Could not resolve host`: `trends.google.com`, `www.sciencedaily.com` (science y health), `www.esa.int`, `www.agenciasinc.es` y `unamglobal.unam.mx`.
- `curl: (28) Resolving timed out after 6000 milliseconds`: `www.sciencedaily.com` (space_time), `phys.org`, `www.nasa.gov`, `www.nature.com` y `www.eurekalert.org`.
- Crossref API y `doi.org`: `curl: (28) Resolving timed out after 6000 milliseconds`.

El respaldo HTML oficial de Google Trends México abrió y mostró 210 tendencias; la primera página no produjo un candidato científico apto sin una fuente primaria adicional. Se conservan los cinco candidatos del radar existente; ningún DOI se marca como verificado por resolver y no se añade storyboard.

## 8. Acciones y límites

No se modificaron `data/*.json`, main, permisos, secretos ni workflows. No se crearon medios, frames, voz, audio, video, renders ni placeholders. No se publicó, programó, canceló o reprogramó contenido; no se consumieron créditos.
