# Control de cola y auditoría CAPCOT — 23 de noviembre de 2026

Inicio de revisión: 00:57 CDMX; cierre de auditoría: 01:23 CDMX. Rama de trabajo: `feature/capcot-video-discovery-continuity`. `main` se consultó solo en lectura. Este registro contiene cambios y verificaciones de este run; no autoriza dispatch, publicación ni producción de medios.

## Resultado material del run

- `proyectos/2026-11-23_supersequias-722-eventos/storyboard.json`: se añadió `narrative_qa` en una revisión independiente de solo narración. Resultado FAIL 82/100; siete checks true; `critical_flags=[STAKES_NO_EXPLICADOS]`. La narración no explica qué consecuencia concreta vuelve importante reconocer una supersequía. No se reescribieron narración ni claims.
- `docs/briefs/2026-11-23_RADAR_CAPCOT.md`: corregidas las ocupaciones de slots, la fuente de la colisión 07:00, el candidato de glaciares y los errores reales de RSS/Trends. El borrador supersequías queda no apto para promoción.
- `docs/briefs/2026-11-22_CONTROL_COLA.md`: añadida errata verificable para corregir el origen de la colisión y actualizar el inventario posterior.
- Lectura de vuelta confirmada para los tres archivos modificados. No se modificó `data/*.json`, `main`, `cola/entrada`, `cola/estado`, medios ni publicaciones.

## Inventario de proyectos y QA

### Proyectos 18–23 nov en feature

| Proyecto | QA actual | Escenas / palabras | Decisión de auditoría |
|---|---:|---:|---|
| `2026-11-18_dato-catorce-campos-hidrotermales` | PASS 90 | 8 / 196 | Conservar PASS; no repetir |
| `2026-11-18_dato-kuroshio-puente-atmosferico` | PASS 90 | 8 / 206 | PASS previo; DOI/resolvedor no se revalida en este run |
| `2026-11-19_dato-dia-luz-dos-manos-oro-poroso` | PASS 88 | 8 / 194 | Conservar PASS; no repetir |
| `2026-11-19_dato-estrella-dentro-de-estrella` | PASS 87 | 8 / 188 | Conservar PASS; no repetir |
| `2026-11-20_dato-dia-atlantico-humedad-sapropeles` | PASS 91 | 8 / 214 | Conservar PASS; no repetir |
| `2026-11-20_dato-marea-cerebral-en-sueno` | FAIL 82 | 8 / 202 | No promover |
| `2026-11-21_fentale-metano-sin-erupcion` | FAIL 82 | 8 / 198 | No promover |
| `2026-11-21_homo-erectus-selva-tropical` | FAIL 86 | 8 / 203 | No promover; flags vigentes |
| `2026-11-21_pulsar-gamma-reticulo` | FAIL 86 | 8 / 203 | No promover; flags vigentes |
| `2026-11-22_bao-estrella-fusion-andromeda` | FAIL 84 | 8 / 213 | No promover |
| `2026-11-22_genes-estatura-etapas` | FAIL 72 | 8 / 231 | No promover |
| `2026-11-22_voyager-1-un-dia-luz` | FAIL 83 | 8 / 206 | No promover |
| `2026-11-22_yubarta-genoma-soplo` | PASS 92 | 8 / 220 | Conservar PASS; no repetir |
| `2026-11-23_supersequias-722-eventos` | FAIL 82 | 8 / 220 | No promover; DOI y cifra 139/234 pendientes |
| `2026-11-23_tropical-biodiversity-turnover` | FAIL 82 | 8 / 218 | No promover; conflicto de slot 13:30 con main |

Los quince proyectos anteriores se consultaron individualmente en `proyectos/`. Sus quince archivos `cola/estado/<project_id>.json` devuelven 404: `RECEPCION_GROK_NO_CONFIRMADA`. No se creó ni modificó ningún estado Grok.

### Lote 5–7 nov: 12 IDs requeridos

- QA vigente: 2 PASS y 10 FAIL. No se repitió QA PASS ni se modificó ninguna narración.
- Los doce estados `cola/estado/<project_id>.json` devuelven 404: `RECEPCION_GROK_NO_CONFIRMADA`.
- Nueve de los doce tienen video_id en la evidencia de main; se clasifican `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`: `2026-11-05_kids-dia-en-venus` (`phVfyHp3CnY`), `2026-11-05_comida-palomitas` (`zTP5akrGA9M`), `2026-11-05_inter-arboles-se-comunican` (`EX0W3q-yKRw`), `2026-11-06_kids-ballena-azul-corazon` (`wbFrlM2e_YE`), `2026-11-06_inter-ranas-congeladas` (`UBFuKBU3cx0`), `2026-11-06_inter-arena-cantante` (`m4RqQRaz55k`), `2026-11-07_comida-hielo-caliente` (`HSgrnejAcaI`), `2026-11-07_inter-nubes-pesan` (`4Qpl17Ts_vI`) y `2026-11-07_kids-huesos-bebe` (`uEsoscBrfgU`).
- Los tres sin video_id confirmado son `2026-11-05_inter-rayo-globular`, `2026-11-06_comida-aguacate-negro` y `2026-11-07_inter-pulpo-suenos`; continúan FAIL, sin entrada plana y sin autorización para promover.
- No se reejecutaron workflows ni se redispatchó ningún ID antiguo.

## Slots 23 nov — main frente a feature

| Slot CDMX | Evidencia main | Evidencia feature | Clasificación |
|---|---|---|---|
| 07:00 | `IQEU2Bqy3v0` y `tmOji99zGPE` comparten `publishAt=2026-11-23T13:00:00Z` en `data/miniaturas_auditoria_2026-11-21.json` | Sin proyecto asignado | `COLISION_PUBLISHAT`; no tocar |
| 13:30 | Rosetta `p5PM4xZfDyc` en el mismo snapshot | `2026-11-23_tropical-biodiversity-turnover` | `CONFLICTO_DE_SLOT_ENTRE_RAMAS`; no promover |
| 17:00 | Pirámides `gWJxoGjWQeM` | Sin proyecto asignado | `OCUPADO_EN_MAIN` |
| 19:00 | Gutenberg `i3SpxSQglm4` | Sin proyecto asignado | `OCUPADO_EN_MAIN` |
| 23:30 | Sin ocupación en el snapshot main disponible | `2026-11-23_supersequias-722-eventos` | `OCUPADO_EN_FEATURE`; no redispatch |

