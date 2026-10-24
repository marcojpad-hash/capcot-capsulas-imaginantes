# SKILL DRAFT — Cápsula diaria de imaginantes (CAPCOT)

Fuente de verdad: docs/PLAN_MAESTRO_AUTOMATICO.md. Este draft = procedimiento probado en el box (2026-10-24).
**Nunca publicar sin aprobación de Mj** (publicar.py es dry-run por defecto).

## Principios
Periodismo informativo-narrativo con arco dramático · in medias res · cierre con pregunta ontológica/abierta ·
cortinilla de fuentes REALES (1–4, verificadas) · la imagen narra, voz mínima (≥1 escena muda, ≤190 palabras) ·
estilo visual distinto por cápsula · 60–90 s, 1080x1920, h264/aac 30 fps, −14 LUFS, subs abajo ≤3 palabras, aviso IA.

## Requisitos (instalados en el box)
python3, ffmpeg/ffprobe, `pip install edge-tts pillow requests`. Voz: es-MX-JorgeNeural.

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
6. QA: `python3 scripts/qa_capsula.py capsula.mp4 storyboard.json` → todo PASA. Mirar la cortinilla:
   `ffmpeg -ss <dur-3> -i capsula.mp4 -frames:v 1 /tmp/c.png` (usar `ref_display` en fuentes con URL larga).
7. Publicación (solo con aprobación): `python3 scripts/publicar.py <salida> --ejecutar`
   (CAPCOT_YT_TOKEN para YouTube; CAPCOT_TIKTOK_ACCESS_TOKEN → inbox de TikTok como borrador).
8. Métricas: `python3 scripts/metricas.py registrar|recolectar|reporte` (SQLite data/metricas.db).

## Git
`git pull --rebase` antes de commit; solo docs/scripts/storyboards/guion/fuentes; medios en .gitignore; no borrar archivos ajenos.

## Credenciales pendientes
CAPCOT_LLM_API_KEY, CAPCOT_IMAGE_API_KEY, OAuth YouTube (CAPCOT_YT_TOKEN), CAPCOT_TIKTOK_ACCESS_TOKEN, música con licencia.
