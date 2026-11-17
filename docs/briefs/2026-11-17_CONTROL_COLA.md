# Auditoría CAPCOT — control de cola y rotación
**Fecha de auditoría:** 17-nov-2026, 15:35 CDMX  
**Repositorio:** `marcojpad-hash/capcot-capsulas-imaginantes`  
**Rama:** `feature/capcot-video-discovery-continuity`  
**Árbol revisado antes de este informe:** `d4a6b5fc1b32201a1179edc80e788f398a275786`  
**Resultado general:** el proyecto del día pasa la lectura narrativa, pero queda bloqueado por contradicción de voz; no hay entrada de cola ni recepción de Grok. El lote 5–7 sigue abierto: 2 PASS narrativos, 10 FAIL y 0/12 aptos bajo el contrato estructural ampliado.

## 1. Briefs y archivos del día

Se confirmaron:
- `docs/briefs/2026-11-17_RADAR_CAPCOT.md`
- `ajustes_entre_modelos/ESTADO_SLOTS_2026-11-17.md`
- Informe anterior: `docs/briefs/2026-11-16_CONTROL_COLA.md`

No existía todavía `docs/briefs/2026-11-17_CONTROL_COLA.md`; este archivo es el nuevo informe.

### Inventario del 17-nov

| Ubicación | Elementos | Fecha de creación | Fecha objetivo | Slot | Estado |
|---|---:|---|---|---|---|
| `proyectos/2026-11-17_dato-suelo-dos-relojes/storyboard.json` | 1 borrador | 17-nov, commit inicial 08:19 CDMX | 17-nov | 17:00, `intermedio_1` | Propuesta; no seleccionada |
| `cola/entrada/*.json` | 0 | — | — | — | Sin entradas |
| `cola/entrada/<project_id>/storyboard.json` | 0 del 17-nov | — | — | — | Sin paquetes del día |
| `salidas/2026-11-17/` | 0 | — | — | — | Sin salida |
| `cola/bloqueados/2026-11-17/` | 0 | — | — | — | Sin bloqueados del día |

El storyboard del día se creó a las 08:19; se completó fecha/slot a las 08:20; se añadió `narrative_qa` a las 15:07 y la verificación DOI/revisión estática se registró a las 15:09. El radar de las 08:11 es una fotografía anterior a la creación del storyboard, no evidencia de un borrador omitido.

No existe `data/horario_2026-11-17.json`. El slot 17:00 cae dentro de la ventana de tarde vigente (16:30–18:00), pero `intermedio_1` sigue siendo una clasificación propuesta en el storyboard/radar, no una selección formal de Grok. El radar indica 07:00 ocupado por un vídeo privado, 13:30 ocupado por Baffin, 19:00 con riesgo de una programación LDL pese a estar retirado y 23:30 como candidato `PENDING_SOURCE`. No se creó paquete adicional.

## 2. Revisión en frío del proyecto del día

**Proyecto:** `2026-11-17_dato-suelo-dos-relojes`

- 8 escenas; 214 palabras de narración; 78 s de escenas + 6 s de cortinilla = 84 s.
- Gancho: 5 palabras. Arco y cierre hablado presentes; termina con “Esto fue Datos y ociosidades.”
- `narrative_contract` completo.
- `narrative_qa` releído desde GitHub: **PASS / 89**, siete checks verdaderos, `critical_flags=[]`, `review_basis=lectura_en_frio_solo_narracion`. Se actualizó `reviewed_at` a 17-nov 15:35 CDMX.
- `source_ids` consistentes; el DOI `10.1038/s41467-026-79474-w` figura como verificado en Crossref y página editorial en el commit `a8623cff`. No se volvió a consultar el resolvedor en esta corrida.
- `estilo_id=papel_stop_motion` existe en el catálogo; `prompt_base` coincide con el catálogo y todos los prompts de escena comienzan con él.
- Mapa y capa de dato/gráfico presentes; ambiente y SFX declarados en las ocho escenas.
- `approved_assets=[]`; `export.render_status=NOT_GENERATED`; no hay `asset_filename`, `asset_type` ni rutas de medios.
- `publicacion.status=PENDIENTE_DECISION_GROK`; el proyecto sigue en propuesta, sin producción, QA audiovisual ni publicación.

