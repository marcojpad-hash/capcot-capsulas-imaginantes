# CONTROL DE COLA — 2026-11-21

Repositorio: `marcojpad-hash/capcot-capsulas-imaginantes`  
Rama: `feature/capcot-video-discovery-continuity`  
Corte: 2026-11-21, America/Mexico_City  
HEAD auditado antes de este registro: `41ed5025eebbff79a618665b55296f5349e28bfb`  
Tipo: auditoría de solo lectura, contraste de cinco storyboards y verificación de rutas. No se generaron medios ni se despacharon workflows.

## 1. Fuentes efectivamente leídas

- Plan Maestro, Receta, Guía del modelo externo, Flujo Externo, contrato Grok y contrato narrativo.
- QA narrativo en frío, plantilla `storyboard_vertical.template.json`, catálogo `scripts/estilos.json`.
- `scripts/tendencias.py`, `scripts/registro_editorial.py`, `scripts/rotacion.py`, `scripts/validar_storyboard.py`.
- `.github/workflows/capcot-grok-dispatch.yml` y workflows de validación pertinentes.
- `data/horarios.json`, `data/publicaciones.json`, `data/rotacion.json`, `data/temas_del_dia.json`, `data/estilos_usados.json` en lectura; no se modificó ningún JSON de datos.
- Inventarios de `proyectos/`, `cola/entrada/`, `cola/bloqueados/`, `salidas/`, `handoffs/grok_inbox/` y los 12 IDs del lote 5–7 nov.
- `main/data/horarios.json` y `main/data/publicaciones.json` para conflicto exacto `fecha_objetivo + slot_local`.

## 2. Inventario actual

En `proyectos/` existen cinco storyboards recientes:

1. `2026-11-21_fentale-metano-sin-erupcion`
2. `2026-11-21_homo-erectus-selva-tropical`
3. `2026-11-21_pulsar-gamma-reticulo`
4. `2026-11-22_voyager-1-un-dia-luz`
5. `2026-11-22_yubarta-genoma-soplo`

`cola/entrada/` contiene solo dos carpetas anidadas heredadas: `2026-11-09_dato-robot-ensambla-orbita/` y `2026-11-11_dato-ratas-topo-damaraland/`, además de `.gitkeep`. No hay JSON plano de ninguno de los cinco proyectos recientes.

`handoffs/grok_inbox/` contiene únicamente el marker histórico `2026-11-09_dato-robot-ensambla-orbita.json` y README. No hay markers para los cinco proyectos recientes.

`salidas/` contiene expedientes antiguos hasta octubre; no hay salida de ninguno de los cinco proyectos recientes.

## 3. Cinco storyboards recientes: lectura de vuelta y compuertas

La revisión estructural de esta ejecución fue estática contra el contrato y las reglas visibles de `scripts/validar_storyboard.py`; no se ejecutó el script Python ni `--check-doi`. Se verificaron campos, voz, catálogo de estilo, escenas, palabras, suma de duración, cortinilla, mapas/datos, assets y estado de exportación. Los cinco cumplen esa revisión estática estructural. Esto no equivale a una ejecución del validador oficial ni a validación DOI.

| project_id | SHA actual del storyboard | Fecha / slot | Narrative QA existente | Revisión estructural estática | Fuente / DOI | Decisión |
|---|---|---|---|---|---|---|
| `2026-11-21_fentale-metano-sin-erupcion` | `54a2e8fb82f00ed383fb6f9b58815aebe798e518` | 21-nov · 23:30 | PASS 90/100 | 8 escenas; 170 palabras; 84 s; sin errores estáticos | Nature Geoscience; DOI `10.1038/s41561-026-02137-4`, `PENDIENTE_RESOLVEDOR` | NOT_DISPATCHABLE; no promover |
| `2026-11-21_homo-erectus-selva-tropical` | `e09d1311e77cf3d5176babbbd26f52eff589fc8d` | 21-nov · 07:00 | FAIL 83/100 | 8 escenas; 196 palabras; 84 s; sin errores estáticos | Nature; DOI `10.1038/s41586-026-11155-6`, resuelto en registro PubMed | NOT_DISPATCHABLE; no promover |
| `2026-11-21_pulsar-gamma-reticulo` | `372fc5aa84417eaf6e86735a2b5dc079f09167ee` | 21-nov · 17:00 | FAIL 83/100 | 8 escenas; 209 palabras; 84 s; sin errores estáticos | Physical Review Letters; DOI `10.1103/vlt2-xzgk`, página APS/DOI verificados | NOT_DISPATCHABLE; no promover |
| `2026-11-22_voyager-1-un-dia-luz` | `f47f173c2603ecce1ce137398e438725eff49e95` | 22-nov · 07:00 | FAIL 83/100 | 8 escenas; 180 palabras; 84 s; sin errores estáticos | NASA/JPL; fuente primaria, no aplica DOI | NOT_DISPATCHABLE; no promover |
| `2026-11-22_yubarta-genoma-soplo` | `4f5bf2ef427621828768327a4b3341eade37029c` | 22-nov · 17:00 | PASS 90/100 | 8 escenas; 180 palabras; 84 s; sin errores estáticos | Wiley; DOI `10.1111/1755-0998.70219`, enlace DOI resuelto a página editorial | NOT_DISPATCHABLE; no promover por ventana en prueba |

No se repitió QA narrativo ni se reescribieron narraciones/claims. Los PASS existentes se conservaron; los FAIL permanecen FAIL.

Para los cinco IDs, `cola/estado/<project_id>.json` devuelve 404: **`RECEPCION_GROK_NO_CONFIRMADA`**. Para los cinco, `salidas/<project_id>/` devuelve 404. No se creó ni editó estado Grok.

## 4. Dispatchabilidad real

El workflow `.github/workflows/capcot-grok-dispatch.yml` selecciona exclusivamente `cola/entrada/*.json` a profundidad 1; el filtro de diff también exige `^cola/entrada/[^/]+\.json$`. Las cinco storyboards están en `proyectos/<id>/storyboard.json`, no en la ruta seleccionable.

- Los cinco proyectos recientes: **NOT_DISPATCHABLE**.
- Las dos carpetas heredadas de `cola/entrada/`: tampoco coinciden con el selector JSON plano.
- El marker del robot es `pending`; no acredita lectura ni recepción Grok.
- No se creó ni modificó `cola/estado/`, no se enviaron payloads y no se disparó workflow.
- El estado de `GROK_WEBHOOK_URL` y `GROK_WEBHOOK_TOKEN` no se infirió: no se encontró una ejecución reciente del dispatch que permita afirmar que faltan.

## 5. Backlog de 12 IDs del 5–7 nov

Se rele­yeron los 12 `storyboard.json` y se compararon sus QA existentes con el corte del 20-nov. Los estados y scores no cambiaron; no se repitió ningún PASS.

| project_id | QA actual | Score |
|---|---:|---:|
| `2026-11-05_kids-dia-en-venus` | PASS | 88 |
| `2026-11-05_comida-palomitas` | FAIL | 82 |
| `2026-11-05_inter-arboles-se-comunican` | FAIL | 78 |
| `2026-11-05_inter-rayo-globular` | FAIL | 81 |
| `2026-11-06_kids-ballena-azul-corazon` | FAIL | 80 |
| `2026-11-06_comida-aguacate-negro` | FAIL | 79 |
| `2026-11-06_inter-ranas-congeladas` | FAIL | 83 |
| `2026-11-06_inter-arena-cantante` | PASS | 94 |
| `2026-11-07_kids-huesos-bebe` | FAIL | 82 |
| `2026-11-07_comida-hielo-caliente` | FAIL | 81 |
| `2026-11-07_inter-pulpo-suenos` | FAIL | 72 |
| `2026-11-07_inter-nubes-pesan` | FAIL | 78 |

Resultado: 2 PASS y 10 FAIL. Los 12 accesos `cola/estado/<id>.json` devuelven 404: `RECEPCION_GROK_NO_CONFIRMADA`. Se confirmó que siguen existiendo sidecars de plataforma en siete proyectos: Venus, palomitas, ballena azul, aguacate negro, ranas congeladas, arena cantante y hielo caliente. No se redispatchan por la mera presencia de sidecars.

