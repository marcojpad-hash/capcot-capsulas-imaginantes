# CONTROL DE COLA CAPCOT — 2026-11-01

**Corte:** 2026-11-01 19:08 CDMX.  
**Rama:** `feature/capcot-video-discovery-continuity`.  
**HEAD previo al informe:** `4ac34e3b31d1ed4dbbb1091d4980911a04183dea`.  
**Método:** lectura GitHub, comparación de rutas/estados/logs y revisión estática. Sin checkout ni runtime local.

## Dictamen

**HANDOFF BLOQUEADO.** Hay cuatro borradores en `proyectos/`, cero JSON activos en `cola/entrada/`, dos carpetas históricas bloqueadas y cinco slots ordinarios en el horario más una pieza extra de madrugada. El slot 23:30 sigue registrado como `dato-TBD-news`, aunque existe un brief específico para `2026-11-01_dato-cambio-horario-corazon`.

- QA narrativo: pulpo **FAIL 72**, cebolla **FAIL 79**, red eléctrica **PASS 89**, dato del día **FAIL 84**.
- Ningún storyboard vigente tiene acuse de Grok. Para los siete IDs revisados: **RECEPCION_GROK_NO_CONFIRMADA**.
- No se creó entrada de cola ni se disparó Actions. El dato del día no se promueve porque falla la longitud obligatoria del cierre y además repite estilo con Baffin.
- No hay confirmación inequívoca de publicación pública: varios registros de YouTube dicen `privacyStatus=private` y `publishAt`, mientras `endscreens_rotacion.json` registra vistas y cambios de pantallas. Se conserva la discrepancia, sin declarar PUBLICADO.

## 1. Briefs y borradores en proyectos

Briefs leídos: Plan Maestro, Receta, Guía de modelo externo, Flujo Externo, contrato unificado, contrato de estado Grok, QA narrativo, continuidad audiovisual, catálogo, líneas temáticas, brief del dato del día, línea editorial §8–9 y protocolo de carga de Grok. Existe también el radar del 1-nov.

| Borrador | Creación comprobada por commit | Fecha objetivo / slot | QA frío | Estado / dispatch |
|---|---|---|---|---|
| `2026-11-01_pulpo-tres-corazones` | 31-oct 17:12 CDMX | 1-nov 07:00 | FAIL 72 | Bloqueado; NOT_DISPATCHABLE |
| `2026-11-01_llorar-cebolla-quimica` | 31-oct 17:12 CDMX | 1-nov 13:30 | FAIL 79 | Bloqueado; NOT_DISPATCHABLE |
| `2026-11-01_red-electrica-pulso-minuto` | 1-nov 14:36 CDMX | Sin slot en horario | PASS 89 | Propuesta no seleccionada; NOT_DISPATCHABLE |
| `2026-11-01_dato-cambio-horario-corazon` | 1-nov 17:54 CDMX | 1-nov 23:30 según brief; horario aún dice TBD | FAIL 84 | Borrador en proyectos; NOT_DISPATCHABLE |

### Dato del día — Sandhu 2014

Archivo: `proyectos/2026-11-01_dato-cambio-horario-corazon/storyboard.json`. Commit de QA y metadatos: `e4c4a11df1399357f9d0e6df953be89c26596461`.

- 8 escenas; 219 palabras por conteo léxico; 78 s de escenas + 6 s de cortinilla = **84 s**.
- Gancho de 4 palabras; voz `es-MX-JorgeNeural`, +7 %, -2 Hz, pausas continuas.
- Cinco fuentes; DOI principal `10.1136/openhrt-2013-000019` marcado como resuelto. Los source_ids existen. Se añadió como URL complementaria la referencia oficial de Transport Canada AIM 2026-1 para el cambio horario canadiense; NIST cubre EE. UU. y DOF/SENER cubren la excepción mexicana.
- Mapa, gráfico, prompt_base exacto de `art_deco_poster`, ambiente y SFX presentes.
- `approved_assets=[]`, `render.render_status=NOT_GENERATED`; sin `asset_filename`, `asset_type` ni rutas de medios.
- Narración: 1,290 caracteres, dentro del total requerido. Penúltima escena: 156 caracteres, dentro de 120–170. Última escena antes del sello: **101 caracteres**, por debajo del mínimo de 110.
- Lectura en frío independiente: los siete checks narrativos son true, pero score 84 y flag `CIERRE_PRESELLO_INFERIOR_A_110_CARACTERES`; por tanto **FAIL**. La narración no se reescribió. El QA está registrado en el storyboard.
- Se añadieron `created_at`, `fecha_objetivo`, `slot_local`, `timezone`, `prioridad` y `origen=externa` para separar creación, destino y procedencia.
- **No promover:** el QA falla y el estilo `art_deco_poster` ya está asignado a Baffin en el slot 17:00 del mismo día. No se cambió el estilo porque sería una decisión editorial.

