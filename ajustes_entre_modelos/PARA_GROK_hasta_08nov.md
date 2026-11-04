# PARA GROK (app principal, NO el bot) — Plan hasta el 8-nov-2026 (CDMX)

> Mj: el bot Imaginantes ya va en ~66% de créditos en 1.5 días. **Tú usas tus propios créditos** (GenerateImage de la app). Lo que hace el bot: docs y commits.
> Estados: `data/horario_semana_2026-11-01_07.json`. Handoff base: `salidas/_ops/2026-10-28_HANDOFF_TOTAL_grok_principal.md`, `ajustes_entre_modelos/HANDOFF_GROK_PRODUCCION.md`, `docs/FLUJO_EXTERNO.md`, `docs/RECETA_CAPSULA.md`.

## 0. HUECOS HOY 4-nov (madrugada 02:30 CDMX)
1. **19:00** `2026-11-04_inter-cielo-azul-atardecer` (respaldo de Machu Picchu, sin OK de Mj): montar en cuanto ChatGPT entregue el guion; mp4 listo antes de 16:00 CDMX.
2. **23:30** `2026-11-04_dato-polvo-atrapa-oro` (brief en `PARA_CHATGPT_dato_del_dia.md`, 10:10 CDMX): montar el mismo día cuando ChatGPT entregue en `cola/entrada/`; mp4 listo antes de 21:30 CDMX; YT+TT+FB 23:30 CDMX (TT AI ON y UI NY 00:30; FB sin AI).

## 1. Tu rol (cuando ChatGPT entregue un paquete en `cola/entrada/<pid>/`)
1. **QA de arco y cierre**: paradoja al inicio, cableado entre escenas, antítesis y un cierre con eco (LINEA_EDITORIAL §8–9). Cuenta 205–235 palabras y revisa las fuentes. Si falla, lo devuelves con una nota en `BITACORA_COORDINACION.md`; no lo reescribas tú a fondo.
2. **Frames** (8) con tu GenerateImage, en el estilo del prompt_visual.
3. **Montar** el mp4 (voz es-MX-JorgeNeural +7%, en continuo) siguiendo RECETA_CAPSULA.
4. **YouTube**: programarlo a la hora CDMX del slot. Anota el yt_id REAL en el JSON y haz commit.
5. **TikTok / Facebook**: vía TikTok Studio y Meta Business Suite a la misma hora.

## 2. Checklist por hueco
| Hueco | Fuente | Fecha límite para montar | Notas |
|---|---|---|---|
| 3-nov 07:00 kids | Grok Bot | hecho | leche-enchilado YT 7HfvkkR5Jf4; TT+FB programados (ver 2026-11-03_SLOT_0700_CUBIERTO.md) |
| 23:30 dato 1–7 nov | ChatGPT (b) | mismo día 22:30 | 23:30 CDMX = 05:30Z del día siguiente. Si "SIN DATO", deja el slot vacío |
| 5–7 nov ×12 | ChatGPT (c) rewrite | día anterior 22:00 | Si no llega la v2 → monta el storyboard v1 que ya está en cola (sirve) |
| 4-nov 19:00 Machu/cielo azul | Mj OK o respaldo de ChatGPT (d) | 3-nov 22:00 | |
- [x] Swap arqueas→tiburón 1-nov: borrados YT/TT/FB ya hechos (`salidas/_ops/2026-11-01_swap_arqueas_tiburon.md`). No re-borrar.

## 3. Reglas
- **No regenerar overlays caros**: reutiliza los frames y overlays que ya existen; solo genera lo que falte.
- **Thumbnail de YT = frame 0 del mp4.**
- **DST**: la UI de NY = CDMX + 1 h (ej.: 07:00 CDMX → 08:00 NY).
- Hashtags simples (3–5, nada de cadenas trending largas).
- Etiqueta IA: **TT ON / FB OFF**.
- No marcar "Hecho para niños" en YT.
- No inventes yt_ids; si no se programó, el estado sigue `pendiente`.

## 4. YA programado (NO duplicar)
1-nov: 03:00 xolo (aZn5eTyiQPQ), 07:00 pulpo (PQzLUQnHbcA), 13:30 cebolla (ZWF6ke9Zec0), 17:00 Baffin (HDQr9OGpFJM), 19:00 tiburón (0x1B9_rMm-I).
2-nov: 07:00 camarón mantis (5sxxx0vuXFE), 13:30 pan duro (V9bO9EUN0JA), 17:00 murciélagos (c-7pMF3-B-g), 19:00 sequías (OwfxfQ4RPSo).
3-nov: 13:30 Maillard (JOA1Bm6KYDs), 17:00 Juno (bpeRL5XtYLI), 19:00 SmartPE (-WBW0X9KpLM).
4-nov: 07:00 hipo (Rg-iTgMExWw), 13:30 miel (jpDyCX6zSgQ), 17:00 bioluminiscencia (4xylLT3vSIU).

## 5. Ahorro
- Prefiere **remontar paquetes que ya están en cola** (storyboards 5–7 nov) antes que pedir nuevos.
- Nada de chats largos con el bot Imaginantes; si hace falta, un solo mensaje: "actualiza JSON + commit".
- Si faltan créditos, aplica el mínimo viable de `salidas/_ops/2026-11-01_cobertura_hasta_fin_semana.md`.
