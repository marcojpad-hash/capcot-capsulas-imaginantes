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


### Corrección de atribución de Semgrep — PR #15

Precisión sobre la sección anterior: los **27 hallazgos** pertenecen al run Semgrep `45004241269` citado en el cuerpo del PR. La consulta del head actual `30101e9aca8aaafb8d1894df30574a66067ff4a8` devuelve además el run `45004335607` con conclusión FAILURE, pero no se verificó en sus logs el mismo conteo. No se atribuyen los 27 hallazgos al run más reciente. Las pruebas unitarias del PR siguen pendientes.


## Reauditoría de borrador modificado después del último corte — marea cerebral

El commit `39e6566aedeab236284f905bf796bfe1872aff45` del 23-nov modificó solo `narrative_qa` de `proyectos/2026-11-20_dato-marea-cerebral-en-sueno/storyboard.json`; no cambió narración ni claims. El QA independiente ahora queda **FAIL/82**, `review_basis=lectura_en_frio_solo_narracion`, reviewer `auditor_capcot_independiente`, flag `STAKES_NO_EXPLICADOS`. No se repitió la lectura en frío porque el texto narrado no cambió.

- Slot: 2026-11-20 17:00. El `data/publicaciones.json` actual de main contiene para esa fecha solo 07:00 y 13:30; no se encontró registro main a 17:00 ni colisión de `publishAt` en el snapshot disponible. No se declara `CONFLICTO_DE_SLOT_ENTRE_RAMAS` para este proyecto.
- Lectura de vuelta: 84 s, 8 escenas, `approved_assets=[]`, `export.render_status=NOT_GENERATED`, publicación pendiente. `cola/estado/2026-11-20_dato-marea-cerebral-en-sueno.json` y `ESTADO_EJECUCION.md` devolvieron 404; **RECEPCION_GROK_NO_CONFIRMADA**. Clasificación: **NOT_DISPATCHABLE** por QA FAIL y ausencia de recepción confirmada.
- No se modificó el storyboard, no se reescribió narración, no se promovió a cola y no se generaron medios.


## Reauditoría posterior — 2026-11-23, 09:55 CDMX

### Cambios posteriores al corte anterior

- La rama feature avanzó a `083a59abd3ceac9f81ce3751a69b73621cb09cca` (09:44 CDMX). Ese commit modifica únicamente `data/endscreens_rotacion.json`: reasigna la pantalla final de `4Vi_TnIl9FI` a `41PYjWbQuJo`, con `actualizado_cdmx=09:40` y `pendiente_studio=false`. **DISCREPANCIA DE POLÍTICA:** `data/*.json` está definido como solo lectura. Se conserva el commit observado; este operador no editó, revirtió ni volvió a aplicar la acción de Studio.
- El commit anterior `66b0aac` modificó únicamente este radar. No hay cambio de narración en los dos storyboards del 23-nov ni en los doce IDs del lote 5–7 nov.

### Auditoría de los dos proyectos del 23-nov

- Lectura de vuelta de `2026-11-23_supersequias-722-eventos`: 220 palabras concatenadas, 8 escenas, 84 s totales; voz `es-MX-JorgeNeural`, rate +7 %, pitch -2 Hz; `approved_assets=[]`, `export.render_status=NOT_GENERATED`, publicación pendiente y sin rutas de medios.
- Lectura de vuelta de `2026-11-23_tropical-biodiversity-turnover`: 171 palabras, 8 escenas, 84 s; misma configuración de voz y controles de medios.
- Ambos conservan `narrative_qa=FAIL/82`, `review_basis=lectura_en_frio_solo_narracion`, reviewer `auditor_capcot_independiente`, siete checks verdaderos y `critical_flags=[STAKES_NO_EXPLICADOS]`. La revisión existente sí identifica un auditor distinto; no se repitió QA porque la narración no cambió. El conteo estructural aquí es una inspección estática, no una ejecución del validador.
- Conflictos vigentes: supersequías 23:30 con Oso Wojtek en main; biodiversidad tropical 13:30 con Rosetta en main. Ambos `NOT_DISPATCHABLE`. Sus `cola/estado/<id>.json` y `ESTADO_EJECUCION.md` siguen en 404: `RECEPCION_GROK_NO_CONFIRMADA`. No se promovió copia plana ni se disparó workflow.

### Cola heredada y producción preexistente

- La entrada anidada `2026-11-09_dato-robot-ensambla-orbita` conserva QA narrativo PASS/90, pero no es redispatchable. En feature, `frames/` contiene solo `.gitkeep`; los medios no están en ese árbol. En main existe una copia con `capsula.mp4`, subtítulos, QA, metadata y `programacion.json`, además de `video_id=ZG4iQgmWrLI` y `publishAt=2026-11-22T01:00:00Z`. Se mantiene `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR` y `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO` para la copia feature. Su estado Grok individual sigue en 404. No se movió ni duplicó.
- `main/salidas/2026-11-07_comida-hielo-caliente/` conserva video, QA y registro de publicación; el lote 5–7 nov no se redispatcha. El corte previo de 12 IDs (2 PASS, 10 FAIL; nueve IDs de video en snapshots y tres sin video_id confirmado) no cambió.

### CI y producción nueva en main

- Main avanzó a `6a5de3f1bba7928ee73875ae68ede80f4e95c7c7` (09:54:59 CDMX), con cuatro variantes inglesas, sus `qa_en.json`, `render_en.log` y scripts de montaje. Los cuatro directorios no contienen `programacion.json`; se clasifican como producción/render preexistente, sin inferir un slot ni copiar/re-renderizar.
- Semgrep main run `45210561724`: FAILURE, 37 findings bloqueantes sobre 1,145 archivos; la carga SARIF quedó skipped y no se produjo artifact. No se atribuyen hallazgos a feature ni se modificó main.
- Gitleaks main run `45210561913`: SUCCESS, 1,149 archivos.
- El último CI feature sigue siendo `45075532329` (SUCCESS) y valida únicamente Kuroshio. Su comando no incluye `--check-doi`; no acredita DOI ni valida los dos storyboards del 23-nov. No hay run de `capcot-grok-dispatch.yml`. El workflow de despacho continúa limitado a JSON plano en `cola/entrada/*.json`; la raíz no contiene paquete plano.
- La página editorial de Nature para DOI `10.1038/s41597-026-08886-6` sí muestra el estudio de 722 eventos y los resultados de correspondencia publicados. Crossref API y `doi.org` siguen inaccesibles en esta verificación; el DOI permanece `PENDIENTE_RESOLVEDOR`. La cifra `139/234` no aparece en el HTML primario consultado y permanece `PENDING_SOURCE`. No se alteraron claims ni narración.

