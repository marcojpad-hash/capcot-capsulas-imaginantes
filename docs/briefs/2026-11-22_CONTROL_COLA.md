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

### Lectura de vuelta final de esta bitácora — 22-nov-2026

La reconciliación y su corrección de atribución quedaron guardadas y releídas. El HEAD de `feature/capcot-video-discovery-continuity` después de ambas actualizaciones es `b7c38402f9fd2fba3d8caf82805de08e758350d7`; blob actual de este control: `a77794738961365c1deab3d01bbe0f95a381a84b`.

### Prueba adicional del resolvedor DOI — 22-nov-2026

Se intentó además abrir directamente los cinco DOI del radar mediante `https://doi.org/<doi>`. Los cinco devolvieron el mismo error del lector: `URL https://doi.org/<doi> is not accessible via this tool`. DOI consultados: `10.1038/s41586-026-11221-z`, `10.1038/s41586-026-11298-6`, `10.1111/1755-0998.70219`, `10.1126/sciadv.aeg1602` y `10.3897/zookeys.1295.205902`. Esto **no demuestra que los DOI estén rotos**; demuestra que este lector no pudo verificar el salto del resolvedor. Los cinco siguen pendientes de una comprobación Crossref/resolvedor ejecutable.

### Estado final de PRs y HEAD — 22-nov-2026

- HEAD final de feature tras las adendas de control: `c36319fd4228e40dad031c062c80bdd610d533a0`.
- PR #3: OPEN/DRAFT, `mergeable=false`, 1,246 commits y 696 archivos. No integrar.
- PR #15: sigue OPEN, pero ahora `mergeable=false`. Su base registrada es `d30814995de642e3b6100d19d968115264a3d690`; feature está 26 commits por delante de esa base. No actualizar la rama del PR ni fusionar durante esta operación. Los 26 hallazgos Semgrep y la suite de 14 tests no ejecutada siguen abiertos.
- Lectura de vuelta del control: el archivo incluye esta adenda y el HEAD coincide con el commit final.

## Reconciliación adicional — 22-nov-2026, 11:55 CDMX

### Autoridad de ramas y nuevos cambios en main

- Feature estaba en `29cc2f3` antes del nuevo borrador; main avanzó hasta `77bf85b`. Se detectó un paquete nuevo en main, `2026-11-22_pulsar-criptografia`, tanto en `proyectos/` como en `cola/entrada/`; no se modificó main.
- El paquete Pulsar declara 22-nov 13:30 en `programacion.json`, pero `yt_programado=false`, `mp4=false` y privacidad `private`. La carpeta de cola contiene solo `storyboard.json`; no hay `cola/estado/<id>.json`, salida, carpeta bloqueada ni handoff marker. Su storyboard tiene 7 escenas, 146 palabras y 78 s de escenas + 6 s de cortinilla = 84 s frente a objetivo 85; no tiene `narrative_qa`, `approved_assets` ni `export.render_status`, y conserva `asset_filename` y `export.filename`. Además carece de `fecha_objetivo` y `slot_local` en el JSON.
- La programación de main ya ocupa 22-nov 13:30 con Gutenberg. Por tanto Pulsar es `NOT_DISPATCHABLE`, `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR` y conflicto de slot con Gutenberg; no duplicar ni mover desde main.
- Main también registra Salem publicado a 07:00, Ada programado a 17:00 y Webb con `publishAt`/privacidad privada a 19:00. La auditoría de miniaturas registra Rosetta el 23-nov a 13:30. No se canceló ni reprogramó ningún ID.

### Reconciliación de los storyboards de feature

| Proyecto | QA narrativo leído | Slot declarado | Reconciliación con main | Recepción |
|---|---:|---:|---|---|
| Voyager | FAIL 83 | 22-nov 07:00 | Salem ya publicado a 07:00; conflicto | `RECEPCION_GROK_NO_CONFIRMADA` (404) |
| Bao | FAIL 84 | 22-nov 13:30 | Gutenberg programado y Pulsar planificado a 13:30; conflicto | `RECEPCION_GROK_NO_CONFIRMADA` (404) |
| Yubarta | PASS 90 | 22-nov 17:00 | Ada programado a 17:00; conflicto | `RECEPCION_GROK_NO_CONFIRMADA` (404) |
| Biodiversidad tropical | FAIL 82 | El texto de ocasión dice 23-nov 13:30, pero faltan `fecha_objetivo` y `slot_local` en el JSON | Rosetta aparece programado a 23-nov 13:30; conflicto inferido desde el texto, no normalizado en campos | `RECEPCION_GROK_NO_CONFIRMADA` (404) |

Los cuatro directorios de proyecto no contienen `ESTADO_EJECUCION.md`; no se crearon estados Grok ni se promovió ninguna copia. El robot orbital conserva QA narrativo PASS 90, pero main contiene MP4, portada, frames y programación preexistente; el marker de handoff sigue `pending` y el estado Grok es 404. Se mantiene `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`.

### Selector y automatizaciones

- El run `45050940152` del trabajador terminó SUCCESS, pero el log dice literalmente `sin trabajo en cola`. `scripts/trabajador_cola.py` consulta Issues con etiqueta `cola`; no procesa los directorios anidados de `cola/entrada/`.
- `.github/workflows/capcot-grok-dispatch.yml` escucha la rama feature y archivos planos `cola/entrada/*.json`; su selector manual usa profundidad máxima 1. No detecta el paquete Pulsar anidado en main ni el robot anidado.
- Main Semgrep run `45048155842` terminó FAILURE con 32 hallazgos bloqueantes; Gitleaks `45048155841` terminó SUCCESS. El último validador de feature, run `44951621909`, corresponde al commit anterior `ed8659e`, no al HEAD actual; no acredita validación de los borradores nuevos.
- PR #3 sigue draft/no mergeable (696 archivos, 13 JSON de data y 145 rutas de cola). PR #15 sigue abierto y desfasado respecto a feature (head `30101e9`, base `d308149`); su revisión anterior registró 27 hallazgos Semgrep y 14 pruebas sin ejecutar. PR #14 conserva QA FAIL 82; PR #13 aporta un informe separado con 13 hallazgos, nueve pendientes. PR #6 delega a un workflow reutilizable del repo adicional público `agente-cero-costo` mediante `secrets: inherit`; el workflow leído solo consume `BUS_GITHUB_TOKEN`, pero la herencia completa es más amplia de lo necesario. PR #4 conserva una actualización de estado del robot incompatible con la producción preexistente. No se fusionó ni cerró ningún PR.

### Borrador nuevo y compuertas

