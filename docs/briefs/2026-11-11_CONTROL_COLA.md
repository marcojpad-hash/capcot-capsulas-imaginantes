# Auditor CAPCOT — control de cola y rotación

**Corte:** 2026-11-11 15:25:07 America/Mexico_City  
**Rama auditada:** `feature/capcot-video-discovery-continuity`  
**Modo:** auditoría documental y narrativa; sin producción, medios, publicación, dispatch ni consumo de créditos.

## 1. Resultado ejecutivo

- **Día 11-nov:** 0 storyboards en `proyectos/`, 0 entradas de cola con fecha objetivo 11-nov, 0 paquetes del día en `salidas/` y 0 en `cola/bloqueados/`. El brief del día existe: `docs/briefs/2026-11-11_RADAR_CAPCOT.md`.
- **Lote obligatorio 5–7 nov:** 12/12 borradores presentes en `proyectos/`; 12/12 coinciden con el horario semanal en `project_id`, `fecha_objetivo`, `slot_local` y `slot_cesta`.
- **QA narrativo en frío, releído y registrado en este corte:** 2 PASS / 10 FAIL. Los JSON releídos desde GitHub contienen exactamente los scores y checks de la tabla de la sección 3.
- **Validador estructural:** 0/12 aptos. Las 85 escenas carecen de seis campos narrativos obligatorios: 510 campos ausentes. Además, el storyboard de árboles tiene 169 palabras y no contiene mapa ni capa de dato/gráfico.
- **Promociones a cola:** 0. Los dos PASS narrativos (Venus y arena) no pasan la validación estructural; los diez FAIL tampoco son promovibles.
- **Recepción Grok:** los 12 archivos `cola/estado/<project_id>.json` devolvieron HTTP 404: `RECEPCION_GROK_NO_CONFIRMADA`. No se creó ni modificó ningún estado.
- **No redispatch:** cinco proyectos del lote tienen evidencia de publicación o programación en los registros diarios. Se clasifican `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`; sus medios no están en el árbol GitHub: `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`.

## 2. Fuentes y autoridad revisadas

Leídos en la rama auditada:

- `docs/CONTRATO_OPERATIVO_UNIFICADO.md`, `docs/PLAN_MAESTRO_AUTOMATICO.md`, `docs/RECETA_CAPSULA.md`, `docs/GUIA_MODELO_EXTERNO.md`, `docs/FLUJO_EXTERNO.md`, `docs/GROK_STATUS_CONTRACT.md` y `docs/QA_NARRATIVO_EN_FRIO.md`.
- Plantillas `templates/storyboard_vertical.template.json`, `templates/grok_status.template.json` y `templates/storyboard.template.json`.
- Catálogo canónico `scripts/estilos.json` y vista `docs/ESTILOS_VISUALES.md).
- `scripts/validar_storyboard.py`, `scripts/procesar_cola.py` y `scripts/registro_editorial.py).
- Los 20 JSON existentes directamente bajo `data/`, incluidos los horarios diarios 8–11 nov, el horario semanal 1–7 nov, rotación, publicaciones, estilos, temas, cola, balances y vistas históricas.
- Brief del día `docs/briefs/2026-11-11_RADAR_CAPCOT.md` y `ajustes_entre_modelos/ESTADO_SLOTS_2026-11-11.md`.

La jerarquía vigente es la del Contrato Operativo Unificado. Los estados, la selección editorial, el QA audiovisual y la publicación corresponden a Grok/Imaginantes; la presencia de un archivo en GitHub no acredita recepción ni producción.

## 3. Lote obligatorio 5–7 nov: identidad, QA y estructura

Los 12 borradores canónicos fueron incorporados al repositorio por el commit `7a415426f5907c2ab03687a47f3d160a595cb669`, fechado 2026-11-02 22:11:24Z (16:11:24 CDMX). La fecha objetivo y el slot se toman del horario semanal, no de la fecha de ese commit.