**Resultado del corte:** sin promoción, redispatch, ejecución de workflow, generación de medios ni cambio de programación. No se leyeron secretos ni valores de webhook; no se consultaron ni modificaron estados Grok.


## Revalidación de fuentes de programación entre ramas — 2026-11-23, 10:22 CDMX

Esta pasada es de solo lectura para `main` y `data/*.json`. Se registra la divergencia para evitar usar snapshots antiguos de feature como autoridad de programación.

| Fuente | main | feature/capcot-video-discovery-continuity | Resultado |
|---|---|---|---|
| `data/horarios.json` | blob `2261993d542de445df23e0abbe63bca9b54c2ff1`, actualizado 2026-11-23 | blob `550599906c26e747de71b6b962080b6bd469f23f`, actualizado 2026-11-09 | Feature no contiene la política del 23-nov |
| `data/publicaciones.json` | blob `774e3b7022c910d5b1b1d3f86a4590df0ee5847d`, tres registros del 23-nov | blob `a17dbe541d35b7e3d8a835756a06f0588039049a`, cero registros del 23-nov | Usar main para ocupación; no copiar registros |
| `data/vistas_historico.json` | blob `ce6859cae15e6b3914f7440e2fda0a43115eaf0c`, 108 registros, último corte 22-nov 13:50 | blob `ab48713b7d6f3a4604dacd606dff14817cbfb4e3`, 74 registros, último corte 28-oct 08:08 | Snapshot feature desfasado |
| `data/cierre_diario/` | 19 archivos, hasta 22-nov | solo 25, 26 y 27-oct | El cierre 22-nov citado arriba pertenece a main, no a feature |

### Programación ya existente en main

`main/data/publicaciones.json` registra tres publicaciones/programaciones del 23-nov: 09:00 CDMX, `CW02WClntYA` (Orfismo); 11:00, `Tq2ASLkFTbo` (Evemerismo); y 17:00, `6OuHVN5dbbs` (Mitraísmo). Se clasifican como **PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR**. No sustituyen ni eliminan los conflictos ya identificados para feature: 13:30 con Rosetta y 23:30 con Oso Wojtek.

La política activa de main desde 23-nov fija 06:30–07:30 y 16:30–18:00, conserva 23:30 como dato del día y evita 19:00 y 20:00–23:00. La ventana 13:00–14:30 aparece como prueba, no como ventana activa. Por tanto, el borrador tropical de 13:30 está además fuera de las ventanas activas, aparte de su conflicto con Rosetta.

### Cola y recepción

- `cola/entrada/` feature contiene `.gitkeep` y el paquete anidado `2026-11-09_dato-robot-ensambla-orbita/`; no hay JSON plano de primer nivel.
- `cola/estado/` devuelve 404 en la rama feature; no existe directorio de estados visible. Para los dos borradores del 23-nov se conserva **RECEPCION_GROK_NO_CONFIRMADA**.
- El workflow `capcot-grok-dispatch.yml` solo acepta JSON plano en `cola/entrada/*.json` por evento push; `workflow_dispatch` es otra ruta manual. El workflow tiene permisos de escritura para generar markers y no contiene una compuerta narrativa/slot equivalente a esta auditoría. No se disparó, no se envió payload y no se consultaron valores de secretos.
- El árbol no contiene un archivo dedicado `historial_youtube`; la auditoría usa `data/publicaciones.json`, snapshots de programación/miniaturas, `data/vistas_historico.json` y cierres diarios.

**Decisión:** conservar main como autoridad de ocupación, mantener los dos borradores en `proyectos/` como **NOT_DISPATCHABLE**, no copiar datos entre ramas y no modificar `data/*.json`, main, cola, estados Grok, secretos ni programación externa.

## Corrección de ocupación main para el slot 23:30 — 2026-11-23, revalidación posterior

La atribución anterior de **Oso Wojtek en main a las 23:30 del 23-nov** no se pudo reproducir y queda **RETIRADA COMO CONFLICTO_VERIFICADO**. Se conserva el antecedente histórico, pero esta lectura de las fuentes actuales lo supersede:

- `main/data/publicaciones.json` (blob `774e3b7022c910d5b1b1d3f86a4590df0ee5847d`): los registros con slot 23:30 corresponden a `2026-11-21_colon-no-llamo-america`, YT `RwTTwSNGm10`, publicado/programado el 21-nov 23:30 CDMX. No hay registro del 23-nov a las 23:30. Los tres registros del 23-nov siguen siendo 09:00, 11:00 y 17:00.
- `main/data/miniaturas_auditoria_2026-11-21.json` (blob `afc0a587025534eb5a338169383171bb0f38254c`): confirma Rosetta `p5PM4xZfDyc` a las 13:30 del 23-nov; su entrada a 23:30 corresponde a otro día.
- `main/data/horarios.json` (blob `2261993d542de445df23e0abbe63bca9b54c2ff1`): mantiene 23:30 como slot fijo del dato, pero no asigna allí un proyecto por nombre.
- El árbol recursivo actual de main no contiene rutas con `Oso` ni `Wojtek`. El único texto “El oso que aprendió a no morir” hallado en publicaciones es un placeholder antiguo del tardígrado, fechado 25-oct, sin slot 23-nov.

**Clasificación corregida:**
- `2026-11-23_supersequias-722-eventos`, 23:30: **no hay CONFLICTO_DE_SLOT_ENTRE_RAMAS verificable en main**. Permanece asignado en feature y **NOT_DISPATCHABLE** por QA FAIL/82, DOI pendiente de resolvedor, cifra 139/234 aún `PENDING_SOURCE` y `RECEPCION_GROK_NO_CONFIRMADA`.
- `2026-11-23_tropical-biodiversity-turnover`, 13:30: conserva **CONFLICTO_DE_SLOT_ENTRE_RAMAS** con Rosetta `p5PM4xZfDyc`; además 13:00–14:30 es ventana de prueba, no ventana activa de la política main del 23-nov.

