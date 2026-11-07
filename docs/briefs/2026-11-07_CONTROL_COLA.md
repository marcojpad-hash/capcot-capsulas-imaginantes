# Auditor CAPCOT — control de cola
**Fecha de auditoría:** 2026-11-07, 15:45 CDMX  
**Repositorio:** `marcojpad-hash/capcot-capsulas-imaginantes`  
**Rama:** `feature/capcot-video-discovery-continuity`  
**Alcance:** día actual + lote obligatorio 5–7 nov. Sin producción de medios, publicación, dispatch ni consumo de créditos.

## 1. Resultado ejecutivo

- **12** storyboards canónicos encontrados en `proyectos/<project_id>/storyboard.json`: cuatro por fecha, 5, 6 y 7 de noviembre.
- **4** son los borradores de la fecha actual (7-nov).
- `cola/entrada/` contiene únicamente `.gitkeep`: **0 entradas activas**, tanto JSON de primer nivel como carpetas con `storyboard.json`.
- QA narrativo en frío, releído solo desde las narraciones concatenadas: **2 PASS / 10 FAIL**. Los valores coinciden con los JSON releídos después de esta auditoría.
- **0/12** pasan el validador estructural. Los dos PASS narrativos también quedan bloqueados por estructura.
- **0 promociones** a `cola/entrada/`; no había copias activas que mover a bloqueados.
- **0 recepciones Grok confirmadas**. Los doce archivos `cola/estado/<project_id>.json` devolvieron 404.
- Venus y arena tienen evidencia documental de versiones v1 programadas en YouTube. Se clasifican **PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR**; no se borró ni canceló nada.
- El reporte y las doce marcas de revisión se escribieron en esta rama y se releen/verifican.

## 2. Inventario canónico, fechas y QA

Los doce JSON comparan correctamente `project_id`, `fecha_objetivo`, `slot_local` y `slot_cesta` contra `data/horario_semana_2026-11-01_07.json`. La fecha de creación no es la fecha objetivo: el historial Git muestra que los doce archivos se incorporaron a `proyectos/` en el commit `7a415426f5907c2ab03687a47f3d160a595cb669`, el **2026-11-02 16:11:24 CDMX**. La última edición anterior del contenido fue el 6-nov, entre 15:17:19 y 15:17:52 CDMX. En esta auditoría solo se actualizó `narrative_qa.reviewed_at`; no se cambió narración, claim, fuente, tema ni decisión editorial.

| ID canónico | Fecha objetivo | Slot / cesta | QA releído | Checks falsos / motivo crítico |
|---|---|---|---|---|
| `2026-11-05_kids-dia-en-venus` | 05-nov | 07:00 / kids | **PASS 88** | Los siete checks true; flags vacíos |
| `2026-11-05_comida-palomitas` | 05-nov | 13:30 / comida_familia | **FAIL 82** | apertura_in_medias_res, progresion_por_escena; apertura definicional y escena 6 reitera causas |
| `2026-11-05_inter-arboles-se-comunican` | 05-nov | 17:00 / intermedio_1 | **FAIL 78** | apertura_in_medias_res; apertura genérica |
| `2026-11-05_inter-rayo-globular` | 05-nov | 17:45 / intermedio_2 | **FAIL 81** | apertura_in_medias_res; apertura histórica descriptiva |
| `2026-11-06_kids-ballena-azul-corazon` | 06-nov | 07:00 / kids | **FAIL 80** | payoff_cierre_apertura; el cierre sobreafirma «casi se detiene» |
| `2026-11-06_comida-aguacate-negro` | 06-nov | 13:30 / comida_familia | **FAIL 79** | progresion_por_escena, transiciones_causales; repetición de escenas 5–6 |
| `2026-11-06_inter-ranas-congeladas` | 06-nov | 17:00 / intermedio_1 | **FAIL 83** | progresion_por_escena, transiciones_causales; repetición de límites de especie/condiciones |
| `2026-11-06_inter-arena-cantante` | 06-nov | 17:45 / intermedio_2 | **PASS 94** | Los siete checks true; flags vacíos |
| `2026-11-07_kids-huesos-bebe` | 07-nov | 07:00 / kids | **FAIL 82** | progresion_por_escena, transiciones_causales; escena 6 repite conteo y fusión |
| `2026-11-07_comida-hielo-caliente` | 07-nov | 13:30 / comida_familia | **FAIL 81** | apertura_in_medias_res; apertura basada en creencia, no en acción/anomalía |
| `2026-11-07_inter-pulpo-suenos` | 07-nov | 17:00 / intermedio_1 | **FAIL 80** | progresion_por_escena, transiciones_causales, payoff_cierre_apertura; repetición y payoff vago |
| `2026-11-07_inter-nubes-pesan` | 07-nov | 17:45 / intermedio_2 | **FAIL 78** | progresion_por_escena, transiciones_causales, payoff_cierre_apertura; la última escena repite cifra/límite y no paga la suspensión |