Todos los registros de QA se relevaron a `reviewed_at=2026-11-11T15:25:07-06:00`. Se ocultaron título, resumen, arco, notas y `narrative_contract`; la lectura se hizo únicamente sobre la narración concatenada. Todos conservan `review_basis=lectura_en_frio_solo_narracion` y los siete checks explícitos: `pregunta_central_reconstruible`, `apertura_in_medias_res`, `progresion_por_escena`, `transiciones_causales`, `giro_cientifico_explicado`, `limite_evidencia_explicito`, `payoff_cierre_apertura`.

| Project ID | Slot / cesta | Escenas / palabras | QA releído | Checks false / critical_flags |
|---|---|---:|---|---|
| `2026-11-05_kids-dia-en-venus` | 07:00 / kids | 7 / 170 | **PASS 88** | Ninguno; siete checks true; flags vacíos |
| `2026-11-05_comida-palomitas` | 13:30 / comida_familia | 7 / 173 | **FAIL 82** | `apertura_in_medias_res`, `progresion_por_escena`; `APERTURA_DEFINICIONAL_NO_IN_MEDIAS_RES`, `ESCENA_6_REITERA_CAUSAS_DE_GRANOS_NO_REVENTADOS_SIN_INFORMACION_NUEVA` |
| `2026-11-05_inter-arboles-se-comunican` | 17:00 / intermedio_1 | 8 / 169 | **FAIL 78** | `apertura_in_medias_res`; `APERTURA_GENERICA_NO_IN_MEDIAS_RES` |
| `2026-11-05_inter-rayo-globular` | 17:45 / intermedio_2 | 7 / 197 | **FAIL 81** | `apertura_in_medias_res`; `APERTURA_HISTORICA_DESCRIPTIVA_NO_IN_MEDIAS_RES` |
| `2026-11-06_kids-ballena-azul-corazon` | 07:00 / kids | 7 / 174 | **FAIL 80** | `payoff_cierre_apertura`; `PAYOFF_SOBREAFIRMA_CASI_SE_DETIENE` |
| `2026-11-06_comida-aguacate-negro` | 13:30 / comida_familia | 7 / 170 | **FAIL 79** | `progresion_por_escena`, `transiciones_causales`; `REPETICION_ESCENAS_5_6_SIN_AVANCE_CAUSAL` |
| `2026-11-06_inter-ranas-congeladas` | 17:00 / intermedio_1 | 7 / 177 | **FAIL 83** | `progresion_por_escena`, `transiciones_causales`; `REPETICION_ESCENAS_5_6_LIMITES_DE_ESPECIE_Y_CONDICIONES` |
| `2026-11-06_inter-arena-cantante` | 17:45 / intermedio_2 | 7 / 206 | **PASS 94** | Ninguno; siete checks true; flags vacíos |
| `2026-11-07_kids-huesos-bebe` | 07:00 / kids | 7 / 172 | **FAIL 82** | `progresion_por_escena`, `transiciones_causales`; `ESCENA_6_REPITE_VARIACION_DE_CONTEO_Y_FUSION` |
| `2026-11-07_comida-hielo-caliente` | 13:30 / comida_familia | 7 / 172 | **FAIL 81** | `apertura_in_medias_res`; `APERTURA_DE_CREENCIAS_NO_IN_MEDIAS_RES` |
| `2026-11-07_inter-pulpo-suenos` | 17:00 / intermedio_1 | 7 / 170 | **FAIL 80** | `progresion_por_escena`, `transiciones_causales`, `payoff_cierre_apertura`; `REPETICION_ESCENAS_5_6_Y_PAYOFF_VAGO` |
| `2026-11-07_inter-nubes-pesan` | 17:45 / intermedio_2 | 7 / 221 | **FAIL 78** | `progresion_por_escena`, `transiciones_causales`, `payoff_cierre_apertura`; `ESCENA_7_REITERA_CIFRA_Y_LIMITE_SIN_PAYOFF_DE_SUSPENSION` |

