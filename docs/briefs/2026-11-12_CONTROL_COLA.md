# CONTROL COLA CAPCOT — 2026-11-12

**Corte de auditoría:** 2026-11-12, 15:38 America/Mexico_City  
**Repositorio:** marcojpad-hash/capcot-capsulas-imaginantes  
**Rama:** feature/capcot-video-discovery-continuity  
**Commit de rama leído antes de crear este informe:** a185fb72dd7516ee7413eb71fcbaac84245ac07d

## 0. Autoridad y alcance leído

Se leyeron el Contrato Operativo Unificado, Plan Maestro, Receta, Guía de Modelo Externo, Flujo Externo, contrato de estado Grok, protocolo de descarga/carga, QA Narrativo en Frío, catálogo canónico scripts/estilos.json, plantillas, archivos data/*.json existentes, scripts/procesar_cola.py, scripts/validar_storyboard.py, scripts/registro_editorial.py, briefs y storyboards pertinentes.

Precedencia aplicada: Contrato Operativo Unificado → Plan Maestro/Receta/Guía/Flujo Externo → plantilla vertical vigente → catálogo JSON. La plantilla vigente para preproducción es templates/storyboard_vertical.template.json. templates/storyboard.template.json es un formato antiguo 16:9/120 s con rutas de assets; storyboard_generico.template.json también incorpora asset_filename y export.filename, por lo que no se debe usar para una entrada textual limpia de preproducción.

No se generaron cápsulas, frames, imágenes, voz, audio, video ni renders. No se publicó, programó, disparó un workflow, envió un payload ni consumió créditos.

## 1. Día actual: 12 de noviembre

### Briefs y archivos

- Existe docs/briefs/2026-11-12_RADAR_CAPCOT.md.
- Este archivo es el control de cola creado para completar el corte del día.
- El radar original tiene corte de las 08:00 y registra correctamente que entonces no había project_id del 12-nov. El storyboard fue creado después, en el commit 8a292b5ae6990724225e52030634a050978f9e7f, a las 14:23:31Z (08:23:31 CDMX). La sección de reejecución NO_DUPLICAR del propio radar ya reconoce el proyecto posterior. No atribuirlo al investigador automatizado sin evidencia adicional de ejecución.

### Inventario completo

| Ubicación | Resultado |
|---|---|
| proyectos/2026-11-12*/storyboard.json | 1: 2026-11-12_dato-pedorreta-chimpances |
| cola/entrada/*.json del 12-nov | 0 |
| cola/entrada/<project_id>/storyboard.json del 12-nov | 0 |
| salidas/2026-11-12*/ | 0 |
| cola/bloqueados/2026-11-12*/ | 0 |
| cola/estado/2026-11-12_dato-pedorreta-chimpances.json | 404 |

Para el proyecto vigente, el estado exacto es **RECEPCION_GROK_NO_CONFIRMADA**. No se creó ni modificó el archivo de estado: solo Grok puede hacerlo.

### Proyecto del día

Archivo: proyectos/2026-11-12_dato-pedorreta-chimpances/storyboard.json  
Lectura final desde GitHub: blob 9cdf19e915274ca617d08c23a8c1b41639f4fdc9.

- project_id y fecha_objetivo: 2026-11-12.
- slot_local: 17:00, expresamente descrito en el paquete como referencia de staging, no como hora de publicación.
- slot_cesta: ausente. No se inventó una cesta ni una asignación de horario.
- editorial_status: PROPUESTA_PENDIENTE_DE_GROK.
- publicacion.status: PENDIENTE_DECISION_GROK.
- No existe ESTADO_EJECUCION.md, salida ni entrada de cola.

**QA narrativo en frío:** PASS, score 91, review_basis=lectura_en_frio_solo_narracion, siete checks true, critical_flags=[]; reviewer_role=auditor_capcot_independiente. Se ocultaron título, resumen, arco, notas y narrative_contract; la evaluación se hizo sobre la narración concatenada.