Se creó y leyó de vuelta `proyectos/2026-11-22_genes-estatura-etapas/storyboard.json` en el slot 23:30, libre en los registros de main. Tiene 8 escenas, 229 palabras, 84 s totales, voz `es-MX-JorgeNeural +7% / -2Hz`, prompt_base `papel_stop_motion`, mapa institucional con coordenadas, gráficos de 574,580 mediciones y 106 proteínas, ambiente/SFX por escena y cierre hablado exacto. No tiene `narrative_qa`, no está marcado PREPARADO, no contiene medios ni rutas, `approved_assets=[]`, `export.render_status=NOT_GENERATED` y `publicacion.status=PENDIENTE_DECISION_GROK`. El DOI sigue pendiente; no se promovió.

Hallazgo de proceso: `scripts/validar_storyboard.py` exige `narrative_qa` incluso para un borrador, aunque el investigador tiene prohibido crear ese campo. La auditoría independiente debe añadir QA después; el validador actual acopla estructura y QA y no demuestra su independencia. No se cambió el script ni se disparó workflow en este run.

### Datos de rotación y registros

Los JSON de data permanecen solo lectura. Feature conserva snapshots viejos (temas hasta 28-oct, rotación hasta 31-oct y 22 publicaciones), mientras main tiene 48 publicaciones y una rotación más reciente de 39 entradas. Para el slot actual se usó main como cotejo de ocupación; el estilo `papel_stop_motion` no aparece en las 39 entradas consultadas ni en los proyectos activos. No se modificó ningún `data/*.json`.

### Corrección de evidencia — medios y estado individual

- El storyboard Pulsar de main contiene referencias de archivo, pero la carpeta de proyecto solo contiene `storyboard.json`, `programacion.json` y `fuentes.md`; `capsula.mp4` devuelve 404. Clasificación obligatoria: `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`. No se modifica ni se retira la copia de main.
- Los cuatro proyectos de feature revisados (Bao, Voyager, Yubarta y Biodiversidad tropical) no incluyen `asset_filename`, `asset_type` ni rutas en sus escenas; todos tienen `approved_assets=[]` y `export.render_status=NOT_GENERATED`. Sus carpetas contienen únicamente `storyboard.json`; no hay `ESTADO_EJECUCION.md`.
- El nuevo borrador de estatura tampoco tiene estado Grok: `cola/estado/2026-11-22_genes-estatura-etapas.json` devolvió 404. Registrar `RECEPCION_GROK_NO_CONFIRMADA`; no se creó ni modificó estado.



## Actualización de ejecución — 22-nov-2026, 12:22 CDMX

### Proyecto nuevo y compuertas

Se auditó `proyectos/2026-11-22_genes-estatura-etapas/storyboard.json`, creado después del corte de la auditoría anterior.

- **Fuente:** DOI `10.1038/s41467-026-79465-x` verificado en Crossref; título/editorial coinciden con Nature Communications y la página primaria fecha la publicación el 22-nov-2026.
- **Mapa:** NIPH confirma oficialmente las direcciones de visita Lovisenberggata 6 y 8, Oslo. La coordenada Oslo es de nivel calle, no de edificio. UK Biobank confirma Greenheys, Manchester Science Park, Pencroft Way, M15 6GZ; su enlace oficial de Google Maps resuelve a 53.4630203, -2.23864. El mapa se etiqueta como ubicación institucional, no como ubicación de participantes.
- **Correcciones mecánicas verificadas:** engine `edge-tts`; `voice_id=es-MX-JorgeNeural`, rate +7%, pitch -2Hz; `_schema=CAPCOT_STORYBOARD_TEXT_V2`; aliases de `estructura`, `estilo_id`, contrato narrativo, citas y `scene.id`; prompt_base copiado literalmente del catálogo `papel_stop_motion`; `word_count` corregido de 229 a 231. Narración, claims, título y arco permanecen sin cambios.
- **Comprobación estructural manual previa a QA:** cero errores en campos requeridos, fuentes referenciadas, capa de mapa, capa de dato, coordenadas, prompts, voz, 231 palabras, 8 escenas, 78 segundos de escenas + 6 segundos de cortinilla = 84 segundos, cierre exacto, `approved_assets=[]`, `export.render_status=NOT_GENERATED` y publicación pendiente. Esto no equivale a ejecución del validador oficial.
- **QA:** `narrative_qa` sigue ausente deliberadamente. No se hizo lectura independiente en frío porque corresponde al auditor separado. `scripts/validar_storyboard.py` exige `narrative_qa`; por tanto, su resultado final seguirá siendo FAIL hasta que exista esa revisión independiente y PASS válido. No se inventó QA.
- **Handoff:** `cola/entrada/<id>.json` no existe; `cola/estado/2026-11-22_genes-estatura-etapas.json` devuelve 404; tampoco existe `ESTADO_EJECUCION.md` ni salida de medios. Estado: `NOT_DISPATCHABLE`, `RECEPCION_GROK_NO_CONFIRMADA`, `BORRADOR_EN_PROYECTOS`. No se promovió, despachó ni marcó preparado.

Commits de este corte: `d130e72f62b324e44efb475f0c09faff899c7e4c` (metadatos y esquema), `dabeb4c3ee963931572a8780b09857c17a5057af` (radar y DOI).

### Inventario y autoridad de datos

- El inventario de proyectos de fecha actual/backlog interdiario y el lote antiguo contiene **26 proyectos**: 12 del 5–7-nov, 6 del 18–20-nov, 7 del 21–23-nov y el borrador adicional de genética de estatura del 22-nov. La auditoría anterior contabilizaba 25; se corrige a 26.
- QA previo sin cambios en los 25 existentes: lote 5–7-nov = 2 PASS / 10 FAIL; 18–20-nov = 5 PASS / 1 FAIL; 21–23-nov = 2 PASS / 5 FAIL. El proyecto de genética queda **pendiente de auditor independiente**, no se suma a PASS ni FAIL. Total actual: 9 PASS, 16 FAIL, 1 pendiente.
- Fuente de verdad main: `data/publicaciones.json` contiene **52** registros y `data/rotacion.json` **39**. La nota anterior de 48 publicaciones era incorrecta. Los snapshots feature tienen 22 publicaciones y 27 rotaciones; no se usan como autoridad de ocupación.
- Main registra publicación 22-nov 07:00 Salem y `publishAt` 21:00 Cleopatra. El plan semanal mantiene 13:30 Gutenberg, 17:00 Ada y 19:00 Webb. En paralelo, `proyectos/2026-11-22_pulsar-criptografia/programacion.json` declara 13:30, pero `yt_programado=false`, `mp4=false` y privacidad `private`. La discrepancia de 13:30 queda abierta; no afecta el 23:30, que no aparece ocupado en main.

### Actions, PR y dispatch

