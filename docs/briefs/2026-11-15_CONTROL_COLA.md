# CONTROL COLA CAPCOT — 2026-11-15

**Repositorio:** `marcojpad-hash/capcot-capsulas-imaginantes`  
**Rama:** `feature/capcot-video-discovery-continuity`  
**Corte:** 2026-11-15, 15:51 CDMX  
**Rol:** auditoría; sin producción, medios, publicación, dispatch ni consumo de créditos.

## 0. Precedencia y briefs confirmados

Leídos el Contrato Operativo Unificado, Plan Maestro, Receta, Guía de Modelo Externo, Flujo Externo, contrato de estados Grok, QA narrativo en frío, Continuidad Audiovisual, líneas temáticas, política de voces, plantillas, catálogo `scripts/estilos.json`, validador, procesador, rotación, registro editorial y los 20 JSON de `data/`.

Briefs:
- Existe [RADAR_CAPCOT_2026-11-15](2026-11-15_RADAR_CAPCOT.md). Su reejecución de 09:33 registra dos borradores y cinco slots con registro. La sección inicial de ese radar es una instantánea anterior; prevalece su sección posterior de reejecución y, para QA, prevalecen los storyboards releídos.
- Existe [CONTROL_COLA_2026-11-14](2026-11-14_CONTROL_COLA.md).
- Este archivo es el control del 15-nov; no existía antes de esta auditoría.

Precedencia aplicada: Contrato Operativo → Plan Maestro → Receta/Guía → Flujo Externo/Contrato Grok → plantillas, catálogo y validadores.

La plantilla vigente es `templates/storyboard_vertical.template.json` (9:16). `templates/storyboard.template.json` sigue siendo un esquema legado 16:9/120 s con rutas de assets; `templates/storyboard_generico.template.json` devuelve 404. `docs/FLUJO_DE_PRODUCCION.md` conserva instrucciones antiguas de 60–180 s, 16:9 y assets locales; el Contrato Operativo lo subordina a la Receta/Flujo Externo vigentes. No se usó como contrato de preproducción.

## 1. Día actual — 15 de noviembre

### Inventario exacto

En el árbol actual de la rama hay **dos** borradores de la fecha en `proyectos/<project_id>/storyboard.json`:

| Proyecto | Creación del borrador (CDMX) | Fecha objetivo | Slot declarado | Estado narrativo releído | Dispatch |
|---|---|---|---|---|---|
| `2026-11-15_dato-quasar-pareja-cosmic-dawn` | 15-nov 09:17:15, commit `20aa7ae3d07bfb71165adef7d12f0ab345f4439c` | 15-nov | 17:00 / `intermedio_1` | FAIL 82 | NOT_DISPATCHABLE |
| `2026-11-15_dato-dia-diapausa-lestes-sponsa` | 15-nov 09:18:41, commit `b8fe24acb0a3cb4bf9aeb7d569c1b115642757bf` | 15-nov | 23:30 / `dato_del_dia` | PASS 90 | NOT_DISPATCHABLE |

Los commits iniciales están firmados por la cuenta del repositorio; no se atribuye la creación a una automatización/investigador concreto sin evidencia adicional.

**Cola del 15-nov:** 0 archivos en `cola/entrada/*.json` y 0 carpetas `cola/entrada/<project_id>/` de esa fecha. La carpeta `cola/entrada/` conserva tres paquetes históricos anidados (7, 9 y 11-nov), ninguno del día actual. No hay salida ni carpeta bloqueada del 15-nov.

El índice de búsqueda de GitHub devuelve referencias antiguas a `2026-11-15_atlas-3d-cerebro` y `2026-11-15_comida-arroz-olvidado`; las rutas directas en esta rama devuelven 404 y no aparecen en el listado actual de `proyectos/` ni `cola/entrada/`. No se cuentan como paquetes vigentes.

### Lectura en frío y estado de los dos borradores

La lectura usó únicamente la narración concatenada; no se consultaron título, resumen, arco, notas ni `narrative_contract` para decidir QA.

