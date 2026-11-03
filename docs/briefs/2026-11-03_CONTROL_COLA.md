# CONTROL COLA — 2026-11-03

**Repositorio:** `marcojpad-hash/capcot-capsulas-imaginantes`  
**Rama:** `feature/capcot-video-discovery-continuity`  
**Corte:** 2026-11-03, 15:07 CDMX  
**Rol:** auditoría; sin producción de medios, publicación ni dispatch.

## 1. Resultado ejecutivo

- Se localizaron y auditaron los **12 borradores** del lote 5–7 de noviembre.
- QA narrativo en frío: **3 PASS / 9 FAIL**. Los scores y estados de la tabla se releyeron de los JSON de GitHub después de registrarlos.
- **0 promociones** a `cola/entrada/<project_id>.json`: los 12 fallan el validador estructural por ausencia de los seis campos narrativos obligatorios en cada escena. Los tres PASS narrativos tampoco superan esa compuerta.
- Los 12 están **NOT_DISPATCHABLE** desde su ubicación actual en `proyectos/`.
- Para los 12 falta `cola/estado/<project_id>.json`: estado exacto **RECEPCION_GROK_NO_CONFIRMADA**. No se creó ni modificó ningún estado de Grok.
- La única entrada de cola del 3 de noviembre era un paquete rechazado de enzimas en una carpeta anidada. Se conservó íntegro en `cola/bloqueados/` y se retiró de la cola activa después de verificar las cuatro copias.
- No se generaron imágenes, frames, voz, audio, video ni renders. No se publicaron contenidos ni se consumieron créditos.

## 2. Briefs y horario 5–7 nov

Confirmados:
- `docs/briefs/2026-11-05_RADAR_CAPCOT.md`
- `docs/briefs/2026-11-06_RADAR_CAPCOT.md`
- `docs/briefs/2026-11-07_RADAR_CAPCOT.md`
- `docs/briefs/2026-11-02_CONTROL_COLA_5-7nov.md`

Los doce `project_id`, `fecha_objetivo`, `slot_local` y `slot_cesta` de `proyectos/` coinciden con `data/horario_semana_2026-11-01_07.json`. Los temas y títulos corresponden al slot asignado.

**Contradicciones de horario:**
- Los tres briefs RADAR todavía describen el segundo slot intermedio como **19:00**.
- El horario semanal, `data/horarios.json` y el control del 2 de noviembre fijan ese slot en **17:45**; 19:00 está retirado para este lote.
- `docs/PLAN_MAESTRO_AUTOMATICO.md`, `docs/FLUJO_EXTERNO.md` y `scripts/rotacion.py` conservan cinco ventanas antiguas, incluida 19:00. El código todavía define ventanas 16:00–18:00 y 18:00–21:00, por lo que 17:00 y 17:45 caen en la misma ventana del código.
- Los doce registros del horario siguen con `estado: pedir_chatgpt` aunque ya existe `proyectos/<id>/storyboard.json`. El control del 2 de noviembre indica que deben quedar en proyectos esperando PASS del auditor. No se modificó `data/*.json`.

## 3. QA narrativo en frío del lote

Se ocultaron título, resumen, arco, notas y `narrative_contract`; la lectura se hizo sobre la narración concatenada. Cada JSON recibió `narrative_qa` con siete checks, `review_basis: lectura_en_frio_solo_narracion`, `reviewer_role: auditor_capcot_independiente` y `critical_flags`.