- HEAD feature observado antes de este corte: `4771cd03`; main: `77bf85b`. Los commits de esta actualización quedaron en feature. No se escribió en main.
- PR #3: 697 archivos cambiados, 13 archivos `data/*.json` y 145 rutas de cola; OPEN/DRAFT, dirty, base antigua `6397fbd`. No integrar.
- PR #15: head `30101e9`, base `d308149` (no el HEAD actual de feature); GitHub informa `mergeable=true` pero `mergeable_state=unstable`. No hay CI de su head; sus 14 pruebas siguen sin evidencia de ejecución y Semgrep mantiene 32 hallazgos en el run de main. No integrar.
- La última validación de feature disponible, run `44951621909`, corresponde al commit antiguo `ed8659ec` y al proyecto Kuroshio; no valida este storyboard ni el HEAD actual. Los checks SUCCESS de PR #3 ejecutados sobre main no se atribuyen a feature.
- Worker main run `45050940152`: SUCCESS, log literal `sin trabajo en cola.` Semgrep main run `45048155842`: FAILURE, 32 hallazgos. Gitleaks main run `45048155922`: SUCCESS.
- `capcot-grok-dispatch.yml` solo observa JSON planos de primer nivel en `cola/entrada/*.json`; el storyboard nuevo está exclusivamente en `proyectos/<id>/storyboard.json`. No es despachable por esa ruta. No se dispararon workflows ni se enviaron payloads.
- Presencia de `GROK_WEBHOOK_URL` y `GROK_WEBHOOK_TOKEN`: no verificable mediante el listado disponible; no se declararon ausentes ni se consultaron valores.

No se modificó ningún `data/*.json`, main, secreto, permiso, publicación ni medio.


## Reconciliación del operador — 22-nov-2026, corte 14:04 CDMX

### Proyecto 23:30 y QA

- Releído desde GitHub `proyectos/2026-11-22_genes-estatura-etapas/storyboard.json`, blob `e0e32f9705bba8ccd87dfd6e24c2d36b11724346`. El JSON conserva 8 escenas, 231 palabras según la expresión regular del validador, 78 s de escenas + 6 s de cortinilla = 84 s, gancho de 5 palabras, voz `es-MX-JorgeNeural` +7% / -2Hz, prompt_base literal `papel_stop_motion`, mapa institucional con coordenadas, capa de dato/gráfico, ambiente/SFX por escena, cierre exacto, `approved_assets=[]`, `export.render_status=NOT_GENERATED`, sin nombres/rutas de medios y `publicacion.status=PENDIENTE_DECISION_GROK`.
- El preflight estructural estático reprodujo las reglas relevantes del validador y no encontró errores de estructura, voz, estilo, prompt, arcos, referencias, mapa, dato, duración o assets. **No se ejecutó el script oficial** `validar_storyboard.py` ni CI con `--check-doi`; no se declara validación oficial.
- No se escribió `narrative_qa`: este operador no es el Auditor CAPCOT independiente y no debe sustituirlo. Estado: `PENDIENTE_AUDITOR`. El borrador no se promueve ni se copia a cola. La lectura narrativa independiente queda para el auditor separado; no se reescribió narración ni claims.
- La fuente primaria Nature Communications y el DOI constan en el storyboard como `VERIFICADO_CROSSREF`; el corte previo del radar registra `status=ok`. En este run, las aperturas del API Crossref y de doi.org no fueron accesibles mediante el lector (`URL ... is not accessible via this tool`); no se afirma una nueva verificación, pero tampoco se invalida la comprobación previa registrada.
- El slot 22-nov 23:30 queda ocupado por este borrador: `NO_DUPLICAR`. No se creó una segunda versión.

### Cruce de main, cola y producción

- Main contiene `2026-11-22_pulsar-criptografia` con `programacion.json` para 13:30 CDMX, `yt_programado=false`, `mp4=false`, `export.filename=capsula.mp4` pero sin MP4 en el árbol ni carpeta `salidas/<id>/`. La copia de cola está anidada; el selector del workflow no la detecta. Se conserva `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR` / `NOT_DISPATCHABLE_POR_SELECTOR` para ese paquete. Ocupa 13:30, no 23:30; no hay conflicto de slot con genética de estatura.
- El robot orbital conserva producción verificable en `main/cola/entrada/2026-11-09_dato-robot-ensambla-orbita/`: MP4 de 25,795,339 bytes, portada, frames, subtítulos y QA audiovisual 21/21, duración 87.57 s. `programacion.json` registra YouTube `ZG4iQgmWrLI`, TikTok y Facebook programados para 21-nov 19:00 CDMX (`publish_at=2026-11-22T01:00:00Z`), timestamp ya vencido. La búsqueda pública del ID no devolvió resultados y `historial_youtube.json` no existe en ninguna de las dos ramas; estado público real no verificado. Clasificación: `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`; no cancelar ni reprogramar.
- El paquete robot en feature contiene solo storyboard/textos y un directorio de frames; los medios se verifican en main, no en feature. El marker de `handoffs/grok_inbox` no equivale a recepción Grok.
- Las 26 consultas individuales `cola/estado/<project_id>.json` de los storyboards auditados devolvieron 404; la consulta adicional del robot también devolvió 404. Total: **27 `RECEPCION_GROK_NO_CONFIRMADA`**. No se creó ni modificó ningún estado.

### Inventario, datos y rotación

- Inventario del alcance: **26 storyboards** (12 del 5–7 nov, 6 del 18–20 nov, 7 del 21–23 nov y el borrador de genética). QA existente: **9 PASS / 16 FAIL / 1 PENDIENTE_AUDITOR**. No se repitió ningún PASS ni se modificó narración.
- Main: 52 publicaciones, 39 entradas de rotación y 32 estilos usados. Feature: 22 publicaciones, 27 entradas de rotación y 21 estilos usados. `temas_del_dia.json` continúa hasta 28-oct; los snapshots feature son incompletos y no sustituyen main. `historial_youtube.json` devuelve 404 en ambas ramas. Todos los `data/*.json` permanecen solo lectura.
- `papel_stop_motion` existe en el catálogo y no aparece en las 39 entradas de rotación de main ni en el storyboard Pulsar de main (que usa `van_gogh`).

### Issues, PR y CI

- CAPCOT Issue #11 sigue OPEN con etiqueta `hecho`; su storyboard de cuásares ya conserva `narrative_qa` FAIL/82 y el PR #13 está OPEN/no mergeable. El ledger `ajustes_entre_modelos/LEDGER_ASIGNACIONES.md` de main todavía muestra `CUASARES-AUDITORIA` en `cola`; discrepancia documental, sin editar main.
- PR #3 sigue OPEN/DRAFT/no mergeable. El listado actual devuelve 697 archivos, 13 JSON de `data/` y 145 rutas de cola; este run no modificó ningún JSON de data.
- PR #15 sigue OPEN/no mergeable (head `30101e9`, base `d308149`), con solo `validar_storyboard.py` y su test en el diff; 27 hallazgos previos (26 activos y uno suprimido) y 14 pruebas sin evidencia de ejecución.
- El HEAD actual de feature no tiene checks combinados registrados. La última validación disponible `44951621909` corresponde a `ed8659e`, no al HEAD actual. No se dispararon workflows ni se enviaron payloads.
- Presencia de `GROK_WEBHOOK_URL` y `GROK_WEBHOOK_TOKEN` no verificada; no se declararon ausentes ni se consultaron valores.

