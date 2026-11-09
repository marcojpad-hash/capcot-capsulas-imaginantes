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


## 11. Reauditoría complementaria — 2026-11-09 16:20 CDMX

**Snapshot de entrada:** rama `feature/capcot-video-discovery-continuity`, HEAD `39023fa794bbe29f2e6217dac4d27464f0189518`; `main` observado solo en lectura, HEAD `dddb49a46e00fa8091fb753d42e0c905026ca9d5`. PR #3 sigue abierto, Draft, no merged, `mergeable=false`; 592 archivos, 58,083 adiciones y 1,694 eliminaciones. No se modificó `main` ni el PR.

### 11.1 Inventario actual y fechas

- En `feature`, el árbol contiene 57 `proyectos/*/storyboard.json`; ninguno tiene prefijo `2026-11-09_`. Hay 0 borradores y 0 entradas de cola del 9-nov en esta rama. El radar del día no autoriza un proyecto nuevo; el horario diario registra el slot 07:00 como publicación atrasada de ranas y el slot fijo 23:30 queda excluido por instrucción.
- El único path visible en `cola/entrada/` de `feature` es la carpeta histórica `2026-11-07_dato-clavo-te-cocina/`; corresponde a un slot 23:30 excluido. No se le hizo QA ni se creó una copia bajo esta reauditoría.
- Los doce storyboards obligatorios del lote 5–7 nov están en `proyectos/<project_id>/storyboard.json`, no en cola. Sus doce primeros commits de archivo apuntan al commit `7a4154...`, 2026-11-02 16:11:24 CDMX; los registros de QA fueron actualizados por el commit `934f7f7...`, 2026-11-09 15:53:26 CDMX. GitHub muestra la cuenta `marcojpad-hash` como actor de esos commits; no hay evidencia que permita atribuir la redacción a una automatización o modelo concreto.

| Proyecto | Fecha objetivo / slot / cesta | QA frío releído | Estado estructural | Dispatch | Estado Grok |
|---|---|---:|---|---|---|
| `2026-11-05_kids-dia-en-venus` | 05-nov 07:00 / kids | PASS 88 | FAIL | NOT_DISPATCHABLE | RECEPCION_GROK_NO_CONFIRMADA |
| `2026-11-05_comida-palomitas` | 05-nov 13:30 / comida_familia | FAIL 82 | FAIL | NOT_DISPATCHABLE | RECEPCION_GROK_NO_CONFIRMADA |
| `2026-11-05_inter-arboles-se-comunican` | 05-nov 17:00 / intermedio_1 | FAIL 78 | FAIL | NOT_DISPATCHABLE | RECEPCION_GROK_NO_CONFIRMADA |
| `2026-11-05_inter-rayo-globular` | 05-nov 17:45 / intermedio_2 | FAIL 81 | FAIL | NOT_DISPATCHABLE | RECEPCION_GROK_NO_CONFIRMADA |
| `2026-11-06_kids-ballena-azul-corazon` | 06-nov 07:00 / kids | FAIL 80 | FAIL | NOT_DISPATCHABLE | RECEPCION_GROK_NO_CONFIRMADA |
| `2026-11-06_comida-aguacate-negro` | 06-nov 13:30 / comida_familia | FAIL 79 | FAIL | NOT_DISPATCHABLE | RECEPCION_GROK_NO_CONFIRMADA |
| `2026-11-06_inter-ranas-congeladas` | 06-nov 17:00 / intermedio_1 | FAIL 83 | FAIL | NOT_DISPATCHABLE | RECEPCION_GROK_NO_CONFIRMADA |
| `2026-11-06_inter-arena-cantante` | 06-nov 17:45 / intermedio_2 | PASS 94 | FAIL | NOT_DISPATCHABLE | RECEPCION_GROK_NO_CONFIRMADA |
| `2026-11-07_kids-huesos-bebe` | 07-nov 07:00 / kids | FAIL 82 | FAIL | NOT_DISPATCHABLE | RECEPCION_GROK_NO_CONFIRMADA |
| `2026-11-07_comida-hielo-caliente` | 07-nov 13:30 / comida_familia | FAIL 81 | FAIL | NOT_DISPATCHABLE | RECEPCION_GROK_NO_CONFIRMADA |
| `2026-11-07_inter-pulpo-suenos` | 07-nov 17:00 / intermedio_1 | FAIL 80 | FAIL | NOT_DISPATCHABLE | RECEPCION_GROK_NO_CONFIRMADA |
| `2026-11-07_inter-nubes-pesan` | 07-nov 17:45 / intermedio_2 | FAIL 78 | FAIL | NOT_DISPATCHABLE | RECEPCION_GROK_NO_CONFIRMADA |

