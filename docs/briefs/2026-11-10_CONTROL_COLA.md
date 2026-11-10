# Auditor CAPCOT — control de cola y rotación

**Corte:** 2026-11-10 15:47:50 CDMX  
**Repositorio:** `marcojpad-hash/capcot-capsulas-imaginantes`  
**Rama auditada:** `feature/capcot-video-discovery-continuity`  
**Alcance:** proyectos del 10-nov + lote obligatorio 5–7 nov + comprobación de cola histórica necesaria para evaluar dispatchabilidad. Sin producción de cápsulas ni medios, sin publicación, sin dispatch ni consumo de créditos.

## 1. Resultado ejecutivo

- **10-nov:** 1 storyboard en `proyectos/`; 0 entradas de cola del 10-nov. El borrador `2026-11-10_comida-aprendizaje-sabor-nutriente` obtuvo **PASS narrativo 92** y revisión estructural estática sin bloqueos de esquema. No se promovió: el brief lo define como propuesta de una ventana de prueba 13:30, sin slot_cesta ni decisión editorial final, y escribir una entrada plana en cola activaría el workflow.
- **Lote 5–7 nov:** 12/12 IDs existen en `proyectos/`; 12/12 coinciden exactamente con el horario canónico en project_id, fecha_objetivo, slot_local y slot_cesta. QA en frío: **2 PASS / 10 FAIL**. Validación estructural: **0/12 aptos**.
- Se relevaron los 12 registros de `narrative_qa.reviewed_at` a este corte, sin cambiar narración, claims, fuentes ni decisión editorial. Se añadió el QA faltante al borrador del 10-nov. Los JSON fueron releídos desde GitHub después de escribir.
- Cinco de los doce proyectos del lote tienen evidencia externa de publicación/procesamiento: Venus, palomitas, arena, ranas y aguacate. Todos quedan **PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR**. En los cinco, el storyboard aún declara `publicacion.status=PENDIENTE_DECISION_GROK`.
- Los cinco tienen referencias de medios fuera del árbol GitHub o no verificables desde él: **MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO**. No existe QA audiovisual en `salidas/<project_id>/qa.json` para esos cinco.
- La carpeta de cola del robot ASTRA del 9-nov existe anidada, pero el workflow no la selecciona. Su marcador de handoff sigue en `pending`; `cola/estado/` devuelve 404 y `frames/` contiene solo `.gitkeep`. **RECEPCION_GROK_NO_CONFIRMADA**.
- No se modificó `data/*.json`, `main`, workflows, secretos, permisos, estados de Grok, publicaciones ni archivos de medios. No se movieron copias bloqueadas.

## 2. Briefs, creación y fecha objetivo

Se leyeron Plan Maestro, Receta, Guía de modelo externo, Flujo Externo, contrato de estado Grok, contrato operativo, plantillas, catálogo de estilos, scripts y todos los JSON directos de `data/`. También se contrastaron los briefs/control del 2, 5, 6, 7, 8, 9 y 10 de noviembre.

- Los doce borradores 5–7 se incorporaron a `proyectos/` en el commit `7a415426f5907c2ab03687a47f3d160a595cb669`, fechado **2026-11-02 16:11:24 CDMX**. Esa es su fecha de creación en Git; no es su fecha objetivo.
- El borrador del 10-nov se incorporó en el commit `29a79447241ec2116c5b9e59a3773e1feb8c0c26`, fechado **2026-11-10 09:12:24 CDMX**. El radar registra un corte de investigación 08:57; el commit del storyboard es posterior a ese corte.
- Los doce IDs 5–7 coinciden 12/12 con `data/horario_semana_2026-11-01_07.json`. Se conserva como fuente canónica el horario corregido: el segundo intermedio de 5–7 es **17:45**, no 19:00.
- Identidad temática preservada: `2026-11-05_inter-arboles-se-comunican` sí trata redes micorrícicas comunes y Karst et al. 2023. No se marcó desajuste temático. `inter-arboles-mito-respiran` es una variante distinta. El slot 2026-11-07 17:45 es exactamente `2026-11-07_inter-nubes-pesan`; `extra-nubes-pesan` es material de origen, no un segundo proyecto.

## 3. Inventario y QA narrativo del lote 5–7

La lectura en frío usó únicamente la narración concatenada. Se ocultaron título, resumen, arco, notas y narrative_contract. Los siete checks registrados en cada JSON son: `pregunta_central_reconstruible`, `apertura_in_medias_res`, `progresion_por_escena`, `transiciones_causales`, `giro_cientifico_explicado`, `limite_evidencia_explicito` y `payoff_cierre_apertura`. Todos quedaron con `review_basis="lectura_en_frio_solo_narracion"`, `reviewer_role="auditor_capcot_independiente"` y `reviewed_at="2026-11-10T15:47:50-06:00"`.