**Bloqueo de contrato:** el tema es biología/ecología del suelo. `docs/VOCES_POR_TEMA.md` asigna `narradora_es` a biología; el storyboard declara `es-MX-JorgeNeural`. La Receta y `scripts/validar_storyboard.py` todavía exigen JorgeNeural global. No se cambió la voz ni se resolvió unilateralmente la contradicción. Se registró `BLOCKED_CONTRACT_CONFLICT` en `validation_notes.2026-11-17_auditor_review`. El PASS estático anterior corresponde al contrato/validador legado y no elimina el conflicto del mapa temático vigente.

Se corrigieron dos notas documentales obsoletas del storyboard: la que decía que el DOI seguía pendiente y la que decía que no existía `narrative_qa`. La corrección no cambió narración, claims, fuente ni decisión editorial.

**Dispatchabilidad:** `NOT_DISPATCHABLE`. El storyboard permanece en `proyectos/`; no existe `cola/entrada/2026-11-17_dato-suelo-dos-relojes.json`.  
**Recepción:** `RECEPCION_GROK_NO_CONFIRMADA`; no existe `cola/estado/2026-11-17_dato-suelo-dos-relojes.json` ni marcador en `handoffs/grok_inbox/`.

## 3. Inventario de cola preexistente

No hay JSON de primer nivel en `cola/entrada/*.json`. Los directorios históricos encontrados fueron:

| Paquete | Ubicación/fecha | Estado de ruta | Observación |
|---|---|---|---|
| `2026-11-07_dato-clavo-te-cocina` | Carpeta anidada | No despachable por workflow | Slot 23:30 de dato del día: exclusión absoluta. No se inspeccionó su contenido ni se modificó. |
| `2026-11-09_dato-robot-ensambla-orbita` | `cola/entrada/<id>/storyboard.json` | `NOT_DISPATCHABLE` | 9 escenas, 210 palabras, 88 s; QA narrativo persistido PASS/90. `frames/` contiene solo `.gitkeep`, no PNG. `ESTADO_EJECUCION` dice `PREPARADO_PENDIENTE_FRAMES_GROK`. |
| `2026-11-11_dato-ratas-topo-damaraland` | Carpeta anidada | Bloqueado | El storyboard no tenía `narrative_contract` ni `narrative_qa`, declaraba ocho `asset_filename` y `export.filename`, y no tenía `approved_assets=[]` ni `render_status`. Había ocho PNG reales (1.5–2.4 MB cada uno), no placeholders. |
| `2026-11-15_dato-dia-diapausa-lestes-sponsa` | Carpeta anidada | Bloqueado | QA narrativo persistido PASS/90, pero ocho `asset_filename` en `production_mode=storyboard_only`; no existen los frames referenciados. |

### Movimientos verificados

- Ratas topo: `storyboard.json` y `fuentes.md` se copiaron a `cola/bloqueados/2026-11-11_dato-ratas-topo-damaraland/`; se rele­yeron y compararon antes de retirar los originales de `cola/entrada/`. Los ocho PNG se conservaron intactos en la carpeta de entrada; quedó sin storyboard, por lo que ya no es paquete seleccionable.
- Lestes: `storyboard.json`, `fuentes.md` y `ESTADO_EJECUCION.md` se copiaron a `cola/bloqueados/2026-11-15_dato-dia-diapausa-lestes-sponsa/`; se rele­yeron antes de retirar los originales. El estado documental se corrigió exactamente a `BORRADOR_EN_PROYECTOS_NO_APTO_PARA_PROMOCION`.
- La afirmación del estado de Lestes de que el validador no consideró errores los ocho assets contradice el código vigente: `scripts/validar_storyboard.py` rechaza `asset_filename`/ `asset_type` en modo `storyboard_only` (regla actual alrededor de las líneas 223–225).
- El marcador de `handoffs/grok_inbox/2026-11-09_dato-robot-ensambla-orbita.json` dice `status=pending`, apunta a la rama `main` y no es acuse de Grok. Su estado individual en `cola/estado/` devuelve 404.

No se modificó ningún archivo `cola/estado/`. Para el proyecto del día, los doce proyectos del lote y los paquetes robot/ratas/Lestes consultados, la ausencia del JSON individual se registró como **`RECEPCION_GROK_NO_CONFIRMADA`**. El directorio `cola/estado/` no existe en el árbol de esta rama.

## 4. Lote obligatorio 5–7 de noviembre