No se modificó main ni `data/*.json`; no se canceló ni reprogramó ningún contenido. No se promovió ni redispatchó el borrador de supersequías.

## Reconciliación adicional de programación y Actions — 23-nov-2026, 11:59 CDMX

### Corrección de la conclusión sobre 23:30

La lectura directa de `main/data/tt_fb_alineacion_2026-11-23.json` (blob `3d44386a12298ee06b222ccabfaefb65fe61a6e8`) contradice la conclusión de que 23:30 está libre. En el bloque `hoy_en_yt_sin_mp4_local_ni_tt_fb` figura Oso Wojtek con `video_id=pTmQgkchC68` y `hora_cdmx=23:30`. Es un registro explícito de alineación de YouTube con ID y hora; la clasificación conservadora para ese slot es `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR` y `CONFLICTO_DE_SLOT_ENTRE_RAMAS` mientras el registro siga vigente. Esto **supersede** la conclusión del commit `13095a5f5ba940ee4be9e56c7eb7155cf1a81a78` que retiró el conflicto por falta de corroboración en otros archivos.

La discrepancia permanece abierta, no se convierte en una afirmación de publicación confirmada:
- `main/data/publicaciones.json` (blob `774e3b7022c910d5b1b1d3f86a4590df0ee5847d`) contiene 55 registros totales y solo tres entradas del 23-nov; no incluye `pTmQgkchC68`.
- `main/data/miniaturas_auditoria_2026-11-21.json` (blob `afc0a587025534eb5a338169383171bb0f38254c`) es un snapshot del 21-nov y no contiene Oso a las 23:30. Por ser anterior, no invalida el registro de alineación del 23-nov.
- La misma alineación y el snapshot sí identifican a Rosetta (`WtuxaKrS4-Q`) a las 13:30; el borrador `2026-11-23_tropical-biodiversity-turnover` conserva conflicto de slot con main.
- La alineación lista diez IDs de YouTube distribuidos en ocho horas locales (07:00 dos; 09:00; 11:00; 13:30; 17:00 dos; 19:00; 21:00; 23:30). No se afirma que sean diez cápsulas distintas, pero el registro excede las cinco ventanas autorizadas y no permite tratar otro slot como libre. `scripts/rotacion.py` mantiene `MAX_POR_DIA=5`.

La rama feature no contiene los snapshots `tt_fb_alineacion` ni `miniaturas_auditoria` de main; sus datos locales incluyen únicamente `endscreens_rotacion.json`, `horarios.json`, `publicaciones.json`, `reprogramacion_tt_fb_v4_2026-11-01_03.json` y `rotacion.json`. Por tanto, `registro_editorial.py`/`rotacion.py` no pueden reconciliar por sí solos esos registros de main. La verificación cruzada manual sigue siendo obligatoria antes de asignar slots.

### Estado de QA, recepción y rutas

- Los 15 storyboards del 18–23 nov conservan los estados QA de la tabla de fuente de verdad incluida en la sección «Relectura y correcciones verificadas — 06:23 CDMX»; los dos borradores del 23-nov siguen FAIL/82. Los doce IDs del lote 5–7 nov permanecen en 2 PASS y 10 FAIL. No cambió ninguna narración ni se repitió un PASS.
- El árbol actual de feature no contiene archivos en `cola/estado/`. Para los 15 proyectos recientes y los 12 IDs del lote 5–7 nov, la recepción se mantiene como `RECEPCION_GROK_NO_CONFIRMADA`.
- No hay JSON plano actual en `cola/entrada/`; permanece únicamente la entrada histórica anidada del robot del 9-nov. No hay salida nueva para los dos borradores del 23-nov.
- `proyectos/2026-11-23_supersequias-722-eventos/ESTADO_EJECUCION.md` y `fuentes.md`, y los equivalentes de biodiversidad, devuelven 404. No existe un estado `PREPARADO` que corregir. No se creó estado Grok ni entrada de cola.

### Workflow y ejecuciones observadas

- El workflow vigente de feature observa `cola/entrada/*.json` en primer nivel; su selector usa `find -maxdepth 1`. `scripts/procesar_cola.py` contempla profundidad adicional, por lo que la entrada histórica anidada sigue siendo `NOT_DISPATCHABLE`. No se disparó workflow ni se envió payload.
- El último run de dispatch observado es `#41306776689`, push del 1-nov-2026 12:29Z en feature; falló con el error literal `Falta configurar GROK_WEBHOOK_URL.` La versión actual del workflow tiene un paso de webhook opcional. No se leyeron valores de secretos y la presencia actual de esa variable queda sin verificar; el fallo histórico no se atribuye automáticamente al estado actual.
- El CI de feature `#45075532329` terminó SUCCESS para Kuroshio únicamente. Su workflow ejecuta `validar_storyboard.py` sin `--check-doi`; no valida los dos borradores actuales ni acredita DOI/Crossref.
- En main, Semgrep `#45225684539` terminó FAILURE (exit code 1); los runs recientes de CodeQL y Gitleaks terminaron SUCCESS. PR #3 continúa OPEN/DRAFT/no mergeable. PR #15 continúa OPEN/NOT MERGED; es mergeable, pero sus pruebas unitarias siguen sin evidencia de ejecución. No se modificaron PRs.
- La ejecución real del validador estructural sobre los dos borradores no se pudo completar en este entorno. Se leyó su código por GitHub; la descarga local alternativa falló por resolución DNS (`URLError: <urlopen error [Errno -3] Temporary failure in name resolution>`) y la apertura web del archivo devolvió `DisabledError`. La revisión manual de JSON no se presenta como ejecución del validador. No se usó workflow_dispatch ni se alteraron storyboards para forzar CI.

### Decisión de este run

Ambos borradores permanecen `NOT_DISPATCHABLE`: Supersequías por FAIL/82 y conflicto de 23:30 con el registro Oso en main; biodiversidad por FAIL/82 y conflicto de 13:30 con Rosetta. No se promovió, no se reescribió narración, no se modificó `data/*.json`, main, cola, estados Grok, programación, secretos ni permisos. No se generaron medios ni se consumieron créditos.