| ID | QA releído | Score | Hallazgo narrativo |
|---|---:|---:|---|
| `2026-11-05_kids-dia-en-venus` | PASS | 88 | La anomalía día sideral/año organiza el relato y el cierre la paga. |
| `2026-11-05_comida-palomitas` | FAIL | 82 | Apertura definicional; el proceso aparece después. |
| `2026-11-05_inter-arboles-se-comunican` | FAIL | 78 | Apertura genérica, sin acción ni anomalía concreta en curso. |
| `2026-11-05_inter-rayo-globular` | FAIL | 81 | Apertura histórica descriptiva; el caso instrumental llega en la segunda escena. |
| `2026-11-06_kids-ballena-azul-corazon` | FAIL | 80 | El cierre sobreafirma que el corazón «casi se detiene» al resumir 2 latidos/min. |
| `2026-11-06_comida-aguacate-negro` | FAIL | 79 | Las escenas 5–6 reiteran mecanismo y límite sin avance suficiente. |
| `2026-11-06_inter-ranas-congeladas` | FAIL | 83 | Las escenas 5–6 repiten la limitación de especie y condiciones. |
| `2026-11-06_inter-arena-cantante` | PASS | 94 | La avalancha abre en acción; mecanismo, medición y condiciones progresan causalmente. |
| `2026-11-07_kids-huesos-bebe` | FAIL | 82 | La escena 6 repite el matiz de conteo y fusión ya expuesto en la 5. |
| `2026-11-07_comida-hielo-caliente` | FAIL | 81 | Abre con la formulación general de una creencia, no con el fenómeno en curso. |
| `2026-11-07_inter-pulpo-suenos` | FAIL | 80 | Repite límites en escenas 5–6 y cierra con payoff vago/pregunta especulativa. |
| `2026-11-07_inter-nubes-pesan` | PASS | 91 | El contraste masa/flotación conduce al cálculo acotado y al mecanismo de suspensión. |

Los tres PASS tienen los siete checks en true y `critical_flags=[]`. En los nueve FAIL hay al menos un check false y una bandera crítica. No se reescribieron narraciones ni claims.

### Identidad del tema de árboles

El borrador canónico actual `2026-11-05_inter-arboles-se-comunican` trata la **red micorrícica común / wood-wide web**, que sí corresponde al horario. La versión de respiración nocturna está en `cola/bloqueados/2026-11-05_inter-arboles-mito-respiran`, con otro ID y fuera de cola. Por tanto, la instrucción anterior sobre el tema equivocado corresponde a esa variante bloqueada, no al storyboard canónico actual. El actual recibe FAIL narrativo por apertura genérica, no por desajuste temático.

### Estructura y medios de preproducción

Comprobaciones estáticas de los doce:
- 7 escenas en once proyectos; 8 en árboles.
- 170–235 palabras en once; árboles tiene **169**.
- 84 s totales: 78 s de escenas + cortinilla de 6 s. Objetivo dentro de 75–90 s.
- Títulos/gancho dentro de seis palabras; voz `edge-tts / es-MX-JorgeNeural`, `+7%`, `-2Hz`.
- `narrative_contract` tiene los seis campos no vacíos en los doce.
- `sources` incluye `cita_corta` y URL; los `source_ids` de escenas resuelven a fuentes declaradas. Hay fuentes institucionales sin DOI, con URL. No se ejecutó resolución externa de DOI.
- Ambiente y SFX están presentes en todas las escenas.
- Mapa y dato/gráfico aparecen en once. Árboles carece de ambas capas.
- Once estilos coinciden con el `prompt_base` del catálogo. Árboles no coincide: su `visual_identity.prompt_base` y sus `image_prompt` no usan el prefijo literal del catálogo.
- En ranas, la capa de dato añade `−16 °C` y cita PubMed 23966588, pero esa fuente no está en `sources` y la cifra no aparece en la narración. No se añadió ni se retiró evidencia.
- En los doce: `approved_assets=[]`, `export.render_status=NOT_GENERATED`, sin `asset_filename`, `asset_type` ni rutas de medios.

**Bloqueo estructural común:** cada escena de los doce carece de `dramatic_beat`, `scene_function`, `causal_bridge_from_previous`, `question_state`, `reason_to_continue` y `new_information`. El validador exige esos campos. Árboles suma además 169 palabras, ausencia de mapa/gráfico y desajuste de prompt_base. Ranas conserva el desajuste de fuente en su capa de dato. No se completaron esos campos porque requerirían redactar funciones o puentes narrativos y podrían alterar la decisión editorial.

## 4. Handoff y dispatchabilidad

Para cada uno de los doce IDs:
- Ubicación actual: `proyectos/<project_id>/storyboard.json`.
- Resultado: **NOT_DISPATCHABLE**. Esa ruta no coincide con `.github/workflows/capcot-grok-dispatch.yml`.
- No existe `cola/entrada/<project_id>.json` ni una carpeta activa de entrada para esos IDs.
- No existe `cola/estado/<project_id>.json`: **RECEPCION_GROK_NO_CONFIRMADA**.
- No existe `salidas/<project_id>/`, ID de YouTube ni programación en plataformas. No hay procesamiento previo para los doce.