Se rele­yeron los doce `proyectos/<id>/storyboard.json` y se compararon `project_id`, `fecha_objetivo`, `slot_local` y `slot_cesta` con `data/horario_semana_2026-11-01_07.json`. **Los doce coinciden exactamente**. El storyboard canónico de árboles sí trata redes micorrícicas comunes y Karst et al. 2023; no se marca desajuste temático. La variante `2026-11-05_inter-arboles-mito-respiran` en bloqueados es otro artefacto y no se confunde con el canónico.

| Project ID | QA releído | Score | Checks | Observación principal |
|---|---:|---:|---|---|
| `2026-11-05_kids-dia-en-venus` | PASS | 88 | 7/7 true | Narración coherente |
| `2026-11-05_comida-palomitas` | FAIL | 82 | 5/7 true | Apertura definicional y repetición en escena 6 |
| `2026-11-05_inter-arboles-se-comunican` | FAIL | 78 | 6/7 true | Apertura genérica; tema y Karst 2023 sí corresponden |
| `2026-11-05_inter-rayo-globular` | FAIL | 81 | 6/7 true | Apertura histórica descriptiva |
| `2026-11-06_kids-ballena-azul-corazon` | FAIL | 80 | 6/7 true | Payoff sobreafirma “casi se detiene” |
| `2026-11-06_comida-aguacate-negro` | FAIL | 79 | 5/7 true | Escenas 5–6 repiten causas sin avance |
| `2026-11-06_inter-ranas-congeladas` | FAIL | 83 | 5/7 true | Repetición de límites de especie/condiciones |
| `2026-11-06_inter-arena-cantante` | PASS | 94 | 7/7 true | Narración coherente |
| `2026-11-07_kids-huesos-bebe` | FAIL | 82 | 5/7 true | Escena 6 repite conteo/fusión |
| `2026-11-07_comida-hielo-caliente` | FAIL | 81 | 6/7 true | Apertura de creencias, no in medias res |
| `2026-11-07_inter-pulpo-suenos` | FAIL | 72 | 3/7 true | La fuente es de *Octopus laqueus*, no *O. insularis*; repetición y payoff vago |
| `2026-11-07_inter-nubes-pesan` | FAIL | 78 | 4/7 true | Escena 7 reitera cifra/límite sin payoff |

Los doce `narrative_qa` se actualizaron solo en `reviewed_at` a 17-nov-2026 15:35 CDMX. Los scores, checks y flags no se alteraron; se rele­yeron después de escribir.

### Revisión estructural del lote

- 12/12 tienen 7–9 escenas, 170–235 palabras, duración total de 84 s (78 s de escenas + 6 s de cortinilla), gancho de hasta seis palabras y cierre hablado.
- 85 escenas en total; faltan seis campos narrativos obligatorios por escena (`dramatic_beat`, `scene_function`, `causal_bridge_from_previous`, `question_state`, `reason_to_continue`, `new_information`): **510 ausencias**. El validador Python actual no impone todos estos campos del contrato ampliado.
- 75/85 arrays SFX están vacíos; la receta exige silencio explícito cuando no hay efecto.
- 11/12 proyectos contienen capa de mapa y dato/gráfico; árboles carece de ambas.
- Los 85 `source_ids` de escena apuntan a fuentes existentes; todos los `estilo_id` existen y los prompts coinciden con el `prompt_base` del catálogo.
- Ambiente declarado en las 85 escenas.
- `approved_assets=[]`, `export.render_status=NOT_GENERATED` y sin rutas de assets en los doce storyboards.
- Siete proyectos usan JorgeNeural aunque el mapa por tema asigna narradora_es a biología/cocina: palomitas, árboles, ballena, aguacate, ranas, huesos y pulpo. Receta/validador global y mapa por tema siguen en conflicto.
- Cinco afinidades estilo-tema son débiles según la descripción del propio catálogo: Venus/constructivista_ruso, palomitas/papel_recortado_popup, rayo/pixel_art, hielo/satira_periodico y pulpo/amigurumi. Los IDs y prompt_base sí existen. No hubo repetición de estilo dentro del mismo día.
- Cuatro fuentes de la muestra usan URL oficial sin DOI; en las demás el DOI está registrado. No se ejecutó `--check-doi` en esta auditoría.

### Producción y publicación preexistentes

No hay `salidas/<project_id>/` ni `qa.json` audiovisual para los doce IDs. Sí existen sidecars de TikTok/Facebook en siete carpetas de proyecto, con horarios posteriores al slot canónico; esos siete se clasifican **`PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`**:

| Proyecto | Evidencia de plataforma | Hora/visibilidad | ID / discrepancia |
|---|---|---|---|
| Venus | TikTok y Facebook publicados | TT 7-nov 17:00 Everyone; FB 7-nov 17:58 Public | Sidecar no vincula un YT ID; no atribuir `phVfyHp3CnY` sin evidencia |
| Palomitas | YT, TikTok y Facebook publicados | 8-nov 07:00; TT Everyone, FB Público | YT `zTP5akrGA9M`; slot real difiere del 5-nov 13:30 |
| Ballena | YT+TT publicados; FB programado | 11-nov 07:00; TT Everyone, FB Público sin post_id/URL | YT `wbFrlM2e_YE`; FB no confirmado como publicado |
| Aguacate | YT+TT publicados; FB programado | 10-nov 07:00; TT Everyone, FB Público sin post_id/URL | YT `nSS_q2tj2P0` |
| Ranas | YT+TT publicados; FB programado | 9-nov 07:00; TT Everyone, FB Público sin post_id/URL | YT `UBFuKBU3cx0` |
| Arena | YT, TikTok y Facebook publicados | TT 7-nov 13:30 Everyone; FB 7-nov 17:58 Public | YT público `m4RqQRaz55k`; `ztIkYcXB91U` sigue descrito como programado a las 19:00: riesgo de duplicado |
| Hielo caliente | YT/TT/FB programados | 11-nov 13:30; TT Everyone y FB Público | YT `HSgrnejAcaI`; TT/FB tienen registros de programación, no confirmación de publicación |

Los sidecars apuntan a MP4 bajo rutas locales `/workspace/...` que no existen en el árbol GitHub. Para los siete: **`MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`**. No se canceló ni borró ninguna programación.

Los bloqueados contienen snapshots anteriores y variantes. Hay snapshots con el mismo `project_id` para Rayo, Aguacate, Ranas, Arena, Huesos y Nubes; no se sobrescribieron. `2026-11-07_extra-nubes-pesan` comparte el project_id de Nubes, pero es material variante, no un segundo proyecto. Las variantes de Venus, Palomitas, Árboles, Ballena, Hielo y Pulpo con IDs distintos no sustituyen a los canónicos. La variante nocturna de árboles tampoco se confunde con el storyboard canónico de micorrizas.

**Corrección respecto al informe del 16-nov:** el recuento anterior de cinco proyectos con procesamiento preexistente era incompleto. La lectura de sidecars y horarios diarios confirma siete, al incluir Venus y Arena.

## 5. Workflow, procesador y registro editorial

### Workflow de Grok

`.github/workflows/capcot-grok-dispatch.yml`:
- Push trigger: `cola/entrada/*.json` (solo JSON de primer nivel).
- Push selector: regex `^cola/entrada/[^/]+\.json$`.
- Manual `all`: `find cola/entrada -maxdepth 1 -type f -name '*.json'`.
- Manual por ID: `cola/entrada/<project_id>.json`.
- No valida fecha objetivo interna ni limita la selección a la fecha actual.
- El workflow escribe `handoffs/grok_inbox/` con `status=pending`; ese marcador no es recepción. El webhook es opcional; si se habilita, requiere `GROK_WEBHOOK_URL` y `GROK_WEBHOOK_TOKEN`. No crea `cola/estado/`.

Por ruta, los paquetes anidados robot/ratas/Lestes no son despachables por el workflow. El proyecto del 17-nov en `proyectos/` tampoco es despachable. No hay JSON de primer nivel en la cola.

### Actions

La última ejecución específica de `capcot-grok-dispatch.yml` disponible es run #147, 1-nov-2026, fallo. Error literal: `Falta configurar GROK_WEBHOOK_URL.` La versión actual hace el webhook opcional y permite el buzón sin webhook; no hay ejecución posterior de este workflow que demuestre el nuevo flujo. El run #6 del 8-nov es `tts-tooling-smoke.yml`, no es despacho Grok.

### Procesador y registro