| Proyecto | Escenas | Palabras | Escenas + cortinilla | Gancho | QA JSON |
|---|---:|---:|---:|---:|---|
| Quasar | 8 | 180 | 78 + 6 = 84 s | 5 | FAIL 82 |
| Diapausa de `Lestes sponsa` | 8 | 183 | 78 + 6 = 84 s | 6 | PASS 90 |

- **Quasar — FAIL 82:** la escena 2 vuelve a nombrar Gemini North y añade ubicación, pero no hace avanzar la pregunta; la transición 2→3 hacia la edad cósmica no tiene puente causal suficiente. Checks falsos: `progresion_por_escena`, `transiciones_causales`. Flags: `ESCENA_002_REITERA_GEMINI_NORTH_Y_NO_AVANZA_LA_PREGUNTA`, `TRANSICION_002_003_NO_CAUSAL`.
- **Lestes — PASS 90:** la apertura presenta la eclosión en curso; la narración reconstruye qué señal termina la diapausa, explica el papel del frío, separa resultado experimental de hipótesis climática y cierra pagando la apertura. Siete checks verdaderos; flags vacíos.

Corrección mecánica aplicada: `word_count` de Quasar pasó de 178 a 180, conforme al conteo del validador; la narración no se modificó. Se añadieron los dos objetos `narrative_qa` y se releeron desde GitHub. Blobs posteriores: Quasar `ab3edf2a95875f820fe0b190ea61ade0b646cd98`; Lestes `1164b4944082f56e7ab7b319c02c4ca99ab0b4be`.

### Estructura, fuentes y handoff

Ambos borradores tienen `narrative_contract` completo; voz `edge-tts / es-MX-JorgeNeural` (+7%, -2 Hz); estilo existente en catálogo y `visual_identity.prompt_base` literal; prompts de escena con ese prefijo; `source_ids` válidos; mapa con coordenadas y fuente; capa de dato/gráfico con fuente; ambiente y SFX no vacíos; cortinilla de 6 s; arcos completos y sello hablado exacto. En ambos: `approved_assets=[]`, `export.render_status=NOT_GENERATED`, sin `asset_filename`, `asset_type`, `export.filename` ni rutas de medios.

- Quasar usa `van_gogh`; DOI `10.3847/2041-8213/aeb11f` sigue `PENDIENTE_RESOLVEDOR`. Sus otras dos fuentes son comunicado institucional y coordenadas de Gemini North.
- Lestes usa `rubber_hose_1930s`; DOI `10.1038/s41598-026-80392-6` sigue `PENDIENTE_RESOLVEDOR`. El pin de Lund es referencia regional, no el sitio exacto de muestreo.

Ambos conservan `editorial_status=PENDIENTE_DECISION_GROK`, `publicacion.status=PENDIENTE_DECISION_GROK` y `estado=PENDIENTE_AUDITOR`. No existe `ESTADO_EJECUCION.md` en ninguno de los dos directorios. No se modificó la decisión editorial.

**Handoff:** ambos están en `proyectos/`, no en `cola/entrada/`; por tanto, **NOT_DISPATCHABLE**. Para ambos: **RECEPCION_GROK_NO_CONFIRMADA** (no existe `cola/estado/<project_id>.json`). Lestes no se promovió aunque su QA narrativo sea PASS: no hubo runtime para ejecutar el validador real ni `--check-doi`, el DOI sigue pendiente y la instrucción de este run prohíbe provocar un workflow mediante una escritura en la ruta de cola. Quasar permanece en proyectos por FAIL.

## 2. Slots, rotación y cupo del día

`ajustes_entre_modelos/ESTADO_SLOTS_2026-11-15.md` registra cinco elementos:

- 07:00 — colibrí, YouTube privado/programado para 13:00Z.
- 13:30 — agua-imanes, slot de prueba ocupado.
- 17:00 — Quasar, borrador existente.
- 19:00 — autismo-microbioma, registrado en el estado diario.
- 23:30 — Lestes, borrador existente, cesta `dato_del_dia`.

No existe `data/horario_2026-11-15.json`. La configuración `data/horarios.json` (política desde 09-nov) conserva las ventanas 06:30–07:30 y 16:30–18:00, más 23:30 fijo; 19:00 aparece retirado. Por tanto, el registro 19:00 del estado diario contradice la política vigente. El slot 13:30 figura como prueba en el historial de horarios. El estado diario dice que los cinco registros alcanzan el cupo; no se autoriza añadir otro.

