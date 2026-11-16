# CONTROL DE COLA — 2026-11-16

- Repositorio: `marcojpad-hash/capcot-capsulas-imaginantes`
- Rama auditada: `feature/capcot-video-discovery-continuity`
- HEAD observado antes de esta auditoría: `9967476e77684c41e50c811d9da5bb0a87a13532`
- Alcance: inventario del día, handoff/dispatch, lote obligatorio 5–7 nov, producción preexistente, datos, procesador, workflow y registro editorial.
- Restricciones respetadas: no se generaron medios, no se publicaron cápsulas, no se dispararon workflows, no se enviaron payloads, no se modificaron `data/*.json`, estados de Grok, workflow, permisos, secretos ni `main`.

## 1. Briefs e inventario del 16-nov

Briefs existentes en la rama:
- `docs/briefs/2026-11-16_RADAR_CAPCOT.md`: existe.
- `docs/briefs/2026-11-16_CONTROL_COLA.md`: no existía al iniciar esta auditoría; creado con este informe.
- `docs/briefs/2026-11-15_CONTROL_COLA.md`, `2026-11-14_CONTROL_COLA.md` y `2026-11-13_CONTROL_COLA.md`: existen.

Inventario exhaustivo de rutas del día en el árbol de la rama:
- Borradores en `proyectos/<project_id>/storyboard.json`: **1**.
- Entradas de `cola/entrada/*.json` o `cola/entrada/<project_id>/storyboard.json` con fecha objetivo 2026-11-16: **0**.
- Salidas en `salidas/<project_id>/` para el día: **0**.
- Estados `cola/estado/<project_id>.json` del proyecto del día: **404**.
- Marcador `handoffs/grok_inbox/<project_id>.json` del proyecto del día: no existe.

Único borrador:
- `proyectos/2026-11-16_dato-polen-desenreda-nanotubos/storyboard.json`
- `project_id`: `2026-11-16_dato-polen-desenreda-nanotubos`
- `fecha_objetivo`: `2026-11-16`
- `slot_local`: `17:00`
- `slot_cesta`: `intermedio_1`
- `editorial_status`: `PENDIENTE_DECISION_GROK`
- `publicacion.status`: `PENDIENTE_DECISION_GROK`
- Estado documental después de auditoría: `BORRADOR_EN_PROYECTOS_PENDIENTE_VALIDACION_ESTRUCTURAL`.

El RADAR propone 17:00 como candidato principal. La hora cae dentro de la ventana 16:30–18:00 de `data/horarios.json`, pero no existe `data/horario_2026-11-16.json` ni una selección oficial de cesta. Lunes no aparece como día preferido, pero tampoco como día excluido. Por tanto, sigue siendo **propuesta**, no selección.

El candidato de 23:30 del RADAR permanece `PENDING_SOURCE`; no existe storyboard para ese slot.

### QA narrativo independiente del borrador

Se leyó únicamente la narración concatenada, sin título, resumen, arco ni `narrative_contract`.

- `narrative_qa.status`: **PASS**
- `narrative_qa.score`: **91**
- `review_basis`: `lectura_en_frio_solo_narracion`
- Siete checks: true.
- `critical_flags`: `[]`.

La historia abre con la tinta que se apelmaza, reconstruye cómo los microgeles de polen capturan y ayudan a desagregar CNT con agitación suave, explica la estabilización con alginato y cierra aclarando que el polen no es el conductor.

### Estructura y fuente del borrador

- 8 escenas; 196 palabras por conteo del validador estático.
- 78 s de escenas + 6 s de cortinilla = 84 s.
- Gancho: 4 palabras.
- Voz: edge-tts `es-MX-JorgeNeural`, +7%, −2 Hz.
- `narrative_contract`: seis campos presentes.
- Las ocho escenas contienen los seis campos de progresión dramática requeridos.
- `source_ids` válidos en todas las escenas.
- `prompt_base` coincide literalmente con `scripts/estilos.json`; los ocho prompts empiezan con él.
- Estilo `collage_cientifico_vintage`: existe en el catálogo.
- Mapa y capa de dato presentes; ambiente y SFX declarados en las ocho escenas.
- `approved_assets=[]`; `export.render_status=NOT_GENERATED`.
- Sin `asset_filename`, `asset_type`, rutas de medios ni `export.filename`.

Correcciones mecánicas hechas en el storyboard, sin reescribir narración ni claims:
- Añadido `trend_source`.
- Añadido `cita_corta` a las tres fuentes.
- Registrado `narrative_qa` PASS/91.
- Estado documental actualizado a pendiente de validación estructural.

