# Ledger de asignaciones — tablero vivo

Una fila por trabajo. Estado: `cola` | `en-progreso` | `hecho` | `bloqueado`.
Sin evidencia no está hecho. Se actualiza en cada corrida del trabajador de
cola y en cada asignación manual. Ver
`ajustes_entre_modelos/COORDINACION_AUTONOMA.md`.

| ID | Trabajo | Dueño | Estado | Evidencia | Actualizado |
|---|---|---|---|---|---|
| MOZART-REPRO | Reproducción independiente del caso Mozart con texto, por ejecución | Amor | hecho | Nota + recibo en motor-u6-storage, rama alterno/reconexion-2a1, commit 41cb2333. 118 s, exit 0, recibo COMPLETED, H1/H2 idénticos, verificador 19/20 (el 1 que falta es el cambio esperado del 13-nov en la calibración). | 2026-11-15 ~16:54 CST |
| MOZART-REVISION-CHATGPT | Revisión de ChatGPT de la auditoría Mozart (5 hallazgos) | ChatGPT | hecho | motor/REVISION_CHATGPT_MOZART_20261113.md, commit ada99a37, 15-nov 16:41 CST, 114 líneas. Corrobora las 5 correcciones; NO certifica una reproducción ejecutada por ChatGPT. | 2026-11-15 16:41 CST |
| LESTES-VALIDAR | Validar storyboard de Lestes con el validador Python real + --check-doi | Amor | hecho | Amor ejecutó localmente el validador Python con `--check-doi`: exit 0 y DOI SRC-001 resuelto. Storyboard de `proyectos/` y copia de validación en `cola/entrada/<id>/` sincronizados, ambos blob `09500f5ccb8cf4261c69eb4bff543595acf7fe0e`; commits de sincronización `0c7dcac` (cola) y `8e0bf3e` (proyectos). Paquete de tres archivos: `storyboard.json`, `fuentes.md` y `ESTADO_EJECUCION.md`; sin medios generados. | 2026-11-15 20:00 CST |
| LESTES-GROK-RECEPCION | Obtener recepción individual de Grok para el paquete Lestes | Grok / Imaginantes | bloqueado | Paquete preparado en carpeta anidada `cola/entrada/2026-11-15_dato-dia-diapausa-lestes-sponsa/`; no existe `cola/estado/<id>.json`. `scripts/procesar_cola.py` acepta carpeta anidada, pero `capcot-grok-dispatch.yml` solo escucha JSON de primer nivel y su búsqueda `workflow_dispatch` también es plana. No declarar recepción ni producción. | 2026-11-15 20:00 CST |
| CUASARES-AUDITORIA | Auditoría narrativa independiente del storyboard de cuásares | Trabajador de cola (Groq gpt-oss-120b; distinto de ChatGPT) | hecho | Informe en PR #13 (abierto, no fusionado), sobre `proyectos/2026-11-15_dato-quasar-pareja-cosmic-dawn/storyboard.json`, commit `54c8ade`. 13 hallazgos: 9 pendientes y 4 corregidos/por diseño. | 2026-11-15 19:05 CST |
| CUASARES-CORRECCION | Aplicar hallazgos de auditoría independiente al storyboard | ChatGPT | en-progreso | PR #14 abierto: `chatgpt/quasar-audit-fixes-20261115`; head `5161e6dae520f37710b625de1abce865f2dd5964`. Corrige apertura/progresión, Aether, puentes causales, redundancia y marcador del límite de evidencia. 175 palabras, 8 escenas, 84 s; 8/8 `asset_filename`. QA histórico FAIL/82 intacto. | 2026-11-15 20:00 CST |
| CUASARES-VALIDACION | Ejecutar `scripts/validar_storyboard.py --check-doi` sobre la revisión corregida | Trabajador de cola (sin LLM) | bloqueado | PR #14 aún abierto. El worker hace checkout de `main`, por lo que no valida la rama propuesta. Desbloqueo: integrar PR #14 y después crear un Issue `tipo: validar` para la ruta del storyboard. | 2026-11-15 19:50 CST |
| CUASARES-REAUDITORIA | Nueva auditoría narrativa independiente sobre el storyboard corregido | Trabajador de cola (Groq; distinto de ChatGPT) | bloqueado | PR #14 aún abierto; el worker lee `main`. Desbloqueo: integrar PR #14, pasar el validador y reencolar la auditoría sobre el nuevo contenido. | 2026-11-15 19:50 CST |
| GROK-RECEPCION | Que Grok reciba y ejecute órdenes del bus | Grok | bloqueado | Sin vía programática gratuita: la API es de pago (sin nivel gratuito permanente) y grok.com bloquea el navegador en la nube con Cloudflare; recepción no verificable (404s). Nada puede depender de Grok. Su trabajo se re-rutea al trabajador de cola. | 2026-11-15 |
| MIGRACION-ACUSE | Acuse formal de otro modelo en ChatGPT-migracion | Otro modelo (no ChatGPT) | cola | Falta el acuse formal. No se puede rellenar en nombre de otro modelo. | 2026-11-15 |

## Reglas del ledger

- Todo trabajo nuevo entra como Issue (plantillas en
  `.github/ISSUE_TEMPLATE/`) y como fila aquí.
- `bloqueado` lleva escrito QUÉ lo desbloquea. Sin eso, es un abandono.
- La evidencia es un enlace a PR/commit, no un acuse.
