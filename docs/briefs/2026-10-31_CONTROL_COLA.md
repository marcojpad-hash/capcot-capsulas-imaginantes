# CONTROL DE COLA CAPCOT — 2026-10-31

**Repositorio:** marcojpad-hash/capcot-capsulas-imaginantes  
**Rama auditada:** feature/capcot-video-discovery-continuity  
**HEAD de la rama:** 676d8ae62519fd8ab56ed8bfa5b0ddbcba9cde60  
**Corte:** 2026-10-31  
**Tipo:** auditoría de cola, estructura, rotación, estados y consistencia. Sin producción de medios.

## 1. Resultado ejecutivo

La auditoría anterior de este archivo quedó superada por nuevas entradas y salidas en la rama. El estado actual no es «una sola entrada fechada 31-oct y ninguna producción»:

- El único storyboard asignado al slot del **31-oct 23:30** es Pardelas, pero hay **cuatro JSON con prefijo 2026-10-31** en cola: Pardelas, murciélagos, sequías y SmartPE. Los otros tres tienen fecha de creación 31-oct y están asignados a slots del 2 y 3 de noviembre.
- Murciélagos, sequías y SmartPE ya tienen carpetas de proyecto/salida, QA JSON y registros de carga privada/programación en YouTube. Sus QA no pasan todos los checks.
- Camarón mantis y pan duro tienen QA JSON con 21/21 checks en true y registros de YouTube subidos como privados y programados. El video de pan dura 74.33 s, por debajo del mínimo editorial de 75 s. TikTok y Facebook siguen explícitamente pendientes en sus registros de publicación.
- Tiburón de Groenlandia y Maillard ya tienen paquetes textuales completos para el 3-nov, cada uno con storyboard, fuentes y estado de ejecución. El horario semanal todavía los marca como pedir_chatgpt.
- No existe ningún archivo cola/estado para los proyectos revisados. La recepción formal por Grok no está confirmada. Los QA JSON y los registros de plataforma son evidencia de artefactos, pero no permiten atribuir su ejecución a Grok.
- Hay contradicciones entre horario semanal, publicación por plataforma, IDs de YouTube, storyboards de salida y documentos operativos. No se corrigieron estados ni IDs porque requieren verificación de plataforma o decisión del responsable.

## 2. Brief vigente y unicidad

### Briefs leídos

- ajustes_entre_modelos/PARA_CHATGPT_semana_01-07nov.md, actualizado 2026-10-31 14:48 CDMX.
- ajustes_entre_modelos/PARA_CHATGPT_tips_ciencia_hack_31oct.md.
- docs/briefs/2026-10-31_RADAR_CAPCOT.md.
- docs/briefs/2026-10-31_CAPSULAS_PENDIENTES_GROK.md.
- docs/briefs/2026-10-31_AUDITORIA_INTEGRIDAD_CAPCOT.md.
- Este CONTROL_COLA, que contenía una fotografía anterior de la cola y se reemplaza con esta actualización.

### Entradas con prefijo 31-oct

| Project | Slot objetivo según horario/brief | Evidencia en cola/proyectos/salidas |
|---|---|---|
| 2026-10-31_pardelas-jetlag-solar | 31-oct 23:30 | JSON de cola; sin carpeta de proyecto ni salida verificable |
| 2026-10-31_murcielagos-viroma-global | 2-nov 17:00 | JSON de cola, proyecto, salida, QA y publicación YT |
| 2026-10-31_sequias-energia-renovable | 2-nov 19:00 | JSON de cola, proyecto, salida, QA y publicación YT |
| 2026-10-31_smartpe-edicion-plantas | 3-nov 19:00 | JSON de cola, proyecto, salida, QA y publicación YT |

Por tanto, hay un solo candidato textual para el slot 31-oct 23:30, pero no hay una sola entrada con prefijo 31-oct. El procesador selecciona por prefijo de archivo/directorio; al ejecutarse con fecha 2026-10-31 encuentra las cuatro. No debe confundirse fecha de creación del paquete con fecha objetivo de publicación.

