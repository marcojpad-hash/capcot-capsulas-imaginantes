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

- HEAD de `feature/capcot-video-discovery-continuity` sigue en `49db1df246b241e431683f7eb501911dcae72ec9`; no hubo commits posteriores a la adenda 13. Se releyó el inventario de `proyectos/`: los cinco storyboards 21–22 nov conservan los mismos blobs, estructura y QA; no se repitió lectura narrativa PASS.
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