## 6. Colisión con main y política de horarios

`main/data/publicaciones.json` contiene dos publicaciones para 2026-11-21:

- `2026-11-02_oxoboranos-estables`, 13:30 CDMX, YouTube ID `K4qNkx2f4RI`: **CONFLICTO_DE_SLOT_ENTRE_RAMAS** para cualquier nuevo paquete a las 13:30.
- `2026-11-09_dato-robot-ensambla-orbita`, 19:00 CDMX, YouTube ID `ZG4iQgmWrLI`: **PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR**. No cancelar, reprogramar ni duplicar.

`main/data/horarios.json` está actualizado al 2026-11-16: ventanas regulares 06:30–07:30 y 13:00–14:30; tarde 16:30–18:00 en prueba; 23:30 fijo para dato del día; 19:00 solo como prueba puntual con OK Mj, no como ventana regular. No hay publicación de 22-nov en `main/data/publicaciones.json` al corte; 22-nov 13:30 aparece libre, sujeto a fuente y rotación.

La copia de `feature/data/horarios.json` conserva corte 2026-11-09. `scripts/rotacion.py` sigue codificando cinco franjas (07:00, 13:30, 17:00, 19:00 y 23:30), por lo que hay divergencia entre política vigente en main, JSON histórico de feature y selector de rotación. `data/*.json` es de solo lectura y no se corrigió aquí.

## 7. Actions y logs

- **Trabajador de cola, run #21**: [run 44875678607](https://github.com/marcojpad-hash/capcot-capsulas-imaginantes/actions/runs/44875678607), 2026-11-21 06:28:09Z, rama `main`, conclusión success. Job `trabajar` terminó con salida literal `[trabajador] sin trabajo en cola.`. Solo consultó main; no procesó la rama feature.
- **Validación Kuroshio, run #7**: [run 44832382024](https://github.com/marcojpad-hash/capcot-capsulas-imaginantes/actions/runs/44832382024), rama feature, conclusión success. El log ejecutó `python scripts/validar_storyboard.py proyectos/2026-11-18_dato-kuroshio-puente-atmosferico/storyboard.json` sin `--check-doi`, y la comprobación textual del expediente. No valida DOI y no corresponde a los cinco proyectos actuales.
- No apareció una ejecución reciente de `capcot-grok-dispatch` en las 100 ejecuciones consultadas. No se infiere recepción ni estado de secretos.

## 8. Resultado de esta auditoría

- Inventario actual de cinco proyectos: EJECUTADO y leído de vuelta.
- Revisión estructural estática: 5/5 sin errores detectados; no se declara ejecución del validador oficial.
- QA narrativo: conservado; 2 PASS y 3 FAIL entre los cinco proyectos.
- Backlog 5–7 nov: 12/12 QA re-leídos; 2 PASS, 10 FAIL, sin cambios de estado.
- Recepción Grok: no confirmada para los cinco proyectos y los doce IDs del backlog.
- Dispatchabilidad: los cinco proyectos actuales NOT_DISPATCHABLE por ruta.
- Conflictos: 21-nov 13:30 ocupado por oxoboranos; 21-nov 19:00 tiene producción/programación previa del robot.
- Medios: no generados; publicación/programación: no ejecutada; créditos: no consumidos.
- Cambios de esta ejecución: solo los documentos de radar y control. No se modificaron storyboards, `data/*.json`, workflow, `main`, estados Grok, secretos ni decisiones editoriales.

## 9. Siguiente operación mínima

1. Resolver el DOI de Fentale y confirmar la frescura de la fuente antes de considerar el slot 23:30.
2. Corregir las narraciones FAIL en el flujo de investigación y someterlas después a QA frío independiente; esta auditoría no las reescribe.
3. Confirmar explícitamente si la ventana 16:30–18:00 se usa para publicaciones o sigue siendo solo prueba.
4. Reconciliar el selector de rotación con la política fechada de horarios sin modificar `data/*.json` ni ampliar el dispatch a carpetas heredadas.
5. Mantener los cinco storyboards fuera de cola hasta que todas las compuertas y la recepción estén respaldadas.


## 10. Relectura del backlog interdiario 18–20 nov

Se releyeron los seis storyboards que siguen en `proyectos/`. Sus QA existentes no cambiaron; no se repitió ninguna lectura PASS. Los SHA siguientes son los blobs leídos en esta revisión.

| project_id | blob actual | slot | QA | estructura leída | compuerta pendiente |
|---|---|---:|---:|---|---|
| `2026-11-18_dato-catorce-campos-hidrotermales` | `912fb2222ea5106d763c9e94bd95d9f9d66ebe41` | 23:30 | FAIL 68 | 8 escenas, 198 palabras, 84 s; mapa con punto regional | QA FAIL y **CONFLICTO_DE_SLOT_ENTRE_RAMAS** con Beta Pictoris en main |
| `2026-11-18_dato-kuroshio-puente-atmosferico` | `2046152ade90fffaf9527d180e13cc5f6009fb60` | 17:00 | PASS 90 | 8 escenas, 222 palabras, 84 s; capa de regiones válida | DOI `10.1038/s41561-026-02139-2` sigue `PENDIENTE_RESOLVEDOR`; 17:00 sigue siendo ventana de prueba |
| `2026-11-19_dato-dia-luz-dos-manos-oro-poroso` | `a211420b3a8850a1866e9311b5930c4360b0703c` | 23:30 | PASS 91 | 8 escenas, 188 palabras, 84 s; puntos institucionales etiquetados como afiliaciones | DOI `10.1038/s41467-026-78158-9` sin resolver independientemente |
| `2026-11-19_dato-estrella-dentro-de-estrella` | `b55ae1d811cd70fd8953efb1f443851478b611dd` | 17:00 | PASS 90 | 8 escenas, 197 palabras, 84 s; coordenadas ecuatoriales J2000 RA/Dec | DOI `10.1038/s41586-026-11221-z` pendiente y estilo repetido el mismo día |
| `2026-11-20_dato-dia-atlantico-humedad-sapropeles` | `8f93c79d319da22c7af80e72f4b1a41c0446abda` | 23:30 | PASS 91 | 8 escenas, 215 palabras, 84 s; punto IODP U1385 | DOI `10.1038/s41561-026-02141-8` sin resolver independientemente |
| `2026-11-20_dato-marea-cerebral-en-sueno` | `5941a27c80610e22402dd98d36150464bbd4fa48` | 17:00 | PASS 92 | 8 escenas, 218 palabras, 84 s; campus BU/MIT etiquetados como aproximados | DOI `10.1038/s43587-026-01270-4` pendiente y 17:00 sigue siendo ventana de prueba |

**Corrección de mapa:** la capa de la estrella declara `Ecuatoriales J2000 (RA/Dec)`; el validador vigente acepta RA/Dec además de lat/lon. No se conserva la objeción anterior de que esa capa carece de coordenadas válidas. La compuerta DOI sigue abierta.

**Rotación:** Juno, programado en main para el 19-nov a las 13:30, usa `art_deco_poster`; la estrella del 19-nov a las 17:00 usa el mismo estilo. La repetición queda confirmada por los dos storyboards y el registro de publicación de main, no por los JSON de rotación: `data/estilos_usados.json` termina el 28-oct y `data/rotacion.json` el 31-oct. Ambos siguen solo lectura y no se corrigieron.

**Producción preexistente en main:**
- Beta Pictoris ocupa el 18-nov 23:30 con YouTube ID `2a36r5QOvi4`, duración registrada 61.27 s y programación privada. No redispatchar.
- REACT proteínas/microbios conserva programación para el 20-nov 13:45 (`publish_at=2026-11-20T19:45:00Z`). Su storyboard referencia `capsula.mp4`, pero el MP4 no aparece en el árbol de main: `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR` y `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`.
- Ninguno de los seis storyboards de 18–20 nov tiene entrada plana exacta, salida ni estado Grok en feature. `cola/estado/` contiene cero archivos en el árbol actual; la recepción sigue `RECEPCION_GROK_NO_CONFIRMADA`.