No se verificó YouTube Studio externo. El snapshot de miniaturas es evidencia de programación registrada, no una lectura en vivo de Studio.

## Cola, Grok, dispatch y producción preexistente

- `proyectos/` feature contiene los quince storyboards 18–23 nov indicados arriba. `cola/entrada/` feature contiene solo el `.gitkeep` y la entrada heredada anidada del 9-nov; no hay JSON plano de los proyectos 18–23. `salidas/` feature no contiene salidas 18–23 nov.
- `cola/bloqueados/` conserva copias heredadas de los IDs 5–7 nov; no se modificaron.
- `handoffs/grok_inbox/` contiene un marcador del robot del 9-nov. Un marcador GitHub no demuestra recepción Grok.
- `capcot-grok-dispatch.yml` dispara por `cola/entrada/*.json` y selecciona con `find -maxdepth 1`; no recoge la entrada anidada. `scripts/procesar_cola.py` contempla JSON planos y `cola/entrada/*/storyboard.json`, por lo que hay discrepancia de profundidad entre procesador y workflow. No se modificó ni disparó el workflow.
- El último run de dispatch disponible es del 1-nov y terminó FAILURE sin jobs/logs recuperables. No hay dispatch reciente en los runs consultados. La validación CI disponible más reciente es de Kuroshio, no de los proyectos 23-nov, y no ejecuta `--check-doi`.
- Entrada heredada `cola/entrada/2026-11-09_dato-robot-ensambla-orbita`: conserva QA PASS 90 histórico. La relectura de main muestra `proyectos/<id>/` con `storyboard.json` y `fuentes.md`; no aparece `salidas/<id>/` (404), `frames/` en feature contiene solo `.gitkeep` y `main/salidas/` no contiene una salida identificable del robot. `main/data/publicaciones.json` registra `yt_id=ZG4iQgmWrLI` y `publishAt` para 21-nov 19:00 CDMX, pero ese registro no verifica que MP4/portada/nueve frames estén presentes ni confirma publicación efectiva. `cola/estado/<id>.json` devuelve 404. Clasificación: `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR` + `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO` + `RECEPCION_GROK_NO_CONFIRMADA`. No cancelar ni duplicar.
- Entrada main `2026-11-22_pulsar-criptografia`: anidada, sin `narrative_qa`, sin fecha/slot y sin estado Grok; 7 escenas, 146 palabras, `export.filename` declarado, pero no hay MP4/portada en el árbol. `NOT_DISPATCHABLE` y `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`. Main se mantuvo solo lectura.

## Producción preexistente 25–29 nov

`data/rehechos_2026-11-22.json` contiene nueve reworks con `yt_id`/`publishAt` y rutas locales bajo `/workspace/capcot_main`. Las carpetas correspondientes en Git contienen storyboard y `render.log`, pero no MP4/portadas verificables. Clasificación para los nueve: `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR` + `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`. No se canceló ni modificó programación.

## Datos, rotación y fuentes

| Fuente main | Estado leído |
|---|---|
| `data/publicaciones.json` | 52 registros |
| `data/rotacion.json` | 39 registros; último registro visible 21-nov |
| `data/estilos_usados.json` | 32 registros; `collage_cientifico_vintage` no aparece en la rotación reciente |
| `data/temas_del_dia.json` | 5 entradas; última fecha visible 28-oct; snapshot desactualizado |
| `data/miniaturas_auditoria_2026-11-21.json` | 36 registros; 6 colisiones; incluye la programación 23-nov 07:00/13:30/17:00/19:00 |
| `data/vistas_historico.json` | 108 registros; último corte visible 22-nov 13:50 |
| `data/cierre_diario/2026-11-22.md` | Corte separado 22-nov 23:21 |
| `data/cola.json` | Vacío |

No se encontró un archivo `historial_youtube` dedicado en el árbol consultado; se usaron los registros disponibles de publicaciones, miniaturas, vistas y cierre diario. Los archivos `data/*.json` permanecen sin cambios.

### RSS, Trends y Crossref

- Se ejecutó el contenido vigente de `scripts/tendencias.py` en runtime temporal. Los diez feeds científicos definidos (ScienceDaily general, salud y espacio; Phys.org; NASA; ESA; Nature; EurekAlert; SINC; UNAM Global) y Google Trends RSS México fallaron con `<urlopen error [Errno -3] Temporary failure in name resolution>`. No se escribió JSON.
- Respaldo oficial: Nature Scientific Data (supersequías y esponjas), Scientific Reports (tilapia), Nature Climate Change (glaciares-lagos) y PLOS Biology (Varroa). Se mantiene un shortlist de cinco candidatos; tilapia queda `NO_DUPLICAR`, esponjas `PENDING_MAP_COORDINATES`, glaciares candidato futuro, Varroa candidato futuro. W2246-0526 queda `PENDING_SOURCE` porque no se encontró página primaria para DOI `10.1126/sciadv.aek9035`.
- Crossref API para `10.1038/s41597-026-08886-6` falló con `URLError: <urlopen error [Errno -3] Temporary failure in name resolution>`. La página editorial Nature muestra el DOI, pero el resolvedor no quedó verificado. La cifra 139/234 (59.4%) no se confirmó en el texto primario accesible y queda `PENDING_SOURCE`.
- Se intentó clonar el repositorio para ejecutar `scripts/validar_storyboard.py` localmente; `git clone` falló con `Could not resolve host: github.com`. No se disparó CI. Se hizo inspección estructural manual, que no sustituye el validador real.