### Otros borradores

**Pulpo:** 8 escenas, 228 palabras; el JSON declara 78 s de escenas + 12 s de cortinilla = 90 s, aunque su `ESTADO_EJECUCION.md` heredado decía 78+6=84. Faltan `narrative_contract`, campos causales por escena, mapa y dato/gráfico. Hay ocho `asset_filename` heredados sin archivos correspondientes en el árbol GitHub; SFX sin contenido explícito. QA frío FAIL 72. Su `ESTADO_EJECUCION.md` activo se corrigió a `QA_NARRATIVO_FAIL_NO_PROMOVER`; no se reescribió la narración.

**Cebolla:** 8 escenas, 231 palabras; 78+12=90 s en el JSON, frente a 78+6=84 en el estado heredado. Faltan `narrative_contract`, campos causales por escena, mapa y dato/gráfico. Hay ocho `asset_filename` sin archivos correspondientes en el árbol GitHub; SFX sin contenido explícito. QA frío FAIL 79. Su `ESTADO_EJECUCION.md` activo se corrigió a `QA_NARRATIVO_FAIL_NO_PROMOVER`; no se reescribió la narración.

Los dos proyectos ya tienen copias en `cola/bloqueados/<project_id>/`; no había copia activa que mover. Los snapshots bloqueados conservan los archivos heredados y aún no incorporan el campo `narrative_qa`; sus `ESTADO_EJECUCION.md` son históricos y todavía dicen `PENDIENTE_REVISION_GROK`. No se alteraron esos snapshots.

**Red eléctrica:** 8 escenas, 196 palabras, 78+6=84 s, título de cinco palabras, voz correcta, source_ids válidos, mapa/dato, ambiente/SFX, prompt_base exacto de `risografia`, sin rutas de medios, `approved_assets=[]`, `render_status=NOT_GENERATED`, QA PASS 89. El DOI `10.1038/s41560-026-02144-0` continúa `PENDIENTE`; no tiene slot en el horario y no aparece como selección. No se promueve.

## 2. Cola, estados y dispatchabilidad

Inventario de rutas:

- `cola/entrada/`: solo `.gitkeep`; cero JSON de primer nivel.
- `cola/entrada/<project_id>/storyboard.json`: cero carpetas/archivos.
- `cola/estado/`: sin archivos de estado.
- `cola/bloqueados/`: snapshots de pulpo y cebolla; no son entradas activas.
- Los cuatro borradores de `proyectos/` son **NOT_DISPATCHABLE** por ruta.

Para cada storyboard vigente y salida del día se consultó `cola/estado/<project_id>.json`; los siete devolvieron 404:

- `2026-11-01_dato-cambio-horario-corazon` — **RECEPCION_GROK_NO_CONFIRMADA**
- `2026-11-01_pulpo-tres-corazones` — **RECEPCION_GROK_NO_CONFIRMADA**
- `2026-11-01_llorar-cebolla-quimica` — **RECEPCION_GROK_NO_CONFIRMADA**
- `2026-11-01_red-electrica-pulso-minuto` — **RECEPCION_GROK_NO_CONFIRMADA**
- `2026-11-01_dato-xolo-mictlan` — **RECEPCION_GROK_NO_CONFIRMADA**
- `2026-10-26_baffin-bay-ice-shelf` — **RECEPCION_GROK_NO_CONFIRMADA**
- `2026-11-03_kids-tiburon-groenlandia` — **RECEPCION_GROK_NO_CONFIRMADA**

El workflow `.github/workflows/capcot-grok-dispatch.yml` escucha `cola/entrada/*.json` en la rama autorizada. El selector por push usa regex `^cola/entrada/[^/]+\.json$`; `workflow_dispatch all` usa `find -maxdepth 1`. Por tanto, solo un JSON raíz sería DISPATCHABLE. Una carpeta `cola/entrada/<id>/storyboard.json` y todos los proyectos/salidas/bloqueados son NOT_DISPATCHABLE. El workflow no filtra por fecha; un JSON histórico de primer nivel también podría dispararlo.

No se creó JSON raíz ni anidado. No se ejecutó `workflow_dispatch`, no se envió payload y no se modificaron workflows, secretos o permisos.

## 3. Paquetes de salida asociados a slots del 1-nov

