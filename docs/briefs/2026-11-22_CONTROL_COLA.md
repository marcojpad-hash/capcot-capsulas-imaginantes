# Control de cola y auditoría CAPCOT — 2026-11-22

**Corte:** 2026-11-22 01:58 CDMX  
**Rama:** `feature/capcot-video-discovery-continuity` · HEAD observado `8e3df802`  
**Main:** HEAD observado `22cc55e0`

## Resultado

- **0 proyectos promovibles; 0 dispatches; 0 medios generados.**
- No se modificaron `data/*.json`, main, estados Grok, secretos, permisos ni programación.
- No se disparó Actions ni se envió payload a Grok.
- Se relevaron 7 proyectos recientes, los 12 IDs del lote 5–7 nov, cola en ambas profundidades, bloqueados, salidas, main, inventario de publicación, workflow y Actions.

## Proyectos recientes: 21–23 nov

| Proyecto | Slot | QA existente | Defecto estructural / decisión |
|---|---|---:|---|
| `2026-11-21_fentale-metano-sin-erupcion` | 21 nov 23:30 | PASS 90 | `prompt_base` y `scenes[1].capa.tipo=mapa` presentes; main ya contiene `Eldk0fVWqpo`: `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR` |
| `2026-11-21_homo-erectus-selva-tropical` | 21 nov 07:00 | FAIL 83 | `prompt_base` y mapa en `scenes[2].capa` presentes; `GIRO_CIENTIFICO_NOMBRADO_PERO_NO_EXPLICADO`; slot pasado |
| `2026-11-21_pulsar-gamma-reticulo` | 21 nov 17:00 | FAIL 83 | `prompt_base` y mapa celeste ICRS en `scenes[2].capa` presentes; `GIRO_CIENTIFICO_NOMBRADO_PERO_NO_EXPLICADO`; 17:00 sigue en prueba |
| `2026-11-22_voyager-1-un-dia-luz` | 22 nov 07:00 | FAIL 83 | `prompt_base` y mapa DSN con tres puntos WGS84 en `scenes[2].capa` presentes; `FECHA_DE_HITO_Y_CONFIRMACION_CONFUNDIDAS`; main ocupa Salem |
| `2026-11-22_bao-estrella-fusion-andromeda` | 22 nov 13:30 | FAIL 84 | `prompt_base` y mapa celeste RA/Dec en `scenes[1].capa` presentes; `STAKES_NO_EXPLICADOS`; main ocupa Gutenberg |
| `2026-11-22_yubarta-genoma-soplo` | 22 nov 17:00 | PASS 90 | `prompt_base` y mapa regional con bounding box en `scenes[2].capa` presentes; main ocupa Ada y 17:00 sigue en prueba |
| `2026-11-23_tropical-biodiversity-turnover` | 23 nov 13:30 | FAIL 82 | `prompt_base` y mapa regional con un punto respaldado por fuente primaria en `scenes[1].capa`; `STAKES_NO_EXPLICADOS`; main ocupa Rosetta |

Los siete tienen 8 escenas y 171–208 palabras. Los seis campos narrativos por escena están presentes. No se repitió QA ni se reescribieron narraciones. **Corrección de auditoría tras lectura directa de los siete JSON:** los siete contienen `visual_identity.prompt_base` y una capa estructurada `scenes[n].capa.tipo=mapa`; por tanto, se retira el hallazgo previo de ausencia de `prompt_base` y mapa. Localización de capa: Fentale `scene_002`, Homo erectus `scene_003`, púlsar `scene_003`, Voyager `scene_003`, AT 2025abao `scene_002`, yubarta `scene_003`, biodiversidad `scene_002`. Los bloqueos reales son los consignados en cada fila: QA FAIL en Homo, púlsar, Voyager, Bao y biodiversidad; producción previa en Fentale; conflicto de slot en Voyager, Bao, Yubarta y biodiversidad; `SRC-002=PENDING_SOURCE` en biodiversidad. No se repitió QA ni se reescribió narración.

## Lote 5–7 nov: 12 IDs canónicos

`2026-11-05_comida-palomitas`, `2026-11-05_inter-arboles-se-comunican`, `2026-11-05_inter-rayo-globular`, `2026-11-05_kids-dia-en-venus`, `2026-11-06_comida-aguacate-negro`, `2026-11-06_inter-arena-cantante`, `2026-11-06_inter-ranas-congeladas`, `2026-11-06_kids-ballena-azul-corazon`, `2026-11-07_comida-hielo-caliente`, `2026-11-07_inter-nubes-pesan`, `2026-11-07_inter-pulpo-suenos`, `2026-11-07_kids-huesos-bebe`.

- QA existente: **2 PASS** (Venus 88, arena 94), **10 FAIL**.
- Estructura: 85 escenas; **510 campos narrativos estructurales ausentes** (seis por escena).
- Nueve coincidencias de video/publicación preexistente en main; no redispatchar:
  - palomitas `zTP5akrGA9M`
  - árboles `EX0W3q-yKRw`
  - Venus `phVfyHp3CnY`
  - arena `m4RqQRaz55k`
  - ranas `UBFuKBU3cx0`
  - corazón de ballena azul `wbFrlM2e_YE`
  - hielo caliente `HSgrnejAcaI`
  - peso de nubes `4Qpl17Ts_vI`
  - huesos de bebé `uEsoscBrfgU`
- Rayo globular, aguacate negro y sueños del pulpo no tienen coincidencia inequívoca de publicación. Siguen sin ser promovibles por QA/estructura.
- Las salidas de árboles e hielo contienen metadatos/publicación, pero no `capsula.mp4` en el árbol Git. Para los nueve casos con video ID: `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`; donde el MP4 no aparece: `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`.
- Las copias heredadas de nombres anteriores ya están en `cola/bloqueados/`. Los 12 IDs canónicos siguen en `proyectos/`; no hay copia de esos IDs en cola activa. No se movió ni borró nada.

## Cola, Grok y medios

- En feature, `cola/entrada/` contiene solo `.gitkeep` y `2026-11-09_dato-robot-ensambla-orbita/` anidado; no hay JSON plano.
- `cola/estado/<id>.json` devolvió 404 para los 7 proyectos recientes, los 12 IDs y el robot: **20 comprobaciones**, todas `RECEPCION_GROK_NO_CONFIRMADA`.
- El marcador en `handoffs/grok_inbox/` no es un estado Grok ni prueba de recepción.
- El robot tiene `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR` en `ESTADO_EJECUCION.md`; main registra `ZG4iQgmWrLI`. Sus medios aparecen en la carpeta de cola, pero no hay salida local equivalente. No redispatchar.
- Main contiene entradas anidadas de árboles e hielo con procesamiento previo; sus `cola/estado` también devolvieron 404. No se modificaron.
- El workflow `.github/workflows/capcot-grok-dispatch.yml` selecciona JSON planos de primer nivel (`find -maxdepth 1`); `scripts/procesar_cola.py` admite carpetas anidadas. No hay ejecución reciente de dispatch en las Actions consultadas.
- No se comprobó la existencia de secretos del webhook; no se leyeron ni modificaron valores.

## Main, horarios e historial

