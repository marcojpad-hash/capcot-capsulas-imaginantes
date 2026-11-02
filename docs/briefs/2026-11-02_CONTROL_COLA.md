# Control de cola CAPCOT — 2 de noviembre de 2026

**Repositorio:** `marcojpad-hash/capcot-capsulas-imaginantes`  
**Rama:** `feature/capcot-video-discovery-continuity`  
**Alcance:** auditoría de los cinco slots del 2 de noviembre y continuidad de agenda/cola del 5 al 7 de noviembre; revisión estática de GitHub, workflows, Actions, logs, storyboards y estados. No se ejecutó producción ni se enviaron paquetes.

## Resultado ejecutivo

**Estado general: NO DISPATCHABLE**

- `cola/entrada/` contiene únicamente `.gitkeep`: **0 paquetes listos para despacho**.
- `cola/estado/` no existe: **recepción por Grok no confirmada para todos los proyectos revisados**.
- No hay borradores de estas fechas en `proyectos/`; las copias encontradas están en `cola/bloqueados/`.
- La agenda vigente tiene 12 slots de contenido para el 5–7 nov (07:00, 13:30, 17:00 y 17:45) más tres slots 23:30 `TBD-news`. Los IDs programados ya no coinciden con varios nombres de paquetes bloqueados; ver tabla corregida.
- Los 12 project_id del 5–7 tienen copias JSON directas bloqueadas. Además hay 10 copias `<project_id>/storyboard.json`; esto crea representaciones duplicadas del mismo material. En nubes hay dos versiones de carpeta/JSON con el mismo project_id; deben reconciliarse antes de cualquier QA o handoff.
- Las 10 copias de carpeta revisadas tienen 7 escenas y no contienen `narrative_qa`. Los 13 JSON directos revisados también tienen 7 escenas y no contienen `narrative_qa`. El validador exige un QA independiente PASS antes del handoff.
- No hay frames, audio, assets aprobados ni render acreditado en los storyboards revisados.

## Inventario de agenda 5–7 nov y reconciliación con bloqueados

No hay borradores de estas fechas en `proyectos/` ni entradas activas en `cola/entrada/`. La agenda actual de `data/horario_semana_2026-11-01_07.json` cambió varios IDs respecto de los paquetes archivados en `cola/bloqueados/`.

| Fecha / slot vigente | project_id en agenda | Paquete bloqueado encontrado | Reconciliación |
|---|---|---|---|
| 5-nov 07:00 | `2026-11-05_kids-dia-en-venus` | `2026-11-05_inter-venus-dia-largo` (JSON + carpeta) | ID distinto; no asumir equivalencia |
| 5-nov 13:30 | `2026-11-05_comida-palomitas` | `2026-11-05_comida-palomitas-explotan` (JSON + carpeta) | ID distinto |
| 5-nov 17:00 | `2026-11-05_inter-arboles-se-comunican` | `2026-11-05_inter-arboles-mito-respiran` (JSON + carpeta) | ID distinto |
| 5-nov 17:45 | `2026-11-05_inter-rayo-globular` | `2026-11-05_inter-rayo-globular` (JSON) | Coincide |
| 6-nov 07:00 | `2026-11-06_kids-ballena-azul-corazon` | `2026-11-06_inter-corazon-ballena-azul` (JSON + carpeta) | ID distinto |
| 6-nov 13:30 | `2026-11-06_comida-aguacate-negro` | `2026-11-06_comida-aguacate-negro` (JSON + carpeta) | Coincide |
| 6-nov 17:00 | `2026-11-06_inter-ranas-congeladas` | `2026-11-06_inter-ranas-congeladas` (JSON + carpeta) | Coincide |
| 6-nov 17:45 | `2026-11-06_inter-arena-cantante` | `2026-11-06_inter-arena-cantante` (JSON) | Coincide |
| 7-nov 07:00 | `2026-11-07_kids-huesos-bebe` | `2026-11-07_kids-huesos-bebe` (JSON + carpeta) | Coincide |
| 7-nov 13:30 | `2026-11-07_comida-hielo-caliente` | `2026-11-07_inter-mpemba-mito` (JSON + carpeta) | ID distinto |
| 7-nov 17:00 | `2026-11-07_inter-pulpo-suenos` | `2026-11-07_inter-suenos-pulpo` (JSON + carpeta) | ID distinto |
| 7-nov 17:45 | `2026-11-07_inter-nubes-pesan` | `2026-11-07_inter-nubes-pesan.json` y carpeta `2026-11-07_extra-nubes-pesan/` | Coincide un JSON; carpeta duplicada con otro ID |

