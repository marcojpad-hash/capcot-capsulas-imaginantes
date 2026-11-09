# CAPCOT — control de cola, rotación y dispatchabilidad

**Corte de auditoría:** 2026-11-09 15:53:26 America/Mexico_City  
**Repositorio y rama auditados:** marcojpad-hash/capcot-capsulas-imaginantes / feature/capcot-video-discovery-continuity  
**HEAD al cerrar QA narrativo:** 934f7f7d4623c986b7f787c5dd20f2fa497b2796  
**PR #3:** abierto, Draft, no merged, mergeable=false; 592 archivos, 58,061 adiciones, 1,694 eliminaciones. Comparación GitHub: 672 commits ahead y 125 behind de main.

## 1. Dictamen

**NO LISTO PARA HANDOFF NI PRODUCCIÓN.** La lectura narrativa independiente quedó registrada para los doce proyectos del lote 5–7 nov. Dos pasan narrativa, pero ninguno pasa estructura; diez fallan narrativa. No se promovió ningún proyecto a cola.

En la rama auditada no hay proyecto ni entrada de cola del 9-nov. Sí existe un paquete distinto del 9-nov en main, fuera de esta rama, con una copia anidada en cola y sin QA narrativo, contrato ni medios verificables. Esa divergencia entre ramas se registra abajo; no se modificó main.

## 2. Briefs y día actual

En la rama feature existen:
- docs/briefs/2026-11-09_RADAR_CAPCOT.md
- docs/briefs/2026-11-09_CONTROL_COLA.md

El RADAR del 9-nov indica que no hay proyecto nuevo autorizado para esa fecha. La lectura del horario diario de la rama confirma que el slot de 07:00 corresponde a la publicación del proyecto de ranas del 6-nov. El slot 23:30 de dato del día queda excluido de esta auditoría de contenido, conforme a la instrucción; no se hizo QA ni copia de ese paquete.

**Inventario de la rama feature para 2026-11-09:** 0 borradores en proyectos y 0 entradas de cola del día. No se encontró un paquete plano ni una carpeta de cola del 9-nov en esta rama.

**Discrepancia de main:** main contiene proyectos/2026-11-09_andes-virus-aminoacido/storyboard.json y cola/entrada/2026-11-09_andes-virus-aminoacido/storyboard.json. No están en feature. El storyboard de main tiene 7 escenas, 130 palabras, objetivo 82 s, carece de narrative_contract y narrative_qa y referencia siete frames que no existen en el árbol. Su programacion.json propone YT privado a las 14:15 CDMX (publish_at 20:15Z), pero no aporta ID/URL de plataforma; la rama feature no tiene slot de 14:15 en el horario del 9-nov. No existe cola/estado ni marcador inbox para ese ID. Clasificación: NOT_DISPATCHABLE, RECEPCION_GROK_NO_CONFIRMADA, MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO y no redispatchar hasta reconciliar la divergencia. No se escribió en main.

## 3. Lote obligatorio 5–7 nov: identidad y slots

Los doce storyboard canónicos existen en proyectos/. Para los doce, project_id, fecha_objetivo, slot_local y slot_cesta coinciden con data/horario_semana_2026-11-01_07.json. No se encontró campo fecha_creacion en los storyboards; el prefijo del ID no demuestra la fecha de creación. narrative_qa.reviewed_at es fecha de revisión, no fecha de creación.

| Proyecto | Slot CDMX / cesta | Palabras | QA frío |
|---|---|---:|---:|
| 2026-11-05_kids-dia-en-venus | 05-nov 07:00 / kids | 170 | PASS 88 |
| 2026-11-05_comida-palomitas | 05-nov 13:30 / comida_familia | 173 | FAIL 82 |
| 2026-11-05_inter-arboles-se-comunican | 05-nov 17:00 / intermedio_1 | 169 | FAIL 78 |
| 2026-11-05_inter-rayo-globular | 05-nov 17:45 / intermedio_2 | 197 | FAIL 81 |
| 2026-11-06_kids-ballena-azul-corazon | 06-nov 07:00 / kids | 174 | FAIL 80 |
| 2026-11-06_comida-aguacate-negro | 06-nov 13:30 / comida_familia | 170 | FAIL 79 |
| 2026-11-06_inter-ranas-congeladas | 06-nov 17:00 / intermedio_1 | 177 | FAIL 83 |
| 2026-11-06_inter-arena-cantante | 06-nov 17:45 / intermedio_2 | 206 | PASS 94 |
| 2026-11-07_kids-huesos-bebe | 07-nov 07:00 / kids | 172 | FAIL 82 |
| 2026-11-07_comida-hielo-caliente | 07-nov 13:30 / comida_familia | 172 | FAIL 81 |
| 2026-11-07_inter-pulpo-suenos | 07-nov 17:00 / intermedio_1 | 170 | FAIL 80 |
| 2026-11-07_inter-nubes-pesan | 07-nov 17:45 / intermedio_2 | 221 | FAIL 78 |