| Project ID | Slot / cesta | Escenas / palabras | narrative_qa | Resultado estructural |
|---|---|---:|---|---|
| `2026-11-05_kids-dia-en-venus` | 07:00 / kids | 7 / 170 | **PASS 88** | FAIL: faltan seis campos narrativos por escena |
| `2026-11-05_comida-palomitas` | 13:30 / comida_familia | 7 / 173 | **FAIL 82** | FAIL: faltan seis campos narrativos por escena |
| `2026-11-05_inter-arboles-se-comunican` | 17:00 / intermedio_1 | 8 / 169 | **FAIL 78** | FAIL: faltan seis campos; 169 palabras; sin mapa ni dato/gráfico |
| `2026-11-05_inter-rayo-globular` | 17:45 / intermedio_2 | 7 / 197 | **FAIL 81** | FAIL: faltan seis campos narrativos por escena |
| `2026-11-06_kids-ballena-azul-corazon` | 07:00 / kids | 7 / 174 | **FAIL 80** | FAIL: faltan seis campos narrativos por escena |
| `2026-11-06_comida-aguacate-negro` | 13:30 / comida_familia | 7 / 170 | **FAIL 79** | FAIL: faltan seis campos narrativos por escena |
| `2026-11-06_inter-ranas-congeladas` | 17:00 / intermedio_1 | 7 / 177 | **FAIL 83** | FAIL: faltan seis campos narrativos por escena |
| `2026-11-06_inter-arena-cantante` | 17:45 / intermedio_2 | 7 / 206 | **PASS 94** | FAIL: faltan seis campos narrativos por escena |
| `2026-11-07_kids-huesos-bebe` | 07:00 / kids | 7 / 172 | **FAIL 82** | FAIL: faltan seis campos narrativos por escena |
| `2026-11-07_comida-hielo-caliente` | 13:30 / comida_familia | 7 / 172 | **FAIL 81** | FAIL: faltan seis campos narrativos por escena |
| `2026-11-07_inter-pulpo-suenos` | 17:00 / intermedio_1 | 7 / 170 | **FAIL 80** | FAIL: faltan seis campos narrativos por escena |
| `2026-11-07_inter-nubes-pesan` | 17:45 / intermedio_2 | 7 / 221 | **FAIL 78** | FAIL: faltan seis campos narrativos por escena |

Checks falsos y flags, tal como quedaron releídos en los JSON:

- **Palomitas 82:** `apertura_in_medias_res`, `progresion_por_escena`; `APERTURA_DEFINICIONAL_NO_IN_MEDIAS_RES`, `ESCENA_6_REITERA_CAUSAS_DE_GRANOS_NO_REVENTADOS_SIN_INFORMACION_NUEVA`.
- **Árboles 78:** `apertura_in_medias_res`; `APERTURA_GENERICA_NO_IN_MEDIAS_RES`.
- **Rayo 81:** `apertura_in_medias_res`; `APERTURA_HISTORICA_DESCRIPTIVA_NO_IN_MEDIAS_RES`.
- **Ballena 80:** `payoff_cierre_apertura`; `PAYOFF_SOBREAFIRMA_CASI_SE_DETIENE`.
- **Aguacate 79:** `progresion_por_escena`, `transiciones_causales`; `REPETICION_ESCENAS_5_6_SIN_AVANCE_CAUSAL`.
- **Ranas 83:** `progresion_por_escena`, `transiciones_causales`; `REPETICION_ESCENAS_5_6_LIMITES_DE_ESPECIE_Y_CONDICIONES`.
- **Huesos 82:** `progresion_por_escena`, `transiciones_causales`; `ESCENA_6_REPITE_VARIACION_DE_CONTEO_Y_FUSION`.
- **Hielo caliente 81:** `apertura_in_medias_res`; `APERTURA_DE_CREENCIAS_NO_IN_MEDIAS_RES`.
- **Pulpo 80:** `progresion_por_escena`, `transiciones_causales`, `payoff_cierre_apertura`; `REPETICION_ESCENAS_5_6_Y_PAYOFF_VAGO`.
- **Nubes 78:** `progresion_por_escena`, `transiciones_causales`, `payoff_cierre_apertura`; `ESCENA_7_REITERA_CIFRA_Y_LIMITE_SIN_PAYOFF_DE_SUSPENSION`.
- Venus 88 y arena 94: siete checks true y `critical_flags=[]`.

