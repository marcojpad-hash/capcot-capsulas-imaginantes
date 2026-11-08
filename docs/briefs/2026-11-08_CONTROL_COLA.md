# Auditor CAPCOT — control de cola
**Fecha de auditoría:** 2026-11-08, corte 15:31 CDMX  
**Repositorio:** `marcojpad-hash/capcot-capsulas-imaginantes`  
**Rama:** `feature/capcot-video-discovery-continuity`  
**Head antes de crear este reporte:** `eca5598674fcb3f65aec487620909d487b2eff65`  
**Alcance:** inventario ordinario del 8-nov + lote obligatorio 5–7 nov. Sin producción de medios, publicación, dispatch ni consumo de créditos.

## 1. Resultado ejecutivo

- **0** borradores con prefijo `2026-11-08` en `proyectos/`.
- **0** JSON de primer nivel de fecha 8-nov en `cola/entrada/`.
- Existe una carpeta anidada de un slot 23:30 del 7-nov; queda fuera de esta auditoría por la exclusión expresa de dato del día. No se leyó su storyboard ni su estado.
- El radar vigente `docs/briefs/2026-11-08_RADAR_CAPCOT.md` registra `NO_DUPLICAR`: el slot 07:00 ya está ocupado por una publicación de un proyecto previo y no asigna slots nuevos; la ventana 19:00 está retirada.
- **12** storyboards canónicos en `proyectos/` para 5–7 nov; los doce coinciden con `data/horario_semana_2026-11-01_07.json` en `project_id`, `fecha_objetivo`, `slot_local` y `slot_cesta`.
- QA narrativo independiente en frío, releído desde los JSON después de escribir: **2 PASS / 10 FAIL**. Los valores exactos son los que siguen en la tabla.
- **0/12** pasan la validación estructural completa. Los dos PASS narrativos no se promocionan.
- **0 promociones** a `cola/entrada/`; no había copias activas de estos doce paquetes que mover.
- **12/12** estados individuales de Grok devuelven HTTP 404: `RECEPCION_GROK_NO_CONFIRMADA`.
- Tres proyectos tienen evidencia de procesamiento/publicación preexistente (Venus, palomitas y arena): `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`.
- Se creó este reporte y se relee desde GitHub. No se modificó `data/*.json`, `main`, workflows, secretos, permisos, estados de Grok ni decisiones editoriales.

## 2. Inventario del 8 de noviembre

El árbol actual no contiene `proyectos/2026-11-08_*/storyboard.json`, `salidas/2026-11-08_*/` ni JSON de cola con fecha 8-nov. El brief diario existente es `docs/briefs/2026-11-08_RADAR_CAPCOT.md`; este CONTROL_COLA es el primer control de cola del día.

`data/horario_2026-11-08.json` tiene un slot 07:00 ya publicado para `2026-11-05_comida-palomitas`; no es un storyboard nuevo del 8-nov. No asigna 13:30, 17:00 ni 17:45 y la ventana 19:00 está retirada. La carpeta de cola anidada del slot 23:30 se deja intacta y sin revisión por la exclusión expresa.

## 3. Lote canónico 5–7 noviembre: fecha de creación, fecha objetivo y QA

Los doce storyboards se incorporaron a `proyectos/` en el mismo commit `7a415426f5907c2ab03687a47f3d160a595cb669`, el **2026-11-02 16:11:24 CDMX**. Esa es la fecha de creación del borrador; no es la fecha objetivo del slot. En esta auditoría solo se actualizó `narrative_qa.reviewed_at` a `2026-11-08T15:27:31-06:00`; no se cambió narración, claims, fuentes, tema ni decisión editorial. Los doce valores fueron releídos desde GitHub.