Los doce `cola/estado/<project_id>.json` devolvieron 404. Se conserva el literal `RECEPCION_GROK_NO_CONFIRMADA` en los doce casos; no se creó ni modificó estado. Los valores de QA de la tabla coinciden con los JSON releídos. La relectura en frío de esta pasada no justificó cambiar scores/checks ni reescribir narraciones.

### 11.2 Revalidación estructural y rotación

- Los doce `project_id`, `fecha_objetivo`, `slot_local` y `slot_cesta` coinciden con `data/horario_semana_2026-11-01_07.json`. El horario actualizado ubica los slots intermedios 5, 6 y 7 nov en 17:45; el brief semanal antiguo conserva referencias a 19:00 y está desactualizado.
- 12/12: 7–8 escenas; cortinilla de 6 s; escenas + cortinilla = 84 s; `target_duration_seconds=84`; gancho de hasta seis palabras; arco y cierre hablado presentes; voz `es-MX-JorgeNeural`, +7%, -2Hz; contrato narrativo con seis campos no vacíos; `source_ids` apuntan a IDs existentes; prompts comienzan con el `prompt_base` literal del catálogo; `ambiente` y `sfx` están presentes.
- 11/12 cumplen 170–235 palabras. Árboles tiene 169, carece de capa mapa y de capa dato/gráfico. Las otras once tienen mapa y dato/gráfico con fuente.
- Las 85 escenas carecen de los seis campos estructurales exigidos por `validar_storyboard.py`: `dramatic_beat`, `scene_function`, `causal_bridge_from_previous`, `question_state`, `reason_to_continue` y `new_information`. Total: 510 campos ausentes. Por eso 0/12 pasan estructura, incluidos Venus y arena aunque su QA narrativo sea PASS.
- 12/12 mantienen `approved_assets=[]`, `export.render_status=NOT_GENERATED`, sin `asset_filename`, `asset_type` ni rutas de medios. No se contaron placeholders como medios. En las 12 biblias visuales `seed=null` y `reference_assets=[]`; no bloquea el contrato textual, pero la continuidad visual futura necesitará resolver semilla/referencias antes de producción.
- 85/85 escenas declaran ambiente; 75 tienen `sfx=[]` y diez contienen efectos. La plantilla permite lista vacía y el validador comprueba presencia, no si el silencio está descrito de forma editorial.
- Las doce declaran `estructura="pregunta"`: cuatro repeticiones el 5-nov, cuatro el 6-nov y cuatro el 7-nov. Esto incumple la rotación de estructura dentro del día. El estilo `papel_rasgado_capas` aparece en árboles (5-nov) y ranas (6-nov), posible repetición entre días. Los temas del lote son distintos. El storyboard canónico de árboles sigue siendo el de redes micorrícicas y Karst et al. 2023; no es un desajuste temático. `extra-nubes-pesan` conserva el mismo `project_id` canónico y es material de origen, no un segundo proyecto.

### 11.3 Claims y trazabilidad de fuentes

- Pulpo: la narración identifica `Octopus insularis`, pero el artículo de Nature DOI `10.1038/s41586-023-06203-4` estudia `Octopus laqueus`. No es una variante de nombre: es una discrepancia de especie. Fuente primaria: https://www.nature.com/articles/s41586-023-06203-4.
- Ranas: la capa que muestra `Hasta −16 °C` cita PubMed 23966588 / DOI `10.1242/jeb.089342` (estudio de Interior Alaska, 2013), pero `sources[]` solo contiene el trabajo de 1993 DOI `10.1242/jeb.181.1.245`; el `source_ids` de la capa sigue siendo `SRC-001`. El dato tiene fuente externa identificable, pero no está registrado como segundo source_id. Referencia: https://pubmed.ncbi.nlm.nih.gov/23966588/.
- Arena: `scene_002` coloca Agadir con una fuente que cita Douady et al. 2006 / DOI `10.1103/PhysRevLett.97.018002`, y `scene_004` narra sincronización de granos; ambas escenas solo declaran `source_ids=["SRC-001"]`, que corresponde a Andreotti 2004. La fuente `SRC-002` sí existe en `sources[]`, pero no está vinculada a esas escenas.
- Aguacate: `sources[0].doi` está vacío, aunque el artículo de Heliyon 2025 enlazado por PMC tiene DOI `10.1016/j.heliyon.2025.e42588` (PMID 40034293). Además, el mapa pincha el Western Regional Research Center de Albany, pero las afiliaciones del artículo corresponden a instituciones colombianas; el pin no queda sustentado por esa fuente. Referencia: https://pubmed.ncbi.nlm.nih.gov/40034293/.
- Ballena: se mantiene la sobreafirmación del cierre “casi se detiene”; el estudio registra un mínimo de 2 latidos/min en un ejemplar, no detención.
- Los nueve DOI distintos declarados en `sources[]` siguen marcados como verificados por resolver en los JSON. Hay dos DOI adicionales relevantes que no están bien registrados: el de la capa de ranas y el omitido en la fuente de aguacate. No se ejecutó Crossref ni `--check-doi`.

