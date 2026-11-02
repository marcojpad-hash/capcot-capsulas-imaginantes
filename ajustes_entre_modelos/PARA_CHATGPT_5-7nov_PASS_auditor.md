# PARA CHATGPT — lote 5–7 nov: una copia canónica + PASS del Auditor (2-nov-2026 ~16:06 CDMX)

**Regla Mj:** sin **PASS del Auditor CAPCOT** no hay promoción a `cola/entrada/` ni producción (ni frames, ni montaje, ni publicación).

## Qué haces tú (ChatGPT)
1. Para cada slot 5–7 nov (07:00 / 13:30 / 17:00 / 17:45) deja **UNA sola copia canónica** en `proyectos/<project_id>/` con `storyboard.json` que incluya bloque `narrative_contract`.
2. `project_id` = el del horario `data/horario_semana_2026-11-01_07.json` (tabla abajo). Si tu borrador tiene otro nombre en `cola/bloqueados/`, muévelo/renómbralo al ID del horario y borra duplicados (dir + .json sueltos).
3. **No te autoevalúes.** No escribas `narrative_qa` ni copies a `cola/entrada/`.
4. El **Auditor** (otra conversación, corre a las **15:00**) escribe `narrative_qa`; solo con **PASS** (score ≥ 85, los 7 checks OK, `flags` vacío) copia a `cola/entrada/<id>.json`.
5. Dato del día 23:30 (5/6/7 nov) sigue **TBD** salvo que tú entregues uno.
6. **Fuera de este lote:** 3-nov 07:00 kids (falta reemplazo) y Machu Picchu 4-nov 19:00 (espera OK Mj).

## Los 12 temas: ID destino (horario) ← rutas actuales
| Slot | ID canónico destino | Rutas actuales a mover/restaurar |
|---|---|---|
| 5-nov 07:00 kids | `2026-11-05_kids-dia-en-venus` | `cola/bloqueados/2026-11-05_inter-venus-dia-largo/` + `.json` |
| 5-nov 13:30 comida | `2026-11-05_comida-palomitas` | `cola/bloqueados/2026-11-05_comida-palomitas-explotan/` + `.json` |
| 5-nov 17:00 inter1 | `2026-11-05_inter-arboles-se-comunican` | `cola/bloqueados/2026-11-05_inter-arboles-mito-respiran/` + `.json` (ojo: el tema del borrador es «mito respiran»; ajusta título o avisa) |
| 5-nov 17:45 inter2 | `2026-11-05_inter-rayo-globular` | `cola/bloqueados/2026-11-05_inter-rayo-globular.json` |
| 6-nov 07:00 kids | `2026-11-06_kids-ballena-azul-corazon` | `cola/bloqueados/2026-11-06_inter-corazon-ballena-azul/` + `.json` |
| 6-nov 13:30 comida | `2026-11-06_comida-aguacate-negro` | `cola/bloqueados/2026-11-06_comida-aguacate-negro/` + `.json` |
| 6-nov 17:00 inter1 | `2026-11-06_inter-ranas-congeladas` | `cola/bloqueados/2026-11-06_inter-ranas-congeladas/` + `.json` |
| 6-nov 17:45 inter2 | `2026-11-06_inter-arena-cantante` | `cola/bloqueados/2026-11-06_inter-arena-cantante.json` |
| 7-nov 07:00 kids | `2026-11-07_kids-huesos-bebe` | `cola/bloqueados/2026-11-07_kids-huesos-bebe/` + `.json` |
| 7-nov 13:30 comida | `2026-11-07_comida-hielo-caliente` | `cola/bloqueados/2026-11-07_inter-mpemba-mito/` + `.json` (Mpemba = agua caliente que congela) |
| 7-nov 17:00 inter1 | `2026-11-07_inter-pulpo-suenos` | `cola/bloqueados/2026-11-07_inter-suenos-pulpo/` + `.json` |
| 7-nov 17:45 inter2 | `2026-11-07_inter-nubes-pesan` | **Duplicado:** `cola/bloqueados/2026-11-07_inter-nubes-pesan.json` y `cola/bloqueados/2026-11-07_extra-nubes-pesan/`. El horario dice **inter** → canónico `inter-nubes-pesan`; fusiona lo mejor de `extra-` y deja `extra-` fuera. |

## Estado de cola (docs)
Estos 12 pasan de «pedir_chatgpt» a **«en proyectos → espera PASS del Auditor»** en cuanto subas la copia canónica. El JSON del horario no se toca hasta PASS.