| Project ID | Fecha objetivo | Slot / cesta | QA narrativo | Checks falsos / critical flags |
|---|---|---|---|---|
| `2026-11-05_kids-dia-en-venus` | 05-nov | 07:00 / kids | **PASS 88** | Ninguno; 7 checks true, flags vacíos |
| `2026-11-05_comida-palomitas` | 05-nov | 13:30 / comida_familia | **FAIL 82** | apertura_in_medias_res, progresion_por_escena; apertura definicional y escena 6 repite causas |
| `2026-11-05_inter-arboles-se-comunican` | 05-nov | 17:00 / intermedio_1 | **FAIL 78** | apertura_in_medias_res; apertura genérica |
| `2026-11-05_inter-rayo-globular` | 05-nov | 17:45 / intermedio_2 | **FAIL 81** | apertura_in_medias_res; apertura histórica descriptiva |
| `2026-11-06_kids-ballena-azul-corazon` | 06-nov | 07:00 / kids | **FAIL 80** | payoff_cierre_apertura; el cierre sobreafirma «casi se detiene» |
| `2026-11-06_comida-aguacate-negro` | 06-nov | 13:30 / comida_familia | **FAIL 79** | progresion_por_escena, transiciones_causales; repetición de escenas 5–6 |
| `2026-11-06_inter-ranas-congeladas` | 06-nov | 17:00 / intermedio_1 | **FAIL 83** | progresion_por_escena, transiciones_causales; escenas 5–6 reiteran límites |
| `2026-11-06_inter-arena-cantante` | 06-nov | 17:45 / intermedio_2 | **PASS 94** | Ninguno; 7 checks true, flags vacíos |
| `2026-11-07_kids-huesos-bebe` | 07-nov | 07:00 / kids | **FAIL 82** | progresion_por_escena, transiciones_causales; escena 6 repite conteo y fusión |
| `2026-11-07_comida-hielo-caliente` | 07-nov | 13:30 / comida_familia | **FAIL 81** | apertura_in_medias_res; apertura basada en creencia, no en anomalía en curso |
| `2026-11-07_inter-pulpo-suenos` | 07-nov | 17:00 / intermedio_1 | **FAIL 80** | progresion_por_escena, transiciones_causales, payoff_cierre_apertura; escenas 5–6 reiteran el límite y payoff vago |
| `2026-11-07_inter-nubes-pesan` | 07-nov | 17:45 / intermedio_2 | **FAIL 78** | progresion_por_escena, transiciones_causales, payoff_cierre_apertura; escena 7 reitera cifra y límite sin pagar la suspensión |

Los siete checks guardados son `pregunta_central_reconstruible`, `apertura_in_medias_res`, `progresion_por_escena`, `transiciones_causales`, `giro_cientifico_explicado`, `limite_evidencia_explicito` y `payoff_cierre_apertura`. Todos los JSON contienen `review_basis="lectura_en_frio_solo_narracion"` y `reviewer_role="auditor_capcot_independiente"`. No se consultaron título, resumen, arco, notas ni `narrative_contract` durante la lectura narrativa.

**Identidad temática:** el canónico `2026-11-05_inter-arboles-se-comunican` sí trata redes micorrícicas comunes y Karst et al. 2023; no se marcó desajuste temático. `cola/bloqueados/2026-11-05_inter-arboles-mito-respiran/` es otra variante y no se confundió con el canónico. El slot 7-nov 17:45 corresponde solo a `2026-11-07_inter-nubes-pesan`; `extra-nubes-pesan` permanece como material de origen, no como proyecto.

## 4. Validación estructural estática

Los doce JSON cumplen varios parámetros básicos:
- 7–8 escenas por storyboard.
- 78 s de escenas + 6 s de cortinilla = **84 s totales**.
- Gancho `titulo` de 3–5 palabras.
- Arco completo con apertura, desarrollo, cierre y reflexión; cierre hablado exacto.
- Voz declarada correcta: edge-tts, `es-MX-JorgeNeural`, rate `+7%`, pitch `-2Hz`.
- `narrative_contract` y `narrative_qa` presentes.
- `visual_identity.prompt_base` coincide literalmente con `scripts/estilos.json`; los `image_prompt` comienzan con ese prompt.
- `source_ids` de escenas apuntan a fuentes existentes; los registros tienen ID, cita corta y URL. Se revisaron DOI/URL de forma estática; no se ejecutó Crossref ni un resolvedor en vivo.

Bloqueos estructurales:
- **510 campos narrativos ausentes**: las 85 escenas carecen de los seis campos obligatorios `dramatic_beat`, `scene_function`, `causal_bridge_from_previous`, `question_state`, `reason_to_continue` y `new_information`.
- El canónico de árboles tiene **169 palabras** según el conteo del validador, una por debajo del mínimo de 170; además carece de capa de mapa y de dato/gráfico.
- Los otros once storyboards tienen una capa de mapa y una capa de dato/gráfico con coordenadas/fuentes declaradas.
- En ranas, la capa de dato cita PubMed 23966588, pero esa referencia no está incorporada como fuente del JSON; el único `source_id` declarado corresponde al DOI 10.1242/jeb.181.1.245. No se alteró la cifra ni se añadió una fuente.
- Ambiente está declarado en 85/85 escenas. **75/85** tienen `sfx: []`; no se declara expresamente si esas escenas deben ser silenciosas.
- En los doce: `approved_assets=[]`, `export.render_status=NOT_GENERATED`, sin `asset_filename`, `asset_type`, `export.filename` ni rutas de medios en los storyboards de preproducción.