Rotación:
- Los dos candidatos no repiten entre sí tema, estructura, estilo ni cama musical.
- `van_gogh` y `rubber_hose_1930s` existen en `scripts/estilos.json` y sus prompts base coinciden literalmente.
- `data/estilos_usados.json` llega solo al 28-oct; el estilo del colibrí 07:00 y el de agua-imanes no están documentados en el estado diario. La unicidad respecto de esos slots no es certificable.

## 3. Workflow, cola, procesador y Grok

### Dispatchabilidad

`.github/workflows/capcot-grok-dispatch.yml`:
- El evento push escucha solo `cola/entrada/*.json`.
- El selector manual `all` busca con `-maxdepth 1`.
- El selector manual por ID espera `cola/entrada/<project_id>.json`.
- No filtra por fecha.
- No selecciona `proyectos/<id>/storyboard.json` ni `cola/entrada/<id>/storyboard.json`.

Por ello, los dos borradores del día y los tres paquetes históricos anidados son **NOT_DISPATCHABLE** por el workflow actual. La presencia en GitHub no demuestra recepción.

### Procesador y registro editorial

`scripts/procesar_cola.py`:
- Descubre JSON de primer nivel y `cola/entrada/*/storyboard.json`.
- Por defecto toma la fecha actual de America/Mexico_City y filtra por el prefijo de fecha del nombre/ruta.
- Permite `--fecha AAAA-MM-DD`; no impide explícitamente pasar una fecha histórica. El comportamiento predeterminado es fecha actual, no una prohibición absoluta de override.
- Invoca `validar_storyboard.py --check-doi`; no se ejecutó ese helper en este run.

`scripts/registro_editorial.py`:
- Lee registros de `data/rotacion.json`, `data/publicaciones.json`, `data/cola.json` y storyboards de `proyectos/`, `cola/entrada/`, `cola/`, `salidas/`.
- No lee `cola/bloqueados/`, `handoffs/grok_inbox/`, `ajustes_entre_modelos/ESTADO_SLOTS_*.md` ni los JSON diarios `data/horario_*.json`.
- Un storyboard que solo está en `proyectos/` se clasifica por defecto como origen `propia`, aunque sea una propuesta externa de ChatGPT.

`scripts/rotacion.py` fija `MAX_POR_DIA=5`, pero `hecha_hoy()` depende de `registro_editorial.registros_dia()`. Los tres slots previos del estado 15-nov no aparecen en los registros canónicos actuales, por lo que el cupo computado puede contar solo los dos borradores y permitir entradas adicionales indebidamente. Además, `VENTANAS` aún incluye 18:00–21:00 (slot 19:00), en contradicción con `data/horarios.json`.

### Entradas históricas y recepción

`cola/entrada/` contiene solo tres carpetas históricas anidadas: 7, 9 y 11-nov. No hay JSON de primer nivel ni carpeta del 15-nov. Los tres paths anidados no coinciden con el workflow. `handoffs/grok_inbox/` contiene solo `2026-11-09_dato-robot-ensambla-orbita.json`, con `status=pending`; no es un acuse de lectura por Grok. No hay marcador del 15-nov.

`cola/estado/` devuelve 404 como directorio. Se consultaron los 14 IDs vigentes de este control (dos del 15-nov y los doce del lote 5–7): todos devuelven 404. Para cada uno: **RECEPCION_GROK_NO_CONFIRMADA**. También se consultaron los estados de los tres paquetes históricos anidados; no hay JSON de estado. No se creó ni modificó ningún estado Grok.

### Actions

La última ejecución identificada de `capcot-grok-dispatch` es run #147, 2026-11-01, failure. El log conserva literalmente: `Falta configurar GROK_WEBHOOK_URL.` Esa ejecución corresponde a una versión anterior del workflow. El archivo actual trata el webhook como opcional y deja un marcador en `handoffs/grok_inbox/`; no se encontró una ejecución posterior de este workflow. No hay evidencia de que falte `GROK_WEBHOOK_TOKEN`; no se afirma.