La fuente primaria es Gao et al., *Nature Communications*, publicada en línea el 14-nov-2026, DOI [10.1038/s41467-026-79607-1](https://doi.org/10.1038/s41467-026-79607-1). El PDF editorial confirma el mecanismo de captura-colisión-fricción con agitación suave, la estabilización con alginato y estabilidad acuosa superior a seis meses: [artículo/PDF oficial](https://www.nature.com/articles/s41467-026-79607-1). El campo del storyboard sigue `PENDIENTE_RESOLVEDOR`: no se ejecutó `--check-doi` ni Crossref.

**Handoff:** `NOT_DISPATCHABLE`. El borrador está en `proyectos/`, no en `cola/entrada/`; el workflow solo escucha JSON de primer nivel en `cola/entrada/*.json`. No se promovió porque la instrucción prohíbe disparar workflows y el validador Python real no pudo ejecutarse. Recepción: **RECEPCION_GROK_NO_CONFIRMADA**.

## 2. Cola histórica presente en la rama

Hay cuatro paquetes anidados en `cola/entrada/`; ninguno tiene fecha objetivo 16-nov y ninguno coincide con el patrón de paths del workflow:

| ID | Contenido observado | Estado Grok | Dispatch |
|---|---|---|---|
| `2026-11-07_dato-clavo-te-cocina` | 8 escenas, 202 palabras; sin `narrative_qa`; paquete textual | 404 | NOT_DISPATCHABLE |
| `2026-11-09_dato-robot-ensambla-orbita` | 9 escenas, 210 palabras; `narrative_qa` PASS/90; frames pendientes | 404; marcador de inbox `pending` | NOT_DISPATCHABLE |
| `2026-11-11_dato-ratas-topo-damaraland` | 8 escenas, 212 palabras; falta `narrative_contract` y `narrative_qa`; 8 `asset_filename` y 8 PNG reales en `frames/` | 404 | NOT_DISPATCHABLE |
| `2026-11-15_dato-dia-diapausa-lestes-sponsa` | 8 escenas, 182 palabras; QA PASS/90; 8 `asset_filename` para JPG que no existen en el árbol | 404 | NOT_DISPATCHABLE |

El marcador `handoffs/grok_inbox/2026-11-09_dato-robot-ensambla-orbita.json` tiene `status: pending`, rama `main` y paquete anidado. **No es recibo de Grok**. No hay marcador para el proyecto del 16-nov.

Los ocho PNG de ratas topo sí existen como archivos del repositorio; no fueron generados en esta auditoría. Los JPG de Lestes son rutas planeadas, no medios. El estado de Lestes dice `PREPARADO_PENDIENTE_REVISION_GROK` y reporta un validador previo exit 0, pero el storyboard conserva rutas `asset_filename` prohibidas por el contrato vigente; no se pudo reproducir el validador en este run.

## 3. Lote obligatorio 5–7 de noviembre

Los doce `project_id`, `fecha_objetivo`, `slot_local` y `slot_cesta` coinciden con `data/horario_semana_2026-11-01_07.json`. Se verificó el tema de cada uno. El canónico `2026-11-05_inter-arboles-se-comunican` sí trata redes micorrícicas comunes y Karst et al. 2023; no se marca desajuste temático.

QA en frío releído y `reviewed_at` actualizado a 2026-11-16. Los scores/statuses siguientes son los valores de los JSON releídos después de escribir:

| Proyecto | Score | Status |
|---|---:|---|
| `2026-11-05_kids-dia-en-venus` | 88 | PASS |
| `2026-11-05_comida-palomitas` | 82 | FAIL |
| `2026-11-05_inter-arboles-se-comunican` | 78 | FAIL |
| `2026-11-05_inter-rayo-globular` | 81 | FAIL |
| `2026-11-06_kids-ballena-azul-corazon` | 80 | FAIL |
| `2026-11-06_comida-aguacate-negro` | 79 | FAIL |
| `2026-11-06_inter-ranas-congeladas` | 83 | FAIL |
| `2026-11-06_inter-arena-cantante` | 94 | PASS |
| `2026-11-07_kids-huesos-bebe` | 82 | FAIL |
| `2026-11-07_comida-hielo-caliente` | 81 | FAIL |
| `2026-11-07_inter-pulpo-suenos` | 72 | FAIL |
| `2026-11-07_inter-nubes-pesan` | 78 | FAIL |

Dos PASS narrativos, diez FAIL. Ninguno supera el contrato estructural completo.

Resumen estructural verificado:
- 85 escenas en total.
- **510 campos narrativos ausentes**: seis por escena (`dramatic_beat`, `scene_function`, `causal_bridge_from_previous`, `question_state`, `reason_to_continue`, `new_information`).
- **75 arrays SFX vacíos**; la receta exige expresar el silencio explícitamente.
- `2026-11-05_inter-arboles-se-comunican`: 169 palabras (mínimo 170), sin capa de mapa ni dato/gráfico.
- Los otros once cumplen 7–9 escenas, 170–235 palabras, 75–90 s con cortinilla de 6 s y gancho de máximo seis palabras.
- Los doce tienen estilo del catálogo, `prompt_base` literal, voz prevista correcta y `source_ids` que resuelven.
- Los doce tienen `approved_assets=[]`, `export.render_status=NOT_GENERATED` y no contienen `asset_filename` ni `asset_type`.
- Los doce estados `cola/estado/<project_id>.json` devolvieron 404: **RECEPCION_GROK_NO_CONFIRMADA**.

Hallazgo factual: el storyboard de pulpo atribuye el estudio de Pophale et al. a *Octopus insularis*, pero el artículo original estudió *Octopus laqueus*: [Nature, 28-jun-2023](https://www.nature.com/articles/s41586-023-06203-4). No se reescribió el claim.

Identidad de variantes:
- `2026-11-05_inter-arboles-mito-respiran` es una variante/material separado; no sustituye al canónico de redes micorrícicas.
- `2026-11-07_extra-nubes-pesan` es material de origen, no un segundo proyecto; el canónico sigue siendo `2026-11-07_inter-nubes-pesan`.
- Las variantes de Venus, palomitas, ballena y pulpo en `cola/bloqueados/` no se contaron como proyectos canónicos adicionales.
- No hay copias de estos doce IDs en `cola/entrada/`; por tanto no hubo que mover copias heredadas.

## 4. Guardia de producción preexistente

La revisión de `proyectos/<id>/facebook.json`, `tiktok.json`, `data/horario_2026-11-08.json` a `2026-11-11.json` y `data/endscreens_rotacion.json` eleva el recuento de producción preexistente a **siete**, no cinco. El recuento anterior omitió Venus y Arena.

| Proyecto | Evidencia YouTube | TikTok | Facebook / discrepancia |
|---|---|---|---|
| Venus | Sin ID YT en los sidecars revisados | `7705488176793652481`, Everyone; 07-nov 17:00 | `2544385142727016`, Público; 07-nov 17:58 |
| Palomitas | `zTP5akrGA9M`, público | `7705593452003691794`, Everyone; 08-nov 07:00 | `1167496802382795`, Público; 08-nov 07:00 |
| Ballena | `wbFrlM2e_YE`, público; 11-nov 07:00 | `7705594333574991122`, Everyone; 11-nov 07:00 | `programado_lote_7nov`; sin URL capturada en la revisión |
| Aguacate | `nSS_q2tj2P0`, público; 10-nov 07:00 | `7705594217136966920`, Everyone; 10-nov 07:00 | `programado_lote_7nov`; sin URL capturada |
| Ranas | `UBFuKBU3cx0`, público; 09-nov 07:00 | `7705596671807245586`, Everyone; 09-nov 07:00 | `programado_lote_7nov`; sin URL capturada |
| Arena | `m4RqQRaz55k`, público; además `ztIkYcXB91U` sigue descrito como programado a las 19:00 | `7705502155427368212`, Everyone; 07-nov 13:30 | `2224920108452190`, Público; 07-nov 17:58 |
| Hielo caliente | `HSgrnejAcaI`, privado/programado para 11-nov 13:30 | `7706905447424347393`, Everyone/programado; 11-nov 13:30 | Programado, Público, UI “En proceso” |

Los siete quedan como `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`. No borrar ni cancelar nada. Arena tiene riesgo explícito de duplicado: un ID YT público y otro ID aún descrito como programado.

No hay `salidas/<project_id>/` con los medios de estos siete. Los sidecars contienen rutas de workspace y/o IDs de plataforma, pero el árbol GitHub no contiene los MP4 referenciados: **MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO**. No se afirma que esos MP4 existan en el repo.

No existe un archivo independiente `historial_youtube` en el árbol. Se revisaron los IDs disponibles en sidecars, horarios y rotación de endscreens; el riesgo de Arena queda registrado.

Los otros cinco del lote (árboles, rayo, huesos, pulpo y nubes) no muestran IDs/programaciones de plataforma ni salidas en esta rama.

## 5. Datos, rotación y registro editorial

Se leyeron todos los JSON de `data/` en la raíz. Fechas máximas relevantes:
- `temas_del_dia.json`: 2026-10-28.
- `estilos_usados.json`: 2026-10-28.
- `vistas_historico.json`: 2026-10-28.
- `rotacion.json`, `publicaciones.json`, `cola.json`: 2026-10-31.
- `tendencias_estilos.json`: 2026-10-31.
- `horarios.json`: actualizado 2026-11-09; solo contiene ventanas generales.
- Horarios diarios disponibles hasta 2026-11-11; no existe horario diario del 16-nov.
- `endscreens_rotacion.json`: actualizado 2026-11-16 14:32 CDMX; recoge IDs públicos/aplicados de endscreens.
- `horario_semana_2026-11-01_07.json`: usado para el lote obligatorio.

El estilo `collage_cientifico_vintage` del borrador del 16-nov existe en el catálogo y no repite los estilos de los storyboards del 13–15 nov (`dibujo_cientifico_scratchboard`, `papel_rasgado_capas`, `rubber_hose_1930s`, `van_gogh`). La estructura `paradoja_mecanica` tampoco repite las estructuras de esos días. La unicidad completa no puede certificarse con `data/estilos_usados.json` porque está detenido en 28-oct.

`scripts/registro_editorial.py`:
- Recorre storyboards de `proyectos/`, `cola/entrada/`, `cola/` y `salidas/`.
- No recorre `cola/bloqueados/`, `handoffs/grok_inbox/` ni los sidecars `facebook.json`/`tiktok.json`.
- Deriva fecha desde el `project_id`, no valida `fecha_objetivo` contra el horario.
- Por ello no incorpora de forma fiable los siete casos de producción preexistente.

`scripts/procesar_cola.py`:
- Por defecto usa la fecha actual CDMX.
- Acepta `--fecha`, que permite seleccionar fechas históricas manualmente.
- Filtra por prefijo de nombre de archivo/carpeta, no por `fecha_objetivo` dentro del storyboard.
- Acepta paquetes anidados, a diferencia del workflow.

Contradicciones detectadas:
- `templates/storyboard.template.json` es una plantilla antigua 16:9/120 s con `asset_filename`, `asset_type`, `voice_asset` y rutas de exportación. La plantilla vigente es `templates/storyboard_vertical.template.json` (9:16, 84 s, sin medios).
- `docs/RECETA_CAPSULA.md` exige expresar el silencio explícitamente; el ejemplo de `storyboard_vertical.template.json` muestra `sfx: []`. Esto explica parte de los 75 arrays vacíos y requiere unificar la instrucción.
- El workflow solo observa `cola/entrada/*.json` de primer nivel, mientras `procesar_cola.py` acepta `cola/entrada/*/storyboard.json`. Los cuatro paquetes históricos anidados no son despachables por el workflow actual.

## 6. Workflow y Actions

`.github/workflows/capcot-grok-dispatch.yml`:
- El trigger de push cubre solo `cola/entrada/*.json`.
- La búsqueda/selector manual opera en profundidad máxima 1.
- No cubre `proyectos/<id>/storyboard.json` ni `cola/entrada/<id>/storyboard.json`.
- El borrador del 16-nov y los cuatro paquetes históricos están `NOT_DISPATCHABLE` por su ruta.

En los últimos 100 registros de Actions no aparece una ejecución de `capcot-grok-dispatch`. La última ejecución sobre el HEAD observado de esta rama es CodeQL (#330), concluida con éxito; no es despacho. La última falla global visible corresponde a Semgrep en `main` (#184); el endpoint de logs devolvió contenido vacío, así que no hay error literal adicional que registrar. No se atribuye esa falla al workflow Grok.

No se comprobaron valores de secretos ni se modificó configuración. No se creó ningún marcador de handoff ni estado Grok.

## 7. Rama y alcance

La rama `main` contiene artefactos del 16-nov (HERA en cola y Sarampión en salidas) que no aparecen en `feature/capcot-video-discovery-continuity`. Se mantuvo el alcance solicitado: esta auditoría no los mezcló con el inventario de feature, no copió archivos ni hizo merge.

## 8. Resultado y límites

- Proyecto del día: QA narrativo PASS/91; contrato estático sin errores tras completar metadatos mecánicos; DOI permanece `PENDIENTE_RESOLVEDOR`.
- No promovido ni despachado: no hay selección Grok, no hay estado Grok, el path actual no es despachable y no se pudo ejecutar el validador Python real.
- Lote 5–7: 2 PASS narrativos, 10 FAIL; 0/12 aptos estructuralmente.
- Producción preexistente: 7 proyectos protegidos contra redispatch.
- Recepción Grok no confirmada para el proyecto del día, los doce del lote y los cuatro paquetes históricos consultados.

No había runtime local del repositorio para ejecutar `validar_storyboard.py`, `procesar_cola.py` o `registro_editorial.py`; la comprobación fue estática sobre los archivos de GitHub. No se revisaron APIs porque no se identificó un cambio oficial nuevo que lo justificara.