Los tres slots 23:30 (5, 6 y 7-nov) permanecen como `dato-TBD-news`, sin storyboard ni paquete. No se creó ni renombró ningún paquete para resolver las diferencias. La revisión de este corte comparó rutas/IDs; no volvió a ejecutar QA narrativo de los 5–7 nov.
## Contrato de handoff: corrección de jerarquía

La instrucción semanal del 31-oct pide carpetas `cola/entrada/<project_id>/` con tres archivos. Sin embargo, el contrato operativo unificado vigente desde 1-nov tiene mayor jerarquía y define:
1. Borrador en `proyectos/<project_id>/storyboard.json`.
2. QA narrativo independiente PASS.
3. Promoción a `cola/entrada/<project_id>.json` (JSON de primer nivel).

Corrección técnica: el workflow solo admite JSON de primer nivel; `scripts/procesar_cola.py` admite tanto `cola/entrada/<id>.json` como `cola/entrada/<id>/storyboard.json`. La incompatibilidad de profundidad está en el workflow, no en el procesador. No se modifica el workflow. Los tres informes RADAR del 5–7 ya recibieron una nota de estado; esta auditoría aclara que la incompatibilidad está en la instrucción semanal heredada, no en el contrato vigente ni en el workflow.

## Dispatch: evidencia de Actions

Última ejecución visible del workflow: run `41306776689`, 1-nov-2026 12:29:58Z, conclusión FAILURE.
- Paso de resolución/validación: SUCCESS; detectó y validó un JSON.
- Paso de configuración del receptor: FAILURE.
- Error literal: `Falta configurar GROK_WEBHOOK_URL.`
- El log muestra `WEBHOOK_URL` vacío y `WEBHOOK_TOKEN` vacío en esa ejecución.
- El paso de entrega y acuse quedó SKIPPED. No hubo POST ni `receipt_id`.

La API de GitHub disponible no permite leer los valores actuales de secretos. Por tanto, el estado actual de esos secretos no se puede certificar desde aquí; la última ejecución sí acredita que estaban vacíos el 1-nov.

## Compuertas pendientes

1. Restaurar una sola copia canónica por project_id; resolver específicamente la duplicación de nubes.
2. Colocar los borradores vigentes en `proyectos/` (sin promoverlos todavía).
3. Revisión narrativa independiente en frío y registro real de `narrative_qa`; no se puede inventar PASS. Los borradores observados no tienen ese campo.
4. Ejecutar el validador estructural después de cualquier corrección del redactor. Esta auditoría fue estática; no se declara ejecución local del validador.
5. Solo después de PASS y validación, promover JSON de primer nivel a `cola/entrada/`.
6. Configurar por el propietario del repositorio los secretos de Actions `GROK_WEBHOOK_URL` (HTTPS) y `GROK_WEBHOOK_TOKEN`; no se pueden crear ni leer desde esta integración.
7. Ejecutar dispatch y comprobar acuse individual `accepted=true` + `receipt_id`; después esperar el archivo de estado que solo Grok puede crear.

## Conclusión

La causa inmediata que impide generación es doble: **no hay ningún paquete en la cola activa** y **el último dispatch falló antes de llamar al receptor por falta de configuración del webhook**. Aun colocando archivos en cola, no deben enviarse hasta superar el QA narrativo independiente y la validación estructural. No se declara generación ni recepción de Grok.

## Auditoría del 2 de noviembre — fecha objetivo

### Inventario completo del día

Se contaron los slots de `data/horario_semana_2026-11-01_07.json`, no solo los IDs que empiezan por 2026-11-02. Hay cuatro proyectos con salida y programación preexistente, más un slot de noticia sin paquete.