## Decisiones de cierre

- No promover supersequías: QA FAIL 82, DOI/resolvedor pendiente, cifra 139/234 sin confirmación accesible y validador estructural real no ejecutado.
- No promover tropical: QA FAIL 82 y `CONFLICTO_DE_SLOT_ENTRE_RAMAS` a 13:30.
- No redispatchar robot 9-nov, lote 5–7 nov ni los nueve reworks 25–29 nov.
- No modificar main, `data/*.json`, estados Grok, secretos, permisos, workflow, medios ni decisiones editoriales.
- Siguiente paso mínimo: el investigador debe revisar stakes y la cifra 139/234 en supersequías sin que auditoría reescriba la narración; después ejecutar validador estructural y resolver DOI. Tropical requiere decisión editorial de slot, no una promoción automática.
## Commits y verificación de cierre

- Rama feature HEAD inmediatamente antes del registro de cierre: `aaf3ec57d49a4c72a1c5a31dbd3d5c60d3db20b2`; este registro de cierre quedó en `10958969d5c8f79924f7a64b3c11238cefa15a3f`.
- Main HEAD consultado, sin escritura: `c371aec46595b092d0b4d2f74ac38670e8897754`.
- `4abdb6c8594860abad18228ae29ee2e00c261e0d`: única adición de `narrative_qa` FAIL al storyboard de supersequías; el diff confirma que la narración y el resto del storyboard no cambiaron.
- `2cdbc50f0f1a0ee7ac116e0b680c86836f006f3b` y `a283f8796ba1f80a9d0ad89d8d7fe21c7b1fb0b2`: corrección del radar y actualización de compuertas.
- `9541695801d060e1c21b3b50a84e237c2435d04c`: errata de inventario/programación en el control del 22-nov.
- `aaf3ec57d49a4c72a1c5a31dbd3d5c60d3db20b2`: creación de este control del 23-nov.
- `10958969d5c8f79924f7a64b3c11238cefa15a3f`: registro de commits y verificación final.
- Lecturas de vuelta verificadas para storyboard, radar, control del 22-nov y este control. Después de estos commits no apareció un nuevo run de Actions; el último run disponible sigue siendo la validación de Kuroshio `45075532329` sobre un commit anterior, sin `--check-doi`.
- La ejecución RSS se hizo desde una copia temporal del contenido de `scripts/tendencias.py` leído de GitHub; el repositorio no se clonó por el error DNS. No se escribió ningún resultado temporal al repositorio.

## Revalidación del operador — 2026-11-23 01:56 CDMX

### Inventario, cola y recepción

- La rama feature estaba en `6182055130d0c00d78950c3e063110b6e86adca2` al comenzar esta revalidación. El único cambio de storyboard no ocurrió: el commit posterior a este control anterior solo había tocado el propio control. Los proyectos 20–23 fueron releídos; no apareció un proyecto del 24-nov.
- Los 12 proyectos del lote 5–7 nov fueron releídos. Sus `cola/estado/<id>.json` siguen en 404. Hay copias heredadas en `cola/bloqueados/` para los 12 títulos, aunque varios usan un `project_id` histórico distinto al de `proyectos/`. No se movió ni borró ninguna copia. Los QA registrados en los 12 proyectos se mantienen en 2 PASS y 10 FAIL; no se reescribieron.
- Reconciliación de video IDs: `main/data/publicaciones.json` confirma dos coincidencias exactas de `project_id` dentro de esos 12: `2026-11-07_comida-hielo-caliente` (`HSgrnejAcaI`; la nota del registro indica que ya no aparecía en el canal el 12-nov, aunque TT/FB sí constaban publicados) y `2026-11-07_inter-nubes-pesan` (`4Qpl17Ts_vI`; publicación/agenda registrada). El conteo anterior de 9/12 no se pudo reproducir con los archivos actuales: `data/vistas_historico.json` contiene 108 registros sin coincidencia por esos títulos y no se encontró un archivo separado `historial_youtube` en raíz ni en `data/`. No se atribuyen otros siete video IDs sin evidencia actual.
- Para los dos proyectos del 23-nov, ambos tienen `narrative_qa=FAIL/82`, siete checks true y flag única `STAKES_NO_EXPLICADOS`. `supersequias` fue revisado el 23-nov 00:57 CDMX; `tropical-biodiversity-turnover` fue revisado el 21-nov 14:24 CDMX. Los commits posteriores de tropical cambiaron fuente/coordenadas y metadata, no la narración; no se repitió QA. El slot tropical 13:30 entra en `CONFLICTO_DE_SLOT_ENTRE_RAMAS` con main (`p5PM4xZfDyc`, `publishAt=2026-11-23T19:30:00Z`). `supersequias` 23:30 no tiene video individual en main, pero el cupo diario ya está en 5/5 por los dos videos de 07:00 y los slots 13:30, 17:00 y 19:00. Ambos siguen en `proyectos/`; `ESTADO_EJECUCION.md`, `cola/entrada`, `cola/estado` y `salidas` devuelven 404. Clasificación `NOT_DISPATCHABLE` + `RECEPCION_GROK_NO_CONFIRMADA`; no promover.
- `cola/entrada/` solo muestra la carpeta histórica `2026-11-09`; su contenido no existe en GitHub (404). `cola/estado/` y `publicaciones/` no existen en la rama. `salidas/` conserva únicamente artefactos antiguos, sin salida del 23/24-nov.
- Worker main `45126580443`: SUCCESS; el log termina en `[trabajador] sin trabajo en cola.`. No hubo procesamiento nuevo.
- `.github/workflows/capcot-grok-dispatch.yml` sigue filtrando únicamente `cola/entrada/*.json` (primer nivel); `scripts/procesar_cola.py` sí contempla profundidad adicional. La discrepancia permanece documentada; no se disparó workflow ni se envió payload.
- PR #3 permanece OPEN/DRAFT/dirty y contiene cambios en archivos `data/*.json`, que siguen siendo solo lectura. No se fusionó ni se modificó.

