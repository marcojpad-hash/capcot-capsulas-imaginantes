# Control de cola CAPCOT — 25 nov 2026, corte 14:09 CDMX

## Cambios desde el control anterior

- Rama de trabajo: feature/capcot-video-discovery-continuity, HEAD observado antes de este registro 3d4c0f4be6cbba91a546d61c6f487a930a89a940.
- main: HEAD f4af1797e02fa3113f89385c3146ae0c4b49034e. El único cambio posterior al corte anterior fue data/endscreens_rotacion.json, commit f4af179, con snapshot/propuesta 2026-11-25_14 y estado pendiente_studio. No cambió ningún storyboard, cola, horario ni publicación.
- En feature, el compare desde el HEAD del control anterior solo agregó el control de 12H; no hubo cambios de narración ni storyboards. En main, el compare desde el HEAD anterior solo cambió el snapshot de pantallas.
- Se creó una actualización del radar con cuatro candidatos nuevos y los errores exactos de lectura RSS. No se asignó slot ni se creó storyboard.

## Inventario 5–7 nov

- Se releyó ajustes_entre_modelos/PARA_CHATGPT_5-7nov_PASS_auditor.md en la rama feature. Contiene los 12 IDs y exige auditoría independiente; no autoriza autoevaluación del redactor.
- El control previo conserva 2 PASS y 10 FAIL. No se repitieron PASS ni se reescribieron narraciones: el compare confirma que no cambiaron storyboards desde el corte anterior.
- La cola bloqueada conserva el lote y sus copias heredadas; no se movió ni promovió ningún archivo.

## Proyectos y producción preexistente en main

### Nueve reworks del 25–29 nov

- data/rehechos_2026-11-22.json contiene nueve reworks con YouTube ID y publishAt_utc: dos el 25, dos el 26, dos el 27, dos el 28 y uno el 29; el estado de la ficha es private→public programado.
- Los nueve render.log dicen OK; las duraciones medidas en esos logs van de 86,47 a 88,80 s y las fichas tienen siete escenas.
- No hay MP4 dentro de los árboles de proyectos ni carpetas salidas/<id>. Por tanto: PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR y MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO. Los logs y los IDs de YouTube no sustituyen el archivo de video.
- La auditoría narrativa fría anterior dejó 6 PASS y 3 FAIL. No se repitió porque las narraciones no cambiaron; esos resultados externos no están embebidos como narrative_qa en los storyboards de main.
- Para los nueve IDs, cola/estado/<project_id>.json devuelve 404: RECEPCION_GROK_NO_CONFIRMADA. No están en cola/entrada ni en salidas.

### React — bacterias anticáncer

