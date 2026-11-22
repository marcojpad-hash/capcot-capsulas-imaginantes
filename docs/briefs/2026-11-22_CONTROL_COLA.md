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
