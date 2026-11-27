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

- **PASS:** `2026-11-05_kids-dia-en-venus` (88) y `2026-11-07_inter-pulpo-suenos` (94).
- **FAIL:** los otros diez IDs.
- Los doce carecen de los seis campos estructurales anteriores; los árboles del 5 nov también carecen de capa de mapa y dato/gráfico.
- Siete copias heredadas permanecen en `cola/bloqueados/` en la rama de trabajo. No se movieron ni borraron duplicados.
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