| Slot CDMX | project_id | Fecha del ID / creación observada | Paquete y estado |
|---|---|---|---|
| 07:00 | `2026-11-02_camaron-mantis` | ID objetivo 2-nov; el estado atribuye la carga inicial al commit de Grok Bot del 31-oct | `proyectos/`, `cola/bloqueados/<id>/` y `salidas/`; **PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR** |
| 13:30 | `2026-11-02_comida-pan-duro` | ID objetivo 2-nov; el estado atribuye la carga inicial al mismo commit de Grok Bot del 31-oct | `proyectos/`, `cola/bloqueados/<id>/` y `salidas/`; **PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR** |
| 17:00 | `2026-10-31_murcielagos-viroma-global` | ID 31-oct; objetivo 2-nov según agenda | `proyectos/`, JSON en `cola/bloqueados/` y `salidas/`; **PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR** |
| 19:00 | `2026-10-31_sequias-energia-renovable` | ID 31-oct; objetivo 2-nov según agenda | `proyectos/`, JSON en `cola/bloqueados/` y `salidas/`; **PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR** |
| 23:30 | `2026-11-02_dato-TBD-news` | Objetivo 2-nov | `pendiente_dato_dia`; no hay storyboard, entrada de cola ni salida |

Los dos proyectos 10/31 tienen fecha de ID anterior, pero la agenda los asigna explícitamente al 2-nov. Se incluyen por fecha objetivo, no se excluyen por el prefijo del ID.

### QA narrativo independiente en frío

Se ocultaron título, resumen, arco y notas. La lectura se hizo sobre la narración concatenada, sin usar el contrato narrativo. Se registró `narrative_qa` en los borradores de `proyectos/` y en los dos JSON candidatos de `cola/bloqueados/` que contienen una versión distinta.

| Versión revisada | Palabras | Status / score | Hallazgo principal |
|---|---:|---|---|
| `2026-11-02_camaron-mantis` (proyectos y copia bloqueada) | 223 | **PASS / 90** | Apertura en acción, mecanismo de cavitación, límite por especie/condiciones y payoff coherente |
| `2026-11-02_comida-pan-duro` (proyectos y copia bloqueada) | 230 | **FAIL / 84** | El cierre afirma «no está seco» y contradice el matiz previo de que la pérdida de humedad también interviene |
| `2026-10-31_murcielagos-viroma-global` (proyectos/salida, versión larga) | 228 | **FAIL / 72** | Apertura estática con escenario no documentado; transiciones genéricas; cifra de 300,000 sin unidad de análisis clara; giro comparativo no explicado |
| `2026-10-31_murcielagos-viroma-global` (JSON bloqueado, versión corta) | 131 | **FAIL / 80** | Pregunta genérica de apertura; el resultado comparativo se nombra, pero no se explica; «unidades virales» queda sin definición |
| `2026-10-31_sequias-energia-renovable` (proyectos/salida, versión larga) | 205 | **FAIL / 56** | Apertura definicional; porcentajes sin dirección interpretable; giro solar solo nombrado; cierre de almacenamiento no derivado del estudio |
| `2026-10-31_sequias-energia-renovable` (JSON bloqueado, versión corta) | 152 | **FAIL / 54** | Mismo patrón de ficha de datos: apertura definicional, cifras sin dirección, giro sin explicación y payoff no derivado |

Los scores/statuses anteriores se releen del JSON actualizado; no se infieren de `qa.json`. La versión larga de murciélagos en `proyectos/` no coincide con el JSON bloqueado; tampoco coincide la versión larga de sequías con el JSON bloqueado. Son versiones diferentes del mismo `project_id`, no se fusionaron ni se reescribieron.

### Compuerta estructural y handoff

