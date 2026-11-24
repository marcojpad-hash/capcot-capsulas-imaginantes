# CONTROL DE COLA — 2026-11-24 04:00 CDMX

## Autoridad y alcance

- Rama auditada: `feature/capcot-video-discovery-continuity`, HEAD `44c7ee21e0d6f9da4131d28b0efb95ad189286f9`.
- `main` consultada solo para ocupación, publicaciones, salidas y producción preexistente; HEAD `05c62dd3c9b9a8ccdbff5c303080b16bb3b71c7e`.
- La comparación entre ramas reporta 1,350 commits adelante y 566 detrás para feature. No se sincronizaron ramas ni se hizo merge.
- Se relevaron 32 storyboards de proyecto en el backlog auditado: 12 del lote 5–7 nov, 4 del 14–16 nov, 14 del 17–22 nov y 2 nuevos del 23-nov.

## Inventario de QA y estructura

| Grupo | Proyectos | Narrative QA PASS | FAIL | Observación estructural principal |
|---|---:|---:|---:|---|
| 5–7 nov | 12 | 2 | 10 | 85 escenas; 510 campos de progresión ausentes; 82 escenas sin SFX; un proyecto sin mapa ni gráfico |
| 14–16 nov | 4 | 3 | 1 | Los cuatro cumplen la estructura mecánica auditada; Quásares conserva FAIL/0 |
| 17–22 nov | 14 | 7 | 7 | Tres proyectos con QA PASS carecen de capa de mapa |
| 23 nov | 2 | 0 | 2 | Ambos FAIL/82; estructura mecánica completa |
| **Total** | **32** | **12** | **20** | **Ninguno promovible en este corte** |

Los estados QA son los ya registrados; no se repitió una revisión PASS ni se reescribió narración. La inspección estructural se hizo por separado.

### Lote 5–7 nov (12)

- IDs: `2026-11-05_comida-palomitas`, `2026-11-05_inter-arboles-se-comunican`, `2026-11-05_inter-rayo-globular`, `2026-11-05_kids-dia-en-venus`, `2026-11-06_comida-aguacate-negro`, `2026-11-06_inter-arena-cantante`, `2026-11-06_inter-ranas-congeladas`, `2026-11-06_kids-ballena-azul-corazon`, `2026-11-07_comida-hielo-caliente`, `2026-11-07_inter-nubes-pesan`, `2026-11-07_inter-pulpo-suenos`, `2026-11-07_kids-huesos-bebe`.
- Narrative QA existente: Venus 88 PASS y Arena 94 PASS; los otros diez FAIL.
- Los 85 scenes carecen de los seis campos de progresión (`dramatic_beat`, `scene_function`, `causal_bridge_from_previous`, `question_state`, `reason_to_continue`, `new_information`): 510 ausencias. 82 escenas no tienen SFX. `ambiente` sí está presente.
- 11/12 contienen una capa `mapa` con puntos lat/lon y 11/12 una capa de dato/gráfico. `inter-arboles-se-comunican` carece de ambas. Las coordenadas declaradas no se re-resolvieron individualmente contra cada fuente en este run.
- Los doce cumplen los rangos de escena/palabras/duración y conservan voz, `prompt_base`, cortinilla de 6 s, `approved_assets=[]` y `export.render_status=NOT_GENERATED`. Los dos PASS narrativos no pasan estructura por los campos ausentes.
- `cola/bloqueados/` contiene doce copias JSON planas. Hay nueve carpetas de proyecto con estado BORRADOR y una carpeta `extra-nubes-pesan` clasificada como `MATERIAL_DE_ORIGEN_NO_ES_PROYECTO`; no se cuenta como proyecto adicional. La variante `inter-mpemba-mito` permanece BORRADOR.

### Backlog 14–16 nov (4)

- `2026-11-14_dato-microplasticos-pantanal`: PASS/88. Fuente primaria Nature, DOI `10.1038/s41586-026-11285-x` (publicación 11-nov-2026).
- `2026-11-15_dato-dia-diapausa-lestes-sponsa`: PASS/90. DOI `10.1038/s41598-026-80392-6` (Scientific Reports, 15-nov-2026). Existe copia bloqueada y su `fuentes.md` reporta una ejecución local de `--check-doi` con salida 0; no se encontró artefacto de esa ejecución para reproducirla desde este run.
- `2026-11-15_dato-quasar-pareja-cosmic-dawn`: FAIL/0, `REVISION_INDEPENDIENTE_AUSENTE`.
- `2026-11-16_dato-polen-desenreda-nanotubos`: PASS/91. Fuente primaria Nature Communications, DOI `10.1038/s41467-026-79607-1` (publicación 14-nov-2026).
- Los cuatro cumplen la estructura mecánica inspeccionada: 8 escenas, 182–196 palabras, 84 s, voz y prompt_base correctos, mapa/gráfico, SFX y campos de progresión presentes, cortinilla 6 s, sin medios.