**Revisión estructural estática posterior a normalización mecánica:**

- 8 escenas; 198 palabras; 78 s de escenas + 6 s de cortinilla = 84 s.
- Gancho de 5 palabras.
- Voz: edge-tts, es-MX-JorgeNeural, +7%, -2 Hz, pausas continuas.
- Estilo collage_cientifico_vintage existe en el catálogo; prompt_base coincide literalmente en todas las escenas.
- 4 fuentes; source_ids válidos. Hay una capa de mapa y una de dato/gráfico, ambas con fuente. Ambiente y SFX están declarados por escena.
- approved_assets=[]; export.render_status=NOT_GENERATED; no asset_filename, asset_type, rutas de medios ni export.filename.

Se corrigieron únicamente claves de compatibilidad con la plantilla/validador: estilo_id y estilo_visual desde visual_identity, id/arc desde scene_id/arco, id/cita_corta desde los identificadores/citas existentes, style_id por escena, fuente en las capas de mapa/dato y modo de pausas. Se conservaron las claves originales; no se cambió narración, claims ni decisión editorial. También se añadió narrative_qa.

**Bloqueo restante:** el DOI 10.1073/pnas.2606837123 aparece en la página editorial oficial de PNAS y el comunicado de University of Warwick respalda el caso del modelo adulto; sin embargo, verification_status permanece PENDIENTE_RESOLVEDOR porque el resolvedor directo devolvió HTTP 500 y no se obtuvo confirmación Crossref. Fuentes: https://www.pnas.org/doi/10.1073/pnas.2606837123 y https://warwick.ac.uk/news/pressreleases/chimpanzees-blowing-raspberries/.

La revisión estática no encontró errores de estructura después de las normalizaciones, pero dejó la advertencia de DOI pendiente. No se ejecutó scripts/validar_storyboard.py ni su opción --check-doi: no había runtime local del repositorio. Por tanto, no se declara una ejecución exitosa del validador. El proyecto permanece en proyectos/ y **NOT_DISPATCHABLE**. No se promovió a cola: falta la ejecución real del validador/resolvedor y no hay selección editorial ni slot oficial del 12-nov. Además, crear un JSON en la raíz de cola/entrada dispararía el workflow push, expresamente prohibido en esta auditoría.

## 2. Lote obligatorio 5–7 de noviembre

### Identidad y horario

Los 12 project_id, fecha_objetivo, slot_local y slot_cesta de proyectos/<id>/storyboard.json coinciden exactamente con data/horario_semana_2026-11-01_07.json: **12/12 coincidencias**. El estado de esos slots en el horario semanal es pedir_chatgpt; eso no equivale por sí mismo a selección de Grok.

| Fecha | Slot CDMX | Cesta | Project ID | narrative_qa |
|---|---:|---|---|---:|
| 05-nov | 07:00 | kids | 2026-11-05_kids-dia-en-venus | PASS 88 |
| 05-nov | 13:30 | comida_familia | 2026-11-05_comida-palomitas | FAIL 82 |
| 05-nov | 17:00 | intermedio_1 | 2026-11-05_inter-arboles-se-comunican | FAIL 78 |
| 05-nov | 17:45 | intermedio_2 | 2026-11-05_inter-rayo-globular | FAIL 81 |
| 06-nov | 07:00 | kids | 2026-11-06_kids-ballena-azul-corazon | FAIL 80 |
| 06-nov | 13:30 | comida_familia | 2026-11-06_comida-aguacate-negro | FAIL 79 |
| 06-nov | 17:00 | intermedio_1 | 2026-11-06_inter-ranas-congeladas | FAIL 83 |
| 06-nov | 17:45 | intermedio_2 | 2026-11-06_inter-arena-cantante | PASS 94 |
| 07-nov | 07:00 | kids | 2026-11-07_kids-huesos-bebe | FAIL 82 |
| 07-nov | 13:30 | comida_familia | 2026-11-07_comida-hielo-caliente | FAIL 81 |
| 07-nov | 17:00 | intermedio_1 | 2026-11-07_inter-pulpo-suenos | FAIL 80 |
| 07-nov | 17:45 | intermedio_2 | 2026-11-07_inter-nubes-pesan | FAIL 78 |

