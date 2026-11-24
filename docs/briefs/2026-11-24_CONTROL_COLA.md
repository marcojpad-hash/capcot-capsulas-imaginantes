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


## Reconciliación posterior — 2026-11-24 10:00 CDMX

### Autoridad de datos y cambios desde el corte anterior
- HEAD de `main` releído: `a450e6273d1bafc4a1fc5099cf69e959dbfde91f` (24-nov, 14:20:23Z). HEAD de esta rama feature: `b59425a3b52e30b8c170cfdd736fa15dd58d3a6c`.
- La comparación desde el HEAD documentado en el corte de 06:27 registra 15 commits en feature y no muestra cambios bajo `proyectos/` ni storyboards. No se repitieron QA narrativos ni se atribuyeron borradores nuevos.
- Para la programación se tomó `main` como autoridad de solo lectura: `data/horarios.json` (actualización 23-nov), `data/tt_fb_alineacion_2026-11-24.json`, `data/miniaturas_auditoria_2026-11-21.json`, `data/rehechos_2026-11-22.json`, `data/publicaciones.json` y `data/rotacion.json`. La copia de `data/` en feature está desfasada respecto de main.
- `publicaciones.json`: 62 registros; `rotacion.json`: 39. `miniaturas_auditoria` contiene 36 programaciones revisadas y `rehechos` contiene 9 reworks. La rotación no representa por sí sola la parrilla futura del 25–29; se contrastaron los snapshots específicos.

### Corrección de conteo y colisiones
La cifra anterior de **24-nov 5/5 queda corregida y supersedida**: el snapshot `tt_fb_alineacion_2026-11-24.json` contiene 8 IDs únicos de YouTube para el día, frente al máximo `MAX_POR_DIA=5`:
- Dos publicados en la ventana de 07:00.
- Uno preexistente programado a las 17:00.
- Cinco pendientes en el snapshot a las 13:30, 15:00, 17:00, 19:00 y 23:30.
- Hay dos colisiones de hora: 07:00 (dos publicaciones) y 17:00 (dos videos programados). La lista `colisiones_horario_mismo_publishAt` de miniaturas solo registra la de 17:00; la de 07:00 se detecta al cruzar con `publicaciones.json` y el snapshot de alineación. Es una omisión del inventario de colisiones.
- 13:30 está fuera de la ventana activa (solo aparece como ventana de prueba), 15:00 y 19:00 están fuera de las ventanas activas; 23:30 es el slot fijo.

Recuento reconciliado:
- 24-nov: **8/5**, con dos colisiones de hora.
- 25–28 nov: **7/5 cada día** (cinco programaciones base, incluidas las colisiones documentadas, más dos reworks a las 10:00 y 15:00).
- 29-nov: **5/5** (cuatro programaciones base y un rework).
- Ventanas activas en `main/data/horarios.json`: 06:30–07:30 y 16:30–18:00; slot fijo 23:30. Los reworks de 10:00/15:00 y las programaciones a 13:30/19:00 no pertenecen a las ventanas activas.
- No hay slot libre confirmado. No se canceló, reprogramó ni duplicó ninguna publicación.

### Handoffs y recepción
- La carpeta `cola/estado/` no existe en feature; los 32 IDs auditados en el corte anterior siguen sin un archivo de estado individual y sus storyboards no cambiaron en los commits comparados. Estado: `RECEPCION_GROK_NO_CONFIRMADA`; ningún marcador de handoff se toma como recibo.
- Issues #1065 (Thomas Harris) y #1066 (evolución cuántica) siguen abiertos en `agente-cero-costo`; sus marcadores de `handoffs/grok_inbox/` continúan `pending`. No se declara recepción ni entrega completada.
- El paquete orbital en `main/cola/entrada/2026-11-09_dato-robot-ensambla-orbita/` conserva procesamiento y publicación preexistentes. `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`; no se despachó de nuevo.

