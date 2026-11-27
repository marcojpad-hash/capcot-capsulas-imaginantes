# CONTROL DE COLA Y AUDITORÍA — 2026-11-27

**Corte inicial:** 27-11-2026 00:02 CDMX.  
**Rama de trabajo:** `feature/capcot-video-discovery-continuity`.  
**Rama de consulta:** `main`.  
**Alcance:** proyectos 24–30 nov, backlog interdiario, lote canónico 5–7 nov, colas anidadas y producción preexistente.

## Cambios ejecutados y lectura de vuelta

| Elemento | Resultado |
|---|---|
| `proyectos/2026-11-30_rapaces-clima-reino-unido/storyboard.json` | Se añadieron `new_information` a las ocho escenas y se normalizaron los cuatro valores de `arc` admitidos por el validador. No se cambió narración ni claims. Se sustituyó SRC-002 por la página oficial ONS de límites UK 2024. Lectura de vuelta: 182 palabras, 8 escenas, 78 s de escenas + 6 s de cortinilla = 84 s; los seis campos estructurales por escena están presentes; todos los arcos son válidos. |
| QA de rapaces | `FAIL/0`, `REVISION_INDEPENDIENTE_AUSENTE`. No se atribuye una auditoría independiente a una revisión del mismo autor. |
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
- QA: `FAIL/0`, `REVISION_INDEPENDIENTE_AUSENTE`.
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
- `data/publicaciones.json`: 62 registros; los últimos registros visibles llegan al 23-11-2026. No contiene `HSgrnejAcaI`.
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
