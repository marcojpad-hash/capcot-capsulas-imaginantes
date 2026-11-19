# CONTROL DE COLA — 2026-11-19

Repositorio: marcojpad-hash/capcot-capsulas-imaginantes  
Rama auditada: feature/capcot-video-discovery-continuity  
Corte: 2026-11-19, 15:04 CDMX

## 1. Alcance y fuentes revisadas

Se releen el brief del 19-nov, el control del 18-nov, Plan Maestro, Contrato Operativo Unificado, Receta, Guía de Modelo Externo, Flujo Externo, contrato de estados Grok, QA Narrativo en Frío, catálogo JSON de estilos, plantillas vertical y genérica, registro_editorial.py, procesar_cola.py y capcot-grok-dispatch.yml. También se inspeccionan los 20 JSON existentes bajo data/ en la rama de trabajo y los datos pertinentes de main para cruces de slot, programación y publicación.

La autoridad vigente es CONTRATO_OPERATIVO_UNIFICADO.md, seguida por PLAN_MAESTRO_AUTOMATICO.md, RECETA_CAPSULA.md, GUIA_MODELO_EXTERNO.md y FLUJO_EXTERNO.md. La plantilla vertical es la aplicable. No se generan medios, no se publica, no se programa, no se modifica main ni data/*.json.

## 2. Inventario del día y entradas existentes

El brief docs/briefs/2026-11-19_RADAR_CAPCOT.md existe y presenta dos borradores. No había CONTROL_COLA del 19-nov antes de esta auditoría.

| Artefacto | Creación observada en Git | Fecha objetivo | Slot CDMX / cesta | QA narrativo releído | Estado |
|---|---:|---|---|---|---|
| proyectos/2026-11-19_dato-estrella-dentro-de-estrella/storyboard.json | 19-nov 08:12 | 19-nov | 17:00 / intermedio_1 | PASS 90 | En proyectos; no hay entrada de cola |
| proyectos/2026-11-19_dato-dia-luz-dos-manos-oro-poroso/storyboard.json | 19-nov 08:12 | 19-nov | 23:30 / dato_del_dia | PASS 91 | En proyectos; no hay entrada de cola |

Los dos archivos tienen 8 escenas, 197 y 188 palabras respectivamente, 84 s totales con cortinilla de 6 s, gancho de 5 palabras, voz es-MX-JorgeNeural, source_ids válidos, prompt_base del catálogo, mapa y capa de dato, ambiente/SFX, approved_assets=[] y export.render_status=NOT_GENERATED. No contienen asset_filename, asset_type ni rutas de medios.

La lectura en frío se registró directamente en ambos storyboard.json: los siete checks están en true, review_basis=lectura_en_frio_solo_narracion, critical_flags=[] y reviewer_role=auditor_capcot_independiente. No se reescribió narración ni claims.

Bloqueos:
- El storyboard de oro tiene DOI 10.1038/s41467-026-78158-9 con doi_validation_status=PENDIENTE_RESOLVEDOR. La página/PDF editorial fue consultada, pero no se confirmó el resolvedor/Crossref. Main no contiene una publicación registrada para el 19-nov 23:30; tampoco se encontró un paquete con ese slot. Main sí conserva el proyecto msl-acetilacion del 19-nov sin slot_local, por lo que ese artefacto no permite descartar por sí solo una asignación no registrada.
- El storyboard de la estrella tiene DOI 10.1038/s41586-026-11221-z con verificación pendiente de resolvedor/Crossref. Main no registra paquete para 19-nov 17:00; la parrilla pública de main muestra Juno a las 13:30 y ADN a las 19:00. No hay conflicto exacto de slot, pero art_deco_poster ya figura en la rotación de Juno ese mismo día.
- El mapa celeste de la estrella usa coordenadas RA/Dec. El validador actual solo acepta lat/lon geográficas para puntos; la lectura estática devuelve scene_002:map_point. No se transforma RA/Dec en coordenadas terrestres ni se inventa una proyección.
- art_deco_poster del storyboard de la estrella repite el estilo que main registra para Juno el mismo 19-nov a las 13:30. PLAN_MAESTRO prohíbe repetir estilo el mismo día. Es un conflicto de rotación, no un fallo de lectura narrativa.

No existe cola/estado para ninguno: RECEPCION_GROK_NO_CONFIRMADA. No existe salidas/<project_id>/ para ninguno. Ninguno es dispatchable porque todavía está en proyectos/.

## 3. Backlog inmediato y cruce de ramas

### 3.1 Proyectos del 18-nov

| Proyecto | Creación observada | Objetivo / slot | QA | Validación y cruce |
|---|---:|---|---|---|
| 2026-11-18_dato-catorce-campos-hidrotermales | 18-nov 17:04 | 18-nov / 23:30 | FAIL 68 | QA recién registrado; sin ejecución local del validador; main tiene conflicto exacto de slot |
| 2026-11-18_dato-kuroshio-puente-atmosferico | 18-nov 08:19 | 18-nov / 17:00 | PASS 90 | CI estructural exitoso; DOI resolver/Crossref pendiente |

Catorce campos: la narración enumera localización, métodos, litologías, fluidos, actividad y oxidación, pero no sostiene una pregunta central ni una progresión causal única. El mecanismo que diferenciaría los campos basálticos de los ultramáficos queda nombrado, no explicado; el cierre resume el inventario y no paga la apertura. Se registraron siete checks, score 68 y flags PREGUNTA_CENTRAL_NO_RECONSTRUIBLE, SECUENCIA_DE_HALLAZGOS_SIN_PROGRESION_CAUSAL, GIRO_CIENTIFICO_NOMBRADO_PERO_NO_EXPLICADO y CIERRE_RESUMEN_SIN_PAYOFF. El estado documental se corrigió a BORRADOR_EN_PROYECTOS_NO_APTO_PARA_PROMOCION. No se modificó narración ni evidencia.

Cruce obligatorio de main: cola/entrada/2026-11-18_hielo-sucio-beta-pictoris/programacion.json ya contiene video_id 2a36r5QOvi4, publish_at 2026-11-19T05:30:00Z (18-nov 23:30 CDMX) y privacidad private→público. Es el mismo fecha_objetivo + slot_local que catorce campos. Clasificación: CONFLICTO_DE_SLOT_ENTRE_RAMAS / PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR. Su QA audiovisual mide 61.27 s y solo comprueba 60–120 s; no satisface el contrato 75–90 s. No se cancela ni modifica.

Kuroshio: el run 44417215473, commit f78ab7bc9d312e4b4b87903099707b6e2b0685d1, ejecutó exactamente:
python scripts/validar_storyboard.py proyectos/2026-11-18_dato-kuroshio-puente-atmosferico/storyboard.json
Resultado: OK, salida 0. El comando no incluyó --check-doi. La página editorial y PDF muestran el DOI 10.1038/s41561-026-02139-2, pero el propio storyboard dice RESOLVEDOR_CROSSREF_NO_CONFIRMADO. Por tanto, la validación estructural sí está ejecutada; DOI sigue bloqueando promoción. No hay conflicto exacto de slot en main para 18-nov 17:00. El estado documental se actualizó a BORRADOR_EN_PROYECTOS_NO_APTO_PARA_PROMOCION y se dejó constancia de la corrección: el validador acepta regiones con bounds válidos aunque puntos=[]; el reporte anterior que marcó fallo por puntos vacíos no coincide con el código vigente ni con el CI exitoso.

### 3.2 Proyectos con QA PASS y revisión estática

| Proyecto | QA | Estructura estática | DOI |
|---|---:|---|---|
| 2026-11-10_comida-aprendizaje-sabor-nutriente | PASS 92 | Sin errores estáticos | PENDIENTE |
| 2026-11-10_dato-adn-sincroniza-flujo | PASS 91 | Sin errores estáticos | DOI visible en fuente primaria; resolvedor pendiente |
| 2026-11-12_dato-pedorreta-chimpances | PASS 91 | Sin errores estáticos | PENDIENTE_RESOLVEDOR |
| 2026-11-13_dato-caracol-16-embriones | PASS 91 | Sin errores estáticos | PENDIENTE_RESOLVEDOR |
| 2026-11-14_dato-microplasticos-pantanal | PASS 88 | Sin errores estáticos | VERIFICADO_RESOLVEDOR |
| 2026-11-15_dato-dia-diapausa-lestes-sponsa | PASS 90 | Sin errores estáticos | VERIFICADO_RESOLVEDOR |
| 2026-11-16_dato-polen-desenreda-nanotubos | PASS 91 | Sin errores estáticos | PENDIENTE_RESOLVEDOR |
| 2026-11-17_dato-suelo-dos-relojes | PASS 89 | Sin errores estáticos | VERIFICADO_FUENTE_PRIMARIA_Y_CROSSREF |

Los proyectos del 14, 15 y 17-nov son los únicos de este grupo con QA PASS, revisión estructural estática sin errores y DOI verificado. No se promovieron: no se ejecutó el validador oficial para esos archivos y la instrucción de este run prohíbe disparar workflows o crear entradas que activarían dispatch. Los demás conservan su bloqueo DOI. 2026-11-15_dato-quasar-pareja-cosmic-dawn permanece FAIL 82, con progresión y transición causal fallidas.

2026-11-09_dato-robot-ensambla-orbita tiene QA PASS 90 en el proyecto de la rama de trabajo. Sin embargo, main contiene un paquete de producción en cola/entrada/2026-11-09_dato-robot-ensambla-orbita/: capsula.mp4, frames, qa.json, metadata y programación. Está programado para 21-nov 19:00 CDMX con YouTube ZG4iQgmWrLI (privacidad private→público); TikTok y Facebook figuran programados sin IDs. El storyboard de main declara 95 s, mientras qa.json mide 87.57 s y solo valida 60–120 s. Hay deriva de versión frente al proyecto de la rama, que declara 88 s. Clasificación: PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR. La nota de programación dice “montaje 2026-11-14 (Grok Bot)”, pero handoffs/grok_inbox conserva status=pending y no existe estado Grok ni archivo en grok_done: no se atribuye recepción formal ni QA a Grok.

## 4. Lote obligatorio 5–7 noviembre

Los 12 IDs se compararon con data/horario_semana_2026-11-01_07.json. project_id, fecha_objetivo, slot_local y slot_cesta coinciden. El slot 2026-11-07 17:45 corresponde exactamente a 2026-11-07_inter-nubes-pesan; extra-nubes-pesan es material de origen, no segundo proyecto. El storyboard canónico de árboles sigue tratando redes micorrícicas y Karst et al. 2023: no se marca desajuste temático. El blob SHA histórico indicado para el canónico es 854c12ed9b77f82f66ec736797dea4d700983d78; el blob actual de la copia con QA es 05618f1d5d2cd8f713ee43ac802bcfb04bb9bb1d. La diferencia corresponde al archivo actualizado, no a un cambio de tema. La variante de respiración nocturna en bloqueados es otro artefacto.

Los 12 tienen 7–8 escenas, 170–221 palabras, 78 s de escenas + 6 s de cortinilla, ganchos de 3–5 palabras, approved_assets=[] y render_status=NOT_GENERATED. No hay asset_filename ni asset_type en estos storyboard.json. Sin embargo, todos omiten los seis campos narrativos obligatorios por escena (dramatic_beat, scene_function, causal_bridge_from_previous, question_state, reason_to_continue, new_information). Además, los arrays SFX están vacíos en la mayoría de las escenas; la Receta exige declarar el silencio explícitamente. El proyecto de árboles tampoco tiene capa de mapa ni de dato/gráfico. Por tanto, los dos QA PASS no superan la compuerta estructural.

| ID | Slot | QA leído de GitHub | Fallos/observación principal | Producción preexistente |
|---|---:|---|---|---|
| 2026-11-05_kids-dia-en-venus | 07:00 | PASS 88 | Estructura falla por seis campos narrativos ausentes por escena | TikTok 7705488176793652481 Everyone, 7-nov 17:00; Facebook 2544385142727016 Public, 7-nov 17:58. Sin ID YouTube. MP4 referenciado en /workspace/capcot_prod_20261107/venus/, no está en GitHub |
| 2026-11-05_comida-palomitas | 13:30 | FAIL 82 | Apertura definicional; escena 6 repite causas sin información nueva | YouTube zTP5akrGA9M; TikTok 7705593452003691794 Everyone; Facebook 1167496802382795 Público; 8-nov 07:00. MP4 externo a GitHub |
| 2026-11-05_inter-arboles-se-comunican | 17:00 | FAIL 78 | Apertura genérica; 170 palabras; faltan mapa y dato/gráfico, además de campos narrativos | Main contiene otro ID, 2026-11-07_arboles-comunicacion-bosque, con YouTube EX0W3q-yKRw, privado programado para 13-nov 13:30. Es duplicación temática bajo otro ID, no el storyboard canónico. QA audiovisual 87.50 s solo acepta 60–120 s; capsula.mp4 no está en el árbol GitHub |
| 2026-11-05_inter-rayo-globular | 17:45 | FAIL 81 | Apertura histórica descriptiva | Copia heredada en cola/bloqueados; sin evidencia de producción |
| 2026-11-06_kids-ballena-azul-corazon | 07:00 | FAIL 80 | Payoff sobreafirma “casi se detiene” | YouTube wbFrlM2e_YE; TikTok 7705594333574991122 Everyone, 11-nov 07:00; Facebook Público programado sin ID. MP4 externo |
| 2026-11-06_comida-aguacate-negro | 13:30 | FAIL 79 | Escenas 5–6 repetidas, sin avance causal | YouTube nSS_q2tj2P0; TikTok 7705594217136966920 Everyone, 10-nov 07:00; Facebook Público programado sin ID. MP4 externo |
| 2026-11-06_inter-ranas-congeladas | 17:00 | FAIL 83 | Repetición entre escenas 5–6; límites de especie/condiciones | YouTube UBFuKBU3cx0; TikTok 7705596671807245586 Everyone, 9-nov 07:00; Facebook Público programado sin ID. MP4 externo |
| 2026-11-06_inter-arena-cantante | 17:45 | PASS 94 | Estructura falla por seis campos narrativos ausentes por escena | TikTok 7705502155427368212 Everyone, 7-nov 13:30; Facebook 2224920108452190 Public, 7-nov 17:58; YouTube m4RqQRaz55k público. Segundo ID ztIkYcXB91U sigue descrito como programado a las 19:00, sin privacidad registrada: riesgo de duplicado. MP4 externo |
| 2026-11-07_kids-huesos-bebe | 07:00 | FAIL 82 | Escena 6 repite variación de conteo/fusión | Copia bloqueada; sin producción verificada |
| 2026-11-07_comida-hielo-caliente | 13:30 | FAIL 81 | Apertura de creencias, no in medias res | Main tiene cola y salidas del mismo ID. YouTube HSgrnejAcaI privado programado 11-nov 13:30; TikTok 7706905447424347393 Everyone programado; Facebook asset 1460158683840154 Público, estado “En proceso”. QA audiovisual mide 89.83 s, pero su prueba solo acepta 60–120 s. capsula.mp4 referenciado no está en el árbol GitHub: MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO |
| 2026-11-07_inter-pulpo-suenos | 17:00 | FAIL 72 | Fuente primaria corresponde a Octopus laqueus, no O. insularis; repetición y payoff vago | Sin producción verificada |
| 2026-11-07_inter-nubes-pesan | 17:45 | FAIL 78 | Escena 7 repite cifra/límite sin payoff | Copia bloqueada; sin producción verificada |

Para los siete proyectos con sidecars de plataforma, los campos mp4 apuntan a rutas /workspace/... fuera del árbol GitHub. Se marca MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO; no se afirma que esos medios existan en GitHub. El storyboard de árboles tiene una salida distinta en main, pero su capsula.mp4 tampoco aparece en el árbol. El storyboard de hielo tiene una salida de producción, pero su MP4 no aparece en el árbol. No se usa qa.json audiovisual como narrative_qa.

data/horario_semana_2026-11-01_07.json conserva estado pedir_chatgpt en los 12 slots, aunque siete tienen sidecars de publicación/programación y algunos tienen QA FAIL. Ese estado de parrilla está desactualizado frente a la evidencia de plataforma. No se modifica data. Los estilos del lote son distintos por día; la discrepancia temática real está en el pulpo, no en árboles.

## 5. Inventario histórico sin QA narrativo

La rama contiene 79 storyboard.json bajo proyectos/. Además de los proyectos auditados arriba, 41 borradores fechados del 24-oct al 2-nov carecen de narrative_qa. Treinta y dos tienen salidas/ en la rama; catorce de esos también conservan copias en cola/bloqueados. No se redispatchan. Los nueve que no tienen salidas ni cola son:
- 2026-10-24_osedax-comehuesos
- 2026-10-24_serpientes-que-ruedan
- 2026-10-25_ave-jurasica-sin-vuelo
- 2026-10-25_reina-olor
- 2026-10-25_sueno-electricidad-qom
- 2026-10-26_hongo-gente-diminuta
- 2026-10-26_pimiento-verde-rojo
- 2026-11-01_dato-cambio-horario-corazon
- 2026-11-01_red-electrica-pulso-minuto

La lista completa de los 41 sin narrative_qa es:
- 24-oct: 2026-10-24_abejas-bullying; 2026-10-24_ideonella-pet; 2026-10-24_osedax-comehuesos; 2026-10-24_serpientes-que-ruedan.
- 25-oct: 2026-10-25_ave-jurasica-sin-vuelo; 2026-10-25_corales-contacto; 2026-10-25_reina-olor; 2026-10-25_sueno-electricidad-qom.
- 26-oct: 2026-10-26_baffin-bay-ice-shelf; 2026-10-26_catrina-posada-monerismo; 2026-10-26_hongo-gente-diminuta; 2026-10-26_papel-picado-dia-muertos; 2026-10-26_papel-picado-dia-muertos_parte2; 2026-10-26_pimiento-verde-rojo.
- 27-oct: 2026-10-27_cempasuchil-ciencia; 2026-10-27_corneja-decision-rapida; 2026-10-27_ddm-parte3-pomuch; 2026-10-27_familia-ajolote; 2026-10-27_kids-serpiente-voladora; 2026-10-27_noct-anfibio-marino.
- 28-oct: 2026-10-28_ddm-parte4-templo-mayor; 2026-10-28_familia-voyager-disco-oro; 2026-10-28_kids-titanoboa; 2026-10-28_monarca-almas; 2026-10-28_mosquito-fruitless-audicion; 2026-10-28_noct-lince-milanos; 2026-10-28_pan-de-muerto-huesos.
- 29-oct: 2026-10-29_juno-choque-proa; 2026-10-29_muralismo-cu.
- 30-oct: 2026-10-30_arqueas-origen-eucariotas; 2026-10-30_kromdraai-primera-fecha.
- 31-oct: 2026-10-31_murcielagos-viroma-global; 2026-10-31_pardelas-jetlag-solar; 2026-10-31_sequias-energia-renovable; 2026-10-31_smartpe-edicion-plantas.
- 1-nov: 2026-11-01_dato-cambio-horario-corazon; 2026-11-01_llorar-cebolla-quimica; 2026-11-01_pulpo-tres-corazones; 2026-11-01_red-electrica-pulso-minuto.
- 2-nov: 2026-11-02_camaron-mantis; 2026-11-02_comida-pan-duro.

También permanecen ocho artefactos sin fecha/slot operativo y sin narrative_qa: 2026-11-xx_kids-flamencos-rosas_RESPALDO, demo-001, guiones_lote_01 y lote01-01-el-nino, lote01-02-petroleo, lote01-03-balon-curva, lote01-04-tardigrado, lote01-05-chicxulub. El respaldo de flamencos declara REDACTADO_Y_MONTADO_POR_GROK_BOT_3NOV_SLOT_KIDS, pero no tiene estado Grok; no se toma esa etiqueta como recepción ni QA. demo-001 tiene 11 escenas y 154 palabras; los cinco lote01 tienen 43–63 palabras; guiones_lote_01 no contiene narración de escenas. No se promueven.

Se respetaron las exclusiones del lote: no se revisaron los slots de dato del día 23:30, kids 3-nov 07:00 ni Machu Picchu 4-nov 19:00.

## 6. Cola, dispatch y recepción

Inventario en la rama de trabajo:
- No hay archivos JSON directamente en cola/entrada/*.json.
- Hay dos entradas en forma de carpeta: cola/entrada/2026-11-07_dato-clavo-te-cocina/storyboard.json y cola/entrada/2026-11-09_dato-robot-ensambla-orbita/storyboard.json.
- Ambas son NOT_DISPATCHABLE. capcot-grok-dispatch.yml escucha cola/entrada/*.json y su selector manual busca archivos JSON a profundidad 1; no encuentra storyboard.json dentro de subcarpetas.
- No hay archivos cola/estado/*.json en la rama. Para todos los proyectos actuales: RECEPCION_GROK_NO_CONFIRMADA.
- El marker handoffs/grok_inbox del robot tiene status=pending; no hay entrada correspondiente en grok_done. Un marker de inbox pendiente no es acuse de recepción.

La entrada de clavo fue creada el 7-nov 18:00 CDMX; el storyboard declara objetivo 7-nov 23:30, pero data/horario_2026-11-08 registra su programación para 8-nov 23:30 con YouTube EwZ3dHalUn0 y TikTok/Facebook programados. La fecha del ID/storyboard y la fecha efectiva del registro de programación discrepan. No se evalúa narrativamente por la exclusión 23:30; solo se constata que la ruta en carpeta no dispara el workflow.

La entrada del robot se creó el 9-nov 18:40 CDMX para el slot original 23:30. En main hay un paquete completo de producción, con capsula.mp4 real en el árbol, y programación nueva para 21-nov 19:00. Se clasifica PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR. No existe archivo historial_youtube en el árbol; por ello no se puede certificar un inventario histórico completo de IDs. El segundo ID ztIkYcXB91U de Arena cantante, aún descrito como programado y sin privacidad, permanece como riesgo de duplicado.

Última ejecución observada de capcot-grok-dispatch: 1-nov-2026, run 41306776689, failure. Error literal: “Falta configurar GROK_WEBHOOK_URL.” No hay ejecuciones de dispatch posteriores en la rama. El run antiguo no permite confirmar el estado actual de GROK_WEBHOOK_TOKEN; no se exponen valores de secretos.

El procesador procesar_cola.py usa fecha_actual_cdmx() por defecto, pero admite --fecha con cualquier fecha. La selección compara el prefijo de fecha del nombre/ruta, no fecha_objetivo dentro del JSON. Por tanto, el comportamiento por defecto apunta al día actual, pero el código no impide procesar históricos si se pasa --fecha; tampoco detecta por sí mismo un desajuste entre prefijo y fecha_objetivo. No se modifica el procesador.

registro_editorial.py combina proyectos, cola de entrada, salidas y data seleccionada, pero no cubre por sí solo cola/bloqueados, handoffs ni cola/estado. El inventario manual de este control añade esas rutas.

## 7. Contradicciones documentales y rotación

- FLUJO_DE_PRODUCCION.md todavía indica 60–180 s y generación manual de medios; templates/storyboard.template.json usa 120 s y asset_filename/voice_asset. Ambos contradicen el contrato vigente. El Contrato Operativo los deja como legado; rigen Receta + plantilla vertical de 84 s, 6 s de cortinilla y storyboard textual sin assets.
- VOCES_POR_TEMA.md asigna narradora_es a biología y cocina, mientras Plan Maestro, Receta, plantilla vertical y validador fijan es-MX-JorgeNeural. No se cambia voz ni plantilla; queda registrada la contradicción.
- La rotación de main registra art_deco_poster para Juno el 19-nov 13:30; el borrador de estrella usa el mismo estilo a las 17:00. También main registra papel_rasgado_capas para sinergia-algas el 18-nov 19:00; catorce campos usa el mismo estilo a las 23:30. No se modifican decisiones ni data.
- data/estilos_usados.json, temas_del_dia.json, rotacion.json y publicaciones.json de la rama de trabajo están atrasados respecto de proyectos/ y salidas/; main contiene registros más recientes. No se editan data ni main.
- data/horario_semana_2026-11-01_07.json mantiene pedir_chatgpt en los 12 slots, pese a las salidas y sidecars señalados. No se altera la parrilla.
- No se encontró en los documentos ni briefs del repositorio un aviso oficial nuevo que justificara revisar APIs. No se hizo una búsqueda externa de cambios de proveedor.

## 8. Cambios realizados y límites

Cambios realizados exclusivamente en la rama de trabajo:
1. Se añadió narrative_qa independiente a los dos storyboards del 19-nov: estrella PASS 90 y oro PASS 91.
2. Se añadió narrative_qa a catorce campos: FAIL 68, siete checks y cuatro critical_flags.
3. Se corrigió el estado documental de catorce campos a BORRADOR_EN_PROYECTOS_NO_APTO_PARA_PROMOCION.
4. Se actualizó ESTADO_EJECUCION de Kuroshio: CI estructural exitoso, DOI resolver/Crossref pendiente y recepción Grok no confirmada.
5. Se prepara este CONTROL_COLA.

No se cambió narración, claims, fuentes, data/*.json, main, workflows, secretos, permisos, salidas ni estados Grok. No se creó ninguna entrada de cola, no se movió ningún archivo bloqueado, no se envió payload y no se generó medio.

Incidencia de ejecución: las dos escrituras consecutivas de ESTADO_EJECUCION de Kuroshio coincidieron con el path filter de validar-kuroshio.yml y dispararon dos workflows de validación: run 44617395667, commit 369d0da1007f6b2eafd3502bd369c4284d3acee1, 19-nov 15:18:16–15:18:35 CDMX; y run 44617431497, commit b399dda95661b2e134a24c99d9ede803f597f1bb, 19-nov 15:18:28–15:18:44 CDMX. Ambos ejecutaron exactamente python scripts/validar_storyboard.py proyectos/2026-11-18_dato-kuroshio-puente-atmosferico/storyboard.json y ambos devolvieron OK, salida 0; ninguno incluyó --check-doi. No fueron dispatch a Grok ni generaron medios. Esto no debió activarse bajo la instrucción de no disparar workflows y queda registrado. No se activaron más workflows.

## 9. Decisión de handoff

No se promueve ningún paquete en este run.

- Oro: QA PASS y estructura estática correcta, pero DOI resolver/Crossref pendiente.
- Estrella: QA PASS, pero mapa celeste no compatible con el validador geográfico y estilo repetido el mismo día.
- Kuroshio: QA PASS y CI estructural OK, pero DOI resolver/Crossref pendiente.
- Catorce campos: QA FAIL y conflicto exacto de slot en main.
- Lote 5–7: los dos QA PASS fallan estructura; los otros diez fallan narrativa; siete proyectos ya tienen producción/publicación/scheduling y no se redispatchan.
- Microplásticos (14-nov), diapausa (15-nov) y suelo (17-nov): QA PASS, revisión estática sin errores y DOI verificado, pero no se creó handoff porque no se ejecutó el validador oficial y está prohibido disparar workflows en esta auditoría.

La ausencia de cola/estado sigue significando RECEPCION_GROK_NO_CONFIRMADA. No se afirma selección, producción, QA oficial ni publicación de Grok sin el estado y evidencia correspondientes.