Resultado: **0/12 estructuralmente aptos**. Los dos PASS narrativos no pueden promocionarse; los otros diez tampoco superan QA narrativo.

## 5. Producción preexistente: no redispatchar

Se detectaron tres proyectos con evidencia de publicaciones en archivos de plataforma y/o registros de pantallas finales. Los tres se clasifican `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`. El campo `publicacion.status` del storyboard sigue en `PENDIENTE_DECISION_GROK`, por lo que existe discrepancia documental. No se corrigió ese campo ni se canceló nada.

| Proyecto | Evidencia de plataforma | Privacidad registrada | Discrepancia / riesgo |
|---|---|---|---|
| `2026-11-05_kids-dia-en-venus` | YT `phVfyHp3CnY` (54 vistas en `endscreens_rotacion`); TT `7705488176793652481`; FB Reel `2544385142727016` | TT Everyone; FB Public; privacidad YT no indicada en el registro consultado | Slot objetivo 05-nov 07:00; TT se registra público 07-nov 17:00 y FB 17:58. El storyboard sigue pendiente. |
| `2026-11-06_inter-arena-cantante` | YT público `m4RqQRaz55k` (33 vistas); TT `7705502155427368212`; FB Reel `2224920108452190` | TT Everyone; FB Public; privacidad YT no indicada | Slot objetivo 06-nov 17:45; TT registra 07-nov 13:30 y FB 17:58. Además, `ztIkYcXB91U` sigue descrito como YT programado a las 19:00: **riesgo de duplicado**; no borrar ni cancelar. |
| `2026-11-05_comida-palomitas` | YT `zTP5akrGA9M`; TT `7705593452003691794`; FB Reel `1167496802382795` | YT Public; TT Everyone; FB Público | Slot original 05-nov 13:30; publicado 08-nov 07:00. El commit de Grok Bot del 8-nov registra que ya estaba publicado y que no se subió nada. |

Los archivos de plataforma de los tres proyectos referencian MP4 en rutas `/workspace/...` fuera del árbol GitHub. Resultado para los tres: **MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO**. No existe `salidas/<project_id>/qa.json` para ellos; no se afirma QA audiovisual ni se usa un QA local como sustituto narrativo.

La auditoría anterior del 7-nov describía Venus y arena solo como versiones programadas; los archivos de plataforma ahora leídos muestran publicaciones efectivas en TT/FB y registros YT. Este control deja constancia de esa discrepancia sin reescribir el reporte anterior.

## 6. Cola, bloqueados y dispatchabilidad

- `cola/entrada/` no contiene JSON de primer nivel de estos doce proyectos.
- Los doce paquetes siguen en `proyectos/<project_id>/storyboard.json`: cada uno es **NOT_DISPATCHABLE** desde su ruta actual.
- `.github/workflows/capcot-grok-dispatch.yml` escucha `cola/entrada/*.json`; el selector de push filtra `^cola/entrada/[^/]+\.json$`. En `workflow_dispatch`, `all` usa `find cola/entrada -maxdepth 1 -type f -name '*.json'`; un ID individual resuelve `cola/entrada/<id>.json`. No recoge `proyectos/<id>/storyboard.json` ni `cola/entrada/<id>/storyboard.json`.
- `scripts/procesar_cola.py` sí contempla carpetas anidadas y por defecto usa la fecha CDMX actual, pero permite `--fecha`; por tanto, el filtro es por fecha solicitada, no una prohibición absoluta de procesar históricos.
- La carpeta anidada del slot 23:30 excluido tampoco coincide con el selector del workflow; no se inspeccionó su contenido.
- `handoffs/grok_inbox/` contiene solo README; no hay marcador de handoff. `handoffs/grok_done/` solo tiene `.gitkeep`.
- Los doce `cola/estado/<project_id>.json` devolvieron 404. Para cada uno: **RECEPCION_GROK_NO_CONFIRMADA**.
- `cola/bloqueados/` conserva copias heredadas planas y carpetas con slugs alternos. No hay copia activa de estos doce en `cola/entrada/`, así que no se movió nada. Se preservaron las variantes: `inter-arboles-mito-respiran` no es el canónico de redes micorrícicas; `extra-nubes-pesan` es material de origen; los slugs alternos de Venus, palomitas, ballena, Mpemba y pulpo no se fusionaron con los IDs canónicos. Los `ESTADO_EJECUCION.md` de las carpetas bloqueadas revisadas ya estaban en `BORRADOR_EN_PROYECTOS_NO_APTO_PARA_PROMOCION` o `MATERIAL_DE_ORIGEN_NO_ES_PROYECTO`; no hubo que cambiarlos.