### Quásares — issue #11 y PR #13

- El storyboard vigente conserva `narrative_qa=FAIL`, score 0 y `REVISION_INDEPENDIENTE_AUSENTE`.
- PR #13 contiene un informe de auditoría separado, pero el informe hace referencia a título/pregunta/arco/límite de evidencia y no acredita una lectura ciega de solo narración con `review_basis=lectura_en_frio_solo_narracion`; tampoco incorpora los siete checks formales al storyboard. No sustituye la compuerta fría exigida.
- Issue #11 sigue OPEN con etiqueta `hecho`; PR #13 sigue OPEN/no merged. No se cambió el issue ni se copió un QA incompleto al storyboard.

### Backlog 17–22 nov (14)

- IDs: `2026-11-17_dato-suelo-dos-relojes`, `2026-11-18_dato-catorce-campos-hidrotermales`, `2026-11-18_dato-kuroshio-puente-atmosferico`, `2026-11-19_dato-dia-luz-dos-manos-oro-poroso`, `2026-11-19_dato-estrella-dentro-de-estrella`, `2026-11-20_dato-dia-atlantico-humedad-sapropeles`, `2026-11-20_dato-marea-cerebral-en-sueno`, `2026-11-21_fentale-metano-sin-erupcion`, `2026-11-21_homo-erectus-selva-tropical`, `2026-11-21_pulsar-gamma-reticulo`, `2026-11-22_bao-estrella-fusion-andromeda`, `2026-11-22_genes-estatura-etapas`, `2026-11-22_voyager-1-un-dia-luz`, `2026-11-22_yubarta-genoma-soplo`.
- Siete PASS y siete FAIL. Los tres PASS sin mapa son Kuroshio, estrella-dentro-de-estrella y yubarta; los catorce sí tienen capa de gráfico, SFX y campos de progresión completos.
- Los únicos dos `ESTADO_EJECUCION.md` de proyecto encontrados en este grupo (campos hidrotermales y Kuroshio) ya dicen `BORRADOR_EN_PROYECTOS_NO_APTO_PARA_PROMOCION`; no hubo que corregir estados.

### Borradores 23 nov (2)

- `2026-11-23_supersequias-722-eventos`: FAIL/82.
- `2026-11-23_tropical-biodiversity-turnover`: FAIL/82.
- Ambos tienen 8 escenas, 171/220 palabras, 84 s, mapa, gráfico, voz, prompt_base, cortinilla, SFX y progresión completos. El bloqueo es narrativo; no se reescribió.

### Resumen estructural agregado

- 32 proyectos; 12 PASS narrativos / 20 FAIL.
- 4 proyectos sin mapa: `inter-arboles-se-comunican`, Kuroshio, estrella-dentro-de-estrella y yubarta.
- 1 proyecto sin capa de gráfico: `inter-arboles-se-comunican`.
- 82 escenas sin SFX y 510 campos de progresión ausentes, todos concentrados en el lote 5–7 nov.
- Los 32 conservan `approved_assets=[]` y `export.render_status=NOT_GENERATED`; no se generaron medios ni placeholders.

## Estados Grok, cola y dispatch

- Se consultaron los 32 paths `cola/estado/<project_id>.json`: todos devolvieron 404. Estado para los 32: `RECEPCION_GROK_NO_CONFIRMADA`. No se creó ni editó ningún estado Grok.
- No hay entradas planas nuevas en `cola/entrada/`. El único paquete anidado observado en feature es `2026-11-09_dato-robot-ensambla-orbita`.
- `.github/workflows/capcot-grok-dispatch.yml` filtra `cola/entrada/*.json` y el selector usa profundidad 1. `scripts/procesar_cola.py` reconoce carpetas anidadas, pero el workflow no; el paquete robot anidado no es despachable por el workflow vigente.
- `handoffs/grok_inbox/` contiene un marcador del robot con estado `pending`, no un recibo. No se infiere recepción a partir del marcador. No se disparó workflow ni se envió payload.

### Robot orbital — procesamiento preexistente