### Ocupación del 24-nov y radar

- `main/data/miniaturas_auditoria_2026-11-21.json` confirma cinco videos programados para el 24-nov: 07:00 `RBUcAeptGAU`, 13:30 `WtuxaKrS4-Q`, 17:00 `cGb7Z0ZEz8w` y `_YzBY4OfUeo` (misma hora/publishAt), y 19:00 `9W9nn72rmfE`.
- `scripts/rotacion.py` establece `MAX_POR_DIA=5`. El slot 23:30 no tiene video en el snapshot, pero el día ya está en 5/5; por eso no se creó storyboard. La colisión de 17:00 no se canceló ni reprogramó.
- La rotación automática no ingiere `miniaturas_auditoria_*.json`; la ocupación de videos programados debe seguir reconciliándose manualmente antes de crear un sexto paquete.
- Se creó y leyó de vuelta `docs/briefs/2026-11-24_RADAR_CAPCOT.md` (candidatos Varroa, plancton, lagos glaciares y grafito). Varroa queda recomendado, no asignado. Nature queda `PENDING_SOURCE` hasta acceso directo; grafito queda `PENDING_SOURCE`; el DOI de Varroa permanece pendiente de resolver.
- Las diez URL RSS de `scripts/tendencias.py` y Google Trends México fallaron con `curl: (6) Could not resolve host: <host>`; Crossref y `doi.org` también fallaron por DNS. Los errores exactos y el respaldo editorial están en el radar.
- No se creó storyboard, `narrative_qa`, entrada de cola, estado Grok, medio ni placeholder. No se leyeron valores de secretos.

### Límites de esta revalidación

No se cambió `data/*.json`, main, programación, publicaciones, bloqueados, estados Grok, secretos ni permisos. El siguiente paso es esperar un slot que esté libre tanto por fecha/hora como por cupo diario, y volver a resolver DOI antes de cualquier promoción.

### Commits y lectura de vuelta de esta revalidación

- `36b29c21d02c63ee6468fc13a6072ba4595830a2`: creación de `2026-11-24_RADAR_CAPCOT.md`.
- `30987a394651cfe974f22ef96a8b124348169d02`, `b2946e1d38737e7b806cc345b14a4bbb8553ff7b` y `46ae529355d98d777c3991c2c178261d2da58cdc`: correcciones sucesivas para separar acceso a fuente primaria, estado PENDING_SOURCE y DOI pendiente.
- `63d54fbc0f3726bb0e3fa9b6beba4aecadbd15b3`: actualización de este control. El radar y el control se releen desde GitHub; los hashes de contenido se comprobaron en la respuesta de lectura de vuelta.
- No hubo cambios de storyboard ni de `data/*.json` en estos commits.


## Revalidación adicional — 23-nov-2026, 04:02 CDMX

### Proyectos y lote 5–7 nov

- Se releyeron los doce storyboards canónicos del lote 5–7 nov. Se mantienen **2 PASS y 10 FAIL**; no se repitió ninguna revisión PASS ni se alteró la narración.
- Los doce `cola/estado/<project_id>.json` devolvieron HTTP 404. Clasificación para cada uno: `RECEPCION_GROK_NO_CONFIRMADA`.
- La evidencia de `main/data/publicaciones.json` y `main/data/miniaturas_auditoria_2026-11-21.json` volvió a confirmar nueve IDs de video ya procesados/programados. Los tres sin video ID confirmado —rayo globular, aguacate negro y pulpos— no aparecen por título en esos registros. Ninguno se promovió ni redispatchó.
- `cola/bloqueados/` conserva doce copias planas. Nueve tienen además carpeta anidada con `storyboard.json`, `fuentes.md` y `ESTADO_EJECUCION.md`; los nueve estados Markdown ya dicen `BORRADOR_EN_PROYECTOS_NO_APTO_PARA_PROMOCION`, pero sus JSON heredados aún dicen `PENDIENTE_REVISION_GROK` y no contienen `narrative_qa`. Se conserva la discrepancia, sin mover ni editar copias bloqueadas. Tres IDs solo tienen copia plana.
- La comparación de commits desde el control anterior hasta el HEAD previo mostró únicamente cambios en este archivo de control; no hubo modificación de storyboards posteriores a la auditoría del 01:23 CDMX.

### Entrada anidada del robot — 9 nov

- Relectura de `cola/entrada/2026-11-09_dato-robot-ensambla-orbita/storyboard.json`: conserva QA PASS histórico y estado de publicación pendiente de decisión Grok.
- `cola/estado/2026-11-09_dato-robot-ensambla-orbita.json` devuelve HTTP 404: `RECEPCION_GROK_NO_CONFIRMADA`.
- La carpeta `frames/` contiene únicamente `.gitkeep`. La carpeta `salidas/2026-11-09_dato-robot-ensambla-orbita/` no existe en main (404). La fila de `main/data/publicaciones.json` sí conserva YouTube ID `ZG4iQgmWrLI`, con programación registrada para el 21-nov-2026 a las 19:00 CDMX.
- Clasificación: `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR` + `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`. Además, la entrada está anidada y el workflow solo acepta `cola/entrada/*.json` en primer nivel; por la ruta actual es `NOT_DISPATCHABLE`. No se disparó el workflow ni se envió payload.

### Cupo futuro y radar del 25 nov