| Paquete | Creación del storyboard | Slot objetivo | Evidencia / defectos |
|---|---|---:|---|
| Xolo Mictlán | 31-oct 23:44 CDMX | 03:00 extra | 7 escenas, 214 palabras, 77+12=89 s; sin QA; sin mapa ni dato/gráfico; 7 asset_filename; 5 escenas sin SFX. |
| Pulpo | 31-oct 17:12 CDMX | 07:00 | QA audiovisual local 61.80 s; el QA antiguo usa 60–120 s; falla mapa y dato/gráfico. |
| Cebolla | 31-oct 17:12 CDMX | 13:30 | QA audiovisual local 66.70 s; el QA antiguo usa 60–120 s; falla mapa y dato/gráfico. |
| Baffin | 31-oct 17:12 CDMX | 17:00 | Storyboard 9 escenas, 215 palabras, 81+6=87 s; QA local 20/21; render 91.93 s y 83 bloques de subtítulos superan tres palabras. |
| Tiburón de Groenlandia | 31-oct 17:12 CDMX | 19:00 | 8 escenas, 244 palabras (>235), 78+6=84 s; sin qa.json; 8 asset_filename; 7 escenas sin SFX. |
| Dato cambio horario/corazón | 1-nov 17:54 CDMX | 23:30 pendiente | Solo borrador; FAIL 84; no hay salida ni entrada de cola. |

Los `qa.json` locales no son QA oficial de Grok. Los renders de pulpo y cebolla (61.80 y 66.70 s) no cumplen el umbral vigente de 75–90 s. El QA de Baffin tampoco cumple duración renderizada ni subtítulos. Xolo y tiburón carecen de `qa.json`.

En los storyboards de salida hay referencias `asset_filename` y el estado `NOT_GENERATED`; no se hallaron los frames en el árbol GitHub. No se cuentan nombres de archivo ni placeholders como medios. Los registros de publicación contienen IDs de YouTube y horarios privados/programados, pero `endscreens_rotacion.json` actualizado a 17:52 registra vistas (Xolo 578, pulpo 263, cebolla 1, Baffin 4). Esa evidencia contradice los snapshots `privacyStatus=private`; sin lectura pública actual no se confirma PUBLICADO.

## 4. Reconciliación de tema, estilo y rotación

El horario `data/horario_semana_2026-11-01_07.json` declara `slots_por_dia=5`, pero tiene seis filas el 1-nov: Xolo 03:00, pulpo 07:00, cebolla 13:30, Baffin 17:00, tiburón 19:00 y dato 23:30. Xolo es un slot extra. El slot 23:30 conserva `2026-11-01_dato-TBD-news`; el brief diario identifica `2026-11-01_dato-cambio-horario-corazon`. No se sincronizó `data/*.json`.

Otros conflictos:

- `project_id_plan` no coincide con los IDs reales de pulpo y cebolla.
- `data/reprogramacion_tt_fb_v4_2026-11-01_03.json` mantiene arqueas en 19:00; el horario y `salidas/_ops/2026-11-01_swap_arqueas_tiburon.md` dicen tiburón. El `publicacion.json` del tiburón deja TT/FB como `pendiente_ui` para el slot 1-nov, mientras otro registro dice programado el 3-nov.
- Baffin conserva IDs de YouTube anteriores en `historial_youtube` con nota de borrado manual; la confirmación v4 de TT/FB no resuelve esa lista de YouTube.
- `data/temas_del_dia.json` llega a 28-oct; `rotacion.json` y `publicaciones.json` a 31-oct; `estilos_usados.json` tiene 21 registros hasta 28-oct. No permiten certificar por sí solos la rotación del 1-nov.
- `data/rotacion.json` duplica históricamente familia-ajolote, kids-serpiente-voladora y noct-anfibio-marino.
- `data/cola.json` conserva el fallo de pardelas del 31-oct (`rc=1`) con ruta que no aparece en el árbol actual.
- `data/endscreens_rotacion.json` sí está actualizado el 1-nov a las 17:52 CDMX.

Estilos de los paquetes actuales: Xolo `teatro_sombras`, pulpo `carton_recortado`, cebolla `papel_recortado_popup`, Baffin `art_deco_poster`, tiburón `crayones_infantiles`, dato del día `art_deco_poster`, red eléctrica `risografia`. El dato del día repite el estilo de Baffin del slot 17:00. La falta de actualización de `estilos_usados.json` impide que el registro de rotación lo detecte.

### Procesador y registro editorial