Todos los objetos `narrative_qa` conservan `review_basis="lectura_en_frio_solo_narracion"`, los siete checks explícitos, `reviewer_role="auditor_capcot_independiente"` y sus `critical_flags`. La lectura de este run ocultó título, resumen, arco, notas y `narrative_contract`; no se usaron esos campos para puntuar. Los doce JSON se releyeron después de escribir y contienen exactamente los scores/statuses de la tabla, con `reviewed_at="2026-11-07T15:45:21-06:00"`.

### Identidad temática

- El canónico `2026-11-05_inter-arboles-se-comunican` trata redes micorrícicas comunes y Karst et al. 2023. **No tiene desajuste temático**. Su FAIL es por apertura genérica y defectos estructurales.
- `cola/bloqueados/2026-11-05_inter-arboles-mito-respiran/` y su JSON suelto son otro artefacto: trata respiración nocturna. No se confundió con el canónico.
- El único ID del slot 7-nov 17:45 es `2026-11-07_inter-nubes-pesan`. El directorio `2026-11-07_extra-nubes-pesan/` declara `MATERIAL_DE_ORIGEN_NO_ES_PROYECTO`; no se cuenta como segundo proyecto. El JSON bloqueado suelto con el mismo project_id tampoco crea otro ID.

## 3. Validación estructural estática

No había runtime local del repositorio; **no se ejecutó** `python3 scripts/validar_storyboard.py` ni `--check-doi`. Se inspeccionó el código del validador y se reprodujeron estáticamente sus comprobaciones sobre los doce JSON.

### Cumplen

- 7 escenas en 11 proyectos y 8 en árboles.
- Gancho de 1–6 palabras; arco presente y ordenado.
- Voz exacta del contrato: edge-tts, `es-MX-JorgeNeural`, es-MX, +7%, -2Hz.
- 170–221 palabras en once proyectos; todos menos árboles cumplen el rango 170–235.
- 78 s de escenas + cortinilla de 6 s = **84 s** en los doce; `target_duration_seconds=84`.
- `narrative_contract` con sus seis campos no vacíos.
- `source_ids` referencian fuentes declaradas; entre 1 y 2 fuentes por paquete.
- Los doce `estilo_id` existen en `scripts/estilos.json`; `visual_identity.prompt_base` coincide literalmente con el catálogo y los prompts de escena empiezan con ese texto.
- `approved_assets=[]`, `export.render_status=NOT_GENERATED`; no aparecen claves `asset_filename`/`asset_type`, nombres de exportación ni rutas de medios. No hubo archivos de medios que verificar.

### Bloqueos

1. **Todos los doce:** faltan los seis campos narrativos estructurales en cada escena: `dramatic_beat`, `scene_function`, `causal_bridge_from_previous`, `question_state`, `reason_to_continue` y `new_information`. Son 42 ausencias por storyboard de siete escenas y 48 en árboles (ocho escenas). El validador rechaza los doce por esto, aunque el JSON sea válido.
2. **Árboles:** además tiene 169 palabras, no 170; no tiene capa de mapa con coordenadas/fuente ni capa de dato/gráfico con fuente. Acumula 51 errores estructurales estáticos.
3. **Diez FAIL narrativos:** el propio validador también rechaza `narrative_qa.status`, score, checks falsos y flags. Venus (88) y arena (94) pasan QA narrativo, pero no la estructura, por lo que tampoco se promueven.
4. **Ambiente/SFX:** `ambiente` está presente en las 85 escenas; 75/85 tienen `sfx=[]`. Rayo y arena tienen dos escenas con SFX vacío cada uno; los otros diez proyectos tienen SFX vacío en todas sus escenas. El campo existe, pero el silencio no está declarado explícitamente.
5. **DOI:** ocho proyectos tienen al menos un DOI declarado; Venus, aguacate, huesos y nubes usan fuentes URL sin DOI. Rayo tiene un DOI y una fuente sin DOI. Los estados de verificación son los declarados en los JSON; no se hizo consulta nueva a Crossref. Los mapas y capas de datos existen en once proyectos; árboles carece de ambos.

## 4. Cola, workflow y recepción Grok

### Cola y dispatchabilidad