Cierre: no se promovió ni redispatchó contenido, no se generaron medios, no se publicó ni programó, no se modificó main, `data/*.json`, estados Grok, secretos, permisos ni workflows.


### Clasificación de handoff y cierre de commits

- Los 12 IDs del lote 5–7 nov se cotejaron contra `main/data/horario_semana_2026-11-01_07.json` y `main/ajustes_entre_modelos/PARA_CHATGPT_semana_01-07nov.md`; coinciden con los 12 expedientes revisados.
- Los 26 storyboards del alcance permanecen en `proyectos/<id>/storyboard.json`; no existe copia plana `cola/entrada/<id>.json` para ellos. Resultado de ruta: **26 NOT_DISPATCHABLE**. El paquete robot y el Pulsar de main están en carpetas anidadas, no en el selector plano. `scripts/procesar_cola.py` recorre anidados, pero `.github/workflows/capcot-grok-dispatch.yml` selecciona solo `cola/entrada/*.json` / profundidad 1. No se disparó el workflow.
- `2026-11-22_genes-estatura-etapas`: `NOT_DISPATCHABLE` por ausencia de copia de cola y estado 404; `PENDIENTE_AUDITOR`. No hay conflicto con el proyecto Pulsar de main, cuyo `programacion.json` declara 13:30 CDMX.
- Robot orbital: `NOT_DISPATCHABLE` por ruta anidada y `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`; el estado individual sigue 404 aunque haya marker de handoff y medios en main.
- Commits de este corte: storyboard restaurado sin `narrative_qa` no independiente (blob `e0e32f9705bba8ccd87dfd6e24c2d36b11724346`); control actualizado en `401a1a79e14aef12c455a2153558d7b3579cea78`; radar actualizado en `8563d76f0503d924bdf0776f5568fa69a58efd11`. El control y el radar se verificaron por lectura de vuelta. No se modificó `data/*.json`.


## Corte de auditoría independiente — 22-nov-2026, 15:54 CDMX

**Corte de contenido releído:** feature ``25e1ecfc96faf9a40f86a9feb0e30af90d9d608b``; main ``abc699b9f7523cd39477896492efd0f3c767cda0``. Este addendum sustituye los estados pendientes/obsoletos de los cortes anteriores cuando se contradigan con los JSON actuales.

### Inventario vigente y proyectos del 22-nov

El árbol feature contiene 89 ``proyectos/<id>/storyboard.json``. De ellos, cuatro corresponden a la fecha actual; no son tres:

| Project ID | Slot / cesta | Narrativa | Preflight estático |
|---|---|---:|---|
| ``2026-11-22_voyager-1-un-dia-luz`` | 07:00 / ``manana`` | FAIL 83; ``FECHA_DE_HITO_Y_CONFIRMACION_CONFUNDIDAS`` | 8 escenas, 180 palabras, 84 s, gancho 4 |
| ``2026-11-22_bao-estrella-fusion-andromeda`` | 13:30 / ``slot_cesta`` ausente | FAIL 84; ``STAKES_NO_EXPLICADOS`` | 8 escenas, 192 palabras, 84 s, gancho 6 |
| ``2026-11-22_yubarta-genoma-soplo`` | 17:00 / ``intermedio_1`` | PASS 90; siete checks true, flags vacías | 8 escenas, 180 palabras, 84 s, gancho 4 |
| ``2026-11-22_genes-estatura-etapas`` | 23:30 / ``slot_cesta`` ausente | **FAIL 72**, registrado en esta auditoría | 8 escenas, 231 palabras, 84 s, gancho 5 |

En los cuatro, el preflight estático confirma voz ``edge-tts / es-MX-JorgeNeural / +7% / -2Hz``, estilo existente en catálogo, ``prompt_base`` literal, source_ids internos válidos, capa de mapa y capa de dato/gráfico, ``approved_assets=[]``, ``export.render_status=NOT_GENERATED`` y ausencia de ``asset_filename``, ``asset_type`` y rutas de medios. No se ejecutó el validador oficial para estos cuatro; esta comprobación no equivale a CI ni a ``--check-doi``.

**QA independiente nuevo de genética de estatura:** lectura exclusiva de la narración concatenada; ``narrative_qa.status=FAIL``, ``score=72``, ``review_basis=lectura_en_frio_solo_narracion``. Checks exactos: ``pregunta_central_reconstruible=true``, ``apertura_in_medias_res=false``, ``progresion_por_escena=false``, ``transiciones_causales=false``, ``giro_cientifico_explicado=false``, ``limite_evidencia_explicito=true``, ``payoff_cierre_apertura=true``. ``critical_flags``: ``APERTURA_DEFINICIONAL_NO_IN_MEDIAS_RES``, ``MAPA_DE_INSTITUCIONES_ROMPE_CONTINUIDAD_NARRATIVA``, ``GIRO_CIENTIFICO_NOMBRADO_SIN_MECANISMO_EXPLICADO``. La pregunta se reconstruye y el final vuelve a la premisa, pero la apertura es declarativa, la frase del mapa interrumpe la narración y la asociación proteína/diabetes no explica el mecanismo. No se reescribieron narración ni claims. El JSON fue releído y conserva FAIL/72.

Correcciones documentales sincronizadas en ese storyboard: se sustituyó la nota que decía que ``narrative_qa`` estaba deliberadamente ausente y se actualizó ``trend_source.note``; no se modificó la narración. El DOI ``10.1038/s41467-026-79465-x`` está registrado como ``VERIFICADO_CROSSREF`` por la investigación previa; no se hizo una nueva consulta Crossref en este run. El proyecto no tiene ``slot_cesta``; no está seleccionado ni promovido.

### Cruce de slots con main

``main/data/tt_fb_alineacion_2026-11-22.json`` y ``main/data/publicaciones.json`` muestran ocupación real/programada que bloquea tres slots:

- 07:00: Salem, YouTube ``N21TIYdONZo``, público; TikTok y Facebook publicados. Conflicto con Voyager.
- 13:30: Gutenberg, YouTube ``YXndoPSSeaY``, TikTok y Facebook programados. Conflicto con Bao. Además, ``main/proyectos/2026-11-22_pulsar-criptografia/programacion.json`` declara 13:30, pero registra ``yt_programado=false``, ``mp4=false`` y privacidad ``private``: discrepancia adicional del mismo slot, no resuelta.
- 17:00: Ada, YouTube ``Sc0cX9ejxuw``, TikTok y Facebook programados. Conflicto con Yubarta, aunque su QA narrativo sea PASS.
- 23:30: no aparece publicación coincidente en main para el 22-nov; el borrador de genética no puede ocuparlo porque su QA es FAIL/72.

Bao comparte el DOI ``10.1038/s41586-026-11221-z`` y el tema de estrella dentro de estrella con el proyecto del 19-nov; queda señalado como duplicación temática interdiaria. El DOI de Bao continúa ``PENDIENTE_RESOLVEDOR``. No se promovió ninguno de los cuatro.

### Lote obligatorio 5–7 noviembre: relectura estructural

Los doce ``project_id``, ``fecha_objetivo``, ``slot_local`` y ``slot_cesta`` coinciden con los doce registros de ``data/horario_semana_2026-11-01_07.json``. El slot 7-nov 17:45 corresponde a ``2026-11-07_inter-nubes-pesan``. El storyboard canónico ``2026-11-05_inter-arboles-se-comunican`` sí trata redes micorrícicas y Karst et al. 2023; no hay desajuste de tema. ``2026-11-05_inter-arboles-mito-respiran`` es otra variante en bloqueados y no se confundió con el canónico.

Se conservan los QA narrativos existentes sin repetir la lectura: Venus PASS/88; Arena cantante PASS/94; Palomitas FAIL/82; Árboles FAIL/78; Rayo globular FAIL/81; Ballena FAIL/80; Aguacate FAIL/79; Ranas FAIL/83; Huesos FAIL/82; Hielo caliente FAIL/81; Pulpo FAIL/72; Nubes FAIL/78. Los dos PASS no son promovibles por estructura.

Conteo estático exacto: 85 escenas en los doce storyboards. Faltan en las 85 escenas los seis campos exigidos por la compuerta: ``dramatic_beat``, ``scene_function``, ``causal_bridge_from_previous``, ``question_state``, ``reason_to_continue`` y ``new_information`` (**510 campos ausentes**). Además, 75 escenas tienen ``sfx=[]``, que el validador actual trata como campo vacío (**75 fallos adicionales; 585 valores requeridos ausentes en total**). La voz, prompt_base y referencias de fuentes sí están presentes; hay mapas y capas de dato. ``approved_assets=[]``, render ``NOT_GENERATED`` y no hay rutas de medios. No se ejecutó el validador local; la estructura bloquea incluso a Venus y Arena. En ``2026-11-07_inter-pulpo-suenos``, el tema coincide, pero la fuente citada corresponde a *Octopus laqueus*, no a *Octopus insularis*: desajuste de especie/fuente que no se debe convertir en un desajuste de slot.

### Backlog interdiario y CI

- ``2026-11-18_dato-catorce-campos-hidrotermales``: el JSON actual ya contiene FAIL/68, cuatro flags y ``estado=BORRADOR_PENDIENTE_QA_NARRATIVA``; ``ESTADO_EJECUCION.md`` está corregido a ``BORRADOR_EN_PROYECTOS_NO_APTO_PARA_PROMOCION``. No se repitió su QA.
- Kuroshio conserva PASS/90. Se verificó una ejecución posterior que faltaba en el estado documental: workflow run ``44951621909``, job ``136990599397``, commit ``ed8659ec7184d51cdd84d3575a5ac57c1595ce2c``, resultado SUCCESS. Comando exacto: ``python scripts/validar_storyboard.py proyectos/2026-11-18_dato-kuroshio-puente-atmosferico/storyboard.json``; log ``OK``, salida 0; el segundo paso concluyó ``Expediente textual íntegro; medios no generados; publicación no autorizada.``. Los blobs de storyboard, validador y workflow coinciden con la rama actual. **No** se usó ``--check-doi``; el DOI ``10.1038/s41561-026-02139-2`` sigue ``PENDIENTE_RESOLVEDOR``. Se actualizó ``ESTADO_EJECUCION.md``; el estado sigue no apto.
- Los QA anteriores de 19–21-nov y 23-nov se conservaron; no se repitieron porque no se identificó cambio de narración. El inventario auditado sigue siendo 26 proyectos: **9 PASS / 17 FAIL / 0 pendientes**. El proyecto futuro 23-nov no se cuenta como proyecto del día actual.

### Cola, dispatch y recepción

Relectura del árbol: 89 storyboards en proyectos; **cero** JSON planos en ``cola/entrada/*.json``; un único paquete anidado ``cola/entrada/2026-11-09_dato-robot-ensambla-orbita/storyboard.json``; cero archivos en ``cola/estado/``; un marker en ``handoffs/grok_inbox/2026-11-09_dato-robot-ensambla-orbita.json``. No hay carpetas ``salidas/`` para los cuatro proyectos del 22-nov ni para el robot.

``capcot-grok-dispatch.yml`` escucha ``cola/entrada/*.json`` y su selector de ``workflow_dispatch`` usa profundidad 1. Por tanto, el paquete robot anidado es ``NOT_DISPATCHABLE_POR_SELECTOR``; los cuatro proyectos del 22-nov y los doce del lote 5–7 son ``NOT_DISPATCHABLE`` porque solo están en ``proyectos/``. No se creó ninguna copia de cola. El marker robot dice ``pending``; solo acredita escritura del marker, no lectura por Grok.

Para los 26 storyboards del alcance y el robot, ``cola/estado/<project_id>.json`` no existe: **27 ``RECEPCION_GROK_NO_CONFIRMADA``**. No se creó ni modificó ningún estado.

``scripts/procesar_cola.py`` recorre tanto JSON planos como ``*/storyboard.json`` y compara el prefijo de fecha con ``--fecha``; por defecto usa la fecha CDMX actual y no selecciona historia anterior automáticamente. Sin embargo, permite sobrescribir ``--fecha`` con una fecha histórica: la restricción a hoy es el comportamiento predeterminado, no una prohibición absoluta del CLI.

Corrección respecto del addendum del 20-nov: la versión actual de ``scripts/registro_editorial.py`` **sí** recorre ``handoffs/grok_inbox/`` con ``rglob("*.json")``, además de proyectos, entrada, bloqueados y salidas. El registro ahora descubre markers, pero no los convierte en recibos Grok.

### Producción preexistente del robot — no redispatch

