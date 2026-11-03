# Producción fin de día — 2-nov-2026 ~22:10 CDMX (rutina Imaginantes)

Revisión de parrilla 3–5 nov (slots 07:00 / 13:30 / 17:00 CDMX; 19:00 vale hasta 4-nov; 17:45 desde 5-nov; dato 23:30).
Estado: `cola/entrada/` vacía · `handoffs/grok_inbox/` sin paquetes · `handoffs/grok_done/` vacío · sin mp4 nuevos pendientes de programar.

## Listo (programado YT+TT+FB)
- 3-nov: 13:30 Maillard (JOA1Bm6KYDs), 17:00 Juno (bpeRL5XtYLI), 19:00 SmartPE (-WBW0X9KpLM).
- 4-nov: 07:00 hipo (Rg-iTgMExWw), 13:30 miel (jpDyCX6zSgQ), 17:00 bioluminiscencia (4xylLT3vSIU).

## Huecos reales
| Slot | Estado | Quién |
|---|---|---|
| 3-nov 07:00 kids | **CUBIERTO** leche-enchilado, YT 7HfvkkR5Jf4 (ver 2026-11-03_SLOT_0700_CUBIERTO.md) | Grok app: TT+FB antes de 06:30 |
| 3-nov 23:30 dato | Sin paquete | ChatGPT (rutina dato 10:00/16:00), Grok monta mismo día ≤22:30 |
| 4-nov 19:00 | Machu Picchu pendiente OK Mj; respaldo "cielo azul / atardecer rojo" (NASA SpacePlace / NOAA) | ChatGPT entrega respaldo antes de 3-nov 22:00 si no hay OK; Grok monta |
| 4-nov 23:30 dato | Sin paquete | ChatGPT → Grok |
| 5-nov 07:00 / 13:30 / 17:00 / 17:45 | Storyboards en `proyectos/` (lote 7a41542; árboles c5b7a30), sin `narrative_qa` | Auditor CAPCOT 3-nov 15:00 → si PASS, promover a `cola/entrada/<id>.json` + marcador en `handoffs/grok_inbox/` → Grok monta antes de 4-nov 22:00 |

## PARA_CHATGPT (pegar)
1. 4-nov 19:00: entrega storyboard canónico del respaldo "Por qué el cielo es azul y el atardecer rojo" en `proyectos/2026-11-04_inter-cielo-azul/storyboard.json` (arco LINEA_EDITORIAL, fuentes reales) antes de 3-nov 22:00, salvo OK de Mj a Machu Picchu.
2. Datos 23:30 de 3 y 4-nov: noticia ≤48h con fuente primaria; si no hay, "SIN DATO".
3. No tocar 5-nov hasta el veredicto del Auditor (3-nov 15:00); si FAIL, corregir solo lo señalado.

## PARA_GROK (pegar)
1. Revisa `handoffs/grok_inbox/` después de las 15:30 del 3-nov: solo monta lo que tenga PASS del Auditor (nada desde `cola/bloqueados/`).
2. 5-nov: monta y programa YT/TT/FB a 07:00, 13:30, 17:00 y 17:45 CDMX (UI NY +1 h); anota yt_id real y mueve marcador a `grok_done/`.
3. Si llega respaldo 4-nov 19:00 o dato 23:30, mismo flujo.

No se generaron frames ni voz en este bot. No hay Firebase/webhook de pago.
