# SKILL DRAFT — Cápsula diaria de imaginantes (CAPCOT)

Fuente de verdad: docs/PLAN_MAESTRO_AUTOMATICO.md. Este draft = procedimiento probado en el box (2026-10-24).
**Nunca publicar sin aprobación de Mj** (publicar.py es dry-run por defecto).

## Canal
**Datos y ociosidades** · @datosyociosidades · YouTube UCU2ZI-6pBJEr9aSFsF6bxLw (sin números en nombres/handles).

## Línea editorial y formato
- Periodismo informativo-narrativo, in medias res, solo hechos con fuente verificada (dramatizaciones solo visuales).
- Estructura (investigacion/ANALISIS_ESTILO_IMAGINANTES.md §8 + ANALISIS_CLIPS_MJ.md): **gancho** (paradoja/imagen) →
  **ancla** (quién/cuándo) → **relato en 3 beats** (metáfora, personificación) → **giro** (antítesis) → **cierre**
  (lo pequeño explica lo grande) → **reflexión/pregunta abierta + firma** "Esto fue Datos y ociosidades."
  Campo `arc_imaginantes` por escena.
- 9:16 1080x1920, 30 fps, h264/aac, **75–95 s**, −14 LUFS, subtítulos abajo ≤3 palabras, ~190–230 palabras.
- **Voz:** edge-tts es-MX-JorgeNeural, **rate +8 %** (+6/+10), pitch −2 Hz (default del pipeline).
- **Pausas (regla):** narración casi continua. `voice.modo_pausas="continuo"` (default): la escena dura lo que su voz + 0.6 s;
  pausas por puntuación 0.3–0.6 s; se recorta el silencio que edge-tts deja en cada frase. QA falla si un hueco entre
  subtítulos supera 0.9 s. **Si falta duración, agregar información respaldada, nunca silencio.**
- **Audio de fondo:** `audio.ambiente` = oceano | viento | oceano+viento | archivo; `audio.music_asset` =
  `sintetico:menor_calma` | archivo CC0 (documentar fuente/licencia en `music_license`). Camas a −38/−40 LUFS vs voz −16 LUFS
  + sidechain ducking → música ~22–24 dB bajo la voz.
- **Cortinilla final 6 s:** Fuentes (cita corta + DOI/ref_display), aviso IA/voz/audio, firma del canal.
- **Estilo visual:** distinto en cada cápsula; rotación con scripts/rotar_estilo.py (docs/ESTILOS_VISUALES.md).
- **Publicación:** metadata.json (descripción + fuentes + hashtags + caption TikTok) generado por scripts/metadata.py.

## Requisitos (instalados en el box)
python3, ffmpeg/ffprobe, `pip install edge-tts pillow requests`. Voz: es-MX-JorgeNeural +8 %.

## Paso a paso
1. Tema: `python3 scripts/tendencias.py` (RSS Google Trends MX, score 0–10; descartar crimen/deporte/personas).
2. Guion → storyboard.json:
   - Con key: `CAPCOT_LLM_API_KEY=... python3 scripts/generar_guion_llm.py "<tema>" -o proyectos/<id>/storyboard.json`
     (base x.ai / modelo grok-4 configurables con CAPCOT_LLM_BASE_URL / CAPCOT_LLM_MODEL; sale con código 3 si no hay key).
   - Sin key: el agente redacta el storyboard siguiendo el esquema de proyectos/lote01-*/storyboard.json.
   - Lotes: `python3 scripts/dividir_lote.py proyectos/guiones_lote_01/storyboard.json`.
3. Verificar fuentes: `python3 scripts/validar_storyboard.py <sb> --check-doi` (Crossref). Revisar a mano que cada
   afirmación esté respaldada; reescribir o marcar como dramatización lo que no.
4. Frames: `python3 scripts/generar_frames.py <sb> --proveedor xai|openai|manual|placeholder`
   (xai/openai requieren CAPCOT_IMAGE_API_KEY). Alternativa usada: GenerateImage del agente, 576x1024,
   guardar como frames/scene_NNN.jpg|png junto al storyboard.
5. Todo en uno (sin publicar):
   `python3 scripts/capsula_diaria.py --storyboard proyectos/<id>/storyboard.json --proveedor-img placeholder [--fecha AAAA-MM-DD]`
   → salidas/<fecha>_<id>/ con capsula.mp4, capsula.srt, guion.md, fuentes.md, qa.json, publicacion.json, LEEME.md.
   Montaje solo: `python3 scripts/montar_capsula.py <sb> -o capsula.mp4` (ejecutar con nohup si es largo, ~60 s).
5b. Estilo: `python3 scripts/rotar_estilo.py` (capsula_diaria lo aplica solo; `--estilo <id>` para forzar).
5c. Metadatos: `python3 scripts/metadata.py salidas/<dir>/ [storyboard.json]` → metadata.json.
6. QA: `python3 scripts/qa_capsula.py capsula.mp4 storyboard.json` → todo PASA. Mirar la cortinilla:
   `ffmpeg -ss <dur-3> -i capsula.mp4 -frames:v 1 /tmp/c.png` (usar `ref_display` en fuentes con URL larga).
7. Publicación (solo con aprobación): `python3 scripts/publicar.py <salida> [--video capsula_v2.mp4 --storyboard storyboard_v2.json] --ejecutar` (usa metadata.json; dry-run sin --ejecutar)
   (CAPCOT_YT_TOKEN para YouTube; CAPCOT_TIKTOK_ACCESS_TOKEN → inbox de TikTok como borrador).
8. Métricas: `python3 scripts/metricas.py registrar|recolectar|reporte` (SQLite data/metricas.db).

## Git
`git pull --rebase` antes de commit; solo docs/scripts/storyboards/guion/fuentes; medios en .gitignore; no borrar archivos ajenos.

## Credenciales pendientes
CAPCOT_LLM_API_KEY, CAPCOT_IMAGE_API_KEY, OAuth YouTube (CAPCOT_YT_TOKEN), CAPCOT_TIKTOK_ACCESS_TOKEN, música con licencia.

## Ejemplo de referencia
salidas/2026-10-24_fenomeno-el-nino/capsula_v2.mp4 (87.8 s, QA 11/11): storyboard_v2.json, guion_v2.md, metadata.json, HERRAMIENTAS.md.
