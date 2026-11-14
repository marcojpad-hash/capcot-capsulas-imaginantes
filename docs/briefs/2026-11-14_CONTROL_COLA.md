# CONTROL COLA CAPCOT — 2026-11-14

**Repositorio:** `marcojpad-hash/capcot-capsulas-imaginantes`  
**Rama:** `feature/capcot-video-discovery-continuity`  
**Corte:** 2026-11-14, 15:04 CDMX  
**Rol:** auditoría; no producción, no medios, no publicación, no dispatch.

## 0. Alcance y precedencia

Leídos el Contrato Operativo Unificado, Plan Maestro, Receta, Guía de Modelo Externo, Flujo Externo, contrato de estado Grok, QA narrativo en frío, continuidad audiovisual, líneas temáticas, voces por tema, flujo de producción, plantillas, catálogo `scripts/estilos.json`, validador, procesador, rotación, registro editorial y los 20 JSON existentes en `data/`.

Precedencia aplicada: Contrato Operativo → Plan Maestro → Receta/Guía → Flujo Externo/Contrato Grok → plantillas, catálogo y validadores. `templates/storyboard_vertical.template.json` es la plantilla vigente. `templates/storyboard.template.json` conserva el esquema antiguo 16:9/120 s y rutas de assets; no se utilizó. Los documentos de `docs/obsoleto/2026-10-31/` están archivados por el Plan Maestro. `docs/FLUJO_DE_PRODUCCION.md` sigue visible y no está marcado como obsoleto; conserva un procedimiento anterior de 60–180 s y debe considerarse subordinado a la Receta/Flujo Externo vigentes.

## 1. Día actual — 14 de noviembre

### Briefs y archivos

- Existe `docs/briefs/2026-11-14_RADAR_CAPCOT.md` (corte 08:01 CDMX).
- Antes de esta auditoría no existía `docs/briefs/2026-11-14_CONTROL_COLA.md`; este archivo es el control del día.
- En `proyectos/` hay exactamente un storyboard con fecha objetivo 2026-11-14: [`2026-11-14_dato-microplasticos-pantanal`](../../proyectos/2026-11-14_dato-microplasticos-pantanal/storyboard.json).
- No hay JSON de ese día en `cola/entrada/`, ni salida, bloqueado, estado Grok o marcador de handoff del día.
- No existe `data/horario_2026-11-14.json` (404). `data/horarios.json` sí contiene la ventana de tarde 16:30–18:00; el radar propone 17:00 como staging editorial, no como programación. El storyboard no tiene `slot_cesta`.

### Fecha de creación, fecha objetivo y slot

- Creación del borrador: commit `7accf0d0821a91da1f6dbdc807ef57c5e73e471f`, 2026-11-14 14:22:52 UTC = 08:22:52 CDMX. No se atribuye el commit a un agente sin evidencia.
- Fecha objetivo: 2026-11-14.
- Slot declarado: 17:00 CDMX, dentro de la ventana de tarde. No hay `slot_cesta` ni registro diario específico que lo convierta en una asignación editorial/programación confirmada.

### QA narrativo y validación estructural

<badge>El JSON es la fuente de verdad</badge>

Lectura en frío de la narración concatenada, sin título, resumen, arco, notas ni `narrative_contract`:

- `narrative_qa.status = PASS`
- `score = 88`
- `review_basis = lectura_en_frio_solo_narracion`
- Siete checks verdaderos: pregunta central, apertura in medias res, progresión, transiciones causales, giro científico, límite de evidencia y payoff.
- `critical_flags = []`
- `reviewer_role = auditor_capcot_independiente`
- `reviewed_at = 2026-11-14T15:04:13-06:00`

Revisión estructural estática posterior a correcciones:

| Control | Resultado |
|---|---:|
| Escenas | 8 |
| Palabras según el patrón de `scripts/validar_storyboard.py` | 193 |
| Duración de escenas | 78 s |
| Cortinilla | 6 s |
| Total | 84 s |
| Gancho | 5 palabras |
| Arco | hook_medias_res → desarrollo → cierre_historia → reflexion_o_pregunta |
| `source_ids` | Todos resuelven a SRC-001 |
| DOI | 10.1038/s41586-026-11285-x; verificado en la página oficial de Nature |
| `prompt_base` | Coincide literalmente con `scripts/estilos.json`; los 8 prompts comienzan con él |
| Mapa y dato/gráfico | Capas en escenas 002 y 004, con fuente |
| Ambiente/SFX | Presentes en las 8 escenas |
| `approved_assets` | [] |
| `export.render_status` | NOT_GENERATED |
| `asset_filename`, `asset_type`, rutas y `export.filename` | Ausentes |
| Publicación | PENDIENTE_DECISION_GROK |

El DOI y los datos principales se contrastaron con la página editorial de Nature: https://www.nature.com/articles/s41586-026-11285-x. El artículo confirma 47 muestras, 40 animales con GPS suficiente, 17,165 partículas HQI >75, 2,815 clasificadas como microplásticos (16.4%), 43/47 animales positivos y presencia en todos los individuos muestreados en el Pantanal. También presenta el transporte atmosférico y acuático como vías probables, no como trayectorias individuales demostradas.

### Correcciones documentales efectuadas

Storyboard actualizado y releído desde GitHub:

- Se registró `narrative_qa` PASS 88.
- Se copiaron a las escenas 002 y 004 las capas de mapa y dato que ya existían en el objeto raíz; no se añadieron claims.
- Se corrigió `word_count` de 194 a 193, conforme al patrón del validador.
- Se cambió el estado documental a `QA_NARRATIVO_PASS_PENDIENTE_DECISION_GROK`; `editorial_status` sigue siendo `PROPUESTA_PENDIENTE_DE_GROK`.
- `verification_status` de la fuente pasó a `VERIFICADO_RESOLVEDOR` por verificación en la página oficial del editor. No se ejecutó el helper Crossref.
- No se modificó narración, claims, selección, publicación ni horario.

Commit de sincronización final: `c7c93019651a643dc0f21b5483de7ceaa43ef835`. Blob SHA releído: `c644ec0ecb182b0612ae8aaf69b28e6c8d6660c9`.

**Discrepancia del radar:** el RADAR de las 08:01 todavía dice 194 palabras, DOI pendiente y QA pendiente. Es una instantánea anterior. Prevalece el storyboard releído: 193 palabras, DOI verificado en Nature y QA PASS 88.

### Estado de handoff

- Ruta actual: `proyectos/2026-11-14_dato-microplasticos-pantanal/storyboard.json`.
- Dispatch: **NOT_DISPATCHABLE**. La ruta no está en `cola/entrada/`.
- Estado: `cola/estado/2026-11-14_dato-microplasticos-pantanal.json` no existe.
- Recepción: **RECEPCION_GROK_NO_CONFIRMADA**.
- No se promovió a cola: la instrucción de este run prohíbe disparar workflows; además, no hay cesta editorial asignada y existe una discrepancia de política de voz descrita abajo.
- No se creó ni modificó ningún estado de Grok.

## 2. Inventario de cola del día y dispatchabilidad

**Entradas de cola con fecha 2026-11-14: 0.**  
**Borradores de proyecto con fecha objetivo 2026-11-14: 1.**  
**Salidas/bloqueados/estados de Grok con fecha 2026-11-14: 0.**

La rama conserva tres paquetes históricos anidados en `cola/entrada/<project_id>/storyboard.json`:

| Paquete | Creación del archivo (CDMX) | Fecha objetivo/slot | Ruta y dispatch |
|---|---|---|---|
| 2026-11-07 dato-clavo-te-cocina | 07-nov 18:00:20 | 07-nov, dato del día 23:30 | Anidado; NOT_DISPATCHABLE |
| 2026-11-09 dato-robot-ensambla-orbita | 09-nov 18:40:20 | 09-nov, dato del día 23:30 | Anidado; NOT_DISPATCHABLE |
| 2026-11-11 dato-ratas-topo-damaraland | 11-nov 19:27:46 | 11-nov, dato del día 23:30 | Anidado; NOT_DISPATCHABLE |