Todos los registros narrative_qa fueron releídos desde GitHub y su reviewed_at se actualizó a 2026-11-09T15:53:26-06:00. Se conservaron scores, checks y flags existentes porque coinciden con la nueva lectura en frío. review_basis permanece lectura_en_frio_solo_narracion y reviewer_role auditor_capcot_independiente. No se cambió ninguna narración, claim, título, fuente ni decisión editorial.

Bloqueos narrativos registrados:
- Palomitas: apertura definicional y escena 6 repite causas sin información nueva.
- Árboles: apertura genérica, no in medias res.
- Rayo globular: apertura histórica descriptiva.
- Ballena: payoff sobreafirma que el corazón casi se detiene.
- Aguacate: escenas 5–6 repiten sin avance causal.
- Ranas: escenas 5–6 repiten límites de especie y condiciones.
- Huesos: escena 6 repite variación del conteo y fusión.
- Hielo caliente/Mpemba: apertura de creencias, no in medias res.
- Pulpo: repetición en escenas 5–6 y payoff vago.
- Nubes: escena 7 repite cifra y límite sin pagar la pregunta de la suspensión.
- Venus y arena cantante: los siete checks narrativos permanecen true y critical_flags=[].

## 4. Validación estructural estática

No se ejecutó scripts/validar_storyboard.py ni la suite Python: no hay checkout local/runtime del repositorio conectado. Se hizo revisión estática de los doce JSON y del código del validador.

Hallazgos:
- 12/12 tienen 7–8 escenas; cortinilla de 6 s; 78 s de escenas + 6 s = 84 s; target_duration_seconds=84.
- 11/12 cumplen 170–235 palabras. Árboles tiene 169.
- 12/12 cumplen gancho de máximo seis palabras, arco/cierre hablado, voz es-MX-JorgeNeural (+7%, -2Hz), source_ids conocidos y prompt_base literal del catálogo.
- 12/12 tienen narrative_contract con los seis campos no vacíos.
- 12/12 tienen approved_assets=[] y export.render_status=NOT_GENERATED; no declaran asset_filename, asset_type ni rutas de medios.
- 11/12 tienen capa mapa y dato/gráfico con fuente. Árboles carece de ambas.
- Las 85 escenas tienen ambiente no vacío. En 75/85, sfx es una lista vacía; solo diez escenas declaran efectos. La Receta pide que el silencio se exprese explícitamente, pero la plantilla inicia sfx como [] y el validador solo comprueba presencia del campo, no contenido.
- Faltan en las 85 escenas los seis campos exigidos por el validador: dramatic_beat, scene_function, causal_bridge_from_previous, question_state, reason_to_continue y new_information. Total: 510 campos ausentes.

Resultado: 0/12 pasan el validador estructural. Venus y arena cantante pasan narrativa, pero no pueden promoverse. Los otros diez tampoco pueden promoverse por QA narrativo. No se creó ninguna entrada de cola.

## 5. Fuentes y claims que requieren corrección del investigador

Los nueve DOI distintos presentes en el lote se localizaron en registros de editoriales/PubMed; no se ejecutó Crossref ni el parámetro --check-doi. Las fuentes URL sin DOI siguen identificadas por URL.

- Ranas: la fuente SRC-001 es Costanzo, Lee & Lortz 1993, DOI 10.1242/jeb.181.1.245, sobre glucosa y tolerancia al congelamiento en la población de Ohio. La capa mapa/gráfico cita PubMed 23966588, DOI 10.1242/jeb.089342, estudio 2013 de Interior Alaska que respalda el valor de −16 °C. Ese segundo trabajo no está en sources y la capa lo atribuye al mismo SRC-001. Es una discrepancia de fuente y source_ids; no se corrigió.
  Referencias: https://pubmed.ncbi.nlm.nih.gov/8409827/ y https://pubmed.ncbi.nlm.nih.gov/23966588/