- Camarón mantis: 8 escenas, 223 palabras, 78 s de escenas + 6 s de cortinilla = 84 s, gancho de 5 palabras, voz y `prompt_base` correctos, DOI/source_ids presentes. **FAIL estructural**: falta `narrative_contract`; faltan los seis campos narrativos en las ocho escenas; mapa con cero puntos. Se retiraron mecánicamente los ocho placeholders `asset_filename`/`asset_type` del borrador y de la copia bloqueada. `approved_assets=[]` y `export.render_status=NOT_GENERATED` están correctos; el snapshot de `salidas/` conserva referencias históricas no verificadas.
- Pan duro: 8 escenas, 230 palabras, 84 s, gancho de 6 palabras, voz, DOI/source_ids y prompt base presentes. **FAIL estructural**: falta `narrative_contract`; faltan los seis campos narrativos en las ocho escenas; mapa sin puntos y rotulado «Hábitat marino»; falta `ambiente` en las ocho escenas (solo existe texto descriptivo de ambiente). Se retiraron mecánicamente los ocho placeholders `asset_filename`/`asset_type` del borrador y de la copia bloqueada. `approved_assets=[]` y `render_status=NOT_GENERATED` están correctos; el snapshot de `salidas/` conserva referencias históricas no verificadas.
- JSON bloqueado de murciélagos: 8 escenas, 131 palabras, 84 s, gancho de 4 palabras; **FAIL estructural** por 170–235 palabras, falta de `narrative_contract` y campos narrativos, y ausencia de mapa/dato-gráfico. No declara assets y conserva `approved_assets=[]` / `NOT_GENERATED`.
- JSON bloqueado de sequías: 8 escenas, 152 palabras, 84 s, gancho de 4 palabras; **FAIL estructural** por 170–235 palabras, falta de `narrative_contract` y campos narrativos, y ausencia de mapa/dato-gráfico. No declara assets y conserva `approved_assets=[]` / `NOT_GENERATED`.
- Las versiones largas de murciélagos y sequías en `proyectos/` son snapshots de producción: incluyen `export.filename=capsula.mp4` y referencias de assets por escena, pero esos medios no están en el árbol; además, `voice.language` falta en ambos. No cumplen el contrato de preproducción actual.
- Las seis versiones revisadas tienen etiquetas de arco y cierre hablado exacto; eso no sustituye la historia ni el QA en frío. Ninguna versión se promovió. Camarón mantis tiene PASS narrativo, pero falla estructura y además ya tiene salida/publicación; las otras versiones fallan QA narrativo o estructura. No había copia en `cola/entrada/` que mover: las copias heredadas ya estaban en `cola/bloqueados/`.

### Recepción y dispatchabilidad

`cola/entrada/` contiene solo `.gitkeep`; no existe `cola/estado/`. Para los cuatro proyectos con storyboard, el resultado exacto es **RECEPCION_GROK_NO_CONFIRMADA**:

- `2026-11-02_camaron-mantis`
- `2026-11-02_comida-pan-duro`
- `2026-10-31_murcielagos-viroma-global`
- `2026-10-31_sequias-energia-renovable`

| project_id | Ruta encontrada | ¿DISPATCHABLE? | Evidencia |
|---|---|---|---|
| Camarón mantis | `proyectos/<id>/storyboard.json`, `cola/bloqueados/<id>/storyboard.json`, `salidas/<id>/` | **NOT_DISPATCHABLE** | No existe `cola/entrada/<id>.json`; ninguna ruta encontrada coincide con el selector del workflow |
| Pan duro | `proyectos/<id>/storyboard.json`, `cola/bloqueados/<id>/storyboard.json`, `salidas/<id>/` | **NOT_DISPATCHABLE** | Mismo motivo |
| Murciélagos | `proyectos/<id>/storyboard.json`, `cola/bloqueados/<id>.json`, `salidas/<id>/` | **NOT_DISPATCHABLE** | Mismo motivo; JSON bloqueado fuera de `cola/entrada/` |
| Sequías | `proyectos/<id>/storyboard.json`, `cola/bloqueados/<id>.json`, `salidas/<id>/` | **NOT_DISPATCHABLE** | Mismo motivo |

El workflow escucha `cola/entrada/*.json`; en `workflow_dispatch` usa `find cola/entrada -maxdepth 1 -type f -name '*.json'`. No encuentra carpetas de proyecto, subcarpetas, `cola/bloqueados/` ni `proyectos/`. No se disparó workflow ni se envió payload externo.

### Producción, QA audiovisual y publicación preexistentes

Las cuatro carpetas `salidas/<project_id>/` existen y contienen storyboard, `qa.json`, `publicacion.json` y metadata/licencias. Por ello se aplica **PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR**, aunque falte el acuse de estado de Grok.