Estos tres slots de dato del día 23:30 se enumeran solo como inventario de rutas/fechas; su contenido queda fuera de la revisión por la exclusión expresa de esta instrucción.

### Workflow y procesador

`.github/workflows/capcot-grok-dispatch.yml`:

- Evento push: solo `cola/entrada/*.json`.
- Selector manual `all`: `find cola/entrada -maxdepth 1 -type f -name '*.json'`.
- Selector manual por ID: espera `cola/entrada/<id>.json`.
- Por tanto, los tres paquetes anidados no disparan el workflow; el proyecto del día en `proyectos/` tampoco.
- El workflow actual escribe un marcador `pending` en `handoffs/grok_inbox/`; el webhook es opcional.

`scripts/procesar_cola.py`:

- Descubre JSON de primer nivel y `*/storyboard.json`.
- Por defecto usa la fecha actual de America/Mexico_City.
- Filtra por los primeros diez caracteres del nombre del archivo/directorio, no por `fecha_objetivo` interno.
- Permite sobrescribir la fecha con `--fecha`; por tanto, el comportamiento predeterminado es la fecha actual, pero no existe una prohibición absoluta de procesar una fecha histórica si alguien invoca el override.

`scripts/registro_editorial.py`:

- Lee storyboards de `proyectos/`, `cola/entrada/`, `cola/` y `salidas/`, además de registros canónicos.
- No incluye `cola/bloqueados/`, `handoffs/grok_inbox/`, `handoffs/grok_done/` ni los JSON diarios de publicación; su vista no basta para reconciliar por sí sola bloqueados, handoff y publicaciones recientes.

### Acciones y recepción

- Última ejecución identificada de `capcot-grok-dispatch` en la rama: run #129, 2026-11-01, conclusión failure.
- El endpoint de jobs devolvió una lista vacía; descarga de logs devolvió 404. No hay error literal recuperable ni evidencia para atribuir la falla a un secreto.
- El workflow trata `GROK_WEBHOOK_URL`/`GROK_WEBHOOK_TOKEN` como opcionales; no se reporta que falten.
- Existe un marcador histórico en `handoffs/grok_inbox/2026-11-09_dato-robot-ensambla-orbita.json` con `status=pending`; no es un acuse de lectura por Grok. `handoffs/grok_done/` solo contiene `.gitkeep`.
- No hay archivos bajo `cola/estado/`. Para el proyecto del día y los 12 proyectos del lote, los paths consultados devolvieron 404: **RECEPCION_GROK_NO_CONFIRMADA**.

## 3. Lote obligatorio 5–7 de noviembre

Los 12 storyboards se crearon en el commit de staging `7a415426f5907c2ab03687a47f3d160a595cb669`, 2026-11-02 22:11:24 UTC = 16:11:24 CDMX. Sus `project_id`, `fecha_objetivo`, `slot_local` y `slot_cesta` coinciden con `data/horario_semana_2026-11-01_07.json`.

Los QA se releyeron en frío el 14-nov; se actualizó únicamente `reviewed_at` a `2026-11-14T15:04:13-06:00`. Scores, statuses, checks y flags se conservaron exactamente como aparecen en los JSON.

