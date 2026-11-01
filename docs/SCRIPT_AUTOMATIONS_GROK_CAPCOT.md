# Script de Automations — CAPCOT → Grok principal

Fecha: 2026-11-01 CDMX · De: Puta 3 · Para: Mj pega esto en **grok.com → Automations**

Objetivo: que **Grok app** haga lo que hacían Imaginantes / CAPCOT bots **sin gastar tokens de Grok Bot**.

Grok ya tiene GitHub App write (All repositories). Zona: **America/Mexico_City**. Repo: `marcojpad-hash/capcot-capsulas-imaginantes`.

## Qué sí puede Grok hoy (sin box)
- Investigar tema + fuentes reales (DOI).
- Escribir `storyboard.json` + `fuentes.md`.
- Generar frames 9:16 con **Grok Imagine** y subirlos al repo (o dejar nombres + prompts si el push de binarios falla; entonces commit solo JSON y lista de prompts).
- Commit/push paquetes en `cola/entrada/<id>/` o `proyectos/<id>/`.
- Seguir `docs/AHORRO_RECURSOS_PIPELINE.md` (FFmpeg-first, HD solo tras QA, máx 1–2 I2V héroe).

## Qué NO puede sin box / Actions
- Correr `montar_capsula.py` / `edge-tts` JorgeNeural en local (Grok no tiene el box de Puta 3).
- `metricas.py` con OAuth YouTube del box.
- Publicar YouTube con token `~/.capcot/` del box.

**Por eso C1 entrega PAQUETE listo para montar, no el mp4 final**, salvo que Mj te diga que ya tienes otra máquina o workflow Actions de montaje.

Candado voz: **es-MX-JorgeNeural, rate +7%, pitch −2Hz — intocable** (va en el storyboard; el montaje lo usará quien tenga edge-tts).

No publicar YT/TT sin OK explícito de Mj.

---

## C1 — Cápsula diaria (paquete)

- **Cuándo:** todos los días ~11:00 CDMX (antes de la ventana I2V 12:00–17:30)
- **Nombre sugerido:** `CAPCOT — Paquete cápsula diaria`

**Prompt (pegar tal cual):**

```
Eres Grok principal con write en GitHub (marcojpad-hash). Produce UNA cápsula CAPCOT del día como PAQUETE (sin gastar tokens de Grok Bot / Imaginantes).

Repo: https://github.com/marcojpad-hash/capcot-capsulas-imaginantes
Lee en este orden y obedece:
1) docs/AHORRO_RECURSOS_PIPELINE.md
2) docs/RECETA_CAPSULA.md
3) docs/GUIA_MODELO_EXTERNO.md
4) ajustes_entre_modelos/HANDOFF_GROK_PRODUCCION.md
5) data/rotacion.json + data/publicaciones.json (no repetir tema/estilo/estructura reciente)

Reglas de ahorro (obligatorias):
- Ruta por defecto: storyboard → frames FIJOS (no Flow/Dreamina/Kling/HyperFrames salvo 1–2 insertos héroe I2V y solo si Mj lo pidió).
- No regeneres HD: un set de prompts/frames finales tras validar el guion.
- Voz en storyboard EXACTA: edge-tts es-MX-JorgeNeural rate +7% pitch -2Hz. No cambies TTS.
- No publiques YouTube ni TikTok. Solo paquete en el repo.

Pasos:
1) Elige tema de rotación (prioridad ciencia ≤7 días con DOI real). Verifica que el DOI resuelve.
2) Escribe proyectos/AAAA-MM-DD_slug/storyboard.json (7–9 escenas, 170–235 palabras, 60–95 s, capas mapa+dato, source_ids, estructura distinta a las recientes).
3) Fuentes en proyectos/.../fuentes.md.
4) Genera frames 9:16 con Grok Imagine (un image_prompt por escena = prompt_base del estilo + escena en inglés). Si puedes subir PNG al repo bajo frames/, hazlo; si no, deja la lista de prompts y asset_filename en un README del proyecto y commit el storyboard igual.
5) Copia o deja también cola/entrada/<id>/{storyboard.json, frames/ o lista, fuentes.md} para montaje posterior.
6) Commit + push. Mensaje: `Paquete <id> (<estilo>, <estructura>) para <fecha>`.
7) Responde a Mj en español corto: tema, estilo, path del commit, si frames están en repo o solo prompts, y «listo para montar». Si algo bloquea, di exactamente qué.

Si ya hay paquete del mismo día en cola/entrada o proyectos/: no dupliques; avisa y para.
```

---

## C2 — Revisión de cola / huecos (noche)

- **Cuándo:** todos los días ~20:00 CDMX
- **Nombre:** `CAPCOT — Revisión cola y rotación`

**Prompt:**

```
Repo capcot-capsulas-imaginantes. Sin montar video y sin tokens de bots:
1) Mira cola/entrada/: ¿hay paquetes sin procesar? Lista ids.
2) Mira data/rotacion.json y publicaciones recientes: ¿falta tema de la rotación cultural para mañana?
3) Si falta paquete para mañana y aún no corriste C1 hoy con éxito: arma el paquete ahora con las mismas reglas de docs/AHORRO_RECURSOS_PIPELINE.md + RECETA (un solo paquete).
4) Si la cola está sana y mañana ya tiene tema: silencio o una línea a Mj.

No publiques. No cambies JorgeNeural. No uses HyperFrames.
```

---

## C3 — Métricas ligeras (público, sin OAuth del box)

- **Cuándo:** cada día ~18:00 CDMX
- **Nombre:** `CAPCOT — Snapshot vistas público`

**Prompt:**

```
Canal YouTube «Datos y ociosidades» handle @datosyociosidades (id UCU2ZI-6pBJEr9aSFsF6bxLw).
TikTok @datosyociosidades.

Sin el OAuth del box: usa datos PÚBLICOS (página del canal / búsqueda web) y anota en el repo
avances/metricas_publicas/AAAA-MM-DD.md: top Shorts recientes con vistas aproximadas, nota de 3 líneas (qué sube/baja).
Commit + una línea a Mj solo si hay cambio fuerte (>2× o caída rara). Si no hay cambio notable: silencio.

No sustituyas vistas_historico oficial hasta que Imaginantes/CAPCOT Métricas retomen o haya Actions con OAuth.
No gastes tokens de Grok Bot.
```

---

## Relación con motor (A1–A5)

Las Automations del **motor** siguen en `motor-u6-storage/docs/SCRIPT_AUTOMATIONS_GROK_MOTOR.md` (A1–A5, parche sin box). No mezclar prompts CAPCOT con fábrica del motor.

## Qué queda pausado en bots (ahorro)

| Cosa | Estado |
|------|--------|
| Imaginantes generación / montaje diario | Pausar mientras Grok corre C1–C2 |
| CAPCOT Métricas / Pantallas horarias | Pausar hasta créditos; C3 es sustituto público |
| Puta 3 montaje / procesar_cola | No reactivar salvo que Mj pida un montaje puntual |
| Aviso Premium ~2 dic | Lo sigue Puta 3 |

## Cómo activarlo en grok.com

1. grok.com → **Automations**.
2. Crea C1, C2, C3 (horarios CDMX arriba).
3. Conector GitHub conectado (App All repos + write).
4. Prueba C1 una vez a mano; confirma el commit en el repo.
5. Cuando recuperes créditos de bot, Imaginantes retoma montaje oficial + métricas OAuth; Grok puede dejar C1 como refuerzo de paquetes o bajar frecuencia.