El workflow escucha `cola/entrada/*.json` y su selector manual busca archivos JSON a profundidad máxima 1. No encuentra `proyectos/<id>/storyboard.json`, `cola/bloqueados/` ni paquetes anidados. La carpeta anidada de enzimas tampoco era dispatchable por este workflow.

### Procesador y registro editorial

- `scripts/procesar_cola.py` usa por defecto la fecha actual de CDMX, pero acepta `--fecha` arbitraria. Selecciona por prefijo del nombre de archivo/carpeta, no compara ese prefijo con `fecha_objetivo` dentro del JSON. Por tanto, el comportamiento por defecto evita colas históricas, pero no es una barrera estricta contra una ejecución con fecha forzada o un paquete mal fechado.
- El procesador sí busca `cola/entrada/*/storyboard.json`; por eso podía tomar la carpeta anidada de enzimas aunque el workflow no la despachara.
- `scripts/registro_editorial.py` recoge proyectos, entrada, cola y salidas con búsqueda de un nivel; no incluye `cola/bloqueados`, `cola/estado`, handoffs ni el horario semanal. No es un inventario completo de variantes bloqueadas ni de recepción Grok.
- El registro histórico `data/cola.json` conserva el fallo del 31 de octubre de pardelas; es histórico y no una entrada del día 3.

## 5. Cola del 3 de noviembre

Se encontró un solo paquete lógico en `cola/entrada/2026-11-03_enzimas-incrustadas-oceano/`, con dos archivos JSON de storyboard idénticos (mismo blob SHA), `fuentes.md` y `HYPERFRAMES.md`.

- No tiene slot en `data/horario_semana_2026-11-01_07.json`.
- `HYPERFRAMES.md` registra rechazo de Mj y QA de Imaginantes **FAIL ENGANCHE**; no se atribuye ese QA a Grok.
- Usa esquema alternativo `escenas/fuentes`, carece de `narrative_contract` y `narrative_qa`; las escenas llevan el DOI como `source_id` en lugar de IDs `SRC-001`/ `SRC-002`.
- `export.render_status=NOT_GENERATED`; no hay medios. Su ubicación anidada no era dispatchable por workflow, aunque el procesador sí la habría seleccionado por prefijo de fecha.
- Se copiaron los cuatro archivos a `cola/bloqueados/2026-11-03_enzimas-incrustadas-oceano/`, se verificó igualdad byte a byte y solo entonces se retiraron los originales. `cola/entrada/` quedó únicamente con `.gitkeep`.
- No hay `cola/estado/2026-11-03_enzimas-incrustadas-oceano.json`: **RECEPCION_GROK_NO_CONFIRMADA**.

## 6. Producción preexistente del 3 de noviembre

Estos registros ya existían; no se redispatcharon, cancelaron ni modificaron en plataformas.

| Proyecto | YouTube / privacidad / hora CDMX | QA audiovisual y discrepancias |
|---|---|---|
| `2026-11-03_comida-maillard` | `JOA1Bm6KYDs`, private, 13:30 | Sin `qa.json`; storyboard 236 palabras; `export.render_status=NOT_GENERATED`; publicación dice uploaded/programado, pero no hay MP4 en el árbol. Metadata marca `contenido_sintetico=false` y publicación `containsSyntheticMedia=true`. TikTok/Facebook figuran programados 13:30. |
| `2026-10-29_juno-choque-proa` | `bpeRL5XtYLI`, private, 17:00 | QA local mide **91.84 s**, fuera de 75–90; storyboard 239 palabras. TikTok/Facebook v4 aparecen programados. Los IDs antiguos `73cZz8Pi9TE` y `3IiUmsRb30Y` siguen descritos como programados para la misma hora. |
| `2026-10-31_smartpe-edicion-plantas` | `-WBW0X9KpLM`, private, 19:00 | QA local mide **86.63 s**, dentro de 75–90, pero `capa_mapa=false` y `capa_grafico_o_dato=false`. TikTok/Facebook v4 aparecen programados. Los IDs antiguos `MXsNOywNzcg` y `aOcqxbBhQ0E` siguen descritos como programados para la misma hora. |

