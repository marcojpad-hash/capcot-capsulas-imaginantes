# CONTROL DE COLA Y AUDITORÍA — 2026-11-27

**Corte inicial:** 27-11-2026 00:02 CDMX.  
**Rama de trabajo:** `feature/capcot-video-discovery-continuity`.  
**Rama de consulta:** `main`.  
**Alcance:** proyectos 24–30 nov, backlog interdiario, lote canónico 5–7 nov, colas anidadas y producción preexistente.

## Cambios ejecutados y lectura de vuelta

| Elemento | Resultado |
|---|---|
| `proyectos/2026-11-30_rapaces-clima-reino-unido/storyboard.json` | Se añadieron `new_information` a las ocho escenas y se normalizaron los cuatro valores de `arc` admitidos por el validador. No se cambió narración ni claims. Se sustituyó SRC-002 por la página oficial ONS de límites UK 2024. Lectura de vuelta: 182 palabras, 8 escenas, 78 s de escenas + 6 s de cortinilla = 84 s; los seis campos estructurales por escena están presentes; todos los arcos son válidos. |
| QA de rapaces | JSON vigente: `FAIL/82`; revisor independiente; `giro_cientifico_explicado=false`; flag `GIRO_CIENTIFICO_NOMBRADO_PERO_NO_EXPLICADO`. El `FAIL/0` inicial quedó supersedido. |
| `proyectos/2026-11-15_dato-quasar-pareja-cosmic-dawn/storyboard.json` | El score 82 anterior era autorrevisión. Se reemplazó por `FAIL/0` y flags de revisión independiente/en frío no acreditada. El informe Groq de PR #13 existe, pero revisa metadatos y estructura junto con narración; no demuestra la lectura ciega requerida. Narración y claims intactos. |
| `docs/PLAN_MAESTRO_AUTOMATICO.md` | Se corrigió la tabla horaria antigua de cinco slots y se alineó con la fuente vigente `main:data/horarios.json`. |
| Este radar y este control | Creados en `docs/briefs/` para el corte 27-11-2026. |

**Limitación de validación:** no se ejecutó `scripts/validar_storyboard.py`. Se intentó recuperar el script para ejecución local; GitHub Raw devolvió `DisabledError` desde la herramienta web y el entorno local devolvió `Temporary failure in name resolution`. La comprobación estructural anterior es estática y no se presenta como ejecución del validador. `--check-doi` tampoco se ejecutó.

## Proyectos actuales

### 27-11 — registros intermareales

- `narrative_qa=PASS/90`, siete checks verdaderos y flags vacías en el registro existente. No se repitió la evaluación.
- Slot 23:30 ocupado en `main` por `2026-11-23_animal-stubbs`: su metadata reserva 27-11 23:30 y sus logs registran render de 86.13 s.
- El archivo MP4 señalado por metadata no aparece en el árbol GitHub; `publishAt_utc=null` y no hay video_id observado.
- Flags: `CONFLICTO_DE_SLOT_ENTRE_RAMAS`, `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`, `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`.
- `cola/estado/2026-11-27_dato-registros-intermareales-1950s.json`: 404 → `RECEPCION_GROK_NO_CONFIRMADA`.
- El storyboard permanece en `proyectos/`, sin copia plana en `cola/entrada/<id>.json`: `NOT_DISPATCHABLE`.

### 30-11 — rapaces y clima

- Slot 07:00 dentro de la ventana matutina activa; lunes no es día preferente, aunque no aparece conflicto de fecha+slot en `main`.
- Esquema comprobado estáticamente después de la corrección: 182 palabras, 8 escenas, 84 s totales, 6 s de cortinilla, prompt base del catálogo, mapa y gráfico presentes, `approved_assets=[]`, `export.render_status=NOT_GENERATED`, publicación pendiente.
- SRC-001 (artículo Frontiers) permanece `PENDING_CROSSREF`; la página editorial indica que la versión final formateada aparecerá después.
- QA vigente: `FAIL/82`; revisor independiente; `giro_cientifico_explicado=false`; `critical_flags=[GIRO_CIENTIFICO_NOMBRADO_PERO_NO_EXPLICADO]`. El `FAIL/0` inicial quedó supersedido.
- `cola/estado/2026-11-30_rapaces-clima-reino-unido.json`: 404 → `RECEPCION_GROK_NO_CONFIRMADA`.
- Sin copia plana de entrada: `NOT_DISPATCHABLE`.
- No se generaron medios ni se promovió el storyboard.

### 28-11

- 23:30 no muestra ocupación en los registros consultados.
- No se creó storyboard: todos los candidatos del radar siguen con Crossref/resolvedor pendiente.

## Backlog 24–26 nov en main — solo lectura

Se encontraron 12 storyboards: uno de magnetismo (24 nov), uno de bacterias (25 nov), nueve reescrituras del 25 nov y NBP/nanocables (26 nov). Ninguno tiene `narrative_qa` registrado y todos carecen de los seis campos estructurales (`dramatic_beat`, `scene_function`, `causal_bridge_from_previous`, `question_state`, `reason_to_continue`, `new_information`).

| Grupo | Palabras | Escenas | Duración total observada | Estado |
|---|---:|---:|---:|---|
| Magnetismo P-wave | 121 | 6 | 71 s | Fuera de contrato |
| Bacterias anticáncer | 102 | 6 | 66 s | Fuera de contrato |
| Nueve reescrituras 25 nov | 220–229 | 7 | 76 s | Longitud/duración dentro; estructura narrativa ausente |
| NBP/nanocables | 124 | 7 | 73 s | Fuera de contrato |

Las copias de magnetismo, bacterias y NBP están en carpetas anidadas de `cola/entrada`; sus estados Grok individuales devuelven 404. No se promovieron ni se modificó `main`.

- Magnetismo y bacterias tienen registros de programación/paquete; NBP tiene `programacion.json` para 26-11 17:15 CDMX y metadata.
- No hay MP4 verificable en el árbol para esos paquetes.
- Flags operativas: `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`, `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`, `RECEPCION_GROK_NO_CONFIRMADA`, `NOT_DISPATCHABLE`.

## Lote canónico 5–7 nov — revalidación sin repetir QA

Los doce storyboards canónicos conservan su revisión fechada el 18-11-2026; no se repitió la lectura narrativa porque no se observó cambio de narración.

- **PASS:** `2026-11-05_kids-dia-en-venus` (88) y `2026-11-06_inter-arena-cantante` (94).
- **FAIL:** los otros diez IDs.
- Los doce carecen de los seis campos estructurales anteriores; los árboles del 5 nov también carecen de capa de mapa y dato/gráfico.
- El árbol de `cola/bloqueados/` conserva doce borradores heredados con slugs alternativos para el lote, además de `2026-11-07_extra-nubes-pesan` y `2026-11-07_dato-clavo-te-cocina`. Sus `project_id`, narraciones y contenidos no son copias idénticas de los storyboards canónicos de `proyectos/`; se preservan sin renombrar, fusionar ni borrar durante la auditoría.
- Los doce `cola/estado/<id>.json` devuelven 404 → `RECEPCION_GROK_NO_CONFIRMADA`.
- En `main` existe una copia anidada de `2026-11-07_comida-hielo-caliente` con video_id `HSgrnejAcaI` y `publishAt` 11-11-2026 19:30Z. Es procesamiento histórico preexistente: no redispatchar. El ID no aparece en `data/publicaciones.json`; no existe `historial_youtube` en el árbol para reconciliar el estado externo. No se consultó ni alteró YouTube.

## Inventario de cola, selector y publicación

- `main`: 35 directorios de paquete anidado, 504 archivos bajo `cola/entrada/`, cero JSON planos en la raíz `cola/entrada/*.json`.
- Rama de trabajo: 2 directorios anidados, 8 archivos, cero JSON planos en la raíz.
- `capcot-grok-dispatch.yml` escucha cambios en `cola/entrada/*.json`; las carpetas anidadas no satisfacen ese filtro.
- Run del worker 45937300053: éxito técnico, resultado “No work in queue”. El resultado coincide con la ausencia de JSON planos.
- `data/publicaciones.json`: 62 registros; el campo `fecha` alcanza 24-11-2026 (los últimos elementos del array corresponden a 23-11 y `publishAt` alcanza 24-11).
- No se encontró `historial_youtube` en el árbol. No hay conexión a YouTube Studio verificada en este run.
- No se disparó Grok, no se enviaron payloads y no se inspeccionaron valores de secretos.

## Rotación horaria

`main:data/horarios.json` (23-11-2026) define ventanas activas 06:30–07:30 y 16:30–18:00; 23:30 es slot fijo. 13:00–14:30 figura como prueba y 19:00–21:00 está retirada/no autorizada para producción automática. `scripts/rotacion.py` mantiene 13:00–14:30 como ventana experimental. Se corrigió el Plan Maestro en la rama de trabajo; ningún `data/*.json` fue modificado.

## Issues, PR y Actions

- Issue #11 sigue abierto. PR #12 está cerrado; PR #13 sigue abierto y contiene un informe de Groq. El informe no acredita lectura ciega de narración solamente; Quasar queda FAIL/0.
- Issue #16 sigue abierto: registra 17 MP4 pendientes y 10 resubidas TikTok, además de Pancho EN. No hubo respuesta/comentario nuevo ni envío externo.
- PR #3 sigue abierto y en borrador; su comparación con main indica 1,491 commits por delante y 602 por detrás. No es una base para merge automático.
- PR #15 sigue abierto; no se integró.
- CodeQL de PR #3, run 45951138358: success. No ejecuta el validador estructural ni DOI.
- Worker 45937300053: success sin trabajo.
- Semgrep de main 45944165855: 37 hallazgos. Gitleaks 45944165920: success.
- No se encontró ejecución de Grok dispatch entre las últimas 100 Actions consultadas.

## Restricciones respetadas

No se modificaron `main`, `data/*.json`, secretos, permisos, estados Grok, programación externa ni medios. No se publicó ni se generó audio/video. Las únicas escrituras fueron en la rama de trabajo y en los archivos enumerados al inicio.


## Revalidación y trabajo ejecutado — 27-11-2026 02:04 CDMX

### QA narrativo independiente de rapaces

- Se realizó una pasada separada leyendo únicamente la narración concatenada; no se usaron título, resumen, arco, notas ni `narrative_contract`.
- Se actualizó `proyectos/2026-11-30_rapaces-clima-reino-unido/storyboard.json` con `narrative_qa=FAIL/82`, `review_basis=lectura_en_frio_solo_narracion`, seis checks verdaderos y `giro_cientifico_explicado=false`.
- Flag: `GIRO_CIENTIFICO_NOMBRADO_PERO_NO_EXPLICADO`. La narración plantea el contraste entre halcón y águila y presenta método/resultados, pero no explica qué asociaciones ambientales o rasgos de nicho producen la divergencia. El hallazgo está reportado, no explicado. No se reescribieron narración ni claims.
- Commit de registro QA: `bc0bed724a62a1408da6c3beae8a7a2a93a026cd`. Lectura de vuelta verificada: blob `0d20606559656a4f6070f033a4520fa9c8e463e2`; la narración quedó idéntica.

### Revalidación estructural, rotación y handoff

- Rapaces 30-nov: comprobación estática de 182 palabras, 8 escenas, 78 s de escenas + 6 s de cortinilla = 84 s, gancho de 5 palabras, voz es-MX-JorgeNeural +7% / −2Hz, prompt_base exacto y prefijos visuales correctos. La escena 3 contiene mapa con bounding box WGS84 derivado de ONS; escenas 4–7 contienen capas de datos; los source_ids referencian fuentes existentes. `approved_assets=[]`, `export.render_status=NOT_GENERATED`, publicación pendiente. No se ejecutó `scripts/validar_storyboard.py` ni `--check-doi`.
- El estilo `papel_rasgado_capas` se repite respecto del proyecto 18-nov de campos hidrotermales. No se cambió: es una decisión editorial que debe resolver el redactor.
- Intermareales 27-nov: PASS/90 existente y sin cambio de narración; no se repitió. Su estilo `atlas_antiguo` se repite respecto del proyecto Kuroshio del 18-nov. El slot 23:30 sigue reservado por Stubbs en main; el render de 86.13 s ya existe, aunque el MP4 señalado no está en el árbol. Se mantienen `CONFLICTO_DE_SLOT_ENTRE_RAMAS`, `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR` y `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`.
- Para ambos proyectos, `cola/estado/<project_id>.json` devuelve 404 (`RECEPCION_GROK_NO_CONFIRMADA`) y no existe copia plana en `cola/entrada/<project_id>.json`. Ambos siguen `NOT_DISPATCHABLE`; no se creó cola ni se modificó estado Grok.
- El proyecto de rapaces no tiene conflicto de fecha+slot en main, pero no puede promoverse por QA FAIL, DOI pendiente y estilo repetido.
- `data/estilos_usados.json` sigue congelado en octubre; la comparación real de estilos se hizo contra los storyboards de 18 y 23-nov. No se modificó ningún `data/*.json`.

### Fuentes y tendencias

- Reapertura directa de RSS: ScienceDaily Science/Health/Space devolvió `400 Unsupported content-type: application/xml`; Phys.org `400 Unsupported content-type: text/xml`; NASA `400 Unsupported content-type: application/rss+xml`; ESA `404 Not Found`; Nature `400 Unsupported content-type: application/rss+xml`; UNAM `400 Unsupported content-type: application/rss+xml`; EurekAlert y SINC devolvieron “URL ... is not accessible via this tool”. Google Trends RSS México devolvió el mismo tipo de inaccesibilidad.
- La vista HTML oficial de Google Trends México mostró 253 tendencias; las primeras 25 no aportaron señal científica/natural admisible.
- Se agregó a vigilancia, sin elevarlo a candidato principal, el artículo primario PAV1 de *Frontiers in Plant Science* (26-nov-2026), DOI declarado 10.3389/fpls.2026.2008228. El artículo informa >98% de inhibición in vitro en 48 h y menor incidencia de agalla en plantas de tomate bajo aplicación preventiva; no es evidencia de eficacia de campo en viñedos. La coordenada publicada 41.1081, 16.2606 corresponde al punto de aislamiento de aguas residuales en Bari, no al ensayo en tomate.
- Crossref y `doi.org` devolvieron `Internal Error ()` / URL no accesible para los DOI intentados. PAV1 y SRC-001 de rapaces permanecen `PENDING_CROSSREF`. No se creó storyboard para el 28-nov 23:30 ni se seleccionó un sexto candidato.
- Radar actualizado y releído en commit `b0e3de54d1b46394d8f67b4db7900a0407bc193e`.

### Actions, main y backlog

- Main HEAD `92d6c034b12a86785a5d12eb22e634f8453cd510`: el único archivo cambiado en ese commit es `data/endscreens_rotacion.json`; no cambió la ocupación de proyectos, cola, salidas, publicaciones ni programación.
- Worker 45937300053: SUCCESS técnico; log literal `[trabajador] sin trabajo en cola.`
- Semgrep 45944165855: FAILURE con 37 hallazgos bloqueantes; el paso de carga SARIF fue omitido. Gitleaks 45944165920: SUCCESS.
- CodeQL PR #3, run 45951871951: SUCCESS en Python y Actions; no ejecuta el validador de storyboard ni verifica DOI.
- PR #3 sigue OPEN/DRAFT; PR #15, #14 y #13 siguen abiertos. Issues #11 y #16 siguen abiertos. No se disparó workflow, no se envió payload y no se hizo merge.
- El backlog 24–26 nov de main conserva los mismos 12 storyboards; el commit de main citado no tocó sus archivos. El lote canónico 5–7 nov conserva las revisiones del 18-nov; no se repitieron PASS válidos ni se modificaron copias heredadas.
- No se modificaron main, `data/*.json`, cola, estados Grok, programación externa, secretos, permisos ni medios. No se generó ni publicó contenido.


### CI posterior a los commits de esta revalidación

- Rama de trabajo leída de vuelta: `feature/capcot-video-discovery-continuity` en `68674b8ebe93d386e1c21a6aff5c4f56777e2e43`.
- PR #3 CodeQL: run 45962867108 (commit QA `bc0bed724a62a1408da6c3beae8a7a2a93a026cd`), 45962917048 (radar `b0e3de54d1b46394d8f67b4db7900a0407bc193e`) y 45962966589 (control `68674b8ebe93d386e1c21a6aff5c4f56777e2e43`) terminaron SUCCESS en los jobs Analyze (actions) y Analyze (python). Son análisis CodeQL; no ejecutan el validador estructural ni `--check-doi`.


## Revalidación adicional y trabajo ejecutado — 27-11-2026 03:55 CDMX

### Nuevo borrador PAV1 — 27 nov, 07:00