Siguiente paso mínimo: reconciliar con Imaginantes/propietario el ID Oso de 23:30 y la discrepancia del registro de publicaciones; mantener ambos slots bloqueados hasta esa confirmación y hasta que cada storyboard tenga QA PASS, validador estructural real y DOI verificado.

## Revalidación del operador único — 2026-11-23, 14:04 CDMX

### Cambios posteriores al último corte

- HEAD de partida de este corte: `94c0d04b4f708d7bddeb08d289ab9cf5476b8365`. Los commits posteriores de este run actualizaron únicamente este control; no hay storyboard nuevo ni cambio narrativo posterior al QA registrado.
- `main` releído: HEAD `01877b8764f3bea11ba0aa7a1c61b9e0721afe2a`. El commit añadió el snapshot de `data/balances_6h.json` y `data/vistas_historico.json`; no modificó la política horaria ni los registros de publicación.
- Política vigente en `main/data/horarios.json` desde 23-nov: ventanas activas 06:30–07:30 y 16:30–18:00; 23:30 es el slot fijo del dato del día. 13:00–14:30 permanece como prueba reversible; 19:00 no se programa sin autorización puntual.
- `main/data/tt_fb_alineacion_2026-11-23.json` conserva diez IDs de YouTube distribuidos en ocho horas. Entre ellos están Rosetta a las 13:30 (`p5PM4xZfDyc`) y Oso a las 23:30 (`pTmQgkchC68`). `main/data/publicaciones.json` solo contiene tres registros del día (09:00, 11:00 y 17:00); la alineación es evidencia adicional de video_id/programación, no prueba de publicación terminada.

### Dos proyectos del 23-nov

Releídos los dos storyboards sin volver a redactar ni repetir el QA:

- `2026-11-23_supersequias-722-eventos`, 23:30: 8 escenas, 220 palabras, 78 s de escenas + 6 s de cortinilla = 84 s. Voz es-MX-JorgeNeural, +7 %, −2 Hz; prompt_base coincide con `collage_cientifico_vintage`; mapa con centroides WGS84 y nota de precisión respaldados por SRC-001; 2 gráficos; todas las escenas tienen source_ids, ambiente y SFX. `approved_assets=[]`, `render_status=NOT_GENERATED`, publicación pendiente. QA existente: FAIL/82, siete checks verdaderos, `STAKES_NO_EXPLICADOS`.
- `2026-11-23_tropical-biodiversity-turnover`, 13:30: 8 escenas, 171 palabras, 78 s de escenas + 6 s de cortinilla = 84 s. Misma voz y parámetros; prompt_base coincide con `ligne_claire`; mapa WGS84 de la región de Jambi con precisión limitada explícitamente a la región publicada; 2 gráficos; source_ids, ambiente y SFX presentes en todas las escenas. `approved_assets=[]`, `render_status=NOT_GENERATED`, publicación pendiente. QA existente: FAIL/82, siete checks verdaderos, `STAKES_NO_EXPLICADOS`.
- Los dos IDs aparecen en la alineación de `main`; se clasifican `CONFLICTO_DE_SLOT_ENTRE_RAMAS` y `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`. La propia alineación los lista sin MP4 local ni espejo TT/FB: `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`.
- No se repitió el QA: ambas narraciones conservan el hash/estado de revisión documentado en el último corte. No se reescribieron claims ni narraciones.

### Cola, Grok y Actions

- Inventario de proyectos: 103 directorios; los únicos dos con fecha 23-nov son los anteriores. `cola/entrada/` solo contiene el paquete histórico anidado del robot del 09-nov; no existe JSON plano de ninguno de los dos proyectos actuales. `cola/estado/` no está presente (404): para ambos aplica exactamente `RECEPCION_GROK_NO_CONFIRMADA`.
- `salidas/` no contiene proyectos del 23–25-nov en feature ni en main. `cola/bloqueados/` conserva el backlog previo. El selector del trabajador procesa entradas planas y paquetes anidados, pero el workflow de handoff observado en la rama opera sobre JSON plano; ninguno de los dos proyectos actuales está en una ruta de entrada.
- Run `45254537410` (Trabajador de cola, main, 13:58 CDMX) terminó SUCCESS con “sin trabajo en cola”. No acredita recepción Grok ni procesamiento de la rama feature. No se observó un run reciente del workflow de dispatch; no se enviaron payloads ni se consultaron valores de secretos. La presencia actual de configuración de webhook queda **no verificada**, no declarada ausente.
- En main, run Semgrep `45255115817` terminó FAILURE: 37 hallazgos bloqueantes en 1,236 archivos; la carga SARIF se omitió tras el fallo y el log disponible no expone el detalle por regla. Gitleaks `45255115860` terminó SUCCESS. El push de main `45255114848` terminó SUCCESS. No se reejecutó ningún workflow.

### PRs, issues y datos operativos

- PR #3 sigue OPEN/DRAFT, 704 archivos, `mergeable=false`; no se integra ni se modifica desde este run.
- PR #15 sigue OPEN, `mergeable=true` pero `mergeable_state=unstable`; añade seis pruebas de coordenadas/DOI, pero no hay evidencia de ejecución de esas pruebas unitarias en su head. No se fusiona.
- La auditoría de cuásares del 15-nov ya tiene artefacto de Groq en PR #13 y corrección narrativa abierta en PR #14. El issue #11 conserva etiqueta `hecho`; no se repite una auditoría ChatGPT donde el contrato del issue exige un auditor de modelo distinto.
- Issue #4 sigue OPEN: los nueve PNG de ASTRA del 09-nov solo están documentados en la conversación de Grok; `frames/` conserva únicamente `.gitkeep` y no hay recibo de entrega. La recuperación de los originales es la única vía segura; no se recrean medios.
- Issue #6 sigue OPEN y depende del PR #62 de `agente-cero-costo` (repositorio adicional, solo lectura), que continúa OPEN. No se altera ese repositorio ni se duplica el supervisor.
- El snapshot llamado `balances_6h.json` está fechado 14:01 CDMX, pero su base comparativa es 22-nov 13:50 (24.2 h antes): no es un delta de seis horas. YouTube usa respaldo público de yt-dlp porque OAuth devolvió `invalid_grant`; faltan likes en 27/116 Shorts y comentarios en 105/116, así que 1,240 likes y 28 comentarios son sumas parciales, no totales completos. TikTok también procede del listado público yt-dlp; seguidores no disponibles. Vistas leídas: YouTube 40,009 y TikTok 38,892.
- La verificación directa de Crossref/resolvedor no se pudo completar: los endpoints DOI devolvieron “not accessible” y la búsqueda no devolvió metadatos específicos. Los storyboards marcan fuente primaria verificada, pero eso no acredita la compuerta DOI/Crossref. No se promueve ninguno.