Los IDs antiguos de Juno y SmartPE permanecen en `historial_youtube` con el texto `SIGUE PROGRAMADO`; representan riesgo de duplicado. Sus entradas históricas no especifican privacidad; los IDs actuales están registrados como privados. No se intentó borrarlos en Studio.

Los tres directorios de salida referencian `capsula.mp4` o `capsula_v4.mp4`, pero esos archivos no están en el árbol GitHub: **MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO**. Los QA locales no sustituyen la compuerta editorial de 75–90 s ni el QA narrativo independiente. Los estados de Maillard en sus dos `ESTADO_EJECUCION.md` se cambiaron a `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`; no se alteraron sus registros de publicación.

## 7. Variantes bloqueadas y estados documentales

- Las variantes antiguas de palomitas, Venus, árboles/respiración, aguacate, ballena, ranas, Mpemba, pulpo y huesos permanecen en `cola/bloqueados/`.
- Sus nueve `ESTADO_EJECUCION.md` que aún decían `PREPARADO_PENDIENTE_REVISION_GROK` se corrigieron a `BORRADOR_EN_PROYECTOS_NO_APTO_PARA_PROMOCION`.
- La variante `2026-11-07_extra-nubes-pesan` no se contó como proyecto adicional; su estado documental quedó como `MATERIAL_DE_ORIGEN_NO_ES_PROYECTO`.
- La variante de árboles sobre respiración nocturna sigue bloqueada y no sustituye al storyboard canónico micorrícico.
- No se descartó ningún archivo bloqueado.

## 8. Actions, Grok y datos

- Última ejecución accesible de Actions: **41306776689**, 2026-11-01 12:29:58Z, `failure`. Log literal: `Falta configurar GROK_WEBHOOK_URL.`
- No hay ejecuciones posteriores al 1 de noviembre, aunque el workflow actual ya trata `GROK_WEBHOOK_URL` y `GROK_WEBHOOK_TOKEN` como opcionales y contempla buzón del repositorio. No se muestran ni registran valores de secretos.
- `handoffs/grok_inbox/` contiene solo README; `handoffs/grok_done/` solo `.gitkeep`. No hay marcador de handoff ni archivo de estado de Grok.
- `data/temas_del_dia.json` y `data/estilos_usados.json` llegan hasta el 28 de octubre; `data/rotacion.json` y `data/publicaciones.json` hasta el 31 de octubre; `data/vistas_historico.json` hasta el 28 de octubre; `data/balances_6h.json` hasta el 28 de octubre; los cierres diarios disponibles llegan al 27 de octubre. `data/reprogramacion_tt_fb_v4_2026-11-01_03.json` cubre 1–3 de noviembre y `data/endscreens_rotacion.json` registra actualización del 3 de noviembre a las 14:57.
- Los doce estilos existen en el catálogo y no se repiten dentro del mismo día. La repetición de `papel_rasgado_capas` ocurre en días distintos, no en slots consecutivos.
- No se detectó un cambio oficial nuevo de API que justificara investigación adicional.

## 9. Cambios ejecutados y límites

**Cambios realizados en la rama:**
1. Se registró `narrative_qa` en los doce storyboards y se releerieron los doce JSON; la tabla de scores/status coincide con esos archivos.
2. Se corrigieron los nueve estados documentales preparados en variantes bloqueadas sin PASS.
3. Se clasificó la variante extra de nubes como material de origen, no proyecto.
4. Se clasificó Maillard como procesamiento preexistente sin redispatch.
5. Se movió el paquete rechazado de enzimas a bloqueados después de verificar las cuatro copias.
6. Se creó este informe.

**No se modificó:** `data/*.json`, `main`, workflows, secretos, permisos, decisiones editoriales, estados de Grok, publicaciones ni archivos de medios. No se hizo merge ni se ejecutó dispatch.

**Ejecución:** revisión estática desde GitHub. No había checkout/runtime del repositorio disponible; no se ejecutó `validar_storyboard.py`, `procesar_cola.py` ni `registro_editorial.py`. La conclusión estructural se basa en inspección del código del validador y de los doce JSON, no en una ejecución del validador.