- Ventanas autorizadas: 06:30–07:30 y 13:00–14:30. 16:30–18:00 continúa en prueba; 19:00 fue retirado; 23:30 es el slot fijo de dato del día.
- Main ocupa 07:00/13:30 del 22–29 nov en el snapshot disponible. El 22 nov aparecen Salem (07:00), Gutenberg (13:30), Ada (17:00) y Webb (19:00); el 23 nov, Nudillos (07:00), Rosetta (13:30), Pirámides (17:00) y Gutenberg (19:00).
- 22 nov 23:30 no aparece ocupado, pero el APOD de Juno del día duplica la línea Juno ya publicada el 29 oct; no se seleccionó.
- No se infiere disponibilidad para 1 dic: main no contiene un plan que confirme ese horizonte.
- `data/miniaturas_auditoria_2026-11-21.json`: 36 elementos sin MP4 local y 6 colisiones de `publishAt`.
- `data/publicaciones.json` tiene solo dos registros; no es inventario completo. No existe `historial_youtube` en `data/`; `vistas_historico.json` tiene 107 entradas y no incluye el ID del robot. No se afirmó que videos antiguos sigan programados.
- `data/temas_del_dia.json` está vacío; `data/rotacion.json` y `data/estilos_usados.json` no reflejan rotación reciente (últimos registros visibles: 31 oct y 28 oct). Se dejaron intactos.

## RSS y radar científico

Las ocho fuentes de `scripts/tendencias.py` y Google Trends México se consultaron por HTTP directo. Los nueve endpoints devolvieron el error literal:

`URLError: <urlopen error [Errno -3] Temporary failure in name resolution>`

El script no se ejecutó dentro del repositorio; el error corresponde a las consultas HTTP de esta sesión. Se usaron fuentes oficiales como respaldo.

| Candidato | Fuente / fecha | Hecho respaldado | Estado |
|---|---|---|---|
| Nubes crepusculares de Curiosity | NASA Photojournal, 20 nov 2026 | Imagen tomada 31 oct 2026, sol 5061; aparecen por poco tiempo cada otoño sobre Gale Crater. Coordenada de referencia del aterrizaje: 4.6°S, 137.4°E; no es la posición exacta de la nube. | Candidato para slot regular futuro |
| Floración del desierto de Atacama | NASA Earth Observatory, 19 nov 2026 | Landsat 8/9, imágenes del 14 sep y 24 oct; NASA compara el episodio con 13 floraciones de 1981–2015 y lo describe como posiblemente el más extenso de la era satelital. | Candidato; no apto para dato del día 22 nov |
| Agua antigua más allá de Neptuno | NASA Science, 18 nov; Science Advances, 11 nov | 12 partículas de polvo estratosférico; el origen en el cinturón de Kuiper se infiere por huellas de partículas energéticas, no por muestreo directo. DOI visible: `10.1126/sciadv.aeg1602`. | PENDING_CROSSREF |
| Dos especies de tardígrados marinos | Senckenberg / ZooKeys, 20 nov | Dos especies descritas en el monte submarino Senghor. DOI: `10.3897/zookeys.1295.205902`. | NO_DUPLICAR: ya existe cápsula de tardígrados en salidas del 24 oct |
| Colores de Júpiter en APOD | NASA APOD, 22 nov | Publicación del día sobre una imagen Juno del paso 14 de 2018. | NO_DUPLICAR: ya existe proyecto/salida Juno del 29 oct |

Crossref API y resolvedor no pudieron consultarse. Error de red: `Temporary failure in name resolution`. Los DOI visibles en páginas editoriales no se declararon verificados por Crossref.

**Decisión:** no se creó storyboard. El slot 22 nov 23:30 carece de candidato del día que supere actualidad y no duplicación; los slots regulares 22–29 nov están ocupados; 1 dic no está confirmado por main. No se generaron medios, placeholders ni QA narrativo.

## CI y cierre

- PR #3 sigue OPEN y `mergeable_state=dirty`; no se fusionó.
- CodeQL del PR: run `44999261966`, éxito.
- Semgrep en main: run `44988989131`, 32 findings bloqueantes; la carga SARIF se omitió al fallar el análisis.
- `semgrep.yml` en feature usa `if: always()` y conserva el artifact 7 días; todavía no hay ejecución de Semgrep en feature que pruebe esa corrección.
- No se disparó Actions.

**EJECUTADO:** lectura y auditoría de 19 storyboards, 20 estados Grok, cola, bloqueados, salidas, main, inventario, workflow, Actions y fuentes oficiales.  
**VERIFICADO:** 0 proyectos promovibles; nueve publicaciones/videos preexistentes en el lote; ausencia de MP4 Git en las dos salidas inspeccionadas; 20 estados Grok no confirmados; PR #3 abierto/dirty.  
**PENDIENTE:** revisión narrativa independiente para borradores nuevos; corrección estructural por sus autores; vínculo inequívoco del video `4Qpl17Ts_vI`; acceso a RSS/Crossref; agenda confirmada a partir del 1 dic.

No se reescribieron narraciones, no se alteraron estados Grok, no se promovió ni redispatchó ningún paquete.


**Actualización de fuente y cartografía (22-nov):** se retiraron las coordenadas PT REKI y L. Kepayang que dependían de una tesis secundaria y de un suplemento editorial no accesible. `SRC-002` ahora es Kurniawan et al. (2018), *Biogeosciences*, DOI `10.5194/bg-15-5131-2018`; la página editorial, sección 2.1, publica la coordenada regional de Jambi (2°00′57″ S, 103°15′33″ E) y confirma dos paisajes dentro de esa región. El mapa se redujo a un único localizador regional, sin fingir coordenadas de parcelas, estaciones ni centroide. Storyboard commit `3a0bbcc66f6fba5c52636a6fd0305fd079d24f68`, blob `3ced77b8dc314bcbb8ed594a7fb6f573415f8127`. QA narrativo sigue FAIL/82 por `STAKES_NO_EXPLICADOS`; no se modificó la narración ni se promovió el proyecto.

**Preflight estático posterior al cambio (22-nov):** JSON releído y parseado. Campos raíz obligatorios: 21/21 presentes; campos narrativos y estructurales requeridos: completos en las ocho escenas; estilo del catálogo y prompt_base literal: coinciden; prefijo prompt_base en los ocho image_prompt: coincide; voz: coincide; 8 escenas; 172 palabras narradas; 78 s de escenas + 6 s de cortinilla = 84 s; una capa mapa con coordenadas dentro de rango y fuente; dos capas de dato/gráfico con fuente; source_ids resuelven a fuentes presentes. Este fue un preflight estático por lectura del JSON, **no** una ejecución de scripts/validar_storyboard.py. La compuerta narrativa oficial permanece FAIL/82 por STAKES_NO_EXPLICADOS; por eso no es apto para promoción aunque el preflight estructural revisado no muestra faltantes.


## Addendum de auditoría de PR y Actions — 2026-11-22, 04:00 CDMX

### Pull requests abiertos revisados