### 11.4 Producción preexistente: cuatro proyectos, no redispatch

La lectura conjunta de JSON por plataforma, horarios diarios y `endscreens_rotacion.json` amplía la detección previa: son cuatro proyectos con evidencia de publicación/programación. Esta sección prevalece sobre cualquier resumen anterior que solo contara palomitas y ranas. Los cuatro se clasifican `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`, aunque sus `publicacion.status` en storyboard sigan como pendientes y no haya `salidas/<id>/` ni estado Grok.

| Proyecto | Evidencia de plataforma en repo | Fecha/privacidad registrada |
|---|---|---|
| Venus | YouTube ID de referencia `phVfyHp3CnY` (54 vistas en end screens); TikTok `7705488176793652481`; Facebook `2544385142727016` | TikTok `Everyone`, 07-nov 17:00 CDMX; Facebook `Public`, 07-nov 17:58 CDMX. Privacidad YouTube no consta. TikTok `etiqueta_ia=true`/`aigcLabelType=1`, Facebook `ai_label=false`: divulgación no uniforme. |
| Palomitas | YouTube `zTP5akrGA9M`; TikTok `7705593452003691794`; Facebook `1167496802382795` | Horario diario 08-nov: `publicado_yt_tt_fb`; TikTok `Everyone` y Facebook `Público`, ambos 08-nov 07:00 CDMX. Privacidad YouTube no consta; `etiqueta_ia` y `ai_label` están sin valor. |
| Arena cantante | YouTube `m4RqQRaz55k` (33 vistas en end screens); TikTok `7705502155427368212`; Facebook `2224920108452190`; el registro de TikTok aún menciona otro YouTube ID `ztIkYcXB91U` como programado a las 19:00 | TikTok `Everyone`, 07-nov 13:30 CDMX; Facebook `Public`, 07-nov 17:58 CDMX. Privacidad YouTube no consta. TikTok `etiqueta_ia=true`/`aigcLabelType=1`, Facebook `ai_label=false`. Riesgo de duplicado entre ID con vistas y el ID que sigue descrito como programado. |
| Ranas | YouTube `UBFuKBU3cx0`; TikTok `7705596671807245586`; Facebook programado sin URL/ID | Horario diario 09-nov: YouTube/TikTok `publicado` a las 07:00 CDMX; TikTok `Everyone`; Facebook `Público`, `programado_lote_7nov` a las 07:00 CDMX, sin post ID/URL. Privacidad YouTube no consta; `etiqueta_ia` y `ai_label` sin valor. |

En los cuatro casos, los JSON de plataforma apuntan a MP4/captions bajo `/workspace/...`, pero el árbol GitHub no contiene esos medios: `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`. No se afirma que el MP4 exista. Los horarios semanales todavía dicen `pedir_chatgpt` para esos slots; hay contradicción entre parrilla y registros posteriores. No se canceló ni borró nada.

Las otras ocho propuestas no tienen `salidas/<id>/` ni JSON de publicación por plataforma en el árbol auditado. Para los doce no hay `cola/estado/<id>.json`; la evidencia de publicación externa no se atribuye a Grok sin ese estado.

### 11.5 Divergencia adicional en `main`: Andes del 9-nov

Se detectó en `main` un proyecto del día que no existe en `feature`: `proyectos/2026-11-09_andes-virus-aminoacido/` y una copia anidada `cola/entrada/2026-11-09_andes-virus-aminoacido/storyboard.json`. El commit de creación observado es `4b0ac906...`, 2026-11-09 10:36:22 CDMX, actor GitHub `marcojpad-hash`; no hay evidencia para atribuirlo a un modelo/automatización concreta.