- `2026-11-09_dato-robot-ensambla-orbita` ya tiene en `main/cola/entrada/` medios, frames, subtítulos, QA, programación, `video_id` y `publishAt` del 21-nov 19:00. Clasificación: `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`.
- Los medios están verificados en la carpeta de `main`, pero no en la copia feature (`MEDIOS_VERIFICADOS_EN_MAIN_COLA_ENTRADA; NO_PRESENTES_EN_FEATURE`). El estado individual de Grok sigue sin archivo: `RECEPCION_GROK_NO_CONFIRMADA`.
- El storyboard conserva narrative QA PASS/90 y siete checks; el gancho concatenado tiene 17 palabras, por encima del límite contractual de seis. No se modificó porque ya existe procesamiento/publicación y no debe redispatcharse.

## Ocupación y reworks en main (solo lectura)

| Fecha | Ocupación |
|---|---:|
| 24-nov | 5/5 |
| 25-nov | 7/5 |
| 26-nov | 7/5 |
| 27-nov | 7/5 |
| 28-nov | 7/5 |
| 29-nov | 5/5 |

- `data/rehechos_2026-11-22.json` contiene nueve reworks con `programado_CDMX` y nuevo ID: dos por día del 25 al 28 y uno el 29. Se clasifican `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`.
- Los nueve storyboards/reworks del árbol `proyectos/2026-11-25_*` tienen metadata y `render.log`, pero no hay MP4 en el árbol GitHub. Clasificación de medios: `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`.
- Corrección de conteo: `data/resubidas_2026-11-21.json` tiene tres filas (dos programadas el 22-nov y una bloqueada el 23-nov). Los nueve elementos del 25–29 son reworks en `data/rehechos_2026-11-22.json`, no nueve filas de resubidas.
- `data/publicaciones.json` tiene 55 registros; dos coincidencias exactas con el lote 5–7 nov son Hielo y Nubes. `main/salidas/` también contiene salida de Hielo y una variante temática de árboles. No se duplica ni cancela ninguna publicación.
- No hay slot libre confirmado del 24 al 29. No se creó storyboard ni se promovió contenido.

## Issues, PRs y CI

- Issue #11 (Quásares): OPEN; etiqueta `hecho` no equivale a QA frío formal ni a merge.
- PR #3: OPEN/DRAFT, `mergeable=false`; rama feature muy divergente. No se fusionó.
- PR #13: OPEN/no merged; informe de auditoría de Quásares, sin CI y sin QA frío formal integrado.
- PR #14: OPEN/no merged; corrección de storyboard en rama separada. No se copió a feature ni se fusionó.
- PR #15: OPEN, head `947df50e1ee895e7744e54cc43f3865c78eedf13`; el head no tiene checks de CI asociados en esta consulta. No se atribuye a PR #15 el Semgrep de main.
- Último Semgrep de main observado: run `45364318369`, FAILURE, 37 hallazgos bloqueantes en 1,244 archivos. Último validador de feature observado: run `45278056293` SUCCESS sobre Kuroshio, no sobre el HEAD actual `44c7ee21`; no se declara CI verde del HEAD actual.

## Resultado del run

- No se creó storyboard ni `narrative_qa` nuevo.
- No se promovió, redispatchó ni modificó ninguna copia de cola; no se creó ni editó `cola/estado`.
- No se modificaron `data/*.json`, `main`, workflows, secretos, permisos, decisiones editoriales ni medios.
- Únicos cambios autorizados de este run: este control Markdown y la revalidación del radar 24-nov, ambos en `feature/capcot-video-discovery-continuity`.

## Revalidación adicional — 2026-11-24 06:27 CDMX (operador único, run 3)

### Rama, inventario y continuidad de QA

