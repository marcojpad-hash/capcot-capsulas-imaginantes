# Estado de ejecución — Dato del día 9 nov 2026

- **project_id:** `2026-11-09_dato-robot-ensambla-orbita`
- **Serie:** Datos y ociosidades
- **Fecha objetivo:** 2026-11-09
- **Slot:** 23:30 America/Mexico_City
- **Estado:** `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`
- **Preproducción textual:** COMPLETADA (QA factual + narrative_qa PASS)
- **Fuente primaria:** VERIFICADA (Caltech + DARPA, WebFetch 9-nov)
- **Medios:** VERIFICADOS EN `main` — `capsula.mp4`, `portada.jpg` y nueve frames `scene_001.jpg`–`scene_009.jpg`.
- **Audio / video:** `capsula.mp4` existe en `main`; QA audiovisual registra 21/21 checks y duración 87.57 s.
- **Publicación/programación:** `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`; YouTube ID `ZG4iQgmWrLI`, programado para 2026-11-21 19:00 CDMX (2026-11-22T01:00:00Z). TikTok y Facebook también figuran programados para ese slot, sin IDs de publicación.

## Archivos del paquete
- `storyboard.json` — 9 escenas, 88 s (escenas+cortinilla), `neon_noir`, `export.plano_seconds=5`
- `fuentes.md` — claims y límites
- `PARA_GROK.md` — prompts y nombres de archivo
- `frames/` — vacío; Grok sube aquí los 9 PNG 1080×1920

## Notas para Grok / montaje
1. Portada = scene_001: título en caja crema/amarilla, subrayado rojo (tipografía en post; el frame deja zona libre).
2. Miniatura YT/TT/FB = primer frame (skill entrega-de-cápsula-con-portada).
3. Voz: `es-MX-JorgeNeural` +7%, continuo, pad 0.3 s — la genera Imaginantes al montar, no Grok.
4. No publicar sin OK de Mj.

## Reconciliación de ramas — 2026-11-20

La versión `main` contiene producción posterior para este mismo project_id: `capsula.mp4`, `portada.jpg`, nueve frames, subtítulos y `programacion.json`. La programación registra YouTube ID `ZG4iQgmWrLI` y fecha `2026-11-21 19:00` CDMX; TikTok/Facebook aparecen programados, sin IDs públicos. No se ha comprobado aquí el resultado final de esa programación.

El `qa.json` de `main` contiene 21/21 checks true y mide 87.57 s, dentro del contrato 75–90 s. Esto es QA audiovisual, independiente del `narrative_qa` PASS/90 del storyboard. El paquete no se redispatcha.

En la rama `feature`, `cola/estado/2026-11-09_dato-robot-ensambla-orbita.json` devuelve 404: `RECEPCION_GROK_NO_CONFIRMADA`. La existencia de producción en `main` no sustituye el acuse de recepción.