### Seguridad y CI — nueva evidencia
- Gitleaks run [#45414450492](https://github.com/marcojpad-hash/capcot-capsulas-imaginantes/actions/runs/45414450492), sobre `main` HEAD `a450e627`: escaneó 2,147 commits y ~19.06 MB; FAILURE, **3 hallazgos `generic-api-key`**:
  1. `data/diagnostico_bajas_vistas_2026-11-23.json`, línea 9, commit `20f9ea52959622645d3a832fcf863fff5e95260e`.
  2. `data/auditoria_hashtags_titulos_2026-11-24.json`, línea 46, commit `052c2f9725250dee9440ab4492b1e7c9fc72ab3a`.
  3. `docs/SKILL_DRAFT_capsula_diaria.md`, línea 17, commit `a4ccf1974a8966d5801a991ac25609ef4d7cdca7`.
- Los dos hallazgos en `data/` contienen una referencia al token local de CAPCOT; el tercero está en un ejemplo de comando y requiere triage. Los valores no se copiaron. La credencial no fue revocada ni rotada; no se editaron `data/*.json`, secretos ni historial.
- Semgrep run [#45412987352](https://github.com/marcojpad-hash/capcot-capsulas-imaginantes/actions/runs/45412987352), mismo HEAD de main: FAILURE, 37 hallazgos bloqueantes en 1,248 objetivos.
- PR #3 sigue OPEN/DRAFT, 706 archivos, 84,518 adiciones y 1,699 eliminaciones; `mergeable=false`, estado `dirty`. CodeQL y Analyze (Python/Actions) aprobaron el HEAD `b59425a`, pero esos checks no acreditan estructura/DOI ni resuelven conflictos.
- PR #15 sigue OPEN/no mergeable, con dos archivos y seis pruebas nuevas. En su HEAD `947df50`, Semgrep OSS terminó SUCCESS y Semgrep terminó FAILURE; no aparece una ejecución de pytest en sus checks. No se atribuye PASS a las 14 funciones de prueba del archivo.

### Cierre de esta reconciliación
No se creó storyboard ni cola, no se registró narrative_qa, no se disparó workflow, no se enviaron payloads, no se generaron medios y no se consumieron créditos. `main` y `data/*.json` permanecen sin cambios. La rotación/triage de credenciales y la remediación de Semgrep siguen siendo acciones de seguridad separadas; no se tocaron secretos ni permisos.


## CI posterior a la actualización documental — 2026-11-24 10:00 CDMX

- HEAD de feature verificado después de los dos commits de documentación: `0effc37f11309a084c7cb80d74982f7d58d14471`.
- PR #3 recibió dos ejecuciones posteriores: [#45436538575](https://github.com/marcojpad-hash/capcot-capsulas-imaginantes/actions/runs/45436538575) y [#45436549625](https://github.com/marcojpad-hash/capcot-capsulas-imaginantes/actions/runs/45436549625). En ambas terminaron SUCCESS los jobs `Analyze (python)` y `Analyze (actions)`.
- Estos jobs son análisis estático; no ejecutan `validar_storyboard.py --check-doi`, no hacen QA narrativo en frío y no resuelven el estado `dirty`/no mergeable de PR #3. No se atribuye validación estructural ni DOI.
- No hubo cambios en `main`, `data/*.json`, storyboards, cola ni estados Grok por estas ejecuciones.


## Corte operativo complementario — 2026-11-24 10:28 CDMX

Este corte **supersede el conteo inicial de 24-nov 5/5** que aparece en una sección anterior: el cruce de snapshots de YouTube, resubidas y programación devuelve **8 ocupaciones frente a MAX_POR_DIA=5**.

### Estado de ramas y cambios posteriores a la auditoría

- feature/capcot-video-discovery-continuity HEAD: b04f269ad8663a7e20532f70327720b24f196bc0.
- main HEAD: a450e6273d1bafc4a1fc5099cf69e959dbfde91f.
- Compare actual: feature 1368 commits ahead / 569 behind, estado diverged; no integrar ni sincronizar por esta vía.
- Desde la última auditoría 7777ce2, el compare muestra 31 commits adicionales y no reporta cambios en proyectos/**/storyboard.json. Por eso no se repitieron QA narrativos que siguen ligados a narraciones sin cambios.
- Sí cambió data/endscreens_rotacion.json en feature, commit 9cdd371, aunque data/*.json es de solo lectura. La copia de feature indica 2026-11-23T16:30; la de main indica 2026-11-24 08:05 y contiene snapshots posteriores. No se corrigió ni sobrescribió; queda registrada la discrepancia de una copia de datos modificada y atrasada respecto de main.

### Inventario, cola y Grok

- Última auditoría completa: 103 directorios de proyecto y 90 storyboards.
- Backlog 24–30 oct: 31 storyboards sin narrative_contract ni narrative_qa; siguen sin compuerta narrativa verificable.
- Lote 5–7 nov: 12 IDs; 2 PASS y 10 FAIL. Se mantienen 510 campos dramáticos ausentes y 75 escenas con SFX vacío. Sin cambios de narración desde la auditoría anterior.
- Proyectos 23-nov: supersequias-722-eventos y tropical-biodiversity-turnover, ambos FAIL/82; no se repitió el QA porque no cambió su narración.
- Último inventario: 27 recepciones Grok no confirmadas. cola/estado/ no está disponible en feature; no se infiere recepción desde GitHub.
- main/handoffs/grok_inbox/ contiene marcadores para robot orbital, Thomas Harris y evolución cuántica; los dos últimos están en estado pending. feature/handoffs/grok_inbox/ solo contiene el marcador orbital. grok_done/ contiene únicamente .gitkeep. Los Issues #1065 y #1066 siguen abiertos; los marcadores no son recibos de Grok.
- main/cola/entrada/ contiene 32 directorios anidados; feature conserva el directorio anidado del robot orbital. cola/bloqueados/ contiene 47 entradas y salidas/ 59. La ruta del workflow busca exclusivamente cola/entrada/*.json en profundidad 1; el paquete orbital anidado es procesamiento preexistente y no es dispatchable. DISPATCHABLE: ninguno nuevo. NOT_DISPATCHABLE: paquetes anidados, bloqueados o sin estado Grok confirmado.
- El webhook del workflow actual es opcional; no se consultaron valores de secretos. No se disparó workflow ni se envió payload.

### Programación corregida

- 24-nov: 8/5. Colisiones verificadas a las 07:00 (dos publicaciones) y 17:00 (dos ocupaciones); 13:30, 15:00 y 19:00 quedan fuera de ventanas ordinarias; 23:30 es slot fijo.
- 25–28 nov: 7/5 por día.
- 29-nov: 5/5.
- No hay slot libre autorizado; no se creó storyboard ni copia de cola.
- La auditoría de 12 IDs canónicos encontró coincidencia exacta de publicación para solo 2; las demás referencias incluyen variantes o regrabaciones. No contar nueve reworks como nueve IDs canónicos publicados.

### Validador, CI y PRs

- El código actual de scripts/validar_storyboard.py ya incluye --check-doi para Crossref/doi.org o URL primaria, y se añadieron pruebas en tests/test_validar_storyboard.py. No hay ejecución de esas pruebas en el HEAD actual.
- Kuroshio run #45392906745 usó el commit anterior aabd4f5 y ejecutó python scripts/validar_storyboard.py ... sin --check-doi; pasó estructura y contrato storyboard_only, pero no verifica DOI ni narrative_qa.
- PR #3 sigue OPEN/draft/no mergeable, 706 archivos modificados; el compare con main sigue divergente.
- PR #13 sigue OPEN, con auditoría independiente de cuásares en una rama aparte; Issue #11 continúa OPEN pese a la etiqueta hecho. Ese documento no sustituye la lectura en frío solo de narración exigida por el contrato vigente.
- PR #14 sigue OPEN contra main y conserva asset_filename, incompatible con el contrato de preproducción.
- PR #15 sigue OPEN/no mergeable; Semgrep falló en su HEAD y no hay ejecución pytest verificable para sus seis pruebas nuevas.

### Seguridad

- En main HEAD a450e627, data/auditoria_hashtags_titulos_2026-11-24.json conserva un valor con patrón de credencial en línea 46. Gitleaks #45414450492 terminó FAILURE. No se reproduce el valor.
- Semgrep #45412987352 terminó FAILURE con 37 hallazgos bloqueantes.
- No se modificaron main, data/*.json, secretos, permisos, programación, salidas ni estados Grok.


## Actualización de main posterior al corte 10:28 — 2026-11-24 10:40 CDMX

### Nuevo paquete de 24-nov, solo lectura

- main avanzó a HEAD 0c5374e692a461b55a545c7a0cf5d12a616dbc88 mediante el commit «Paquete 2026-11-24_magnetismo-p-wave-eusi ... 17:15 CDMX».
- Añadió el mismo storyboard a proyectos/ y a cola/entrada/ en un directorio anidado. La cola main pasa de 32 a **33 directorios**. La copia de proyecto y la de cola tienen el mismo blob SHA.
- programacion.json declara publish_at 2026-11-24T23:15:00Z / 17:15 CDMX, YouTube y TikTok, estado programado_para_publicar. La nota dice que falta montar el MP4. Esto es una programación documental previa, no prueba de que Studio tenga el video programado.
- No existe ESTADO_EJECUCION.md, cola/estado/<id>.json, salida ni copia en bloqueados. Recepción Grok no confirmada.
- El workflow solo acepta JSON plano directamente bajo cola/entrada/*.json; este paquete está anidado. NOT_DISPATCHABLE. Por tener programación previa y copia en cola: PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR. Por faltar MP4 en el árbol: MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO.
- El paquete añade **una ocupación planificada** a las ocho ocupaciones ya verificadas del 24-nov: 9/5 planificadas. No afirmo que las nueve estén confirmadas en Studio. El slot 17:15 está dentro de la ventana tarde, pero no es el mismo slot_local que 17:00; no se marca colisión exacta entre ramas. Sí aumenta la sobrecapacidad diaria.
- El compare actual entre main 0c5374e y feature 2dfd7c5 está diverged: feature 1370 commits ahead y 571 behind. No sincronizar ni integrar.

### QA en frío — magnetismo p-wave / EuSi

Lectura independiente realizada sobre la narración concatenada únicamente, sin título, resumen, arco, notas ni narrative_contract. El DOI 10.1038/s41586-026-11295-9 resuelve a la ficha primaria de Nature, publicada el 18-nov-2026; el artículo respalda la fase espiral 33.4–62 K, la reconstrucción electrónica >100 meV y la señal spin-ARPES de textura p-wave.

Registro de auditoría de esta pasada (no escrito en main por la regla SOLO_CONSULTA):

- status: FAIL
- score: 25
- review_basis: lectura_en_frio_solo_narracion
- pregunta_central_reconstruible: false
- apertura_in_medias_res: false
- progresion_por_escena: false
- transiciones_causales: false
- giro_cientifico_explicado: true
- limite_evidencia_explicito: false
- payoff_cierre_apertura: false
- critical_flags: GANCHO_DEFINICIONAL; STAKES_NO_EXPLICADOS; PROGRESION_NO_DRAMATICA; TRANSICIONES_CAUSALES_AUSENTES; LIMITE_EVIDENCIA_AUSENTE; PAYOFF_NO_PAGA_APERTURA; LONGITUD_Y_ESCENAS_FUERA_DE_CONTRATO.

Comprobaciones estructurales:
- 6 escenas y 121 palabras; contrato exige 7–9 escenas y 170–235 palabras.
- target_duration_seconds declara 85, pero 121 palabras a 120–140 ppm equivalen aproximadamente a 52–61 s de voz; sumando 6 s de cortinilla, el total estimado es 58–67 s, no 85. Es una estimación, no duración medida.
- Las seis escenas carecen de dramatic_beat, scene_function, causal_bridge_from_previous, question_state, reason_to_continue y new_information.
- narrative_contract y narrative_qa ausentes.
- map y prompt_base ausentes.
- approved_assets ausente; export.filename está presente y export.render_status no está declarado. Ambos contradicen el contrato de preproducción.
- Voz es-MX-JorgeNeural, +7%, -2Hz: coincide con el perfil solicitado.
- No se encontraron medios montados; programacion.json indica que falta el MP4.

No se modificó main ni el paquete. El resultado no autoriza publicación, promoción ni redispatch.

### Seguridad posterior al nuevo commit

- Gitleaks #45439255464 terminó SUCCESS sobre el último commit, pero la línea 46 del archivo de auditoría sigue conteniendo un valor con patrón de credencial. El éxito del escaneo del último commit no elimina la exposición ni limpia el historial.
- Semgrep #45439255716 terminó FAILURE.
- No se revocaron secretos ni se alteraron datos.


### Precisión de Gitleaks — 2026-11-24

Se leyó el log de [run #45439255464](https://github.com/marcojpad-hash/capcot-capsulas-imaginantes/actions/runs/45439255464). El comando usa --log-opts=-1 y el log confirma literalmente **1 commits scanned**, ~15.92 KB y no leaks found. El commit escaneado fue 0c5374e, que solo añadió el paquete de magnetismo; no volvió a escanear la línea 46 del archivo de auditoría. Por tanto, el SUCCESS no limpia ni invalida el hallazgo anterior. La copia actual de main sigue conservando el valor con patrón de credencial en esa línea.


### Cierre de referencias — 2026-11-24 10:42 CDMX

- HEAD final de feature después de las actualizaciones de control y radar: f6015de0c4deebbb3d54d3297f404a73e0ee0980.
- main permanece en 0c5374e692a461b55a545c7a0cf5d12a616dbc88.
- Compare final: feature 1372 commits ahead y 571 behind; ramas diverged.
- PR #3 sigue OPEN, draft, no mergeable y con 706 archivos modificados.
- No apareció ejecución nueva del workflow de preproducción ni del dispatch en feature después de los commits documentales. El último run sigue siendo #45392906745 sobre aabd4f5, anterior al validador con --check-doi y sin esa bandera.
- Los dos documentos de esta corrida se releen en GitHub: CONTROL_COLA y RADAR_CAPCOT. No se modificó ningún storyboard, data/*.json, main, secreto, estado Grok ni medio.


## Revalidación operativa posterior al corte 10:42 — 2026-11-24 12:00 CDMX

### Autoridad de ramas y cambios nuevos en main

- **main HEAD:** `a24d5ee2ad7f8a640d563ca8dda2cf96961638e0`.
- Desde el HEAD anterior `0c5374e692a461b55a545c7a0cf5d12a616dbc88` entraron dos commits: `424908ae` (`pantallas ... pendiente_studio`) y `a24d5ee2` (`pantallas ... aplicadas en Studio (8/9, flamenco omitido)`). Ambos modifican únicamente `data/endscreens_rotacion.json`.
- **Corrección de interpretación:** el 8/9 del mensaje de commit se refiere a asignaciones de pantallas finales, no a ocho de nueve videos publicados o programados. El archivo de main registra actualización 2026-11-24 11:07; la copia de feature conserva el corte 2026-11-23 16:30. `data/*.json` sigue en solo lectura; no se sincronizó.
- **feature HEAD del PR #3:** `a4f8f1078ef787b8a45925685e45bdba24c4717b`. PR #3 continúa OPEN, draft y `mergeable=false`, con 706 archivos declarados. Compare main→feature: 1,373 commits ahead y 573 behind; ramas divergentes. No sincronizar ni integrar.

### Paquete preexistente de magnetismo p-wave / EuSi

Se releyeron las copias de proyecto y cola en main:

- `proyectos/2026-11-24_magnetismo-p-wave-eusi/storyboard.json` y `cola/entrada/2026-11-24_magnetismo-p-wave-eusi/storyboard.json` tienen el mismo blob SHA `74ae31789be2d69ad984ee47a768ee21f6e525b8`; no cambió desde el QA anterior.
- La narración conserva 6 escenas y 121 palabras. No se repitió la lectura en frío.
- `programacion.json` conserva `publish_at=2026-11-24T23:15:00Z` (17:15 CDMX), plataformas YouTube/TikTok y `estado=programado_para_publicar`; la misma nota dice que falta montar el MP4. Es un registro documental de programación, no una verificación en Studio.
- `cola/estado/2026-11-24_magnetismo-p-wave-eusi.json` devuelve 404: `RECEPCION_GROK_NO_CONFIRMADA`.
- `salidas/2026-11-24_magnetismo-p-wave-eusi/` no existe; no se encontró MP4 en el árbol: `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`.
- El paquete está dentro de un directorio anidado, no como `cola/entrada/<id>.json`. El workflow `.github/workflows/capcot-grok-dispatch.yml` usa `find cola/entrada -maxdepth 1 -type f -name '*.json'` y el filtro de push `^cola/entrada/[^/]+\.json$`. Por ruta, **NOT_DISPATCHABLE**.
- El registro de programación y la copia heredada en cola hacen que aplique **PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR**. No se movió ni duplicó nada en main.

### Worker y seguridad

- Worker de cola [run #45447043932](https://github.com/marcojpad-hash/capcot-capsulas-imaginantes/actions/runs/45447043932), 2026-11-24 11:18 CDMX: SUCCESS. El log dice literalmente `[trabajador] sin trabajo en cola.` Esto es coherente con que el paquete nuevo no sea un JSON plano en el nivel que selecciona el worker; no demuestra que no existan directorios anidados.
- Gitleaks [run #45446747688](https://github.com/marcojpad-hash/capcot-capsulas-imaginantes/actions/runs/45446747688): SUCCESS, pero el comando usa `--log-opts=-1`; el log confirma **1 commit scanned**, ~109.96 KB y `no leaks found`. No vuelve a escanear la línea 46 del archivo de auditoría ni limpia el historial. El hallazgo histórico `generic-api-key` sigue abierto; no se muestra ni modifica el valor.
- Semgrep [run #45446747766](https://github.com/marcojpad-hash/capcot-capsulas-imaginantes/actions/runs/45446747766): FAILURE, 37 hallazgos bloqueantes en 1,253 archivos; 37 archivos mayores de 1 MB fueron omitidos por el escáner.
- Callback [run #45450386352](https://github.com/marcojpad-hash/capcot-capsulas-imaginantes/actions/runs/45450386352): SUCCESS; el log muestra `pending = []`, sin nuevas tareas callback que crear.

### Programación del 24-nov y recepción

- El snapshot de alineación registra 2 IDs publicados a las 07:00, 1 ID programado a las 17:00 y 5 IDs privados programados en 13:30, 15:00, 17:00, 19:00 y 23:30: **8 IDs existentes**. El paquete EuSi añade un noveno registro planificado a las 17:15. Es una sobrecapacidad documental de 9 frente al límite 5; no equivale a 9 confirmaciones en vivo de Studio.
- Issues [#1065](https://github.com/marcojpad-hash/agente-cero-costo/issues/1065) y [#1066](https://github.com/marcojpad-hash/agente-cero-costo/issues/1066) siguen abiertos. Los archivos del bus tienen versión 8 y tipo `indicacion`; no son recibos de ejecución. No se encontró confirmación individual Grok ni marcador `grok_done` que permita cambiar el estado.
- No se creó storyboard nuevo, no se promovió paquete, no se disparó dispatch, no se modificó main, `data/*.json`, programación, secreto, permiso, estado Grok ni medio.


### Verificación de marcadores de handoff — 2026-11-24 12:00 CDMX

- `handoffs/grok_inbox/2026-11-24_serie_thomas_harris.json`: `status=pending`, receipt `repo-2026-11-24_serie_thomas_harris-3f9c18520fc6`, asociado a Issue #1065.
- `handoffs/grok_inbox/2026-11-24_serie_cuantica_evolucion.json`: `status=pending`, receipt `repo-2026-11-24_serie_cuantica_evolucion-3f9c18520fc6`, asociado a Issue #1066.
- `handoffs/grok_done/` devuelve 404. No existe evidencia de cierre de ninguno de los dos handoffs; los marcadores `pending` no son acuses.
- El marcador heredado `handoffs/grok_inbox/2026-11-09_dato-robot-ensambla-orbita.json` también conserva `status=pending`; su nota declara que faltan frames. Las rutas consultadas `proyectos/<id>/programacion.json` y `salidas/<id>/` devolvieron 404. No se infiere producción ni publicación a partir de ese marcador.


---

## Corte operador único — 2026-11-24, 14:00 CDMX

### CAPCOT — corrección de validador y verificación
- **EJECUTADO:** `scripts/validar_storyboard.py` ahora rechaza booleanos como lat/lon, RA/Dec y bounds (Python trata `bool` como subclase de `int`); centraliza `validar_bounds_mapa`; consulta solo hosts HTTPS fijos `api.crossref.org` y `doi.org`, usa el contexto TLS predeterminado y no sigue redirecciones del resolvedor.
- **EJECUTADO:** se añadieron regresiones para coordenadas booleanas, bounds, DOI inválido, TLS verificado y fallback a doi.org. Commits de la rama: validador `08d5cc016d69c59b5ad1f0aae0b2e3dbb50e14c3`; pruebas `05be0c168e312d605e032909b0b7803b7f325136`.
- **VERIFICADO por lectura de vuelta:** los dos archivos contienen los cambios. Nueve pruebas aisladas de la lógica copiada del validador pasaron en Python. Esto no equivale a ejecutar el archivo completo de tests del repositorio.
- **CI VERIFICADO:** `validar-kuroshio` run [#45477532530](https://github.com/marcojpad-hash/capcot-capsulas-imaginantes/actions/runs/45477532530), SUCCESS sobre el commit del validador `08d5cc0`; ejecutó el validador de Kuroshio. El commit posterior que añadió los tests `05be0c1` no quedó incluido en ese run; suite unitaria completa **PENDIENTE**.
- PR #15 continúa OPEN y no mergeable; su corrección quedó portada directamente a la rama de trabajo. PR #3 continúa OPEN/DRAFT, 706 archivos y no mergeable. No se hizo merge ni se cerró ningún PR.
- Semgrep run [#45474972177](https://github.com/marcojpad-hash/capcot-capsulas-imaginantes/actions/runs/45474972177): 37 hallazgos bloqueantes; el log no incluye ubicaciones individuales y no se publicó SARIF (artifacts=[]). No se aplicaron cambios a ciegas.
- Gitleaks run [#45474974235](https://github.com/marcojpad-hash/capcot-capsulas-imaginantes/actions/runs/45474974235): SUCCESS, sin hallazgo de secreto en el commit escaneado.
- Worker run [#45447043932](https://github.com/marcojpad-hash/capcot-capsulas-imaginantes/actions/runs/45447043932): SUCCESS, log indica que no encontró trabajo en cola.
- No se disparó el workflow de Grok ni se envió payload.

### CAPCOT — inventario main y auditoría nueva
- Main HEAD verificado: `6bce6166d424a8a793a81e1f44cbc71031c88462`. La comparación desde `4860fa4` solo cambió `data/endscreens_rotacion.json`; no aparecieron storyboards nuevos después de ese commit.
- Se corrigió el conteo de publicaciones del control anterior: `data/publicaciones.json` tiene **62**, `data/rotacion.json` **39**, `data/cola.json` **0**. El conteo previo de 52 publicaciones era incorrecto.
- Se auditó el nuevo paquete de main: nueve proyectos rehechos del 25–29 nov. La auditoría en frío externa, los siete checks, scores, defectos estructurales, programación preexistente, 404 de `cola/estado` y medios no verificables quedaron en [AUDITORIA_MAIN_REHECHOS_25.md](2026-11-24_AUDITORIA_MAIN_REHECHOS_25.md). No se promovió ninguno.
- Los nueve rehechos ya tienen `programado_CDMX`, IDs de YouTube y programación TT/FB en `data/rehechos_2026-11-22.json`: **PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR**. Los horarios 10:00/15:00 están fuera de las ventanas vigentes; no se cancelaron ni reprogramaron. Los MP4/portadas que el registro ubica en workspace no están verificables en el árbol GitHub.
- `2026-11-24_yo-soy-sam` ya tiene publicación YT/TT/FB, pero carece de storyboard/fuentes y comparte 07:00 con `purpura-no-piedras`: **PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR**; medio no verificable en repo; además está fuera de la línea editorial de Datos y ociosidades.
- `2026-11-24_magnetismo-p-wave-eusi` tiene copia anidada en `cola/entrada/`, programación 17:15 y nota de que falta montar MP4. El selector del workflow solo toma JSON plano raíz; `cola/estado` dio 404. Queda **NOT_DISPATCHABLE**, **RECEPCION_GROK_NO_CONFIRMADA**, **PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR** y **MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO**.
- Se verificaron colisiones de slots 24–28 nov. 24: 07:00 (Yo soy Sam/Púrpura) y 17:00 (Pollo/Vomitorium); 25: 07:00; 26: 17:00; 27: 07:00; 28: 17:00. Los días 25–28 tienen seis horas ocupadas (07:00, 10:00, 13:30, 15:00, 17:00, 19:00) frente a máximo cinco; el slot fijo 23:30 está reservado pero no tiene proyecto individual identificado. El 29 tiene cinco horas ocupadas.
- Los 12 IDs del lote 5–7 nov conservan el último resultado documentado (2 PASS/10 FAIL); no hubo cambios de storyboard en la rama de trabajo desde la auditoría previa, así que no se repitió PASS ni se reescribió QA.
- No se modificaron main, data/*.json, storyboards de main, cola, estados Grok, medios, programación ni publicaciones.

### CAPCOT — radar, RSS y DOI
- Se intentó de nuevo el acceso a feeds: Nature RSS devolvió `DisabledError`; ScienceDaily `Unsupported content-type: application/xml`; NASA `Unsupported content-type: application/rss+xml`; EurekAlert y Google Trends MX devolvieron `URL not accessible via this tool`. No se cambió el contenido de `data/*.json`.
- La búsqueda oficial de respaldo mantiene cinco candidatos en el radar; dos DOI tienen verificación disponible (APS, 21-nov; Nature Astronomy, 20-nov). Los DOI de HK97, lunar y pecio romano no devolvieron una coincidencia exacta verificable en esta pasada; quedan **PENDING_SOURCE**. Las llamadas directas a Crossref API tampoco fueron accesibles desde esta interfaz.
- No hay slot libre autorizado; no se creó storyboard nuevo ni se seleccionó candidato para producción.

- El cambio de main en `data/endscreens_rotacion.json` deja una asignación nueva marcada `pendiente_studio=true`; no se aplicó en YouTube Studio ni se realizó acción externa.


## Revalidación del operador único — 24-nov-2026, 14:27 CDMX

### Diferencias desde el corte anterior

- `feature/capcot-video-discovery-continuity` estaba en HEAD `0343f45`. La comparación desde el corte anterior mostró cuatro commits de documentación; no cambiaron storyboards, cola, estados, medios ni `data/*.json`. Este run agregó el radar de investigación en commit `c09fe00a8f38eab110dc0a7a37e01bd8cea8b77e`.
- `main` estaba en HEAD `269e0da`. La comparación con el corte anterior solo mostró `data/endscreens_rotacion.json`; no apareció un storyboard nuevo ni cambió la cola o la parrilla.
- Se leyeron los 20 JSON de `data/` en la rama de trabajo como solo lectura. En `main` se releyeron horarios, publicaciones, rotación, miniaturas y plan semanal. No se escribió ningún JSON de datos.

### Inventario, recepción y cola

- La rama de trabajo conserva 90 storyboards en `proyectos/`; no hay storyboard nuevo desde el corte anterior.
- `cola/entrada/` de la rama de trabajo conserva cero JSON planos y un único paquete anidado heredado, `2026-11-09_dato-robot-ensambla-orbita`. `cola/estado/` no existe. `cola/bloqueados/` conserva 47 entradas; `salidas/`, 59 entradas. `handoffs/grok_inbox/` contiene el marcador pendiente del robot y `handoffs/grok_done/` solo `.gitkeep`.
- Se consultaron los doce IDs exactos del lote 5–7 nov definidos en `ajustes_entre_modelos/PARA_CHATGPT_5-7nov_PASS_auditor.md`. Los doce `cola/estado/<id>.json` devolvieron 404; se registra `RECEPCION_GROK_NO_CONFIRMADA` para cada uno. Se conserva el resultado de la última lectura fría: 2 PASS y 10 FAIL. No se repitió QA ni se promovió nada porque no cambió ninguna narración.
- En `main`, `cola/entrada/` contiene 33 entradas. `proyectos/2026-11-24_magnetismo-p-wave-eusi/storyboard.json` y su copia en cola tienen el mismo SHA; `programacion.json` fija `publish_at=2026-11-24T23:15:00Z` (17:15 CDMX), ventana tarde y `estado=programado_para_publicar`. La nota de programación dice que falta montar el MP4. No existe `ESTADO_EJECUCION.md`, `cola/estado/2026-11-24_magnetismo-p-wave-eusi.json` devuelve 404 y `salidas/2026-11-24_magnetismo-p-wave-eusi/` devuelve 404; el árbol del proyecto solo contiene `fuentes.md`, `programacion.json` y `storyboard.json`, sin frames ni MP4. El storyboard tiene 6 escenas, 121 palabras narradas y 65 s sumados en escenas frente a `target_duration_seconds=85`; contiene `asset_filename` en las seis escenas y `export.filename=capsula.mp4`, carece de `narrative_qa` y no cumple el contrato de preproducción. Clasificación: `NOT_DISPATCHABLE`, `PROCESSING_PREEXISTENTE_NO_REDISPATCHAR` por cola/programación heredada y `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`. No se declara `CONFLICTO_DE_SLOT_ENTRE_RAMAS` porque la rama feature no tiene un proyecto asignado a 17:15; el registro de main sí ocupa ese slot. No se editó ni movió porque main es solo consulta.
- En `main/handoffs/grok_inbox/` hay dos paquetes con `status=pending`: `2026-11-24_serie_cuantica_evolucion` (Issue #1066) y `2026-11-24_serie_thomas_harris` (Issue #1065). Ambos Issues siguen abiertos; `handoffs/grok_done/` no existe en main y no hay recibo de cierre. No se disparó el webhook, no se enviaron payloads ni mensajes.
- El inventario de `main/data/publicaciones.json`, `data/miniaturas_auditoria_2026-11-21.json` y `data/horarios.json` mantiene programación previa y colisiones para 24–28 nov. El plan semanal y los registros de publicación ocupan los slots; no se detectó una ventana libre para añadir un storyboard. No se canceló ni reprogramó nada.

### Workflow, CI y PRs

- La última ejecución de validación visible, run `45477532530`, terminó SUCCESS sobre el commit `08d5cc`, pero ejecutó `scripts/validar_storyboard.py --structural-only`: no ejecutó `--check-doi`, no acredita DOI y no corresponde al HEAD actual. No se disparó ningún workflow.
- No hay ejecución reciente de `capcot-grok-dispatch.yml`; el último dispatch visible es del 1-nov y registró `Falta configurar GROK_WEBHOOK_URL`. Ese dato es histórico; el estado actual del secreto no se consultó. No se consultó ni se expuso ningún valor de secreto.
- PR #3 continúa draft/no mergeable y abarca 707 archivos, incluidos JSON de datos; no se fusiona. PR #13 y PR #14 continúan abiertos y no hay una nueva lectura fría posterior a la última corrección narrativa. PR #15 continúa abierto/no mergeable; su cambio de validador no se portó porque no se ejecutaron sus pruebas. No se fusionó ni se modificó ningún PR.

### Radar y decisión editorial

- El corte adicional de investigación quedó registrado en `2026-11-24_RADAR_CAPCOT.md`, commit `c09fe00a8f38eab110dc0a7a37e01bd8cea8b77e`: dos artículos primarios de 23-nov (USP7–MAGEL2 y modelos pediátricos) con DOI visible pero resolución Crossref/doi.org pendiente, y un candidato lunar retenido como `PENDING_SOURCE` por falta de fuente primaria accesible.
- Se intentaron las diez URL RSS definidas en `scripts/tendencias.py`; el lector web devolvió errores de tipo MIME (400), un 404 y dos URLs no accesibles. Google Trends RSS México tampoco abrió; su página HTML oficial sí mostró 184 tendencias y las primeras 25 no correspondían a la línea editorial. No se inventó respaldo ni se forzó un tema de tendencia.
- No se creó storyboard, no se escribió `narrative_qa`, no se promovió a cola, no se generaron frames, audio, voz, video ni placeholders, y no se publicó ni programó.

### Estado final del corte

- **EJECUTADO:** lectura de fuentes de verdad, revalidación de ramas/colas/Issues/Actions, verificación de los doce estados 404 y actualización del radar de investigación.
- **VERIFICADO:** commit del radar leído de vuelta; sin cambios de datos, storyboards ni estados Grok; slots ocupados y paquetes heredados identificados.
- **PENDIENTE:** resolución de DOI para los dos artículos primarios; fuente primaria del candidato lunar; revisión narrativa independiente solo si cambia una narración; recepción Grok de los doce IDs y de los dos paquetes en main; decisión del propietario sobre los paquetes heredados de main.