### 3.1 Estructura

Comprobaciones estáticas de los 12 JSON:

- Los campos raíz exigidos por el validador están presentes; los seis campos de `narrative_contract` están completos.
- Todos tienen 7–8 escenas, gancho de 3–5 palabras, arco completo en orden, cierre hablado exacto y `target_duration_seconds=84`.
- Las escenas suman 78 s y la cortinilla de fuentes 6 s: total 84 s. Los 12 declaran resolución 1080×1920.
- 11/12 cumplen 170–235 palabras. Árboles queda en 169.
- Voz uniforme: edge-tts, `es-MX-JorgeNeural`, `es-MX`, `+7%`, `-2Hz`.
- Los `source_ids` de las escenas apuntan a fuentes declaradas. Las fuentes incluyen URL y estado de verificación en el JSON. Los DOI presentes tienen formato y URL DOI; las fuentes sin DOI usan URL primaria.
- Los 12 `style_id` existen en el catálogo; `visual_identity.prompt_base` coincide literalmente con el catálogo y todos los `image_prompt` empiezan con ese prefijo.
- Ambiente y SFX están declarados en todas las escenas.
- 11/12 tienen mapa con puntos/fuente y capa de dato/gráfico con fuente. Árboles no tiene ninguna de las dos.
- Las 85 escenas omiten los seis campos obligatorios `dramatic_beat`, `scene_function`, `causal_bridge_from_previous`, `question_state`, `reason_to_continue` y `new_information`: **510 ausencias**. Esta es una falla estructural común a los 12.
- En los 12: `approved_assets=[]`, `export.render_status=NOT_GENERATED`; no aparecen `asset_filename`, `asset_type`, `export.filename` ni rutas de medios.

**Resultado:** el validador estructural no pasa en ninguno. Venus y arena pasan QA narrativo, pero no pueden promoverse por los seis campos ausentes. Los otros diez permanecen FAIL narrativo y estructural. No se reescribió narración ni claims.

### 3.2 Tema, fuentes y estilos

Los 12 `project_id`, fecha, hora y cesta coinciden con `data/horario_semana_2026-11-01_07.json`. Los temas y fuentes corresponden al slot asignado. El storyboard canónico `2026-11-05_inter-arboles-se-comunican` sí trata redes micorrícicas comunes y Karst et al. 2023; no se marca desajuste temático. La variante `inter-arboles-mito-respiran` en bloqueados es otro artefacto. El slot 2026-11-07 17:45 es exactamente `2026-11-07_inter-nubes-pesan`; `extra-nubes-pesan` es material de origen, no un segundo proyecto.

Los estilos de los storyboards son válidos y los prompts coinciden con el catálogo. `data/estilos_usados.json` termina en 28-oct y no sirve por sí solo para certificar la rotación del lote 5–7.

## 4. Producción preexistente y no redispatch

No existen directorios `salidas/<project_id>/` para los 12 IDs en esta rama. Sin embargo, los horarios diarios posteriores contienen evidencia externa suficiente para bloquear un segundo dispatch en cinco proyectos:

| Proyecto | Evidencia registrada | Clasificación |
|---|---|---|
| `2026-11-05_comida-palomitas` | 8-nov 07:00: YouTube `zTP5akrGA9M`; TikTok `7705593452003691794`; Facebook `1167496802382795`; registro `publicado_yt_tt_fb`. | `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR` |
| `2026-11-06_inter-ranas-congeladas` | 9-nov 07:00: YouTube `UBFuKBU3cx0` público; TikTok `7705596671807245586` publicado; Facebook figura programado en lote previo, sin URL/ID en ese registro. | `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR` |
| `2026-11-06_comida-aguacate-negro` | 10-nov 07:00: YouTube `nSS_q2tj2P0` público; TikTok `7705594217136966920` publicado; Facebook figura programado en lote previo, sin URL/ID en ese registro. | `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR` |
| `2026-11-06_kids-ballena-azul-corazon` | 11-nov 07:00: YouTube `wbFrlM2e_YE` público; TikTok `7705594333574991122` publicado; Facebook figura programado en lote previo, sin URL/ID en esta pasada. | `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR` |
| `2026-11-07_comida-hielo-caliente` | 11-nov 13:30: YouTube `HSgrnejAcaI` privado con publishAt `2026-11-11T19:30:00Z`; TikTok `7706905447424347393` programado; Facebook programado y con estado «En proceso…». | `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR` |