## 7. Actions y configuración de handoff

- La última ejecución de `CAPCOT — entrega automática a Imaginantes` disponible es el run **41306776689**, 2026-11-01 06:29 CDMX, fallido.
- Log literal: `Falta configurar GROK_WEBHOOK_URL.` En ese run las variables asociadas a `GROK_WEBHOOK_URL` y `GROK_WEBHOOK_TOKEN` estaban vacías; no se muestran valores.
- La versión actual del workflow cambió: ahora escribe primero un marcador en `handoffs/grok_inbox/` y trata el webhook como opcional; sin ambos secretos válidos indica modo buzón gratuito. No existe ejecución posterior que pruebe ese flujo.
- Los runs del 8-nov corresponden a TTS tooling smoke check, no al dispatch CAPCOT. No hay un run de entrega el 8-nov.
- El flujo actual no exige webhook para escribir el buzón, pero requiere un JSON de primer nivel en `cola/entrada/`; hoy no existe uno elegible.
- No se disparó ningún workflow ni se envió payload externo.

## 8. Rotación, historial y documentos contradictorios

Se leyeron los 17 JSON existentes en `data/`. Los registros centrales están desfasados: `temas_del_dia.json` y `estilos_usados.json` llegan al 28-oct; `rotacion.json` y `publicaciones.json` al 31-oct. `endscreens_rotacion.json` sí está actualizado al 8-nov y contiene IDs, vistas y enlaces de pantalla final para palomitas, Venus y arena.

`scripts/registro_editorial.py` combina rotación, publicaciones, cola y storyboards de proyectos/cola/salidas, pero no lee `data/horario_2026-11-08.json`, `data/endscreens_rotacion.json`, `cola/bloqueados/` ni los JSON de plataforma dentro de cada proyecto. Por eso registra la fecha original del storyboard (p. ej. 05-nov para palomitas) y no su publicación efectiva el 08-nov; no certifica por sí solo la rotación real del día.

`data/horario_semana_2026-11-01_07.json` conserva 22 IDs en `yt_id_historial`, repartidos en diez slots del 1–3 nov. No hay evidencia de borrado en Studio para todos ellos. En el slot 1-nov 19:00, la nota pide borrar tres IDs (`i2l4BkMvHp0`, `9XflXdWDM0A`, `bICGA3kIBcU`), pero no hay confirmación de eliminación. Se marca **RIESGO_DUPLICADO_HISTORICO_NO_VERIFICADO**; no se intenta borrar ni cancelar.

La plantilla `templates/storyboard.template.json` es legado y contradice la receta vigente: 16:9, 120 s y campos de assets. La plantilla activa es `templates/storyboard_vertical.template.json` (9:16, 84 s, contrato narrativo y preproducción sin assets). Se registra la contradicción sin modificar plantillas.

## 9. Validación, APIs y límites

No había runtime local del repositorio. Se hizo revisión estática de `scripts/validar_storyboard.py`, `scripts/procesar_cola.py`, `scripts/rotacion.py` y `scripts/registro_editorial.py`; **no se ejecutaron** los helpers ni el validador. La revisión de DOI fue estática, sin consulta viva a Crossref. No se revisaron APIs porque no se identificó un cambio oficial nuevo que justificara esa revisión.

No se generaron imágenes, frames, voz, audio, video ni renders. No se publicaron ni programaron contenidos. No se consumieron créditos. No se modificaron `data/*.json`, `main`, workflows, secretos, permisos, estados de Grok ni decisiones editoriales. Los únicos cambios en los doce storyboards fueron las marcas `narrative_qa.reviewed_at` de esta lectura en frío independiente.

## 10. Decisión

- Lote 5–7: **2 PASS narrativos / 10 FAIL narrativos / 0 aptos estructuralmente**.
- Proyectos con producción/publicación previa: Venus, palomitas y arena; **no redispatchar**.
- Los otros nueve permanecen fuera de cola por QA narrativo y/o estructura; los dos PASS también permanecen fuera por estructura y, además, por procesamiento preexistente.
- Día 8-nov: sin borrador nuevo y sin slot nuevo autorizado.
- Recepción formal de Grok: **no confirmada** para los doce proyectos.

El lote permanece abierto. No hay paquete autorizado para handoff.