- `cola/entrada/`: solo `.gitkeep`; no hay `*.json` de primer nivel ni `<project_id>/storyboard.json`.
- Los doce borradores están en `proyectos/<id>/storyboard.json`, fuera de los paths de dispatch. Resultado individual: **NOT_DISPATCHABLE** para los doce.
- El workflow `.github/workflows/capcot-grok-dispatch.yml` escucha `cola/entrada/*.json`. En push filtra `^cola/entrada/[^/]+\.json$`; en dispatch manual usa `find cola/entrada -maxdepth 1 -type f -name '*.json'` o construye `cola/entrada/<INPUT_PROJECT_ID>.json`. No encuentra carpetas anidadas ni `proyectos/`, `cola/bloqueados/` o `salidas/`.
- El procesador `scripts/procesar_cola.py` usa por defecto la fecha CDMX actual y filtra entradas por los primeros diez caracteres del nombre/ruta. Sin embargo, `--fecha` permite seleccionar otra fecha; no es una prohibición absoluta de procesar históricos. La selección de cola no lee `data/cola.json` como entrada: ese archivo contiene solo una incidencia fallida del 31-oct.
- `handoffs/grok_inbox/` contiene solo README; `handoffs/grok_done/` solo `.gitkeep`. No existe marcador de recepción.

### Estados individuales

Cada uno de estos doce paths devolvió 404:

- `cola/estado/2026-11-05_kids-dia-en-venus.json`
- `cola/estado/2026-11-05_comida-palomitas.json`
- `cola/estado/2026-11-05_inter-arboles-se-comunican.json`
- `cola/estado/2026-11-05_inter-rayo-globular.json`
- `cola/estado/2026-11-06_kids-ballena-azul-corazon.json`
- `cola/estado/2026-11-06_comida-aguacate-negro.json`
- `cola/estado/2026-11-06_inter-ranas-congeladas.json`
- `cola/estado/2026-11-06_inter-arena-cantante.json`
- `cola/estado/2026-11-07_kids-huesos-bebe.json`
- `cola/estado/2026-11-07_comida-hielo-caliente.json`
- `cola/estado/2026-11-07_inter-pulpo-suenos.json`
- `cola/estado/2026-11-07_inter-nubes-pesan.json`

Resultado literal para cada uno: **RECEPCION_GROK_NO_CONFIRMADA**. No se creó ni modificó ningún estado Grok.

### Actions

Los quince runs más recientes listados (147–133) son del 1-nov y terminaron en failure; no hay runs posteriores. Se inspeccionó el log completo del run #147 (2026-11-01 06:29:58 CDMX). Error literal:

`Falta configurar GROK_WEBHOOK_URL.`

El entorno de ese run también mostraba vacío `GROK_WEBHOOK_TOKEN`; la ejecución se detuvo en la primera comprobación. Esos logs corresponden al workflow anterior. El workflow actualmente en la rama usa el buzón gratuito `handoffs/grok_inbox/` y deja el webhook como opcional; no ha habido un run posterior que demuestre esa ruta. No se modificaron workflow, secretos ni permisos.

## 5. Producción preexistente y discrepancias de slots

No hay directorios `salidas/<project_id>/` de estos doce proyectos, ni `qa.json`, `publicacion.json`, `metadata.json` o `licencias.json` para el lote. Por tanto, no existe QA audiovisual verificable en el árbol.

El documento `ajustes_entre_modelos/ESTADO_SLOTS_2026-11-07.md` (corte aproximado 12:40 CDMX) registra:

| Tema asociado | ID YouTube | Horario que declara el documento | Evidencia / privacidad |
|---|---|---:|---|
| Venus — asociado por tema a `2026-11-05_kids-dia-en-venus` | `qy2PBz5vSqQ` | 7-nov 17:00, v1 programada | v2 corregida solo local, no subida; privacidad no consignada |
| Arena — asociado por tema a `2026-11-06_inter-arena-cantante` | `ztIkYcXB91U` | 7-nov 19:00, v1 programada | v2 solo local; privacidad no consignada |

Ambos se clasifican **PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR**. Los IDs aparecen en la nota operativa, no en los storyboards canónicos ni en `data/publicaciones.json`. La nota no incluye `project_id` explícito para esos IDs; la asociación es por tema/título. No se borró ni canceló nada. Resultado de medios: **MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO**; no hay carpeta de salida ni archivo audiovisual en el árbol para esos registros.

La discrepancia es material:
- `data/horario_semana_2026-11-01_07.json` asigna el 7-nov 17:00 a `2026-11-07_inter-pulpo-suenos` y 17:45 a `2026-11-07_inter-nubes-pesan`.
- La nota operativa pone Venus a las 17:00 y arena a las 19:00; la propia nota dice que 19:00 estaba retirado de la parrilla desde el 5-nov.
- Los storyboards Venus y arena conservan `publicacion.status=PENDIENTE_DECISION_GROK`, sin `yt_id`; la nota externa dice que sus v1 están programadas. No se actualizó esa decisión ni el horario.
- La misma nota registra que Mpemba (7-nov 13:30) no tiene mp4 ni programación y que su narrativa está FAIL. Esto coincide con el bloqueo del storyboard.
- La nota registra OAuth YouTube con `invalid_grant` desde aproximadamente 11:35 CDMX; no se intentó subir, borrar ni reprogramar por API.