- `scripts/rotacion.py` mantiene `MAX_POR_DIA=5`. Corrección del conteo por colisiones de `publishAt`: **25-nov suma 7/5**, no 6/5. El snapshot contiene cinco videos: 07:00 `cPNiOFeY5_k` y `W9g2tPZTpD4` (colisión), 13:30 `G1ByWhjfxls`, 17:00 `L6ggmPAwBOA` y 19:00 `A3JK0gYuqG8`; se agregan los reworks 10:00 `9RxTSifAcpo` y 15:00 `3rwo_sK1e18`. **26–28 nov también suman 7/5 cada día**: cinco videos del snapshot más dos reworks; las colisiones omitidas en el conteo anterior son 26-nov 17:00 `-1DRh_qj7Bg`, 27-nov 07:00 `nd0rs6iVy8E` y 28-nov 17:00 `fcSNbU809ao`. El 29-nov suma 5/5. No hay cupo autorizable para storyboard del 25 al 29-nov. No se cancela ni reprograma nada. Las fuentes siguen siendo `main/data/miniaturas_auditoria_2026-11-21.json` y `main/data/rehechos_2026-11-22.json`; ambos permanecen solo lectura.
- Se creó `docs/briefs/2026-11-25_RADAR_CAPCOT.md` con cinco candidatos primarios recientes: Varroa/hipoxia, Norma arm, plancton, lagos glaciares y Pantoea/quinoa. Varroa queda como primera recomendación de investigación, no como selección.
- La apertura directa de los diez RSS definidos en `scripts/tendencias.py` devolvió errores de tipo de contenido, 404, redirección a IDP o URL no accesible; Google Trends RSS tampoco abrió. La página HTML oficial de Trends México sí abrió (277 tendencias, 25 visibles), sin tendencia pertinente para ciencia/naturaleza/cocina/cuerpo/espacio. No se afirma que el script se haya ejecutado.
- Crossref REST y resolvedores DOI no devolvieron una verificación reproducible. Los DOI de los candidatos siguen `PENDIENTE_RESOLVEDOR`; los candidatos cuyo texto completo no se pudo leer siguen `PENDING_SOURCE`. No se creó storyboard, QA, entrada, estado Grok ni medio.

### Issue #11 — cuásares

- Issue #11 continúa abierto con etiqueta `hecho`. PR #12 está cerrado sin merge; PR #13 sigue abierto y sin merge. El informe externo de Groq en PR #13 inspecciona el storyboard completo y su metadata, por lo que no acredita la compuerta estricta de lectura en frío de narración concatenada.
- No hay `cola/estado`, entrada, salida ni registro de publicación para `2026-11-15_dato-quasar-pareja-cosmic-dawn`.
- **EJECUTADO y VERIFICADO:** se actualizó únicamente la compuerta del storyboard: `narrative_qa.status=FAIL`, `score=0`, `review_basis=lectura_en_frio_solo_narracion`, siete checks explícitos no acreditados y `critical_flags=[REVISION_INDEPENDIENTE_AUSENTE]`. El estado quedó `BORRADOR_EN_PROYECTOS_NO_APTO_PARA_PROMOCION`. La revisión de esta sesión es de ChatGPT y no se presenta como independiente; el informe de Groq no cumple el método de solo narración. Lectura de vuelta confirmó que la narración y los claims permanecen idénticos. No se modificó el issue ni los PRs.

### Límites y acciones no ejecutadas

No se modificaron `data/*.json`, main, `cola/entrada`, `cola/estado`, bloqueados, programación, publicaciones, workflows, secretos ni permisos. No se leyeron valores de `GROK_WEBHOOK_URL` ni `GROK_WEBHOOK_TOKEN`; su presencia no se infiere. No se generaron medios ni se consumieron créditos.


**Control histórico del PR #13:** la revisión de integración del 17-nov (comentario del propietario en el PR) ya había advertido que el informe Groq confunde duración de escena con aparición temporal del dato, no fija SHA reproducible, mezcla DOI pendiente con fuente inexistente y no demuestra varias transiciones. La instrucción explícita fue no aprobar ni fusionar y exigir reauditoría sobre el SHA exacto. Esa advertencia sigue vigente; no se aprobó ni fusionó el PR.


### CI posterior a las actualizaciones

- Los runs automáticos de PR #3 para los commits `721789a`, `359a5cf` y `d478f44` terminaron `success` en CodeQL. Esto acredita únicamente esos jobs de análisis; no acredita validador estructural, DOI/Crossref ni QA audiovisual.
- PR #3 permanece abierto, Draft y `mergeable=false`. No se marcó listo ni se fusionó.
- No aparece un run nuevo de `capcot-grok-dispatch`; los commits tocaron storyboard de proyecto y documentos, no `cola/entrada/*.json`.


## Auditoría de backlog adicional — Issue #11 (cuásares) — 23-nov-2026

- Issue #11 sigue OPEN con etiqueta `hecho` y 10 comentarios. PR #13 sigue OPEN/NOT MERGED; PR #12 está CLOSED/NOT MERGED.
- El artefacto `AUDITORIA.md` de la rama `trabajador/11`, generado por Groq gpt-oss-120b, inspecciona el storyboard completo: título, escenas, fuentes, metadata y líneas del JSON. No es una lectura en frío de la narración concatenada con título, resumen, arco, notas y `narrative_contract` ocultos; por tanto, no satisface la compuerta narrativa vigente.
- El storyboard canónico conserva `narrative_qa.status=FAIL`, score 0, `reviewer_role=control_compuerta_chatgpt_no_independiente` y `critical_flags=[\"REVISION_INDEPENDIENTE_AUSENTE\"]`. Los siete checks false significan que no están acreditados por una auditoría válida, no un dictamen individual de fallo narrativo.
- `cola/entrada/<id>`, `cola/estado/<id>.json` y `salidas/<id>` devuelven 404; `main/data/publicaciones.json` no tiene coincidencia por ese `project_id`. Clasificación: `NOT_DISPATCHABLE`; no se promovió ni se redispatchó.
- No se disparó el worker, no se envió payload, no se modificó la etiqueta del Issue ni se alteró el estado de los PRs.


## Verificación de Actions de capcot-grok-dispatch — 23-nov-2026