Los registros de los cinco remiten a medios en rutas `/workspace/...` que no están presentes en el árbol GitHub: **`MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`**. No se afirma que esos archivos existan en GitHub. En los cuatro primeros, YouTube/TikTok figuran como publicados; el registro de Facebook varía entre publicado y programado. En hielo caliente, YouTube sigue descrito como privado/programado y Facebook no tiene confirmación final en el registro. No se borró, canceló ni reprogramó nada.

Los otros siete proyectos del lote no muestran en los horarios diarios consultados evidencia de publicación o programación ni directorios de salida en el árbol de esta rama. Esto no equivale a una prueba de que nunca se hayan procesado fuera del repositorio; simplemente no hay evidencia verificable aquí.

## 5. Cola, recepción y dispatchabilidad

### 5.1 Día actual

No existe ningún archivo con fecha objetivo 2026-11-11 en `proyectos/`, `cola/entrada/`, `salidas/` o `cola/bloqueados/`. Por tanto, el inventario del día es **0 proyectos / 0 entradas de cola**. No se creó storyboard ni copia de cola.

### 5.2 Lote 5–7

Los 12 borradores están en `proyectos/<project_id>/storyboard.json`, no en `cola/entrada/`: los doce quedan **NOT_DISPATCHABLE**. Además, todos los estados `cola/estado/<project_id>.json` devolvieron 404; para cada uno el resultado es exactamente **`RECEPCION_GROK_NO_CONFIRMADA`**. No se atribuye recepción, selección, producción, QA audiovisual ni publicación a Grok por la presencia de los borradores.

No hay copias de esos 12 IDs en `cola/entrada/`; no se necesitó mover ninguna a bloqueados. Las variantes históricas en `cola/bloqueados/` se mantienen separadas de los IDs canónicos y no se trataron como proyectos adicionales.

### 5.3 Workflow y paquete histórico ASTRA

`.github/workflows/capcot-grok-dispatch.yml`:

- Push trigger: `cola/entrada/*.json`.
- Selector de push: regex `^cola/entrada/[^/]+\.json$`.
- Manual `all`: `find cola/entrada -maxdepth 1 -type f -name '*.json'`.
- Manual por ID: `cola/entrada/${PROJECT_ID}.json`.

El workflow solo selecciona JSON planos en el primer nivel. `scripts/procesar_cola.py`, en cambio, acepta tanto `cola/entrada/<id>.json` como `cola/entrada/<id>/storyboard.json`. Esa diferencia deja paquetes anidados procesables por el script, pero no despachables por este workflow.

Fuera del lote y del día actual, el paquete ASTRA `2026-11-09_dato-robot-ensambla-orbita` permanece anidado en `cola/entrada/2026-11-09_dato-robot-ensambla-orbita/storyboard.json`: **NOT_DISPATCHABLE** por la ruta. Su marcador `handoffs/grok_inbox/2026-11-09_dato-robot-ensambla-orbita.json` conserva `status=pending`, no un acuse de Grok. `cola/estado/2026-11-09_dato-robot-ensambla-orbita.json` devuelve 404. La carpeta `frames/` contiene solo `.gitkeep`; no hay PNGs. No se atribuye recepción ni producción.

### 5.4 Procesador y selector por fecha