- `scripts/procesar_cola.py` usa la fecha CDMX actual por defecto, pero acepta `--fecha` explícita de cualquier día. Filtra por prefijo de archivo/directorio, no por `fecha_objetivo` interna. No es una garantía absoluta de “solo hoy” si se pasa una fecha distinta.
- El procesador admite JSON raíz y carpeta anidada de un nivel; el workflow solo despacha JSON raíz.
- `scripts/registro_editorial.py` obtiene fecha del prefijo de `project_id`, no de fecha objetivo/slot; no lee `data/horario_semana` ni `cola/bloqueados`. Así clasifica Baffin como 26-oct y tiburón como 3-nov aunque ambos ocupen slots el 1-nov, y omite snapshots bloqueados.
- Los proyectos sin `origen` reciben el valor por defecto `propia`; eso puede contar mal el cupo propio/externo. El dato nuevo declara `origen=externa`; no se inventó origen para los demás.

## 5. Contradicciones documentales

La precedencia del contrato unificado, Plan Maestro, Receta y Flujo resuelve estas divergencias, pero los documentos inferiores siguen sin sincronizar:

1. `docs/FLUJO_EXTERNO.md` y Plan Maestro exigen staging en `proyectos/` y promoción por auditor independiente. `docs/GUIA_MODELO_EXTERNO.md` todavía indica crear directamente `cola/entrada/YYYY-MM-DD_slug.json`.
2. El brief permanente `PARA_CHATGPT_dato_del_dia.md` indica carpeta anidada en `cola/entrada/`, `fuentes.md` y `ESTADO_EJECUCION.md` preparado. El flujo vigente exige primero `proyectos/`, QA PASS y promoción por auditor; Grok es el único que crea `cola/estado/`. No se crearon los archivos pedidos por la instrucción heredada.
3. `PARA_CHATGPT_LINEA_EDITORIAL.md` conserva 75–95 s y 200–235 palabras; Receta/Plan vigentes fijan 75–90 s y 170–235. El brief del dato exige 205–235 y 1,100–1,300 caracteres; se aplicó ese rango específico al dato.
4. `docs/BIBLIA_LINEA_EDITORIAL.md` conserva un cupo de 2–3 al día; Plan/Contrato y código vigente fijan cinco como máximo.
5. `templates/storyboard.template.json` es un esquema legado con 120 s; la plantilla vertical canónica es `templates/storyboard_vertical.template.json`.
6. Pulpo y cebolla conservan `fuentes.md` y `ESTADO_EJECUCION.md` heredados. Sus estados de proyecto se actualizaron a `QA_NARRATIVO_FAIL_NO_PROMOVER`; los snapshots bloqueados no se reescribieron. Los JSON originales aún tienen referencias de assets no encontradas en GitHub y la cortinilla declarada de 12 s; se documenta, no se reescribe el historial.

## 6. Actions y receptor

El workflow tiene 147 ejecuciones acumuladas; las 30 más recientes consultadas terminaron en failure. Los cinco logs más recientes contienen literalmente:

`::error::Falta configurar GROK_WEBHOOK_URL.`

El paso se detiene en la comprobación de URL antes de comprobar `GROK_WEBHOOK_TOKEN`; no se puede afirmar que el token falte. No se expusieron valores. No hay ejecución asociada a los commits de esta auditoría: ninguno tocó `cola/entrada/*.json`.

## 7. Cambios realizados y límites

1. Dato del día: añadidos fecha de creación, fecha objetivo, slot, zona horaria, prioridad y origen externo; ampliada la cobertura de fuente oficial canadiense; registrado QA frío **FAIL 84** en commit `e4c4a11df1399357f9d0e6df953be89c26596461`. Narración intacta.
2. Pulpo y cebolla: sus `ESTADO_EJECUCION.md` activos se actualizaron a `QA_NARRATIVO_FAIL_NO_PROMOVER` para no presentarlos como preparados. Commits `adf18920dfa53a6edf4b9c1936fe480465ca81b0` y `4ac34e3b31d1ed4dbbb1091d4980911a04183dea`.
3. No se modificaron `data/*.json`, `main`, estados de Grok, workflow, secretos, permisos ni decisiones editoriales. No hubo merge. No se crearon entradas de cola ni estados. No se generaron medios, no se publicó ni se consumieron créditos.
4. Revisión estática solamente; no se ejecutaron Python, validador ni helpers por falta de checkout/runtime local.
5. No se abrió revisión de APIs: no se identificó un cambio oficial nuevo que activara esa condición.

## Estado final

- Pulpo: **FAIL 72; bloqueado; no promover**.
- Cebolla: **FAIL 79; bloqueado; no promover**.
- Red eléctrica: **PASS 89; propuesta no seleccionada, DOI pendiente, sin slot; no promover**.
- Dato cambio horario/corazón: **FAIL 84; cierre 101/110–170 caracteres; estilo duplicado; slot no reconciliado; no promover**.
- Cola activa: **vacía**.
- Recepción Grok: **no confirmada para los siete IDs listados**.
- Publicación pública: **no confirmada de forma inequívoca**.