| Proyecto | Slot/cesta | QA | Checks falsos | critical_flags |
|---|---|---:|---|---|
| 2026-11-05_kids-dia-en-venus | 07:00 / kids | PASS 88 | ninguno | [] |
| 2026-11-05_comida-palomitas | 13:30 / comida_familia | FAIL 82 | apertura, progresión | APERTURA_DEFINICIONAL_NO_IN_MEDIAS_RES; ESCENA_6_REITERA_CAUSAS_DE_GRANOS_NO_REVENTADOS_SIN_INFORMACION_NUEVA |
| 2026-11-05_inter-arboles-se-comunican | 17:00 / intermedio_1 | FAIL 78 | apertura | APERTURA_GENERICA_NO_IN_MEDIAS_RES |
| 2026-11-05_inter-rayo-globular | 17:45 / intermedio_2 | FAIL 81 | apertura | APERTURA_HISTORICA_DESCRIPTIVA_NO_IN_MEDIAS_RES |
| 2026-11-06_kids-ballena-azul-corazon | 07:00 / kids | FAIL 80 | payoff | PAYOFF_SOBREAFIRMA_CASI_SE_DETIENE |
| 2026-11-06_comida-aguacate-negro | 13:30 / comida_familia | FAIL 79 | progresión, transiciones | REPETICION_ESCENAS_5_6_SIN_AVANCE_CAUSAL |
| 2026-11-06_inter-ranas-congeladas | 17:00 / intermedio_1 | FAIL 83 | progresión, transiciones | REPETICION_ESCENAS_5_6_LIMITES_DE_ESPECIE_Y_CONDICIONES |
| 2026-11-06_inter-arena-cantante | 17:45 / intermedio_2 | PASS 94 | ninguno | [] |
| 2026-11-07_kids-huesos-bebe | 07:00 / kids | FAIL 82 | progresión, transiciones | ESCENA_6_REPITE_VARIACION_DE_CONTEO_Y_FUSION |
| 2026-11-07_comida-hielo-caliente | 13:30 / comida_familia | FAIL 81 | apertura | APERTURA_DE_CREENCIAS_NO_IN_MEDIAS_RES |
| 2026-11-07_inter-pulpo-suenos | 17:00 / intermedio_1 | FAIL 80 | progresión, transiciones, payoff | REPETICION_ESCENAS_5_6_Y_PAYOFF_VAGO |
| 2026-11-07_inter-nubes-pesan | 17:45 / intermedio_2 | FAIL 78 | progresión, transiciones, payoff | ESCENA_7_REITERA_CIFRA_Y_LIMITE_SIN_PAYOFF_DE_SUSPENSION |

**Resultado narrativo:** 2 PASS, 10 FAIL. Todos conservan los siete checks explícitos en `narrative_qa`, con `review_basis=lectura_en_frio_solo_narracion`.

### Validación estructural estática del lote

- 12/12: 7–8 escenas, 84 s con cortinilla de 6 s, gancho de 3–5 palabras.
- Palabras: Venus 170; palomitas 173; árboles 169; rayo 197; ballena 174; aguacate 170; ranas 177; arena 206; huesos 172; hielo 172; pulpo 170; nubes 221.
- **510 campos narrativos ausentes:** los seis campos `dramatic_beat`, `scene_function`, `causal_bridge_from_previous`, `question_state`, `reason_to_continue` y `new_information` faltan en las 85 escenas.
- **75/85 arrays SFX vacíos**; ambiente presente en las 85 escenas.
- El storyboard de árboles tiene 169 palabras (una menos que el mínimo), y carece de capa de mapa y capa de dato/gráfico en escenas.
- En los demás 11 storyboards sí existen las capas de mapa y dato/gráfico.
- Los 12 estilos existen en el catálogo; `visual_identity.prompt_base` coincide y todos los `image_prompt` empiezan con el prompt exacto.
- `source_ids` resuelven a fuentes declaradas. Los DOI con valor tienen estado de verificación registrado; algunas fuentes institucionales no tienen DOI.
- `approved_assets=[]`, `export.render_status=NOT_GENERATED`; no hay `asset_filename`, `asset_type` ni rutas de medios en los 12 borradores.
- Los dos PASS narrativos (Venus y Arena) no superan la estructura; no son aptos para promoción.

### Tema, identidad y fuentes

- Los 12 temas, títulos y fuentes corresponden al tema del horario, salvo una discrepancia factual puntual: el storyboard de pulpo nombra `Octopus insularis`, pero el DOI 10.1038/s41586-023-06203-4 (Pophale et al., Nature 2023) estudia `Octopus laqueus`. La página primaria lo confirma: https://www.nature.com/articles/s41586-023-06203-4. Es un desajuste de especie/fuente, no de cesta temática.
- El storyboard canónico `2026-11-05_inter-arboles-se-comunican` sigue tratando redes micorrícicas comunes y Karst et al. 2023; no se marca desajuste temático. Su blob actual es `b06ab29701a48a59d5f80e232c72452b8098f615`, distinto del SHA histórico `854c12ed9b77f82f66ec736797dea4d700983d78`. La variante `2026-11-05_inter-arboles-mito-respiran` es otro artefacto bloqueado, no el storyboard canónico.
- El slot 2026-11-07 17:45 sigue siendo exactamente `2026-11-07_inter-nubes-pesan`. `2026-11-07_extra-nubes-pesan` es material/variante del mismo proyecto, no un segundo slot.