- Pulpo: el DOI 10.1038/s41586-023-06203-4 estudia Octopus laqueus; la narración menciona Octopus insularis. El artículo describe dos estados de sueño, pero no respalda esa identificación de especie. No se cambió el claim.
  Referencia: https://www.nature.com/articles/s41586-023-06203-4
- Ballena: PNAS 10.1073/pnas.1914273116 respalda 4–8 latidos/min durante inmersiones y un mínimo de 2; el cierre “casi se detiene” sigue siendo una sobreafirmación narrativa.
- Huesos: OpenStax 6.2 sí indica 270–300 huesos al nacer y fusión hacia 206. La nota PENDING_SOURCE del horario semanal quedó desactualizada; el storyboard cita la página. Es fuente educativa secundaria, no estudio primario.
  Referencia: https://openstax.org/books/anatomy-and-physiology-2e/pages/6-2-bone-classification
- Árboles: el storyboard canónico trata redes micorrícicas y Karst et al. 2023; el tema coincide con el slot. No marcar desajuste temático. El artefacto bloqueado arboles-mito-respiran es otra propuesta y no debe confundirse con este ID.

## 6. Producción preexistente, publicaciones y medios

En feature, para los doce IDs no existen programacion.json ni ESTADO_EJECUCION.md en proyectos; tampoco se encontraron los cinco archivos esperados de salidas (storyboard.json, qa.json, publicacion.json, metadata.json, licencias.json). No hay evidencia de salidas audiovisuales versionadas para esos doce.

Dos proyectos sí tienen evidencia de publicación posterior a su fecha objetivo:
- Palomitas: data/horario_2026-11-08 registra YouTube ID zTP5akrGA9M, TikTok ID 7705593452003691794 y Facebook post 1167496802382795. Clasificación: PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR.
- Ranas: data/horario_2026-11-09 registra YouTube ID UBFuKBU3cx0 y TikTok ID 7705596671807245586; Facebook aparece como programado_lote_7nov, sin URL/ID de publicación en ese registro. Clasificación: PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR.

El horario semanal conserva pedir_chatgpt para los doce, por lo que está desactualizado respecto de palomitas y ranas. Los archivos diarios 8 y 9 nov son la evidencia más reciente para esos dos estados.

En main hay además una copia de cola de 2026-11-07_comida-hielo-caliente, ausente de feature. Esa copia tiene seis escenas, 176 palabras y objetivo 80 s, sin narrative_contract ni narrative_qa. Su ESTADO_EJECUCION dice 6 escenas, 60 s y ~115 palabras, discrepante con el storyboard; reporta clips de prueba y QA local con Kokoro, pero declara QA oficial pendiente. Los seis frames y capsula.mp4 no existen en GitHub. Clasificación: PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR, NOT_DISPATCHABLE y MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO. No se movió ni editó porque está en main, fuera de la rama solicitada.

## 7. Cola, bloqueados y Grok

- Los doce proyectos canónicos no tienen copia en cola/entrada, ni como JSON plano ni como carpeta anidada.
- No existe cola/estado/<project_id>.json para ninguno de los doce: RECEPCION_GROK_NO_CONFIRMADA en los doce casos.
- En feature, handoffs/grok_inbox solo tiene README y handoffs/grok_done solo .gitkeep; no hay marcadores ni confirmaciones.
- La única carpeta conocida en cola/entrada de feature es 2026-11-07_dato-clavo-te-cocina, anidada. Corresponde al slot 23:30 excluido; solo se inventarió la ruta, no se hizo QA de contenido ni se creó copia.
- Hay copias bloqueadas exactas para rayo, aguacate, ranas, arena, huesos y nubes. Aguacate, ranas y huesos tienen además duplicado entre archivo plano y carpeta. Existen variantes con IDs distintos: palomitas-explotan, arboles-mito-respiran, venus-dia-largo, corazon-ballena-azul y suenos-pulpo. extra-nubes-pesan comparte el project_id canónico de nubes y es material de origen, no segundo proyecto. No se borró ni movió nada.
- Ninguna copia de los doce está en cola, por lo que no hubo movimiento a bloqueados en esta pasada.