## 4. Validación estructural estática

No había runtime local del repositorio. Se inspeccionó `scripts/validar_storyboard.py` y se hizo revisión estática de los JSON; **no se ejecutó el validador Python ni los helpers**.

En los doce storyboards 5–7:
- 7–8 escenas; 78 s de escenas + cortinilla de 6 s = **84 s**.
- Gancho de 3–5 palabras, arco completo y cierre hablado; voz declarada `edge-tts / es-MX-JorgeNeural / +7% / -2Hz`.
- `narrative_contract` y `narrative_qa` presentes.
- `visual_identity.prompt_base` coincide con el catálogo y los prompts de escena empiezan con ese prompt_base.
- `source_ids` apuntan a IDs existentes; fuentes con ID, cita corta y URL. DOI/URL se revisaron estáticamente, sin Crossref ni resolvedor vivo.
- Ambiente está presente en 85/85 escenas. **75/85** tienen `sfx: []`; el silencio no queda declarado como intención.
- Once proyectos tienen mapa y capa de dato/gráfico con fuente declarada. Árboles carece de ambas.
- Las 85 escenas carecen de los seis campos exigidos por el validador: `dramatic_beat`, `scene_function`, `causal_bridge_from_previous`, `question_state`, `reason_to_continue` y `new_information`. Son **510 campos ausentes**. No se rellenaron porque hacerlo requeriría decisiones narrativas/editoriales.
- En ranas, la capa de dato cita PubMed 23966588, pero esa referencia no está incorporada en `sources[]`; el source_id declarado apunta al DOI 10.1242/jeb.181.1.245. No se alteró cifra ni fuente.
- En los doce: `approved_assets=[]`, `export.render_status=NOT_GENERATED`, sin `asset_filename`, `asset_type`, `export.filename` ni rutas de medios.

**Resultado: 0/12 estructuralmente aptos.** Los dos PASS narrativos tampoco pueden promocionarse. No había copias activas de estos doce en `cola/entrada/`; las copias heredadas permanecen en `cola/bloqueados/` y no se movieron.

## 5. Producción y publicación preexistente: no redispatchar

La evidencia actual amplía de tres a cinco los proyectos del lote con publicación/procesamiento previo. Los IDs de plataforma, horarios y privacidad disponibles son:

| Proyecto | Evidencia | Hora efectiva / privacidad | Estado y discrepancia |
|---|---|---|---|
| `2026-11-05_kids-dia-en-venus` | YT `phVfyHp3CnY` (54 vistas); TT `7705488176793652481`; FB `2544385142727016` | TT 07-nov 17:00; FB 17:58. TT Everyone; FB Public; privacidad YT no indicada | Publicación acreditada en el control del 8-nov y en endscreens. El storyboard sigue PENDIENTE_DECISION_GROK. |
| `2026-11-05_comida-palomitas` | YT `zTP5akrGA9M` (136 vistas); TT `7705593452003691794`; FB `1167496802382795` | 08-nov 07:00. YT Public; TT Everyone; FB Public | Publicado. Título de plataforma distinto al título del borrador; storyboard sigue PENDIENTE_DECISION_GROK. |
| `2026-11-06_inter-arena-cantante` | YT `m4RqQRaz55k` (33 vistas); TT `7705502155427368212`; FB `2224920108452190` | TT 07-nov 13:30; FB 17:58. TT Everyone; FB Public; privacidad YT no indicada | Publicación acreditada en endscreens. El control del 8-nov reporta además `ztIkYcXB91U` como YT programado a las 19:00; no aparece en los JSON actuales consultados ni hay confirmación de cancelación: riesgo histórico no resuelto. |
| `2026-11-06_inter-ranas-congeladas` | YT `UBFuKBU3cx0` (46 vistas); TT `7705596671807245586`; FB `scheduled_lote_7nov` | 09-nov 07:00. YT Public; TT Everyone; FB programado | Publicación YT/TT acreditada; Facebook sigue programado. El título publicado difiere del título del borrador; storyboard sigue PENDIENTE_DECISION_GROK. |
| `2026-11-06_comida-aguacate-negro` | YT `nSS_q2tj2P0` (30 vistas); TT `7705594217136966920`; FB `scheduled_lote_7nov` | 10-nov 07:00. YT Public; TT Everyone; FB programado | Publicación YT/TT acreditada; Facebook sigue programado. El título publicado, «El hueso no salva tu guacamole», cambia el ángulo respecto del storyboard sobre pardeamiento; storyboard sigue PENDIENTE_DECISION_GROK. |

