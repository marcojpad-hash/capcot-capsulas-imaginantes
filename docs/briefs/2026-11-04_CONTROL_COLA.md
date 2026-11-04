# CONTROL COLA — 2026-11-04

**Repositorio:** marcojpad-hash/capcot-capsulas-imaginantes  
**Rama:** feature/capcot-video-discovery-continuity  
**Corte:** 2026-11-04, 15:58 CDMX  
**Rol:** auditoría independiente. Sin producción de medios, dispatch, publicación ni consumo de créditos.

## 1. Resultado ejecutivo

- Se localizaron **13 borradores canónicos en proyectos/**: el respaldo del 4-nov 19:00 y los 12 proyectos del lote 5–7 nov.
- QA narrativo en frío del lote 5–7: **2 PASS / 10 FAIL**. El respaldo del 4-nov obtuvo PASS 94.
- **0 promociones** a cola/entrada: los 12 proyectos del lote fallan el validador estructural por ausencia de seis campos narrativos obligatorios en cada escena. Los dos PASS narrativos tampoco superan esa compuerta.
- El borrador del cielo del 4-nov supera la revisión narrativa y la comprobación estructural estática, pero sigue siendo un respaldo no seleccionado: el horario conserva el proyecto Machu Picchu como candidato con aprobación pendiente. No se creó entrada de cola.
- cola/entrada/ contiene únicamente .gitkeep. No hay paquetes JSON activos ni marcadores de handoff.
- No existe ningún cola/estado/<project_id>.json para los 13 borradores. Estado exacto para cada uno: **RECEPCION_GROK_NO_CONFIRMADA**.
- Tres proyectos del 4-nov ya tienen salidas, IDs de YouTube y programación multiplataforma. Se clasifican **PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR**; no se alteró ni canceló su programación.
- No se generaron ni verificaron medios. Los archivos de video y frames referenciados por las salidas no están en el árbol GitHub: **MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO**.
- Se registró narrative_qa en los 13 borradores. Se corrigió únicamente el campo Estado documental de los seis archivos de estado del 4-nov que todavía decían PREPARADO_PENDIENTE_REVISION_GROK.

## 2. Briefs, horario y fechas

Briefs leídos:
- docs/briefs/2026-11-04_RADAR_CAPCOT.md
- docs/briefs/2026-11-05_RADAR_CAPCOT.md
- docs/briefs/2026-11-06_RADAR_CAPCOT.md
- docs/briefs/2026-11-07_RADAR_CAPCOT.md
- docs/briefs/2026-11-02_CONTROL_COLA_5-7nov.md
- docs/briefs/2026-11-03_CONTROL_COLA.md

Los doce IDs, project_id, fecha_objetivo, slot_local y slot_cesta de proyectos/ coinciden **12/12** con data/horario_semana_2026-11-01_07.json. La fecha de creación no está declarada dentro de los storyboard; se tomó del primer commit de cada archivo. Los doce se crearon el 2-nov-2026 alrededor de las 16:11 CDMX y su última actualización previa a esta auditoría fue el 3-nov alrededor de las 15:18 CDMX.

| Project ID | Fecha objetivo | Slot CDMX | Cesta | QA narrativo |
|---|---:|---:|---|---:|
| 2026-11-05_kids-dia-en-venus | 05-nov | 07:00 | kids | PASS 88 |
| 2026-11-05_comida-palomitas | 05-nov | 13:30 | comida_familia | FAIL 82 |
| 2026-11-05_inter-arboles-se-comunican | 05-nov | 17:00 | intermedio_1 | FAIL 78 |
| 2026-11-05_inter-rayo-globular | 05-nov | 17:45 | intermedio_2 | FAIL 81 |
| 2026-11-06_kids-ballena-azul-corazon | 06-nov | 07:00 | kids | FAIL 80 |
| 2026-11-06_comida-aguacate-negro | 06-nov | 13:30 | comida_familia | FAIL 79 |
| 2026-11-06_inter-ranas-congeladas | 06-nov | 17:00 | intermedio_1 | FAIL 83 |
| 2026-11-06_inter-arena-cantante | 06-nov | 17:45 | intermedio_2 | PASS 94 |
| 2026-11-07_kids-huesos-bebe | 07-nov | 07:00 | kids | FAIL 82 |
| 2026-11-07_comida-hielo-caliente | 07-nov | 13:30 | comida_familia | FAIL 81 |
| 2026-11-07_inter-pulpo-suenos | 07-nov | 17:00 | intermedio_1 | FAIL 80 |
| 2026-11-07_inter-nubes-pesan | 07-nov | 17:45 | intermedio_2 | FAIL 78 |

**Contradicciones documentales de horario:**
- Los RADAR del 5, 6 y 7 nov todavía describen el segundo slot intermedio como 19:00 y dicen que cuatro paquetes están en cola.
- El horario semanal y el control del 2-nov fijan ese slot en **17:45**. Los storyboards canónicos sí coinciden con 17:45.
- Los RADAR no reflejan la ubicación real: los borradores canónicos están en proyectos/ y los paquetes heredados están en cola/bloqueados/, no en cola/entrada/.
- data/horario conserva estado pedir_chatgpt para los doce aunque los borradores ya existen. No se modificó data/*.json.
- El Plan Maestro todavía enumera una ventana de 19:00. Para este lote prevalece el horario concreto de 17:45.

### Borrador del 4-nov

proyectos/2026-11-04_cielo-azul-atardecer-rojo/storyboard.json:
- Primer commit: 4-nov, 08:16 CDMX; última modificación: 08:20 CDMX.
- fecha_objetivo=2026-11-04, slot_local=19:00, slot_cesta=intermedio_2.
- 8 escenas, 212 palabras, 80 s de escenas + 6 s de cortinilla = 86 s.
- estilo van_gogh; approved_assets=[]; export.render_status=NOT_GENERATED.
- narrative_qa: PASS 94, siete checks true, critical_flags=[].
- La revisión estructural estática no encontró errores después de registrar narrative_qa.

El horario no asigna ese ID al slot: conserva 2026-10-29_machu-picchu-fallas-pisa con estado pendiente_ok_mj y menciona el cielo rojo/azul como respaldo si no hay aprobación. No se revisó el storyboard de Machu Picchu, expresamente excluido. El respaldo del cielo permanece en proyectos/ y **no se promueve** mientras no exista selección editorial verificable.

El storyboard del cielo conserva el campo estado=PENDIENTE_QA_NARRATIVO_INDEPENDIENTE pese al PASS 94 ya registrado; se deja intacto para no convertir un respaldo en seleccionado. La autoridad del QA es narrative_qa; la selección sigue pendiente. El árbol también contiene cola/bloqueados/2026-11-04_machu-picchu-fallas-pisa.json, mientras el horario referencia 2026-10-29_machu-picchu-fallas-pisa. No se equiparan esos IDs y no se abrió el archivo bloqueado por la exclusión expresa.

## 3. QA narrativo en frío del lote 5–7

Se hizo una nueva lectura independiente de la narración concatenada, sin usar título, resumen, arco, notas ni narrative_contract para juzgar la historia. Los 13 JSON auditados registran:
- review_basis=lectura_en_frio_solo_narracion
- reviewer_role=auditor_capcot_independiente
- los siete checks explícitos
- score 0–100 y critical_flags

| Project ID | Estado | Score | Motivo crítico registrado |
|---|---:|---:|---|
| 2026-11-05_kids-dia-en-venus | PASS | 88 | Anomalía día sideral/año; progresión y cierre coherentes. |
| 2026-11-05_comida-palomitas | FAIL | 82 | Apertura definicional y repetición de las causas de granos que no revientan. |
| 2026-11-05_inter-arboles-se-comunican | FAIL | 78 | Apertura genérica, sin acción ni anomalía concreta en curso. |
| 2026-11-05_inter-rayo-globular | FAIL | 81 | Apertura histórica descriptiva; el episodio instrumental llega después. |
| 2026-11-06_kids-ballena-azul-corazon | FAIL | 80 | El cierre sobreafirma que el corazón «casi se detiene». |
| 2026-11-06_comida-aguacate-negro | FAIL | 79 | Las escenas 5–6 repiten mecanismo y límite sin avance causal. |
| 2026-11-06_inter-ranas-congeladas | FAIL | 83 | Las escenas 5–6 repiten especie y condiciones de la evidencia. |
| 2026-11-06_inter-arena-cantante | PASS | 94 | Avalancha, mecanismo, mediciones y condiciones progresan causalmente. |
| 2026-11-07_kids-huesos-bebe | FAIL | 82 | La escena 6 repite el matiz de conteo y fusión de la escena 5. |
| 2026-11-07_comida-hielo-caliente | FAIL | 81 | Abre con una creencia general, no con el fenómeno en curso. |
| 2026-11-07_inter-pulpo-suenos | FAIL | 80 | Repite límites en escenas 5–6 y termina con payoff vago/especulativo. |
| 2026-11-07_inter-nubes-pesan | FAIL | 78 | La escena 7 repite cifra y límite; no paga la apertura con el mecanismo de suspensión. |

La revisión anterior del 3-nov había marcado nubes PASS 91. La lectura actual del storyboard canónico encuentra que su última escena vuelve a los 500,000 kg y a que no todas las nubes son iguales, ya expuestos, en lugar de cerrar con el mecanismo que explica por qué las gotas permanecen suspendidas. El JSON actual prevalece y queda en FAIL 78.

### Identidad de árboles

El storyboard canónico actual 2026-11-05_inter-arboles-se-comunican trata redes micorrícicas comunes / wood-wide web y coincide con el tema del horario. La variante sobre respiración nocturna está en cola/bloqueados/2026-11-05_inter-arboles-mito-respiran/, con otro project_id. La descripción previa que atribuía respiración al borrador canónico no coincide con el contenido vivo de GitHub. El canónico sigue en FAIL por su apertura genérica, no por desajuste temático.

### Identidad de nubes

cola/bloqueados/2026-11-07_extra-nubes-pesan/storyboard.json tiene project_id=2026-11-07_inter-nubes-pesan y su estado indica MATERIAL_DE_ORIGEN_NO_ES_PROYECTO. La variante extra no se contó como un segundo proyecto. También existe un JSON bloqueado de primer nivel con el mismo project_id; ambas son variantes heredadas. El único proyecto canónico del lote es el storyboard de proyectos/2026-11-07_inter-nubes-pesan/.

## 4. Validación estructural y de medios

No había runtime local del repositorio disponible. No se ejecutaron validar_storyboard.py, registro_editorial.py ni procesar_cola.py. Se hizo revisión estática de sus fuentes y se contrastaron los JSON con las reglas del validador.

**Bloqueo estructural común a los doce:** todas las escenas carecen de los seis campos obligatorios:
- dramatic_beat
- scene_function
- causal_bridge_from_previous
- question_state
- reason_to_continue
- new_information

Los dos PASS narrativos (Venus y arena) fallan igualmente la compuerta estructural. Por eso no se promueve ninguno.

Otros hallazgos:
- Los doce tienen 7 escenas, excepto árboles con 8; la duración suma 78 s de escenas + 6 s de cortinilla = 84 s.
- Los doce mantienen voz edge-tts / es-MX-JorgeNeural, rate +7%, pitch -2Hz; ganchos de máximo seis palabras y cierre hablado requerido.
- Árboles tiene **169 palabras**, por debajo del mínimo 170; además carece de capa mapa y de dato/gráfico.
- Árboles usa un prompt_base distinto al literal del catálogo y sus image_prompt no empiezan con el prompt_base vigente.
- Ranas incluye una capa de dato «Hasta −16 °C» con URL PubMed 23966588, pero esa fuente no figura en sources y la cifra no aparece en la narración. No se añadió ni retiró evidencia.
- Los source_ids de escena resuelven a fuentes declaradas. Las fuentes institucionales sin DOI tienen URL; no se ejecutó resolución externa de todos los DOI.
- Diez paquetes usan ambiente genérico «Ambiente discreto; voz al frente» y sfx=[] en todas las escenas. Rayo y arena también tienen escenas sin SFX. La receta exige que el silencio se exprese explícitamente; el validador actual solo comprueba presencia de campos y no detecta esta falta de diseño sonoro.
- En los doce: approved_assets=[], export.render_status=NOT_GENERATED y no aparecen asset_filename, asset_type ni rutas de medios.
- No se cuentan prompts ni placeholders como medios.

El borrador del cielo del 4-nov sí tiene mapa, dato, prompt_base correcto, seis campos narrativos por escena y los demás parámetros estructurales. Su bloqueo es de selección editorial, no de estructura.

## 5. Handoff, cola y recepción de Grok

Inventario del árbol:
- cola/entrada/: únicamente .gitkeep.
- handoffs/grok_inbox/: únicamente README.md; no hay marcadores de paquete.
- cola/estado/: no contiene archivos.
- salidas/ para 5–7 nov: ninguna.
- cola/entrada/<project_id>.json: ninguno de los 13 IDs.

**Dispatchabilidad:** los trece borradores en proyectos/ son NOT_DISPATCHABLE desde su ubicación actual. El workflow escucha cola/entrada/*.json y el selector manual busca JSON con profundidad máxima 1. No toma proyectos/<id>/storyboard.json ni paquetes anidados. Los archivos bloqueados tampoco son dispatchables.

Para cada uno de los doce proyectos 5–7 y el respaldo del 4-nov:
**RECEPCION_GROK_NO_CONFIRMADA**. No se creó ni modificó cola/estado.

### Actions

La ejecución más reciente del workflow capcot-grok-dispatch.yml es la #147, run 41306776689, push del 1-nov-2026 12:29:58Z (06:29:58 CDMX), conclusión failure. Los logs muestran literalmente:
- «Falta configurar GROK_WEBHOOK_URL.»
- «Falta configurar GROK_WEBHOOK_TOKEN.»

El job se detuvo con exit code 1 en la comprobación de GROK_WEBHOOK_URL; los logs muestran ambas variables sin configurar. Se registran solo sus nombres, nunca valores. Las ejecuciones inmediatamente anteriores (#146 y #145) también fallaron por la misma comprobación. No hay ejecuciones posteriores del workflow desde el 1-nov.

El workflow actual en la rama tiene webhook opcional y crea un marcador pendiente en handoffs/grok_inbox; eso no equivale a recepción de Grok. No hay marcadores individuales ni estados de Grok en el árbol actual.

### Procesador y registro editorial

- procesar_cola.py usa por defecto la fecha local America/Mexico_City y filtra por el prefijo de fecha del nombre del JSON o de la carpeta. No procesa automáticamente colas históricas. El parámetro --fecha permite una fecha explícita y el selector no contrasta fecha_objetivo dentro del storyboard.
- El procesador admite JSON de primer nivel y carpetas con storyboard.json; el workflow de despacho solo escucha/selecciona JSON de primer nivel. Es una diferencia de capacidad que debe mantenerse visible.
- registro_editorial.py recorre proyectos, entrada y salidas con glob de un nivel; no recorre recursivamente cola/bloqueados/. La revisión manual de bloqueados fue necesaria para reconciliar variantes.

## 6. Guardia de producción preexistente — 4-nov

Los tres proyectos siguientes tienen salidas/<project_id>/, storyboard, publicacion.json, metadata, licencias y archivos de plataforma. No se redispatchan.

| Proyecto | YouTube ID | Programación CDMX | Privacidad YouTube | TikTok / Facebook |
|---|---|---:|---|---|
| 2026-11-04_kids-hipo-por-que | Rg-iTgMExWw | 07:00 | private | programado / programado |
| 2026-11-04_comida-miel-no-caduca | jpDyCX6zSgQ | 13:30 | private | programado / programado |
| 2026-11-04_inter-bioluminiscencia-mar | 4xylLT3vSIU | 17:00 | private | programado / programado |

YouTube registra uploadStatus=uploaded y publishAt para cada uno; los horarios UTC equivalen a los slots CDMX de la tabla. Los tres tienen selfDeclaredMadeForKids=false y containsSyntheticMedia=true. TikTok declara ai_label=true; Facebook ai_label=false.

**Discrepancias de evidencia:**
- Falta qa.json en las tres salidas. No hay duración audiovisual medida ni QA local que permita comprobar 75–90 s.
- Los storyboards de salidas contienen asset_filename de frames y publicacion.json referencia capsula.mp4, pero esos archivos no están en el árbol GitHub. Estado: **MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO**.
- A la vez, approved_assets=[] y export.render_status=NOT_GENERATED. No se infiere que los medios existan por los nombres de archivo ni por los IDs de plataforma.
- Los storyboard de salidas no contienen narrative_contract ni narrative_qa. No son aptos para una nueva promoción.
- ESTADO_EJECUCION.md decía PREPARADO_PENDIENTE_REVISION_GROK y Publicación pendiente, aunque publicacion.json contiene IDs subidos y slots programados. Se corrigió únicamente el campo Estado documental a BORRADOR_EN_PROYECTOS_NO_APTO_PARA_PROMOCION en los tres archivos de salidas y sus tres copias bloqueadas. No se modificaron IDs, horarios, privacidad, plataformas ni servicios externos.
- Esta corrección no cancela ni revierte la programación existente. La clasificación sigue siendo **PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR**.

**Error bibliográfico en bioluminiscencia:** la descripción programada de 2026-11-04_inter-bioluminiscencia-mar atribuye ambos DOI a revisiones sobre miel de 2022. Los DOI identifican realmente:
- 10.1126/science.1174269: Edith A. Widder, «Bioluminescence in the ocean: origins of biological, chemical, and ecological diversity», Science, 7-may-2010. https://pubmed.ncbi.nlm.nih.gov/20448176/
- 10.1007/s42995-024-00250-0: Laurent Duchatelet y Sam Dupont, «Marine eukaryote bioluminescence: a review of species and their functional biology», publicado en línea el 20-sep-2024 y en volumen 7 (2025). https://link.springer.com/article/10.1007/s42995-024-00250-0

fuentes.md de la copia bloqueada contiene las referencias de bioluminiscencia correctas, pero storyboard/publicacion mantienen los títulos y fechas de miel. No se modificó metadata/publicacion porque el proyecto ya tiene ID y programación preexistente; no se hizo corrección externa.

data/endscreens_rotacion.json registra cambios aplicados en Studio para los IDs de hipo y miel, y el destino de pantalla final entre ellos. Esto refuerza la clasificación de procesamiento preexistente, pero no sustituye QA audiovisual ni prueba recepción por el estado de Grok.

No existe un archivo dedicado historial_youtube en el árbol. data/horario contiene yt_id_historial en registros anteriores, pero no hay historial individual de 4–7 nov que permita afirmar un duplicado. Los tres IDs actuales se registran como IDs de sus respectivos slots, no como historial.

## 7. Rotación, data y contradicciones de catálogo

- data/temas_del_dia.json llega hasta 28-oct; no contiene 4–7 nov.
- data/rotacion.json tiene 27 registros y no contiene 4–7 nov.
- data/publicaciones.json tiene 22 registros y no contiene 4–7 nov.
- data/cola.json conserva un registro fallido de 31-oct; no tiene entradas del 4–7 nov.
- data/estilos_usados.json tiene 21 registros, el último del 28-oct; no registra los estilos actuales.
- Los doce storyboard tienen estilos declarados del catálogo; el prompt_base solo falla en árboles. Hay estilos repetidos en días distintos, pero no repetición consecutiva en la secuencia de slots auditada. La rotación completa no puede certificarse porque data/estilos_usados está atrasado.
- docs/ESTILOS_VISUALES.md declara 50 estilos, mientras scripts/estilos.json contiene 51.
- templates/storyboard.template.json es una plantilla genérica antigua 16:9/120 s con asset_filename y rutas; la plantilla vertical vigente es templates/storyboard_vertical.template.json. La guía debe seguir señalando la plantilla vertical para evitar que otro agente use la antigua.
- Los RADAR 5–7 nov y el Plan Maestro conservan textos de 19:00 que contradicen el horario vigente de 17:45.

## 8. Cambios realizados y límites

Cambios realizados en GitHub, solo en esta rama:
1. Se registró/actualizó narrative_qa en los 13 storyboard de proyectos/ con la lectura en frío del 4-nov. No se reescribió narración, claims, fuentes ni decisión editorial.
2. Se corrigió el token Estado de seis ESTADO_EJECUCION.md del 4-nov: tres copias en cola/bloqueados y tres en salidas. No se alteraron otros campos de producción.
3. Se creó este reporte.

No se modificó data/*.json, main, workflows, secretos, permisos, cola/entrada, cola/estado, storyboard de Machu Picchu, slot 23:30 ni kids 3-nov. No se hizo merge, no se dispararon Actions, no se enviaron payloads externos, no se generaron medios ni se consumieron créditos.

La revisión de API oficial no se ejecutó: no se identificó en esta auditoría un cambio oficial nuevo que justificara abrir esa línea. La validación de scripts fue estática; no se ejecutó un runtime del repositorio.