## 4. Lote obligatorio 5–7 de noviembre

Los doce `project_id`, fechas objetivo, slots y cestas coinciden con `data/horario_semana_2026-11-01_07.json`. Los temas y fuentes corresponden al slot, con la discrepancia de especie del pulpo descrita abajo. Los QA se releyeron en frío y se actualizaron únicamente `reviewed_at` a `2026-11-15T15:51:23-06:00`; scores, checks y flags se releen de los JSON actuales.

| Proyecto | Slot / cesta | narrative_qa | Checks falsos / critical_flags |
|---|---|---:|---|
| `2026-11-05_kids-dia-en-venus` | 07:00 / kids | PASS 88 | ninguno; [] |
| `2026-11-05_comida-palomitas` | 13:30 / comida_familia | FAIL 82 | apertura, progresión; apertura definicional y repetición de causas en escena 6 |
| `2026-11-05_inter-arboles-se-comunican` | 17:00 / intermedio_1 | FAIL 78 | apertura; `APERTURA_GENERICA_NO_IN_MEDIAS_RES` |
| `2026-11-05_inter-rayo-globular` | 17:45 / intermedio_2 | FAIL 81 | apertura; apertura histórica descriptiva |
| `2026-11-06_kids-ballena-azul-corazon` | 07:00 / kids | FAIL 80 | payoff; `PAYOFF_SOBREAFIRMA_CASI_SE_DETIENE` |
| `2026-11-06_comida-aguacate-negro` | 13:30 / comida_familia | FAIL 79 | progresión, transiciones; repetición de escenas 5–6 |
| `2026-11-06_inter-ranas-congeladas` | 17:00 / intermedio_1 | FAIL 83 | progresión, transiciones; repetición de límites de especie/condiciones |
| `2026-11-06_inter-arena-cantante` | 17:45 / intermedio_2 | PASS 94 | ninguno; [] |
| `2026-11-07_kids-huesos-bebe` | 07:00 / kids | FAIL 82 | progresión, transiciones; repetición de conteo/fusión |
| `2026-11-07_comida-hielo-caliente` | 13:30 / comida_familia | FAIL 81 | apertura; `APERTURA_DE_CREENCIAS_NO_IN_MEDIAS_RES` |
| `2026-11-07_inter-pulpo-suenos` | 17:00 / intermedio_1 | FAIL 72 | progresión, transiciones, giro, límite y payoff; fuente de especie incorrecta y repetición |
| `2026-11-07_inter-nubes-pesan` | 17:45 / intermedio_2 | FAIL 78 | progresión, transiciones, payoff; escena 7 reitera cifra/límite sin pagar la suspensión |

Resultado del lote: **2 PASS y 10 FAIL**. El score del pulpo cambió de 80 (reporte anterior) a 72 en el JSON actual tras verificar la fuente primaria; el JSON releído prevalece.

### Tema, identidad y fuente del pulpo

- El storyboard canónico `2026-11-05_inter-arboles-se-comunican` sí trata redes micorrícicas comunes y Karst et al. 2023. No hay desajuste de tema. La variante `2026-11-05_inter-arboles-mito-respiran` es otro artefacto bloqueado y no se confundió con el canónico.
- `2026-11-07_inter-nubes-pesan` es el único proyecto del slot 17:45. `2026-11-07_extra-nubes-pesan` está marcado como material de origen, no como segundo proyecto.
- El storyboard de pulpo atribuye el estudio del DOI `10.1038/s41586-023-06203-4` a `Octopus insularis`. La sección Methods del artículo de Nature especifica que los animales experimentales fueron `O. laqueus`; la fuente no respalda la especie que afirma el storyboard: https://www.nature.com/articles/s41586-023-06203-4. El QA queda FAIL y no se modificó la narración ni el claim.

### Estructura estática del lote