Para los cinco: **PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR**. No existe `salidas/<project_id>/` con `qa.json` en el árbol actual; no se afirma QA audiovisual. Los registros de plataforma apuntan a medios fuera del repositorio o no verificables desde GitHub: **MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO**. No se borró, canceló ni reprogramó nada.

## 6. Inventario de cola, handoff y dispatchabilidad

- `cola/entrada/` no contiene JSON de primer nivel y no contiene carpeta de proyecto del 10-nov.
- Los doce proyectos 5–7 y el borrador del 10-nov permanecen en `proyectos/<id>/storyboard.json`: todos **NOT_DISPATCHABLE** desde esa ruta.
- El árbol de cola contiene dos carpetas históricas anidadas: el slot 23:30 del 7-nov (excluido expresamente del QA de este lote) y `2026-11-09_dato-robot-ensambla-orbita`.
- El paquete ASTRA del 9-nov existe en `proyectos/` y `cola/entrada/` con el mismo blob SHA `fac47f592abdb6f6ea129bd242095da287a53595`. El JSON registra 9 escenas, 210 palabras, 82 s + 6 s = 88 s, narrative_qa PASS 90, `approved_assets=[]`, `export.render_status=NOT_GENERATED` y sin rutas de assets. No se releyó su narrativa en este lote.
- La carpeta `frames/` de ASTRA contiene solo `.gitkeep`: **0 PNG**. `cola/estado/2026-11-09_dato-robot-ensambla-orbita.json` devuelve 404: **RECEPCION_GROK_NO_CONFIRMADA**.
- El marcador `handoffs/grok_inbox/2026-11-09_dato-robot-ensambla-orbita.json` tiene `status=pending` y referencia rama `main`/commit `7ea62b5e...`; no es acuse de Grok ni confirma generación de frames. El paquete de la rama auditada está en un commit distinto.
- `.github/workflows/capcot-grok-dispatch.yml` escucha `cola/entrada/*.json`; el dispatch manual por ID resuelve `cola/entrada/<id>.json`, y `all` usa `find ... -maxdepth 1`. Ninguno recoge `cola/entrada/<id>/storyboard.json`. ASTRA y la carpeta histórica anidada son **NOT_DISPATCHABLE** por ruta.
- `scripts/procesar_cola.py` sí recorre JSON directos y `*/storyboard.json`; por defecto filtra la fecha CDMX actual, pero admite `--fecha` para otra fecha y deriva la fecha del prefijo de ruta, no de `fecha_objetivo`. El procesador y el workflow no comparten la misma profundidad de búsqueda.
- El workflow actual trata el webhook como opcional y puede dejar un marcador pendiente sin entrega externa. Las últimas cinco ejecuciones disponibles de este workflow son runs 143–147 del **1-nov 06:29 CDMX**, todas fallidas. El log literal es `##[error]Falta configurar GROK_WEBHOOK_URL.`; el guard antiguo también nombraba `GROK_WEBHOOK_TOKEN`, pero el fallo registrado se detiene primero en URL. No hay ejecución posterior que pruebe el flujo nuevo.
- Los archivos `cola/estado/<project_id>.json` de los doce IDs, el borrador del 10-nov y ASTRA devolvieron 404. Para cada uno: **RECEPCION_GROK_NO_CONFIRMADA**. No se crearon ni modificaron estados.

## 7. Rotación, publicaciones e IDs históricos

- `data/temas_del_dia.json` y `data/estilos_usados.json` llegan al 28-oct; `data/rotacion.json` y `data/publicaciones.json` al 31-oct; `data/cola.json` solo contiene el registro fallido del 31-oct; `data/vistas_historico.json` llega al 28-oct. `data/endscreens_rotacion.json` sí está actualizado al 10-nov 10:49 e incluye vistas y cambios de pantalla final para los cinco IDs publicados.
- `scripts/registro_editorial.py` combina esos registros con storyboards de proyectos/cola/salidas, pero no lee `data/horario_2026-11-08.json`, `data/horario_2026-11-09.json`, `data/horario_2026-11-10.json`, `data/endscreens_rotacion.json`, `cola/bloqueados/` ni los JSON de plataforma externos. Por eso registra la fecha objetivo del storyboard, no la publicación real posterior. La rotación diaria puede no ver los cinco lanzamientos efectivos del 7–10 nov.
- `data/horario_semana_2026-11-01_07.json` conserva **22 IDs** en `yt_id_historial` distribuidos en diez slots. En el slot de `2026-11-03_kids-tiburon-groenlandia`, el ID actual es `0x1B9_rMm-I` y siguen listados `i2l4BkMvHp0`, `9XflXdWDM0A` y `bICGA3kIBcU` como históricos. No hay confirmación de borrado: **RIESGO_DUPLICADO_HISTORICO_NO_VERIFICADO**. No se intenta borrar ni cancelar.
- `ztIkYcXB91U` aparece como programado a las 19:00 en el control del 8-nov, pero no lo encontré en los JSON actuales de horario/endscreens. Se conserva como referencia histórica no resuelta, no como programación activa confirmada.
- La política vigente del horario retira 19:00 después del 4-nov y fija intermedio_2 de 5–7 a 17:45. Los encabezados antiguos de los RADAR 5–7 que todavía dicen 19:00 contradicen esa corrección; prevalece el horario semanal.