Se volvieron a leer las narraciones concatenadas sin consultar título, resumen, arco, notas ni narrative_contract. Los doce narrative_qa se releen desde GitHub; solo se actualizó reviewed_at a 2026-11-12T15:38:50-06:00. Scores, statuses, siete checks y critical_flags permanecen exactamente como en los JSON. Resultado: 2 PASS y 10 FAIL.

### Validación estructural y de medios

- 85 escenas en total; todas las cápsulas tienen 7 u 8 escenas.
- Duración total registrada: 84 s con cortinilla de 6 s en los doce.
- Ganchos: 3–5 palabras; todos dentro del máximo de seis.
- Palabras: 170–221 salvo 2026-11-05_inter-arboles-se-comunican, con 169.
- Faltan los seis campos narrativos obligatorios en cada escena: dramatic_beat, scene_function, causal_bridge_from_previous, question_state, reason_to_continue y new_information. Total: **510 campos ausentes**.
- Se encontraron **75 arrays SFX vacíos**; ambiente está presente en las 85 escenas. El validador actual comprueba la existencia de la clave sfx, pero no rechaza un array vacío: la revisión manual sí lo marca como defecto.
- 2026-11-05_inter-arboles-se-comunican no tiene capa de mapa ni de dato/gráfico. No se marca desajuste temático: el storyboard canónico trata redes micorrícicas comunes y Karst et al. 2023, conforme a la identidad fijada por el usuario.
- En los doce, los source_ids apuntan a fuentes existentes y los image_prompt respetan el prompt_base del catálogo. Los proyectos que no tienen DOI mantienen URL de fuente; no se inventaron DOI.
- Los doce tienen approved_assets=[], export.render_status=NOT_GENERATED, no asset_filename/asset_type ni rutas de assets y no export.filename. No se cuentan placeholders como medios.

El equivalente estático de la validación estructural falla para los doce: los seis campos narrativos faltan en todas las escenas; además, el proyecto de árboles queda por debajo de 170 palabras y no tiene mapa/dato. Los dos PASS narrativos (Venus y arena) tampoco son promovibles: el QA narrativo no sustituye el validador estructural.

### Handoff, bloqueos y recepción Grok

Los doce storyboards están en proyectos/, no en cola/entrada/. No existe copia de entrada para ninguno de los doce; por tanto, no había una copia heredada en cola/entrada que mover. Hay JSON bloqueados de nivel raíz para rayo-globular, aguacate-negro, ranas-congeladas, arena-cantante, nubes-pesan y huesos-bebe. Esos archivos bloqueados conservan estado=PENDIENTE_REVISION_GROK y no tienen narrative_qa; no se usaron como evidencia de QA ni se modificaron. Las carpetas bloqueadas exactas de aguacate, ranas y huesos incluyen ESTADO_EJECUCION.md con BORRADOR_EN_PROYECTOS_NO_APTO_PARA_PROMOCION, pero sus storyboard.json conservan el estado antiguo PENDIENTE_REVISION_GROK. Se registra la discrepancia documental y se dejan intactos. Las variantes de Venus, palomitas, árboles, ballena, hielo y pulpo tienen slugs distintos y no se contaron como copias canónicas de esos project_id.

Para los doce IDs, cola/estado/<project_id>.json devolvió 404. Estado de cada uno: **RECEPCION_GROK_NO_CONFIRMADA**. No se atribuye recepción, selección, QA ni publicación a Grok por la existencia de un storyboard o una copia bloqueada.