| project_id | `qa.json` de `capsula.mp4` | Log M4 de `capsula_v4.mp4` | Lectura estricta 75–90 s |
|---|---:|---:|---|
| Camarón mantis | 75.35 s | 89.52 s | El primero entra; el segundo no tiene QA audiovisual propio |
| Pan duro | 74.33 s | 89.33 s | `qa.json` queda 0.67 s bajo el mínimo; M4 no sustituye QA |
| Murciélagos | 65.47 s | 90.33 s | Ambos fuera de rango; no hay QA específico de v4 |
| Sequías | 91.87 s | 88.83 s | QA de `capsula.mp4` fuera de rango; v4 solo tiene log, no QA |

Los `qa.json` locales aceptan 60–120 s, por lo que no prueban cumplimiento de 75–90 s. En los dos paquetes nuevos, `qa.json` cuenta 181/186 palabras frente a 223/230 en los storyboards. En murciélagos, el QA cuenta 131 palabras y coincide con el JSON bloqueado, no con la versión larga de `proyectos/`; en sequías cuenta 216, que no coincide ni con 205 ni con 152. No se puede certificar que QA, audio y storyboard sean la misma versión.

El árbol GitHub no contiene los MP4, frames ni audio referenciados por metadata, publicación y logs. Los registros de bytes/rutas y los logs no son archivos verificables. Se marca **MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO** para los cuatro proyectos.

### IDs de YouTube, horarios y riesgo de duplicado

Los snapshots de `publicacion.json` registran:

- Camarón mantis: ID actual `5sxxx0vuXFE`; `privacyStatus=private`; `publishAt=2026-11-02T13:00:00Z` (07:00 CDMX). Historial aún describe `tmxMkxA6nOw` y `d-tYvAM8hGE` como programados.
- Pan duro: ID actual `V9bO9EUN0JA`; `privacyStatus=private`; `publishAt=2026-11-02T19:30:00Z` (13:30 CDMX). Historial aún describe `TbZRvpiDjdk` y `sHjf4QF9QiM` como programados.
- Murciélagos: ID actual `c-7pMF3-B-g`; privado con `publishAt=2026-11-02T23:00:00Z` (17:00 CDMX). Historial aún describe `dFwKjIb8tFI` y `6ts8TvhgKa8` como programados.
- Sequías: ID actual `OwfxfQ4RPSo`; privado con `publishAt=2026-11-03T01:00:00Z` (19:00 CDMX). Historial aún describe `SQ7_g-vz8Ow`, `pMkzlwB-7bo` y `-HfaDUCg4OE` como programados.

Los IDs antiguos representan riesgo de duplicado. No se borró ni canceló nada. El snapshot de `publicacion.json` mantiene privacidad `private`; `data/endscreens_rotacion.json` actualizado 14:55 CDMX registra 65 vistas para camarón y 1 para pan. Esa diferencia no permite declarar estado público: el snapshot de publicación sigue discrepando y no se consultó Studio en esta auditoría.

En TikTok/Facebook, los objetos internos `reemplazo_v4` conservan estados `pendiente_ui` en algunos registros mientras el objeto superior y `data/reprogramacion_tt_fb_v4_2026-11-01_03.json` dicen `programado_v4`/viejo borrado. Se registra discrepancia; no se modificó ninguna programación.

### Reconciliación de datos, procedencia y rotación