- **PR #3**, base `main`, head `feature/capcot-video-discovery-continuity`: sigue OPEN/DRAFT, `mergeable=false`, `mergeable_state=dirty`; head `d30814995de642e3b6100d19d968115264a3d690`. El diff agrega workflows de descubrimiento, dispatch, Semgrep, TTS y validación Kuroshio, además de documentación y helpers. No aparece modificación de storyboards ni de `data/*.json` en los archivos revisados. CodeQL del PR terminó SUCCESS en run `45003635410`.
- **PR #15**, base `feature/capcot-video-discovery-continuity`: sigue OPEN. Su diff se limita a `scripts/validar_storyboard.py` y `tests/test_validar_storyboard_textual.py`. Añade rechazo explícito de booleanos como coordenadas terrestres/celestes y bounds; fija el host HTTPS de Crossref y codifica el DOI antes de solicitarlo. No modifica storyboards ni datos. Semgrep run `45004335607`, commit `30101e9aca8aaafb8d1894df30574a66067ff4a8`, terminó FAILURE: 26 hallazgos bloqueantes en 1,097 archivos con 360 reglas. La carga SARIF terminó SUCCESS y dejó artifact `14746933868`. No se ejecutó aquí el validador ni la suite de pruebas de ese PR; no se declara apto para integrar.
- **PR #14**, base `main`: sigue OPEN. Conserva `narrative_qa=FAIL/82`, añade `asset_filename` a ocho escenas y no ejecutó `validar_storyboard.py --check-doi`. Contradice el contrato vigente de preproducción; no promover ni integrar.
- **PR #13**, base `main`: agrega solo `proyectos/2026-11-15_dato-quasar-pareja-cosmic-dawn/AUDITORIA.md`. El informe conserva nueve puntos pendientes y el storyboard sigue FAIL; no se atribuye una revisión nueva ni se integra.
- **PR #6**, base `feature/capcot-video-discovery-continuity`: agrega `.github/workflows/supervisor.yml` y `guardia.config.json`. El workflow se activa en cada push y pull request, invoca un reusable workflow de `agente-cero-costo` y usa `secrets: inherit`. Ese repositorio es adicional y permanece solo lectura; no se auditó el contenido del reusable workflow. Riesgo de alcance de secretos pendiente de revisión antes de integrar.
- **PR #4**, base `feature/capcot-video-discovery-continuity`: modifica el estado documental del robot del 9-nov y ubica los nueve frames en una conversación de Grok. La carpeta `frames/` sigue sin PNG/JPEG en GitHub; no se declara medio verificado. El slot ya pasó y existe procesamiento previo: no redispatchar.
- **PR #7–#9**, base `main`: cambios Dependabot limitados a versiones de acciones en workflows; siguen OPEN y no se integran desde esta operación.

### Dispatch y ejecuciones observadas

- `.github/workflows/capcot-grok-dispatch.yml` en feature selecciona únicamente JSON planos de `cola/entrada/`: el trigger usa `cola/entrada/*.json` y la selección manual usa `find cola/entrada -maxdepth 1`. No cubre paquetes anidados. `scripts/registro_editorial.py` sí recorre `storyboard.json` a profundidad recursiva. Se conserva la discrepancia; no se modificó el workflow.
- El workflow crea un marker `pending` en `handoffs/grok_inbox/` y hace push a la rama. Ese marker no acredita recepción: solo `cola/estado/<project_id>.json` confirma el acuse individual. No se crearon ni editaron estados Grok, ni se inspeccionaron valores de secretos.
- El trabajador programado de **main** corrió en run `45008611769`, commit `22cc55e0185f438fae2f7e5b85d70917185b02eb`. Job `trabajar` SUCCESS; log literal: `[trabajador] sin trabajo en cola.` Esto no acredita ejecución sobre feature ni recepción de Grok.
- No se disparó ningún workflow desde esta auditoría.

### Radar incremental y no duplicación

- NASA confirmó que Voyager 1 alcanzó una distancia de un día-luz el 18-nov; se excluye como candidato nuevo porque ya existe `2026-11-22_voyager-1-un-dia-luz` en proyectos.
- Kilonova Catcher es un proyecto de ciencia ciudadana lanzado en 2019, no un descubrimiento reciente; se descarta como candidato del día.
- Se añade como respaldo futuro el artículo primario de Nature Communications, publicado el 9-nov-2026: “Two functionally distinct amyloid-β intermediates link aggregation pathways to pathology in Alzheimer’s disease”, DOI visible `10.1038/s41467-026-79028-0`. El estudio identifica dos poblaciones de intermediarios en Aβ42 en sistemas recombinantes, modelo murino y tejido cerebral humano; solo una población se convierte en placas. La intervención farmacológica que redujo carga de placas y mejoró cognición se probó en ratones, no en personas. DOI/Crossref y resolvedor no quedaron confirmados en esta sesión: `PENDING_CROSSREF`. No hay storyboard ni asignación de slot.
- Shortlist vigente para slots futuros: Curiosity (NASA, 20-nov), floración de Atacama (NASA, 19-nov), agua antigua más allá de Neptuno (NASA/Science Advances, `PENDING_CROSSREF`) e intermediarios Aβ (Nature Communications, `PENDING_CROSSREF`). Tardígrados y Júpiter se mantienen como NO_DUPLICAR por proyectos/salidas existentes.
- No se creó storyboard adicional: los slots regulares consultados siguen ocupados y no hay autorización de slot nuevo.

### Cierre de este addendum

**EJECUTADO:** revisión de nueve PR abiertos, diff de PR #3/#4/#6/#13/#14/#15 y Dependabot #7–#9; lectura del workflow de dispatch, worker, logs de Actions y fuentes NASA/Nature.  
**VERIFICADO:** PR #3 sigue draft/dirty; PR #15 tiene 26 hallazgos Semgrep y SARIF cargado; worker de main no encontró trabajo; el workflow de dispatch no selecciona carpetas anidadas; el robot conserva medios no verificados.  
**PENDIENTE:** resolución de los 26 hallazgos Semgrep; revisión del reusable workflow externo y del alcance de `secrets: inherit`; Crossref para los dos DOI; acuse Grok individual; correcciones de storyboards por sus autores.  
**SIN CAMBIOS:** no se modificaron storyboards, `data/*.json`, `cola/estado`, secretos, permisos, `main`, medios ni publicaciones. No hubo promoción ni redispatch.


## Verificación de feeds de tendencias — 2026-11-22, 04:00 CDMX

Se intentó abrir cada URL declarada en `scripts/tendencias.py` y Google Trends RSS México mediante el lector web disponible. El lector rechazó varios formatos XML/RSS; esto **no demuestra que los servidores RSS estén caídos**. Tampoco se ejecutó localmente `scripts/tendencias.py`, porque esta sesión no dispone de un runtime de repositorio con salida de red comprobada.

| Feed | Resultado literal del lector web |
|---|---|
| Google Trends México `https://trends.google.com/trending/rss?geo=MX` | `URL ... is not accessible via this tool.` |
| ScienceDaily ciencia | `(400) Unsupported content-type: application/xml` |
| ScienceDaily salud | `(400) Unsupported content-type: application/xml` |
| ScienceDaily espacio | `(400) Unsupported content-type: application/xml` |
| Phys.org | `(400) Unsupported content-type: text/xml` |
| NASA News Release | `(400) Unsupported content-type: application/rss+xml` |
| ESA Space Science | `(404) Not Found` |
| Nature RSS | `(400) Unsupported content-type: application/rss+xml` |
| EurekAlert | `URL ... is not accessible via this tool.` |
| SINC | `URL ... is not accessible via this tool.` |
| UNAM Global | `(400) Unsupported content-type: application/rss+xml` |

**Respaldo oficial consultado:** NASA Science para el hito de Voyager 1 y las nubes crepusculares de Curiosity; NASA Science/Earth Observatory para hielo más allá de Neptuno y floración de Atacama; artículo primario de *Nature Communications* para los intermediarios Aβ. Las fuentes y límites de cada afirmación están en el radar. Voyager se excluyó por duplicación; el candidato Aβ queda `PENDING_CROSSREF`.

**Estado:** RSS_XML_READER_LIMITATION; Google Trends sin lectura; ESA URL devuelve 404; ejecución real del script PENDIENTE. No se inventó que los feeds estuvieran caídos ni se generó storyboard a partir de una tendencia sin fuente primaria.


## Reconciliación de datos main/feature — 2026-11-22, 04:00 CDMX

Lectura de solo lectura de los inventarios JSON:

- `data/horarios.json`: feature está fechado 2026-11-09; main está fechado 2026-11-16 y contiene una política adicional. La rama feature no es fuente suficiente para el calendario actual.
- `data/publicaciones.json`: feature contiene 22 registros; main contiene 48. `data/rotacion.json`: feature contiene 27 registros; main contiene 39. `data/temas_del_dia.json` tiene el mismo blob SHA en ambas ramas (`38e14259090e643123c2004de5057626948e34ac`).
- Main conserva el registro de producción del robot orbital del 21-nov 19:00, YouTube `ZG4iQgmWrLI`, con programación de TikTok/Facebook. Se clasifica `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`; los medios referenciados no se localizaron en el árbol de GitHub.
- `data/resubidas_2026-11-21.json` registra dos resubidas ya programadas: oxoboranos el 22-nov 14:30 CDMX (YouTube `B-75KkHAVDo`) y Cleopatra el 22-nov 21:00 CDMX (YouTube `I8n_5nnUlbI`). Se mantienen intactas; no se creó ni alteró programación.
- El mismo archivo propone 23-nov 14:30 para enana blanca, pero la fila está `bloqueado_sin_mp4`, sin ID nuevo y sin binario. Es propuesta bloqueada, no slot confirmado ni autorización para que el investigador genere otro storyboard.
- `data/miniaturas_auditoria_2026-11-21.json` registra 6 colisiones de horario, 9 miniaturas corregidas, 36 pendientes por falta de MP4 y 4 con rework. Se conserva como trabajo preexistente; no se repitieron operaciones de Studio.
- Los archivos `data/*.json` permanecieron intactos. La diferencia de inventario y calendario entre ramas se conserva explícita; no se sincronizó main con feature ni viceversa.


## Corrección de trazabilidad de Actions — 2026-11-22, 04:10 CDMX

La frase anterior «No se disparó ningún workflow desde esta auditoría» se precisa: **no se ejecutó manualmente `workflow_dispatch`, no se invocó el webhook de Grok y no se despachó contenido**. Sin embargo, los commits documentales hechos en la rama feature activaron automáticamente los checks de CodeQL asociados a PR #3.

Ejecuciones automáticas posteriores a los commits del control/radar:
- Run `45010722941`, head `f27ecdacdc6c3cfb4ae5a108ae4926896ba7c4ec`: CodeQL Analyze (actions) y Analyze (python), ambos SUCCESS.
- Run `45010727491`, head `9f94983941ac2f2bfe54f8d6348709bea970e094`: ambos jobs SUCCESS.
- Run `45010901899`, head `840c40918d16ac4b252ac69dd4a2b77ebc2b24a5`: ambos jobs SUCCESS.
- Run `45010995845`, head `6e39551093c0a35b95a8344a5ee37ad90f361dd8`: ambos jobs SUCCESS; estado terminal consultado y verificado.

La última ejecución de CodeQL cubre el commit final de esta actualización. No se observó un nuevo dispatch de Grok ni una ejecución del trabajador sobre feature. El fallo Semgrep de PR #15 (`45004335607`, 26 findings) permanece independiente y sin resolución.


## Triage del artefacto Semgrep — 2026-11-22