| Control | Resultado |
|---|---:|
| Storyboards | 12 |
| Escenas totales | 85 |
| Escenas por storyboard | 7–8 |
| Duración | 84 s cada uno (78 s escenas + 6 s cortinilla) |
| Gancho | 3–5 palabras |
| Narraciones | 169–221 palabras; Árboles tiene 169, una menos del mínimo |
| Arcos y sello | completos en los 12 |
| Voz, `source_ids`, catálogo y `prompt_base` | presentes/coincidentes |
| Mapa y dato/gráfico | Árboles carece de ambas capas; los otros 11 las tienen |
| Campos narrativos ausentes | **510** (seis por escena: `dramatic_beat`, `scene_function`, `causal_bridge_from_previous`, `question_state`, `reason_to_continue`, `new_information`) |
| SFX vacíos | **75/85**, sin indicación explícita de silencio; ambiente existe en las 85 |
| `approved_assets` | [] en los 12 |
| `export.render_status` | NOT_GENERATED en los 12 |
| Rutas/asset_filename/asset_type | ausentes |

Los 510 campos narrativos faltantes hacen fallar el validador actual. El validador solo comprueba que exista la clave `sfx`, no que el array tenga un SFX ni que un array vacío declare silencio; por ello no detecta los 75 casos sin diseño sonoro explícito. No se añadieron campos interpretativos ni se reescribieron claims.

### Bloqueados y copias heredadas

No hay copias canónicas de los doce en `cola/entrada/` que requieran traslado. Ya existen artefactos bloqueados relacionados: copias canónicas de Rayo, Arena, Nubes, Pulpo, Huesos y Aguacate; carpeta canónica de Ranas; y variantes separadas de Venus, Palomitas, Árboles, Ballena, Mpemba y Nubes extra. Los `ESTADO_EJECUCION.md` leídos en las carpetas bloqueadas ya dicen `BORRADOR_EN_PROYECTOS_NO_APTO_PARA_PROMOCION`; la variante extra de Nubes dice `MATERIAL_DE_ORIGEN_NO_ES_PROYECTO`. No hubo movimientos ni eliminación de archivos.

## 5. Guardia de producción preexistente — NO REDISPATCH

No existen directorios `salidas/<project_id>/` para los doce proyectos del lote: no hay `qa.json`, `publicacion.json`, `metadata.json` ni `licencias.json` por proyecto en el árbol. Aun así, los horarios diarios posteriores muestran procesamiento/publicación para cinco IDs exactos. Todos quedan **PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR**:

| Proyecto | YouTube | TikTok | Facebook | Horario/privacidad/duración registrada |
|---|---|---|---|---|
| Palomitas | `zTP5akrGA9M`, publicado | `7705593452003691794`, publicado | `1167496802382795`, publicado | 08-nov 07:00; privacidad no registrada; duración no disponible en el registro |
| Ranas | `UBFuKBU3cx0`, publicado | `7705596671807245586`, publicado | `programado_lote_7nov`, sin URL | 09-nov 07:00; privacidad no registrada; duración no disponible |
| Aguacate | `nSS_q2tj2P0`, publicado | `7705594217136966920`, publicado | `programado_lote_7nov`, sin URL | 10-nov 07:00; YT 83 s; privacidad no registrada |
| Ballena | `wbFrlM2e_YE`, publicado | `7705594333574991122`, publicado | `programado_lote_7nov`, sin URL | 11-nov 07:00; YT 80 s; privacidad no registrada |
| Hielo caliente | `HSgrnejAcaI`, privado/programado | `7706905447424347393`, Everyone | Público, UI “En proceso…” | 11-nov 13:30; YT publishAt 19:30Z; YT 90 s |

Los primeros cuatro registros no guardan privacidad explícita. Hielo sí: YouTube privado y programado, TikTok Everyone, Facebook Público/En proceso. Las duraciones de 83/80/90 s son metadatos de plataforma, no sustituyen `salidas/qa.json`; no hay QA audiovisual verificable en el árbol.

Los MP4 referenciados no están en el árbol: cuatro apuntan a `/workspace/capcot_prod_20261108_semana/...`; Hielo apunta a `/workspace/capcot_main/salidas/2026-11-07_comida-hielo-caliente/capsula.mp4`, ruta que tampoco existe en el árbol GitHub. En los cinco casos: **MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO**. No se borró ni canceló ninguna programación.

### IDs históricos de YouTube