### Estilos y voz

Los 12 estilos están en el catálogo y no se repiten dentro de un mismo día. `papel_rasgado_capas` aparece el 5 y 6-nov, pero no como repetición dentro del mismo día. El estilo del proyecto 14-nov (`papel_rasgado_capas`) no repite el estilo del storyboard 13-nov (`dibujo_cientifico_scratchboard`).

Hay una contradicción de contrato que afecta handoff: `docs/VOCES_POR_TEMA.md` asigna `narradora_es` (VoxCPM2) a biología y cocina; los siete proyectos de biología/cocina del lote siguen declarando JorgeNeural. `docs/PLAN_MAESTRO_AUTOMATICO.md`, Receta, Continuidad Audiovisual, plantilla vertical y `scripts/validar_storyboard.py` siguen fijando Edge TTS JorgeNeural para todos. El proyecto actual de fauna/ecología también declara JorgeNeural. No se cambió ninguna voz: hace falta reconciliar el contrato y el validador antes de usar esa política.

### Bloqueados y copias heredadas

Se inspeccionaron los artefactos bloqueados relacionados. Hay copias exactas de Rayo globular, Arena cantante, Aguacate negro, Ranas congeladas, Huesos bebé y Nubes pesan. Hay variantes separadas para Palomitas (`comida-palomitas-explotan`), Árboles (`inter-arboles-mito-respiran`), Venus (`inter-venus-dia-largo`), Ballena (`inter-corazon-ballena-azul`) y Pulpo (`inter-suenos-pulpo`); la variante extra de Nubes mantiene el mismo `project_id` canónico. No se movió ni eliminó ningún archivo. No hay copias canónicas de estos 12 en `cola/entrada/` que requieran traslado por FAIL.

## 4. Guardia de producción preexistente

No existen directorios `salidas/<project_id>/` en el árbol GitHub para los 12 proyectos; por tanto, no hay `storyboard.json`, `qa.json`, `publicacion.json`, `metadata.json` ni `licencias.json` audiovisuales verificables allí. Tampoco hay archivo separado `historial_youtube`; `data/vistas_historico.json` contiene 74 snapshots hasta 28-oct y no incluye estos IDs.

Sin embargo, los registros diarios posteriores acreditan procesamiento/programación preexistente para cinco proyectos. Todos quedan como **PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR**:

| Proyecto | YouTube | TikTok | Facebook | Evidencia/horario registrado |
|---|---|---|---|---|
| Palomitas | `zTP5akrGA9M`, publicado | `7705593452003691794`, publicado | `1167496802382795`, publicado | 08-nov 07:00 CDMX; originalmente 05-nov 13:30 |
| Ranas | `UBFuKBU3cx0`, público | `7705596671807245586`, publicado | `programado_lote_7nov` | YT/TT 09-nov 07:00; originalmente 06-nov 17:00 |
| Aguacate | `nSS_q2tj2P0`, público | `7705594217136966920`, publicado | `programado_lote_7nov` | YT/TT 10-nov 07:00; originalmente 06-nov 13:30 |
| Ballena | `wbFrlM2e_YE`, público | `7705594333574991122`, publicado | `programado_lote_7nov` | YT/TT 11-nov 07:00; originalmente 06-nov 07:00 |
| Hielo caliente | `HSgrnejAcaI`, privado/programado | `7706905447424347393`, programado | programado, visibilidad UI pública | 11-nov 13:30 CDMX; originalmente 07-nov 13:30 |