`scripts/procesar_cola.py` calcula por defecto la fecha local de CDMX y filtra las entradas por los primeros diez caracteres del nombre del JSON o de la carpeta que contiene `storyboard.json`. No consume automáticamente las colas históricas cuando no hay entrada para la fecha solicitada. **Matiz:** el argumento `--fecha` puede sobrescribir la fecha actual; por tanto, el script filtra por la fecha indicada, no está codificado para rechazar cualquier fecha histórica introducida manualmente.

## 6. Rotación y registro editorial

Los registros `data/` no cubren el lote reciente: `temas_del_dia.json` llega a 28-oct; `estilos_usados.json` llega a 28-oct; `rotacion.json` y `publicaciones.json` llegan a 31-oct; `cola.json` contiene solo un registro del 31-oct. Se contrastaron con los 12 storyboards y con los horarios diarios 8–11 nov; no se usaron como única fuente.

`scripts/registro_editorial.py` combina `rotacion.json`, `publicaciones.json`, `cola.json` y storyboards de `proyectos/`, `cola/entrada/`, `cola/` y `salidas/`. No incorpora los horarios diarios ni recorre `cola/bloqueados/`; por sí solo puede omitir evidencia de programación/publicación y variantes bloqueadas. Además, cuando un storyboard bajo `proyectos/` no declara `origen`, el script le asigna por defecto `propia`, aunque el Contrato Operativo clasifica los paquetes textuales de ChatGPT como externos. Esto puede distorsionar el desglose por origen/cupo. No se modificó el script ni los JSON de datos.

### 6.1 Plantilla heredada contradictoria

`templates/storyboard.template.json` sigue presente y propone 120 s, 16:9 y campos de assets/rutas. Eso contradice la Receta y la plantilla vigente `templates/storyboard_vertical.template.json` (9:16, 75–90 s, 6 s de cortinilla y sin assets en preproducción). La receta apunta a la plantilla vertical; la plantilla antigua no se usó ni se modificó. Conviene tratarla como legado hasta que el responsable documental decida archivarla.

## 7. Actions, runtime y APIs

- Se leyó el workflow, pero no se pudieron enumerar las últimas ejecuciones ni descargar logs: el endpoint de listado de Actions no está habilitado por el conector disponible (respuesta literal: `HTTP 400: GitHub Fetch URL is not an allowed public GitHub repository or search endpoint.`). No hay un error literal de ejecución que pueda atribuirse a un run actual. No se pudo verificar si existen `GROK_WEBHOOK_URL` y `GROK_WEBHOOK_TOKEN`; no se consultaron ni expusieron valores.
- No había checkout/runtime local del repositorio para ejecutar `validar_storyboard.py`, helpers o `--check-doi`. Se hizo revisión estática del código del validador y de los JSON; no se declara ejecución del validador ni verificación HTTP nueva de Crossref.
- No se abrió una revisión API adicional: el radar del 11-nov ya registra el cambio de Graph API que motivó su actualización; en esta auditoría no se presentó otra evidencia oficial nueva que justificara modificar documentación API.

## 8. Cambios de esta auditoría

- Se releyeron las 12 narraciones en frío y se actualizó únicamente `narrative_qa.reviewed_at` en los 12 storyboards a `2026-11-11T15:25:07-06:00`. Los scores, statuses, checks, flags, narraciones, claims, fuentes y decisiones editoriales se conservaron.
- Los 12 JSON se volvieron a leer desde GitHub. Los valores de la sección 3 coinciden con esos archivos.
- Se creó este control de cola. No se promovió ningún paquete, no se movió ni eliminó contenido, no se creó/actualizó ningún estado Grok, no se modificó `data/*.json`, el workflow, los secretos, los permisos ni `main`; no hubo merge, producción, generación de medios, publicación o gasto de créditos.

**Estado:** lote 5–7 abierto. Ninguno de los 12 está autorizado para promoción. Los cinco con evidencia de programación/publicación quedan protegidos contra redispatch.