**Dispatchabilidad:** el workflow .github/workflows/capcot-grok-dispatch.yml escucha solo cola/entrada/*.json; el modo all busca con maxdepth 1 y el selector individual construye cola/entrada/<project_id>.json. Por ruta, todos los storyboards que permanecen en proyectos son NOT_DISPATCHABLE. Los paquetes anidados de main tampoco cumplen esa ruta. main no tiene este workflow. El workflow solo valida sintaxis JSON; no ejecuta QA narrativo ni estructural antes de escribir el marcador inbox. El marcador inbox tampoco equivale a recepción Grok: solo cola/estado escrito por Grok confirma recepción.

## 8. Procesador, registro y contradicciones documentales

- scripts/procesar_cola.py usa la fecha CDMX actual por defecto y filtra por fecha; acepta --fecha, por lo que una invocación explícita puede seleccionar histórico. También admite entradas planas y anidadas, mientras el contrato canónico y el workflow autorizan solo JSON plano. No comprueba cola/estado ni salidas/publicaciones antes de procesar; existe riesgo de reprocesar si alguien invoca manualmente una fecha histórica.
- scripts/registro_editorial.py lee rotacion, publicaciones, cola y storyboards de proyectos/entrada/salidas, pero no escanea cola/bloqueados ni los horarios diarios/semanales; deriva fecha del ID y no conserva fecha_objetivo, slot_local ni slot_cesta. No basta para la reconciliación requerida.
- README todavía indica entregar directamente a cola/entrada; contradice Plan Maestro, Guía, QA en frío y Flujo Externo, que requieren staging en proyectos y promoción por auditor independiente.
- La plantilla deja sfx=[] por defecto; la Receta exige declarar el silencio. El validador no detecta listas vacías.
- No se encontró archivo historial_youtube. Ninguno de los doce renglones del horario semanal trae yt_id_historial. No se detectó un ID histórico de esos doce aún descrito como programado.
- data/rotacion.json (27 registros) y data/publicaciones.json (22) llegan a 31-oct; temas_del_dia llega a 28-oct; vistas_historico y balances_6h llegan a 28-oct; data/cola tiene un registro de 31-oct. No sirven para certificar rotación/publicación del lote 5–7.
- data/tendencias_estilos llega a 31-oct. Los doce estilo_id existen en el catálogo y los prompts coinciden con prompt_base; no se repite estilo dentro de cada día, pero no puede verificarse rotación reciente contra el historial posterior al 31-oct. El horario semanal no asigna estilo.
- data/endscreens_rotacion llega al 8-nov y registra end screens, no rotación de estilos.

## 9. Actions y handoff

- No hay ejecución PR-triggered asociada al HEAD actual 934f7f7. El conector consultado solo expone ejecuciones asociadas a PR, por lo que no certifica el inventario total de push/workflow_dispatch.
- El run de dispatch 41306776689 (1-nov) falló con el texto literal: “Falta configurar GROK_WEBHOOK_URL.” En ese job GROK_WEBHOOK_TOKEN también aparecía sin configurar, sin un error separado. No se copian valores de secretos.
- El smoke TTS 42447536352 (8-nov) fue SUCCESS en compilación/interfaz/CLI; no demuestra generación real de voz ni audio final.
- La versión actual del workflow deja el marcador inbox antes del webhook opcional, pero no hay run posterior que pruebe ese camino. No se envió payload ni se disparó workflow.

## 10. Cambios efectuados y límites

Cambios realizados:
1. Se actualizó únicamente narrative_qa.reviewed_at en los doce storyboard canónicos a 2026-11-09T15:53:26-06:00. Se conservaron exactamente status, score, checks, flags, narrativa y claims.
2. Se reemplazó este control con el corte actual y se verificará su lectura de vuelta.

No se modificaron data/*.json, main, workflows, secretos, permisos, cola/estado, handoffs, salidas, decisiones editoriales ni publicaciones. No se promovió ningún storyboard, no se movió ninguna copia y no se corrigieron claims.

No se generaron cápsulas, frames, imágenes, voz, audio, video ni renders. No se publicó, programó, envió payload externo ni consumió créditos. No se revisaron APIs comerciales porque no se identificó un cambio oficial nuevo que justificara esa comprobación.

**Conclusión:** 0/12 aptos para promoción; 2/12 PASS narrativo pero FAIL estructural; 10/12 FAIL narrativo y estructural. No hay handoff Grok confirmado. PR #3 permanece Draft y no integrable.