### Resultado de este corte

**EJECUTADO:** relectura de ramas, inventario, horarios, alineación, publicaciones, cola, salidas, bloqueados, workflow, Actions, PRs, issues y estructura de los dos storyboards; actualización de esta bitácora.

**VERIFICADO:** no hay storyboard nuevo; ambos proyectos actuales siguen FAIL/82 y en conflicto de slot; no existe estado Grok individual; el trabajador no encontró entrada; no se generaron medios ni se promovió ningún paquete.

**PENDIENTE:** revisión narrativa corregida por el autor en una nueva versión; resolución Crossref/DOI; decisión de slot tras reconciliar la alineación de main; confirmación de recepción/medios por Grok/Imaginantes. No se modifica `data/*.json`, main, estados Grok, secretos, permisos, medios ni programación.


---

## RECTIFICACIÓN DE AUDITORÍA — CORTE 2026-11-23

Esta sección prevalece sobre cualquier cifra o resumen anterior de este archivo cuando exista discrepancia. Se releyeron los JSON actuales de GitHub. No se repitió QA narrativo ya registrado cuando la narración no cambió.

### Inventario, creación, objetivo y cola

- Rama auditada: `feature/capcot-video-discovery-continuity`, HEAD observado `af1584ace60d349b07eff387799e9e06b6713618`.
- Árbol `proyectos/`: **103 directorios, 90 storyboard.json y 13 directorios sin storyboard.json**. Los directorios sin storyboard no se cuentan como borradores.
- Fecha objetivo 23-nov: exactamente **2** storyboards:
  - `2026-11-23_supersequias-722-eventos`: primer commit del storyboard `2026-11-23T06:51:31Z` (00:51:31 CDMX); objetivo 23-nov; slot 23:30; `slot_cesta` ausente.
  - `2026-11-23_tropical-biodiversity-turnover`: primer commit `2026-11-21T20:21:12Z` (14:21:12 CDMX); objetivo 23-nov; slot 13:30; `slot_cesta` ausente.
- `cola/entrada/`: **cero entradas del 23-nov**, tanto planas como anidadas. Solo permanece el paquete histórico anidado `cola/entrada/2026-11-09_dato-robot-ensambla-orbita/storyboard.json`.
- Para los dos proyectos del día y para los storyboards vigentes auditados no hay archivos individuales en `cola/estado/<project_id>.json`: registrar literalmente **RECEPCION_GROK_NO_CONFIRMADA**. El marker de handoff del robot no sustituye el estado Grok.
- Los dos storyboards del 23-nov son **NOT_DISPATCHABLE**: están en `proyectos/`, no en `cola/entrada/`. El robot anidado también es **NOT_DISPATCHABLE**: el workflow escucha `cola/entrada/*.json` y su selector manual usa `find -maxdepth 1`; no alcanza `cola/entrada/<project_id>/storyboard.json`.

### QA y estructura de los dos proyectos del 23-nov

Los dos JSON conservan `narrative_qa.status=FAIL`, `score=82`, los siete checks en true y `critical_flags=["STAKES_NO_EXPLICADOS"]`. El FAIL es correcto: una bandera crítica impide PASS aunque los checks estén true. No se reescribió narración ni se repitió la lectura en frío.

| Proyecto | Escenas | Palabras | Escenas + cortinilla | Gancho | Resultado estructural estático |
|---|---:|---:|---:|---:|---|
| Supersequías | 8 | 220 | 78 + 6 = 84 s | 4 | FAIL: etiquetas de arco incompatibles con la secuencia del contrato |
| Tropical biodiversity turnover | 8 | 171 | 78 + 6 = 84 s | 5 | Sin fallo de arco observado; DOI y validador ejecutado siguen pendientes |

Ambos usan `es-MX-JorgeNeural`, tienen source_ids resolubles dentro del propio JSON, prompt_base coincidente con el catálogo, mapa y gráficos, ambiente y SFX no vacíos, `approved_assets=[]`, `export.render_status=NOT_GENERATED` y no contienen `asset_filename`, `asset_type`, nombres de exportación ni rutas de medios. El arco de Supersequías usa `hook/question/method/result/threshold/validation_examples/validation_limit/payoff`, no la secuencia contractual `hook_medias_res/desarrollo/cierre_historia/reflexion_o_pregunta`. Los DOI de ambos no tienen evidencia de una ejecución `--check-doi`; no se afirma verificación Crossref.

**Cruce con main:** el slot 23-nov 13:30 está ocupado por Rosetta (`p5PM4xZfDyc`) y el 23:30 por Oso (`pTmQgkchC68`). Son paquetes distintos, no los IDs de estos dos borradores. La alineación de main los describe sin MP4 local: **MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO**. Se clasifican ambos slots como `CONFLICTO_DE_SLOT_ENTRE_RAMAS / PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`; no se promueve ninguno.

El archivo de alineación de main registra 10 IDs en ocho ventanas; `data/publicaciones.json` solo tiene tres registros del 23-nov. Además, la nota de duplicados mueve Mitra a 18:00, pero `programacion.json` y la alineación todavía muestran 17:00. La discrepancia permanece abierta.

### Lectura autoritativa de narrative_qa: proyectos 18–23 nov

Los scores siguientes son los valores releídos de cada `proyectos/<id>/storyboard.json`; prevalecen sobre la tabla anterior de este informe:

| project_id | status | score |
|---|---:|---:|
| 2026-11-18_dato-catorce-campos-hidrotermales | FAIL | 68 |
| 2026-11-18_dato-kuroshio-puente-atmosferico | PASS | 90 |
| 2026-11-19_dato-dia-luz-dos-manos-oro-poroso | PASS | 91 |
| 2026-11-19_dato-estrella-dentro-de-estrella | PASS | 90 |
| 2026-11-20_dato-dia-atlantico-humedad-sapropeles | PASS | 91 |
| 2026-11-20_dato-marea-cerebral-en-sueno | FAIL | 82 |
| 2026-11-21_fentale-metano-sin-erupcion | PASS | 90 |
| 2026-11-21_homo-erectus-selva-tropical | FAIL | 83 |
| 2026-11-21_pulsar-gamma-reticulo | FAIL | 83 |
| 2026-11-22_bao-estrella-fusion-andromeda | FAIL | 84 |
| 2026-11-22_genes-estatura-etapas | FAIL | 72 |
| 2026-11-22_voyager-1-un-dia-luz | FAIL | 83 |
| 2026-11-22_yubarta-genoma-soplo | PASS | 90 |
| 2026-11-23_supersequias-722-eventos | FAIL | 82 |
| 2026-11-23_tropical-biodiversity-turnover | FAIL | 82 |

Rectificaciones concretas frente al resumen anterior: catorce campos es **FAIL/68**, no PASS/90; luz es PASS/91, no 88; estrella es PASS/90, no 87; Fentale es PASS/90, no FAIL/82; Homo y Pulsar son FAIL/83; Yubarta es PASS/90, no 92. El JSON prevalece. En catorce campos, el campo documental `estado` sigue diciendo pendiente de QA aunque ya contiene FAIL/68; la discrepancia se registra, no se reescribe narración.

Cruces de slot que impiden promoción aun donde el QA narrativo es PASS:
- Fentale, 21-nov 23:30, coincide con Colón (`RwTTwSNGm10`) en main.
- Bao, 22-nov 13:30, coincide con Gutenberg (`YXndoPSSeaY`).
- Voyager, 22-nov 07:00, coincide con Salem (`N21TIYdONZo`).
- Yubarta, 22-nov 17:00, coincide con Ada (`Sc0cX9ejxuw`).
- Genes, 22-nov 23:30, no tiene paquete coincidente en la alineación consultada.
- Kuroshio, luz, estrella y Atlántico no presentan coincidencia de slot en los paquetes main consultados; siguen sin promoción por los bloqueos estructurales/DOI y la falta de una ejecución completa de preproducción.

### Lote obligatorio 5–7 nov: relectura de los 12 JSON

Los doce `project_id`, `fecha_objetivo`, `slot_local` y `slot_cesta` coinciden con el horario de la rama feature. Se conservan los QA ya registrados; no se repitió lectura narrativa.

| project_id | narrative_qa | score |
|---|---:|---:|
| 2026-11-05_kids-dia-en-venus | PASS | 88 |
| 2026-11-05_comida-palomitas | FAIL | 82 |
| 2026-11-05_inter-arboles-se-comunican | FAIL | 78 |
| 2026-11-05_inter-rayo-globular | FAIL | 81 |
| 2026-11-06_kids-ballena-azul-corazon | FAIL | 80 |
| 2026-11-06_comida-aguacate-negro | FAIL | 79 |
| 2026-11-06_inter-ranas-congeladas | FAIL | 83 |
| 2026-11-06_inter-arena-cantante | PASS | 94 |
| 2026-11-07_kids-huesos-bebe | FAIL | 82 |
| 2026-11-07_comida-hielo-caliente | FAIL | 81 |
| 2026-11-07_inter-pulpo-suenos | FAIL | 72 |
| 2026-11-07_inter-nubes-pesan | FAIL | 78 |

Validación estática conjunta: 85 escenas, 2,172 palabras, 84 s totales por paquete (78 s de escenas + cortinilla de 6 s), siete u ocho escenas por storyboard, voz `es-MX-JorgeNeural`, source_ids y prompt_base presentes, `approved_assets=[]`, `render_status=NOT_GENERATED` y sin rutas ni nombres de assets. Hallazgos estructurales: **510 campos narrativos obligatorios ausentes** (seis por escena), **75 escenas con SFX vacío** y el storyboard canónico de árboles carece de capa de mapa y de gráfico/dato. No se promovió Venus ni Arena pese a PASS narrativo.

Identidad y fuentes:
- `2026-11-05_inter-arboles-se-comunican` sí corresponde a redes micorrícicas comunes y Karst et al. 2023. No se marca desajuste temático. La variante de respiración nocturna es otro artefacto bloqueado.
- `2026-11-07_inter-nubes-pesan` es el ID exacto del slot feature 17:45. `2026-11-07_extra-nubes-pesan` es material de origen, no un segundo proyecto.
- En pulpos, la fuente primaria citada corresponde a *Octopus laqueus*, no a *Octopus insularis*: desajuste fuente-especie.

**Cruce con main y producción preexistente (corrección del conteo anterior):**
- Solo dos de los doce IDs canónicos tienen registro exacto en `data/publicaciones.json` de main: Hielo caliente (`HSgrnejAcaI`) y Nubes pesan (`4Qpl17Ts_vI`). No son nueve IDs canónicos.
- Hielo caliente tiene `salidas/<id>/qa.json` audiovisual de 89.83 s y 21/21 checks; publicación privada programada para 11-nov 13:30 CDMX, TT/FB publicados y nota de que el Short ya no aparecía el 12-nov. El árbol GitHub no contiene el MP4 referenciado: **MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO**.
- Nubes pesan tiene registro público `4Qpl17Ts_vI`, programado/publicado el 12-nov 07:00 CDMX, TT/FB publicados; no hay carpeta `salidas/<id>/` ni archivo de video en el árbol: **MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO**. Main cambió el slot de 17:45 a 19:00, mientras feature conserva el slot canónico 17:45.
- Arena cantante aparece como original `m4RqQRaz55k` en `data/rehechos_2026-11-22.json`; el rework `6VUxaJtqbF0` está programado para 28-nov 10:00 CDMX. Su ruta MP4 está fuera del árbol GitHub: **MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO**.
- El rework de Nubes usa el original `4Qpl17Ts_vI` y el nuevo ID `9RxTSifAcpo`, programado para 25-nov 10:00 CDMX; la ruta MP4 declarada tampoco está en GitHub: **MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO**.
- Existe otro paquete de árboles, `2026-11-07_arboles-comunicacion-bosque`, con ID `EX0W3q-yKRw`, QA audiovisual de 87.50 s y publicación programada para 13-nov 13:30. Es otro `project_id`, pero trata el mismo tema micorrícico y usa Karst 2023: riesgo de duplicado temático, no desajuste del storyboard canónico. El MP4 referenciado no está en el árbol: **MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO**.
- Los QA de Hielo y Árboles son audiovisuales, no narrative_qa. Sus duraciones medidas están dentro de 75–90 s; no sustituyen el QA narrativo.
- Hay cinco copias planas antiguas en `cola/bloqueados/` con IDs canónicos (Rayo, Aguacate, Arena, Nubes y Huesos). Algunas difieren en narración; no se copiaron, sobrescribieron ni retiraron. Los demás nombres de variantes son artefactos distintos, no se fusionan con los canónicos.
- Main cambió Rayo (5-nov), Arena (6-nov) y Nubes (7-nov) de 17:45 a 19:00. Se registra `CONFLICTO_DE_SLOT_ENTRE_RAMAS`; la identidad feature de Nubes a 17:45 se conserva.