- `data/horario_semana_2026-11-01_07.json` programa los cuatro slots del 2-nov y conserva el slot 23:30 como TBD.
- La nota del slot de camarón apunta a `proyectos/2026-xx_kids_camaron-mantis-punetazo`, ruta que no existe; el ID real es `2026-11-02_camaron-mantis`. La misma nota afirma entrega por ChatGPT y estado `PREPARADO_PENDIENTE_REVISION_GROK`, pero `ESTADO_EJECUCION.md` atribuye la carga inicial a Grok Bot (commit `c83c35814499ae0a73443beb4d02d84e0e62c144`) y el estado vigente es `BORRADOR_EN_PROYECTOS_NO_APTO_PARA_PROMOCION`. No se atribuye el paquete a la automatización investigadora.
- La nota de pan conserva `PENDING_SOURCE exacta`, aunque `fuentes.md` y `sources[]` contienen DOI y la verificación declarada. El campo `trend_source.fecha_publicacion` estaba en 2005-10-01 frente a 2003-01 en la fuente; se corrigió a `2003-01` en `proyectos/` y en la copia bloqueada. No se modificó `data/horario_semana` ni el snapshot de `salidas/`.
- Las notas de murciélagos/sequías dicen «Cola JSON ChatGPT 31-oct», pero no se encontró evidencia de commit que permita atribuir esas copias a la automatización investigadora.
- `data/rotacion.json` llega a 31-oct; `data/estilos_usados.json` y `data/temas_del_dia.json` llegan a 28-oct; `data/publicaciones.json` llega a 31-oct; `data/cola.json` solo conserva una entrada fallida de 31-oct. No contienen un registro canónico completo del 2-nov.
- La última salida programada del 1-nov 19:00 usa `crayones_infantiles`; el 2-nov se asignan `teatro_sombras` y `papel_rasgado_capas`, sin repetición inmediata observada. La secuencia no puede certificarse desde `data/rotacion.json`/ `data/estilos_usados.json` porque están desactualizados. Los estilos están en el catálogo; el ajuste temático de papel rasgado para pan es débil frente a los temas declarados del estilo.
- `scripts/registro_editorial.py` une rotación/publicaciones/cola y storyboards de proyectos, entrada y salidas, pero no incluye ningún contenido de `cola/bloqueados/` (ni JSON directo ni subcarpeta) y no lee los `publicacion.json` de salidas para IDs/plataformas. No es una reconciliación completa.
- `scripts/procesar_cola.py` usa por defecto la fecha local CDMX y filtra por fecha extraída del nombre/ID. Sin embargo, permite pasar `--fecha` explícita; no existe una prohibición dura de seleccionar una fecha histórica si alguien fuerza ese argumento.


### APIs

El documento técnico de Meta/Google Trends tiene corte 31-oct-2026. No se encontró en el repositorio un cambio oficial posterior que justifique reabrir la investigación; por la regla de alcance, no se hizo una nueva búsqueda de APIs. La integración sigue condicionada a OAuth/credenciales del titular y Google Trends API continúa documentada como alfa limitada.


### Actions y configuración de receptor

No hay ejecución de `capcot-grok-dispatch.yml` el 2-nov. La última visible es el run `41306776689` del 1-nov-2026 12:29:58Z. La resolución/validación detectó un JSON; la verificación del receptor falló con el error literal:

`Falta configurar GROK_WEBHOOK_URL.`

El workflow requiere `GROK_WEBHOOK_URL` y `GROK_WEBHOOK_TOKEN`; no se muestran ni se modifican valores. El paso de entrega quedó SKIPPED: no hubo POST ni `receipt_id`.

### Cambios realizados en esta auditoría

1. Se añadió `narrative_qa` a ocho JSON de borrador/copia bloqueada; los scores/statuses son los de la tabla de QA narrativo. Se retiraron los placeholders de assets de los dos paquetes del 2-nov, sin tocar los snapshots de `salidas/`.
2. Se corrigió `trend_source.fecha_publicacion` del pan a `2003-01` en `proyectos/` y `cola/bloqueados/`; no se tocó el snapshot de salida ni `data/*.json`.
3. Se actualizaron los dos `ESTADO_EJECUCION.md` de proyectos 2-nov con QA y fallos estructurales.
4. Se corrigieron los dos estados de las copias bloqueadas de `PREPARADO_PENDIENTE_REVISION_GROK` a `BORRADOR_EN_PROYECTOS_NO_APTO_PARA_PROMOCION`; también se retiró la atribución no demostrada a ChatGPT y se anotó la QA/publicación preexistente sin adjudicarla a esa copia.
5. Se alineó `docs/GUIA_MODELO_EXTERNO.md` con la secuencia proyectos → QA independiente → promoción.
6. Se corrigió este informe: los slots 5–7 se reubicaron de 19:00 a 17:45 y se separó el comportamiento del workflow del procesador.

No se modificaron `data/*.json`, workflows, secretos, permisos, estados de Grok ni salidas de producción. No se ejecutó el validador Python ni `registro_editorial.py`: no había runtime del repositorio en esta auditoría; la comprobación fue estática. No se generaron medios, no se publicaron contenidos, no se enviaron payloads, no se dispararon Actions y no se consumieron créditos.

