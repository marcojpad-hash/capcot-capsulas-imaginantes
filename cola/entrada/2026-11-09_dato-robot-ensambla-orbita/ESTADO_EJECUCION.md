# Estado de ejecución — Dato del día 9 nov 2026

- **project_id:** `2026-11-09_dato-robot-ensambla-orbita`
- **Serie:** Datos y ociosidades
- **Fecha objetivo:** 2026-11-09
- **Slot:** 23:30 America/Mexico_City
- **Estado:** `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`
- **Preproducción textual:** COMPLETADA (QA factual + narrative_qa PASS)
- **Fuente primaria:** VERIFICADA (Caltech + DARPA, WebFetch 9-nov)
- **Medios:** `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO` (reconciliación run 12: la carpeta `salidas/2026-11-09_dato-robot-ensambla-orbita/` y los archivos `capsula.mp4`/`portada.jpg` devuelven 404 en `main`; `frames/` en `feature` contiene solo `.gitkeep`).
- **Audio / video:** no verificables en el árbol actual. Los 21/21 checks y 87.57 s quedan como registro histórico de QA, no como verificación reproducible del medio en el repositorio.
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


## Corrección de evidencia — run 12, 2026-11-20

La reconciliación previa que afirmaba que los medios estaban en `main` no se pudo reproducir. Se consultaron directamente la carpeta de salida, `capsula.mp4` y `portada.jpg`; los tres recursos devolvieron HTTP 404. La carpeta de frames en la rama de trabajo solo contiene `.gitkeep`. Por tanto, el estado vigente es `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`; no se borró ni regeneró ningún recurso.

Se conserva `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`: `main/data/publicaciones.json` mantiene el YouTube ID `ZG4iQgmWrLI` y `publishAt=2026-11-22T01:00:00Z` (21-nov, 19:00 CDMX), además de programación registrada para TikTok y Facebook. No cancelar ni redispatchar.

`cola/estado/2026-11-09_dato-robot-ensambla-orbita.json` sigue devolviendo 404: `RECEPCION_GROK_NO_CONFIRMADA`. El marcador en `handoffs/grok_inbox` no sustituye el acuse de estado.
## Reconciliación de medios y programación — 22 nov 2026

**Corrección de la clasificación de medios:** la búsqueda anterior se limitó a `salidas/2026-11-09_dato-robot-ensambla-orbita`, que no existe. La lectura del árbol completo de `main` encontró los medios en `cola/entrada/2026-11-09_dato-robot-ensambla-orbita/`; por tanto, el antiguo `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO` queda **SUPERSEDIDO**. Estado actual: `MEDIOS_VERIFICADOS_EN_MAIN_COLA_ENTRADA; NO_PRESENTES_EN_FEATURE`.

Evidencia de árbol `main`:
- `capsula.mp4`: SHA `72d7ca5757a18b5d7a248503ac0e096dc0ac37ff`, 25,795,339 bytes.
- `portada.jpg`: SHA `c8cd5a72f88c95c95b97f2ed81ee254c783f4a86`, 213,315 bytes.
- Nueve frames `scene_001.jpg`–`scene_009.jpg` presentes.
- `programacion.json`: SHA `395eed4055388a8eaab6b89a3008061e4097118b`; `qa.json`: SHA `9dc15174cf92bd354edd4bc0b8309fddceeeaf52`; `metadata.json`: SHA `5a6b2a08752a499aa2d18774705e091adc0f919c`.
- QA audiovisual: 21/21 checks, 87.57 s. Esto no sustituye el `narrative_qa` PASS 90 del storyboard.

**Producción preexistente, no redispatchar:** `programacion.json` mantiene `estado=programado`, YouTube `ZG4iQgmWrLI`, `publish_at=2026-11-22T01:00:00Z` (21-nov 19:00 CDMX), TikTok y Facebook programados. `publishAt` ya quedó en el pasado, pero no se confirmó el estado público: el fetch de la URL de YouTube devolvió `DisabledError`; no existe archivo `historial_youtube` en el árbol y `vistas_historico.json` no contiene ese ID. `metadata.json` conserva `privacyStatus=private` mientras `programacion.json` dice `programado`; se registra como **PUBLICACIÓN_REAL_NO_VERIFICADA / RIESGO_DE_ESTADO_PROGRAMADO_ANTIGUO**. No cancelar, reprogramar ni redispatchar.

El paquete de `main` está anidado en `cola/entrada/<id>/`; el workflow actual selecciona solo JSON planos de primer nivel, así que su ruta es `NOT_DISPATCHABLE_POR_SELECTOR`. El paquete de `feature` también es anidado y solo contiene storyboard/`.gitkeep`. El archivo de estado de `main` permanece con texto del 10-nov que dice audio/video no generados y frames pendientes; esa ficha es **DESACTUALIZADA** frente a los medios, QA y programación actuales. `cola/estado/<id>.json` sigue 404: `RECEPCION_GROK_NO_CONFIRMADA`. No se infiere recepción por la carpeta ni por GitHub.

No es un segundo proyecto ni un slot nuevo: el mismo `project_id` conserva en storyboard el slot original 9-nov 23:30, mientras la programación de producción lo movió a 21-nov 19:00. La clasificación correcta sigue siendo `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`; no se declara conflicto entre proyectos distintos ni se altera `main`.