Identidades que se preservan:
- 2026-11-05_inter-arboles-se-comunican es el storyboard canónico de micorrizas; la variante inter-arboles-mito-respiran es otro artefacto bloqueado y no se usa para juzgar el tema canónico.
- 2026-11-07_inter-nubes-pesan es exactamente el slot de 17:45. extra-nubes-pesan es material de origen, no un segundo proyecto.
- Se respetaron las exclusiones: slots 23:30 de dato del día, kids del 3-nov 07:00 y Machu Picchu del 4-nov 19:00. No se auditaron ni se crearon copias para esos elementos.

## 3. Guardia de producción preexistente y no redispatch

La búsqueda de salidas/<project_id>/ no encontró directorios GitHub para ninguno de los doce; tampoco hay qa.json, publicacion.json, metadata.json ni licencias.json en salidas para este lote. Sin embargo, los registros diarios data/horario_2026-11-08.json a data/horario_2026-11-11.json contienen evidencia de plataforma para cinco project_id. Esa evidencia prevalece sobre la ausencia de una carpeta salidas para la decisión de no redispatch:

| Project ID | Último registro interno | Evidencia de plataforma | Riesgo/decisión |
|---|---|---|---|
| 2026-11-05_comida-palomitas | 08-nov, 07:00 CDMX | YT zTP5akrGA9M; TikTok 7705593452003691794; Facebook 1167496802382795; estado publicado_yt_tt_fb | PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR |
| 2026-11-06_inter-ranas-congeladas | 09-nov, 07:00 CDMX | YT UBFuKBU3cx0; TikTok 7705596671807245586; Facebook figura programado_lote_7nov sin URL capturada | PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR |
| 2026-11-06_comida-aguacate-negro | 10-nov, 07:00 CDMX | YT nSS_q2tj2P0; TikTok 7705594217136966920; Facebook figura programado_lote_7nov sin URL capturada | PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR |
| 2026-11-06_kids-ballena-azul-corazon | 11-nov, 07:00 CDMX | YT wbFrlM2e_YE; TikTok 7705594333574991122; Facebook figura programado_lote_7nov sin URL capturada | PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR |
| 2026-11-07_comida-hielo-caliente | 11-nov, 13:30 CDMX, cesta extra del registro diario | YT HSgrnejAcaI en privado/programado para 19:30Z; TikTok 7706905447424347393 programado, Everyone; Facebook programado, visibilidad Pública, estado UI “En proceso…” | PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR |

Los primeros cuatro tienen registro de publicación YT+TikTok; Palomitas también tiene Facebook publicado. Hielo estaba programado, no consta como publicado en ese corte. No se borró, canceló ni reprogramó nada.

Los registros citan rutas MP4 en espacios de trabajo externos a este árbol GitHub. Para los cinco se marca **MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO**. No se afirma que esos archivos existan en GitHub. Las duraciones de plataforma disponibles (aguacate 83 s, ballena 80 s, hielo 90 s) son metadatos de plataforma, no QA audiovisual. No existe qa.json local para sustituir la comprobación oficial de 75–90 s.

No hay un archivo historial_youtube en el árbol. Los IDs anteriores aparecen en los horarios diarios citados; deben tratarse como riesgo de duplicado. No se intentó abrir Studio, borrar IDs ni cancelar programaciones. No se consultaron las plataformas en vivo en esta ejecución; los estados descritos son los últimos registros internos disponibles.

La clasificación anterior de cinco proyectos con procesamiento preexistente queda confirmada por los horarios diarios: cuatro publicados y uno programado. Los otros siete IDs no tienen evidencia de publicación/programación en esos registros ni directorios salidas en GitHub. Eso no los vuelve seleccionados ni recibidos; siguen sujetos a sus QA y bloqueos.

Hay una discrepancia documental concreta: los ESTADO_EJECUCION.md de las carpetas bloqueadas de aguacate y ranas dicen Medios: NO_GENERADOS y BORRADOR_EN_PROYECTOS_NO_APTO_PARA_PROMOCION, pero los horarios del 10 y 9 de noviembre respectivamente registran YT/TikTok publicados y rutas MP4 externas. Los documentos de estado son anteriores (31-oct) y no reflejan esos registros posteriores. Se dejaron intactos.