- Slot 07:00 dentro de la ventana activa 06:30–07:30; no se encontró ocupación en main ni en la rama de trabajo para ese fecha+slot. El 23:30 sí está ocupado por Stubbs en main.
- Fuente primaria: Frontiers in Plant Science, artículo original del 26-11-2026, DOI 10.3389/fpls.2026.2008228. La página primaria está accesible y muestra DOI, coordenada y resultados. El acceso directo a doi.org no estuvo disponible desde la herramienta; Crossref/`--check-doi` queda pendiente.
- Creado `proyectos/2026-11-27_dato-pav1-bacteriofago/storyboard.json`, commit `fb4b39a920ae52e3b0c56adf307d49725b7fe2b1`. Lectura de vuelta: blob `060ac46a49e176d81905589d7c16aa19ff2a5388`; 187 palabras, 8 escenas, 78 s + 6 s = 84 s, gancho 5 palabras, voz exacta, mapa con 41.1081 N / 16.2606 E (sitio de aislamiento), dato >98% in vitro y gráfico de incidencia en tomate, ambiente/SFX por escena, `approved_assets=[]`, `export.render_status=NOT_GENERATED`, publicación pendiente.
- No se creó `narrative_qa`, `ESTADO_EJECUCION.md`, carpeta de medios ni copia en `cola/entrada`. El investigador no se autoaudita ni marca preparado.
- Clasificación: `NOT_DISPATCHABLE`; no hay `cola/estado/2026-11-27_dato-pav1-bacteriofago.json` (`RECEPCION_GROK_NO_CONFIRMADA)), no hay copia plana de cola y el validador estructural real/`--check-doi` no se ejecutó.

### Intermareales — corrección de registro

- Se conservó `narrative_qa=PASS/90` existente sin repetir la lectura.
- Se retiraron dos notas históricas contradictorias que seguían diciendo FAIL/0 y revisión independiente ausente, porque una nota posterior ya registra la auditoría ciega PASS/90. El objeto `narrative_qa` no se modificó.
- Sigue `CONFLICTO_DE_SLOT_ENTRE_RAMAS` por Stubbs en main el 27-11 23:30; el render de 86.13 s está registrado, pero el MP4 señalado no aparece en el árbol. Estilo `atlas_antiguo` repetido respecto del proyecto Kuroshio del 18-11. No promover.

### Lote canónico 5–7 nov — corrección de inventario

| Project ID | QA existente | Estructura estática |
|---|---:|---|
| `2026-11-05_kids-dia-en-venus` | PASS/88 | FAIL |
| `2026-11-05_comida-palomitas` | FAIL/82 | FAIL |
| `2026-11-05_inter-arboles-se-comunican` | FAIL/78 | FAIL |
| `2026-11-05_inter-rayo-globular` | FAIL/0 | FAIL |
| `2026-11-06_kids-ballena-azul-corazon` | FAIL/80 | FAIL |
| `2026-11-06_comida-aguacate-negro` | FAIL/79 | FAIL |
| `2026-11-06_inter-ranas-congeladas` | FAIL/83 | FAIL |
| `2026-11-06_inter-arena-cantante` | PASS/94 | FAIL |
| `2026-11-07_kids-huesos-bebe` | FAIL/0 | FAIL |
| `2026-11-07_comida-hielo-caliente` | FAIL/0 | FAIL |
| `2026-11-07_inter-pulpo-suenos` | FAIL/0 | FAIL |
| `2026-11-07_inter-nubes-pesan` | FAIL/0 | FAIL |

- Las dos PASS conservan siete checks verdaderos, score ≥85 y flags vacías; no se repitió QA.
- Prechequeo estático contra los campos obligatorios actuales del validador: 0/12 estructuralmente aptos. Faltan seis campos narrativos por escena (`dramatic_beat`, `scene_function`, `causal_bridge_from_previous`, `question_state`, `reason_to_continue`, `new_information`): 510 omisiones en 85 escenas, más tres incidencias adicionales en el borrador de árboles. El script Python real no se ejecutó porque el clon/descarga de GitHub no estuvo disponible; este prechequeo no se reporta como ejecución del validador.
- No hay rutas `cola/estado/<id>.json` en el árbol para los doce IDs: `RECEPCION_GROK_NO_CONFIRMADA` en todos. Ninguno se promueve.
- Los doce borradores heredados de `cola/bloqueados/` tienen slugs alternativos y contenido distinto de los storyboards canónicos; se preservan sin fusionar ni renombrar durante esta pasada. `2026-11-07_comida-hielo-caliente` tiene además una copia producida en main: video_id `HSgrnejAcaI`, `publishAt=2026-11-11T19:30:00Z`, salida QA y programación; `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`. El MP4 no está en el árbol: `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`.
- El extra `2026-11-07_dato-clavo-te-cocina` es un borrador bloqueado fuera del lote canónico, con fecha objetivo 2026-11-07 y slot 23:30. QA FAIL/82; el estado registra YouTube `EwZ3dHalUn0` y TikTok `7705655549571894529` como publicados, Facebook programado para 8-nov 23:30 sin confirmación final. La historia registra YouTube a `2026-11-09T05:30:22Z` (8-nov 23:30 CDMX), por lo que el `fecha_objetivo` del storyboard y el historial no coinciden. `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`; no se redispatcha ni se altera el storyboard.

### 26 nov NBP/nanocables — main solo lectura

- `proyectos/2026-11-26_nbp-nanocables`, `cola/entrada/2026-11-26_nbp-nanocables` y `salidas/2026-11-26_nbp-nanocables` contienen storyboard, programación y metadata de salida. El storyboard tiene 124 palabras, 7 escenas y 73 s; no tiene narrative_qa ni cumple duración/longitud. La carpeta de salida prueba procesamiento preexistente; el MP4 referenciado no aparece en el árbol. No redispatchar ni modificar main.
- No se encontraron archivos `historial_youtube` en el árbol consultado. No se consultó YouTube Studio ni se infirió estado externo.

### Selector, workflow y Actions

- `.github/workflows/capcot-grok-dispatch.yml` mantiene el filtro `cola/entrada/*.json` (solo JSON plano en la raíz); las carpetas anidadas no satisfacen el trigger. No se disparó ningún workflow ni se envió payload.
- La rama de trabajo HEAD actual es `d2cf42a2d994cd9ad86ecb21a243ce03bbcde950`. La consulta de Actions por rama no mostró ejecución posterior a ese HEAD; CodeQL de commits anteriores no acredita el validador ni DOI.
- El repositorio sigue sin `historial_youtube` visible en el árbol; no se inventó estado de IDs antiguos.

### Radar y tendencias

- Google Trends HTML México: 257 tendencias en la consulta actual; las primeras 25 no mostraron tema científico/natural admisible.
- Se reintentaron los RSS directos; permanecen errores XML/RSS, ESA 404 y URLs no accesibles. No se ejecutó `scripts/tendencias.py` localmente.
- Radar actualizado con cinco candidatos activos: PAV1 (seleccionado para 07:00), riesgo genético mesopelágico, `Westlothiana`, L-BAIBA y `Uintatherium`. Los cinco candidatos del corte 00:02 siguen `PENDING_SOURCE` hasta resolver correspondencia DOI/URL.
- No se generaron medios, no se publicó, no se programó y no se gastaron créditos.


## Corrección de evidencias heredadas y selector — 27-11-2026 03:55 CDMX

- `2026-11-07_comida-hielo-caliente`: el storyboard canónico de feature marca 2026-11-07 13:30 y FAIL/81. Main contiene el mismo `project_id` en `cola/entrada` y una salida con QA de 89.83 s. `publicacion.json` registra video `HSgrnejAcaI`, `privacyStatus=private`, `publishedAt=2026-11-10T21:01:55Z` y `publishAt=2026-11-11T19:30:00Z`; el historial `data/horario_2026-11-08.json` registra el mismo ID como publicado a `2026-11-09T05:30:22Z`. La ruta `cola/entrada/.../programacion.json` devolvió 404. Se conserva la discrepancia temporal sin resolverla por inferencia. Clasificación: `CONFLICTO_DE_SLOT_ENTRE_RAMAS` + `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`. El storyboard declara `capsula.mp4`, pero el MP4 no aparece en el árbol: `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`.
- `2026-11-07_dato-clavo-te-cocina`: el estado archivado confirma QA FAIL/82, recepción Grok no confirmada y procesamiento previo. YouTube/TikTok constan como publicados; Facebook figura programado sin confirmación final. El registro histórico sitúa la publicación de YouTube en 8-nov 23:30 CDMX, aunque el storyboard conserva `fecha_objetivo=2026-11-07`. No se encontró salida ni medios en los árboles consultados; se mantiene `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO` y no se redispatcha.
- `2026-11-07_extra-nubes-pesan` contiene otro storyboard con el mismo `project_id=2026-11-07_inter-nubes-pesan`, pero 176 palabras frente a 221 del proyecto canónico. La lectura de `ESTADO_EJECUCION.md` devolvió `ConnectTimeout`; se preserva como versión divergente, sin fusionar ni sobrescribir.
- Las copias planas y carpetas bloqueadas de los doce slugs alternativos difieren de los storyboards canónicos de `proyectos/`; no son duplicados byte-a-byte. No se borran ni se renombra ninguna durante esta pasada. Las cuatro parejas flat/nested comparadas también difieren; las tres copias planas sin carpeta anidada difieren del proyecto canónico.
- `scripts/` no contiene scripts separados llamados selector/profundidad/Grok; el selector está embebido en `.github/workflows/capcot-grok-dispatch.yml`. En líneas 44 y 50 usa `find cola/entrada -maxdepth 1` y el filtro `^cola/entrada/[^/]+\.json$`: solo procesa JSON plano en la raíz. El paso de validación ejecuta únicamente `python -m json.tool`; no ejecuta `scripts/validar_storyboard.py` ni `--check-doi`. El paso siguiente crea un marcador `handoffs/grok_inbox` con `status=pending`; eso no es acuse de Grok. No se disparó el workflow ni se inspeccionaron valores de secretos.

## Revalidación PAV1 y backlog — 27-11-2026 04:23 CDMX

- **PAV1 / 07:00:** `proyectos/2026-11-27_dato-pav1-bacteriofago/storyboard.json` permanece solo en `proyectos/`. La lectura de `cola/estado/2026-11-27_dato-pav1-bacteriofago.json` devolvió HTTP 404: `RECEPCION_GROK_NO_CONFIRMADA`. `cola/entrada/` no contiene JSON plano para PAV1; el workflow escucha `cola/entrada/*.json`. Clasificación: `NOT_DISPATCHABLE`; no se creó handoff ni se envió payload.
- **QA narrativo PAV1:** se registró `FAIL`, score `0`, `review_basis=lectura_en_frio_solo_narracion`, `reviewer_role=auditor_no_independiente`, `critical_flags=[REVISION_INDEPENDIENTE_AUSENTE]`. No hay evidencia verificable de un auditor independiente distinto del redactor. Narración y claims intactos; no se promueve.
- **Prechequeo estructural estático PAV1:** 187 palabras; 8 escenas; 78 s de escenas + 6 s de cortinilla = 84 s; gancho de 5 palabras; voz es-MX-JorgeNeural +7% / -2Hz; `prompt_base` coincide con `scripts/estilos.json`; capas de mapa y gráfico presentes; punto de aislamiento publicado en Bari (41.1081, 16.2606), sin inventar coordenadas para los ensayos de tomate; ambiente y SFX por escena; `approved_assets=[]`; `export.render_status=NOT_GENERATED`; sin rutas ni nombres de medios. Esto es revisión estática, **no** ejecución del validador Python.
- **DOI PAV1:** la página primaria de Frontiers está accesible y muestra el DOI `10.3389/fpls.2026.2008228`; Crossref REST y resolución `doi.org` no quedaron confirmados. `--check-doi` no se ejecutó. La URL primaria sí fue consultada; el DOI permanece pendiente de resolver.
- **Slot y producción PAV1:** `main/proyectos/` no contiene proyecto del 27 ni del 30-nov; `main/data/publicaciones.json` no contiene PAV1; las rutas `salidas/2026-11-27_dato-pav1-bacteriofago/` y `cola/bloqueados/2026-11-27_dato-pav1-bacteriofago/` devolvieron 404. No se observó producción previa ni conflicto de slot en main. No existe `ESTADO_EJECUCION.md` en el proyecto.
- **Intermareales:** PASS/90 permanece sin cambios; el mismo slot 27-nov 23:30 está ocupado en main por Stubbs y hay producción previa. Se conserva `CONFLICTO_DE_SLOT_ENTRE_RAMAS` / `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`; no repetir PASS ni redispatchar.
- **Rapaces:** FAIL/82 permanece sin cambios; no se repitió QA. `cola/estado/2026-11-30_rapaces-clima-reino-unido.json` devolvió 404; no hay entrada, salida ni copia bloqueada en feature. No se promueve.
- **Lote 5–7 nov:** los 12 storyboards canónicos conservan sus últimos commits del 18-nov (grupos de commits `34a5775`, `2c7c0b7`, `56b077e`); estado QA agregado sigue 2 PASS / 10 FAIL. No hubo cambios de storyboard posteriores, por lo que no se repitieron PASS ni auditorías narrativas.
- **Entrada anidada heredada:** `cola/entrada/2026-11-09_dato-robot-ensambla-orbita/` sigue siendo paquete previo; su estado declara `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`, YouTube `ZG4iQgmWrLI` programado para 21-nov 19:00 CDMX y `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`. `frames/` contiene solo `.gitkeep`; `cola/estado/<id>.json` devuelve 404. No se redispatcha.
- **Actions:** el trabajador de main, run `45937300053`, terminó con el log literal `[trabajador] sin trabajo en cola.` El run `45898334232` ejecutó `python scripts/validar_storyboard.py` únicamente sobre Kuroshio (18-nov), sin `--check-doi`; no valida PAV1. No se dispararon workflows.
- **Fuentes y tendencias:** la consulta RSS no pudo ejecutarse desde el runtime local por `URLError: <urlopen error [Errno -3] Temporary failure in name resolution>`; se usó el respaldo HTML oficial de Google Trends, documentado en el radar. No se modificaron `data/*.json`, main, estados Grok, secretos, permisos ni medios.

## Reconciliación de programación e historial — 27-11-2026 04:34 CDMX

- `main/data/horarios.json` (SHA `2261993d…`) fue actualizado el 23-nov: ventanas activas 06:30–07:30 y 16:30–18:00; 23:30 es el slot fijo del dato del día. El slot PAV1 07:00 cae en la ventana activa. El archivo define ventanas, no asignaciones por fecha.
- `main/data/publicaciones.json` contiene 62 registros y ninguno entre 25–30 nov; `main/data/vistas_historico.json` contiene 110 y ninguno en ese rango; `main/data/cola.json` está vacío. No existen `programacion.json` ni `historial_youtube.json` en raíz o `data/` en el corte consultado.
- La fuente local vigente de rehechos es `data/rehechos_2026-11-22.json`: 9 filas con nuevos IDs programados para 25–29 nov (dos ya vencidas del 25, dos del 26, dos del 27 a 10:00/15:00, dos del 28 a 10:00/15:00 y una del 29 a 10:00). La misma fuente declara originales intactos; no se cambió privacidad ni se canceló nada.
- `data/resubidas_2026-11-21.json` registra dos nuevos IDs de YouTube con `publishAt` 22/23-nov y originales conservados; `enana-blanca` sigue bloqueada sin MP4. Los registros son históricos y no acreditan el estado real actual de YouTube Studio.
- No hay `historial_youtube.json` ni `programacion.json` que permita reconciliar si los `publishAt` pasados se publicaron. Los IDs originales siguen marcados como intactos en los registros, así que existe riesgo de duplicidad de contenido si los nuevos IDs también quedaron públicos; no se borran ni cancelan.
- La lista de nueve paquetes con colisión exacta 17:00 citada en el informe del 26-nov no se pudo reproducir desde los archivos actuales de `main` (`publicaciones`, `horarios`, `cola`, `rehechos` y `resubidas`). Se conserva como hallazgo histórico no revalidado, no como estado actual confirmado. No se afirma sobrecarga vigente sin un registro actual de programación.

## Lote 5–7 nov — slots, QA y copias bloqueadas — 27-11-2026 04:34 CDMX

- Los 12 `project_id` canónicos coinciden **12/12** con `data/horario_semana_2026-11-01_07.json` (blob `a567b140bab9616ab8e52666925aa79dd267223e`) en `fecha_objetivo`, `slot_local` y `slot_cesta`. No hay desajuste de tema-slot en los metadatos.
- PASS narrativo existente y válido: `2026-11-05_kids-dia-en-venus` 88/100 y `2026-11-06_inter-arena-cantante` 94/100; ambos tienen siete checks true, `critical_flags=[]`, `review_basis=lectura_en_frio_solo_narracion` y `reviewer_role=auditor_capcot_independiente`. Narraciones sin cambios desde 18-nov: no se repitió el PASS.
- Diez FAIL conservados, sin reescritura: palomitas 82 (`APERTURA_DEFINICIONAL_NO_IN_MEDIAS_RES`, repetición en escena 6); árboles 78 (`APERTURA_GENERICA_NO_IN_MEDIAS_RES`); rayo 81 (`APERTURA_HISTORICA_DESCRIPTIVA_NO_IN_MEDIAS_RES`); ballena 80 (`PAYOFF_SOBREAFIRMA_CASI_SE_DETIENE`); aguacate 79 (`REPETICION_ESCENAS_5_6_SIN_AVANCE_CAUSAL`); ranas 83 (`REPETICION_ESCENAS_5_6_LIMITES_DE_ESPECIE_Y_CONDICIONES`); huesos 82 (`ESCENA_6_REPITE_VARIACION_DE_CONTEO_Y_FUSION`); hielo 81 (`APERTURA_DE_CREENCIAS_NO_IN_MEDIAS_RES`); pulpo 72 (`FUENTE_PRIMARIA_CORRESPONDE_A_OCTOPUS_LAQUEUS_NO_INSULARIS`, `REPETICION_ESCENAS_5_6_Y_PAYOFF_VAGO`); nubes 78 (`ESCENA_7_REITERA_CIFRA_Y_LIMITE_SIN_PAYOFF_DE_SUSPENSION`).
- Los 12 `cola/estado/<project_id>.json` devolvieron HTTP 404: `RECEPCION_GROK_NO_CONFIRMADA` en todos. Ninguno de los 12 canónicos aparece en `cola/entrada/`; por tanto no hay recepción formal ni dispatch confirmado.
- En `cola/bloqueados/` solo hay tres nombres exactos de los canónicos (aguacate, ranas y huesos). Las demás copias tienen `project_id` distinto y son variantes históricas (`comida-palomitas-explotan`, `inter-arboles-mito-respiran`, `inter-venus-dia-largo`, `inter-corazon-ballena-azul`, `inter-arena-cantante`, `inter-mpemba-mito`, `inter-suenos-pulpo`, `inter-nubes-pesan`, entre otras); se verificó que el `project_id` interno coincide con el nombre variante, no con el canónico. Ya están bloqueadas: no se renombraron, fusionaron ni sobrescribieron.
- `2026-11-07_extra-nubes-pesan` se mantiene como material de origen, no como segundo proyecto. Los dos PASS son únicamente narrativos; no hay acreditación de validador estructural/DOI ni promoción a cola.

## Inventario `data/*.json` de feature — solo lectura — 27-11-2026 04:34 CDMX

- Se consultaron los 20 JSON de primer nivel de `feature/data/`; ninguno fue modificado. `data/horario_semana_2026-11-01_07.json` declara `total=35`, pero su arreglo contiene 36 slots. Los 12 IDs obligatorios sí coinciden con su registro individual.
- Los registros de rotación/estilos están atrasados: `temas_del_dia.json` llega al 28-oct; `estilos_usados.json` al 28-oct; `rotacion.json` al 31-oct; `tendencias_estilos.json` al 31-oct. `publicaciones.json` llega al 31-oct (22 filas) y `vistas_historico.json` al 28-oct (74 cortes). No son inventario vigente para el 27-nov.
- `horarios.json` de feature sigue actualizado al 09-nov, mientras que `main/data/horarios.json` está actualizado al 23-nov; para el slot actual se usó main en solo lectura. `horario_2026-11-08/09/10/11.json` son cortes históricos, no programación de hoy.
- `balances_6h.json` termina el 28-oct; `reprogramacion_tt_fb_v4_2026-11-01_03.json` es del 31-oct con 10 slots históricos; `cola.json` contiene una sola entrada fallida del 31-oct (`2026-10-31_pardelas-jetlag-solar`, rc=1). `endscreens_rotacion.json` tiene última revisión 23-nov y conserva mapeos fijos/exclusiones; no se tocaron.
- La discrepancia `total=35` vs 36 slots y los JSON atrasados quedan documentados, no corregidos, por la regla de solo lectura de `data/*.json`.


## Revalidación operador único — 27-11-2026, 05:58 CDMX (run 10)

### CAPCOT: comprobaciones ejecutadas

- Rama de trabajo observada sin cambios de storyboard desde el corte anterior. No se repitieron QA PASS ni se reescribieron narraciones.
- **PAV1:** lectura de vuelta: 187 palabras, 8 escenas, 78 s de escenas + 6 s de cortinilla = 84 s; voz `es-MX-JorgeNeural`, rate `+7%`, pitch `-2Hz`; `9:16`; prompt_base coincide exactamente con `scripts/estilos.json`; mapa y gráfico citan SRC-001; coordenada del aislamiento confirmada en Métodos del artículo primario; ambiente y SFX presentes en las ocho escenas; cierre hablado exacto; `approved_assets=[]`, `NOT_GENERATED`, sin rutas de medios. La revisión narrativa permanece **FAIL/0** con `REVISION_INDEPENDIENTE_AUSENTE`; no se atribuyó independencia al redactor.
- PAV1: el artículo completo de Frontiers figura como publicado el 26-11-2026 y contiene el DOI y la coordenada del sitio de aislamiento. El resolver DOI redirigió a la URL editorial; Crossref REST no pudo consultarse por DNS. Se conserva `VERIFICADO_URL`, sin afirmar verificación Crossref. El validador estructural real no se ejecutó en este runtime.
- PAV1: `cola/estado/<project_id>.json`, `cola/entrada/<project_id>.json` y `salidas/<project_id>/` no existen (404). Estado: `RECEPCION_GROK_NO_CONFIRMADA`; **NOT_DISPATCHABLE**. No se creó entrada.
- **Intermareales:** PASS/90 independiente conservado sin repetirlo; 173 palabras, 8 escenas y 84 s totales. En main, `2026-11-23_animal-stubbs` ocupa el 27-11-2026 23:30 y su `render.log` registra 86.13 s; `capsula.mp4` devuelve 404 en el árbol. Se confirma `CONFLICTO_DE_SLOT_ENTRE_RAMAS`, `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR` y `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`. El estado Grok del proyecto también devuelve 404; **NOT_DISPATCHABLE**.
- El siguiente slot de 23:30, 28-11-2026, está reservado en main por `2026-11-23_animal-tama`; su render.log registra 85.11 s y el MP4 referenciado tampoco está en el árbol. No se usó ese slot.
- Actions: el trabajador de main run `45937300053` terminó SUCCESS con `[trabajador] sin trabajo en cola`. El validador run `45898334232` terminó SUCCESS sobre Kuroshio, pero ejecutó `python scripts/validar_storyboard.py ...` sin `--check-doi`; no acredita DOI ni valida PAV1. No se disparó ningún workflow ni se envió payload.
- `registro_editorial.py` recorre storyboards a cualquier profundidad y separa markers de `handoffs/grok_inbox`; esos markers no confirman recepción. `capcot-grok-dispatch.yml` acepta entradas planas `cola/entrada/*.json`, no carpetas anidadas.

### Radar y continuidad

- La copia local del script de tendencias falló en los diez RSS científicos y en Google Trends RSS con `URLError(gaierror(-3, 'Temporary failure in name resolution'))`. El respaldo oficial HTML de Google Trends México mostró 249 tendencias en las últimas 24 h; las primeras 25 no ofrecieron candidato científico/natural admisible.
- El lote 5–7 nov, rapaces y los demás proyectos sin cambios de narración permanecen con sus QA previos; no se repitieron PASS ni se promovieron copias.
- No se modificaron `data/*.json`, storyboards, cola, estados Grok, main, workflows, secretos o permisos. No hubo medios, publicaciones, dispatches ni consumo de créditos.

**Resultado del corte:** cero promociones y cero nuevos storyboards. PAV1 sigue fuera de promoción por QA independiente ausente y Crossref no confirmado; Intermareales no se redispatcha por conflicto y procesamiento previo.

## Run 11 — 2026-11-27 07:59 CDMX

### Inventario, rotación y slot

- Se releyeron el inventario/control del 27-11, el plan semanal de main, `data/publicaciones.json`, `data/rehechos_2026-11-22.json`, `data/horarios.json`, la rotación y los storyboards de proyectos activos.
- El slot 2026-11-28 23:30 está ocupado en main por `2026-11-23_animal-tama`; no se reutiliza. El slot 2026-11-27 23:30 también tiene procesamiento previo (Stubbs), según el inventario vigente.
- El proyecto de rapaces de feature ocupa 2026-11-30 07:00. Su estructura/estilo son `pregunta` / `papel_rasgado_capas`.
- Para 2026-11-30 17:00 no se encontró registro coincidente en `main/data/publicaciones.json` (sin registros 29–30 nov), el plan semanal consultado termina el 28-11, y las rutas main de proyecto/cola/salida consultadas para el proyecto de rapaces devolvieron 404. El horario maestro mantiene activa la ventana 16:30–18:00. Resultado: slot 17:00 sin conflicto encontrado en las fuentes de main consultadas; no se afirma ausencia absoluta fuera de esas fuentes.
- El día 30 tiene un borrador existente a las 07:00; el nuevo borrador de las 17:00 usa tema, estructura `comparacion`, estilo `rubber_hose_1930s` y cama `pulso` distintos. El cupo diario configurado es cinco; no se superó.
- `data/rotacion.json` y `data/temas_del_dia.json` conservan fechas históricas antiguas. No se modificaron: `scripts/registro_editorial.py` inspecciona recursivamente storyboards en proyectos, cola de entrada, bloqueados y salidas para construir el registro vigente.

### Investigación y storyboard nuevo

- Se probaron los diez RSS de `scripts/tendencias.py` y Google Trends RSS México; los once fallaron con `URLError(gaierror(-3, 'Temporary failure in name resolution'))`.
- Respaldo oficial: Google Trends México HTML mostró 249 tendencias en 24 h; el primer bloque de 25 no ofreció tema científico.
- El radar 2026-11-27 se actualizó con tres artículos primarios nuevos: EpTFIIAγ/cereales, m⁶A/YTH.2 en malaria y cPLA₂/LTA₄H. Se separaron observación, cálculo, inferencia y recomendación.
- Se creó `proyectos/2026-11-30_liquen-gen-cereales/storyboard.json` para 17:00, como `PROPUESTA_PENDIENTE_DECISION_GROK`, no como selección final.
- Relectura del JSON el 27-11 09:59: 199 palabras de narración (no 200), 8 escenas, 78 s de escenas + 6 s de cortinilla = 84 s; gancho de seis palabras; voz `es-MX-JorgeNeural`, rate +7%, pitch -2Hz; `visual_identity.prompt_base` coincide con catálogo; capa de dato 19.4–32.8%; ambiente y SFX en cada escena. **La capa mapa no estaba en el JSON**, aunque el reporte anterior la había dado por presente; se corrigió después con un commit independiente.
- `approved_assets=[]`, `export.render_status=NOT_GENERATED`, sin `asset_filename`, `asset_type`, rutas ni `export.filename`; `publicacion.status=PENDIENTE_DECISION_GROK`. No se creó `narrative_qa`, `ESTADO_EJECUCION`, medios ni placeholders.
- Se ejecutó un prechequeo estructural propio sobre el contenido leído de vuelta; pasó los conteos y campos anteriores. **No equivale al validador oficial** `scripts/validar_storyboard.py`; ese validador no se ejecutó en este run.
- La fuente primaria de Nature es accesible y el artículo incluye DOI, resultados y coordenadas de los cuatro sitios. Crossref REST y doi.org fallaron con el error DNS exacto; DOI = `PENDING_CROSSREF`.

### Handoff y producción previa

- `cola/entrada/2026-11-30_liquen-gen-cereales.json`: 404; no se creó entrada.
- `cola/estado/2026-11-30_liquen-gen-cereales.json`: 404; se registra `RECEPCION_GROK_NO_CONFIRMADA`. No se creó ni modificó estado Grok.
- `cola/bloqueados/2026-11-30_liquen-gen-cereales/storyboard.json`: 404.
- `salidas/2026-11-30_liquen-gen-cereales/metadata.json`: 404.
- Clasificación: `NOT_DISPATCHABLE`. Faltan revisión narrativa independiente PASS, validador estructural oficial y DOI/Crossref; recepción Grok no confirmada. No se promovió copia a cola.
- El workflow `.github/workflows/capcot-grok-dispatch.yml` fue leído: el disparador de entrada atiende `cola/entrada/*.json` plano; el borrador permanece en `proyectos/` y no dispara handoff. No se disparó workflow ni se envió payload.
- El intento de consultar directamente el run de Actions devolvió `DisabledError`; no se atribuyó una ejecución nueva. El último estado de Actions conservado en este control sigue siendo el registrado en el corte anterior.
- No se inspeccionaron ni revelaron valores de secretos; no se nombran variables por no existir evidencia de que falten.

### Resultado del run

- **EJECUTADO:** borrador textual en `proyectos/`, radar y control actualizados.
- **VERIFICADO:** lectura de vuelta del storyboard, radar y control; slot consultado; ausencia de cola/estado/salida para el nuevo ID.
- **PENDIENTE:** DOI/Crossref, validador oficial, revisión narrativa independiente y recepción individual Grok.
- **NO REALIZADO:** render, audio, imágenes, video, publicación, programación, dispatch, cambios en `data/*.json`, main, secretos o permisos.

### Referencias de persistencia del run 11

- Radar actualizado: commit `f370ca43b968054b1bff40d54f840e7ef4ca272a`; blob verificado `5ca46365bd4966d07ac18498af78fc1b6ae5898f`.
- Control actualizado: commit anterior `317aa7d6455e5d52ec842de6659d3ae2ac6595ff`; blob actual previo a esta nota `f50ca4c7a065ade5f18ea8291e18b3fc68dd2c93`.
- Storyboard `proyectos/2026-11-30_liquen-gen-cereales/storyboard.json`: blob verificado `5f9bd265a7af4379b8d83122ec93edb3d7a20c0f`.
- Fuentes U6 inspeccionadas en solo lectura: `preparar_entrada_solo.py` blob `891e37a482207399f9f929824e0935486b4b95b1`; pruebas `test_preparar_entrada_solo.py` blob `6faa007e40a41c4648262df81302907c6c57fde6`; gate Z90 `5d4627514e7aa33500183fc395b6795bb4fb925d`. No se ejecutó ni modificó U6.


## Revalidación operativa — 27-11-2026 09:59 CDMX

### Borrador EpTFIIAγ — corrección estructural verificada

- Se releyó `proyectos/2026-11-30_liquen-gen-cereales/storyboard.json` y se detectó que no tenía ninguna `scenes[].capa` de tipo `mapa`; el control anterior afirmaba erróneamente que ya existía.
- **EJECUTADO:** se añadió la capa `mapa` a S02, sin cambiar narración ni claims. Incluye cuatro puntos publicados en Métodos de Du et al. (Nature, 25-11-2026): Yangling (34.2667, 108.0667), Heyang (35.7167, 110.0333), Cangzhou (38.5500, 116.6333) y Linfen (36.9333, 112.5667). La ventana `region` se calcula desde esos puntos con margen de 0.5° y se declara como extensión de visualización, no como límite administrativo.
- **VERIFICADO:** commit `e2ef0e4a074ef614c641f70ee8e68852b58a9bc5`; blob leído de vuelta `4fb4e1aaf7580251995c29062c211948846e8181`. El recuento real de narración es 199 palabras; 8 escenas; 78 s + 6 s = 84 s; 4 coordenadas válidas; una capa de dato; `visual_identity.prompt_base` y los ocho `image_prompt` coinciden con el catálogo; voz, ambiente, SFX, `approved_assets=[]`, `NOT_GENERATED` y publicación pendiente se conservan.
- **PENDIENTE:** no se ejecutó `scripts/validar_storyboard.py --structural-only`. El intento de recuperar el script desde GitHub en el contenedor falló literalmente con `curl: (6) Could not resolve host: raw.githubusercontent.com`; el visor web rechazó los archivos raw con `DisabledError`. La consulta de Actions para el commit devolvió `workflow_runs=[]`. La revisión estática de campos no se presenta como ejecución del validador oficial.
- **PENDIENTE:** Crossref REST y `doi.org` no fueron accesibles desde esta sesión; DOI `10.1038/s41586-026-11151-w` sigue `PENDING_CROSSREF`. La página/PDF primaria sí muestra el DOI y los cuatro sitios.
- **QA y handoff:** `narrative_qa` continúa ausente; no se realizó una pasada independiente posterior. `cola/estado/2026-11-30_liquen-gen-cereales.json` sigue 404 (`RECEPCION_GROK_NO_CONFIRMADA`); no existe entrada plana, salida ni copia bloqueada. Clasificación `NOT_DISPATCHABLE`; no promover.

### Revalidación de agenda y rotación

- `main/data/horarios.json` mantiene ventanas 06:30–07:30 y 16:30–18:00; 17:00 es un horario permitido, no una asignación por fecha.
- `main/data/rehechos_2026-11-22.json` contiene nueve paquetes y no registra 27-11 17:00 ni 30-11 17:00. `main/data/publicaciones.json` contiene 62 registros y no presenta entradas 27–30 nov. Esto no acredita ausencia de IDs externos programados.
- No se creó storyboard para 27-11 17:00: falta una fuente de historial/programación externa que permita descartar con seguridad un ID antiguo. El slot 30-11 17:00 sigue sin conflicto encontrado en las fuentes de main consultadas, no como ausencia absoluta fuera de ellas.
- `feature/data/rotacion.json`, `data/temas_del_dia.json` y `data/estilos_usados.json` siguen desactualizados respecto de noviembre (últimos registros en octubre). No se modificaron. La rotación se contrastó con los storyboards recientes: rapaces usa `papel_rasgado_capas`, intermareales `atlas_antiguo`, PAV1 `microscopio_psicodelico` y EpTFIIAγ `rubber_hose_1930s`; no se repitió el estilo en este nuevo borrador.

### Radar científico y señales de tendencia — 09:59 CDMX

- Se actualizó `docs/briefs/2026-11-27_RADAR_CAPCOT.md`, commit `90c4114b13ce4c08c2f3bafeb766e4e6395f4637`, con shortlist vigente de cinco candidatos: EpTFIIAγ, malaria m⁶A/YTH.2, actividad fuera del blanco de CAY10641/CAY10650, CAST tipo I-F y circuito intestino-cerebro de Drosophila. Los candidatos históricos previos permanecen sin cambio y no se cuentan de nuevo.
- Los dos candidatos añadidos se respaldan en artículos primarios de Nature publicados el 25-11-2026: DOI `10.1038/s41586-026-11196-x` (CAST) y `10.1038/s41586-026-11315-8` (circuito intestino-cerebro). No se creó storyboard para ninguno: no hay coordenadas geográficas de ensayo publicadas para satisfacer el mapa exigido.
- Apertura directa de RSS en esta sesión: ScienceDaily (tres feeds) 400 `Unsupported content-type: application/xml`; Phys.org 400 `text/xml`; NASA 400 `application/rss+xml`; ESA 404; Nature RSS 400 `application/rss+xml`; UNAM Global 400 `application/rss+xml`; EurekAlert, SINC y Google Trends RSS no accesibles desde esta herramienta. No se ejecutó localmente `tendencias.py` en este corte.
- Respaldo HTML oficial de Google Trends México: 250 tendencias en las últimas 24 h; “agujero de la capa de ozono” aparece con 2K+ búsquedas y actividad unas 6 h antes. Se registra como señal `PENDING_SOURCE`, no como candidato.
- Crossref y `doi.org` devolvieron “URL ... is not accessible via this tool”; ningún DOI nuevo se marca verificado por resolver.

### Estado de los proyectos existentes

- Rapaces 30-nov: `FAIL/82`, una revisión fría independiente registrada el 27-11 02:04; no repetir ni reescribir.
- PAV1 27-nov: `FAIL/0`, `REVISION_INDEPENDIENTE_AUSENTE`; no promover.
- Intermareales 27-nov 23:30: `PASS/90` existente, sin cambio de narración; no repetir. Sigue el conflicto con Stubbs en main, procesamiento previo y medios no verificados.
- Lote 5–7 nov: 12 proyectos sin cambios narrativos posteriores al último control; se conservan los QA previos (2 PASS / 10 FAIL), sin repetir PASS ni modificar copias bloqueadas.
- No se disparó workflow, no se envió payload, no se creó ni modificó `cola/estado`, no se generaron medios ni se consumieron créditos.


### Relectura individual del lote canónico 5–7 nov — 27-11 09:59 CDMX

Se recuperó la lista canónica desde `ajustes_entre_modelos/PARA_CHATGPT_semana_01-07nov.md` y se leyeron los doce `proyectos/<id>/storyboard.json`. No se repitió la evaluación narrativa: se inspeccionó el registro existente y no se reescribió ninguna narración.

| project_id | narrative_qa | score | checks true | flags |
|---|---:|---:|---:|---|
| `2026-11-05_kids-dia-en-venus` | PASS | 88 | 7/7 | — |
| `2026-11-05_comida-palomitas` | FAIL | 82 | 5/7 | `APERTURA_DEFINICIONAL_NO_IN_MEDIAS_RES`; `ESCENA_6_REITERA_CAUSAS_DE_GRANOS_NO_REVENTADOS_SIN_INFORMACION_NUEVA` |
| `2026-11-05_inter-arboles-se-comunican` | FAIL | 78 | 6/7 | `APERTURA_GENERICA_NO_IN_MEDIAS_RES` |
| `2026-11-05_inter-rayo-globular` | FAIL | 81 | 6/7 | `APERTURA_HISTORICA_DESCRIPTIVA_NO_IN_MEDIAS_RES` |
| `2026-11-06_kids-ballena-azul-corazon` | FAIL | 80 | 6/7 | `PAYOFF_SOBREAFIRMA_CASI_SE_DETIENE` |
| `2026-11-06_comida-aguacate-negro` | FAIL | 79 | 5/7 | `REPETICION_ESCENAS_5_6_SIN_AVANCE_CAUSAL` |
| `2026-11-06_inter-ranas-congeladas` | FAIL | 83 | 5/7 | `REPETICION_ESCENAS_5_6_LIMITES_DE_ESPECIE_Y_CONDICIONES` |
| `2026-11-06_inter-arena-cantante` | PASS | 94 | 7/7 | — |
| `2026-11-07_kids-huesos-bebe` | FAIL | 82 | 5/7 | `ESCENA_6_REPITE_VARIACION_DE_CONTEO_Y_FUSION` |
| `2026-11-07_comida-hielo-caliente` | FAIL | 81 | 6/7 | `APERTURA_DE_CREENCIAS_NO_IN_MEDIAS_RES` |
| `2026-11-07_inter-pulpo-suenos` | FAIL | 72 | 2/7 | `FUENTE_PRIMARIA_CORRESPONDE_A_OCTOPUS_LAQUEUS_NO_INSULARIS`; `REPETICION_ESCENAS_5_6_Y_PAYOFF_VAGO` |
| `2026-11-07_inter-nubes-pesan` | FAIL | 78 | 4/7 | `ESCENA_7_REITERA_CIFRA_Y_LIMITE_SIN_PAYOFF_DE_SUSPENSION` |

**Verificación Grok:** los doce `cola/estado/<id>.json` devolvieron HTTP 404; se conserva `RECEPCION_GROK_NO_CONFIRMADA` para cada uno. No se creó ni editó ningún estado.

**Resultado:** 2 PASS / 10 FAIL, sin cambios narrativos ni nuevos PASS. Las doce copias heredadas con slugs alternativos permanecen en `cola/bloqueados/` sin renombrar, fusionar ni borrar; la copia anidada de `2026-11-07_comida-hielo-caliente` en main conserva el video_id y publishAt históricos ya documentados. No se redispatcha ninguna.


## Revalidación complementaria — 27-11-2026 10:26 CDMX

### Storyboards vigentes y compuertas

Se releen los cuatro storyboards actuales del backlog y se consulta individualmente `cola/estado/<project_id>.json`. Los cuatro estados devolvieron HTTP 404; se conserva exactamente `RECEPCION_GROK_NO_CONFIRMADA` para cada ID. No se creó ni editó ningún estado.

| project_id | slot | narración | duración total | narrative_qa | fuentes / handoff | decisión |
|---|---:|---:|---:|---|---|---|
| `2026-11-27_dato-pav1-bacteriofago` | 07:00 | 187 palabras / 8 escenas | 84 s | FAIL/0; `REVISION_INDEPENDIENTE_AUSENTE` | URL primaria verificada; DOI no acreditado por Crossref en esta sesión; estado 404 | `NOT_DISPATCHABLE`; slot ya transcurrido |
| `2026-11-27_dato-registros-intermareales-1950s` | 23:30 | 173 palabras / 8 escenas | 84 s | PASS/90; siete checks true | cuatro fuentes con DOI/resolvedor registrados como verificados; estado 404 | `NOT_DISPATCHABLE`; `CONFLICTO_DE_SLOT_ENTRE_RAMAS` con Stubbs en main |
| `2026-11-30_liquen-gen-cereales` | 17:00 | 199 palabras / 8 escenas | 84 s | ausente | Nature primaria accesible; DOI `10.1038/s41586-026-11151-w` sigue `PENDING_CROSSREF`; estado 404 | `NOT_DISPATCHABLE`; falta QA independiente y validación oficial |
| `2026-11-30_rapaces-clima-reino-unido` | 07:00 | 182 palabras / 8 escenas | 84 s | FAIL/82; giro científico no explicado | DOI `10.3389/fevo.2026.1922294` sigue `PENDING_CROSSREF`; fuentes oficiales auxiliares accesibles; estado 404 | `NOT_DISPATCHABLE`; no reescribir ni repetir QA válido |

En los cuatro casos se comprobó: voz `es-MX-JorgeNeural` (+7%, -2Hz), gancho de seis palabras o menos, estilo presente en catálogo, prefijo `prompt_base` en prompts, capa mapa con coordenadas/bounds y fuente, capa de dato/gráfico, ambiente y SFX por escena, 170–235 palabras, 7–9 escenas, cortinilla de 6 s, total de 75–90 s, `approved_assets=[]`, `export.render_status=NOT_GENERATED` y publicación pendiente. El prechequeo fue estático/parcial; **no es ejecución del validador oficial**.

No se creó `narrative_qa` nuevo ni se promovió ningún storyboard. No se alteró la narración de PAV1, intermareales, liquen ni rapaces. El PASS/90 de intermareales se conserva sin repetirlo; el FAIL/82 de rapaces se conserva sin repetirlo.

### Producción preexistente, slots y Actions

- `main/data/rehechos_2026-11-22.json` confirma producción previa y programación: 27-nov 10:00 (miel, video_id `p06UCGu0-Og`) y 15:00 (ola azul, `HKpani8TTeY`); 28-nov 10:00 (dunas, `6VUxaJtqbF0`) y 15:00 (Júpiter, `Dx3lqkAb8Sc`); 29-nov 10:00 (Dunkelflaute, `m1FeS0mhfZ4`). Se clasifican `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`; no se duplican ni cancelan.
- `main/data/publicaciones.json` no contiene todavía esos registros del 27–29 nov; no se usa por sí solo como prueba de ausencia. `main/data/duplicados_privatizados_2026-11-23.json` y `main/data/vistas_historico.json` no contienen los IDs originales ni los nuevos de esos cinco paquetes. El estado actual de los IDs antiguos no queda acreditado por esos archivos: riesgo de programación histórica **no verificado**, sin tocar videos.
- El workflow `.github/workflows/capcot-grok-dispatch.yml` escucha JSON plano en `cola/entrada/*.json`; no se disparó ni se envió payload. El run `46009658666` de `Trabajador de cola` terminó SUCCESS, pero el log literal fue `[trabajador] sin trabajo en cola.`; no es acuse Grok.
- El run `46032854305` de PR #3 terminó SUCCESS en CodeQL. PR #3 sigue abierto, draft y no mergeable; PR #15 sigue abierto y no mergeable. Ninguno acredita ejecución de `scripts/validar_storyboard.py`.
- El intento de clonar el repositorio para ejecutar el validador local falló literalmente: `fatal: unable to access 'https://github.com/marcojpad-hash/capcot-capsulas-imaginantes.git/': Could not resolve host: github.com`. No se disparó CI como alternativa porque el workflow de dispatch puede escribir handoffs y enviar webhook.

### Resultado

- **EJECUTADO:** relectura de cuatro storyboards, cuatro consultas individuales de estado Grok, contraste con main, lectura de Actions/logs y prechequeo estructural parcial.
- **VERIFICADO:** cuatro 404 de estado Grok; un conflicto de slot entre ramas; cinco paquetes con producción/programación previa en main; worker sin trabajo; CodeQL exitoso sin validador estructural.
- **PENDIENTE:** auditoría narrativa verdaderamente independiente para PAV1 y liquen; DOI/Crossref para liquen y rapaces; ejecución del validador oficial; confirmación externa del estado de IDs antiguos.
- **NO REALIZADO:** promoción a cola, dispatch, publicación, reprogramación, cancelación, cambios en `data/*.json`, main, secretos o permisos.


## Actualización de radar y Trends — 27-11-2026

- Se abrió el respaldo HTML oficial de Google Trends México: 253 tendencias en las últimas 24 h. “agujero de la capa de ozono” aparece con 2K+ búsquedas y actividad aproximada de seis horas antes del corte.
- Se localizó la fuente primaria oficial que faltaba: comunicado NOAA/NASA del 04-11-2026. Reporta el séptimo mayor agujero por área media estacional en 48 años; 9.6 millones de millas² de promedio (7-sep a 13-oct), máximo de 10.5 millones de millas² el 18-sep y mínimo de 105 DU sobre el Polo Sur el 17-oct. La explicación atribuye el tamaño inusual al vórtice polar y conserva la lectura de recuperación a largo plazo por el Protocolo de Montreal.
- La señal cambia de `PENDING_SOURCE` a `SEÑAL_TREND_CON_FUENTE_PRIMARIA`, pero no entra a la shortlist de cinco ni se convierte en `DATO_DIA`: la fuente tiene 23 días y no satisface la ventana de 48 h. No se crea storyboard ni se asigna slot.
- **EJECUTADO y VERIFICADO:** radar actualizado y leído de vuelta; commit `6c82ca9b80a2a518a0c8e05560380ca7ff5a9f69`, blob `dca4d3a89d5d19e4fbf6ba58920093f2a0e9fcb2`.
- Los diez RSS de `scripts/tendencias.py` y Google Trends RSS fueron intentados por apertura directa; se conservan los errores exactos en el radar. El respaldo HTML sí abrió. No se afirma ejecución local de `tendencias.py`.


## Revalidación de slots y Actions — 2026-11-27 12:13 CDMX

Esta revalidación supersede la conclusión anterior de que main no ocupaba slots del 27-11. Se consultaron main y la rama de trabajo en solo lectura; no se modificaron main, data/*.json, cola ni estados Grok.

### Main: ocupación real del 27-11
- **07:00 — microondas.** `docs/briefs/produccion_2026-11-23_28/plan_semana.json` registra QA PASS, 77 s, `yt_videoId=nd0rs6iVy8E`, `publishAt=2026-11-27T13:00:00Z` y un MP4 bajo `/workspace/capcot_prod_20261121/`. El plan aún indica privacidad `private`; no hay `data/historial_youtube.json` ni resultados de búsqueda para `historial_youtube`. **No se afirma publicación pública**. El ID tiene `publishAt` vencido respecto del corte y su estado externo requiere revisión en YouTube Studio. El MP4 no está en el árbol Git: `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`. Esto invalida la conclusión previa de ausencia de conflicto para PAV1/07:00: **CONFLICTO_DE_SLOT_ENTRE_RAMAS** y `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`.
- **17:00 — bacterias-vuelta-oxigeno.** Main contiene `proyectos/2026-11-27_bacterias-vuelta-oxigeno/`; `programacion.json` registra `programado_sin_montar` y `publish_at=2026-11-27T23:00:00Z`, sin `video_id`, render ni salida encontrada. Es una reserva/programación, no evidencia de producción montada; aun así ocupa el slot de main: **CONFLICTO_DE_SLOT_ENTRE_RAMAS** y no redispatchar. El storyboard tiene 84 palabras/7 escenas y no contiene `narrative_contract` ni `narrative_qa`: **NOT_DISPATCHABLE**. No se corrigió porque está en main.
- **23:30 — animal-stubbs.** Main registra hueco 27-11 23:30 y `render.log` confirma 86.13 s; metadata apunta a un MP4 bajo `/workspace/capcot_main/`, ausente del árbol. Sin `video_id` ni `publishAt` en metadata. **PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR**, **MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO** y conflicto con intermareales/23:30. No se afirma publicación.

### Rama feature: clasificación actual
- `2026-11-27_dato-pav1-bacteriofago`, 07:00: 187 palabras/8 escenas; QA FAIL/0 por independencia no acreditada. Conflicto con microondas de main; **NOT_DISPATCHABLE**.
- `2026-11-27_dato-registros-intermareales-1950s`, 23:30: PASS/90 previo sin cambio narrativo; conflicto con animal-stubbs de main; **NOT_DISPATCHABLE**.
- `2026-11-30_rapaces-clima-reino-unido`, 07:00: FAIL/82; `giro_cientifico_explicado=false`; estilo `papel_rasgado_capas` repetido frente al proyecto hidrotermal del 18-11; **NOT_DISPATCHABLE**.
- `2026-11-30_liquen-gen-cereales`, 17:00: 199 palabras/8 escenas; sin `narrative_qa`, DOI aún PENDING_CROSSREF; **NOT_DISPATCHABLE**.
- Para los cuatro IDs anteriores, `cola/estado/<id>.json`, `cola/entrada/<id>.json` y `cola/entrada/<id>/storyboard.json` devolvieron 404. Registrar exactamente **RECEPCION_GROK_NO_CONFIRMADA**; no se crearon estados ni entradas.
- Main reserva además animal-cher-ami/30-11 23:30; no coincide con rapaces/07:00 ni liquen/17:00. No se detectó conflicto de esos dos slots con main.

### Acciones y límites
- Worker run `46009658666`: job `trabajar` SUCCESS; log: `[trabajador] sin trabajo en cola.` Checkout de ese run fue main `92d6c034b12a86785a5d12eb22e634f8453cd510`, anterior a los paquetes que aparecen en el main actual; el resultado no acredita el estado posterior.
- CodeQL run `46032854305`: Analyze (python) y Analyze (actions) SUCCESS; no ejecuta el validador estructural ni verifica DOI.
- Al corte inicial de esta revalidación, PR #3 seguía OPEN/DRAFT; no se hizo merge ni dispatch.
- `data/publicaciones.json` no refleja los registros de 27-11; `data/rotacion.json` y `data/estilos_usados.json` llegan aproximadamente al 21-11 y `data/temas_del_dia.json` al 28-10. Se consideran incompletos para estado actual; se mantienen solo lectura.
- No se ejecutó `scripts/validar_storyboard.py`; el archivo se leyó por GitHub, pero no se obtuvo un runtime local del repositorio. No se atribuye PASS estructural a CI/CodeQL.

Resultado: no hay promoción segura ni slot libre para el 27-11. No se generaron medios, no se creó cola, no se dispararon workflows y no se modificó main.


### Trazabilidad de esta revalidación
- El paquete `2026-11-27_bacterias-vuelta-oxigeno` apareció en main mediante commit `0e5bc28010ee93896d041ed4f4b5f592d43fe2b0` (2026-11-27 16:37:55Z). El worker `46009658666` había checkout `92d6c034b12a86785a5d12eb22e634f8453cd510` antes de ese commit; su log “sin trabajo en cola” no cubre el estado posterior.
- La revalidación quedó registrada y verificada por lectura de vuelta: radar en commit `b51f69465606f25880b1394cfcb0eabaaf04c6ef`; control/trazabilidad en commits `5a3ff4cfb7efe62c708b196af582bb3509ebb74d`, `ed119363c1fc16ba2fb2a2edf7cf9098f5d462dc` y `caef06be256dfcece28ddbfb8cf1d1df741e4352`. PR #3 permanece OPEN/DRAFT; no se hizo merge ni dispatch.


## QA narrativo independiente — 27-11-2026 12:32 CDMX

Esta sección supersede los estados narrativos anteriores de PAV1 y EpTFIIAγ. Se realizó una ejecución/conversación distinta de la redacción, ocultando título, resumen, arco, notas y `narrative_contract`; la revisión leyó únicamente la narración concatenada de cada storyboard. No se cambió narración, claims, estructura de escenas ni decisiones editoriales.

| project_id | QA anterior | QA actual | checks | commit / blob verificado |
|---|---|---|---:|---|
| `2026-11-27_dato-pav1-bacteriofago` | FAIL/0 por revisión independiente ausente | **PASS/90** | 7/7 | `653a7ad38bb136229414bcd180aa9971d5d5f38e` / `0ed2ef7b88a27d24997cfe7e0f9a019a0408d141` |
| `2026-11-30_liquen-gen-cereales` | QA ausente | **PASS/93** | 7/7 | `a3d9e5cb991f29a296a06a52a9a045378a7a16d4` / `20ea3a0e9b78f9b583565f5c74f89b1abff971ad` |

En ambos registros se guardó `review_basis=lectura_en_frio_solo_narracion`, `reviewer_role=auditor_capcot_independiente`, siete checks true y `critical_flags=[]`. PAV1 conserva explícito el límite: el ensayo preventivo fue en tomate; no demuestra eficacia de campo en viñedos. EpTFIIAγ conserva el límite: líneas experimentales, no variedad comercial. No se repitió el PASS/90 de intermareales ni el FAIL/82 de rapaces porque sus narraciones no cambiaron.

### Relectura de handoff y estado Grok

Se consultaron individualmente para los cuatro storyboards vigentes:
- `cola/estado/<project_id>.json`;
- `cola/entrada/<project_id>.json`;
- `cola/entrada/<project_id>/storyboard.json`;
- `salidas/<project_id>/`.

Los 16 accesos devolvieron HTTP 404. Se conserva exactamente `RECEPCION_GROK_NO_CONFIRMADA` para cada ID; no se creó ni editó ningún estado Grok ni entrada de cola. Clasificación: los cuatro continúan `NOT_DISPATCHABLE`.

- PAV1 / 27-11 07:00: QA narrativo ahora PASS/90, pero slot en conflicto con microondas de main y procesamiento previo; no redispatchar.
- Intermareales / 27-11 23:30: PASS/90 previo sin cambio; conflicto con Stubbs de main y medios no verificados; no redispatchar.
- EpTFIIAγ / 30-11 17:00: QA narrativo ahora PASS/93; no se encontró conflicto de slot en main. Continúa bloqueado por DOI/Crossref y validador estructural oficial no ejecutado.
- Rapaces / 30-11 07:00: FAIL/82 y estilo repetido; no reescribir ni repetir QA.

### Compuertas que siguen separadas

- El DOI de PAV1 (`10.3389/fpls.2026.2008228`) y el de EpTFIIAγ (`10.1038/s41586-026-11151-w`) aparecen en sus artículos primarios, pero Crossref/doi.org no fueron accesibles; siguen `PENDING_CROSSREF`.
- `scripts/validar_storyboard.py` fue leído. `--structural-only` es una compuerta estructural distinta y no autoriza handoff; el modo completo con `--check-doi` es obligatorio. No se ejecutó el validador oficial ni se disparó CI en este corte. La recuperación local del repositorio sigue afectada por el error de DNS ya registrado (`Could not resolve host: github.com`); la lectura por GitHub no se presenta como ejecución del script.
- No hubo promoción, dispatch, generación de medios, programación, publicación ni cambios en `data/*.json` o `main`.

## Revalidación de backlog — lote 5–7 nov y proyectos interdiarios — 27-11-2026 12:36 CDMX

### Lote obligatorio de 12 IDs

Se releó `data/horario_semana_2026-11-01_07.json` (blob `a567b140bab9616ab8e52666925aa79dd267223e`) y los 12 `storyboard.json`. Los cuatro campos de identidad/slot (`project_id`, `fecha_objetivo`, `slot_local`, `slot_cesta`) coinciden con el horario en **12/12**. No se modificó el horario.

| ID | Slot | QA vigente | Blob actual |
|---|---|---:|---|
| `2026-11-05_kids-dia-en-venus` | 05-nov 07:00 kids | PASS/88 | `3660c16f866d6ec74471e6ad88e640ea7df7df1d` |
| `2026-11-05_comida-palomitas` | 05-nov 13:30 comida | FAIL/82 | `8c913dc8ad16b005735da9ebe882206d285c96bf` |
| `2026-11-05_inter-arboles-se-comunican` | 05-nov 17:00 intermedio_1 | FAIL/78 | `05618f1d5d2cd8f713ee43ac802bcfb04bb9bb1d` |
| `2026-11-05_inter-rayo-globular` | 05-nov 17:45 intermedio_2 | FAIL/81 | `5cd02d9a5d21ecdbd416a2858e433395cb9acc63` |
| `2026-11-06_kids-ballena-azul-corazon` | 06-nov 07:00 kids | FAIL/80 | `37eda55883011c0f7a2ec022c43e880d33b58313` |
| `2026-11-06_comida-aguacate-negro` | 06-nov 13:30 comida | FAIL/79 | `d63b2afcbf22a579b7d5d8ced11265aca8b3dc2a` |
| `2026-11-06_inter-ranas-congeladas` | 06-nov 17:00 intermedio_1 | FAIL/83 | `84585c042be07fa1ea52f1c9de310e83a1105f16` |
| `2026-11-06_inter-arena-cantante` | 06-nov 17:45 intermedio_2 | PASS/94 | `386ad015311e277782a09f82a72b7e1118b72e69` |
| `2026-11-07_kids-huesos-bebe` | 07-nov 07:00 kids | FAIL/82 | `981f384d44db08469ef8290b988b96fd26bc4cd0` |
| `2026-11-07_comida-hielo-caliente` | 07-nov 13:30 comida | FAIL/81 | `fe8baf47a0e97f4c3607a187f6bac5524546e875` |
| `2026-11-07_inter-pulpo-suenos` | 07-nov 17:00 intermedio_1 | FAIL/72 | `89080ebda22783403d5d8033d52c93dd00bc5fde` |
| `2026-11-07_inter-nubes-pesan` | 07-nov 17:45 intermedio_2 | FAIL/78 | `190090e434d16acb4126e83d86fea17ad6e8f4e6` |

Los dos PASS (Venus 88 y arena 94) conservan siete checks true y flags vacías; no se repitió la lectura narrativa porque no cambió el contenido. Los diez FAIL conservan sus flags y no se reescribieron.

Inventario estático, no ejecución del validador oficial: **85 escenas**, los seis campos dramáticos obligatorios ausentes en las 85 escenas (**510 omisiones**), y **75 escenas con SFX vacío**. Los 12 tienen `approved_assets=[]`, `export.render_status=NOT_GENERATED`, `export.filename` ausente y ninguna referencia `asset_filename`, `asset_type` ni ruta de asset. Esta comprobación estática no sustituye `scripts/validar_storyboard.py`; por los campos ausentes, ninguno pasa el precheck estructural.

Los 12 archivos `cola/estado/<id>.json` devolvieron HTTP 404. `cola/entrada/` contiene solo `.gitkeep` y la carpeta heredada del 09-nov; no hay entradas planas de estos 12. En `main:data/publicaciones.json` aparecen `2026-11-07_comida-hielo-caliente` y `2026-11-07_inter-nubes-pesan`; el primero también aparece en `main:data/rotacion.json`. Se conserva el bloqueo de redispatch y la discrepancia histórica de publicación ya documentada. No se creó ninguna copia de cola.

### Backlog interdiario

- `2026-11-18_dato-catorce-campos-hidrotermales`: blob `912fb2222ea5106d763c9e94bd95d9f9d66ebe41`, 8 escenas/198 palabras, QA vigente FAIL/68 con cuatro flags; narración y QA sin cambio. `ESTADO_EJECUCION.md` ya dice `BORRADOR_EN_PROYECTOS_NO_APTO_PARA_PROMOCION`. Estado Grok, cola plana y cola anidada devolvieron 404. Se conserva fuera de cola.
- `2026-11-15_dato-quasar-pareja-cosmic-dawn`: Issue #11 sigue abierto; PR #14 sigue OPEN/NOT MERGED y apunta a main. Su diff añade `asset_filename` a las ocho escenas, incompatible con el contrato de preproducción; tampoco ejecuta `--check-doi` y conserva FAIL/82 histórico. El issue exige auditor distinto de ChatGPT (Groq/Gemini); no se atribuye esa auditoría a este run. Estado Grok y ambas rutas de cola devolvieron 404. No merge, no promoción y no redispatch.

### Resultado de backlog

- Lote 5–7 nov: 12/12 identidades y slots correctos; 2 PASS narrativos, 10 FAIL; 0/12 supera el precheck estructural; 0/12 con recepción Grok confirmada.
- Backlog interdiario comprobado: 18-nov sigue FAIL/68 y correctamente marcado como borrador; cuásares sigue pendiente de auditoría por modelo distinto y PR #14 no integrado.
- No se modificaron `data/*.json`, main, cola/estado, narraciones, claims ni decisiones editoriales.

## Revalidación de profundidad del handoff — 27-11-2026 12:36 CDMX

- `.github/workflows/capcot-grok-dispatch.yml` blob `47bbd228cfce5a1d402dc952e283e8d0f8e37030`: el trigger `push.paths` observa solo `cola/entrada/*.json`; tanto el selector del evento como `workflow_dispatch` enumeran archivos con `find cola/entrada -maxdepth 1 -type f -name '*.json'`. Las carpetas anidadas no disparan ni entran en la selección plana del workflow.
- `scripts/procesar_cola.py` blob `64c1f94c3cf60adee25f5a869cb03633a420db97` sí admite dos formas: `cola/entrada/<id>.json` y `cola/entrada/<id>/storyboard.json`. Esta capacidad del procesador no corrige la profundidad plana del workflow.
- `scripts/registro_editorial.py` blob `c95a5fbbd0e8366877fc4e64d2f96fe096fff668` ya recorre recursivamente `storyboard.json` y dispone de `handoffs_grok_inbox()` con lectura recursiva. Esto supersede la nota obsoleta del prompt de auditoría que afirmaba que el registro no recorría `handoffs/grok_inbox/`.
- Un marker en `handoffs/grok_inbox/` sigue siendo solo un payload/marker pendiente. La única confirmación individual de recepción es `cola/estado/<project_id>.json`; nunca se crea ni modifica desde este operador.
- Clasificación por ruta: los cuatro borradores de `proyectos/` no son dispatchables; la entrada heredada anidada del 09-nov no activa el workflow de push ni la selección plana de `workflow_dispatch`. No se disparó workflow ni se envió payload.

## Historial de publicación y riesgo de IDs antiguos — 27-11-2026 12:47 CDMX

No existe un archivo separado `historial_youtube` en el árbol de esta rama ni en `main` (ruta/directorio 404). La trazabilidad disponible se verificó en `main:data/publicaciones.json` (blob `a822459849571a443196e6a5b5d4ee73d109b1cd`), `main:data/rotacion.json` (blob `1cb16c1cfad8b968e24221793047df27d83eb5e0`) y los horarios/histórico de vistas. Esto no equivale a una consulta actual de la API de YouTube.

- `2026-11-07_comida-hielo-caliente`: registro de publicación del 11-11, YouTube ID `HSgrnejAcaI`, `publishAt_utc=2026-11-11T19:30:00Z`; la nota almacenada dice que `videos.list` no lo encontró el 12-11 07:20 CDMX, mientras TikTok y Facebook figuran publicados. El estado actual del ID de YouTube no se pudo confirmar.
- `2026-11-07_inter-nubes-pesan`: YouTube ID `4Qpl17Ts_vI`, `publishAt_utc=2026-11-12T13:00:00Z`; TikTok y Facebook figuran publicados.

Ambos son `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`; no cancelar, duplicar ni reprogramar. La ausencia de un `historial_youtube` separado queda como limitación de trazabilidad, no como evidencia de que un ID esté libre.

## Revalidación de paquete en main — 27-11-2026 14:04 CDMX

Se detectó un paquete adicional en `main`: `2026-11-27_bacterias-vuelta-oxigeno`. Main se mantuvo en solo lectura.

- **Slot ocupado en main:** `programacion.json` declara `2026-11-27 17:00` CDMX (`publish_at=2026-11-27T23:00:00Z`), estado `programado_sin_montar`, privacidad `private` hasta la hora programada. La política horaria vigente de `main:data/horarios.json` coloca 17:00 dentro de 16:30–18:00. PAV1 permanece en feature a 07:00 y registros intermareales a 23:30; no hay conflicto con esos dos paquetes, pero **17:00 del 27-nov queda ocupado en main**. Cualquier promoción de feature para la misma fecha+slot debe clasificarse `CONFLICTO_DE_SLOT_ENTRE_RAMAS`; no asignar otro slot dentro de la misma ventana.
- **No redispatchar:** la programación y `publish_at` preexistentes activan `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`, aunque el estado diga `programado_sin_montar`. No se canceló ni modificó la programación.
- **Ruta de handoff defectuosa:** `cola/entrada/2026-11-27_bacterias-vuelta-oxigeno/` contiene `fuentes.md` y `storyboard.json`, pero el contenido leído de este último es literalmente `PLACEHOLDER`, no JSON. El workflow de feature selecciona únicamente archivos planos `cola/entrada/*.json` con profundidad 1; la carpeta anidada no es dispatchable. `cola/estado/2026-11-27_bacterias-vuelta-oxigeno.json` devuelve 404: `RECEPCION_GROK_NO_CONFIRMADA`.
- **Medios no verificados:** el storyboard de main declara `export.filename=capsula.mp4`, pero el directorio del proyecto solo contiene `fuentes.md`, `metadata.json`, `programacion.json` y `storyboard.json`; la entrada anidada solo contiene `fuentes.md` y el placeholder; `salidas/2026-11-27_bacterias-vuelta-oxigeno/` devuelve 404. No se encontró el MP4 en las rutas verificadas: `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`.
- **Fuente primaria:** Nature Physics publicó el artículo el 27-nov-2026 y el DOI `10.1038/s41567-026-03530-x` resuelve a la página editorial. Crossref REST no fue accesible en esta ejecución; se registra resolución editorial, no verificación Crossref. [Artículo primario](https://www.nature.com/articles/s41567-026-03530-x).
- **Precheck estático del storyboard de main:** 84 palabras, 7 escenas, duración declarada 82s, voz es-MX-JorgeNeural +7% -2Hz; no existe `narrative_contract`, `narrative_qa`, `approved_assets` ni `publicacion.status`; `export.filename` está presente. Faltan campos dramáticos en 7/7 escenas (42 omisiones). No se ejecutó el validador oficial.
- **QA narrativo:** no hay revisión independiente persistida ni identidad de autor/revisor que permita acreditarla. Por contrato se mantiene `FAIL/0`, `critical_flags=["REVISION_INDEPENDIENTE_AUSENTE"]`; no se escribe `narrative_qa` en main. La lectura del contenido revela apertura en forma de pregunta genérica, giro físico nombrado sin explicación suficiente y ausencia de límite explícito entre el resultado de laboratorio y la infección in vivo. El cierre "truco ... para sobrevivir" excede lo demostrado por el estudio. No se reescribió narración ni claims.
- **Publicación/rotación:** el proyecto no aparece en `main:data/publicaciones.json` ni en `main:data/rotacion.json`; esto no anula la programación individual de 17:00. Sin `video_id` observado. Clasificación final: `NOT_DISPATCHABLE`, `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`, `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`, `RECEPCION_GROK_NO_CONFIRMADA`; el slot 17:00 queda reservado contra cualquier paquete paralelo de feature.

No se modificaron `main`, `data/*.json`, cola/estado, programación, medios ni decisiones editoriales. Las referencias de webhook del workflow están presentes; no se leyeron ni se expusieron valores de secretos.


## PRs y CI revalidados — 27-11-2026 14:04 CDMX

- **PR #15 — validador/DOI y coordenadas:** sigue OPEN, sin merge y `mergeable=false`; rama `fix/capcot-map-coordinate-types-20261122`, base feature. El último run de Semgrep (#45310165026, 24-nov) terminó FAILURE: 26 hallazgos bloqueantes, exit code 1; SARIF sí fue cargado. Ese workflow ejecutó Semgrep, no las pruebas unitarias. La supresión añadida para `HTTPSConnection` no produjo un CI verde. No se fusiona ni se declara verificado el cambio.
- **PR #13 — auditoría cuásares:** sigue OPEN. Su informe no satisface la compuerta vigente de lectura en frío solo de narración: cita duración de escenas, metadatos y estado DOI; la revisión de integración también señaló rangos de líneas sin SHA reproducible y conclusiones que no se desprenden del dato citado. No se acredita como `narrative_qa` PASS.
- **PR #14 — corrección cuásares:** sigue OPEN y no mergeable. Es posterior a la auditoría del blob `54c8ade`; no hay una revisión independiente posterior del storyboard corregido. Se conserva el estado no apto y no se repite el QA anterior como si cubriera el nuevo texto. La siguiente compuerta es una lectura en frío realizada por un revisor distinto del redactor, con solo narración concatenada.
- Los PRs antiguos/dependencias (#3, #4–#9 y #37 en U7) permanecen fuera de esta acción; no se abrió, cerró ni fusionó ningún PR.

- **Cierre de slots del 27-nov:** 07:00 está ocupado por PAV1 en feature, 17:00 por el paquete programado en main y 23:30 por registros intermareales en feature. No queda slot autorizado libre para otro storyboard hoy; no se creó uno.


## Revalidación posterior de PR y CI — 27-11-2026

- **PR #3 — rama principal de trabajo:** sigue OPEN, base `main`, head `2b8a289d752eb5b5c1a53f2af3e636b136abfa0c`. Los checks CodeQL, Analyze (actions), Analyze (python) y `validar` terminaron SUCCESS. La lectura de `mergeable_state` devuelve `dirty` y `mergeable=false`: el PR no está integrable en este corte. No se intentó resolver conflictos ni fusionar.
- El job `validar` del run `46073709847` ejecutó literalmente `python scripts/validar_storyboard.py proyectos/2026-11-18_dato-kuroshio-puente-atmosferico/storyboard.json`; salida `OK`. El paso adicional confirmó `production_mode=storyboard_only`, `approved_assets=[]` y `export.render_status=NOT_GENERATED`. No incluyó `--check-doi`; acredita únicamente la validación textual/estructural y la ausencia de medios declarados, no Crossref.
- **PR #15 — booleanos en coordenadas y Crossref:** sigue OPEN, base feature, sin merge. El check `Semgrep OSS` terminó SUCCESS, pero el job separado `semgrep` del run `45310165026` terminó FAILURE, exit code 1. El log resume 26 hallazgos bloqueantes en 1,104 archivos. El SARIF descargado contiene 27 registros: 11 referencias mutables de Actions, 11 usos dinámicos de urllib, 2 usos de subprocess con argumentos tainted, 1 uso dinámico de `globals()`, 1 MD5 y 1 `HTTPSConnection`.
- El único registro SARIF dentro de los dos archivos modificados por PR #15 es `python.lang.security.audit.httpsconnection-detected.httpsconnection-detected` en `scripts/validar_storyboard.py:27`. El cambio fija el host `api.crossref.org` y usa contexto TLS verificado, pero Semgrep sigue marcándolo pese al comentario de supresión. Los demás hallazgos están en otros archivos del árbol; no se atribuyen todos al diff de PR #15. No se modificó la rama del PR ni se relajó el escaneo.
- **Kuroshio:** la actualización de `ESTADO_EJECUCION.md` registra el run `45898334232` (SUCCESS), commit ejecutado `8461bf23dcb99562340d751ebbbfb2731a085524`, comando textual sin `--check-doi` y salida `OK`. La estructura sigue acreditada para el blob ejecutado; DOI `10.1038/s41561-026-02139-2` continúa `PENDIENTE_RESOLVEDOR` y el estado permanece `BORRADOR_EN_PROYECTOS_NO_APTO_PARA_PROMOCION`.
- No se modificaron `main`, `data/*.json`, storyboards, cola, estados Grok, workflows, secretos, medios ni programación. No hubo dispatch, publicación, merge ni generación de medios.


## Revalidación de backlog 30-nov — 27-11-2026

Se releyó el inventario de `feature/capcot-video-discovery-continuity` y se localizaron **dos** borradores para el 30-nov, no uno. La rama `main` no contiene proyectos, entradas ni salidas para esos IDs; `main:data/publicaciones.json` y `main:data/rotacion.json` tampoco contienen registros del 30-nov. No hay conflicto de slot entre ramas en este corte.

### `2026-11-30_rapaces-clima-reino-unido` — 07:00 CDMX

- 8 escenas, 182 palabras, 84 s declarados, 9:16 y voz `es-MX-JorgeNeural` `+7%` / `-2Hz`.
- `narrative_qa` ya persistido: **FAIL/82**; `giro_cientifico_explicado=false`; `critical_flags=["GIRO_CIENTIFICO_NOMBRADO_PERO_NO_EXPLICADO"]`. La revisión se registró en un commit posterior al borrador; no se repitió ni se reescribió la narración.
- Fuente primaria declarada: Frontiers, DOI `10.3389/fevo.2026.1922294`; estado `PENDING_CROSSREF`.
- `approved_assets=[]`, `export.render_status=NOT_GENERATED`, `publicacion.status=PENDIENTE_DECISION_GROK`.
- `cola/estado/2026-11-30_rapaces-clima-reino-unido.json` y `cola/entrada/2026-11-30_rapaces-clima-reino-unido.json`: HTTP 404. No hay ruta anidada ni salida en el árbol. `RECEPCION_GROK_NO_CONFIRMADA`; `NOT_DISPATCHABLE`.

### `2026-11-30_liquen-gen-cereales` — 17:00 CDMX

- 8 escenas, 199 palabras, 84 s declarados, 9:16 y voz `es-MX-JorgeNeural` `+7%` / `-2Hz`.
- `narrative_qa` ya persistido: **PASS/93**, siete checks true y flags vacías. El registro declara lectura en frío posterior y separada; existe un commit de QA posterior al commit inicial del borrador. No se repitió el PASS. GitHub no registra el modelo/identidad del redactor, por lo que la separación queda documentada por la pasada posterior y su rol, no por una atribución verificable del autor original.
- Fuente primaria: Du et al., *Nature*, DOI `10.1038/s41586-026-11151-w`. El PDF primario se abrió y se verificó el método en p. 5 / texto de métodos: las coordenadas publicadas son Yangling (34°16′N, 108°04′E), Heyang (35°43′N, 110°02′E), Cangzhou (38°33′N, 116°38′E) y Linfen (36°56′N, 112°34′E). Las cuatro parejas WGS84 del storyboard coinciden con esas coordenadas convertidas a decimales. El artículo también reporta aumentos de 19.4–32.8% en rendimiento por parcela bajo agua limitada (resumen y resultados). DOI visible en el PDF editorial; Crossref y `doi.org` no fueron accesibles, por lo que el estado sigue `PENDING_CROSSREF`.
- `approved_assets=[]`, `export.render_status=NOT_GENERATED`, `publicacion.status=PENDIENTE_DECISION_GROK`.
- `cola/estado/2026-11-30_liquen-gen-cereales.json` y `cola/entrada/2026-11-30_liquen-gen-cereales.json`: HTTP 404. No hay ruta anidada ni salida en el árbol. `RECEPCION_GROK_NO_CONFIRMADA`; `NOT_DISPATCHABLE` hasta ejecutar el validador estructural real y completar Crossref/doi.org.

### Discrepancia de inventario

El radar del 27-nov describe EpTFIIAγ como el único borrador nuevo, pero el árbol de proyectos contiene además el borrador de rapaces para 30-nov 07:00. Se conserva como backlog ya existente, no se incorpora a la shortlist ni se crea un duplicado. Los slots 07:00 y 17:00 del 30-nov están ocupados en feature; no se promueve ninguno a cola. No se modificaron storyboards, `main`, `data/*.json`, estados Grok, cola, salidas, medios ni programación.


---

## Revalidación final — 27-nov-2026

Corte de lectura: feature HEAD 53ad156371717984ad8ed701099dc2bb79a4bfe3; main HEAD 66b2cf076499e24f0b0d6bfa2f8e619df0c158aa. Esta sección prevalece sobre conteos anteriores del mismo informe cuando difieran.

### 1. Inventario completo de proyectos

Se releen los 94 archivos proyectos/*/storyboard.json de feature. Distribución exacta de narrative_qa leída desde cada JSON:

- 23 PASS.
- 28 FAIL.
- 42 sin narrative_qa.
- 1 PENDING, sin score válido.

**PASS — scores exactos**

| Proyecto | JSON |
|---|---:|
| 2026-11-01_red-electrica-pulso-minuto | PASS/89 |
| 2026-11-02_camaron-mantis | PASS/90 — falta narrative_contract; no está preparado |
| 2026-11-04_cielo-azul-atardecer-rojo | PASS/94 |
| 2026-11-05_kids-dia-en-venus | PASS/88 |
| 2026-11-06_inter-arena-cantante | PASS/94 |
| 2026-11-09_dato-robot-ensambla-orbita | PASS/90 — procesamiento preexistente |
| 2026-11-10_comida-aprendizaje-sabor-nutriente | PASS/92 |
| 2026-11-10_dato-adn-sincroniza-flujo | PASS/91 |
| 2026-11-12_dato-pedorreta-chimpances | PASS/91 |
| 2026-11-13_dato-caracol-16-embriones | PASS/91 |
| 2026-11-14_dato-microplasticos-pantanal | PASS/88 |
| 2026-11-15_dato-dia-diapausa-lestes-sponsa | PASS/90 |
| 2026-11-16_dato-polen-desenreda-nanotubos | PASS/91 |
| 2026-11-17_dato-suelo-dos-relojes | PASS/89 |
| 2026-11-18_dato-kuroshio-puente-atmosferico | PASS/90 — DOI pendiente |
| 2026-11-19_dato-dia-luz-dos-manos-oro-poroso | PASS/91 |
| 2026-11-19_dato-estrella-dentro-de-estrella | PASS/90 |
| 2026-11-20_dato-dia-atlantico-humedad-sapropeles | PASS/91 |
| 2026-11-21_fentale-metano-sin-erupcion | PASS/90 |
| 2026-11-22_yubarta-genoma-soplo | PASS/90 |
| 2026-11-27_dato-pav1-bacteriofago | PASS/90 — SFX 8/8 y mapa/dato presentes; DOI `10.3389/fpls.2026.2008228` solo `VERIFICADO_URL` (Crossref pendiente); conflicto 07:00 |
| 2026-11-27_dato-registros-intermareales-1950s | PASS/90 — conflicto de slot |
| 2026-11-30_liquen-gen-cereales | PASS/93 — SFX 8/8, mapa y dato presentes; DOI `10.1038/s41586-026-11151-w` PENDING_CROSSREF; `slot_cesta` ausente |

**FAIL — scores exactos**

| Proyecto | JSON |
|---|---:|
| 2026-10-31_murcielagos-viroma-global | FAIL/72 |
| 2026-10-31_sequias-energia-renovable | FAIL/56 |
| 2026-10-31_smartpe-edicion-plantas | FAIL/80 |
| 2026-11-01_dato-cambio-horario-corazon | FAIL/84 |
| 2026-11-01_llorar-cebolla-quimica | FAIL/79 |
| 2026-11-01_pulpo-tres-corazones | FAIL/72 |
| 2026-11-02_comida-pan-duro | FAIL/84 |
| 2026-11-05_comida-palomitas | FAIL/82 |
| 2026-11-05_inter-arboles-se-comunican | FAIL/78 |
| 2026-11-05_inter-rayo-globular | FAIL/81 |
| 2026-11-06_comida-aguacate-negro | FAIL/79 |
| 2026-11-06_inter-ranas-congeladas | FAIL/83 |
| 2026-11-06_kids-ballena-azul-corazon | FAIL/80 |
| 2026-11-07_comida-hielo-caliente | FAIL/81 |
| 2026-11-07_inter-nubes-pesan | FAIL/78 |
| 2026-11-07_inter-pulpo-suenos | FAIL/72 |
| 2026-11-07_kids-huesos-bebe | FAIL/82 |
| 2026-11-15_dato-quasar-pareja-cosmic-dawn | FAIL/0 |
| 2026-11-18_dato-catorce-campos-hidrotermales | FAIL/68 |
| 2026-11-20_dato-marea-cerebral-en-sueno | FAIL/82 |
| 2026-11-21_homo-erectus-selva-tropical | FAIL/83 |
| 2026-11-21_pulsar-gamma-reticulo | FAIL/83 |
| 2026-11-22_bao-estrella-fusion-andromeda | FAIL/84 |
| 2026-11-22_genes-estatura-etapas | FAIL/72 |
| 2026-11-22_voyager-1-un-dia-luz | FAIL/83 |
| 2026-11-23_supersequias-722-eventos | FAIL/82 |
| 2026-11-23_tropical-biodiversity-turnover | FAIL/82 |
| 2026-11-30_rapaces-clima-reino-unido | FAIL/82 |

**Sin narrative_qa — 42 rutas**

1. 2026-10-24_abejas-bullying
2. 2026-10-24_ideonella-pet
3. 2026-10-24_osedax-comehuesos
4. 2026-10-24_serpientes-que-ruedan
5. 2026-10-25_ave-jurasica-sin-vuelo
6. 2026-10-25_corales-contacto
7. 2026-10-25_reina-olor
8. 2026-10-25_sueno-electricidad-qom
9. 2026-10-26_baffin-bay-ice-shelf
10. 2026-10-26_catrina-posada-monerismo
11. 2026-10-26_hongo-gente-diminuta
12. 2026-10-26_papel-picado-dia-muertos
13. 2026-10-26_papel-picado-dia-muertos_parte2
14. 2026-10-26_pimiento-verde-rojo
15. 2026-10-27_cempasuchil-ciencia
16. 2026-10-27_corneja-decision-rapida
17. 2026-10-27_ddm-parte3-pomuch
18. 2026-10-27_familia-ajolote
19. 2026-10-27_kids-serpiente-voladora
20. 2026-10-27_noct-anfibio-marino
21. 2026-10-28_ddm-parte4-templo-mayor
22. 2026-10-28_familia-voyager-disco-oro
23. 2026-10-28_kids-titanoboa
24. 2026-10-28_monarca-almas
25. 2026-10-28_mosquito-fruitless-audicion
26. 2026-10-28_noct-lince-milanos
27. 2026-10-28_pan-de-muerto-huesos
28. 2026-10-29_juno-choque-proa
29. 2026-10-29_muralismo-cu
30. 2026-10-30_arqueas-origen-eucariotas
31. 2026-10-30_kromdraai-primera-fecha
32. 2026-10-31_pardelas-jetlag-solar
33. 2026-11-03_dato-polvo-africano-microbios
34. 2026-11-03_kids-leche-enchilado
35. 2026-11-xx_kids-flamencos-rosas_RESPALDO
36. demo-001
37. guiones_lote_01
38. lote01-01-el-nino
39. lote01-02-petroleo
40. lote01-03-balon-curva
41. lote01-04-tardigrado
42. lote01-05-chicxulub

El único PENDING es 2026-11-04_dato-polvo-atrapa-oro. De los 42 sin QA, 39 también carecen de narrative_contract; tres sí tienen contrato, pero no revisión. Camarón mantis conserva PASS/90 sin narrative_contract, por lo que tampoco está preparado. El directorio _RESPALDO de flamencos conserva un project_id sin el sufijo de respaldo: se trata como respaldo, no como proyecto editorial adicional.

Cuatro storyboards antiguos tienen project_id sin el prefijo de fecha de su carpeta: cempasuchil-ciencia, familia-ajolote, kids-serpiente-voladora y noct-anfibio-marino. Sus fechas objetivo/slots no están completos; no se infieren desde el nombre de carpeta. El resto de los artefactos legacy también requiere cautela: la fecha del directorio no sustituye fecha_objetivo ni slot_local.

### 2. Proyectos del 27-nov y entradas de cola

| Rama/ruta | Creación Git | Fecha objetivo / slot | Estado |
|---|---|---|---|
| feature: proyectos/2026-11-27_dato-pav1-bacteriofago/storyboard.json | 2026-11-27 10:15:34Z (04:15:34 CDMX) | 27-nov, 07:00; slot_cesta ausente | PASS/90; no promovido |
| feature: proyectos/2026-11-27_dato-registros-intermareales-1950s/storyboard.json | 2026-11-26 22:11:55Z (16:11:55 CDMX) | 27-nov, 23:30; slot_cesta ausente | PASS/90; no promovido |
| main: proyectos/2026-11-27_bacterias-vuelta-oxigeno/storyboard.json | 2026-11-27 16:37:55Z (10:37:55 CDMX) | programacion indica 17:00; storyboard sin fecha_objetivo, slot_local ni slot_cesta | Sin narrative_contract ni narrative_qa |
| main: cola/entrada/2026-11-27_bacterias-vuelta-oxigeno/storyboard.json | 2026-11-27 16:38:02Z | carpeta anidada | Contenido literal PLACEHOLDER; no es JSON válido |

**Feature, cola/entrada:** cero JSON planos y cero entradas anidadas del 27-nov. Solo permanece el paquete histórico anidado del robot orbital. **Main, cola/entrada:** cero JSON planos y una carpeta anidada del 27-nov, pero su storyboard es PLACEHOLDER. No hay paquete válido del día en cola.

PAV1 tiene 8 escenas, 187 palabras, 78 s de escenas + cortinilla de 6 s = 84 s, título de 5 palabras, voz definida, mapa y capa de dato/gráfico, source_ids válidos, prompt_base consistente, seis campos narrativos por escena, SFX y ambiente presentes en 8/8, approved_assets=[] y export.render_status=NOT_GENERATED. No contiene rutas de assets. Bloqueos: el DOI correcto es `10.3389/fpls.2026.2008228` (`VERIFICADO_URL`); la página oficial de Frontiers lo identifica como artículo publicado el 26-11-2026, pero no hay resolución Crossref/doi.org ni ejecución `--check-doi`; falta `slot_cesta`. La anotación previa de SFX vacío y el DOI `10.1126/science.abc…` eran incorrectos. El slot 07:00 ya está ocupado en main por microondas.

Intermareal tiene 8 escenas, 174 palabras, 78 + 6 = 84 s, título de 5 palabras, voz definida, mapa y capa de dato, SFX y ambiente presentes, source_ids válidos, prompt_base consistente, seis campos narrativos por escena, DOI con verificación Crossref/resolvedor registrada, approved_assets=[] y export.render_status=NOT_GENERATED; no contiene rutas de assets. Falta slot_cesta. Su slot 23:30 colisiona con el paquete de Stubbs, que ya tiene evidencia de render y QA audiovisual. No se promueve.

El proyecto de main “bacterias-vuelta-oxigeno” tiene 7 escenas, 84 palabras, 74 s de escenas + 6 s de cortinilla = 80 s frente a 82 declarados, y título de 9 palabras. No declara fecha_objetivo, slot_local, slot_cesta, narrative_contract, narrative_qa, approved_assets ni export.render_status. Introduce asset_filename y export.filename; los archivos referenciados no están en el árbol. La programación marca 17:00, private, programado_sin_montar, sin video_id y publish_at 2026-11-27T23:00:00Z. La carpeta de cola anidada es solo placeholder y NOT_DISPATCHABLE.

**Main registra cinco paquetes para el 27-nov; solo tres ocupan ventanas vigentes.**

| Slot CDMX | Paquete/evidencia | ID/privacidad/estado |
|---|---|---|
| 07:00 | Rehecho microondas, plan semanal | YouTube nd0rs6iVy8E; private; publishAt 13:00Z; QA audiovisual 77 s; MP4 referido fuera del árbol |
| 10:00 | Rehecho miel (fuera de ventana autorizada) |
| 15:00 | Rehecho ola azul (fuera de ventana autorizada) |
| 17:00 | Bacterias vuelta al oxígeno | Sin video_id; private; programado_sin_montar; no hay medios |
| 23:30 | Animal Stubbs | Sin video_id ni publishAt; metadata y logs de render, QA audiovisual ES 86.13 s / EN 84.97 s; MP4 referido fuera del árbol |

Las tres ventanas vigentes de main para el 27-nov —07:00, 17:00 y 23:30— ya están ocupadas por registros preexistentes (microondas, bacterias y Stubbs, respectivamente); PAV1 colisiona con 07:00 e Intermareal con 23:30. Los reworks de 10:00 y 15:00 son registros heredados fuera de ventanas activas y no cuentan como capacidad autorizada. No hay ventana activa libre. Los IDs originales de miel y ola azul (`jpDyCX6zSgQ`, `4xylLT3vSIU`) siguen descritos como intactos junto con los nuevos IDs (`p06UCGu0-Og`, `HKpani8TTeY`): riesgo de duplicado; no se borró/canceló nada ni se verificó Studio. Se marca MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO para microondas, miel, ola azul, bacterias y Stubbs: los paths referidos no están en el árbol GitHub. No se afirma que existan fuera de él.

### 3. Procesador, dispatch y handoffs

La revisión cruzada detecta una diferencia importante entre ramas:

- Feature, scripts/procesar_cola.py (blob 64c1f94…): usa fecha_actual_cdmx(), extrae la fecha del path y filtra candidatos por fecha_archivo == --fecha. La selección por defecto se limita al día CDMX. Un --fecha histórico explícito todavía puede solicitar una fecha anterior; no hay selección histórica automática.
- Main, scripts/procesar_cola.py (blob fd567091…): versión legacy con datetime.date.today() y selección ent[0] sin filtro por fecha. Con la cola histórica actual puede tomar el primer storyboard antiguo. Esta versión no debe ejecutarse para producción. El cambio seguro está en el PR #3, que sigue abierto y no integrado.
- docs/FLUJO_EXTERNO.md en feature describe el comportamiento nuevo y coincide con el script de feature.
- capcot-grok-dispatch.yml existe en feature, no en main. Su trigger y selector solo aceptan JSON planos en cola/entrada/*.json; workflow_dispatch busca con profundidad máxima 1. No encuentra cola/entrada/<project_id>/storyboard.json. El procesador admite rutas anidadas, pero el dispatcher no: contrato de rutas inconsistente.
- El registro editorial de feature recorre recursivamente proyectos, cola, cola/bloqueados, salidas y handoffs/grok_inbox. No se ejecutó porque no hay runtime local.
- trabajador-cola.yml es una copia de staging, no está instalado en los workflows activos de main. scripts/trabajador_cola.py es un worker de Issues, no el procesador de paquetes CAPCOT. Su log histórico “sin trabajo en cola” no demuestra que cola/entrada esté vacía.

En feature se verificó 404 para cola/estado de los dos proyectos del 27-nov, los dos del 30-nov, los dos casos del 18-nov, los doce IDs del lote 5–7 nov y el robot orbital. Para los 19 IDs consultados se registra exactamente: RECEPCION_GROK_NO_CONFIRMADA. No se crea ni modifica ningún estado.

Markers actuales de main en handoffs/grok_inbox:
- Robot orbital: status pending, branch main, package_path anidado; no confirma recepción.
- Serie cuántica evolución: pending, Issue #1066, brief en guiones/serie_cuantica_evolucion.
- Serie Thomas Harris: pending, Issue #1065, brief en guiones/serie_thomas_harris.

handoffs/grok_done solo contiene .gitkeep. No hay archivos cola/estado. La presencia de markers no acredita lectura por Grok. La presencia de GROK_WEBHOOK_URL y GROK_WEBHOOK_TOKEN no pudo verificarse con los permisos disponibles; no se leyeron valores. No hubo ejecución de capcot-grok-dispatch en los últimos 100 runs consultados.

### 4. Lote obligatorio 5–7 nov

Se releyeron los doce storyboards y el horario semanal. project_id, fecha_objetivo/fecha, slot_local/hora y slot_cesta/cesta coinciden exactamente en los doce. Los scores/statuses conservados son:

- PASS/88: 2026-11-05_kids-dia-en-venus.
- PASS/94: 2026-11-06_inter-arena-cantante.
- FAIL/82: 2026-11-05_comida-palomitas.
- FAIL/78: 2026-11-05_inter-arboles-se-comunican.
- FAIL/81: 2026-11-05_inter-rayo-globular.
- FAIL/79: 2026-11-06_comida-aguacate-negro.
- FAIL/83: 2026-11-06_inter-ranas-congeladas.
- FAIL/80: 2026-11-06_kids-ballena-azul-corazon.
- FAIL/81: 2026-11-07_comida-hielo-caliente.
- FAIL/78: 2026-11-07_inter-nubes-pesan.
- FAIL/72: 2026-11-07_inter-pulpo-suenos.
- FAIL/82: 2026-11-07_kids-huesos-bebe.

No se repitió lectura narrativa porque los JSON conservan los QA previos y no se identificó cambio de narración en esos doce archivos. Estructura revalidada estáticamente:

- 85 escenas en total; todas las cápsulas tienen 7–9 escenas.
- 170–221 palabras por narración.
- 78 s de escenas + 6 s de cortinilla = 84 s.
- Títulos dentro del máximo de seis palabras; voz, source_ids y prompt_base presentes.
- 11/12 tienen mapa y capa de dato/gráfico. El storyboard canónico de redes micorrícicas es el único sin ambas capas.
- Faltan los seis campos dramáticos obligatorios en las 85 escenas: 510 ausencias.
- 75 escenas tienen SFX vacío sin silencio explícito; ambiente sí está presente.
- Los doce tienen approved_assets=[], export.render_status=NOT_GENERATED y no incluyen rutas de assets.

El canónico 2026-11-05_inter-arboles-se-comunican sigue correspondiendo a redes micorrícicas comunes y Karst et al. 2023. No se marca desajuste temático. La variante de respiración nocturna permanece como artefacto separado en bloqueados. Los dos PASS narrativos no pasan estructura; ninguno de los doce se promueve. Todos tienen RECEPCION_GROK_NO_CONFIRMADA.

### 5. Producción preexistente y YouTube

No existe archivo central historial_youtube en el árbol. Se inspeccionaron 51 programacion.json de main. Quince IDs antiguos siguen descritos como programados aunque su publishAt ya pasó; se registra riesgo de duplicado/estado obsoleto, sin borrar ni cancelar:

| YouTube ID | Slot local registrado | Fecha programada |
|---|---:|---|
| 45WOvkNQTHo | 13:30 | 16-nov |
| KnP1j4y72ug | 13:30 | 17-nov |
| -fDL2pBjH30 | 13:30 | 18-nov |
| vj5RZDt-dfc | 13:30 | 19-nov |
| WTlFSZV9HYg | 13:30 | 20-nov |
| K4qNkx2f4RI | 13:30 | 21-nov |
| aTau_z2yWq8 | 19:00 | 15-nov |
| XL0f90ZtwpY | 19:00 | 16-nov |
| 25mWYJVOPLk | 19:00 | 17-nov |
| NKDhKlY1rVI | 19:00 | 18-nov |
| zyTl_cVGN6E | 19:00 | 19-nov |
| ZG4iQgmWrLI | 19:00 | 21-nov |
| O9QlSaft5DY | 13:30 | 15-nov |
| WcTviUWqbes | 07:00 | 12-nov |
| maLtsoQpxwI | 19:00 | 11-nov |

Seis IDs aparecen además en registros de salidas como publicados: EX0W3q-yKRw, WcTviUWqbes, es6hWxPdt2A, dz2C-Y8klXA, maLtsoQpxwI y cci90_HP6R4. WcTviUWqbes y maLtsoQpxwI siguen simultáneamente en registros de cola como programados y en salidas como publicados; discrepancia de estado y riesgo de duplicado.

**Robot orbital — discrepancia entre copias:**

- El storyboard de proyectos en feature y main comparte el mismo blob, 9 escenas, 210 palabras, target 88 s, cortinilla 6 s y narrative_qa PASS/90. Aun así contiene asset_filename, por lo que no cumple contrato de preproducción.
- La copia de cola/entrada en main tiene otro blob y otra narración: 9 escenas, 187 palabras, cortinilla 13 s, export.filename y media real. Conserva PASS/90 copiado, pero ese QA narrativo no corresponde a la narración alterada y no se revalida como PASS válido.
- El QA audiovisual de esa copia registra 21/21 checks y 87.57 s. Es QA audiovisual, no narrativa. La duración medida cae dentro de 75–90, pero el storyboard de cola declara 82 s de escenas + 13 s de cortinilla = 95 s; discrepancia con la duración medida y con el contrato de cortinilla de 6 s.
- La copia de cola incluye capsula.mp4, nueve frames, subtítulos y archivos de apoyo dentro de GitHub. No se marca MEDIOS_NO_VERIFICADOS para ese paquete.
- programacion.json conserva ZG4iQgmWrLI, publish_at 2026-11-22T01:00:00Z (21-nov 19:00 CDMX), private→public programado. El marker de handoff, en cambio, identifica el paquete como 9-nov 23:30. El mismo project_id tiene discrepancia de fecha/slot entre marker, proyecto y programación.
- No existe salidas/<project_id>/ para el robot; el paquete audiovisual está anidado en cola/entrada. Se clasifica PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR. No se modifica ni redispatcha.

### 6. Datos, plantillas, Actions y PRs

**Datos y estilos**

| Fuente | Feature | Main |
|---|---|---|
| temas_del_dia.json | última fecha 28-oct | 28-oct |
| rotacion.json | 31-oct | 21-nov |
| estilos_usados.json | 28-oct | 11-nov |
| horarios.json | 09-nov | 23-nov |
| publicaciones.json | 01-nov | 24-nov |
| cola.json | 31-oct | revisar: no es inventario exhaustivo |

Main usa además plan_semana para microondas, data/rehechos_2026-11-22.json para miel y ola azul, programacion.json para bacterias y metadata/logs para Stubbs. No se alteró ningún data/*.json. La rotación de estilos no puede certificarse con data/estilos_usados por su antigüedad; se contrasta con los style_id presentes en proyectos.

**Plantillas**

- templates/storyboard_vertical.template.json es la plantilla alineada al contrato actual.
- templates/storyboard.template.json conserva asset_filename, asset_type, rutas de audio y export.filename; es una plantilla legacy incompatible con preproducción.
- templates/grok_status.template.json existe y coincide con el contrato: solo Grok escribe cola/estado.

**Actions**

- Kuroshio run #23 (`46073709847`, job `140756420589`) y revalidación posterior run #24 (`46076761978`, job `140766191962`): #24 concluyó SUCCESS el `2026-11-27T22:27:35Z`, commit `53ad156371717984ad8ed701099dc2bb79a4bfe3`; comando exacto `python scripts/validar_storyboard.py proyectos/2026-11-18_dato-kuroshio-puente-atmosferico/storyboard.json`; salida literal `OK` y `Expediente textual íntegro; medios no generados; publicación no autorizada.` No se usó `--check-doi`; el DOI sigue `RESOLVEDOR_CROSSREF_NO_CONFIRMADO`. Los blobs storyboard/validador/workflow coinciden con HEAD. `ESTADO_EJECUCION.md` actualizado y releído con run #24.
- Semgrep run 46061613357, main commit 194257: FAILURE; 37 findings, 37 blocking, 1283 targets escaneados, 37 archivos grandes omitidos. Error literal: “Process completed with exit code 1.”
- CodeQL run 460747 en PR #3: SUCCESS.
- Worker run 460096: log “[trabajador] sin trabajo en cola.” No acredita cola CAPCOT vacía; el workflow es staging y el script relacionado procesa Issues.
- No se encontró ejecución de capcot-grok-dispatch en los últimos 100 runs.

**Pull requests abiertos; ninguno se integró**

- #3: OPEN/DRAFT, base `main`, head `feature/capcot-video-discovery-continuity` (`2f49e05c5817d8846a043d8205b51f580a6ebb5f`), mergeable=false; 724 archivos, 1547 commits, 91,535 adiciones y 1,735 eliminaciones.
- #14: OPEN hacia main; añade asset_filename a ocho escenas y conserva narrative_qa histórico FAIL/82; no ejecuta --check-doi. Incompatible con preproducción.
- #15: OPEN hacia feature; modifica validador y pruebas de coordenadas; no integrado.
- #13: OPEN, documentación de auditoría; no sustituye lectura narrativa.
- #4: OPEN, documentación/paquete del robot; no se integra.
- #6: OPEN, supervisor/workflow; no se integra.
- #7–#9: actualizaciones de dependencias; no cambian QA narrativo ni se integran.

No se identificó cambio oficial nuevo de APIs que justificara revisión adicional.

### 7. Resultado y límites

- No hubo runtime local. Revisión estática de todos los JSON indicados, scripts, workflows, plantillas, datos, briefs, handoffs y registros; contraste con ejecuciones CI existentes.
- No se ejecutó procesador, validador local, workflow, dispatch ni envío externo.
- No se promovió ni redispatchó ningún proyecto.
- No se modificaron storyboards, cola/entrada, cola/estado, cola/bloqueados, data/*.json, workflows, secretos, permisos, PRs ni main.
- Cambios de este corte: actualización documental de `CONTROL_COLA.md` y `ESTADO_EJECUCION.md` de Kuroshio con el run CI #24 y corrección de discrepancias del inventario. No se modificaron storyboards, `data/*.json`, cola, estados Grok, workflows, secretos, permisos, PRs ni `main`.
- No se generaron cápsulas, frames, imágenes, voz, audio, video, renders ni publicaciones; no se consumieron créditos.




## Revalidación del 27-nov-2026 — 16:35 CDMX

### Estado actual de proyectos y QA

- HEAD auditado antes de estas dos actualizaciones documentales: `2f49e05c5817d8846a043d8205b51f580a6ebb5f`. Se contaron 94 `proyectos/*/storyboard.json`: 23 PASS, 28 FAIL, 42 sin `narrative_qa` y 1 PENDING. Los scores/statuses de la tabla de inventario se cotejaron con los JSON vigentes.
- Los dos borradores de feature para el 27-nov siguen con QA independiente PASS/90 y no se repitió la lectura narrativa: PAV1 (creado 27-nov 10:15:34Z; QA actualizado por commit `653a7ad38bb136229414bcd180aa9971d5d5f38e`) e Intermareal (creado 26-nov 22:11:55Z; QA PASS registrado en commit `4ba5b682c9f4b294bd183018f71151d062f0ba3f`; las modificaciones posteriores fueron limpieza de notas, no narración). Ambos tienen `slot_cesta` ausente.
- PAV1: 8 escenas, 187 palabras, 78+6=84 s; 8/8 SFX y ambientes presentes; mapa y dato/gráfico presentes; seis campos dramáticos en todas las escenas; source_ids válidos; prompt_base exacto; `approved_assets=[]`, `render_status=NOT_GENERATED`, sin rutas de assets. Fuente primaria Sabri et al., Frontiers in Plant Science, publicada 26-nov-2026, DOI `10.3389/fpls.2026.2008228`, estado JSON `VERIFICADO_URL`; no se ejecutó Crossref/doi.org ni `--check-doi`. Enlace editorial: https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2026.2008228/full. Conflicto de slot con microondas en main a las 07:00. No promover.
- Intermareal: 8 escenas, 174 palabras, 78+6=84 s; 8/8 SFX y ambientes; mapa y capa de dato; seis campos dramáticos; source_ids válidos; prompt_base exacto; `approved_assets=[]`, `render_status=NOT_GENERATED`, sin rutas. Fuente primaria Sinde-Mano et al. publicada 26-nov-2026, DOI `10.1038/s41597-026-08947-w` (`VERIFICADO_CROSSREF`); los tres datasets GBIF también conservan estado de resolvedor. Colisión de 23:30 con el proyecto Stubbs ya renderizado/QA en main. No promover.
- Main contiene además `2026-11-27_bacterias-vuelta-oxigeno`: 7 escenas, 84 palabras, 74 s + cortinilla 6 = 80 s frente a 82 declarados, título de 9 palabras, sin `narrative_contract` ni `narrative_qa`, siete `asset_filename` y `export.filename`; `programacion.json` lo deja private/programado_sin_montar a las 17:00, sin video_id. Su copia anidada en `cola/entrada/<id>/storyboard.json` es el literal `PLACEHOLDER`, no JSON válido y NOT_DISPATCHABLE.
- El JSON actual de Rapaces es `FAIL/82`, con `giro_cientifico_explicado=false` y `critical_flags=[GIRO_CIENTIFICO_NOMBRADO_PERO_NO_EXPLICADO]`. Las referencias iniciales a FAIL/0 eran el estado fail-closed anterior y quedaron supersedidas por el QA independiente registrado el 27-nov; el score actual del archivo es 82.
- Liquen (30-nov) conserva PASS/93. Relectura estructural de metadatos: 8 escenas, 200 palabras, 78+6=84 s; seis campos dramáticos presentes; SFX y ambientes 8/8; mapa en escenas 2 y 5; capa de dato en escena 6; `approved_assets=[]`, `render_status=NOT_GENERATED`, sin rutas. El único bloqueo DOI es `10.1038/s41586-026-11151-w` (`VERIFICADO_URL; DOI PENDING_CROSSREF`); `slot_cesta` falta. Las notas previas que afirmaban SFX vacíos y ausencia de mapa/dato eran incorrectas.
- El caso 2026-11-18_dato-catorce-campos-hidrotermales conserva FAIL/68 y estado documental `BORRADOR_EN_PROYECTOS_NO_APTO_PARA_PROMOCION`. Los ocho `ESTADO_EJECUCION.md` existentes en proyectos fueron revisados; no se encontró otro estado `PREPARADO` contradictorio que requiriera corrección.

### Ventanas y reconciliación de main

- El Plan Maestro vigente (revisión 27-nov) y `main:data/horarios.json` (actualizado 23-nov) definen solo tres ventanas autorizadas: 06:30–07:30, 16:30–18:00 y el slot fijo 23:30. 13:00–14:30 es experimental; 19:00–21:00 está retirado. La antigua cuenta de cinco slots es obsoleta.
- Main tiene cinco registros del 27-nov, pero solo tres caen en ventanas autorizadas: 07:00 microondas (`nd0rs6iVy8E`, private, `publishAt=13:00Z`, QA audiovisual 77 s); 17:00 bacterias (sin video_id, private/programado_sin_montar); 23:30 Stubbs (sin video_id ni publishAt, pero metadata + render.log + QA audiovisual 86.13 s ES / 84.97 s EN). Los registros de miel 10:00 y ola azul 15:00 están fuera de ventanas autorizadas; no cuentan como capacidad productiva vigente.
- Los reworks de miel y ola azul conservan IDs originales `jpDyCX6zSgQ` y `4xylLT3vSIU`, mientras sus nuevas copias tienen `p06UCGu0-Og` y `HKpani8TTeY`. Se marca riesgo de duplicado; los registros dicen que los originales siguen intactos. No se borró, canceló ni cambió privacidad; no se verificó YouTube Studio.
- Las tres ventanas activas están ocupadas: PAV1 colisiona con microondas a las 07:00; 17:00 está ocupado por bacterias; Intermareal colisiona con Stubbs a las 23:30. No hay ventana activa libre. Los paths MP4 referidos por microondas, miel, ola azul, bacterias y Stubbs no aparecen en el árbol GitHub: `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`.
- `main:data/publicaciones.json` tiene 62 registros y no contiene entradas del 27-nov; el último campo fecha llega a 24-nov. Feature conserva 22 registros hasta 31-oct (publishAt hasta 1-nov). No se usó el ledger como inventario exhaustivo.

### Cola, estados, selector y Actions

- Feature: cero entradas de 27-nov en `cola/entrada/*.json` y cero anidadas del día; permanece el paquete histórico anidado del robot orbital 9-nov. Main: una carpeta anidada del 27-nov, pero su archivo es `PLACEHOLDER`. Ninguno de esos paquetes es dispatchable.
- El dispatcher de feature selecciona exclusivamente `cola/entrada/*.json`; para `workflow_dispatch` usa `find -maxdepth 1` y para push filtra `^cola/entrada/[^/]+\.json$`. No alcanza `cola/entrada/<id>/storyboard.json`. El procesador de feature filtra por fecha CDMX por defecto, aunque un `--fecha` explícito permite solicitar históricos; el procesador legacy de main usa `datetime.date.today()` solo para el registro y selecciona `ent[0]` sin filtro por fecha.
- Los 18 estados consultados (dos proyectos actuales, main bacteria, Stubbs, Kuroshio, catorce y los doce IDs del lote 5–7 nov) devolvieron 404. Resultado exacto: `RECEPCION_GROK_NO_CONFIRMADA`. El único marker en `handoffs/grok_inbox/` es el del robot 9-nov con `status=pending`; solo prueba marker, no lectura/recepción de Grok.
- En los últimos 100 Actions de feature no hay ejecuciones recientes del dispatcher; las 45 ejecuciones encontradas corresponden al 1-nov. La más reciente, run `41306776689`, falló en “Verificar configuración del receptor”; error literal: `Falta configurar GROK_WEBHOOK_URL.`. El chequeo posterior de `GROK_WEBHOOK_TOKEN` no llegó a ejecutarse; los logs muestran ambas variables de entorno vacías, pero no se exponen valores. El workflow actual de feature trata el webhook como opcional y no tiene ejecuciones recientes.
- Kuroshio run #24 quedó registrado en `ESTADO_EJECUCION.md` y releído desde GitHub. Run `46076761978`, commit `53ad156371717984ad8ed701099dc2bb79a4bfe3`, comando sin `--check-doi`, resultado `OK`; los blobs del storyboard, validador y workflow coinciden con HEAD. DOI permanece pendiente.

### Pull requests abiertos

- #3 OPEN/DRAFT: base main, head feature, SHA `2f49e05c5817d8846a043d8205b51f580a6ebb5f`, 724 archivos, 1547 commits, 91,535 adiciones, 1,735 eliminaciones, mergeable=false; incluye cambios extensos de cola, datos, proyectos, procesador, registro y dispatcher. No integrar.
- #14 OPEN hacia main: añade `asset_filename` a ocho escenas de Quasar y conserva FAIL/82; incompatible con preproducción.
- #15 OPEN hacia feature: cambia validador/pruebas de tipos de coordenadas; no integrado.
- #13 OPEN hacia main: informe documental; no sustituye QA narrativo.
- #4 OPEN hacia feature: ubicación de frames ASTRA; #6 OPEN hacia feature: supervisor; #7–#9 OPEN hacia main: dependencias de workflows. Ninguno se integró.

### Límites y resultado

- No hubo runtime local; se hizo revisión estática y contraste con GitHub Actions. No se ejecutó validador local ni `--check-doi` para PAV1/Intermareal/Liquen.
- No se modificaron storyboards, claims, `data/*.json`, cola/entrada, cola/estado, cola/bloqueados, workflows, secretos, permisos, PRs ni `main`. Solo se actualizaron este control y el expediente documental de Kuroshio.
- No se promovieron paquetes, no se disparó dispatch, no se enviaron payloads, no se generaron medios ni se consumieron créditos. No se encontró cambio oficial de API que justificara revisión adicional.


## Revalidación 27-nov-2026 — 17:57 CDMX

### Ramas, PR y CI

- La rama de trabajo sigue siendo **feature/capcot-video-discovery-continuity**. Antes de este corte, HEAD era **22dbaea61d3bb870dbd5a3ff93a8ea67ccdb5499**; ese commit modificó únicamente este control (58 altas, 13 bajas), no storyboards. Este run actualizó el radar en **23ab8d705efd98b59546cef2648ae1c6d5a93e9f** y corrigió su título/cifras en **b14af7946b5bfda4da8e10a8400d862e110013e2**.
- **main** permanece solo lectura. Su HEAD **6a96b3eb18b0bf3369e454269649663295685207** cambió únicamente **data/endscreens_rotacion.json**, por el commit “pantallas 2026-11-27_17 pendiente_studio”; no se tocó ese archivo.
- La última CI de feature consultada (**46078959750**) terminó SUCCESS en SHA **1003644ee**, anterior al HEAD documental 22dbaea y a los dos commits de radar. Su comando no incluye **--check-doi**; no acredita DOI.
- Semgrep **46080610450** terminó FAILURE en main, SHA **6a96b3eb**, con **37 hallazgos bloqueantes** y SARIF no publicado por fallo. CodeQL **46080611866** terminó SUCCESS sobre el mismo SHA. La falla Semgrep es de main; no se atribuye a PR #15.
- PR #3 continúa abierto y mergeable_state=dirty (724 archivos; no integrar). PR #13, #14 y #15 continúan abiertos; no se fusionó ni cerró ninguno.
- Issue #16 sigue abierto, sin comentarios nuevos: lote Imaginantes de 17 MP4, 10 resubidas TikTok y Pancho EN con chat Grok bloqueado. No se enviaron mensajes ni se hicieron resubidas.

### Reconciliación de fechas, slots y producción previa

- **27-nov, 07:00 — Microondas en main:** plan_semana.json conserva videoId=nd0rs6iVy8E, publishAt=2026-11-27T13:00:00Z y QA audiovisual de 77 s. El MP4 referenciado vive bajo /workspace, fuera del árbol Git. Resultado: **PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR** + **MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO**.
- **27-nov, 17:00 — Bacterias en main:** programacion.json conserva publish_at=2026-11-27T23:00:00Z, privacidad private y estado programado_sin_montar, sin video_id. El storyboard de proyecto contiene siete escenas, asset_filename y export.filename; las duraciones de escena suman 74 s y la cortinilla 6 s (80 s frente a target_duration_seconds=82). La carpeta anidada de cola/entrada contiene un storyboard.json literal PLACEHOLDER, no una copia JSON válida; no existe MP4 verificable en el árbol. Resultado: **PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR**, **MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO**, **NOT_DISPATCHABLE** y **RECEPCION_GROK_NO_CONFIRMADA** (estado 404). No se corrigió ni canceló la programación de main.
- **27-nov, 23:30 — Stubbs en main:** existe render previo con duración registrada de 86,13 s; el medio referenciado no está en el árbol. Resultado: **PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR** + **MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO**.
- **28-nov, 17:00 — Mareo en main:** plan_semana.json conserva videoId=fcSNbU809ao, publishAt=2026-11-28T23:00:00Z y QA audiovisual de 79,8 s. El MP4 referenciado está fuera del árbol. No cancelar ni redispatchar. El slot fijo **28-nov, 23:30** permanece libre en los registros consultados.
- **Proyectos en feature:** PAV1 (27-nov 07:00) mantiene PASS/90, 8 escenas y 187 palabras; conflicto con Microondas en main. Intermareal (27-nov 23:30) mantiene PASS/90, 8 escenas y 173 palabras; conflicto con Stubbs en main. Liquen (30-nov 17:00) mantiene PASS/93, 8 escenas y 199 palabras, pero DOI PENDING_CROSSREF y slot_cesta ausente. Rapaces (30-nov 07:00) mantiene FAIL/82, 8 escenas y 182 palabras, flag GIRO_CIENTIFICO_NOMBRADO_PERO_NO_EXPLICADO, DOI PENDING_CROSSREF y slot_cesta ausente.
- Se consultó cola/estado/<project_id>.json para PAV1, Intermareal, Liquen, Rapaces y Bacterias; los cinco devolvieron 404. Registrar en todos: **RECEPCION_GROK_NO_CONFIRMADA**.
- El workflow escucha cola/entrada/*.json y su selector usa find -maxdepth 1; las carpetas anidadas no son dispatchables. Feature no tiene entradas planas nuevas; la entrada de Bacterias en main también es anidada. No se creó cola ni se promovió ningún storyboard.
- data/rotacion.json de main llega hasta 21-nov y data/estilos_usados.json hasta 09-nov; no acreditan rotación actual para el 27–30. Se contrastaron los proyectos y la parrilla real; no se modificó ningún data/*.json.
- No existe archivo independiente historial_youtube en el árbol consultado. Las fuentes disponibles para historial/programación son data/publicaciones.json (62 registros) y docs/briefs/produccion_2026-11-23_28/plan_semana.json.
- Los 12 IDs del lote 5–7 nov permanecen en el resultado ya registrado: 2 PASS y 10 FAIL. El commit previo de feature modificó solo este control, no sus storyboards; no se repitió PASS ni se generó nueva QA. No hubo promoción.
- Los cuatro proyectos de feature consultados no contienen ESTADO_EJECUCION.md; no había un estado PREPARADO que corregir.

### Radar y cierre

- El radar recibió tres candidatos nuevos y el corte de Google Trends en docs/briefs/2026-11-27_RADAR_CAPCOT.md. Crossref REST y doi.org devolvieron Internal Error () para los tres DOI; el slot 28-nov 23:30 queda libre, sin selección ni storyboard.
- No se generaron medios, frames, imágenes, voz, audio, video, renders ni placeholders. No se disparó el workflow Grok, no se enviaron payloads, no se publicó ni programó, no se modificó main, data/*.json, secretos o permisos.


## Revalidación de inventario y compuertas — 27 nov 2026, corte 19:56 CDMX

### Estado remoto y rutas

- HEAD de `feature/capcot-video-discovery-continuity`: `d9071f894a992e061bc183d56b01363f1cbde286`. HEAD de `main`: `6a96b3eb18b0bf3369e454269649663295685207`.
- En feature siguen cuatro proyectos con solo `storyboard.json`; no existe `ESTADO_EJECUCION.md` en esas carpetas. QA sin cambios: PAV1 PASS/90, Intermareal PASS/90, Liquen PASS/93, Rapaces FAIL/82. No se repitió PASS porque las narraciones no cambiaron.
- Los seis estados consultados (PAV1, Intermareal, Liquen, Rapaces, Stubbs y Bacterias) devolvieron 404. Clasificación literal: `RECEPCION_GROK_NO_CONFIRMADA`. No se crearon ni editaron estados.
- Feature `cola/entrada`: 2 elementos, ninguno es JSON plano en la raíz; los proyectos actuales no están en cola. `cola/bloqueados`: 47 elementos; `salidas`: 59; sin coincidencias para los cuatro IDs actuales. La carpeta `cola/estado` no existe en esta rama.
- El workflow escucha `cola/entrada/*.json` y selecciona archivos con profundidad máxima 1. Por evidencia de ruta, los cuatro proyectos siguen `NOT_DISPATCHABLE`; no se disparó workflow ni se envió payload.
- `GROK_WEBHOOK_URL` y `GROK_WEBHOOK_TOKEN` son los nombres referenciados por el workflow. El último error histórico registrado señala ausente `GROK_WEBHOOK_URL`; presencia actual del URL y del token no se puede confirmar sin ejecución. No se consultaron valores.

### Conflictos y procesamiento preexistente en main

- **PAV1 — 27 nov 07:00:** conflicto de slot con Microondas, que figura en `plan_semana.json` con `videoId=nd0rs6iVy8E` y `publishAt=2026-11-27T13:00:00Z`. `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`; el medio referenciado no está en el árbol: `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`.
- **Intermareal — 27 nov 23:30:** conflicto con Stubbs en main. `metadata.json` y `render.log` registran render de 86.13 s; el MP4 referenciado está fuera del árbol. `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`, `CONFLICTO_DE_SLOT_ENTRE_RAMAS`, `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`.
- **Bacterias — 27 nov 17:00:** main conserva `programado_sin_montar` y una copia anidada placeholder; no es entrada plana despachable. Se mantiene `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`; medios referenciados no verificados en el árbol.
- **Mareo — 28 nov 17:00:** `plan_semana.json` contiene `videoId=fcSNbU809ao` y `publishAt`; slot ocupado, no redispatchar.
- **28 nov 23:30:** libre en main y feature, pero sin candidato con DOI/Crossref resuelto. Estado editorial: `PENDING_CROSSREF`; no se creó storyboard.
- **Liquen — 30 nov 17:00:** PASS/93 y estructura previamente validada, pero DOI/Crossref pendiente; no promover.
- **Rapaces — 30 nov 07:00:** FAIL/82 y DOI/Crossref pendiente; no promover.

### Inventario, Actions y rotación

- No apareció ningún JSON plano nuevo ni ejecución del dispatcher. La última Action de main es `Callback - aviso de delegaciones` (run 46095573475, success), no un dispatch. Los tres checks dinámicos recientes de PR #3 concluyeron success; PR #3 sigue draft/open y no mergeable. PR #13, #14 y #15 siguen abiertos. En main, Semgrep sigue failure (run 46080610450); Gitleaks y CodeQL success.
- `data/publicaciones.json` conserva 62 registros y no hay archivo separado `historial_youtube` en el inventario leído. `data/rotacion.json` y `data/estilos_usados.json` siguen atrasados respecto del backlog; no se modificaron y no se certifica rotación con ellos.
- El corte anterior de los 12 IDs del 5–7 nov permanece en 2 PASS / 10 FAIL; no se reescribieron narraciones ni se repitió QA válido.
- No se modificó `data/*.json`, main, secretos, estados Grok, colas, salidas ni medios. No se creó ni promovió storyboard.


## Reconciliación posterior — 27 nov 2026, corte 20:08 CDMX

- El HEAD de main avanzó de `6a96b3eb` a `2b30693dac44d3a60271065369f0465b7ba0b174`. El commit es de Grok Bot y modifica únicamente `data/endscreens_rotacion.json`; añade `snapshot_2026-11-27_20`/`propuesta_2026-11-27_20` con estado `pendiente_studio`. No añade storyboard, cola, salida ni publicación. Se leyó como evidencia externa; el archivo `data/*.json` no se modificó.
- La Action programada `Callback - aviso de delegaciones` (46095573475) terminó success. El log muestra el recorrido de delegaciones; no hubo salida de issue creado y no aparecieron issues nuevos. No se envió mensaje externo desde este run.
- En el nuevo commit de main, Semgrep (46096596549) volvió a fallar con **37 hallazgos bloqueantes**; Gitleaks y CodeQL terminaron success. No se alteraron hallazgos ni configuración.
- PR #3 continúa draft/open y no mergeable. Los checks dinámicos para los commits documentales de este corte quedaron en curso/cola al momento de esta lectura; no se hizo merge ni se disparó el dispatcher Grok.
- La nueva entrada `pendiente_studio` no cambia los conflictos de PAV1/Intermareal ni habilita Liquen/Rapaces. Los slots y clasificaciones de la sección anterior se mantienen.