- Se leyó `.github/workflows/capcot-grok-dispatch.yml`; su ruta de entrada de `push` observa `cola/entrada/*.json`. Los commits de esta revisión tocaron únicamente `docs/briefs/*.md`; no se modificó cola ni se lanzó el workflow.
- La consulta de historial por GitHub Fetch devolvió literalmente `INVALID_ARGUMENT 400: GitHub Fetch URL is not an allowed public GitHub repository or search endpoint`. La apertura de la página de Actions devolvió `DisabledError`. Por ello, el listado completo de ejecuciones recientes de ese workflow queda **no verificado por el conector**; no se afirma que no existan runs.
- No se envió payload, no se inspeccionaron valores de secretos y no se infirió recepción Grok a partir de commits o Actions.


## Relectura y correcciones verificadas — 23-nov-2026, 06:23 CDMX

### Fuente de verdad de QA: 15 storyboards del 18–23 nov

La relectura de los 15 JSON encontró que la tabla anterior de este control tenía varios scores distintos de los almacenados en los storyboards. Para evitar conservar un reporte contradictorio, los valores vigentes de `narrative_qa` son:

| Project ID | QA vigente en storyboard |
|---|---:|
| `2026-11-18_dato-catorce-campos-hidrotermales` | FAIL / 68 |
| `2026-11-18_dato-kuroshio-puente-atmosferico` | PASS / 90 |
| `2026-11-19_dato-dia-luz-dos-manos-oro-poroso` | PASS / 91 |
| `2026-11-19_dato-estrella-dentro-de-estrella` | PASS / 90 |
| `2026-11-20_dato-dia-atlantico-humedad-sapropeles` | PASS / 91 |
| `2026-11-20_dato-marea-cerebral-en-sueno` | FAIL / 82 |
| `2026-11-21_fentale-metano-sin-erupcion` | PASS / 90 |
| `2026-11-21_homo-erectus-selva-tropical` | FAIL / 83 |
| `2026-11-21_pulsar-gamma-reticulo` | FAIL / 83 |
| `2026-11-22_bao-estrella-fusion-andromeda` | FAIL / 84 |
| `2026-11-22_genes-estatura-etapas` | FAIL / 72 |
| `2026-11-22_voyager-1-un-dia-luz` | FAIL / 83 |
| `2026-11-22_yubarta-genoma-soplo` | PASS / 90 |
| `2026-11-23_supersequias-722-eventos` | FAIL / 82 |
| `2026-11-23_tropical-biodiversity-turnover` | FAIL / 82 |

Se corrigió únicamente el QA de `2026-11-20_dato-marea-cerebral-en-sueno`: el JSON contenía PASS/92 sin `reviewed_at`, mientras la revisión anterior de este control registraba FAIL/82. Se realizó una nueva lectura en frío de la narración concatenada, sin usar título, resumen, arco, notas ni `narrative_contract`. Resultado: FAIL/82, siete checks verdaderos y `critical_flags=[STAKES_NO_EXPLICADOS]`. La consecuencia concreta de la diferencia por edad para el funcionamiento o la salud no queda explicada. Se comparó la narración antes/después y permaneció idéntica. Solo cambió `narrative_qa`; commit `39e6566aedeab236284f905bf796bfe1872aff45`, blob leído de vuelta `b751a2dc413ba8c607f8fe7fe89e264632d4945f`.

No se repitieron los demás QA ya registrados ni se reescribieron narraciones o claims. Los dos `ESTADO_EJECUCION.md` presentes para el 18-nov ya dicen `BORRADOR_EN_PROYECTOS_NO_APTO_PARA_PROMOCION`; no requieren corrección. No hay `ESTADO_EJECUCION.md` para los otros trece proyectos.

### Recepción, cola y producción

- Los 15 archivos `cola/estado/<project_id>.json` de los proyectos 18–23 devolvieron 404; se conserva `RECEPCION_GROK_NO_CONFIRMADA` para cada uno.
- Los 12 archivos `cola/estado/<project_id>.json` del lote 5–7 nov también devolvieron 404: 12/12 sin acuse individual.
- El árbol vigente no contiene el directorio `cola/estado/`, JSON plano actual en `cola/entrada/` ni salidas de los proyectos 18–23. La única entrada heredada es el paquete anidado del 9-nov; no satisface el selector de `cola/entrada/*.json`.
- El workflow `capcot-grok-dispatch.yml` solo selecciona JSON planos en el nivel superior de `cola/entrada/`. No se disparó workflow ni se envió payload. No se consultaron valores de secretos ni se afirmó que falten.

### Lote interdiario de 12 IDs — relectura de los storyboards

| Project ID | QA vigente |
|---|---:|
| `2026-11-05_kids-dia-en-venus` | PASS / 88 |
| `2026-11-05_comida-palomitas` | FAIL / 82 |
| `2026-11-05_inter-arboles-se-comunican` | FAIL / 78 |
| `2026-11-05_inter-rayo-globular` | FAIL / 81 |
| `2026-11-06_kids-ballena-azul-corazon` | FAIL / 80 |
| `2026-11-06_comida-aguacate-negro` | FAIL / 79 |
| `2026-11-06_inter-arena-cantante` | PASS / 94 |
| `2026-11-06_inter-ranas-congeladas` | FAIL / 83 |
| `2026-11-07_comida-hielo-caliente` | FAIL / 81 |
| `2026-11-07_inter-nubes-pesan` | FAIL / 78 |
| `2026-11-07_inter-pulpo-suenos` | FAIL / 72 |
| `2026-11-07_kids-huesos-bebe` | FAIL / 82 |

El lote suma 85 escenas. Las seis propiedades narrativas obligatorias `dramatic_beat`, `scene_function`, `causal_bridge_from_previous`, `question_state`, `reason_to_continue` y `new_information` faltan en todas las escenas: 510 ausencias. No se reabrió ningún slot pasado.

