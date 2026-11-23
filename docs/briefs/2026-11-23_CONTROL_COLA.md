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
- Entrada heredada `cola/entrada/2026-11-09_dato-robot-ensambla-orbita`: QA PASS 90, pero main contiene MP4, portada, nueve frames, QA y programación con `publishAt` 21-nov 19:00 CDMX. Metadata aún marca `privacyStatus=private`; el estado Grok individual devuelve 404. Clasificación `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`; publicación real no confirmada. No cancelar ni duplicar.
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