## 8. Documentos contradictorios y discrepancias

- Los RADAR 5, 6 y 7-nov conservan encabezados/fragmentos antiguos que hablan de 19:00 o de paquetes en cola; los controles posteriores y el horario semanal fijan 17:45 y los doce borradores en `proyectos/`.
- El CONTROL del 9-nov decía que el paquete ASTRA no estaba en la rama auditada; el árbol actual y el RADAR del 10-nov muestran ahora el paquete anidado en `proyectos/` y `cola/entrada/`, con marcador pending.
- El CONTROL del 8-nov documentaba tres publicaciones preexistentes (Venus, palomitas, arena); los horarios del 9 y 10-nov añaden ranas y aguacate. El total comprobable ahora es cinco.
- Los storyboards de esos cinco siguen con `publicacion.status=PENDIENTE_DECISION_GROK`, aunque hay IDs de plataforma. No se corrigió ese campo para no alterar decisiones editoriales.
- `templates/storyboard.template.json` es legado (16:9, 120 s y campos de assets) y contradice la receta/plantilla activa `templates/storyboard_vertical.template.json` (9:16, 84 s, contrato narrativo y preproducción sin assets). No se modificaron plantillas.
- El RADAR del 10-nov describe una ventana de prueba 13:30; `data/horario_2026-11-10.json` no contiene ese slot. El borrador 10-nov no tiene `slot_cesta`, no está seleccionado ni programado.

## 9. Cambios realizados y límites

- Se actualizaron únicamente los doce objetos `narrative_qa` del lote 5–7 con fecha de lectura 10-nov, conservando sus scores/statuses y checks revalidados.
- Se añadió `narrative_qa` al storyboard 10-nov: **PASS 92**, siete checks true, `critical_flags=[]`. Lectura en frío de narración únicamente.
- El storyboard 10-nov: 8 escenas, 192 palabras, 78 s + cortinilla 6 s = 84 s; gancho de 4 palabras; voz declarada correcta; 4 fuentes, source_ids válidos, mapa y dato/gráfico; prompt_base coincide con catálogo; ambiente y SFX presentes en 8/8 escenas; `approved_assets=[]`; `export.render_status=NOT_GENERATED`; sin `asset_filename`, `asset_type` ni rutas de medios. Su DOI `10.1038/s41586-026-11229-5` existe en el JSON, pero `verification_status=PENDIENTE`; no se resolvió en vivo.
- No se ejecutó el validador Python ni helpers por falta de runtime local; esta auditoría es estática. No se revisaron APIs porque no apareció un cambio oficial nuevo que justificara esa revisión.
- No se reescribió narración ni claims; no se rellenaron los seis campos ausentes; no se movieron bloqueados; no se promovió nada a cola; no se dispararon workflows ni webhooks; no se generaron medios ni se publicaron contenidos.

## 10. Decisión de auditoría

- **Lote 5–7:** 2 PASS narrativos / 10 FAIL narrativos / 0 estructuralmente aptos. Cinco proyectos con procesamiento/publicación preexistente: no redispatchar. Los otros siete permanecen fuera de cola.
- **10-nov:** 1 borrador, PASS narrativo 92 y revisión estructural estática favorable, pero sigue como propuesta sin slot oficial ni decisión editorial; no se promueve.
- **ASTRA 9-nov:** QA PASS 90 ya registrado, estructura estática compatible, pero handoff no confirmado, frames 0/9 y ruta no dispatchable.
- **Cola del 10-nov:** 0 entradas.
- El lote 5–7 permanece abierto hasta que se resuelvan los bloqueos estructurales; no se generaron ni se dejaron nuevas entradas de cola.