No hay `yt_id_historial` en las doce entradas 5–7 de la parrilla. Los dos IDs de arriba son registros operativos separados, no se reinterpretan como historial ni como publicaciones verificadas.

## 6. Bloqueados, rotación y documentos contradictorios

### Copias bloqueadas

Se inventariaron las variantes heredadas en `cola/bloqueados/`: palomitas-explotan, árboles-mito-respiran, Venus-día-largo, rayo-globular, corazón-ballena-azul, aguacate-negro, ranas-congeladas, arena-cantante, Mpemba-mito, sueños-pulpo, huesos-bebé, nubes-pesan y extra-nubes-pesan. Varias conservan tanto JSON suelto como carpeta con `storyboard.json`; no son entradas activas. Los `ESTADO_EJECUCION.md` de las carpetas revisadas ya dicen `BORRADOR_EN_PROYECTOS_NO_APTO_PARA_PROMOCION`; extra-nubes dice `MATERIAL_DE_ORIGEN_NO_ES_PROYECTO`. No hubo que corregirlos ni moverlos porque `cola/entrada/` está vacía.

### Datos y rotación

- `data/temas_del_dia.json` llega hasta 2026-10-28.
- `data/estilos_usados.json` llega hasta 2026-10-28.
- `data/publicaciones.json` y `data/rotacion.json` están vacíos.
- `data/cola.json` conserva una entrada fallida del 31-oct, fuera de la cola activa.
- `data/horario_semana_2026-11-01_07.json` sigue marcando los doce slots como `pedir_chatgpt`, aunque los borradores ya están en `proyectos/`.
- Los doce estilos existen en catálogo y ninguno es uno de los estilos prohibidos. No hay repetición dentro de un mismo día; `papel_rasgado_capas` se repite en árboles (5-nov) y ranas (6-nov). Como el registro de estilos usados se detiene el 28-oct, no puede certificarse la rotación histórica completa.
- `scripts/registro_editorial.py` incorpora proyectos, entradas de cola y salidas, pero su recorrido no incluye las variantes anidadas de `cola/bloqueados/`; el registro no sustituye el inventario manual de bloqueados.

### Documentos

- Existen los radares `2026-11-05_RADAR_CAPCOT.md`, `2026-11-06_RADAR_CAPCOT.md` y `2026-11-07_RADAR_CAPCOT.md`. Los tres conservan corte de investigación/Trends del 1-nov; no son investigación fresca del día. El radar del 7-nov reproducía los QA anteriores y decía que no había hecho nueva lectura; este run sí releyó las narraciones y actualizó solo la marca de revisión.
- `PARA_CHATGPT_semana_01-07nov.md` conserva la ruta antigua `cola/entrada/<id>/` con tres archivos, ocho escenas y 1100–1300 caracteres. Es legado y contradice el contrato operativo vigente.
- `PARA_CHATGPT_hasta_08nov.md` afirma que los paquetes estaban en cola y mantiene horarios antiguos de 19:00; no coincide con el árbol actual ni con el horario semanal vigente.
- `PARA_CHATGPT_5-7nov_PASS_auditor.md` contiene los doce IDs canónicos y reconoce 17:45, además de distinguir el material extra de nubes. Se mantiene la jerarquía del `CONTRATO_OPERATIVO_UNIFICADO.md`.
- `ESTADO_SLOTS_2026-11-07.md` es más reciente que varios briefs, pero contradice la parrilla en 17:00/17:45/19:00. Se registra como discrepancia, no como modificación autorizada del horario.

## 7. Cierre de ejecución

Cambios realizados en esta auditoría:
1. Relectura en frío de las doce narraciones.
2. Actualización exclusiva de `narrative_qa.reviewed_at` a `2026-11-07T15:45:21-06:00` en los doce storyboards; status, score, siete checks y flags se conservaron.
3. Creación de este reporte y lectura de vuelta desde GitHub.

No se modificaron `data/*.json`, `main`, workflow, secretos, permisos, decisiones editoriales, narraciones, claims, fuentes, estados Grok ni publicaciones. No se promovió ni movió ningún paquete. No se ejecutaron scripts por falta de runtime local; revisión estática. No se revisaron APIs de plataforma porque no se identificó un cambio oficial nuevo sustentado. No se generaron frames, imágenes, voz, audio, video ni renders; no se publicó ni se consumieron créditos.

**Decisión:** lote abierto. Los doce borradores permanecen en `proyectos/`; Venus y arena, además, quedan protegidos contra redispatch por programación preexistente. No hay paquete listo para handoff.
