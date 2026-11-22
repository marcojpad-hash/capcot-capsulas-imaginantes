# Reconciliación de slots con main — 2026-11-21 23:57 CDMX

## Alcance y criterio

Auditoría de solo lectura sobre `main` para detectar procesamiento/programación previa antes de cualquier promoción desde `feature/capcot-video-discovery-continuity`. No se modificaron `main`, `data/*.json`, estados Grok, programación ni medios. No se disparó ningún workflow ni webhook.

La comparación de ramas devolvió `main` en `22cc55e0185f438fae2f7e5b85d70917185b02eb` y estado `diverged`: feature está 1,211 commits adelante y 509 detrás. No se sincronizó ni fusionó.

## Evidencia nueva de programación en main

La relectura de `main/data/miniaturas_auditoria_2026-11-21.json` (corte 23:12 CDMX) revela registros de YouTube con `estado=programado` y `publishAt` concretos. Esto reemplaza la conclusión anterior de que algunos slots de 22–23 nov solo aparecían en el plan semanal o no tenían ID visible.

| Fecha/slot CDMX | Resultado de cruce | Proyecto feature afectado |
|---|---|---|
| 21-nov 23:30 | Ocupado en main por programación preexistente | `2026-11-21_fentale-metano-sin-erupcion` |
| 22-nov 07:00 | Ocupado en main | `2026-11-22_voyager-1-un-dia-luz` |
| 22-nov 13:30 | Ocupado en main | `2026-11-22_bao-estrella-fusion-andromeda` |
| 22-nov 17:00 | Ocupado en main; además no es ventana autorizada por la política vigente | `2026-11-22_yubarta-genoma-soplo` |
| 23-nov 13:30 | Ocupado en main | `2026-11-23_tropical-biodiversity-turnover` |

La misma instantánea registra otros slots preexistentes el 22–23 nov, incluidos 19:00, fuera de la política horaria vigente. Se conservan como procesamiento/programación preexistente: no cancelar, reprogramar ni duplicar.

El archivo separado `main/data/resubidas_2026-11-21.json` registra dos resubidas ya programadas para el 22-nov (14:30 y 21:00 CDMX) y una propuesta posterior bloqueada por falta de MP4. No se copian aquí IDs privados/no publicados ni rutas de medios.

**Regla aplicada:** cualquier slot ocupado en main se clasifica `CONFLICTO_DE_SLOT_ENTRE_RAMAS`; cualquier video, salida o programación preexistente se clasifica `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`. No se promueve ninguno de los proyectos afectados.

## Revalidación de los siete storyboards recientes

Todos los archivos individuales `cola/estado/<project_id>.json` consultados devolvieron 404; se registra `RECEPCION_GROK_NO_CONFIRMADA`. No se crearon ni editaron estados.

| Proyecto | QA ya registrado | Hallazgo de esta pasada | Clasificación |
|---|---:|---|---|
| Fentale, 21-nov 23:30 | PASS 90 | DOI figura `VERIFICADO_CROSSREF` en el radar; Nature fecha el artículo 19-nov, no cumple la condición de dato publicado el mismo día. Main ya ocupa 23:30. | `NOT_DISPATCHABLE` |
| Homo erectus, 21-nov 07:00 | FAIL 83 | QA no supera compuerta. | `NOT_DISPATCHABLE` |
| Púlsar gamma, 21-nov 17:00 | FAIL 83 | QA no supera compuerta; 17:00 no está autorizado por la política vigente en main. | `NOT_DISPATCHABLE` |
| Voyager 1, 22-nov 07:00 | FAIL 83 | QA no supera compuerta y main ocupa el slot. | `NOT_DISPATCHABLE` |
| Bao, 22-nov 13:30 | FAIL 84 | QA no supera compuerta, falta `slot_cesta` y main ocupa el slot. | `NOT_DISPATCHABLE` |
| Yubarta, 22-nov 17:00 | PASS 90 | QA no elimina el conflicto de slot ni la ventana no autorizada. | `NOT_DISPATCHABLE` |
| Biodiversidad tropical, 23-nov 13:30 | FAIL 82 | `SRC-002=PENDING_SOURCE`, falta `slot_cesta` y main ocupa el slot. | `NOT_DISPATCHABLE` |

No se repitió ningún PASS ni se reescribieron narraciones/claims. Para Bao y Biodiversidad se releyeron también los paths de `ESTADO_EJECUCION.md`; ambos no existen.

## Lote interdiario 5–7 nov

Se releyeron los 12 storyboards y sus 12 paths de estado Grok: todos los estados devolvieron 404 (`RECEPCION_GROK_NO_CONFIRMADA`). Se conservan los dos QA PASS y diez FAIL previamente registrados; no se repitió la auditoría narrativa.

La inspección estructural estática vuelve a encontrar seis campos dramáticos obligatorios ausentes por escena (`dramatic_beat`, `scene_function`, `causal_bridge_from_previous`, `question_state`, `reason_to_continue`, `new_information`): **510 ausencias en total** entre los 12 storyboards. Los dos PASS narrativos no superan por ello la compuerta estructural. Ninguno es promovible.

## Cola heredada y recepción

- `cola/entrada/` conserva un único directorio anidado del robot orbital; no hay JSON plano de primer nivel en el inventario de control vigente.
- Su `ESTADO_EJECUCION.md` ya dice `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`, `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO` y `RECEPCION_GROK_NO_CONFIRMADA`.
- El marcador de `handoffs/grok_inbox` tiene estado `pending`; no es recibo de Grok.
- El workflow de despacho solo observa `cola/entrada/*.json` y el selector usa profundidad 1. La ruta anidada no es dispatchable. No se movió ni duplicó porque la programación previa en main está documentada y no debe alterarse.
- La auditoría de medios en main informa 36 videos programados sin MP4 local y seis colisiones de `publishAt` entre el 23 y el 28-nov. No se crearon medios ni placeholders.

## Historial y límites de verificación

No se encontró un archivo llamado `historial_youtube`. El recurso disponible es `main/data/vistas_historico.json`, cuyo último snapshot es 2026-11-21 13:54 CDMX; sirve para vistas, no como estado de programación en vivo. La auditoría de miniaturas de 23:12 es posterior y contiene el estado de programación usado arriba.

Una anotación histórica del control previo sobre un ID antiguo no pudo confirmarse en la búsqueda actual del árbol principal. Se mantiene como riesgo no verificado; no se canceló ni modificó ningún video. No hubo consulta autenticada a YouTube Studio en esta pasada.

## Resultado del run

- Storyboards recientes promovidos: **0**.
- Entradas Grok creadas: **0**.
- Estados Grok modificados: **0**.
- Webhooks/workflows disparados: **0**.
- Medios generados: **0**.
- Cambios en `main` o `data/*.json`: **0**.
- Decisión: mantener los siete proyectos en `proyectos/`; ninguno es `DISPATCHABLE`. El siguiente paso editorial es esperar un slot realmente libre y una fuente/estructura/QA que supere todas las compuertas, no duplicar la programación ya presente en main.