### Backlog interdiario anterior

- **31 storyboards de 24–30 oct** carecen de `narrative_contract` y `narrative_qa`. Sus IDs son:
  - 24-oct: `abejas-bullying`, `ideonella-pet`, `osedax-comehuesos`, `serpientes-que-ruedan`.
  - 25-oct: `ave-jurasica-sin-vuelo`, `corales-contacto`, `reina-olor`, `sueno-electricidad-qom`.
  - 26-oct: `baffin-bay-ice-shelf`, `catrina-posada-monerismo`, `hongo-gente-diminuta`, `papel-picado-dia-muertos`, `papel-picado-dia-muertos_parte2`, `pimiento-verde-rojo`.
  - 27-oct: `cempasuchil-ciencia`, `corneja-decision-rapida`, `ddm-parte3-pomuch`, `familia-ajolote`, `kids-serpiente-voladora`, `noct-anfibio-marino`.
  - 28-oct: `ddm-parte4-templo-mayor`, `familia-voyager-disco-oro`, `kids-titanoboa`, `monarca-almas`, `mosquito-fruitless-audicion`, `noct-lince-milanos`, `pan-de-muerto-huesos`.
  - 29-oct: `juno-choque-proa`, `muralismo-cu`.
  - 30-oct: `arqueas-origen-eucariotas`, `kromdraai-primera-fecha`.
- De esos 31, 24 tienen `salidas/<id>/`, cinco también tienen copia bloqueada y siete no tienen ni salida ni copia bloqueada: OseDax, serpientes, ave jurásica, reina olor, sueño electricidad Qom, hongo gente diminuta y pimiento verde/rojo. Ninguno se promueve sin contrato y QA independiente.
- 31-oct: cuatro borradores sin `narrative_contract`; uno carece de narrative_qa y tres conservan FAIL 77/78/81.
- 1–2 nov: seis borradores; cinco carecen de `narrative_contract`; cuatro QA FAIL y dos PASS (89 y 90), pero estos dos PASS no habilitan promoción sin contrato/validación estructural.
- 9–17 nov: diez borradores con contrato; nueve PASS (88–92) y Quasar FAIL/0 por revisión independiente ausente. Varios estados documentales siguen en pendiente pese a PASS; se conservan como bloqueos, no como recepción Grok.
- El inventario 18–23 nov se detalla en la tabla autoritativa anterior. No se repitió QA válido con narración sin cambios.

### Registro, procesador, Actions y PRs

- `scripts/registro_editorial.py` actual sí recorre `handoffs/grok_inbox/` recursivamente y también las estructuras anidadas de storyboards. El addendum 20-nov que decía que no recorría handoffs/profundidades quedó obsoleto. Un marker sigue sin demostrar lectura de Grok.
- `scripts/procesar_cola.py` usa la fecha CDMX actual por defecto y filtra por prefijo de fecha; el argumento `--fecha` permite seleccionar manualmente una fecha histórica. Por tanto, el comportamiento por defecto es del día actual, pero no existe un bloqueo absoluto contra una invocación histórica explícita.
- Último dispatch de entrega observado: run `41306776689`, 1-nov 12:29:58Z, FAILURE. Error literal: `Falta configurar GROK_WEBHOOK_URL.` El log no llegó a probar si `GROK_WEBHOOK_TOKEN` faltaba; no se consultaron ni divulgaron valores. No hay dispatch posterior. El workflow actual limita paths y selector a JSON planos.
- Worker main `45254537410`: SUCCESS, log indica que no había trabajo en cola. Semgrep `45255115817`: FAILURE, 37 hallazgos bloqueantes; Gitleaks `45255115860`: SUCCESS sin leaks; push main `45255114848`: SUCCESS.
- PRs abiertos revisados: #3 (base main, head feature, draft, 704 archivos; 119 storyboards, 13 data JSON y cinco workflows; no merge); #4 (robot, solo estado documental; abierto); #6 (supervisor workflow; abierto); #13 (auditoría Grok, no sustituye narrative_qa; abierto); #14 (base main, head `chatgpt/quasar-audit-fixes-20261115`, añade `asset_filename` a ocho escenas, contrato incompatible; OPEN/NOT MERGED); #15 (base feature, head `fix/capcot-map-coordinate-types-20261122`, cambios de validador/DOI no integrados). #7–9 son dependencias. Ningún PR se integró.
- El estado de Kuroshio se actualizó para registrar el run CI #45075532329, commit `25e1ecfc96faf9a40f86a9feb0e30af90d9d608b`, comando exacto y resultado. Fue validación estructural `OK`, **sin `--check-doi`**; DOI sigue pendiente.

### Datos, ejecución y límites