## 11. Relectura de selector, Actions e Issues

- `.github/workflows/capcot-grok-dispatch.yml` selecciona JSON planos de primer nivel en `cola/entrada/`; no recoge `proyectos/<id>/storyboard.json` ni JSON anidados. `scripts/procesar_cola.py` contempla el nivel raíz y un nivel anidado; `registro_editorial.py` recorre recursivamente. El selector del workflow no equivale a esos lectores. No se amplió el dispatch ni se modificó el workflow.
- `Trabajador de cola`, run [44875678607](https://github.com/marcojpad-hash/capcot-capsulas-imaginantes/actions/runs/44875678607), terminó SUCCESS con salida literal `[trabajador] sin trabajo en cola.`; corrió en main, no en feature.
- Los checks CodeQL del PR #3 posteriores a los commits de documentación terminaron SUCCESS: runs 44892824568 y 44892820908. No fueron dispatches Grok.
- Dependabot, run 44888462739, terminó FAILURE: `Failed to parse GITHUB_REGISTRIES_PROXY environment variable` y `dependency_file_not_found` para el directorio `/`. No se cambió configuración en main.
- El callback programado 44890871984 terminó SUCCESS. Su workflow tiene permiso de Issues y contiene `gh issue create` para delegaciones; esta auditoría no lo disparó. La búsqueda actual no encontró Issues abiertos con etiqueta `callback`.
- No se encontró ejecución reciente de `capcot-grok-dispatch` entre las 100 ejecuciones consultadas. El estado de `GROK_WEBHOOK_URL` y `GROK_WEBHOOK_TOKEN` sigue sin inferirse.
- PRs abiertos sin merge: #3 (draft, feature→main), #13 y #14 (→main), #4 y #6 (feature). No se cambió ni aprobó ninguno.
- Issues abiertos con etiquetas `cola` o `bloqueado` en CAPCOT: cero. En el ledger de main, `CUASARES-AUDITORIA` pertenece a revisión independiente, `GROK-RECEPCION` está bloqueado en Grok y `MIGRACION-ACUSE` corresponde a otro modelo; ninguno está asignado a ChatGPT.

**Cierre ampliado:** seis proyectos interdiarios re-leídos; 5 PASS preservados y 1 FAIL preservado. No se repitió QA narrativo, no se promovió ningún proyecto, no se generaron medios ni se consumieron créditos. Los JSON de `data/`, los workflows, main, los estados Grok y las decisiones editoriales permanecen intactos.


## ADENDA DE RELECTURA — 2026-11-21 (verificación posterior)

### Inventario y recepción

- Relectura de **23 storyboards**: 5 del 21–22 nov, 6 interdiarios del 18–20 nov y los 12 canónicos del lote 5–7 nov. En los 23 casos, `cola/estado/<project_id>.json` devuelve 404: **RECEPCION_GROK_NO_CONFIRMADA**. No se creó ningún estado.
- QA sin cambios: actuales **2 PASS / 3 FAIL**; interdiarios **5 PASS / 1 FAIL**; lote 5–7 nov **2 PASS / 10 FAIL**. No se repitió lectura narrativa PASS ni se promovió ningún storyboard.
- No hay `ESTADO_EJECUCION.md` para los 12 canónicos del lote. Los dos expedientes interdiarios que sí lo tienen —catorce campos hidrotermales y Kuroshio— declaran `BORRADOR_EN_PROYECTOS_NO_APTO_PARA_PROMOCION`; no se encontró estado PREPARADO que requiriera corrección.

### Lote 5–7 nov: copias bloqueadas

- Se verificaron las **12 rutas heredadas** indicadas en `ajustes_entre_modelos/PARA_CHATGPT_5-7nov_PASS_auditor.md`. También existen **9 archivos .json paralelos** y la carpeta adicional `2026-11-07_extra-nubes-pesan/`.
- Las copias bloqueadas no contienen `narrative_qa`. Al comparar narración con los 12 storyboards canónicos de `proyectos/`, diez conservan la misma narración; difieren las versiones bloqueadas de árboles (**182 frente a 170 palabras**) y nubes (**227 frente a 221 palabras**).
- Todo permanece dentro de `cola/bloqueados/`; no se fusionó, sobrescribió ni eliminó ninguna variante. Las copias bloqueadas no se consideran recepción Grok ni habilitan despacho.

### Producción previa y medios

- `2026-11-07_comida-hielo-caliente` y `2026-11-07_inter-nubes-pesan` ya tienen registros de publicación en main (YouTube IDs `HSgrnejAcaI` y `4Qpl17Ts_vI`). Solo se encontró storyboard de salida para comida caliente; los MP4 referenciados no están en el árbol. **PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR / MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO**.
- El paquete anidado de robot conserva QA PASS y un marcador de inbox con estado `pending`, pero no `cola/estado`. Main registra programación para el 21-nov a las 19:00 CDMX; no se localizaron `publicacion.json`, `metadata.json`, `qa.json`, `storyboard.json` ni `capsula.mp4` bajo `salidas/<id>/`. **PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR / MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO**.
- Ratas topo ya aparece publicado el 12-nov a las 07:00 CDMX (YouTube `WcTviUWqbes`) y conserva storyboard, metadata, QA y publicación en `salidas/`; el MP4 no está en el árbol. **PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR / MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO**.
- No se encontró `salidas/<id>/storyboard.json` ni registro en `data/publicaciones.json` para los cinco proyectos actuales y los seis interdiarios.

### Compuertas y automatización

- La revisión estructural manual de Fentale y Yubarta da **84 s**, 8 escenas y **172 / 180 palabras**, con voz, capas de mapa/dato, ambiente/SFX, `approved_assets=[]` y `render_status=NOT_GENERATED`. Esto no sustituye una ejecución del validador.
- Fentale mantiene DOI `10.1038/s41561-026-02137-4` pendiente de resolución independiente. Yubarta registra `VERIFICADO_RESOLVEDOR` para `10.1111/1755-0998.70219`; PubMed coincide con el DOI. El run de validación `44832382024` no usó `--check-doi`. Fentale (23:30 fijo) y Yubarta (17:00, ventana en prueba) siguen **NOT_DISPATCHABLE** por compuertas pendientes y ausencia de estado Grok.
- El workflow `capcot-grok-dispatch.yml` solo selecciona JSON planos en la raíz de `cola/entrada/`; las carpetas anidadas no entran. Escribe un marcador `pending` en `handoffs/grok_inbox/`, no un estado Grok. No se disparó.
- Actions verificadas: run `44875678607` terminó SUCCESS con `[trabajador] sin trabajo en cola`; run `44832382024` terminó SUCCESS con validación textual, sin DOI; CodeQL del PR #3 `44893426171` SUCCESS. Dependabot mantiene fallo de configuración. PR #3 y PR #14 siguen abiertos; no se hizo merge.
- Rotación aún desfasada: `data/rotacion.json` llega al 31-oct, `data/estilos_usados.json` al 28-oct, `data/tendencias_estilos.json` al 31-oct y `data/cola.json` al 31-oct. Los archivos `data/*.json` permanecieron intactos.

**Acciones de esta relectura:** solo consultas y comparación de blobs/logs. No se escribieron entradas de cola, estados Grok ni data; no se dispararon workflows, no se generaron medios, no se publicó ni se consumieron créditos.


## 12. Relectura de Actions, PRs y producción heredada — 2026-11-21 (corte 08:02–08:06 CDMX)

### Rama y ejecuciones
- HEAD de feature al corte: `0516a346538a61f5a0ecd960c980fb1b64d8459c`; main permanece en `8ceba2a913806acb665c5491fca8a76f93fab2ba`. El commit de feature actualizó únicamente este RADAR existente (+114 líneas); no creó un segundo radar.
- La automatización investigadora terminó a las 08:05:14 CDMX y su resultado atribuye el commit `0516a346` al radar del 21-nov. No se atribuye ese cambio a esta auditoría.
- CodeQL del PR #3, run [44912070522](https://github.com/marcojpad-hash/capcot-capsulas-imaginantes/actions/runs/44912070522), SUCCESS en los análisis Python y Actions. No es un dispatch Grok.
- Gitleaks, run [44901564264](https://github.com/marcojpad-hash/capcot-capsulas-imaginantes/actions/runs/44901564264), FAILURE: un hallazgo `generic-api-key` en `docs/SKILL_DRAFT_capsula_diaria.md:17`, asociado al commit histórico `a4ccf1974a8966d5801a991ac25609ef4d7cdca7`. La línea histórica es prosa documental que comienza «Con key:» y continúa con un comando Python; parece un falso positivo del patrón genérico, pero requiere triage del mantenedor. La versión actual de main tiene otra línea 17. No se reprodujo ni copió ningún valor, no se modificó ninguna credencial y no se declaró un secreto real.
- El run del trabajador de cola [44875678607](https://github.com/marcojpad-hash/capcot-capsulas-imaginantes/actions/runs/44875678607) terminó SUCCESS en main con `[trabajador] sin trabajo en cola.`; no acredita procesamiento de feature. En las 15 Actions recientes consultadas no aparece ejecución de `capcot-grok-dispatch`.
- La consulta de inventario de secretos de Actions no está expuesta por el conector; devolvió literalmente `HTTP 400: GitHub Fetch URL is not an allowed public GitHub repository or search endpoint.` No se clasificó ningún nombre como ausente y no se leyó ningún valor.

### Pull requests abiertos — relectura viva
- **PR #3**, feature→main: OPEN, draft, `mergeable=false`; 686 archivos, 76,820 adiciones y 1,694 eliminaciones. El diff contiene 13 archivos `data/*.json` modificados/agregados y 78 artefactos bajo `_tmp/`. Esto contradice la regla vigente de solo lectura de data y deja el PR no apto para merge sin separar/restaurar esos cambios. No se modificó el PR ni sus datos.
- **PR #14**, cuásares: OPEN, mergeable. Modifica el storyboard y el ledger; agrega `asset_filename` a las ocho escenas, conserva el `narrative_qa` histórico FAIL/82 y declara que no ejecutó `validar_storyboard.py --check-doi`. No cumple las compuertas actuales; no se promovió.
- **PR #13**, auditoría independiente de cuásares: OPEN; agrega `AUDITORIA.md`, no actualiza por sí mismo el `narrative_qa` del storyboard ni habilita promoción.
- **PR #4**, ubicación de frames ASTRA: OPEN. Cambia el estado del paquete robot para decir que los frames fueron generados en el chat de Grok, pero la carpeta `cola/entrada/2026-11-09_dato-robot-ensambla-orbita/frames/` contiene únicamente `.gitkeep`. Los binarios no están verificados en GitHub.
- **PR #6**, supervisor genérico: OPEN hacia feature. Añade un workflow con `secrets: inherit` y permiso `issues: write`; el workflow reutilizable en `agente-cero-costo` puede crear/comentar una orden en el bus central al fallar, o hacerlo en el repo llamador si no dispone del token opcional. No se ejecutó. Queda como revisión de alcance/permisos antes de cualquier integración.
- **PR #7, #8 y #9**, actualizaciones de Actions: OPEN, sin merge. No se alteraron dependencias ni workflows.

### Inventario, slots y medios
- Se releyeron los cinco storyboards del 21–22 nov con la expresión de palabras de `scripts/validar_storyboard.py`: Fentale 170, Homo erectus 196, púlsar 209, Voyager 180 y yubarta 180; los cinco tienen 8 escenas y 84 s. QA preexistente: 2 PASS / 3 FAIL. No se repitió lectura narrativa PASS.
- El 21-nov sigue completamente ocupado: feature 07:00 Homo erectus, 17:00 púlsar y 23:30 Fentale; main 13:30 oxoboranos y 19:00 robot. Fentale conserva fuente del 19-nov, no apta para la regla de dato del día del 21. El 22-nov ya tiene Voyager 07:00 y yubarta 17:00 en proyectos; la ventana de yubarta sigue siendo de prueba. No se creó storyboard nuevo.
- `cola/estado/` devuelve 404. `handoffs/grok_inbox/` contiene solo el marker histórico del robot con estado `pending`; no acredita recepción. No se creó ni modificó estado Grok.
- `cola/entrada/` contiene dos carpetas anidadas heredadas y ningún JSON plano: robot y ratas topo. El workflow Grok selecciona JSON planos de primer nivel; las rutas anidadas no son dispatchables por ese selector.
- Robot: main conserva programación del 21-nov 19:00 y YouTube ID `ZG4iQgmWrLI`; no hay salida del robot en main y los frames de feature son solo `.gitkeep`. Clasificación: `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR` y `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`.
- Ratas topo: main contiene `salidas/2026-11-11_dato-ratas-topo-damaraland/` con storyboard, QA, publicación y programación; feature conserva ocho PNG en su carpeta de frames. La pieza ya está publicada y el MP4 no aparece en el árbol. No redispatchar.
- `cola/bloqueados/` tiene 47 entradas; los 12 IDs canónicos del 5–7 nov mantienen 2 PASS / 10 FAIL. Se releyeron sus storyboards canónicos y se compararon copias disponibles; las variantes de árboles y nubes siguen siendo distintas. No se fusionó, movió ni borró ninguna copia.
- Los JSON de `data/`, main, workflows, estados Grok, medios, publicaciones y programación permanecieron intactos.

### Resultado de esta auditoría
- Operación ejecutada: relectura de inventario, estados, PRs, Actions, logs y fuentes cruzadas; se añadió esta adenda al control existente.
- No se ejecutó el validador Python en runtime ni `--check-doi`; los conteos anteriores son estáticos con la expresión del script.
- No se promovió ni redispatchó, no se generaron medios, no se publicó, no se consumieron créditos, no se enviaron mensajes, no se cambiaron secretos/permisos y no se hizo merge.


## 13. Compuertas estructurales de los cinco storyboards 21–22 nov — verificación estática

Se releyeron los cinco JSON directamente desde GitHub y se contrastaron con la expresión de palabras de `scripts/validar_storyboard.py` y con `scripts/estilos.json`.

| Proyecto | Slot | Palabras | Escenas | Duración total | Estilo/prompt | QA |
|---|---:|---:|---:|---:|---|---|
| Fentale | 21-nov 23:30 | 170 | 8 | 84 s | catálogo coincide | PASS/90 |
| Homo erectus | 21-nov 07:00 | 196 | 8 | 84 s | catálogo coincide | FAIL/83 |
| Púlsar gamma | 21-nov 17:00 | 209 | 8 | 84 s | catálogo coincide | FAIL/83 |
| Voyager 1 | 22-nov 07:00 | 180 | 8 | 84 s | catálogo coincide | FAIL/83 |
| Yubarta | 22-nov 17:00 | 180 | 8 | 84 s | catálogo coincide | PASS/90 |

- Los cinco usan `edge-tts`, voz `es-MX-JorgeNeural`, rate `+7%`, pitch `-2Hz`; todos tienen cortinilla de 6 s, `approved_assets=[]`, `export.render_status=NOT_GENERATED`, `publicacion.status=PENDIENTE_DECISION_GROK` y no contienen `asset_filename`, `asset_type` ni `export.filename`.
- En los cinco, `visual_identity.prompt_base` coincide exactamente con el estilo de `scripts/estilos.json`; las ocho escenas contienen ambiente y SFX; todos los `source_ids` de escena existen en `sources`.
- Los cinco contienen capa de mapa y capa de dato: Fentale usa coordenadas GVP (localizan el complejo, no el punto exacto de emisión); Homo usa el sitio de referencia; el púlsar usa coordenadas celestes ICRS; Voyager usa tres puntos de trayectoria; yubarta usa límites regionales de referencia del catálogo Hakai, no coordenadas exactas de muestras. No se inventaron coordenadas.
- Fentale y Yubarta conservan QA independiente en commits separados posteriores al borrador: `18492e0d9f0db615f5af81cb420d48efaf07606a` y `5abae820ba8ac3a244db8d081738c979d4d2aaff`, respectivamente. En ambos hay siete checks true, `review_basis=lectura_en_frio_solo_narracion` y `critical_flags=[]`; no se repitió la lectura narrativa.
- Homo y púlsar conservan FAIL/83 por giro científico nombrado pero no explicado. Voyager conserva FAIL/83 por confundir fecha del hito con fecha de confirmación. No se reescribieron narraciones ni claims.
- DOI: Homo, púlsar y yubarta conservan estado verificado; Voyager usa fuentes sin DOI; Fentale sigue `PENDIENTE_RESOLVEDOR`. Se intentaron rutas Crossref REST, página Crossref y doi.org; las tres fueron rechazadas por la herramienta web con `URL ... is not accessible via this tool`. No se marcó Fentale como verificado y no se ejecutó `--check-doi`.
- Ninguna carpeta de proyecto 21–22 contiene `ESTADO_EJECUCION.md`; los cinco siguen como borradores en `proyectos/`. La revisión estructural de esta sección es estática, no una ejecución del validador Python.


## 14. Reconciliación operativa posterior — 2026-11-21, 10:00 CDMX

### Estado vivo de rama, slots y recepción

- HEAD de `feature/capcot-video-discovery-continuity` al inicio de esta reconciliación era `49db1df246b241e431683f7eb501911dcae72ec9`; no había commits de trabajo posteriores a la adenda 13. Esta reconciliación queda registrada en el commit `a6e86c01637aac47e89ee7f01910d8f33b8d6f35`. Se releyó el inventario de `proyectos/`: los cinco storyboards 21–22 nov conservan los mismos blobs, estructura y QA; no se repitió lectura narrativa PASS.
- Los cinco proyectos siguen sin `ESTADO_EJECUCION.md`; no existe un estado PREPARADO que requiera corrección.
- Para los cinco IDs actuales, `cola/estado/<project_id>.json` devuelve 404: **RECEPCION_GROK_NO_CONFIRMADA**. No se creó ni modificó ningún estado.
- `cola/entrada/` contiene `.gitkeep` y dos directorios heredados anidados (robot y ratas topo), pero ningún JSON plano en la raíz. `handoffs/grok_inbox/` contiene únicamente el marcador histórico del robot con estado `pending`; no acredita recepción.
- Se releyó `data/publicaciones.json` de main: el 21-nov aparecen oxoboranos a las 13:30 y robot orbital a las 19:00, ambos con datos de publicación/programación. Ninguno coincide exactamente con los slots de los cinco borradores actuales (21-nov 07:00, 17:00, 23:30; 22-nov 07:00 y 17:00). Por tanto, no se registra conflicto de slot para esos cinco; el robot conserva **PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR**. No se duplicó ni canceló nada.
- El trabajador de cola, run [44922052187](https://github.com/marcojpad-hash/capcot-capsulas-imaginantes/actions/runs/44922052187), terminó SUCCESS en **main**. Su log contiene literalmente `[trabajador] sin trabajo en cola.`; no procesó la rama feature ni acredita recepción Grok.
- La consulta de Actions entre el 1 y el 2 de noviembre devuelve 48 ejecuciones de `capcot-grok-dispatch`, todas FAILURE; entre el 20 y el 21 de noviembre no aparece ninguna. No se disparó el workflow. El estado actual de `GROK_WEBHOOK_URL` y `GROK_WEBHOOK_TOKEN` sigue sin inferirse.

### Seguridad y calidad de código

- Gitleaks, run [44901564264](https://github.com/marcojpad-hash/capcot-capsulas-imaginantes/actions/runs/44901564264), terminó FAILURE por una regla `generic-api-key` en `docs/SKILL_DRAFT_capsula_diaria.md:17`, commit histórico `a4ccf1974a8966d5801a991ac25609ef4d7cdca7`. Se leyó ese blob histórico: la línea contiene únicamente el literal documental `CAPCOT_LLM_API_KEY=...`, no un valor de credencial. Clasificación: **FALSO_POSITIVO_PROBABLE**; se deja el hallazgo para triage del mantenedor, sin cerrar el finding, modificar secretos ni exponer valores.
- CodeQL del PR #3, run [44912070522](https://github.com/marcojpad-hash/capcot-capsulas-imaginantes/actions/runs/44912070522), terminó SUCCESS. No es una validación de DOI ni un dispatch.
- `scripts/registro_editorial.py` normaliza publicaciones sin conservar `slot_local`, `publishAt` ni `video_id`, y no lee `data/horarios.json` ni `data/horario_*.json`. El snapshot de horarios de feature sigue fechado el 9-nov y no refleja los dos registros de publicación de main del 21-nov. Esto puede subcontar ocupación y rotación al usar el inventario de feature por sí solo. Se documenta como mejora pendiente de script y pruebas; no se modificó el script ni ningún `data/*.json`.
- Se intentó ejecutar el validador estructural real fuera de Actions. `container.download` rechazó la URL porque no estaba disponible para lectura web; la alternativa `curl` devolvió literalmente `Could not resolve host: raw.githubusercontent.com`. No se disparó un workflow como alternativa. La revisión estructural permanece **ESTÁTICA**, no se declara ejecución del validador ni de `--check-doi`.
- Las consultas Crossref REST y DOI resolver continuaron inaccesibles desde la herramienta web; las páginas editoriales/PubMed visibles corroboran los identificadores de los artículos correspondientes, pero no sustituyen la compuerta oficial `--check-doi`. Fentale conserva `PENDIENTE_RESOLVEDOR`.

### Cierre de esta reconciliación

No se promovió ningún storyboard, no se escribió en cola, no se creó estado Grok, no se envió webhook, no se publicaron ni programaron cápsulas, no se generaron medios, no se consumieron créditos y no se modificó main, `data/*.json`, workflows, secretos o permisos. El siguiente paso técnico de CAPCOT es corregir y probar el inventario de slots en `registro_editorial.py` en una revisión aislada, y ejecutar el validador real con `--check-doi` cuando exista una vía de ejecución autorizada.


## 15. Frescura de `data/*.json` — lectura 2026-11-21

Se relevaron los JSON de `data/` sin modificarlos. La fotografía de rotación/publicación no está sincronizada con los proyectos actuales:

- `horarios.json`: último dato 2026-11-09; no contiene 21–22 nov.
- `horario_2026-11-11.json`: último archivo diario de horario; no hay archivos diarios 12–21 nov.
- `horario_semana_2026-11-01_07.json`: cubre únicamente 1–7 nov.
- `publicaciones.json` de feature: 22 registros, rango 24-oct–1-nov; no contiene los registros actuales del 21–22 nov que sí aparecen en main.
- `rotacion.json`: rango 24–31 oct. `cola.json`: un registro del 31-oct. `temas_del_dia.json`: rango 24–28 oct. `estilos_usados.json`: 21 registros y rango 24–28 oct. `tendencias_estilos.json`: actualizado 31-oct.
- `balances_6h.json` y `vistas_historico.json` terminan el 28-oct; `cierre_diario/` solo contiene 25, 26 y 27-oct. `reprogramacion_tt_fb_v4_2026-11-01_03.json` conserva el lote 1–3 nov.
- `endscreens_rotacion.json` sí tiene actualización hasta 17-nov, pero es un registro de pantallas finales, no una parrilla de slots diarios.

Conclusión: los JSON de rotación, horario, publicaciones e historial no pueden usarse como fuente actual única para reservar slots del 21–22 nov. Para esta reconciliación se contrastaron los storyboards vivos de feature con `data/publicaciones.json` de main. El inventario `registro_editorial.py` no lee los snapshots de horario ni conserva todos los campos de publicación, por lo que no detecta por sí solo esta divergencia. No se cambió ningún `data/*.json`.


---

## Reconciliación adicional — 21-nov-2026, 12:03 CDMX

### Cambios materiales en el inventario

**EJECUTADO — `scripts/registro_editorial.py`**

La vista de inventario ahora expone `ocupacion_slots` con:
- evidencia de `data/publicaciones.json`, `data/rotacion.json` y `data/cola.json`;
- storyboards y sidecars JSON bajo `proyectos/`, `cola/` y `salidas/`, incluida la profundidad anidada;
- normalización de `publishAt`, `publishedAt` y timestamps UTC a `America/Mexico_City`;
- conflictos entre proyectos distintos en el mismo `fecha + slot_local`;
- discrepancias de slot entre evidencias del mismo project_id;
- inconsistencias entre el timestamp publicado/programado y la fecha/hora local declarada;
- referencias de medios presentes o ausentes en el árbol, con `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO` cuando corresponde;
- IDs y estados anidados de YouTube/TikTok/Facebook sin confundir IDs de fuentes con IDs de video.

El CLI incluye ahora el inventario de slots. El código no escribe `data/*.json`; solo los lee. El inventario sigue siendo **local a la rama ejecutada**: la comparación contra main debe hacerse aparte y no se considera resuelta por la salida de feature.

**EJECUTADO — pruebas**

- `tests/test_registro_editorial.py` contiene 17 métodos de prueba.
- Un harness Python aislado verificó 14 casos/condiciones: slots de storyboard, conversión UTC→CDMX, conflicto entre proyectos, discrepancia de un mismo proyecto, estados bloqueados, fecha sin hora, timestamp discordante, sidecars anidados de YouTube, publicación anidada, IDs de fuente no confundidos con video y referencias de medios presentes/ausentes.
- **Límite:** no se ejecutó la suite unittest completa desde un checkout del repositorio. Los checks CodeQL automáticos de PR #3 completaron SUCCESS para varios commits; los runs más recientes siguen IN_PROGRESS. CodeQL no equivale a ejecutar las pruebas unitarias.

### Ocupación confirmada

- **21-nov:** 07:00 Homo erectus (feature); 13:30 oxoboranos (registro de publicación en main); 17:00 púlsar gamma (feature); 19:00 robot orbital (registro de publicación en main); 23:30 Fentale (feature). Los cinco slots están ocupados. No se creó otro proyecto para el 21.
- **22-nov:** 07:00 Voyager 1 y 17:00 Yubarta ocupados en feature. 13:30, 19:00 y 23:30 no muestran ocupación en los inventarios visibles de ambas ramas al corte. 23:30 permanece reservado a un dato publicado el mismo día y dentro de 48 horas.

### Auditoría de proyectos y handoffs

- Cinco proyectos nuevos de 21–22 nov revisados. QA registrado: Fentale PASS/90; Homo erectus FAIL/83; Púlsar gamma FAIL/83; Voyager 1 FAIL/83; Yubarta PASS/90. Los cinco `cola/estado/<id>.json` devolvieron 404: `RECEPCION_GROK_NO_CONFIRMADA`. No hay entrada plana nueva para ellos y no se promovió ninguno.
- Los doce storyboards del lote 5–7 nov fueron releídos; todos sus estados individuales de Grok devolvieron 404. Los siete proyectos con sidecars sociales conservan evidencia de publicaciones/programaciones preexistentes; no se redispatchó. Las copias heredadas ya presentes en `cola/bloqueados/` se dejaron intactas.
- Nueve proyectos/paquetes de 15–20 nov en main fueron contrastados con `cola/entrada/`, `salidas/`, `programacion.json` y estados. No se modificó main. Hay paquetes con programación/IDs preexistentes, una divergencia de SHA entre proyecto y cola para Accidente IA, y referencias `capsula.mp4` que no aparecen en el árbol de algunos proyectos. Clasificación: `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`, `DIVERGENCIA_DE_COPIA_PROYECTO_COLA` o `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO` según evidencia. Los estados Grok individuales ausentes se mantienen como `RECEPCION_GROK_NO_CONFIRMADA`.
- Los registros de publicación en main para 21-nov confirman los slots 13:30 y 19:00. La copia de `data/publicaciones.json` en feature no incluye esos registros; por eso no se usó el inventario de feature como prueba suficiente de disponibilidad global.

### Investigación y preproducción

Se creó `docs/briefs/2026-11-22_RADAR_CAPCOT.md` y el borrador `proyectos/2026-11-22_bao-estrella-fusion-andromeda/storyboard.json`.

- AT 2025abao, paper de Nature del 18-nov, seleccionado para 22-nov 13:30.
- Narración verificada por conteo: 192 palabras; 8 escenas; 78 s de escenas + 6 s de cortinilla = 84 s; gancho de 6 palabras; cierre hablado exacto.
- Voz `es-MX-JorgeNeural`, rate +7%, pitch -2Hz; estilo `art_deco_poster` del catálogo.
- Mapa con RA/Dec de NASA (RA 00:38:48.60; Dec +40:46:08.23) y conversión aritmética explícita a grados.
- Incluye dato/gráfico de masas estimadas y observación infrarroja de Webb 47 días después del pico.
- **No** se creó `narrative_qa`; no hubo pasada independiente en frío. El proyecto permanece `BORRADOR_EN_PROYECTOS_NO_APTO_PARA_PROMOCION`, con `approved_assets=[]`, `export.render_status=NOT_GENERATED` y `publicacion.status=PENDIENTE_DECISION_GROK`.
- No se creó cola, estado Grok, medio, render ni publicación.

### Ingesta RSS y límites de verificación

Los feeds definidos en `scripts/tendencias.py` y Google Trends RSS México no entregaron contenido utilizable en esta sesión: ScienceDaily `application/xml`; Phys.org `text/xml`; NASA/Nature/UNAM `application/rss+xml`; ESA `404 Not Found`; EurekAlert, SINC y Trends no devolvieron cuerpo parseable. La descarga alternativa de ScienceDaily terminó en `download failed`. Se usaron páginas oficiales y papers como respaldo; los fallos no se interpretaron como ausencia de noticias.

### No modificados

`data/*.json`, `cola/entrada/`, `cola/estado/`, workflows, secretos, permisos, main, publicaciones y medios permanecen sin cambios por este run. No se disparó el workflow de dispatch ni se envió payload a Grok.

## 16. Corrección técnica de ocupación horaria — run operador, 2026-11-21

### Cambios ejecutados y leídos de vuelta

- `scripts/registro_editorial.py`: `ocupacion_slots()` incorpora los snapshots `data/horario_*.json`, tanto `slots` como `atrasados_revisados`. Omite slots sin ID, conserva la fecha/hora original de atrasados y reconoce timestamps de YouTube/TikTok/Facebook.
- La extracción de medios incluye `mp4`, rutas de video/audio y referencias de escena. La búsqueda comprueba rutas relativas desde la raíz del repositorio y desde la carpeta del proyecto. Cada evidencia conserva su archivo y posición de origen.
- Se añade `politica_horaria` de solo lectura: fecha de corte, ventanas regulares, ventanas de prueba y slot fijo. Cada ocupación expone `coincidencia_horaria`, `estado_frescura_horaria` y `fecha_politica_horaria`; una política anterior a la fecha objetivo queda identificada y no se presenta como confirmación vigente.
- `tests/test_registro_editorial.py`: tres pruebas nuevas cubren snapshots diarios/slots vacíos/atrasados, clasificación de ventanas y política con corte anterior.

**Commits:** código final `0306cf7e46b0af826ebbdb6a4d7d50bd1ccffe57`; pruebas `e7e2fa36c57a8d799045aaf6f6d96a733e31f19`. La rama feature se comparó contra el commit final y devolvió `identical`. Lectura de vuelta: script blob `c95a5fbbd0e8366877fc4e64d2f96fe096fff668`; tests blob `b5908f4efb2713b4fd36ed97c8dd468c2e6f20b5`.

### Verificación y límites

- **Smoke aislado ejecutado:** cuatro clasificaciones de política (slot fijo, regular, prueba y fuera de ventana) dieron el resultado esperado. Una muestra de snapshot produjo dos ocupaciones con fecha/hora local correcta, omitió el slot sin ID y reconoció el ID de video. Esto prueba la lógica aislada, no la suite del repositorio.
- **Pytest/CI:** no ejecutados. La consulta de runs asociados y estados de commit devolvió listas vacías para ambos commits; no se declara PASS de la suite.
- **Política desfasada en feature:** `data/horarios.json` de esta rama tiene corte 2026-11-09; `main/data/horarios.json` consultado en solo lectura tiene corte 2026-11-16 y una política distinta. El nuevo campo `CORTE_ANTERIOR_A_FECHA_OBJETIVO` hace visible la limitación; el script no importa ni copia datos de main. No se modificó ningún `data/*.json`.
- El snapshot diario 2026-11-11 fue localizado y leído; los intentos de leer `data/horario_2026-11-16.json` y `data/horario_2026-11-20.json` devolvieron 404. No se inventaron snapshots posteriores.

No se modificaron `main`, workflow, cola, estados Grok, secretos ni permisos. No se promovió ni despachó ningún storyboard.

## 17. Relectura de inventario y backlog — 2026-11-21, 12:30 CDMX

Se releyeron los 12 storyboards del lote 5–7 nov, los seis borradores interdiarios 18–20 nov, los cinco storyboards 21–22 nov ya inventariados y el borrador Bao incorporado después del último corte: **24 storyboards**.

- Los 12 del lote 5–7 nov conservan 2 QA PASS y 10 FAIL; no se recalculó ni se reescribió QA. Los seis interdiarios conservan 5 PASS y 1 FAIL. Los cinco iniciales 21–22 conservan 2 PASS y 3 FAIL. Bao no tiene narrative_qa.
- Los 24 archivos individuales `cola/estado/<project_id>.json` consultados devolvieron 404. Se conserva la clasificación `RECEPCION_GROK_NO_CONFIRMADA`; no se crearon estados.
- Se releyeron las 12 rutas originales de `cola/bloqueados/` y las nueve copias planas paralelas. Las copias leídas carecen de narrative_qa; no se promovieron, movieron ni eliminaron.
- `data/horario_semana_2026-11-01_07.json` contiene los 12 IDs antiguos. La lectura de `main/data/publicaciones.json` confirma dos procesamientos preexistentes: hielo caliente, publicado/programado el 2026-11-11 a las 13:30 con video_id `HSgrnejAcaI`; nubes pesan, registro del 2026-11-12 a las 07:00 con video_id `4Qpl17Ts_vI`. Ambos quedan `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`.
- En hielo caliente, `salidas/<id>/storyboard.json` referencia `capsula.mp4` y nueve frames; el MP4 y los frames no se pudieron verificar en el árbol. En nubes pesan, los archivos consultados bajo `salidas/<id>/` devolvieron 404 pese al registro de publicación en main. Ambos conservan `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO` donde corresponde; no se duplicó ni canceló publicación.
- La búsqueda de `historial_youtube` no encontró un archivo independiente en el repositorio; `data/publicaciones.json` sigue siendo la fuente disponible para reconciliar IDs y publicaciones. No se inventó un historial.
- No se encontró una ocupación en main para el slot 2026-11-22 13:30. La política main consultada incluye 13:00–14:30 como ventana regular; esto no equivale a una reserva ni a recepción de Grok.

## 18. Bao — auditoría estructural, fuentes y compatibilidad de carta celeste

Proyecto releído: `2026-11-22_bao-estrella-fusion-andromeda`.

- 8 escenas, 78 segundos de escenas + 6 segundos de cortinilla = 84 segundos; 192 palabras. Voz `es-MX-JorgeNeural`, rate +7%, pitch -2Hz; prompt_base coincide con `art_deco_poster`. Cada escena tiene ambiente y SFX. `approved_assets=[]`, `export.render_status=NOT_GENERATED`, sin archivo de render y `publicacion.status=PENDIENTE_DECISION_GROK`.
- La capa de mapa contiene coordenadas ecuatoriales reales: RA 00:38:48.60 / 9.7025° y Dec +40:46:08.23 / +40.7689528°, con SRC-003. NASA publica esos valores y sitúa AT 2025abao en Andrómeda, a unos 2.5 millones de años luz: https://science.nasa.gov/asset/webb/at-2025abao-in-the-andromeda-galaxy/ (ficha consultada, campos de posición y distancia).
- El renderer previo `scripts/capas_datos.py` trataba toda capa `mapa` como lon/lat terrestres y accedía a `puntos[].lon/lat`; la capa Bao usa correctamente `ra_deg/dec_deg`. Se añadió una rama de carta celeste que valida rangos RA/Dec, deriva una ventana de visualización y dibuja RA creciente hacia la izquierda. No carga Natural Earth ni convierte coordenadas celestes en terrestres.
- Se creó `tests/test_capas_datos.py` con cinco pruebas de bounds, región explícita, mapa terrestre, mezcla inválida y coordenadas fuera de rango. **Smoke aislado ejecutado:** las cinco condiciones se comprobaron con el helper y pasaron. No se ejecutó pytest ni CI y no se llamó `render_capa`; no se generaron imágenes, frames, audio ni video.
- Corrección de trazabilidad sin cambiar narración: la afirmación de 47 días después del pico quedó vinculada a SRC-001 (Nature, DOI 10.1038/s41586-026-11221-z); SRC-002 (NASA) conserva el soporte de la observación del 24 de diciembre de 2025. El DOI figura `VERIFICADO_RESOLVEDOR` en el storyboard; Nature/PubMed confirman el registro bibliográfico y NASA confirma las coordenadas. La API REST de Crossref no fue accesible desde esta ejecución; no se afirma una consulta API exitosa.
- El slot 22-nov 13:30 no aparece ocupado en main. Aun así, Bao sigue `BORRADOR_EN_PROYECTOS_NO_APTO_PARA_PROMOCION` y **NOT_DISPATCHABLE**: falta una revisión narrativa independiente PASS y el estado Grok individual devuelve 404. No se creó narrative_qa, cola ni estado; tampoco se marcó preparado. `fuentes.md` y `ESTADO_EJECUCION.md` no existen en esa carpeta; las fuentes están incorporadas en el storyboard.
- Commits de esta corrección: renderer RA/Dec `fcab046d00056f7b8c7dbf10c879aa20e9565651`; pruebas `d36c1305b11f4be7d6be23f01025ed5e3bf98533`; atribución SRC-001/SRC-002 `1c01ec1162ad3186ada73c4485f9cde681ccb5b6` (blob storyboard `e125839a63564f45745c66589d0e673fe024f9be).

Los cambios de código y metadatos permanecen en feature. No se modificaron `data/*.json`, main, workflows, secretos, permisos, publicaciones ni medios.


## 19. Relectura de inventario, QA y trazabilidad — 2026-11-21, 14:24 CDMX

Se releyó el directorio `proyectos/` en la rama feature (101 carpetas). Para el control temporal y el backlog interdiario quedan **25 storyboards**: 12 del lote 5–7 nov, seis del 18–20 nov, seis con fecha objetivo 21–22 nov y uno del 23 nov. Los `data/*.json` se consultaron en solo lectura.

### QA narrativo vigente

- Lote 5–7 nov: 2 PASS / 10 FAIL.
- Backlog 18–20 nov: 5 PASS / 1 FAIL.
- Fecha objetivo 21–22 nov: 2 PASS / 4 FAIL:
  - Fentale (23:30): PASS 90.
  - Homo erectus (07:00): FAIL 83, `GIRO_CIENTIFICO_NOMBRADO_PERO_NO_EXPLICADO`.
  - Pulsar (17:00): FAIL 83, `GIRO_CIENTIFICO_NOMBRADO_PERO_NO_EXPLICADO`.
  - Voyager (07:00): FAIL 83, `FECHA_DE_HITO_Y_CONFIRMACION_CONFUNDIDAS`.
  - Yubarta (17:00): PASS 90.
  - Bao (13:30): FAIL 84, `STAKES_NO_EXPLICADOS`; el registro ya existía al releerlo a las 14:24. No se repitió ni se alteró esa evaluación.
- Fecha objetivo 23 nov, `2026-11-23_tropical-biodiversity-turnover`: lectura independiente posterior, ocultando título, resumen, arco, notas y narrative_contract y leyendo solo las ocho narraciones concatenadas. Resultado registrado: **FAIL 82**, siete checks true y `critical_flags=["STAKES_NO_EXPLICADOS"]`. La narración explica la paradoja y el cambio de recambio a anidamiento, pero no explica por qué la pérdida de multidiversidad importa para el funcionamiento del ecosistema o las decisiones de conservación. No se reescribió el texto.

Recuento de la cohorte inventariada: **9 PASS / 16 FAIL**. Ningún FAIL se promovió. No se repitió PASS válido.

### Fuentes y metadatos corregidos

- Bao: Nature y PubMed confirman el DOI `10.1038/s41586-026-11221-z` y publicación el 18-nov-2026. Se corrigió `doi_verification_status` de la afirmación falsa `VERIFICADO_CROSSREF_API` a `PENDIENTE_RESOLVEDOR`. Crossref REST y doi.org no fueron accesibles en esta ejecución; no se ejecutó `--check-doi`. Commit `eef7e8568c8484e5ff581dc0755c011362fdc852`.
- Biodiversidad tropical (23 nov): Nature y PubMed confirman el DOI `10.1038/s41586-026-11298-6` y publicación el 18-nov-2026; Crossref REST y doi.org quedaron inaccesibles, por lo que el DOI se marca `PENDIENTE_RESOLVEDOR`.
- Fuente cartográfica de biodiversidad: el DOI `10.1098/rstb.2015.0275` aparece en registros bibliográficos secundarios, pero doi.org devolvió 403 y el suplemento oficial de Royal Society no fue accesible. Las coordenadas se encontraron en una tesis que cita Drescher et al. (2016), no en el suplemento primario. SRC-002 queda `PENDING_SOURCE`; no se considera verificada la coordenada contra ESM Table S1. Commit de storyboard y QA `b08951134e1c6071ad77144dfcc4c2ff466024f4`.
- No se cambió ninguna narración, cifra, fecha objetivo ni decisión editorial.

### Estructura, cola y dispatch

- Biodiversidad (23 nov): 8 escenas, 172 palabras, 78 s de escenas + 6 s de cortinilla = 84 s; voz y prompt_base coinciden con el catálogo; hay mapa y capa de dato/gráfico; cada escena tiene ambiente, SFX y source_ids; `approved_assets=[]`, `export.render_status=NOT_GENERATED`, sin `asset_filename`, `asset_type` ni rutas de medios. La compuerta narrativa y SRC-002 impiden promoción.
- Bao: 8 escenas, 192 palabras, 84 s; coordenadas ecuatoriales RA/Dec, renderer celeste ya corregido. QA FAIL y DOI pendiente impiden promoción.
- Inventario de `cola/entrada/`: `.gitkeep` y dos directorios históricos (9 y 11 nov); no hay JSON plano nuevo. `cola/estado/` devuelve 404; `handoffs/grok_inbox/` contiene solo el marcador histórico del 9-nov; `salidas/` no muestra procesamiento de los proyectos 21–23 nov.
- El workflow escucha únicamente `cola/entrada/*.json` plano en push, o `workflow_dispatch`; no se disparó ninguno. Los nuevos storyboards en `proyectos/` no son dispatchables por esa ruta. No se creó cola ni estado Grok.
- En main, `data/publicaciones.json` contiene dos ocupaciones del 21-nov: oxoboranos a las 13:30 CDMX (`K4qNkx2f4RI`) y robot orbital a las 19:00 (`ZG4iQgmWrLI`, 22-nov 01:00Z). Además, `docs/briefs/2026-11-21_PRODUCCION_SEMANA_23-28nov.md` lista Gutenberg el 22-nov a las 13:30 y nudillos el 23-nov a las 07:00. Por ello Bao (22-nov 13:30) queda marcado `CONFLICTO_DE_SLOT_ENTRE_RAMAS`; biodiversidad (23-nov 13:30) no coincide con los slots exactos de esa programación. `main/data/horarios.json` tiene ventana regular 13:00–14:30 y corte 16-nov; `feature/data/horarios.json` conserva corte 9-nov. Persiste la discrepancia de política horaria entre ramas; no se modificó ningún `data/*.json`.
- `cola/estado/` devuelve 404 tanto en feature como en main; para los storyboards de Bao y biodiversidad (y los demás proyectos sin archivo individual) el estado es `RECEPCION_GROK_NO_CONFIRMADA`. La presencia de `GROK_WEBHOOK_URL` y `GROK_WEBHOOK_TOKEN` no pudo verificarse mediante la conexión GitHub disponible; no se declaran ausentes ni se exponen valores.

No se dispararon workflows, no se enviaron payloads, no se generaron medios ni se modificaron publicaciones, permisos o secretos.


## 20. Entradas anidadas históricas y estado de pruebas — 2026-11-21

- `cola/entrada/2026-11-09_dato-robot-ensambla-orbita/` contiene storyboard, fuentes, instrucciones y estado histórico. Su `ESTADO_EJECUCION.md` ya declara `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`; main conserva YouTube `ZG4iQgmWrLI` programado 21-nov 19:00 CDMX. La carpeta `frames/` de feature contiene solo `.gitkeep`; el estado documenta medios no verificados. Se conserva sin mover ni redispatchar.
- `cola/entrada/2026-11-11_dato-ratas-topo-damaraland/` contiene únicamente `frames/` con ocho PNG y `.gitkeep`; no tiene `storyboard.json`, `ESTADO_EJECUCION.md` ni estado Grok. Es un directorio heredado incompleto, no una entrada canónica plana y no dispatchable. Se conserva intacto; no se infiere recepción ni procesamiento.
- `cola/bloqueados/README.md` confirma que el reingreso exige narrative_contract completo, revisión independiente en frío, PASS >=85 con siete checks y flags vacías, además del validador estructural. No se reingresó ningún paquete.
- La suite `tests/test_registro_editorial.py` tiene 20 funciones `test_*` después del commit `e7e2fa36c57a8d799045aaf6f6d96a733e31f19e` (mensaje: snapshots diarios y clasificación de horarios). El archivo se releyó y el SHA actual es `b5908f4efb2713b4fd36ed97c8dd468c2e6f20b5`.
- HEAD de feature observado al iniciar el cierre de esta relectura: `0360ec603b6310f12ff93a29af2c2c7e27cbd60e`. Después se añadieron correcciones de bitácora y verificación de estado Grok; los commits exactos quedan en el historial de esta rama. Las actualizaciones posteriores incluyen Bao DOI `eef7e8568c8484e5ff581dc0755c011362fdc852`, QA/fuentes de biodiversidad `b08951134e1c6071ad77144dfcc4c2ff466024f4`, control de inventario `0829490ae99b88ca45b74cf390991366af4565b7`, entradas anidadas `e888979ac306b00674c84d2689dc4122e62955dd` y estado Grok `0360ec603b6310f12ff93a29af2c2c7e27cbd60e`. Para ese commit, la consulta de workflow runs y combined status devolvió listas vacías; **pytest y CI no se ejecutaron**. No declarar suite aprobada.

- La corrección del radar que cambia el lead 22-nov 13:30 a `NO_DUPLICAR / SLOT_OCUPADO_EN_MAIN` quedó registrada en `docs/briefs/2026-11-21_RADAR_CAPCOT.md`, commit `8234731a7bde5224bad14f24f9f775c7adf8f6b5`; el risk note de Bao con `CONFLICTO_DE_SLOT_ENTRE_RAMAS` se verificó en commit `879680c597655b4de09bb578aa4147bfcb448795`.

- El plan semanal de main referencia MP4 y portadas bajo `/workspace/capcot_prod_20261121/...`, fuera del árbol GitHub accesible en esta ejecución. Para esos medios programados se registra `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`; no se intentó descargarlos, regenerarlos ni redispatcharlos. Los storyboards Bao y biodiversidad siguen sin rutas ni assets aprobados.
