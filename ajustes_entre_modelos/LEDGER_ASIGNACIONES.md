# Ledger de asignaciones — tablero vivo

Una fila por trabajo. Estado: `cola` | `en-progreso` | `hecho` | `bloqueado`.
Sin evidencia no está hecho. Se actualiza en cada corrida del trabajador de
cola y en cada asignación manual. Ver
`ajustes_entre_modelos/COORDINACION_AUTONOMA.md`.

| ID | Trabajo | Dueño | Estado | Evidencia | Actualizado |
|---|---|---|---|---|---|
| MOZART-REPRO | Reproducción independiente del caso Mozart con texto, por ejecución | Amor | hecho | Nota + recibo en motor-u6-storage, rama alterno/reconexion-2a1, commit 41cb2333. 118 s, exit 0, recibo COMPLETED, H1/H2 idénticos, verificador 19/20 (el 1 que falta es el cambio esperado del 13-nov en la calibración). | 2026-11-15 ~16:54 CST |
| MOZART-REVISION-CHATGPT | Revisión de ChatGPT de la auditoría Mozart (5 hallazgos) | ChatGPT | hecho | motor/REVISION_CHATGPT_MOZART_20261113.md, commit ada99a37, 15-nov 16:41 CST, 114 líneas. Corrobora las 5 correcciones; NO certifica una reproducción ejecutada por ChatGPT. | 2026-11-15 16:41 CST |
| LESTES-VALIDAR | Validar storyboard de Lestes con el validador Python real + --check-doi | Amor | hecho | Storyboard: cola/entrada/2026-11-15_dato-dia-diapausa-lestes-sponsa/storyboard.json ("El huevo que espera al frío"). Fallaba con 8 errores (faltaba asset_filename en las 8 escenas) + aviso del gancho; corregido y el validador pasa (exit 0, DOI SRC-001 resuelve). Commit ba571fac. | 2026-11-15 ~17:00 CST |
| CUASARES-AUDITORIA | Auditoría narrativa independiente del storyboard de cuásares | Por asignar (independiente, NO ChatGPT) | cola | Storyboard: proyectos/2026-11-15_dato-quasar-pareja-cosmic-dawn/storyboard.json, commit 54c8ade, 184 palabras ("Dos cuásares casi se tocan"). FAIL/82 vigente. | 2026-11-15 |
| GROK-RECEPCION | Que Grok reciba y ejecute órdenes del bus | Grok | bloqueado | Sin vía programática gratuita: la API es de pago (sin nivel gratuito permanente) y grok.com bloquea el navegador en la nube con Cloudflare; recepción no verificable (404s). Nada puede depender de Grok. Su trabajo se re-rutea al trabajador de cola. | 2026-11-15 |
| MIGRACION-ACUSE | Acuse formal de otro modelo en ChatGPT-migracion | Otro modelo (no ChatGPT) | cola | Falta el acuse formal. No se puede rellenar en nombre de otro modelo. | 2026-11-15 |

## Reglas del ledger

- Todo trabajo nuevo entra como Issue (plantillas en
  `.github/ISSUE_TEMPLATE/`) y como fila aquí.
- `bloqueado` lleva escrito QUÉ lo desbloquea. Sin eso, es un abandono.
- La evidencia es un enlace a PR/commit, no un acuse.