## 4. Paquete del 11 de noviembre en cola

Se encontró cola/entrada/2026-11-11_dato-ratas-topo-damaraland/storyboard.json dentro de una carpeta anidada. La carpeta contiene ocho PNG reales en frames/frame_01.png a frames/frame_08.png; esos blobs sí existen en el árbol GitHub. El storyboard referencia esos frames y export.filename=capsula.mp4, pero no existe el MP4 en el árbol. No hay ESTADO_EJECUCION.md ni cola/estado/2026-11-11_dato-ratas-topo-damaraland.json; por tanto, **RECEPCION_GROK_NO_CONFIRMADA**. El storyboard no tiene narrative_qa y su estado interno dice PREPARADO_PENDIENTE_REVISION_GROK; no se toma como QA ni recepción.

Este paquete es **NOT_DISPATCHABLE**: está en cola/entrada/<project_id>/storyboard.json y el workflow solo selecciona JSON de primer nivel. No se modificó, movió ni produjo ningún medio en esta auditoría. No es una entrada del día 12-nov.

## 5. Workflow, procesador y registro editorial

### Dispatch

El workflow actual .github/workflows/capcot-grok-dispatch.yml tiene:

- push.paths: cola/entrada/*.json
- En push, filtra únicamente rutas raíz que coincidan con ^cola/entrada/[^/]+\.json$.
- En workflow_dispatch, find cola/entrada -maxdepth 1 -type f -name '*.json'.

Por tanto, las carpetas anidadas no disparan ni entran en el selector del workflow. El procesador sí recoge cola/entrada/*.json y cola/entrada/*/storyboard.json. Hay una discrepancia real de profundidad entre workflow y procesador.

Clasificación:
- Proyecto 12-nov en proyectos/: **NOT_DISPATCHABLE**.
- Paquete 11-nov en cola/entrada/2026-11-11_dato-ratas-topo-damaraland/storyboard.json: **NOT_DISPATCHABLE**.
- Los doce storyboards del lote 5–7 permanecen en proyectos/: **NOT_DISPATCHABLE**.
- No hay entrada raíz del 12-nov; no se creó una.

El workflow actual escribe un marcador pending en handoffs/grok_inbox y usa webhook solo si existen ambas credenciales. Ese marcador no sustituye cola/estado ni confirma que Grok leyó el paquete.

### Selección por fecha

scripts/procesar_cola.py usa America/Mexico_City para el default de --fecha, reúne entradas raíz y carpetas anidadas y filtra fecha_archivo(path) == --fecha. Procesa todas las candidatas de esa fecha; no selecciona automáticamente la cola histórica más antigua. La selección por fecha es correcta. La incompatibilidad está en el workflow, no en ese filtro.

### Actions

La última ejecución encontrada de este workflow es la run #147 del 2026-11-01; no se encontró una ejecución posterior de capcot-grok-dispatch. El log de esa run, correspondiente a una versión anterior del workflow, contiene literalmente: “Falta configurar GROK_WEBHOOK_URL.” y después omite la entrega. La configuración actual cambió: el webhook es opcional y el flujo puede dejar el marcador en handoffs/grok_inbox sin webhook. No se declara que GROK_WEBHOOK_TOKEN falte; el log antiguo no llegó a demostrarlo y el workflow actual lo trata junto con la URL como condición opcional. No se muestran valores de secretos.

### registro_editorial.py y reconciliación

registro_editorial.py une rotacion.json, publicaciones.json, cola.json y storyboards encontrados en proyectos/cola/salidas. No lee los archivos diarios data/horario_YYYY-MM-DD.json ni horario_semana, tampoco cola/estado, historial_youtube o los registros de handoffs. Por eso no reconstruye por sí solo las cinco publicaciones/programaciones documentadas arriba. También obtiene estilo solo de sb.estilo_id; el borrador del 12-nov carecía originalmente de esa clave superior y se añadió como alias mecánico desde visual_identity.style_id.

No se modificó el script ni los registros de datos.