En ``main/cola/entrada/2026-11-09_dato-robot-ensambla-orbita/`` se verificaron realmente ``capsula.mp4`` (25,795,339 bytes), portada, nueve frames, subtítulos, ``metadata.json``, ``programacion.json`` y ``qa.json``. QA audiovisual: 21/21, duración medida 87.57 s. YouTube ``ZG4iQgmWrLI``; ``publish_at=2026-11-22T01:00:00Z``, programado para 21-nov 19:00 CDMX. TikTok y Facebook figuran programados, pero sus IDs son null. Discrepancia: ``metadata.json`` conserva ``privacyStatus=private``, mientras ``programacion.json`` dice ``private→público`` y ``estado=programado``; no se verificó el estado público real. No existe ``salidas/<id>/``. Clasificación: ``PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR``; medios verificados en main, no en feature. No cancelar ni redispatchar.

### Datos, estilos y rotación

Main es la referencia de ocupación: 52 publicaciones, 39 registros de rotación y 32 estilos usados. Los snapshots feature tienen 22 publicaciones, 27 rotaciones y 21 estilos, por lo que no son autoridad para disponibilidad. ``temas_del_dia.json`` sigue limitado a 24–28 oct; ``horarios.json`` está actualizado al 9-nov; ``vistas_historico.json`` y ``balances_6h.json`` llegan a 28-oct; ``tendencias_estilos.json`` llega a 31-oct. ``data/cola.json`` conserva un registro fallido del 31-oct. ``endscreens_rotacion.json`` se actualizó el 22-nov 14:30, pero es rotación de end screens, no selección editorial. Ningún ``data/*.json`` fue modificado.

En la rotación main, ``art_deco_poster`` aparece el 17 y 19-nov (repetición reciente para Bao); ``risografia`` aparece el 27-oct y 17-nov (Voyager); ``tatuaje_acuarela`` aparece el 24-oct (Yubarta); ``papel_stop_motion`` no aparece en los 39 registros ni en los 32 estilos usados, aunque sí existe en el catálogo. No se certifica unicidad a partir de los snapshots feature atrasados.

``historial_youtube.json`` no está presente en el árbol consultado. Los snapshots antiguos conservan algunos ``yt_id_historial``; no se intentó borrar ni cancelar IDs externos.

### Pull requests y Actions

- PR #3: OPEN/DRAFT, base ``main``, 697 archivos, +81,195/-1,697, ``mergeable=false``, ``mergeable_state=dirty``. Es la rama operativa, pero no está integrada.
- PR #14: OPEN hacia ``main``; modifica storyboard y ledger, añade ``asset_filename`` a las ocho escenas, conserva QA histórico FAIL/82 y no aporta ejecución ``--check-doi``. Rechazado como preproducción bajo el contrato actual.
- PR #15: OPEN hacia feature; modifica solo ``scripts/validar_storyboard.py`` y su test. La propuesta de hardening no está integrada: el validador actual sigue en blob ``50335bb6``, mientras el head del PR ofrece ``a52a2f46``. Run Semgrep ``45004335607`` FAILURE; log literal: ``Findings: 26 (26 blocking)`` y ``Process completed with exit code 1.``. No se encontró ejecución de sus pruebas unitarias.
- PR #4: OPEN; solo cambia el estado del robot para decir que los nueve frames permanecen en la conversación Grok. El propio diff reconoce que ``frames/`` está vacío en GitHub; no equivale a subida ni recepción.
- PR #6: OPEN; añade ``.github/workflows/supervisor.yml`` para todos los pushes/PR y ``secrets: inherit``; no integrar sin revisión de seguridad.
- PR #13: OPEN hacia main; solo añade el informe de auditoría de cuásares. PR #7–9: dependabot, actualizaciones de acciones. Ningún PR se fusionó.
- Último run de dispatch accesible: ``41306776689``, 1-nov, FAILURE; error literal: ``Falta configurar GROK_WEBHOOK_URL.``. Es una ejecución histórica con una versión anterior del workflow. La versión actual trata el webhook como opcional y escribe marker; no hay run reciente que pruebe entrega. ``GROK_WEBHOOK_URL`` y ``GROK_WEBHOOK_TOKEN`` no se verificaron; no se consultaron ni registraron valores.
- No hubo revisión de cambios de API porque no se identificó un cambio oficial nuevo que justificara abrir esa compuerta.

### Cambios documentales de este corte

- ``proyectos/2026-11-22_genes-estatura-etapas/storyboard.json``: QA independiente FAIL/72 y sincronización de las notas de estado; narración y claims intactos.
- ``docs/briefs/2026-11-22_RADAR_CAPCOT.md``: addendum que sustituye la nota de QA pendiente.
- ``proyectos/2026-11-18_dato-kuroshio-puente-atmosferico/ESTADO_EJECUCION.md``: run #11 y corrección de obsolescencia; estructura PASS, DOI aún bloqueante.
- Este control: addendum de cierre, con scores y estados cotejados contra JSON releídos.

No se promovió ni redispatchó contenido. No se dispararon workflows ni se enviaron payloads. No se generaron imágenes, frames, voz, audio, video ni renders; no se publicó, no se consumieron créditos, no se modificaron ``data/*.json``, main, secretos, permisos ni workflows.


## Reconciliación de resubidas y etiquetas de IA — 22-nov-2026, 20:02 CDMX

**Fuentes de solo lectura en `main`:** `data/resubidas_2026-11-21.json`, `data/resubidas_2026-11-21/upload_resultado.json`, `data/tt_fb_alineacion_2026-11-22.json`, `data/publicaciones.json`, `data/vistas_historico.json` y `data/miniaturas_auditoria_2026-11-21.json`. No se modificó ningún `data/*.json`.

- **Cleopatra ES — riesgo de etiqueta IA antes del horario registrado.** El nuevo YouTube ID `I8n_5nnUlbI` figura `private` con `publishAt=2026-11-23T03:00:00Z`, equivalente a **22-nov 21:00 CDMX**. TikTok `7710997085197192466` y Facebook `1473122701620334` también figuran programados a las 21:00. El snapshot marca `tt_etiqueta_ia=true`, pero `fb_etiqueta_ia=false`; para YouTube, `containsSyntheticMedia` aparece `null` en el resultado de carga y el registro mantiene pendiente la confirmación en Studio de «Uso de IA = Sí». **Riesgo: etiquetado de IA inconsistente entre plataformas**. No se cambió programación, privacidad ni etiquetas. El original inglés `m8VAsrbfsbE` sigue público y sin cambios.
- **Oxoboranos ES.** `B-75KkHAVDo` tenía `publishAt=2026-11-22T20:30:00Z` (14:30 CDMX), hora ya transcurrida al corte. El snapshot de carga conserva `privacyStatus=private`; `vistas_historico.json` no contiene ese ID y no hay una lectura posterior a la hora programada. Estado correcto: `ESTADO_POST_PUBLICACION_NO_VERIFICADO`; no afirmar que se publicó ni que falló.
- **Rosetta — conflicto de biodiversidad confirmado.** YouTube `p5PM4xZfDyc` figura programado para `2026-11-23T19:30:00Z` (**13:30 CDMX**). Confirma el conflicto con `2026-11-23_tropical-biodiversity-turnover`, cuyo `slot_local=13:30`. Se mantiene `CONFLICTO_DE_SLOT_ENTRE_RAMAS`; no promover ni redispatchar.
- **Corrección de estado de fuentes del proyecto de biodiversidad.** La relectura del JSON muestra `SRC-001` y `SRC-002` como `VERIFICADO_FUENTE_PRIMARIA`; `SRC-001` tiene URL editorial verificada pero `doi_verification_status=PENDIENTE_RESOLVEDOR`; `SRC-002` tiene DOI visible/verificado en la página editorial de Biogeosciences y solo aporta un localizador regional, no coordenadas de parcelas. La mención previa `SRC-002=PENDING_SOURCE` no describe el estado actual de esa fuente. La compuerta DOI pendiente corresponde a `SRC-001`; no se ejecutó `--check-doi` ni se acreditó Crossref en este corte.

No se consultaron ni alteraron secretos. No se publicaron, cancelaron, reprogramaron ni editaron etiquetas; se deja la verificación manual de Studio como acción pendiente de la cuenta propietaria.

## Reintento RSS/Trends y respaldo oficial — 22-nov-2026, 20:02 CDMX

Se reintentó la lectura de los **10 feeds** declarados en `scripts/tendencias.py` y Google Trends RSS México. La apertura de los endpoints desde esta sesión no entregó XML utilizable:

- ScienceDaily science, health y space: `400 Unsupported content-type: application/xml`.
- Phys.org: `400 Unsupported content-type: text/xml`.
- NASA: `400 Unsupported content-type: application/rss+xml`.
- ESA Space Science: `404 Not Found`.
- Nature: `400 Unsupported content-type: application/rss+xml`.
- UNAM Global: `400 Unsupported content-type: application/rss+xml`.
- Google Trends RSS México, EurekAlert y SINC: `URL ... is not accessible via this tool`.

Este corte fue una relectura de endpoints mediante el navegador de la sesión; **no se ejecutó** `scripts/tendencias.py`. El corte anterior del mismo día documentó la ejecución HTTP directa y su error literal `URLError: <urlopen error [Errno -3] Temporary failure in name resolution>`. No se interpretó el fallo de feeds como ausencia de noticias. Se conservan como respaldo los cinco candidatos ya documentados en `2026-11-22_RADAR_CAPCOT.md` (NASA Photojournal, NASA Earth Observatory, NASA Science/Science Advances, Nature y Senckenberg/ZooKeys), con sus estados de duplicación, mapa o Crossref; no se inventó un sexto candidato ni se abrió un storyboard nuevo.

La reconciliación de main mantiene ocupados los slots regulares del 23–28-nov; el proyecto de biodiversidad del 23-nov 13:30 colisiona con Rosetta. La enana blanca propuesta para el 23-nov 14:30 sigue bloqueada por ausencia de MP4. No se creó paquete adicional ni se generaron medios.

## Revisión viva de PR #15 y Actions — 22-nov-2026, 20:02 CDMX

- PR #15 sigue `OPEN`, sin merge, con head `30101e9aca8aaafb8d1894df30574a66067ff4a8` sobre base `d30814995de642e3b6100d19d968115264a3d690`; GitHub lo marca `mergeable=true`. El diff endurece `check_doi` con host HTTPS fijo y rechaza booleanos en coordenadas/bounds de mapas.
- **Defecto detectado por inspección estática del test:** el mock `Connection.__init__(self, host, timeout)` no acepta `context`, pero el código productivo crea `HTTPSConnection(..., timeout=20, context=ssl.create_default_context())`. Si se ejecuta `test_check_doi_uses_fixed_https_host`, el mock puede fallar con `TypeError` por argumento inesperado `context`. No se afirma ejecución de pytest: el conector no ofrece runtime local y el intento de clonar el repositorio terminó con `Could not resolve host: github.com`.
- Para el head del PR, el único workflow PR recuperado fue Semgrep `45004335607`, `completed/failure`; no apareció una ejecución de pruebas unitarias.
- En la rama de trabajo, el run Semgrep `45048155842` terminó `failure` con `Process completed with exit code 1.`; Gitleaks `45048155922` terminó `success`; el trabajador `45050940152` terminó `success`, pero su log dice literalmente `[trabajador] sin trabajo en cola.`.

No se editó PR #15, no se dispararon workflows, no se hizo merge ni se modificó main. La corrección mínima pendiente del test es aceptar/validar el argumento `context` del constructor simulado y ejecutar la suite en un runner autorizado.

## Reconsulta de RSS/Trends y publicaciones post-hora — 22-nov-2026, 22:01 CDMX

### RSS científicos y respaldo de Trends

Se reintentó la lectura de los diez endpoints declarados en `scripts/tendencias.py` mediante el navegador de esta sesión. Los errores exactos fueron:

- ScienceDaily science, health y space: `400 Unsupported content-type: application/xml`.
- Phys.org: `400 Unsupported content-type: text/xml`.
- NASA News Release: `400 Unsupported content-type: application/rss+xml`.
- ESA Space Science: `404 Not Found`.
- Nature RSS: `400 Unsupported content-type: application/rss+xml`.
- EurekAlert y SINC: `URL ... is not accessible via this tool`.
- UNAM Global: `400 Unsupported content-type: application/rss+xml`.

Google Trends RSS México devolvió `URL https://trends.google.com/trending/rss?geo=MX is not accessible via this tool`. Se usó como respaldo la página oficial Trending Now México: https://trends.google.com/trending?geo=MX&hl=es-419. El resultado expuso 258 tendencias; entre las señales no deportivas aparecen «desierto de Atacama» (1K+, activa hace 8 h), «superluna» (2K+, activa hace 13 h), «folclore» (20K+, activa hace 21 h) y «mercado navideño» (20K+, activa hace 23 h). La mayoría de las primeras posiciones corresponde a deportes y entretenimiento; ninguna tendencia aporta por sí sola una afirmación científica ni una fuente primaria.

La página oficial de NASA Science para el 22-nov-2026 enumera el APOD «Swirls and Colors on Jupiter from Juno» y la pieza conmemorativa «65 Years of Human Spaceflight at NASA Johnson». No se encontró en ese corte una noticia/hallazgo científico publicado el mismo día con fuente primaria apta para el slot 23:30. APOD y aniversario no se convierten en hallazgo nuevo. Resultado: `PENDING_SOURCE`; no se creó storyboard adicional ni se adelantó una noticia.

### Reconciliación después de los horarios programados

A las 22:01 CDMX ya habían transcurrido los horarios de Oxoboranos (14:30) y Cleopatra (21:00). La evidencia disponible sigue siendo de programación/subida previa, no una lectura posterior a la hora:

- YouTube Oxoboranos `B-75KkHAVDo`: `main/data/resubidas_2026-11-21.json` y su `upload_resultado.json` conservan `privacyStatus=private` y `publishAt=2026-11-22T20:30:00Z`. No se obtuvo lectura de Studio/API posterior a las 14:30.
- YouTube Cleopatra `I8n_5nnUlbI`: el registro de subida conserva `privacyStatus=private`, `publishAt=2026-11-23T03:00:00Z` y `containsSyntheticMedia=null`. No se obtuvo lectura de Studio/API posterior a las 21:00.
- TikTok Cleopatra `7710997085197192466` y Facebook `1473122701620334` figuran programados a las 21:00 en `main/data/tt_fb_alineacion_2026-11-22.json`; la etiqueta IA figura activa en TikTok y desactivada en Facebook. No hay lectura post-hora de ambas plataformas.
- `main/data/publicaciones.json` conserva el registro de Cleopatra con `publishAt`, pero no prueba estado público actual. No se encontró el ID `B-75KkHAVDo` entre sus 52 registros; queda discrepancia entre el registro de resubida y el índice central de publicaciones.

Los intentos de búsqueda pública por los IDs no devolvieron resultados indexados; esto tampoco demuestra que no se hayan publicado. Estado para ambos paquetes: `PUBLICACION_POST_HORA_NO_VERIFICADA`. No se cambió privacidad, etiqueta de IA, programación ni registro de publicación. No se creó ni modificó estado Grok, no se redispatchó, no se publicó y no se consumieron créditos.

Este corte es una auditoría documental posterior al horario; la verificación definitiva requiere una lectura post-hora en Studio/API por el titular. No se atribuye a esta sesión una confirmación de publicación.


### Corrección de autoridad documental — 22-nov-2026

`ajustes_entre_modelos/PARA_CHATGPT_dato_del_dia.md` conservaba instrucciones históricas incompatibles con la ficha maestra actual: entrega directa en `cola/entrada/`, creación de estado y marca `PREPARADO`. Se añadió un addendum de autoridad en commit `a8df6a33eaf6a380062ddf73cbf399aeb9c8646a`; lectura de vuelta verificada, blob `a614252ff3b6624eb1b2da485cfb617c30f604f8`. El investigador queda limitado a `proyectos/`; la promoción queda reservada al auditor después de todas las compuertas. El commit lleva `[skip ci]`; la consulta de estado devolvió cero workflow runs y cero checks. No se tocó `data/*.json`, cola ni estados Grok.


La advertencia de autoridad también quedó colocada al inicio de `ajustes_entre_modelos/PARA_CHATGPT_dato_del_dia.md` para que preceda a los briefs históricos: commit `a1c1a4fa24ac9e1433365cb0230907ed9f8474e2`, lectura de vuelta verificada, blob `cb8b87030e38ce81683f855f4d054e4dab6242a8`. `[skip ci]`; consulta posterior: cero workflow runs y cero checks.

## Errata y actualización posterior — 2026-11-23 00:57 CDMX

- La colisión de 23-nov 07:00 no está documentada en `data/resubidas_2026-11-21.md`; la fuente correcta es `data/miniaturas_auditoria_2026-11-21.json`, campo `colisiones_horario_mismo_publishAt`, con `IQEU2Bqy3v0` y `tmOji99zGPE` compartiendo `publishAt=2026-11-23T13:00:00Z`.
- El mismo snapshot de main registra Rosetta `p5PM4xZfDyc` a 13:30, Pirámides `gWJxoGjWQeM` a 17:00 y Gutenberg `i3SpxSQglm4` a 19:00. Por tanto, el borrador tropical de feature a 13:30 sí tiene `CONFLICTO_DE_SLOT_ENTRE_RAMAS`; la ausencia de una fila en `data/publicaciones.json` no basta para declarar libre el slot.
- El inventario main consultado en este run tiene 52 registros en `data/publicaciones.json`, 39 en `data/rotacion.json`, 32 en `data/estilos_usados.json`, 5 en `data/temas_del_dia.json` (última fecha visible 28-oct) y 36 registros en `data/miniaturas_auditoria_2026-11-21.json`. `data/vistas_historico.json` conserva 108 registros; el último corte visible es 22-nov 13:50. `data/cierre_diario/2026-11-22.md` contiene un corte separado de 23:21.
- Los 12 IDs del lote 5–7 nov siguen con QA 2 PASS/10 FAIL y todos sus `cola/estado/<id>.json` devuelven 404 (`RECEPCION_GROK_NO_CONFIRMADA`). Nueve de los doce tienen video_id en la evidencia main (ocho en el snapshot de miniaturas y uno adicional en publicaciones); los tres sin video_id son Rayo globular, Aguacate negro y Pulpo sueños. No redispatchar los nueve con producción preexistente; los tres restantes siguen FAIL y no tienen entrada plana.
- `data/rehechos_2026-11-22.json` contiene nueve reworks programados para 25–29 nov. Los registros incluyen `yt_id`/`publishAt` y rutas de medios bajo `/workspace/capcot_main`, pero las carpetas correspondientes en Git solo contienen storyboard y `render.log`; no se verificaron MP4/portadas en el árbol. Clasificación: `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR` + `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`.
- El storyboard 23-nov de supersequías recibió QA narrativo independiente FAIL 82/100, flag `STAKES_NO_EXPLICADOS`; DOI/resolvedor y cifra 139/234 siguen pendientes. El borrador tropical 23-nov sigue FAIL 82 y además tiene conflicto 13:30 con Rosetta. Ninguno se promovió.
- La entrada heredada 9-nov del robot conserva QA PASS 90, pero main contiene MP4, portada, nueve frames, QA y programación con `publishAt` 21-nov 19:00; el metadata sigue `privacyStatus=private` y el estado Grok individual devuelve 404. Se clasifica `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`; publicación real no confirmada.
- La entrada main `2026-11-22_pulsar-criptografia` carece de `narrative_qa`, fecha/slot y estado Grok; tiene 146 palabras y `export.filename` pero no MP4/portada en el árbol. `NOT_DISPATCHABLE` y `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`. Main permanece solo lectura.
- El RSS/Trends ejecutado desde runtime temporal falló por DNS en los diez feeds científicos y Google Trends RSS México: `<urlopen error [Errno -3] Temporary failure in name resolution>`. El Crossref API para el DOI de supersequías falló con el mismo error. Se usaron páginas editoriales primarias como respaldo; no se escribió en `data/*.json`.