- HEAD de feature observado: `4012ef00e99fcbd6f78a2ec3a338d37e5ebc4956`. HEAD de main consultado en solo lectura: `05c62dd` (prefijo).
- Compare desde el HEAD registrado en este control (`44c7ee21`) hasta el HEAD actual: 10 commits adelantados, **ningún `proyectos/**/storyboard.json` modificado**. Los cambios fueron documentales y del validador/pruebas. Por ello se conservan los QA previos; no se repite PASS ni se atribuye una nueva auditoría narrativa.
- Árbol actual de feature: 90 storyboards en `proyectos/`, 56 storyboards bajo `salidas/`, 28 copias `storyboard.json` en bloqueados (61 rutas/artefactos en total bajo `cola/bloqueados/`). La cola contiene una sola carpeta anidada: `2026-11-09_dato-robot-ensambla-orbita`; no hay JSON plano en la raíz ni archivos en `cola/estado/`.
- **NOT_DISPATCHABLE:** la entrada anidada del robot no coincide con el selector del workflow, que escucha `cola/entrada/*.json` y busca con profundidad 1. Además, main contiene el paquete completo con `capsula.mp4`, nueve frames, portada, QA y programación; `data/publicaciones.json` registra el video `ZG4iQgmWrLI`, programado/publicado el 21-nov a las 19:00 CDMX. Clasificación: `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`; no duplicar ni cancelar.
- La ausencia de `cola/estado/<project_id>.json` conserva `RECEPCION_GROK_NO_CONFIRMADA`. No se creó ni modificó estado. En feature solo existe el marker histórico del robot; no hay marker de finalización.
- Los dos markers nuevos de Harris y evolución cuántica están únicamente en main, con `status=pending`, commit de paquete `3f9c1852` e Issues adicionales #1065/#1066 aún OPEN. No existe marker `grok_done` para ninguno; un marker pendiente y un Issue de asignación no prueban recepción ni entrega. No se enviaron payloads ni se despacharon workflows.

### Programación y producción preexistente

- `main/data/horarios.json` (SHA `226e...`) mantiene ventanas activas 06:30–07:30 y 16:30–18:00, slot fijo 23:30; 13:00–14:30 sigue en prueba y 19:00 debe evitarse salvo autorización puntual de Mj.
- Reconciliación de `main/data/miniaturas_auditoria_2026-11-21.json` y `main/data/rehechos_2026-11-22.json`: 24-nov 5/5 con colisión a las 17:00; 25–28 nov 7/5 por cinco programaciones preexistentes más dos reworks diarios a las 10:00/15:00; 29-nov 5/5 por cuatro programaciones más un rework. También hay colisiones de hora en 25 (07:00), 26 (17:00), 27 (07:00) y 28 (17:00). Los 19:00 heredados están fuera de la política actual, pero no se cancelan desde esta auditoría.
- Los nueve reworks tienen programación/plataformas y directorios en main con storyboard, metadata, licencias, créditos y render.log; el árbol GitHub no contiene sus MP4 ni portadas referenciados. Clasificación: `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR` y `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`. No hay slot libre confirmado hasta el 29-nov.
- `main/data/publicaciones.json`: 55 registros; `main/data/rotacion.json`: 39. No se modificó ningún `data/*.json`.

### Seguridad y validación

- `main/data/auditoria_hashtags_titulos_2026-11-24.json` sigue presente (blob `236f4c4d`, 443,162 caracteres). Contiene campos con valores tipo token y una referencia a un archivo local de credenciales; no se reproduce ningún valor. Gitleaks run `45337473897` detectó `generic-api-key` en línea 46, asociado al commit `052c2f9`.
- El Gitleaks posterior `45364318217` terminó SUCCESS, pero su log ejecuta `--log-opts=-1`, reporta un solo commit y aproximadamente 1.66 KB escaneados. **No limpia ni refuta el hallazgo anterior**; el archivo sigue en main. La revocación/rotación y limpieza histórica no se ejecutaron por requerir autorización sobre secretos/datos.
- Semgrep de main `45364318369`: FAILURE, 37 hallazgos bloqueantes en 1,244 archivos.
- Validador Kuroshio `45392906745`: SUCCESS sobre el commit `aabd4f58`, pero el workflow invoca `validar_storyboard.py` sin `--check-doi` y solo verifica el expediente Kuroshio. No acredita Crossref ni valida todos los storyboards ni el HEAD actual `4012ef00`. `tests/test_validar_storyboard.py` está en el HEAD actual, pero no hay una ejecución CI observada de esa suite.
- PR #15 continúa OPEN/no mergeable y declara sus pruebas unitarias pendientes. PR #3 continúa OPEN/DRAFT/no mergeable; PR #13 y #14 siguen OPEN. No se fusionó ni se cerró ningún PR.

### Resultado del corte

No se creó storyboard, no se registró narrative_qa, no se promovió ni redispatchó contenido, no se disparó workflow, no se generaron medios y no se consumieron créditos. Permanecen sin modificación main, `data/*.json`, secretos, permisos, estados Grok y decisiones editoriales.


## Revalidación RSS/Trends vinculada al control — 2026-11-24 06:27 CDMX

- Se reintentaron los 10 RSS científicos y Google Trends RSS México; los XML devolvieron errores de content-type/404/no accesible, documentados con detalle en `2026-11-24_RADAR_CAPCOT.md`.
- El respaldo HTML oficial de Trends mostró 174 tendencias en 24 horas; la primera página no aportó tema admisible. No se añadió candidato ni se seleccionó un tema por fuerza.
- Radar actualizado y releído en feature: commit `aebbcddb81c9bca1d087bd4d0d8853caec04cc3b`, blob `b3e2d90c19c4c0715543add4dfff4bd70c13533f`. Sin storyboard, sin QA narrativo y sin promoción.