Se descargó y parseó el SARIF del artifact `14746933868` del run `45004335607` (commit de PR #15 `30101e9aca8aaafb8d1894df30574a66067ff4a8`). El archivo contiene 27 resultados: **26 activos** y 1 suprimido en código fuente. Los 26 activos coinciden con el mensaje del job.

| Grupo | Activos | Ubicaciones |
|---|---:|---|
| Acciones GitHub con tag mutable | 11 | `capcot-descubrimiento.yml` (3), `capcot-grok-dispatch.yml` (1), `semgrep.yml` (3), `tts-tooling-smoke.yml` (2), `validar-kuroshio.yml` (2) |
| URL dinámica en urllib | 11 | `buscar_generadores_video.py:80`; `descargar_sfx.py:12,16`; `generar_frames.py:23`; `generar_guion_llm.py:32`; `media_api_clients.py:29`; `publicar.py:82,85`; `tendencias.py:14,48`; `tendencias_estilos.py:16` |
| subprocess con argumentos tainted | 2 | `capsula_diaria.py:110`; `procesar_cola.py:57` |
| Índice dinámico de globals | 1 | `publicar.py:43` |
| MD5 | 1 | `rotacion.py:22` |
| Suprimido en fuente | 1 adicional, no activo | `validar_storyboard.py:27`, `HTTPSConnection` |

**Clasificación estática inicial, no veredicto de seguridad:**
- Las 11 referencias mutables son hallazgos de integridad de cadena de suministro y requieren pinning a SHA completo verificado antes de integrar los workflows.
- Los dos `subprocess.run` reciben listas de argumentos y no pasan `shell=True`; el riesgo de shell injection parece un falso positivo, pero las rutas/argumentos siguen necesitando validación de raíz y límites.
- `publicar.py:43` usa la clave literal `"META"` en `globals().get`; el hallazgo de índice dinámico parece falso positivo.
- `rotacion.py:22` usa MD5 como semilla determinista de rotación, no como firma/integridad. Cambiarlo alteraría elecciones deterministas; no se cambia sin prueba de equivalencia.
- Las URL de `tendencias.py`, `tendencias_estilos.py`, `buscar_generadores_video.py` y `media_api_clients.py` se construyen sobre hosts HTTPS fijos y parámetros codificados. En cambio, `generar_frames.py` y `generar_guion_llm.py` aceptan base URL desde variables de entorno; deben exigir HTTPS y rechazar esquemas locales. `descargar_sfx.py` consume una URL de la respuesta de Wikimedia y `publicar.py` consume `upload_url` de TikTok; ambos requieren allowlist de host/protocolo antes de descargar/subir.
- El resultado suprimido de `HTTPSConnection` no cuenta entre los 26 activos.

No se parcheó automáticamente: los hallazgos mezclan warnings de baja confianza, rutas configurables y acciones de workflow; no es seguro aplicar una sustitución global. La corrección debe ser por origen de URL, pinning de SHA verificado y pruebas específicas, sin ejecutar workflows ni despachar contenido.
## Reconciliación de medios y programación — 22 nov 2026

**Corrección de la clasificación de medios:** la búsqueda anterior se limitó a `salidas/2026-11-09_dato-robot-ensambla-orbita`, que no existe. La lectura del árbol completo de `main` encontró los medios en `cola/entrada/2026-11-09_dato-robot-ensambla-orbita/`; por tanto, el antiguo `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO` queda **SUPERSEDIDO**. Estado actual: `MEDIOS_VERIFICADOS_EN_MAIN_COLA_ENTRADA; NO_PRESENTES_EN_FEATURE`.

Evidencia de árbol `main`:
- `capsula.mp4`: SHA `72d7ca5757a18b5d7a248503ac0e096dc0ac37ff`, 25,795,339 bytes.
- `portada.jpg`: SHA `c8cd5a72f88c95c95b97f2ed81ee254c783f4a86`, 213,315 bytes.
- Nueve frames `scene_001.jpg`–`scene_009.jpg` presentes.
- `programacion.json`: SHA `395eed4055388a8eaab6b89a3008061e4097118b`; `qa.json`: SHA `9dc15174cf92bd354edd4bc0b8309fddceeeaf52`; `metadata.json`: SHA `5a6b2a08752a499aa2d18774705e091adc0f919c`.
- QA audiovisual: 21/21 checks, 87.57 s. Esto no sustituye el `narrative_qa` PASS 90 del storyboard.

**Producción preexistente, no redispatchar:** `programacion.json` mantiene `estado=programado`, YouTube `ZG4iQgmWrLI`, `publish_at=2026-11-22T01:00:00Z` (21-nov 19:00 CDMX), TikTok y Facebook programados. `publishAt` ya quedó en el pasado, pero no se confirmó el estado público: el fetch de la URL de YouTube devolvió `DisabledError`; no existe archivo `historial_youtube` en el árbol y `vistas_historico.json` no contiene ese ID. `metadata.json` conserva `privacyStatus=private` mientras `programacion.json` dice `programado`; se registra como **PUBLICACIÓN_REAL_NO_VERIFICADA / RIESGO_DE_ESTADO_PROGRAMADO_ANTIGUO**. No cancelar, reprogramar ni redispatchar.

El paquete de `main` está anidado en `cola/entrada/<id>/`; el workflow actual selecciona solo JSON planos de primer nivel, así que su ruta es `NOT_DISPATCHABLE_POR_SELECTOR`. El paquete de `feature` también es anidado y solo contiene storyboard/`.gitkeep`. El archivo de estado de `main` permanece con texto del 10-nov que dice audio/video no generados y frames pendientes; esa ficha es **DESACTUALIZADA** frente a los medios, QA y programación actuales. `cola/estado/<id>.json` sigue 404: `RECEPCION_GROK_NO_CONFIRMADA`. No se infiere recepción por la carpeta ni por GitHub.

No es un segundo proyecto ni un slot nuevo: el mismo `project_id` conserva en storyboard el slot original 9-nov 23:30, mientras la programación de producción lo movió a 21-nov 19:00. La clasificación correcta sigue siendo `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`; no se declara conflicto entre proyectos distintos ni se altera `main`.


## Actions posteriores a la reconciliación — 22 nov 2026, 06:10 CDMX

- Los commits documentales `0c9d8f234893cdbac2d8050f1671b5667dd022b8` y `fefa616d43dc672906f8b3aaebbf8c30f3b45935` quedaron leídos de vuelta. CodeQL terminó SUCCESS en Python y Actions para ambos: runs `45020786264` y `45020789811`. No se hizo merge; PR #3 sigue OPEN/DRAFT/dirty.
- PR #15 sigue OPEN y Semgrep FAILURE en run `45004335607`; el SARIF conserva 26 hallazgos. No se alteró su rama ni se eludió el control.
- Worker de main `45008611769`: SUCCESS, log literal `[trabajador] sin trabajo en cola.` Callback `45016230714`: SUCCESS; la búsqueda de Issues no encontró títulos `[callback]` nuevos. No se disparó workflow manual ni webhook de Grok.
- El workflow referencia `GROK_WEBHOOK_URL` y `GROK_WEBHOOK_TOKEN`. La consulta de nombres de secretos no fue autorizada por el conector (HTTP 400: `GitHub Fetch URL is not an allowed public GitHub repository or search endpoint`); por tanto, su presencia no está verificada y no se declaran faltantes. No se consultaron valores.


## Reconciliación independiente de agenda y rutas — 22-nov-2026

### Corrección de ocupación por fecha + slot

La lectura directa de `main/data/horarios.json`, `data/publicaciones.json`, `data/miniaturas_auditoria_2026-11-21.json`, `data/resubidas_2026-11-21.json`, `data/vistas_historico.json`, `data/cierre_diario/2026-11-21.md` y `docs/briefs/produccion_2026-11-23_28/plan_semana.json` corrige la tabla anterior. No se modificó ninguno de esos archivos.

| Fecha / slot CDMX | Evidencia en main | Proyecto feature afectado | Clasificación |
|---|---|---|---|
| 21-nov 07:00 | Tejón, YouTube `6XCBYrlO4Eg`, aparece en vistas/histórico | `2026-11-21_homo-erectus-selva-tropical` | `CONFLICTO_DE_SLOT_ENTRE_RAMAS` |
| 21-nov 13:30 | Oxoboranos, `K4qNkx2f4RI`, en publicaciones | — | Slot ocupado |
| 21-nov 17:00 | Napoleón, `8okieDXFIgU`, en cierre/miniaturas | `2026-11-21_pulsar-gamma-reticulo` | `CONFLICTO_DE_SLOT_ENTRE_RAMAS` |
| 21-nov 19:00 | Robot orbital, `ZG4iQgmWrLI`, programado | — | Procesamiento preexistente; no redispatchar |
| 21-nov 23:30 | Colón, `RwTTwSNGm10`, programado | `2026-11-21_fentale-metano-sin-erupcion` | `CONFLICTO_DE_SLOT_ENTRE_RAMAS` |
| 22-nov 07:00 | Salem, `N21TIYdONZo`, programado | `2026-11-22_voyager-1-un-dia-luz` | `CONFLICTO_DE_SLOT_ENTRE_RAMAS` |
| 22-nov 13:30 | Gutenberg, `YXndoPSSeaY`, programado | `2026-11-22_bao-estrella-fusion-andromeda` | `CONFLICTO_DE_SLOT_ENTRE_RAMAS` |
| 22-nov 17:00 | Ada, `Sc0cX9ejxuw`, programado | `2026-11-22_yubarta-genoma-soplo` | `CONFLICTO_DE_SLOT_ENTRE_RAMAS` |
| 22-nov 19:00 | Webb, `BIwG7kgaLic`, programado | — | Preexistente fuera de la política vigente; no reutilizar |
| 23-nov 07:00 | Nudillos, `tmOji99zGPE`, comparte `publishAt=2026-11-23T13:00:00Z` con AI warning, `IQEU2Bqy3v0` | — | `COLISION_DE_PROGRAMACION` dentro de main |
| 23-nov 13:30 | Rosetta, `p5PM4xZfDyc`, programado | `2026-11-23_tropical-biodiversity-turnover` | `CONFLICTO_DE_SLOT_ENTRE_RAMAS` |
| 23-nov 17:00 | Pirámides, `gWJxoGjWQeM`, programado | — | Preexistente en ventana de tarde en prueba |
| 23-nov 19:00 | Gutenberg, `i3SpxSQglm4`, programado | — | Preexistente fuera de la política vigente; no reutilizar |

**Corrección de Fentale:** `Eldk0fVWqpo` corresponde al 20-nov 23:30; no es el mismo slot del 21-nov. Sí existe duplicación temática de metano entre ambos proyectos, y el slot 21-nov 23:30 ya está ocupado por Colón. Se corrige la causalidad del bloqueo: duplicación temática + conflicto de slot, no identidad de fecha/slot con `Eldk0fVWqpo`.

### Política vigente frente a programación heredada

`main/data/horarios.json` actualizado el 16-nov declara ventanas activas 06:30–07:30 y 13:00–14:30, tarde 16:30–18:00 en prueba, slot fijo 23:30 y ventana 19:00 retirada desde el 5-nov. Sin embargo, main conserva elementos preexistentes a las 17:00, 19:00 y 21:00. Se registran como programación heredada; no constituyen autorización para crear nuevos paquetes en esos horarios. No se cancela ni reprograme nada.

`data/resubidas_2026-11-21.json` registra además:
- Oxoboranos nuevo ID `B-75KkHAVDo`, 22-nov 14:30.
- Cleopatra nuevo ID `I8n_5nnUlbI`, 22-nov 21:00.
- `originales_intactos=true`: los IDs originales siguen presentes. Esto crea riesgo de duplicación de publicación, no una autorización para cancelar los nuevos ni retirar los originales.
- Enana blanca, 23-nov 14:30: `bloqueado_sin_mp4`, sin ID nuevo ni medio; es propuesta bloqueada, no programación confirmada.

El 22-nov 23:30 no aparece ocupado en los inventarios consultados. Sigue activo como slot fijo, pero permanece `PENDING_SOURCE`: el radar vigente no tiene candidato del mismo día que supere resolución DOI y cartografía. No se creó storyboard.

### Colisiones de programación posteriores

`data/miniaturas_auditoria_2026-11-21.json` contiene seis colisiones exactas de `publishAt`; no se alteraron:
- 23-nov 07:00: `IQEU2Bqy3v0` + `tmOji99zGPE`.
- 24-nov 17:00: `cGb7Z0ZEz8w` + `_YzBY4OfUeo`.
- 25-nov 07:00: `cPNiOFeY5_k` + `W9g2tPZTpD4`.
- 26-nov 17:00: `JqlKsJOVmdE` + `-1DRh_qj7Bg`.
- 27-nov 07:00: `jiX6RdwJ1gg` + `nd0rs6iVy8E`.
- 28-nov 17:00: `gN6svdqe62Q` + `fcSNbU809ao`.

La auditoría también registra 36 elementos sin MP4 local, 9 miniaturas corregidas y 4 con rework. No se repitieron operaciones de Studio.

### Corrección del inventario de publicaciones

- `main/data/publicaciones.json` contiene 48 registros totales, no dos; solo dos corresponden al 21-nov y no contiene el inventario programado del 22–23. La frase anterior «dos registros» se precisa como conteo de ese día, no del archivo completo.
- `feature/data/publicaciones.json` contiene 22 registros.
- La agenda 22–28 debe reconciliarse con `miniaturas_auditoria`, `resubidas` y el plan semanal; `publicaciones.json` por sí solo no es inventario completo.
- `data/vistas_historico.json` tiene 107 entradas; incluye `6XCBYrlO4Eg`, no incluye `ZG4iQgmWrLI`, Napoleón ni Colón. Estos últimos se contrastaron con cierre diario, miniaturas y programación.
- No existe `historial_youtube` en el árbol. No se afirma que el estado público del robot esté confirmado.

### Robot orbital: estado de publicación sin resolver

Se releyeron los blobs de main: `capsula.mp4` SHA `72d7ca5757a18b5d7a248503ac0e096dc0ac37ff` (25,795,339 bytes), portada, nueve frames, `programacion.json`, `qa.json` y `metadata.json`. La QA audiovisual es 21/21 y 87.57 s. `publish_at=2026-11-22T01:00:00Z` ya pasó; `programacion.json` conserva `estado=programado`, mientras `metadata.json` conserva `privacyStatus=private`. La apertura pública de YouTube devolvió `DisabledError`. Resultado: `PUBLICACION_REAL_NO_VERIFICADA / RIESGO_DE_ESTADO_PROGRAMADO_ANTIGUO`. No cancelar, reprogramar ni redispatchar. El estado de main que dice que los medios no se generaron está desactualizado frente a los blobs presentes.

### Dispatch, recepción y acciones

- Las 20 consultas `cola/estado/<id>.json` (12 IDs del lote 5–7 nov, siete proyectos 21–23 nov y robot) devolvieron 404. Todos conservan `RECEPCION_GROK_NO_CONFIRMADA`.
- Los 19 storyboards de proyectos siguen en `proyectos/<id>/`, sin copia plana promovida. Son `NOT_DISPATCHABLE_NOT_IN_QUEUE`.
- El robot está anidado en `cola/entrada/<id>/storyboard.json`; el workflow usa `cola/entrada/*.json` y `find -maxdepth 1`, por lo que es `NOT_DISPATCHABLE_POR_SELECTOR`. `scripts/procesar_cola.py` admite rutas anidadas, pero no se invocó.
- El workflow no ejecuta `validar_storyboard.py --check-doi`, ni comprueba `narrative_qa`, conflicto de slot o producción previa antes del webhook; solo valida sintaxis JSON. Es una brecha de defensa en profundidad si alguien coloca manualmente un JSON plano en cola. No se modificó ni disparó el workflow.
- El intento de listar el historial de Actions del workflow mediante el conector devolvió `HTTP 400: GitHub Fetch URL is not an allowed public GitHub repository or search endpoint`; no se infiere ausencia de ejecuciones. No se consultaron valores de secretos ni se declararon faltantes.
- CodeQL del commit feature `1bc4e1ba`: ambos jobs SUCCESS. PR #15 continúa OPEN; Semgrep run `45004335607` mantiene 26 hallazgos activos y FAILURE. El clon local de solo lectura falló con `Could not resolve host: github.com`; no se ejecutó la suite de ese PR. PR #3 sigue OPEN/DRAFT/dirty; PR #14 sigue sin PASS narrativo. Issue #11 permanece OPEN con etiqueta `hecho`.

### Radar y fuentes del corte

El investigador completó el radar `775a76aadd34848aa01f247e88c68cecd9367989`: cinco candidatos del 18–22 nov; los cinco DOI permanecen `PENDING_RESOLVER`. Los cinco enlaces DOI consultados directamente devolvieron `URL ... is not accessible via this tool`; no se declara verificación Crossref/resolvedor. El candidato del 22-nov no se usa en 23:30 porque no tiene cartografía exacta verificable. No se creó storyboard.

Google Trends oficial México, últimas 24 h, se abrió como respaldo: 263 tendencias, 25 por página; la primera página está dominada por fútbol/entretenimiento. `superluna` (2 mil+, +1.000 %) y `desierto de Atacama` (1 mil+, +200 %) son tendencias de búsqueda, no evidencia de un hallazgo científico nuevo. Fuente: https://trends.google.com/trending?geo=MX&hl=es

El aviso oficial de Page Insights se verificó: la referencia del endpoint muestra Graph API v27.0 y anuncia deprecaciones para 15-jun-2026; la página detallada solo lista 15-jun-2025, 15-nov-2025 y 14-mar-2024; el blog enlazado devolvió HTTP 429. Se mantiene la discrepancia documental en `INVESTIGACION_API_META_Y_GOOGLE_TRENDS.md §9.11`; no se cambiaron integraciones.

**Cierre:** no se promovió ni redispatchó contenido, no se generaron medios, no se modificaron `data/*.json`, main, estados Grok, programación, secretos ni permisos. El radar vigente queda con cinco candidatos y 23:30 `PENDING_SOURCE`; los conflictos de main quedan documentados para decisión, sin cancelaciones.


### Precisión de PR #15 — suite no ejecutada

La lectura de `tests/test_validar_storyboard_textual.py` en la rama `fix/capcot-map-coordinate-types-20261122` confirma **14 métodos unittest** (contrato narrativo, QA, mapas terrestres/celestes, booleanos en coordenadas/bounds y DOI). `scripts/validar_storyboard.py` fija la conexión HTTPS a `api.crossref.org` y rechaza booleanos antes de convertir coordenadas. El commit `30101e9aca8aaafb8d1894df30574a66067ff4a8` no tiene checks combinados registrados (`state=none`, `statuses=[]`). Se intentó clonar la rama para ejecutar la suite; error literal: `Could not resolve host: github.com`. No se ejecutaron los 14 tests y no se declara el PR validado.


### Cierre de estructura y fuentes de los siete proyectos 21–23 nov

Lectura de vuelta de los siete `storyboard.json` contra `scripts/validar_storyboard.py`, `scripts/estilos.json` y el contrato editorial:
- Los siete tienen 8 escenas, 171–208 palabras, 78 s de escenas + 6 s de cortinilla = 84 s; voz `es-MX-JorgeNeural`, `rate=+7%`, `pitch=-2Hz`; los seis campos narrativos por escena están completos.
- En los siete, `visual_identity.prompt_base` coincide literalmente con el catálogo y cada `image_prompt` empieza con ese texto.
- Todos tienen ambiente y SFX por escena, al menos una capa de dato/gráfico, `approved_assets=[]`, `export.render_status=NOT_GENERATED` y `publicacion.status=PENDIENTE_DECISION_GROK`.
- La cartografía está presente y explícitamente limitada: Fentale WGS84 8.985, 39.906; Homo erectus usa el centro urbano de Chongzuo como localizador regional, no como coordenada de las cuevas; el púlsar usa ICRS RA 245.553° / DEC −72.066° con envoltura RA solo para proyección celeste; AT 2025abao usa RA 9.7025° / Dec 40.7689528° convertido de la ficha NASA; Voyager usa los tres complejos DSN WGS84; yubarta usa bounds regionales Hakai 53.18, −129.6 a 53.68, −129.0 sin pines de muestras; biodiversidad usa el localizador regional publicado de Jambi −2.0158333, 103.2591667, no un centroide de parcelas. No se inventaron puntos de muestreo.
- Los QA PASS existentes de Fentale (90) y yubarta (90) conservan siete checks true, flags vacías y base de lectura en frío; no se repitieron. Homo erectus (83), púlsar (83), Voyager (83), AT 2025abao (84) y biodiversidad (82) conservan FAIL y sus flags originales.

**Corrección de fuente para biodiversidad:** la entrada anterior `SRC-002=PENDING_SOURCE` era incorrecta. `SRC-002` (Kurniawan et al., Biogeosciences 2018, DOI 10.5194/bg-15-5131-2018) está verificada en página editorial y aporta únicamente la coordenada regional de Jambi. El DOI pendiente es `SRC-001` (Nature 2026, 10.1038/s41586-026-11298-6). En AT 2025abao el DOI pendiente es `SRC-001`; NASA `SRC-002` y `SRC-003` están verificadas. Fentale tiene Crossref verificado; Homo y púlsar tienen DOI resuelto; Voyager usa NASA/JPL sin DOI y fuentes secundarias solo para localizadores DSN; yubarta tiene ambos DOI resueltos.

No se modificaron los siete storyboards: los cinco FAIL narrativos, los conflictos de slot, la duplicación temática de Fentale y los DOI pendientes siguen bloqueando cualquier promoción.


### Integridad de copias heredadas en cola/bloqueados — lote 5–7 nov

La lectura de árbol confirma siete artefactos bloqueados: cuatro carpetas con `storyboard.json` + `ESTADO_EJECUCION.md` + `fuentes.md`, y tres JSON planos sin carpeta. Los cuatro estados de carpeta revisados dicen `BORRADOR_EN_PROYECTOS_NO_APTO_PARA_PROMOCION`; no hay medios. Los tres JSON planos siguen bajo `cola/bloqueados`, no en `cola/entrada`.

**No se borró ni sobrescribió ningún artefacto:** en las cuatro parejas que tienen JSON plano y storyboard de carpeta, los contenidos no son idénticos. Las diferencias observadas incluyen:
- palomitas-explotan: 195 palabras en el JSON plano frente a 173 en la carpeta;
- aguacate negro: 198 frente a 170;
- ranas congeladas: 208 frente a 177 y dos fuentes frente a una;
- huesos de bebé: 207 frente a 172.

La variante `comida-palomitas-explotan` no comparte `project_id` con el storyboard canónico `comida-palomitas`. Rayo globular, arena cantante y nubes pesan como JSON plano solamente, sin carpeta/estado. Los otros cinco IDs canónicos del lote no tienen copia bloqueada.

Resultado: `BLOQUEADO_DUPLICADO_DIVERGENTE` para las cuatro parejas; `BLOQUEADO_JSON_PLANO_SIN_CARPETA` para las otras tres. Como no existe copia activa en `cola/entrada`, no se hizo movimiento ni eliminación. Los 12 proyectos originales siguen en `proyectos/`; no tienen `ESTADO_EJECUCION.md` propio.


### Backlog interdiario adicional — 18–20 nov (seis proyectos)

La inspección completa de `proyectos/` encontró seis storyboards posteriores al lote 5–7 nov que no estaban en la tabla anterior. Se leyeron narraciones en frío, QA existente, fuentes, catálogo, mapas, rotación y árbol de producción. No se repitió ningún PASS ni se reescribió narración.

| Proyecto | Slot | QA existente | Estado de slot / compuertas |
|---|---:|---|---|
| `2026-11-18_dato-catorce-campos-hidrotermales` | 23:30 | FAIL 68 | Main ya tiene Hielo sucio `2a36r5QOvi4` a 23:30; conflicto de slot y estilo `papel_rasgado_capas` repetido por Sinergia de algas del 18-nov |
| `2026-11-18_dato-kuroshio-puente-atmosferico` | 17:00 | PASS 90 | Sin video main encontrado al mismo slot; 17:00 sigue siendo ventana en prueba, no autorización regular; DOI visible pero Crossref/resolvedor no confirmado |
| `2026-11-19_dato-dia-luz-dos-manos-oro-poroso` | 23:30 | PASS 91 | No se encontró publicación main al mismo slot; DOI `10.1038/s41467-026-78158-9` sin resolver; estilo `microscopio_psicodelico` repetido por Autismo/microbioma del 15-nov |
| `2026-11-19_dato-estrella-dentro-de-estrella` | 17:00 | PASS 90 | 17:00 en prueba; DOI `10.1038/s41586-026-11221-z` sin resolver; `art_deco_poster` repetido por Baffin (17-nov) y Juno (19-nov) |
| `2026-11-20_dato-dia-atlantico-humedad-sapropeles` | 23:30 | PASS 91 | Main ya tiene Metano `Eldk0fVWqpo` a 23:30; conflicto de slot; DOI `10.1038/s41561-026-02141-8` pendiente de resolvedor; `linograbado` repetido por Corales (16-nov) |
| `2026-11-20_dato-marea-cerebral-en-sueno` | 17:00 | PASS 92 | 17:00 en prueba; DOI `10.1038/s43587-026-01270-4` pendiente de resolvedor; `neon_noir` coincide con Robot orbital del 21-nov |

Los seis cumplen estructura: ocho escenas, 188–222 palabras, 78 s de escenas + 6 s de cortinilla, voz correcta, seis campos narrativos por escena, prompt_base del catálogo, mapa, capa de dato/gráfico, ambiente y SFX; `approved_assets=[]`, `NOT_GENERATED`, publicación pendiente. Los QA PASS tienen siete checks true y flags vacías; sus commits de QA son posteriores y separados de los commits redactores. Hidrotermales conserva FAIL 68 y sus cuatro flags. Los dos `ESTADO_EJECUCION.md` existentes (hidrotermales y Kuroshio) dicen BORRADOR; los otros cuatro no tienen ese archivo, permitido porque el Plan Maestro define el JSON como expediente de proyecto y las fuentes van incorporadas en él.

Las seis consultas `cola/estado/<id>.json` devolvieron 404 exacto: `RECEPCION_GROK_NO_CONFIRMADA`. No hay copias en `cola/entrada/`, `cola/bloqueados/` ni `salidas/`. No se creó QA ni se promovió nada.

### Rotación de estilos — contraste de 13 proyectos 18–23 nov

La comparación manual contra `main/data/rotacion.json` (39 registros; últimos registros publicados 14–21 nov) detecta repeticiones recientes. `scripts/registro_editorial.py` es una vista de lectura y no aplica por sí sola un veto de estilo; se conserva la regla editorial explícita de no repetir:
- `papel_rasgado_capas`: hidrotermales 18-nov / Sinergia de algas main 18-nov.
- `microscopio_psicodelico`: oro poroso 19-nov / Autismo-microbioma main 15-nov.
- `art_deco_poster`: estrella 19-nov y Bao 22-nov / Baffin main 17-nov y Juno main 19-nov.
- `linograbado`: sapropeles 20-nov / Corales main 16-nov.
- `neon_noir`: marea cerebral 20-nov / Robot main 21-nov.
- `dibujo_cientifico_scratchboard`: Homo erectus 21-nov / ADN main 19-nov.
- `pixel_art`: púlsar 21-nov / MXenes main 20-nov.
- `risografia`: Voyager 22-nov / residual-LDL main 17-nov.

Estilos sin repetición en ese corte: `atlas_antiguo` (Kuroshio), `pulp_comic_1940s` (Fentale), `tatuaje_acuarela` (yubarta) y `ligne_claire` (biodiversidad). La repetición no se corrige cambiando el estilo en auditoría; requiere una decisión editorial del investigador. Los proyectos siguen bloqueados por sus respectivos slots, DOI y/o QA.

Con estos seis expedientes, el inventario auditado del backlog interdiario pasa a 25 storyboards: 12 del lote 5–7 nov, seis del 18–20 nov y siete del 21–23 nov. Sumados al robot orbital, las lecturas de `cola/estado` son 26 respuestas 404; no hay recibo Grok confirmado.


### Aclaración de asignación intermedia del 19-nov 17:00

La búsqueda del registro `pendientes/abiertos/2026-11-19_de-pecas_para-imaginantes_montar-5-manana.md` revela una asignación previa a Pecas para `2026-11-05_bacterias-plasticos-oceano`; por tanto, el slot 19-nov 17:00 no era un hueco libre para reasignar a `2026-11-19_dato-estrella-dentro-de-estrella`. El proyecto preexistente está señalado `NO TOCAR (fuentes falsas)` en `ajustes_entre_modelos/DELEGACIONES.md`. El mismo registro reporta un MP4 local de 32.20 s, pero el árbol de main contiene únicamente `README.md`, `HYPERFRAMES.md` y `storyboard.json`: no contiene `capsula.mp4`, frames ni audio. Su `cola/estado/2026-11-05_bacterias-plasticos-oceano.json` devuelve 404. Resultado: `SLOT_RESERVADO_A_PECAS`, `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`, `RECEPCION_GROK_NO_CONFIRMADA`; no redispatchar ni sustituirlo con otro proyecto sin decisión editorial.

La nota del 18-nov que propone Vikingos para 17:00 es obsoleta respecto de la rotación main: Vikingos ya aparece publicado el 17-nov 17:00. No se usa como ocupación del 18-nov. El 20-nov 17:00 no muestra otra asignación en los pendientes consultados, pero continúa siendo ventana en prueba. En consecuencia, los tres proyectos 17:00 (Kuroshio, estrella y marea cerebral) siguen sin autorización de promoción por política de slot; estrella añade la reserva previa a Pecas.


### Recuento final de recepción

El total de 26 respuestas 404 cubre los 25 storyboards en `proyectos/` más el robot orbital. La consulta adicional del storyboard heredado `cola/entrada/2026-11-05_bacterias-plasticos-oceano/` también devolvió 404. Recuento ampliado: **27 estados Grok no confirmados**. No se creó ningún archivo de estado.


### Reconciliación adicional — 22-nov-2026, 10:01 CDMX

#### Ejecuciones y estado de rama
- Investigador CAPCOT: última ejecución terminal observada **COMPLETED** el 22-nov a las 08:12 CDMX; su radar/API ya están incorporados en esta rama. Auditor CAPCOT: última ejecución terminal observada el 21-nov a las 15:30 CDMX; la siguiente ventana del 22-nov aún no había llegado al corte. No se atribuye QA nuevo al auditor.
- HEAD feature observado: `8ff614d061b0430b5d18ce72f96f61e460351f58`; HEAD main observado: `f94300bfcbbd509fdd54c8963b948aadc1372fcf`.
- PR #3 sigue OPEN/DRAFT y `mergeable=false`: 696 archivos, 1,242 commits; feature está 1,242 commits por delante y 512 por detrás de main. Su diff incluye **13 rutas `data/*.json`** y 145 rutas `cola/`. No integrar: el contrato de esta operación mantiene `data/*.json` en solo lectura y el diff no es integrable sin reconciliación independiente.

#### PR #15 — Semgrep y pruebas
- PR #15 sigue OPEN, no draft, mergeable=true; base `feature/capcot-video-discovery-continuity`, head `fix/capcot-map-coordinate-types-20261122`, commit `30101e9aca8aaafb8d1894df30574a66067ff4a8`; dos archivos modificados.
- Run Semgrep `45004335607` terminó FAILURE. El SARIF descargado (artifact `14746933868`) contiene 27 resultados: **26 bloqueantes** y uno con `suppressions.kind=inSource` para `HTTPSConnection`. Los 26 bloqueantes se distribuyen en 11 referencias mutables de GitHub Actions, 11 usos dinámicos de urllib, 2 usos de subprocess, 1 acceso dinámico a globals y 1 uso de MD5. No se interpreta el resultado suprimido como hallazgo bloqueante ni se declara el PR limpio.
- `tests/test_validar_storyboard_textual.py` contiene 14 métodos de prueba, pero el único workflow asociado al commit consultado es Semgrep; el estado combinado de checks del commit es `none` con `statuses=[]`. Se intentó clonar la rama para ejecutar los tests y falló literalmente: `Could not resolve host: github.com`. **Suite no ejecutada; PR no validado.** No se añadió workflow ni se disparó CI.

#### Revalidación de proyectos y recepción
- Se releen los cuatro storyboards de 22–23 nov. Bao (13:30) conserva QA FAIL/84; Voyager (07:00) FAIL/83; yubarta (17:00) PASS/90; biodiversidad (23-nov 13:30) FAIL/82. No se repitió QA ni se modificó narración.
- Las cuatro consultas individuales `cola/estado/<project_id>.json` devolvieron HTTP 404 exacto; se conserva `RECEPCION_GROK_NO_CONFIRMADA`. No se creó estado ni entrada plana. Yubarta mantiene PASS narrativo, pero no se promueve por conflicto de slot/rotación y falta de recepción confirmada.
- Los cuatro storyboards conservan `approved_assets=[]`, `export.render_status=NOT_GENERATED` y `publicacion.status=PENDIENTE_DECISION_GROK`. La entrada de cola existente sigue siendo el robot orbital anidado, con producción previa: no redispatchar.
- La búsqueda del corte del 22-nov no encontró una fuente primaria de ciencia/naturaleza publicada ese mismo día apta para ocupar 23:30. Las fuentes recientes halladas son anteriores: [NASA, hielo antiguo más allá de Neptuno, 18-nov](https://science.nasa.gov/blogs/science-news/2026/11/18/nasa-scientists-find-clues-to-ancient-ice-beyond-neptune/), [ESA, Plasma Observatory, 19-nov](https://www.esa.int/articles/about-us/directorates/science/seven-spacecraft-observatory-to-study-plasma-universe) y [Reuters, fusión estelar Bao, 20-nov](https://www.reuters.com/science/astronomers-observe-huge-puffy-star-merge-with-smaller-companion-2026-11-20/); Bao ya tiene proyecto y QA FAIL. No se reutilizó material antiguo como dato del día.
- Los cinco endpoints DOI consultados en Crossref no fueron accesibles desde el lector actual (`URL ... is not accessible via this tool`). Los DOI que el radar mantiene como `PENDING_RESOLVER` siguen sin verificarse; no se sustituyó Crossref por una página editorial.

**Cierre de esta reconciliación:** no se modificaron `data/*.json`, main, storyboards, estados Grok, cola, programación, workflows, secretos ni permisos. No se promovió, despachó, publicó ni generó medios.

### Corrección de atribución de CodeQL — 22-nov-2026

- El run `45020909784` no corresponde al HEAD actual de feature: la API lo identifica como workflow `PR #3`, evento `dynamic`, `head_branch=refs/pull/3/head`, SHA `1bc4e1ba6113ffc6afd71e8a653f8413ed49698f`. Su SUCCESS acredita ese commit del PR #3, no `8ff614d061b0430b5d18ce72f96f61e460351f58`.
- `fetch_commit_workflow_runs` para el HEAD actual `8ff614d` devolvió lista vacía. La consulta de las últimas diez Actions filtradas por la rama feature mostró únicamente validaciones Kuroshio, con última ejecución el 21-nov 21:27:24Z; no mostró un check de CodeQL para el HEAD actual. Por tanto, no declarar CodeQL verificado en `8ff614d`.
- La corrección no altera ningún workflow ni dispara ejecuciones.