- `scripts/procesar_cola.py` usa la fecha CDMX actual por defecto y filtra por fecha del nombre de archivo/carpeta; admite `--fecha` para procesar fechas históricas explícitas. No es un bloqueo duro: no compara de forma obligatoria el prefijo con `fecha_objetivo` dentro del storyboard.
- El procesador contempla tanto JSON de primer nivel como `cola/entrada/<id>/storyboard.json`; esto difiere de la profundidad que admite el workflow.
- `scripts/registro_editorial.py` reúne storyboards de proyectos/cola/salidas, pero no lee los sidecars `proyectos/<id>/tiktok.json` y `facebook.json`, ni `cola/bloqueados/` ni `handoffs/`. Puede mostrar un storyboard como pendiente aunque ya haya publicación/programación real y subestimar el estado de rotación.

## 6. Data y documentos contradictorios

Se enumeraron los JSON de primer nivel en `data/`. Últimos registros relevantes:
- `data/cola.json`: 31-oct.
- `data/estilos_usados.json`: 28-oct.
- `data/temas_del_dia.json`: 28-oct.
- `data/rotacion.json`: 31-oct.
- `data/publicaciones.json`: 1-nov; no incluye los siete sidecars del lote.
- `data/horario_semana_2026-11-01_07.json`: hasta 7-nov; es la referencia canónica para el lote.
- `data/horario_2026-11-11.json`: 11-nov; confirma reprogramaciones de Palomitas, Ranas, Aguacate, Ballena y Hielo.
- `data/horarios.json`: actualizado 9-nov; contiene dos ventanas preferidas (06:30–07:30 y 16:30–18:00).
- `data/endscreens_rotacion.json`: actualizado 17-nov 13:37; contiene vistas/IDs, no un ledger editorial completo.
- `data/vistas_historico.json`: 28-oct.
- `data/cierre_diario/`: solo 25–27 oct en esta rama.
- No hay `data/horario_2026-11-17.json`.

Contradicciones vigentes:
1. Plan/Receta y validador siguen imponiendo JorgeNeural global; `VOCES_POR_TEMA.md` (11-nov) asigna voz por tema.
2. El contrato/rotación conserva cinco ventanas, incluida 19:00 y 23:30; `data/horarios.json` solo mantiene dos ventanas preferidas y el horario semanal retiró 19:00, reubicando slots a 17:45.
3. El validador no comprueba los seis campos narrativos ampliados ni exige SFX no vacíos, aunque Receta/QA narrativo los requieren.
4. `registro_editorial.py` no incorpora sidecars sociales ni estados de bloqueados/handoff.
5. El radar de las 08:11 precede a la creación del storyboard de suelo (08:19), su QA (15:07) y la verificación DOI (15:09). Las notas internas obsoletas del storyboard se corrigieron en esta auditoría.

No se revisaron APIs externas: no apareció un cambio oficial nuevo en el alcance documental inspeccionado.

## 7. Cambios realizados y límites

- Se actualizó `reviewed_at` de los doce QA del lote a 17-nov 15:35 CDMX; scores/checks/flags no cambiaron. Se rele­yeron los doce JSON desde GitHub.
- Se añadió `reviewed_at` y una nota de auditoría al proyecto del 17-nov; se corrigieron dos notas de verificación obsoletas. Su `narrative_qa` permanece PASS/89.
- Ratas topo y Lestes se movieron a `cola/bloqueados/<project_id>/` después de copiar y releer los archivos; solo después se retiraron las rutas originales de `cola/entrada/`. En Lestes se corrigió el estado documental a `BORRADOR_EN_PROYECTOS_NO_APTO_PARA_PROMOCION`.
- No se modificó `data/*.json`, `main`, workflow, secretos, permisos ni ningún archivo `cola/estado/`. No se hizo merge.
- No se promovió el proyecto del día: falta resolver el conflicto de voz y no hay selección editorial ni recepción.
- No se disparó Actions, no se enviaron payloads, no se generaron imágenes/frames/voz/audio/video/renders, no se publicó y no se consumieron créditos.
- No había runtime local del repositorio: validación estática; no se ejecutaron `validar_storyboard.py`, `procesar_cola.py` ni helpers. El estado de DOI del proyecto del día se tomó del JSON/commit previo, no de una nueva consulta Crossref.

**Conclusión:** el proyecto del 17-nov tiene historia PASS/89, pero permanece como propuesta por conflicto de voz y no es despachable. Los doce proyectos del lote coinciden con el horario; dos pasan narrativamente, diez fallan y ninguno cumple el contrato estructural ampliado. Siete ya tienen procesamiento/publicación preexistente y no deben redispatcharse. El lote 5–7 sigue abierto.