## Revalidación del operador único — 2026-11-24 08:08 CDMX

### Radar y backlog
- El radar del 24-nov fue actualizado por la ejecución independiente de investigación y releído desde GitHub: commit `bd8ab61e5760ab1d6fa441506184a7c5c3edc911`, blob `313e23805c2b62a26dd3d67907b04559b5a93d65`.
- Se registran cinco candidatos recientes. El estudio sobre extracción oceánica de CO₂ queda como recomendación para un futuro slot libre, no como selección. Los DOI/Crossref no quedaron resueltos; Varroa conserva texto primario completo con resolvedor pendiente; los demás mantienen límites de lectura o `PENDING_SOURCE`. No se redactó storyboard.
- La relectura del radar confirma 32 storyboards: 12 PASS y 20 FAIL. Los 32 archivos individuales `cola/estado/<project_id>.json` devolvieron 404; para todos corresponde `RECEPCION_GROK_NO_CONFIRMADA`. No se creó ni modificó ningún estado.
- No hay storyboard nuevo para 24-nov: el cupo sigue agotado. No se creó cola, no se disparó dispatch y no se generaron medios.

### Reconciliación de main
- HEAD actual de CAPCOT main: `3cbc18edf321c89593bc325f479b045b32291fc3`. La comparación con el commit anterior `fb6d35e8` muestra que el cambio posterior fue `data/endscreens_rotacion.json`; no cambió la programación revisada.
- `data/publicaciones.json`: 62 registros, tres con fecha 24-nov. `data/rotacion.json`: 39 registros. Ambos permanecen solo lectura.
- `data/horarios.json` conserva ventanas activas 06:30–07:30 y 16:30–18:00, con dato fijo 23:30. La programación preexistente continúa: 24-nov 5/5; 25–28 nov 7/5 por cinco programaciones más dos reworks diarios; 29-nov 5/5. Los nueve reworks están a las 10:00/15:00, fuera de las ventanas activas. Persisten las colisiones de 24–28 ya descritas. No hay slot libre confirmado.

### QA narrativo y PRs
- PR #13 no satisface la auditoría en frío exigida: su `AUDITORIA.md` cita líneas del storyboard, estado DOI, metadatos y narrativa_qa, por lo que no demuestra lectura aislada de la narración concatenada. PR #14 conserva el `FAIL/82` histórico; no hay una nueva revisión independiente posterior a sus correcciones. Quásares no es promovible.
- PR #3 sigue OPEN/DRAFT y no mergeable. Su HEAD es `bd8ab61e`; el listado completo muestra 706 archivos modificados, incluidos 13 `data/*.json`. No se fusiona. El run #45410383610 fue CodeQL, no una validación estructural/DOI de los storyboards.
- PR #15 sigue OPEN/no mergeable. Su parche añade seis pruebas para coordenadas booleanas, bounds y fijación de HTTPS/Crossref; no hay ejecución CI de ese head y no se ejecutó la suite local. No se atribuye PASS.

### Seguridad
- El archivo `main/data/auditoria_hashtags_titulos_2026-11-24.json` sigue presente en main (blob prefijo `236f4c4d`, 447,466 bytes); no se reproduce ningún valor sensible.
- Gitleaks run [#45410242032](https://github.com/marcojpad-hash/capcot-capsulas-imaginantes/actions/runs/45410242032) terminó SUCCESS sobre HEAD `3cbc18e`, pero el log usa `--log-opts=-1`, informa un commit y ~85.90 KB escaneados. No vuelve a examinar el historial ni refuta el hallazgo anterior #45337473897; el archivo señalado no cambió en el commit analizado.
- Semgrep run [#45410242244](https://github.com/marcojpad-hash/capcot-capsulas-imaginantes/actions/runs/45410242244): FAILURE, 37 hallazgos bloqueantes, 361 reglas y 1,248 objetivos.
- No se rotaron secretos, no se editó `data/*.json`, no se escribió en main y no se cambió ningún permiso.

### Cierre de esta revalidación
No se promovió ni redispatchó contenido. El radar queda como investigación, no selección; el slot queda agotado; los 32 recibos Grok siguen sin confirmación. La alerta Gitleaks y el bloqueo Semgrep permanecen abiertos.