Nueve video_id antiguos aparecen en los registros/snapshots de main: `zTP5akrGA9M`, `EX0W3q-yKRw`, `phVfyHp3CnY`, `m4RqQRaz55k`, `UBFuKBU3cx0`, `wbFrlM2e_YE`, `HSgrnejAcaI`, `4Qpl17Ts_vI` y `uEsoscBrfgU`. Tres proyectos no tienen video_id en `publicaciones.json`, `miniaturas_auditoria_2026-11-21.json` ni `rehechos_2026-11-22.json`: rayo globular, aguacate negro y pulpo-sueños. La ausencia de video_id no habilita redispatch: sus slots ya pasaron y sus QA son FAIL.

### Programación preexistente de main y corrección del auditor de snapshots

El snapshot de main `data/miniaturas_auditoria_2026-11-21.json` contiene seis grupos explícitos de colisión en `colisiones_horario_mismo_publishAt[].videos[]`:

| Fecha / slot CDMX | IDs que comparten publishAt |
|---|---|
| 23-nov 07:00 | `IQEU2Bqy3v0`, `tmOji99zGPE` |
| 24-nov 17:00 | `cGb7Z0ZEz8w`, `_YzBY4OfUeo` |
| 25-nov 07:00 | `cPNiOFeY5_k`, `W9g2tPZTpD4` |
| 26-nov 17:00 | `JqlKsJOVmdE`, `-1DRh_qj7Bg` |
| 27-nov 07:00 | `jiX6RdwJ1gg`, `nd0rs6iVy8E` |
| 28-nov 17:00 | `gN6svdqe62Q`, `fcSNbU809ao` |

Además, `data/rehechos_2026-11-22.json` registra nueve reworks con video_id y publishAt entre el 25 y el 29-nov. Sus rutas declaradas apuntan a `/workspace/capcot_main/proyectos/.../capsula.mp4` y `portada.jpg`; el árbol Git contiene storyboard, metadata, créditos, licencias y `render.log`, pero no esos MP4/JPG. Se marca `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`; los video_id y publishAt bastan para bloquear cualquier redispatch. No se canceló ni movió ninguna programación.

La relectura detectó un defecto real en `scripts/auditar_snapshots_programacion.py`: solo consumía `siguen_mal_sin_mp4_no_se_invento` y `rehechos_*.json`, omitiendo los grupos de colisión explícitos anteriores. Eso dejaba fuera publicaciones programadas que no pertenecen a la lista de medios faltantes. Se corrigió el parser para leer `colisiones_horario_mismo_publishAt[].videos[]`, producir una ocupación por video y deduplicar contra registros de la lista anterior. Se añadieron pruebas para el esquema real y la deduplicación:

- Script: commit `39844689a604b8da71614b2547a7dcb85470754d`; lectura de vuelta confirmada.
- Tests: commit `28e10cb03958ce2cd90ee63fd9f4da72cd55acd8`; lectura de vuelta confirmó las dos pruebas nuevas.
- La suite no se ejecutó en esta sesión. CodeQL de los commits del script y tests terminó en success; eso no equivale a unittest. El workflow semanal `capcot-descubrimiento.yml` ejecuta `python -m unittest discover -s tests -p 'test_*.py' -v` los lunes a las 14:30 UTC (08:30 CDMX); no se disparó manualmente.

Los radars 24 y 25 ya registran el cupo lleno; el snapshot también muestra ocupaciones/collisiones hasta el 29-nov. No se creó storyboard adicional ni se promovió el borrador de 23:30. `supersequias` y `tropical` siguen FAIL/82; el primero conserva DOI/resolvedor pendiente y el segundo tiene conflicto de slot con Rosetta en main. No hay slot libre confirmado.

### Ingesta y cierre

La relectura de RSS y Google Trends, con errores exactos y respaldo editorial primario, quedó añadida al radar 23-nov (commit `be49b2e3bb2124a7b4fdb942b0724724886ad831`). Google Trends HTML mostró 274 tendencias, 25 visibles; no se encontró tema científico/natural utilizable en esa primera página. Cuatro páginas primarias recientes (PLOS Biology, Nature Astronomy, Nature Communications y Nature Climate Change) mostraron sus DOI, pero Crossref y `doi.org` no fueron accesibles; los cuatro permanecen `PENDIENTE_RESOLVEDOR`. No se asignó candidato a un slot.

**Resultado del corte:** QA y recepción revalidados; marea corregido a FAIL82 sin tocar narración; auditor de snapshots corregido y probado por lectura de vuelta; ningún proyecto actual es promocionable; ningún workflow ni publicación se ejecutó.


## CI y asignaciones reconsultadas — 23-nov-2026, 06:23 CDMX

- Semgrep de **main**, run `45117327158`, commit `c371aec`: FAILURE, 361 reglas sobre 1.103 archivos, **34 findings**. El paso de carga SARIF quedó `skipped`; el log no expone el detalle de reglas/ubicaciones y no se atribuyen esos hallazgos a la rama feature. Gitleaks de ese commit: SUCCESS (`45117327157`). No se modificó main.
- Worker de cola main, run `45126580443`: SUCCESS; salida literal `[trabajador] sin trabajo en cola.`. Callback, run `45142865312`: SUCCESS; no se encontraron Issues abiertos con etiqueta `callback`. No se disparó manualmente ninguno de los workflows.
- CodeQL de la rama feature: SUCCESS en los commits `3984468`, `28e10cb`, `39e6566`, `be49b2e` y `13b4faf`. La suite de tests de CAPCOT no se ejecutó en este corte; el workflow semanal de descubrimiento está programado para el lunes 14:30 UTC y no se adelantó.
- `ajustes_entre_modelos/LEDGER_ASIGNACIONES.md` conserva `CUASARES-AUDITORIA` en cola para auditor distinto de ChatGPT, `GROK-RECEPCION` bloqueado y `MIGRACION-ACUSE` pendiente.
- Issue #11 sigue OPEN con etiqueta `hecho`, sin assignee; PR #13 sigue OPEN. El informe de PR #13 inspecciona el storyboard completo, no solo la narración concatenada. El JSON vigente conserva `narrative_qa=FAIL/0`, `review_basis=lectura_en_frio_solo_narracion` y `critical_flags=[REVISION_INDEPENDIENTE_AUSENTE]`. No se cerró el Issue ni se cambió la etiqueta.
- El tablero `ajustes_entre_modelos/DELEGACIONES.md` conserva pendientes antiguos de Mpemba, Barreleye, seguridad, cuenta Clayzo y backlog inglés. El callback no creó Issues nuevos; no se duplicó ni se reasignó trabajo.

