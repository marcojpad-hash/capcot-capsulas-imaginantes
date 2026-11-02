# Control de cola CAPCOT — 2 de noviembre de 2026

**Repositorio:** `marcojpad-hash/capcot-capsulas-imaginantes`  
**Rama:** `feature/capcot-video-discovery-continuity`  
**Alcance:** slots del 5 al 7 de noviembre; auditoría estática de GitHub y lectura de workflow/logs. No se ejecutó producción ni se enviaron paquetes.

## Resultado ejecutivo

<badge>NO DISPATCHABLE</badge>

- `cola/entrada/` contiene únicamente `.gitkeep`: **0 paquetes listos para despacho**.
- `cola/estado/` no existe: **recepción por Grok no confirmada para todos los proyectos revisados**.
- No hay borradores de estas fechas en `proyectos/`; las copias encontradas están en `cola/bloqueados/`.
- Hay 12 project_id para los 12 slots del 5–7 nov. Hay 13 JSON directos bloqueados si se cuenta el paquete de Machu Picchu del 4-nov, que no debe tocarse sin autorización.
- Los 12 project_id del 5–7 tienen copias JSON directas bloqueadas. Además hay 10 copias `<project_id>/storyboard.json`; esto crea representaciones duplicadas del mismo material. En nubes hay dos versiones de carpeta/JSON con el mismo project_id; deben reconciliarse antes de cualquier QA o handoff.
- Las 10 copias de carpeta revisadas tienen 7 escenas y no contienen `narrative_qa`. Los 13 JSON directos revisados también tienen 7 escenas y no contienen `narrative_qa`. El validador exige un QA independiente PASS antes del handoff.
- No hay frames, audio, assets aprobados ni render acreditado en los storyboards revisados.

## Inventario de slots y estado

| Fecha / slot | project_id | Ubicación encontrada | Estado |
|---|---|---|---|
| 5-nov 07:00 | `2026-11-05_inter-venus-dia-largo` | `cola/bloqueados/` (JSON + carpeta) | BLOQUEADO |
| 5-nov 13:30 | `2026-11-05_comida-palomitas-explotan` | `cola/bloqueados/` (JSON + carpeta) | BLOQUEADO |
| 5-nov 17:00 | `2026-11-05_inter-arboles-mito-respiran` | `cola/bloqueados/` (JSON + carpeta) | BLOQUEADO |
| 5-nov 19:00 opcional | `2026-11-05_inter-rayo-globular` | `cola/bloqueados/*.json` | BLOQUEADO |
| 6-nov 07:00 | `2026-11-06_inter-corazon-ballena-azul` | `cola/bloqueados/` (JSON + carpeta) | BLOQUEADO |
| 6-nov 13:30 | `2026-11-06_comida-aguacate-negro` | `cola/bloqueados/` (JSON + carpeta) | BLOQUEADO |
| 6-nov 17:00 | `2026-11-06_inter-ranas-congeladas` | `cola/bloqueados/` (JSON + carpeta) | BLOQUEADO |
| 6-nov 19:00 opcional | `2026-11-06_inter-arena-cantante` | `cola/bloqueados/*.json` | BLOQUEADO |
| 7-nov 07:00 | `2026-11-07_kids-huesos-bebe` | `cola/bloqueados/` (JSON + carpeta) | BLOQUEADO |
| 7-nov 13:30 | `2026-11-07_inter-mpemba-mito` | `cola/bloqueados/` (JSON + carpeta) | BLOQUEADO |
| 7-nov 17:00 | `2026-11-07_inter-suenos-pulpo` | `cola/bloqueados/` (JSON + carpeta) | BLOQUEADO |
| 7-nov 19:00 opcional | `2026-11-07_inter-nubes-pesan` | `cola/bloqueados/` (JSON + carpeta duplicada) | BLOQUEADO; RECONCILIAR |

## Contrato de handoff: corrección de jerarquía

La instrucción semanal del 31-oct pide carpetas `cola/entrada/<project_id>/` con tres archivos. Sin embargo, el contrato operativo unificado vigente desde 1-nov tiene mayor jerarquía y define:
1. Borrador en `proyectos/<project_id>/storyboard.json`.
2. QA narrativo independiente PASS.
3. Promoción a `cola/entrada/<project_id>.json` (JSON de primer nivel).

El workflow y el procesador actual esperan precisamente JSON de primer nivel; no se debe modificar el workflow para adaptarlo al formato de carpeta legado. Los tres informes RADAR del 5–7 ya recibieron una nota de estado; esta auditoría aclara que la incompatibilidad está en la instrucción semanal heredada, no en el contrato vigente ni en el workflow.

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