- `temas_del_dia.json` y `estilos_usados.json`: último corte 28-oct; `rotacion.json` y `tendencias_estilos.json`: 31-oct; `publicaciones.json` de feature: 31-oct; `horarios.json`: 9-nov; `vistas_historico.json`: 27-oct; `balances_6h.json`: 28-oct; reprogramación: 1–3 nov; `horario_semana_2026-11-01_07.json`: solo 1–7 nov. `endscreens_rotacion.json` sí tuvo actualización 23-nov 09:40. `data/cola.json` solo conserva el error histórico de Pardelas del 31-oct.
- No hay runtime local en esta ejecución: revisión estática de estructura/código y lectura de resultados CI existentes. No se ejecutaron helpers localmente. No se revisaron APIs externas porque no apareció un cambio oficial nuevo sustentado.
- No se promovió ningún proyecto, no se movieron copias, no se disparó workflow, no se enviaron payloads, no se modificó `data/*.json`, main, secretos, permisos ni decisiones editoriales. No se generaron medios ni se consumieron créditos.


### Confirmación exhaustiva de estado Grok

La relectura del árbol completo en HEAD `6577868ea826703fa512a2831e5e5ee7c19c6c79` confirma que **no existe ningún path bajo `cola/estado/`** y que `handoffs/grok_done/` solo contiene `.gitkeep`. Por tanto, los 15 IDs de la tabla 18–23 nov, los 12 IDs del lote 5–7 nov y el paquete histórico del robot quedan con **RECEPCION_GROK_NO_CONFIRMADA**. El único marker de `handoffs/grok_inbox/` es el del robot, con `status=pending`; prueba escritura del marker, no lectura por Grok. No se creó ni modificó ningún estado.


**Trazabilidad de commits de auditoría:** el código y los paquetes se inspeccionaron inicialmente en HEAD `af1584ace60d349b07eff387799e9e06b6713618`. Las únicas escrituras posteriores fueron documentales: actualización de `proyectos/2026-11-18_dato-kuroshio-puente-atmosferico/ESTADO_EJECUCION.md` y este brief. El commit `15257001aeb984f5c04164ef0e545872124ffa6b` fue la versión inmediatamente anterior a esta última corrección documental. El HEAD definitivo es el commit que contiene esta corrección; después del corte `af1584a` no cambiaron storyboards, datos, workflows ni paquetes.

## Revalidación del operador — 2026-11-23 18:00 CDMX

### Corte de ramas y ejecuciones
- Auditor CAPCOT: run `790874a5-6500-8327-8780-1e5678ecca67`, terminado 16:18 CDMX; commit `7777ce289c19e67cada531f36c24c12f6d47291e`. Investigador: run `aec348df-574c-8333-aab7-4a37c00aaed3`, terminado 08:22 CDMX; commit `66b0aac71cabd63942e73a2fe61f7c80245b383e`.
- `feature/capcot-video-discovery-continuity` HEAD `26468bf58318a768726a3895c133b1bd91564667` (después de tres commits documentales de este run; corte de auditoría previo `9cdd37160048e6aa75a39c5875da34e89d173aa0`); `main` HEAD `84731657f14e31f16984b95651bc4fe0c2b2c2c2` (17:20 CDMX).
- El diff `af1584a...9cdd371` contiene únicamente el brief de control, el `ESTADO_EJECUCION.md` de Kuroshio y `data/endscreens_rotacion.json`. No cambió ningún storyboard, cola, estado Grok ni workflow después del corte del auditor. No se repitió QA narrativo.

### End screens: divergencia nueva entre ramas
- En `feature`, `data/endscreens_rotacion.json` (blob `bb4eb4580f41423e6f7be4f2ca75c97e249b2e5e`, solo lectura) deja `4Vi_TnIl9FI` → `CW02WClntYA` y marca `pendiente_studio=false`.
- En `main`, `data/endscreens_rotacion.json` (blob `852c5aa623de84c04b5071ba2baddfbafc00de30`) incorpora `propuesta_2026-11-23_17` con estado `aplicado_studio_2026-11-23 17:20` y 14 aplicados/1 ya existente; sin embargo, el `mapa` y `aplicado_studio` canónicos no contienen las nuevas asignaciones. La propuesta trata `4Vi_TnIl9FI` como destino acelerador de los videos de bajo rendimiento, mientras `feature` conserva una asignación saliente de ese ID a `CW02WClntYA`. Es una divergencia de datos/Studio sin reconciliación verificable. No se modificó ninguna rama ni `data/*.json`.

### Actions, PR e incidencias
- `main` Semgrep run `45287956327`: **FAIL**, 37 hallazgos bloqueantes en 1,238 archivos / 361 reglas; exit code 1. El paso de carga SARIF fue `skipped` y no existe artifact; el log no expone rutas/reglas individuales. Gitleaks `45287956278`: success. No se ejecutó ni se alteró el workflow.
- PR #15 sigue OPEN hacia `feature`, mergeable pero `unstable`; su diff añade rechazo de booleanos en coordenadas/bounds y fija el host HTTPS de Crossref, con pruebas. No se integró.
- PR #3 sigue DRAFT/OPEN hacia `main`, 704 archivos, `mergeable=false`, `dirty`. PR #14 y PR #13 siguen OPEN hacia `main`; no se integraron. Issue #11 continúa OPEN con etiqueta `hecho`, pero la QA del storyboard de cuásares permanece FAIL/0 por `REVISION_INDEPENDIENTE_AUSENTE`; la etiqueta no equivale a cierre de la compuerta.
- `capcot-grok-dispatch.yml` continúa limitado a `cola/entrada/*.json` y `find ... -maxdepth 1`; no selecciona entradas anidadas. No se disparó dispatch ni se enviaron payloads.

### Tendencias y cupo
- Google Trends HTML México (`geo=MX`) devolvió 179 tendencias en la vista consultada; no apareció tema elegible de ciencia/naturaleza/cocina/cuerpo/espacio. «Hipótesis de Riemann» es matemáticas y queda fuera del alcance editorial.
- Se conserva la auditoría de ocupación del día ya registrada arriba: 10 IDs de YouTube en ocho horas, colisiones 07:00 y 17:00, y conflictos de los dos borradores feature. No hay slot nuevo autorizado. La nota de Mitra que lo mueve a 18:00 sigue en contradicción con `programacion.json` y la alineación, que conservan 17:00.

### Cierre de este corte
- Sin promociones, redispatch, cambios en `main`, `data/*.json`, `cola/estado`, secretos, permisos o workflows; sin generación de medios ni consumo de créditos. Los dos storyboards del 23 siguen FAIL/82 y fuera de cola.