No existe un archivo separado `historial_youtube` en `data/`. `data/horario_semana_2026-11-01_07.json` conserva **22 IDs antiguos** en `yt_id_historial`, distribuidos en diez slots del 1–3 nov cuyos registros principales siguen con `estado=programado_yt_tt_fb`. No hay confirmación por ID de que los históricos se hayan retirado. Se marca riesgo de duplicado; no se intentó borrarlos en Studio ni en servicios externos.

## 6. Datos, documentos y contradicciones

Se inspeccionaron los 20 JSON existentes en `data/`:
- `rotacion.json`: 27 registros, último 31-oct.
- `publicaciones.json`: 22 registros, último 31-oct.
- `cola.json`: un registro, último 31-oct.
- `temas_del_dia.json`: solo 24–28-oct.
- `estilos_usados.json`: 21 registros, último 28-oct.
- `vistas_historico.json`: 74 snapshots, último 28-oct.
- `balances_6h.json`: 11 balances, último 28-oct.
- `horarios.json`: política actualizada 09-nov; 19:00 retirado.
- `horario_semana_2026-11-01_07.json`: fuente canónica de los doce slots históricos.
- `horario_2026-11-08.json` a `horario_2026-11-11.json`: registros de publicaciones posteriores.
- `reprogramacion_tt_fb_v4_2026-11-01_03.json`: corte 03-nov.
- `endscreens_rotacion.json`: última revisión 14-nov.
- `data/cierre_diario/`: solo 25, 26 y 27-oct.
- No existe `data/horario_2026-11-15.json` ni un `historial_youtube` dedicado.

Contradicciones que afectan operación:
1. El estado diario del 15-nov registra 19:00; `data/horarios.json` lo declara retirado y `scripts/rotacion.py` todavía incluye la ventana 18:00–21:00.
2. El Plan/Contrato describen cinco ventanas/slots, mientras la política desde 09-nov reduce las ventanas activas y conserva 23:30 fijo.
3. `registro_editorial.py` no incorpora el estado diario ni horarios diarios, bloqueados o handoffs. La guardia de cupo puede subcontar los tres slots preexistentes del 15-nov.
4. `procesar_cola.py` usa fecha actual por defecto, pero `--fecha` permite seleccionar una fecha histórica; no es un bloqueo absoluto contra fechas anteriores.
5. `templates/storyboard.template.json` y `docs/FLUJO_DE_PRODUCCION.md` siguen visibles con el contrato viejo; el Contrato Operativo los subordina a la plantilla vertical/Receta vigentes.

## 7. Runtime, APIs y límites

- No había runtime local/checkout ejecutable. No se ejecutaron `validar_storyboard.py`, `procesar_cola.py`, helpers ni pruebas Python. Se hizo revisión estática del código y de los JSON; no se declara validador ejecutado.
- El helper `validar_storyboard.py --check-doi` consulta Crossref. No se ejecutó; los DOI de los dos borradores actuales permanecen pendientes.
- `docs/INVESTIGACION_API_META_Y_GOOGLE_TRENDS.md` ya contiene notas oficiales fechadas 15-nov. No se implementó ni modificó ninguna integración API en esta auditoría; no se identificó un cambio oficial adicional que justificara tocar código.
- No se generaron cápsulas, frames, imágenes, voz, audio, video ni renders; no se publicó, programó, disparó Actions ni envió payload externo; no se consumieron créditos.

## 8. Cambios efectuados y verificación

Se modificaron únicamente los JSON de storyboard en `proyectos/`:
- Dos `narrative_qa` nuevos para el 15-nov.
- Doce `reviewed_at` actualizados para el lote 5–7.
- Pulpo pasó de score 80 a 72 y se añadió el flag de especie/fuente incorrecta tras verificar la página primaria.
- Quasar `word_count` corregido de 178 a 180; narración intacta.

Los 14 storyboards se releen desde GitHub. Los scores/statuses de este informe coinciden con sus JSON actuales. No se modificaron `data/*.json`, `cola/entrada/`, `cola/estado/`, `cola/bloqueados/`, workflows, secretos, permisos, `main` ni se hizo merge. No se promovió ningún proyecto y no se atribuyó recepción/QA audiovisual a Grok.