### Paquetes del 3-nov añadidos a la cola

- 2026-11-03_kids-tiburon-groenlandia: paquete completo, 07:00 CDMX.
- 2026-11-03_comida-maillard: paquete completo, 13:30 CDMX.
- No existe todavía un paquete intermedio nuevo para 3-nov 17:00.

La tabla de data/horario_semana_2026-11-01_07.json todavía marca tiburón y Maillard como pedir_chatgpt, aunque ambos paquetes ya existen. El brief semanal también conserva esos dos pendientes. Esos estados no se actualizaron porque no se modifican data/*.json.

### Conflicto Juno

El horario semanal y el brief actualizado colocan 2026-10-29_juno-choque-proa en 3-nov 17:00. La instrucción editorial previa de Mj fue no reutilizar Juno y cubrir ese slot con un intermedio nuevo. No se creó ni seleccionó un reemplazo en esta auditoría y no se modificó el horario. El conflicto sigue abierto.

### Dato-día

Los slots de 23:30 continúan como TBD y deben producirse el mismo día con noticia de hasta 48 horas y fuente primaria. No se adelantó ninguno.

## 3. Validación de los storyboards con prefijo 31-oct

La validación se hizo mediante lectura y parseo estático del JSON. Los cuatro tienen ocho escenas, arco completo, voz prevista correcta, source_ids resolubles y prompts que comienzan con el prompt_base literal de su estilo. Los cuatro JSON de cola no contienen rutas de assets; approved_assets está vacío y render_status es NOT_GENERATED.

| Proyecto | Palabras | Duración declarada | Gancho | Mapa/dato | Hallazgo |
|---|---:|---:|---:|---|---|
| Pardelas | 218 | 78 + 6 = 84 s | 6 | Sí / sí | Cumple la estructura. Falta music_plan; music_asset y music_license son null. El SFX «latido» no existe en scripts/sfx_manifest.json. |
| Murciélagos | 131 | 78 + 6 = 84 s | 4 | No / no | No cumple 170–235 palabras ni las dos capas obligatorias. |
| Sequías | 152 | 78 + 6 = 84 s | 4 | No / no | No cumple 170–235 palabras ni las dos capas obligatorias. |
| SmartPE | 150 | 78 + 6 = 84 s | 4 | No / no | No cumple 170–235 palabras ni las dos capas obligatorias. |

### Fuentes y estilos

- Pardelas: cuatro fuentes; DOI principal 10.1126/science.adz2542. Los source_ids de escena resuelven. Estilo papel_rasgado_capas.
- Murciélagos: dos registros de fuente con DOI 10.1038/s41467-026-79059-7. Estilo acuarela_linea.
- Sequías: fuente con DOI 10.1038/s43247-026-04183-7. Estilo constructivista_ruso.
- SmartPE: tres fuentes; DOI principal 10.1038/s41477-026-02447-w. Estilo pixel_art.

Los cuatro estilos existen en scripts/estilos.json y los prompts base coinciden literalmente. No se detectó repetición de los estilos de murciélagos, sequías o SmartPE con los cinco estilos registrados para la parrilla del 31-oct. Pardelas usa papel_rasgado_capas; ese estilo ya aparece en data/rotacion.json el 24-oct, por lo que no es históricamente inédito.

### QA de los tres paquetes asignados a fechas futuras

Los siguientes resultados son lo que dicen los archivos QA; no se atribuyen a Grok porque falta cola/estado:

| Proyecto | Checks | Fallos registrados | Duración del archivo |
|---|---:|---|---:|
| Murciélagos | 19/21 | capa_mapa; capa_grafico_o_dato | 65.47 s |
| Sequías | 19/21 | capa_mapa; capa_grafico_o_dato | 77.37 s |
| SmartPE | 18/21 | subs_max_3_palabras; capa_mapa; capa_grafico_o_dato | 77.00 s |

Los tres registros de publicación muestran YouTube uploaded, privacyStatus private y publishAt futuro:
- Murciélagos: dFwKjIb8tFI, 2-nov 17:00 CDMX.
- Sequías: SQ7_g-vz8Ow, 2-nov 19:00 CDMX.
- SmartPE: MXsNOywNzcg, 3-nov 19:00 CDMX.

Los storyboards de producción de estos tres paquetes cambiaron la voz a rate -2% y pad_seconds 0.7; el contrato vigente exige +7% y pad_seconds 0.3. Sus estados de producción siguen diciendo MONTADO_PENDIENTE_PROGRAMAR aunque publicacion.json registra carga privada y publishAt. El QA existente no comprueba el rate/pad de voz.

El brief docs/briefs/2026-10-31_CAPSULAS_PENDIENTES_GROK describe guiones de aproximadamente 190 palabras y mapas/gráficos para estas piezas. Los JSON contienen 131, 152 y 150 palabras, y carecen de ambas capas; los QA confirman esa ausencia. El brief no representa el contenido real de los tres storyboards.

## 4. Paquetes del 2-nov: camarón mantis y pan duro

Los paquetes de cola están en carpetas con storyboard.json, fuentes.md y ESTADO_EJECUCION.md. Sus storyboards textuales cumplen los parámetros principales:

| Proyecto | Palabras | Escenas | Duración | Estilo | Mapa/dato |
|---|---:|---:|---:|---|---|
| 2026-11-02_camaron-mantis | 181 | 8 | 84 s | teatro_sombras | Sí / sí |
| 2026-11-02_comida-pan-duro | 186 | 8 | 84 s | papel_rasgado_capas | Sí / sí |

Los QA JSON contienen 21/21 checks en true:
- Camarón mantis: 75.35 s.
- Pan duro: 74.33 s. Aunque el QA JSON lo acepta porque su regla de duración es 60–120 s, el contrato editorial vigente exige 75–90 s; queda 0.67 s por debajo del mínimo.

Los registros YouTube muestran:
- Camarón mantis: tmxMkxA6nOw, uploaded/private, publishAt 2-nov 07:00 CDMX.
- Pan duro: TbZRvpiDjdk, uploaded/private, publishAt 2-nov 13:30 CDMX.
- En ambos, selfDeclaredMadeForKids=false.
- En ambos, tiktok.estado=pending_tiktok y facebook.estado=pending_fb.

Esto contradice data/horario_semana_2026-11-01_07.json, que marca ambos como programado_yt_tt_fb. Para esos dos proyectos, la evidencia de publicación confirma YouTube privado programado; TikTok y Facebook siguen pendientes en publicacion.json.

Los storyboards copiados en proyectos/ y salidas/ todavía conservan asset_filename de ocho frames, render_status=NOT_GENERATED y publicacion.status=PENDIENTE_DECISION_GROK, aunque existen QA JSON y registros de YouTube uploaded/private con publishAt. El estado de esos storyboards no está reconciliado con los artefactos de producción.

En metadata.json, contiene_ia=true coexiste con contenido_sintetico=false; publicacion.json también registra containsSyntheticMedia=false, mientras la descripción declara imágenes generadas con IA, voz sintética y audio sintetizado. Es una inconsistencia de metadata que requiere revisión; no se cambió el indicador.

## 5. Validación de los paquetes del 3-nov

Ambos paquetes ya están en la estructura de carpeta solicitada y sus estados de ejecución indican PREPARADO_PENDIENTE_REVISION_GROK, medios no generados y recepción no confirmada.

| Proyecto | Palabras | Escenas | Duración | Gancho | Estilo | Mapa/dato |
|---|---:|---:|---:|---:|---|---|
| Tiburón de Groenlandia | 211 | 8 | 84 s | 4 palabras | crayones_infantiles | Sí / sí |
| Reacción de Maillard | 188 | 8 | 84 s | 4 palabras | linea_fina | Sí / sí |

Los dos cumplen serie, idioma, formato, voz +7%/-2Hz/pad 0.3, arco, cierre hablado, source_ids, DOI, prompt_base literal, ambiente/SFX por escena, approved_assets vacío, render NOT_GENERATED y publicación pendiente. Los DOI están consignados como VERIFICADO_RESOLVEDOR:
- Tiburón: 10.1126/science.aaf1703.
- Maillard: 10.1021/acs.jafc.7b00882 y 10.1021/acs.jafc.6b04367.

Pendientes concretos:
- Tiburón: el SFX «Pulso grave» no es una clave de scripts/sfx_manifest.json.
- Maillard: el SFX «Tostado leve» no es una clave de scripts/sfx_manifest.json. La capa mapa coloca un pin en CDMX como referencia editorial y declara que no representa el descubrimiento ni una medición. Tiene coordenadas numéricas, pero no es un mapa geográfico informativo del fenómeno y no aporta fuente cartográfica. No se sustituyó por un diagrama porque eso cambiaría la decisión visual.
- Maillard usa una revisión de 2017 para el mecanismo general y un estudio original de pan de 2016 para el resultado corteza/miga. El claim de mecanismo general depende de la revisión; el estudio original respalda el hallazgo específico de pan.

## 6. Estados por etapa

| Proyecto | Propuesta/paquete | Recepción Grok | Producción | QA en archivos | Publicación |
|---|---|---|---|---|---|
| Pardelas | Sí | No confirmada | Sin carpeta de salida verificable | Sin QA localizado | Horario dice programado, pero ID contradictorio |
| Murciélagos | Sí | No confirmada | Salida y registro de carga YT | QA 19/21, dos fallos | YT privado programado; TT/FB sin evidencia |
| Sequías | Sí | No confirmada | Salida y registro de carga YT | QA 19/21, dos fallos | YT privado programado; TT/FB sin evidencia |
| SmartPE | Sí | No confirmada | Salida y registro de carga YT | QA 18/21, tres fallos | YT privado programado; TT/FB sin evidencia |
| Camarón mantis | Sí | No confirmada | Salida/QA/publicación registrados | QA 21/21 | YT privado programado; TT/FB pendientes |
| Pan duro | Sí | No confirmada | Salida/QA/publicación registrados | QA 21/21; duración 74.33 s | YT privado programado; TT/FB pendientes |
| Tiburón | Sí | No confirmada | No generado | No hay QA | Pendiente |
| Maillard | Sí | No confirmada | No generado | No hay QA | Pendiente |

No existe cola/estado/ para ninguno de estos proyectos. Los archivos ESTADO_EJECUCION.md son registros de preparación, no estados de Grok. No se atribuye recepción, selección ni QA a Grok.

## 7. Parrilla del 31-oct e IDs en conflicto

data/horario_2026-10-31.json registra cinco slots. Hay tres inconsistencias:

- Corales: el horario aún dice programado_yt, mientras data/endscreens_rotacion.json y el cierre operativo lo describen público desde 13:30.
- Kromdraai: data/horario y data/publicaciones conservan ILDMoFhsH74; el campo youtube_id y los documentos operativos señalan MBMjQ5vLZo0. El cierre operativo dice que ILDMoFhsH74 fue borrado.
- Pardelas: data/horario contiene yt_id MSiwJnSu_Dk, youtube_id rLd9DVPXHb8 y youtube_id_old_corrupt IBH8Q95BGVs. data/publicaciones conserva MSiwJnSu_Dk; parrilla_yt.md lista IBH8Q95BGVs y parrilla_cierre.md lista rLd9DVPXHb8. El cierre dice que los duplicados fueron borrados, pero los registros JSON no quedaron reconciliados. Tampoco existe carpeta salidas/2026-10-31_pardelas con QA/publicacion verificables.

No se eligió un ID canónico sin consultar YouTube Studio/API. No se modificaron data/*.json.

Pulpo y cebolla del 1-nov no se reprocesaron. Sus registros YouTube muestran uploaded/private y publishAt para sus slots. El documento operativo TT+FB indica programación en esas plataformas; publicacion.json conserva evidencia de YouTube, no un estado API equivalente para TT/FB.

## 8. Rotación, registro editorial y procesador

### Registro editorial

scripts/registro_editorial.py une data/rotacion.json, data/publicaciones.json, data/cola.json y storyboards de cola/proyectos/salidas, deduplicando por project_id. No lee data/horario_semana_2026-11-01_07.json, QA JSON ni publicacion.json de cada salida.

Por fecha derivada del prefijo project_id, el registro combina cinco piezas del 31-oct con tres paquetes que en realidad se publicarán el 2/3-nov: ocho project_id únicos. Esto sobrecuenta el 31-oct y no asigna esas piezas a sus fechas objetivo. La rotación de 2/3-nov no se puede certificar usando esta vista.

### Procesador

scripts/procesar_cola.py filtra estrictamente por los primeros diez caracteres del archivo o directorio. Excluye las entradas históricas 25–30 cuando se procesa 31-oct, pero selecciona los cuatro JSON con prefijo 31-oct. No usa la fecha objetivo de data/horario_semana. Los paquetes de murciélagos, sequías y SmartPE no serían seleccionados al ejecutar por sus fechas objetivo 2/3-nov porque su prefijo es 31-oct; actualmente ya tienen salidas y programación YT registradas.

El procesador tampoco llama a rotacion.diferencias_con_hoy para imponer estructura/estilo/música distintos; aplica cupo y tema ocupado. No se cambió esa regla porque añadirla alteraría decisiones de selección y requiere pruebas de regresión.

### Correcciones mecánicas aplicadas en esta rama

- scripts/procesar_cola.py: el valor por defecto de --fecha ahora usa America/Mexico_City, no la zona local del runner.
- scripts/procesar_cola.py: el project_id se carga antes de revisar cupo y se excluye del conteo, evitando contar dos veces al propio candidato.
- scripts/registro_editorial.py: una copia posterior en proyectos/ o salidas/ ya no convierte el origen externa de un paquete de cola en propia.
- Se añadieron pruebas para la exclusión del candidato y la conservación del origen externo.

Commits:
- 489377a271bad7ed3f7ffc9d12cc7398788b422a — procesador: fecha CDMX y cupo.
- fc81d787be75d354316f24f2e7b7ae28cf698c45 — prueba de capacidad.
- 7c9227f9c73650d6fecfacd0ba674b0de5ccdb6e — conservar origen externo.
- 5f51b84a7806f7aae86916fa5b8a69edeaa5631c — prueba de origen externo.

No se corrigió la semántica de fecha objetivo; requiere un contrato explícito para separar fecha de creación y fecha de publicación.

## 9. Datos, estilos y divergencia de ramas

- data/rotacion.json y data/publicaciones.json llegan al 31-oct.
- data/temas_del_dia.json y data/estilos_usados.json llegan al 28-oct.
- data/balances_6h.json y data/vistas_historico.json en la rama feature llegan al 28-oct 08:08.
- data/endscreens_rotacion.json contiene una actualización del 31-oct.
- main tiene el commit 4c7d8091b72cc01961ad5fd79378c5d0944dd801 con un snapshot del 31-oct 14:12: YT 23,665 vistas, 798 likes, 24 comentarios y 63 suscriptores; el delta consignado frente al 28-oct es +8,549 vistas, +278 likes, +5 comentarios y +22 suscriptores. TikTok: 15 seguidores, 531 likes de perfil y 30 videos. Ese snapshot no está incorporado a feature y no se copió.
- La comparación actual de ramas reporta feature divergida: 191 commits exclusivos por delante y 13 por detrás de main. No se sincronizó ni se hizo merge.
- data/rotacion registra cinco publicaciones del 31-oct. El registro combinado añade los tres paquetes con prefijo 31-oct, aunque sus slots son futuros. El estilo y la rotación musical de 2/3-nov no quedan certificados por data/rotacion.
- Pardelas tiene cama «None» como texto en data/rotacion y Kromdraai no declara cama; no se normalizaron esos valores.

## 10. Documentos y contratos contradictorios

1. docs/PLAN_MAESTRO_AUTOMATICO.md y docs/GUIA_MODELO_EXTERNO.md aún describen entrada como JSON directo con fuentes dentro del JSON y sin archivo _fuentes. El brief semanal y la instrucción operativa más reciente piden carpetas con storyboard.json, fuentes.md y ESTADO_EJECUCION.md. Los paquetes del 3-nov siguen el formato de carpeta; no se movieron las entradas antiguas.
2. PARA_CHATGPT_tips_ciencia_hack_31oct.md permite frames y dice marcar listo para montaje; contradice el Plan/Guía actuales, que prohíben medios y dejan la decisión a Grok.
3. PARA_CHATGPT_semana_01-07nov.md dice «cola JSON ya recibida»; sin cola/estado no se confirma recepción conforme al contrato Grok.
4. docs/LINEAS_TEMATICAS.md sugiere hasta tres cápsulas al día; el contrato superior vigente y el código usan cinco ventanas y tope global de cinco.
5. docs/SKILL_DRAFT_capsula_diaria.md y templates/storyboard.template.json son legados: permiten generación/publicación y usan 16:9/120 s. La plantilla vigente es templates/storyboard_vertical.template.json.
6. docs/briefs/2026-10-31_RADAR_CAPCOT.md y docs/briefs/2026-10-31_AUDITORIA_INTEGRIDAD_CAPCOT.md conservan afirmaciones de ausencia de producción/salidas que ya no describen la rama actual.
7. docs/briefs/2026-10-31_CAPSULAS_PENDIENTES_GROK.md describe aproximadamente 190 palabras y mapas/gráficos para tres paquetes; los JSON y QA no coinciden.
8. El horario semanal y los registros de publicación no coinciden en el estado de TikTok/Facebook para los paquetes del 2/3-nov.
9. El horario semanal coloca Juno el 3-nov 17:00 pese a la instrucción editorial previa de no reutilizarlo.

No se archivaron ni reescribieron esos documentos porque su autoridad o sus decisiones editoriales requieren reconciliación del responsable.

## 11. Runtime, validadores y APIs

- /workspace/capcot no existe en el entorno de esta ejecución.
- No se ejecutaron scripts/validar_storyboard.py, scripts/procesar_cola.py, scripts/registro_editorial.py, scripts/rotacion.py ni las pruebas unitarias. La revisión de storyboards, QA y estados fue estática, mediante lectura de archivos de GitHub y parseo de JSON.
- Se añadieron pruebas, pero no se declara que hayan pasado.
- No se abrió una revisión de APIs: no apareció un cambio oficial nuevo sustentado que justificara actualizar la investigación Meta/Google Trends en este corte.

## 12. Límites y cierre

En esta auditoría:
- No se generaron cápsulas, frames, imágenes, voz, audio, video ni renders.
- No se publicó ni programó nada.
- No se creó ni modificó cola/estado.
- No se modificó data/*.json, main ni Motor U6.
- No hubo merge ni consumo de créditos.

**Conclusión:** la cola contiene dos paquetes textuales nuevos y estructuralmente sólidos para el 3-nov, pero Maillard requiere corregir la semántica del mapa y mapear sus SFX a recursos disponibles. Pardelas cumple estructura, aunque tiene audio incompleto y estado/ID de publicación contradictorio. Murciélagos, sequías y SmartPE ya muestran producción y carga privada YT, pero sus QA fallan y los guiones incumplen longitud/capas. Mantis y pan muestran QA JSON completo y YT programado; pan queda por debajo de 75 s y ambos tienen TT/FB pendientes. La recepción formal por Grok no está confirmada para ningún proyecto sin cola/estado.