No hay evidencia de un dispatch de Grok en la ventana reciente de Actions. Con `cola/entrada/` sin JSON plano, el selector no tiene paquete que despachar. No se leyeron secretos ni se escribieron estados Grok.


## Revalidación de ocupación en main — 2026-11-23, 07:58 CDMX

**Fuente de verdad consultada en solo lectura:** main HEAD `20fa76409a620d909d690d3c04a87bb34f4b42c6` (commit de programación TT+FB); `data/publicaciones.json` blob `774e3b7022c910d5b1b1d3f86a4590df0ee5847d`; `data/tt_fb_alineacion_2026-11-23.json` blob `3d44386a12298ee06b222ccabfaefb65fe61a6e8`.

- El registro de alineación de main contiene **8 horarios CDMX distintos y 10 video_id del día**: 07:00, 09:00, 11:00, 13:30, 17:00, 19:00, 21:00 y 23:30. Los horarios 07:00 y 17:00 tienen dos IDs cada uno. Esto supera el límite documentado de cinco cápsulas diarias; se registra como **CAPACIDAD_5_DIA_SUPERADA_EN_MAIN** (observación de programación, no afirmación de que todos los videos estén ya públicos).
- 09:00 Bernabé, 11:00 Evémero y 17:00 Mitra aparecen en `publicaciones.json` con `publishAt` y programación TT/FB. El mismo snapshot de alineación también registra Rosetta 13:30, Pirámides 17:00, Gutenberg 19:00, Ley Juárez 21:00 y Oso Wojtek 23:30 como IDs de YouTube sin MP4 local ni TT/FB verificados.
- Para cualquier paquete que coincida con esos horarios se aplica **PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR**. Los medios de los cinco registros YT sin MP4 local quedan **MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO**.
- `2026-11-23_tropical-biodiversity-turnover` (13:30) mantiene **CONFLICTO_DE_SLOT_ENTRE_RAMAS** con Rosetta en main. `2026-11-23_supersequias-722-eventos` (23:30) pasa de “sin ocupación observada” a **CONFLICTO_DE_SLOT_ENTRE_RAMAS** con Oso Wojtek en main. Esta corrección supersede la observación anterior de disponibilidad 23:30.
- Lectura de vuelta de ambos storyboards: siguen `BORRADOR_EN_PROYECTOS_NO_APTO_PARA_PROMOCION`, `narrative_qa=FAIL/82`, siete checks true y `STAKES_NO_EXPLICADOS`; no se repitió QA porque la narración no cambió. Ambos `cola/estado/<project_id>.json` y ambos `ESTADO_EJECUCION.md` devolvieron 404; se conserva `RECEPCION_GROK_NO_CONFIRMADA`. Clasificación: **NOT_DISPATCHABLE**.
- No se modificó main ni `data/*.json`; no se disparó workflow, no se envió payload y no se tocó programación externa.


## Revalidación de PR y CI — 2026-11-23, corte posterior

- Rama feature HEAD verificada tras las dos actualizaciones de este control: `7be3e48f79404589e68eb4f6f1467c4d6b683ddb`. Los dos commits de esta ejecución modificaron únicamente este control y el radar; no tocaron storyboards ni `data/*.json`.
- PR #15 continúa OPEN y no mergeable. Su último Semgrep registrado, run `45004335607`, terminó FAILURE; el propio expediente registra 27 hallazgos. Las pruebas unitarias del cambio de coordenadas/DOI siguen pendientes, por lo que no se declara PASS.
- PR #3 continúa OPEN/DRAFT y no mergeable, con base `main`; su diff todavía contiene cambios a `data/*.json`, que siguen fuera de alcance de escritura. No se integró ni se modificó.
- El último run de Actions visible en la rama feature sigue siendo la validación estructural Kuroshio `45075532329` (SUCCESS) sobre un commit anterior; no valida estos cambios de documentación ni acredita DOI. No apareció un run de `capcot-grok-dispatch.yml`; no hubo dispatch.
- No se abrió/cerró/actualizó ningún PR, no se dispararon workflows y no se leyeron secretos.


## Revisión adicional de rotación de end screens en main — 2026-11-23, 08:07 CDMX

Main avanzó a `b85fcb0e117955def516790393a989d7d78cc93b`; el commit modificó únicamente `data/endscreens_rotacion.json` (blob `c985d2f509b6e55f2004a824c488d609fc2646de`). No cambió `publicaciones.json` ni la alineación horaria ya auditada.

- El snapshot `snapshot_2026-11-23_08` y la propuesta correspondiente están guardados, pero `pendiente_studio=true` y la propuesta tiene estado `pendiente_studio`: no prueban que Studio haya aplicado el cambio.
- **DISCREPANCIA DE REGISTRO:** el campo `motivo` afirma que el video `5XQfUHpyTWs` tiene 46 vistas y carece de pantalla final; el snapshot del mismo archivo registra 989 vistas para ese ID y `aplicado_studio` lo marca como aplicado el 28-oct-2026 hacia `5D96DmjvioU`. No se corrige `data/*.json`; queda como discrepancia de metadatos que requiere verificación en Studio.
- No afecta los ocho horarios del día ya contabilizados. No se cambió main, el JSON ni la propuesta; no se ejecutó ninguna acción en Studio.