- El storyboard de `proyectos/` tiene 7 escenas, 130 palabras, 68 s de escenas + 6 s de cortinilla = 74 s, aunque declara objetivo 82 s. No contiene `narrative_contract` ni `narrative_qa`; declara `export.filename=capsula.mp4` y siete rutas `frames/scene_00x.jpg`.
- La copia de cola no coincide: tiene una sola escena, 16 palabras y 8 s + 6 s = 14 s; conserva objetivo 82 s y una ruta `frames/scene_001.jpg`. No contiene QA narrativo ni contrato.
- `programacion.json` declara `programado_paquete`, YouTube privado hasta 14:15 CDMX y subida TikTok desde teléfono, pero no aporta ID/URL de plataforma. El horario operativo actualizado del 9-nov solo mantiene 06:30–07:30, 16:30–18:00 y el slot fijo 23:30; 14:15 no pertenece a la política vigente. La hora declarada ya pasó y no hay confirmación de publicación.
- `cola/estado/2026-11-09_andes-virus-aminoacido.json` devuelve 404: `RECEPCION_GROK_NO_CONFIRMADA`. No hay `salidas/` ni frames/MP4 en el árbol: `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`.

Clasificación conservadora: `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR` hasta reconciliar la programación declarada; `NOT_DISPATCHABLE` desde el workflow de `feature`, por estar en `main` y usar carpeta anidada, no JSON plano. No se modificó `main`.

### 11.6 Workflow, Actions y helpers

- `.github/workflows/capcot-grok-dispatch.yml` está limitado a la rama `feature/capcot-video-discovery-continuity`; `push.paths` escucha solo `cola/entrada/*.json`; `workflow_dispatch=all` usa `find cola/entrada -maxdepth 1 -type f -name '*.json'`; el selector individual construye `cola/entrada/<project_id>.json`. Ninguno de los doce borradores en `proyectos/` es dispatchable. Las carpetas anidadas de main tampoco lo son. El workflow crea un marcador `status=pending` en `handoffs/grok_inbox`; eso no equivale a recepción de Grok.
- La consulta completa de Actions muestra el último run de dispatch como `41306776689`, 2026-11-01 12:29:58Z, FAIL. Error literal: `Falta configurar GROK_WEBHOOK_URL.` El paso termina antes de comprobar `GROK_WEBHOOK_TOKEN`; no se expone ningún valor. La versión actual del workflow hace el webhook opcional y permite buzón gratuito, pero no existe run posterior que pruebe esa versión. No hay dispatch desde 1-nov.
- TTS smoke `42447536352`, 2026-11-08 04:37Z, SUCCESS: instalación, `py_compile`, `--help` y comprobación de manifiesto. No generó voz/audio. Los dos runs TTS fallidos anteriores no exponen jobs/logs (`total_count=0`).
- `procesar_cola.py` por defecto toma la fecha CDMX actual y filtra por el prefijo de fecha del path; admite archivo plano y carpeta anidada. `--fecha` permite elegir otra fecha explícitamente y no compara `fecha_objetivo` dentro del JSON. El procesador no llama a `rotacion.diferencias_con_hoy`; no aplica la regla de estructura/estilo repetidos. `registro_editorial.py` no incorpora `cola/bloqueados`, JSON sociales ni `data/horario_*.json`; deriva fecha del ID, no fecha real de publicación. Esto explica por qué puede perder los cuatro procesamientos preexistentes.
- Los registros canónicos siguen desfasados: `temas_del_dia` y `estilos_usados` llegan a 28-oct; `rotacion` y `publicaciones` a 31-oct; `cola` a 31-oct; `tendencias_estilos` a 31-oct; `endscreens_rotacion` a 08-nov; `horarios` y `horario_2026-11-09` a 09-nov. No se modificó ningún `data/*.json`.
- Se intentó obtener checkout local para ejecutar Python, pero `git clone` falló con `Could not resolve host: github.com`. Por tanto no se ejecutaron `validar_storyboard.py`, `procesar_cola.py`, `registro_editorial.py` ni la suite. Los resultados de estructura son revisión estática de los JSON/código, no ejecución del validador.
- No se revisaron APIs comerciales: no apareció en el repositorio un cambio oficial nuevo que activara esa revisión.

### 11.7 Acciones de esta reauditoría

- No se modificaron storyboards, `narrative_qa`, claims, fuentes, horarios, `data/*.json`, `cola/estado`, workflows, secretos, permisos, `main` ni decisiones editoriales.
- No se promovió ni movió ningún paquete; no se disparó Actions ni se envió payload externo.
- No se generaron cápsulas, frames, imágenes, voz, audio, video ni renders; no se publicó, programó ni consumieron créditos.
- El estado de cierre sigue siendo 0/12 aptos para promoción: 2/12 PASS narrativo pero FAIL estructural; 10/12 FAIL narrativo y estructural. Cuatro proyectos tienen procesamiento/publicación preexistente y no deben redispatcharse. La divergencia Andes en `main` requiere reconciliación fuera de esta rama.