- El paquete existe en main/proyectos/2026-11-25_react-bacterias-anticancer/ y también como copia anidada en cola/entrada/2026-11-25_react-bacterias-anticancer/storyboard.json. La copia de cola no es plana.
- Corrección al control previo: fuentes.md sí existe en main/proyectos/<id>/fuentes.md. El DOI 10.1126/science.aee2641 aparece asociado al artículo; la afirmación de aceleración 4× continúa PENDING_SOURCE porque no quedó respaldada por la fuente consultada.
- El storyboard mantiene seis escenas, 102 palabras y 66 s efectivos incluyendo cortinilla; declara objetivo de 85 s. El gancho tiene 11 palabras. No presenta mapa con coordenadas reales ni dato/gráfico suficiente.
- Conserva asset_filename en escenas y export.filename; faltan approved_assets=[], export.render_status=NOT_GENERATED y publicacion.status=PENDIENTE_DECISION_GROK. No existe narrative_qa ni ESTADO_EJECUCION.
- programacion.json reserva 17:00. data/miniaturas_auditoria_2026-11-21.json ya tiene L6ggmPAwBOA a las 17:00; además hay dos IDs en 07:00. Resultado: CONFLICTO_DE_SLOT_EN_MAIN y PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR.
- cola/estado/<id>.json y salidas/<id>/ devuelven 404: RECEPCION_GROK_NO_CONFIRMADA. Los asset_filename/export.filename no tienen archivos correspondientes en el árbol: MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO. La copia anidada no satisface el selector de capcot-grok-dispatch.yml, que filtra cola/entrada/*.json y busca con profundidad 1. NOT_DISPATCHABLE.

## Horarios, cola y auditoría

- La ocupación del 25–28 nov conserva seis horas ocupadas (07:00, 10:00, 13:30, 15:00, 17:00 y 19:00) más la reserva fija 23:30. La cifra 7/5 incluye esa reserva; no significa siete videos reales en siete horas distintas. El 25 hay colisión 07:00 y el paquete React añade una segunda ocupación a 17:00.
- El backlog 29 nov conserva la reserva ya registrada. No se reasignaron ni cancelaron slots.
- scripts/registro_editorial.py no ingiere por sí solo miniaturas_auditoria_*.json ni rehechos_*.json; scripts/auditar_snapshots_programacion.py sí está diseñado para esos snapshots y tiene pruebas. No se ejecutó el script en un runner; se inspeccionaron los JSON directamente y se verificaron los nueve render.log.
- cola/estado no contiene estado para ninguno de los diez proyectos del 25 nov. No se creó ni modificó ningún estado Grok.

## Workflow, CI e Issues

- capcot-grok-dispatch.yml solo selecciona archivos planos cola/entrada/*.json y busca con maxdepth 1. No se disparó workflow ni se envió payload.
- PR #3 sigue abierto en draft; su última ejecución CodeQL (45674625888) terminó en éxito.
- El escaneo Semgrep de main (45661236708) terminó en fallo: 37 hallazgos bloqueantes, 361 reglas, 1.260 archivos procesados, 37 archivos mayores de 1 MB omitidos; la carga SARIF se omitió por fallo del escaneo.
- PR #15 sigue abierto, mergeable=false; Semgrep/CI falló y CodeQL seguía pendiente en la última lectura.
- Issue #16 sigue abierto con tareas externas de MP4, TikTok y Pancho EN. No se ejecutó ninguna de esas acciones.
- No se inspeccionaron valores de secretos ni se nombraron variables de webhook porque no se verificó que faltaran.

## Radar y decisión de producción

- Se probaron los diez RSS de scripts/tendencias.py. Errores exactos: ScienceDaily ciencia/salud/espacio = 400 Unsupported content-type application/xml; Phys.org = 400 Unsupported content-type text/xml; NASA = 400 Unsupported content-type application/rss+xml; ESA = 404 Not Found; Nature = 400 Unsupported content-type application/rss+xml; EurekAlert y SINC = URL not accessible via this tool; UNAM Global = 400 Unsupported content-type application/rss+xml. Google Trends RSS México = URL not accessible via this tool.
- Respaldo HTML oficial Google Trends México: 240 tendencias, 25 visibles. En los primeros 25 resultados no se identificó un candidato científico concreto; no se seleccionó ningún tema a partir de tendencias.
- Se añadieron cuatro candidatos al radar: agujero negro W2246-0526, maquinaria de transcripción del poxvirus, interfaz contorneada de batería de estado sólido y síntesis continua N-to-C de péptidos. Todos quedan PENDING_RESOLVER; no hay DOI verificado por Crossref/resolvedor en este corte.
- No hay slot libre autorizado y no se cumplieron las compuertas de DOI/QA. No se creó storyboard, no se promovió cola, no se generaron medios y no se publicó ni programó nada.

## Estado de ejecución

- EJECUTADO: lecturas de repositorios, compare de ramas, lectura de inventario, inspección de 9 reworks, 10 estados Grok, snapshots de horarios, workflow/Actions/Issues, lectura de feeds y búsqueda documental de cuatro candidatos.
- VERIFICADO: main cambió solo el snapshot de pantallas; los nueve reworks tienen render.log OK y programación previa; React sigue no despachable y en conflicto; no hay estado Grok ni salidas para los diez IDs.
- PENDIENTE: resolver DOI de cuatro candidatos; aclarar colisiones/ocupación con la autoridad editorial; completar fuente de la cifra 4×; auditoría independiente embebida y estructural de React solo si vuelve a ser candidato; ejecutar el auditor de snapshots en un runner autorizado.
- Sin cambios en data/*.json, main, cola/estado, cola/entrada, salidas, publicaciones, secretos, permisos ni workflows.

## Detalle verificable de los nueve reworks

| Clave | Slot CDMX | YouTube ID | Duración render |
|---|---:|---|---:|
| nube | 25 nov 10:00 | 9RxTSifAcpo | 86,80 s |
| barreleye | 25 nov 15:00 | 3rwo_sK1e18 | 87,53 s |
| pan | 26 nov 10:00 | 7pzPfqRSagU | 88,47 s |
| ratas | 26 nov 15:00 | MgHVHbeIVS0 | 88,80 s |
| miel | 27 nov 10:00 | p06UCGu0-Og | 86,47 s |
| mar | 27 nov 15:00 | HKpani8TTeY | 87,17 s |
| arena | 28 nov 10:00 | 6VUxaJtqbF0 | 86,70 s |
| juno | 28 nov 15:00 | Dx3lqkAb8Sc | 87,40 s |
| viento | 29 nov 10:00 | m1FeS0mhfZ4 | 88,77 s |

- Cada render.log termina en OK y registra siete escenas. El rework barreleye también contiene el aviso «la cortinilla invade la zona segura inferior»; no se corrigió porque ya tiene YouTube ID y publishAt.
- data/rehechos_2026-11-22.json referencia los MP4 mediante rutas absolutas bajo /workspace/capcot_main. Esas rutas no existen dentro del árbol GitHub consultado; por eso la existencia y el contenido audiovisual no quedan verificados por el repositorio.
- La ficha declara estados programados en YouTube, TikTok y Facebook; no se consultaron APIs externas para confirmar el estado real de publicación.