Discrepancia temporal: cuatro slots originales se ejecutaron días después y varios cambiaron a la franja 07:00. Hielo conserva programación posterior; riesgo de duplicado si se reencola. Los registros dan duración de YouTube de 83 s (aguacate), 80 s (ballena) y 90 s (hielo); no hay `qa.json` audiovisual en GitHub para verificar QA local ni duración medida de Palomitas/Ranas.

Los cinco registros diarios citan rutas MP4 bajo `/workspace/` que no existen en el árbol GitHub: **MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO**. No se afirma que esos medios estén versionados.

Los otros siete proyectos no muestran IDs ni programación en los registros diarios consultados. No tienen salida GitHub; algunos sí tienen artefactos bloqueados. Ninguno se promovió.

## 5. Reconciliación de datos y contradicciones operativas

Se leyeron los 20 JSON de `data/`. Los registros no tienen el mismo corte:

- `data/temas_del_dia.json`: solo 24–28-oct.
- `data/estilos_usados.json`: 21 registros, hasta 28-oct.
- `data/rotacion.json`: 27 registros, hasta 31-oct.
- `data/publicaciones.json`: 22 registros, hasta 01-nov.
- `data/cola.json`: un registro histórico, ninguno del 14-nov.
- `data/vistas_historico.json`: 74 snapshots, hasta 28-oct; no incluye los cinco IDs de publicación de este lote.
- `data/horario_semana_2026-11-01_07.json`: fuente de asignación de los 12 slots; coincide con los storyboards.
- `data/horario_2026-11-08.json` a `data/horario_2026-11-11.json`: registros posteriores de publicaciones/programaciones que contradicen el estado antiguo `pedir_chatgpt` de la parrilla semanal.
- `data/horarios.json`, actualizado 09-nov: ventanas 06:30–07:30 y 16:30–18:00, con 23:30 como slot fijo dato del día.
- `scripts/rotacion.py` todavía declara cinco ventanas: 07–09, 13–15, 16–18, 18–21 y 23–24. Conserva 19:00 aunque `data/horarios.json` dice que se retiró; conserva mediodía como ventana operativa aunque la política lo marca a prueba. El Plan/Contrato también hablan de cinco slots diarios. Hay que reconciliar código, política de horarios y cupo antes de asumir que las cinco ventanas siguen activas.
- `data/horario_2026-11-14.json` no existe; no hay asignación diaria formal para el proyecto actual.

La vista de `registro_editorial.py` no cubre bloqueados, handoffs ni registros diarios. No puede certificar por sí sola unicidad, recepción o publicación.

## 6. Runtime, APIs y límites de esta ejecución

- No había runtime local del repositorio. No se ejecutaron `scripts/validar_storyboard.py`, `procesar_cola.py`, helpers ni pruebas Python. Se hizo revisión estática, incluyendo reproducción manual de las condiciones estructurales del validador para el proyecto del día y el lote.
- El storyboard del día pasa la revisión estática tras las correcciones; los 12 del lote fallan estructura por los 510 campos narrativos ausentes, además de los defectos indicados.
- No se revisaron cambios de APIs: no apareció evidencia de un cambio oficial nuevo que lo justificara. La verificación del DOI del proyecto actual se hizo contra la página oficial de Nature, no mediante el helper Crossref.
- No se dispararon workflows, no se enviaron payloads, no se consultaron ni cambiaron secretos, no se modificaron permisos, `main` ni `data/*.json`.
- No se generaron imágenes, frames, audio, voz, video ni renders; no se publicó, programó ni consumió créditos.

## 7. Decisión de auditoría

1. Proyecto 14-nov: QA narrativo PASS 88 y estructura estática PASS, pero permanece en `proyectos/` como propuesta. No hay slot_cesta ni decisión editorial de Grok; el handoff no está confirmado.
2. Lote 5–7: 2 PASS narrativos, 10 FAIL; 0/12 pasan estructura. No promover.
3. Cinco proyectos con procesamiento/programación preexistente: no redispatchar.
4. Todos los estados Grok consultados que faltan quedan como **RECEPCION_GROK_NO_CONFIRMADA**.
5. El lote obligatorio permanece abierto.