## 6. Estado y antigüedad de data

- data/horario_semana_2026-11-01_07.json es la fuente de los doce slots y coincide 12/12 con los storyboards.
- data/horario_2026-11-08.json, 09, 10 y 11 contienen los cinco registros de plataforma anteriores.
- data/horarios.json llega al 09-nov.
- data/temas_del_dia.json y data/estilos_usados.json llegan hasta el 28-oct; data/rotacion.json, publicaciones.json, cola.json y tendencias_estilos.json llegan al 31-oct.
- data/reprogramacion_tt_fb_v4_2026-11-01_03.json llega al 03-nov.
- data/endscreens_rotacion.json se actualizó el 12-nov, pero es rotación de pantallas finales, no asignación editorial ni historial de publicación.
- No existe data/horario_2026-11-12.json. No hay registro de tema/rotación/publicación para el 12-nov en los JSON canónicos.
- collage_cientifico_vintage existe en el catálogo y aparece dos veces en estilos_usados bajo familia-ajolote; ese registro está atrasado y no permite certificar unicidad histórica. El estilo del paquete de 11-nov es linograbado, distinto del estilo del borrador del 12-nov.

No se encontró historial_youtube.json ni una ruta equivalente. Los horarios diarios son la evidencia disponible de los IDs publicados/programados.

## 7. Contradicciones y límites

1. La plantilla vertical y la receta actuales exigen campos narrativos por escena; los doce storyboards antiguos no los tienen. El validador estructural detecta esos seis campos, pero no detecta arrays SFX vacíos: la auditoría manual añadió ese hallazgo.
2. La plantilla genérica y la plantilla storyboard.template.json antigua contienen rutas/exports y formato 16:9/120 s; no deben sustituir la plantilla vertical de preproducción.
3. El workflow solo admite raíz de cola; el procesador admite carpetas anidadas.
4. registro_editorial.py no incorpora horarios diarios, estados de Grok ni bloqueados; omite evidencia de publicación y puede subestimar el riesgo de duplicado.
5. Los estados de ejecución del 31-oct para aguacate/rana no reflejan las publicaciones posteriores registradas en noviembre.
6. No hay runtime local para ejecutar validador/helpers. Se hizo revisión estática; no se afirma que el script se haya ejecutado.
7. No se encontró cambio oficial nuevo de API que justificara revisar o modificar documentación técnica. No se abrió una revisión de APIs.

## 8. Cambios efectuados y no efectuados

Cambios efectuados:
- Se añadió narrative_qa PASS/91 al borrador del 12-nov tras lectura en frío.
- Se normalizaron claves de esquema y referencias de fuente/estilo/voz del mismo borrador sin modificar narración ni claims.
- Se actualizaron únicamente reviewed_at en los narrative_qa de los doce proyectos del lote; los scores/statuses/checks/flags se conservaron.
- Se creó este informe.

No efectuado:
- No se promovió ningún proyecto a cola.
- No se creó ni modificó cola/estado.
- No se modificó data/*.json, main, workflows, secretos, permisos, motores ni registro_editorial.py.
- No se movieron ni borraron archivos bloqueados.
- No se generaron medios, no se publicó, no se programó, no se enviaron payloads ni se consumieron créditos.

## 9. Conclusión operativa

El único borrador del 12-nov tiene QA narrativo PASS/91 y revisión estructural estática sin errores tras normalizaciones, pero conserva DOI pendiente de resolvedor y no tiene validación ejecutada en runtime, selección editorial ni slot oficial. Permanece en proyectos/ y no es despachable.

En el lote 5–7, los dos PASS narrativos no pasan estructura por los seis campos ausentes en cada escena. Los diez FAIL permanecen fuera de cola. Cinco proyectos tienen procesamiento/publicación preexistente y quedan protegidos contra redispatch; sus medios no están verificados en el árbol GitHub. Los doce carecen de estado Grok verificable.

**El lote 5–7 sigue abierto.** No hay promoción autorizada en esta ejecución.
