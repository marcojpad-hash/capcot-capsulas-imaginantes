# PLAN MAESTRO AUTOMÁTICO — CAPCOT (fuente única de verdad)

Fecha: 2026-10-24 · Autor: Grok Bot · Estado: **vigente**. Si otro documento contradice este, **manda este**. Los documentos de ChatGPT (`docs/ARQUITECTURA_INICIAL.md`, `docs/FLUJO_DE_PRODUCCION.md`, `docs/MATRIZ_HERRAMIENTAS_GRATUITAS.md`, `templates/storyboard.template.json`, `checklists/revision_final.md`) se conservan como antecedente; sus puntos no contradichos siguen valiendo (no inventar fuentes, no versionar medios pesados, registrar hashes, no tocar el motor U6, no eludir límites de proveedores).

## 1. Objetivo
Canal diario **100 % automático** (YouTube Shorts; la descripción enlaza al TikTok existente de Mj) de micro-cápsulas científicas **verticales 9:16, 60–90 s**, concepto *Imaginantes*: periodismo informativo + narrativo, arco dramático, arranque *in medias res*, cierre de la historia + reflexión ontológica o pregunta abierta, la imagen narra, voz sintética mínima, subtítulos quemados, cortinilla con fuentes bibliográficas. Tema elegido por Google Trends (RSS) + backlog; métricas retroalimentan el sistema. **Mj no necesita estar presente**; la revisión humana es opcional.

## 2. Conflictos resueltos (antes → ahora, y por qué)
| # | Antes (ChatGPT) | Ahora | Razón |
|---|---|---|---|
| 1 | Formato 16:9, 1920×1080 | **9:16, 1080×1920** | TikTok/Shorts son verticales; Shorts exige vertical ≤3 min. |
| 2 | Duración 1–3 min (60–180 s) | **60–90 s** (objetivo 80 s, ~150–200 palabras) | Concepto de Mj y retención en short-form (ver `investigacion/ESTRATEGIA_VIRAL_Y_PIPELINE.md`). |
| 3 | Audiencia "público universitario", objetivo pedagógico | **Público general curioso**; periodismo narrativo con arco | Plataforma y estilo Imaginantes; el rigor se mantiene vía fuentes. |
| 4 | Generación de video **manual** con clicks en Flow/Kling | **Ruta por defecto sin clicks**: frames fijos por API de imagen (o local/gratuita) + Ken Burns con ffmpeg | Un humano clicando rompe la automatización diaria; los planes gratuitos web no tienen API ni cuota garantizada. |
| 5 | "Sin API de pago" como principio absoluto | **APIs permitidas cuando son gratuitas o de costo mínimo y con clave de Mj** (imagen, TTS Chirp de respaldo, YouTube Data API) | Sin API no hay automatización; el costo estimado es de pocos dólares/mes. Se sigue sin eludir límites ni automatizar UIs web. |
| 6 | Voz grabada o TTS sin especificar | **edge-tts** (`es-MX-JorgeNeural`, gratis, sin clave) por defecto; **Google Chirp 3 HD** como respaldo (1 M caracteres/mes gratis) | Voz mínima "tipo Loquendo" pero natural; edge-tts es no oficial y puede romperse, de ahí el respaldo. |
| 7 | SRT/VTT a mano y revisión de pronunciación humana | **Subtítulos por palabra** desde los *WordBoundary* del TTS (sin whisper); whisper/faster-whisper solo si el motor TTS no da tiempos | Tiempos exactos, cero transcripción, cero intervención. |
| 8 | Video animado como componente central | **Gancho animado opcional** (1–2 planos de ~5 s) **solo si existe API con créditos** (p. ej. Veo/Kling/Runway API) | Video 100 % generado cuesta US$3–32 por cápsula; híbrido ≈ US$0.25–0.80. |
| 9 | Control de calidad = reproducir y revisar a mano | **Compuertas automáticas** que el bot verifica (sección 5); revisión humana opcional | Mj no quiere estar presente. |
| 10 | Publicación no contemplada / "no publicar hasta revisión" | **YouTube automático** (Data API `videos.insert`, público o `publishAt`); ~~TikTok como borrador~~ → sin TikTok: enlace al TikTok de Mj en la descripción | Direct Post de TikTok sin auditoría solo permite `SELF_ONLY`. |
| 11 | Estados BORRADOR→…→FINAL con aprobaciones humanas | Estados de máquina con criterio automático (sección 4) | Avance sin bloqueo humano. |
| 12 | Plantilla `storyboard.template.json` | **`templates/storyboard_vertical.template.json`** con `arc`, `trend_source`, `voice`, `cortinilla_fuentes`, `publicacion` | Soporta el arco y la automatización. |
| 13 | Medios descargados manualmente (`scene_001.mp4`) | `frames/scene_NNN.png` generados por el pipeline; `.mp4` solo para el gancho opcional | Coherente con la ruta por defecto. |
| 14 | Checklist de 1–3 min | Checklist = compuertas de la sección 5 (el archivo antiguo queda como referencia) | Duración y formato nuevos. |

## 3. Ruta técnica por defecto (sin clicks)
1. **Tendencias** — RSS `https://trends.google.com/trending/rss?geo=MX` (+ES, US, AR), feeds ScienceDaily/Phys.org/EurekAlert, backlog atemporal. Mezcla 70 % atemporal / 30 % tendencia. (pytrends: no usar.)
2. **Guion** — LLM rellena `storyboard_vertical.template.json` (arco completo, ≤12 palabras en la primera frase, una idea, ninguna cifra sin fuente).
3. **Fuentes** — cada DOI se verifica contra Crossref (`api.crossref.org/works/<doi>`); si no resuelve, la fuente y la afirmación se eliminan o el guion se regenera.
4. **Imágenes** — 8–12 frames 1080×1920 con estilo fijo (papel recortado / miniatura) y semilla de estilo. Proveedor intercambiable: API de imagen con clave de Mj (opción recomendada) o modelo local/gratuito. Sin imagen → no se publica (no placeholders en producción).
5. **Gancho animado (opcional)** — solo si `ANIMATED_HOOK_API` tiene créditos; si falla, se usa Ken Burns sin bloquear.
6. **Voz** — edge-tts → si falla, Chirp 3 HD. Ritmo `rate` ajustable para caber en 60–90 s.
7. **Subtítulos** — SRT de 1–3 palabras desde *WordBoundary*, puntuación recuperada del guion, quemados en el tercio inferior (fuera del 20 % inferior).
8. **Montaje** — `scripts/montar_capsula.py`: Ken Burns (zoompan alternando in/out), cortinilla de fuentes, música opcional con *ducking* (`sidechaincompress`), `loudnorm` −14 LUFS, H.264 30 fps.
9. **Publicación** y **métricas** (secciones 6 y 7).

## 4. Pipeline diario y estados (hora CDMX)
| Hora | Estado alcanzado | Criterio automático |
|---|---|---|
| 05:00 | `TEMA_ELEGIDO` | Puntaje ≥6/10 y no sensible/tragedia |
| 05:15 | `GUION_OK` | `validar_storyboard.py` sin errores |
| 05:20 | `FUENTES_VERIFICADAS` | Todos los DOI resuelven (`--check-doi`) |
| 05:30 | `MEDIOS_OK` | Existe cada `asset_filename`, 1080×1920 |
| 05:45 | `RENDER_OK` | MP4 generado |
| 05:50 | `QA_OK` | Todas las compuertas de la sección 5 |
| 06:00 | `PREVIEW_ENVIADO` (opcional) | Si Mj responde "no" antes de la publicación, se cancela; el silencio = aprobación |
| 12:00–14:00 o 19:00–21:00 | `PUBLICADO_YT` / `BORRADOR_TT` | IDs devueltos por las APIs |
| +24 h, +72 h, +7 d | `METRICAS_n` | Registro en SQLite |
Fallo en cualquier compuerta → reintento (máx. 2) con la variable culpable (p. ej. `rate`, otro tema del backlog) → si persiste, `FALLIDO` y se publica una cápsula de reserva del backlog ya renderizada.

## 5. Compuertas de calidad (el bot las verifica solo)
- **Fuentes:** 1–4 fuentes; DOI resuelve en Crossref; cada `source_id` existe; escenas con cifras tienen `source_ids`.
- **Arco:** primera escena `hook_medias_res`; existen `desarrollo`, `cierre_historia`, `reflexion_o_pregunta`; cortinilla 5–6 s.
- **Duración:** 60 ≤ ffprobe ≤ 90 s (el montador sale con código 2 si no).
- **Formato:** 1080×1920, 30 fps, H.264 + AAC, `faststart`.
- **Audio:** −14 LUFS integrados (±1), TP ≤ −1.5 dB.
- **Subtítulos:** ≤3 palabras por bloque, sin solapes, fuente ≥ ~60 px efectivos con contorno, centrados en zona segura (no en el 20 % inferior ni bajo la columna derecha de botones).
- **Zonas seguras:** texto de pantalla y cortinilla dentro de 8 %–85 % horizontal y 10 %–80 % vertical.
- **Divulgación:** aviso "imágenes IA / voz sintética" en cortinilla; `is_aigc` (TikTok) y contenido sintético (YouTube).

## 6. Publicación
- **YouTube:** Data API v3 `videos.insert` (OAuth de la cuenta del canal de Mj, una sola vez), `privacyStatus=public` o `publishAt`; título buscable + `#Shorts`; fuentes completas en la descripción.
- **TikTok:** ~~Content Posting API en modo **upload/borrador** (llega al inbox; Mj publica con un toque) **o** un scheduler ya auditado (Buffer/Metricool/Later, por verificar). Direct Post solo tras auditoría (poco probable para uso propio). Fuentes en comentario fijado.~~ **Corrección 2026-10-24 (Mj): no se crea cuenta nueva de TikTok; no se publica en TikTok desde el sistema. Cada descripción de YouTube enlaza al TikTok existente de Mj (`CAPCOT_TIKTOK_HANDLE`, handle pendiente). TikTok desactivado por defecto en publicar.py.**

## 7. Ciclo de métricas (semanal, domingo)
- Recolecta YouTube Analytics (`views`, `averageViewDuration`, `averageViewPercentage`, `likes`, `comments`, `shares`, `subscribersGained`) (TikTok: fuera de alcance).
- Puntaje = 0.4·retención + 0.3·(compartidos+guardados)/vistas + 0.2·comentarios/vistas + 0.1·subs/vistas.
- **Una sola variable por semana** (tipo de gancho, estilo visual, duración, voz, horario, tendencia vs. atemporal); 80 % explotación / 20 % exploración; el cambio y su resultado se anotan en `avances/`.

## 8. Lo que requiere a Mj (una sola vez)
1. OAuth de YouTube (proyecto Google Cloud + canal) para Data/Analytics API.
2. ~~App TikTok for Developers~~ — solo el handle del TikTok de Mj para el enlace.
3. Clave de API de imagen (proveedor a elegir) y, opcional, Google Cloud TTS (Chirp) y API de video para el gancho.
4. Música con licencia (YouTube Audio Library / Pixabay) en una carpeta local.

## 9. Prototipo probado (2026-10-24)
`scripts/validar_storyboard.py` + `scripts/montar_capsula.py` + `proyectos/demo-001/` (Tunguska 1908, 3 DOI verificados). Render en `/workspace/imaginantes/demo-001.mp4`: 84.37 s, 1080×1920, 30 fps, H.264/AAC, −14.1 LUFS. Frames = placeholders (Pillow).
Uso:
```
python3 scripts/validar_storyboard.py proyectos/<id>/storyboard.json --check-doi
python3 scripts/montar_capsula.py proyectos/<id>/storyboard.json -o /workspace/imaginantes/<id>.mp4
```
Pendiente de implementar: ingesta de tendencias, generador de guion LLM, adaptador de imagen, publicador YT/TikTok, colector de métricas, orquestador diario (cron/rutina).

---
## Addendum 2026-10-24 (Grok Bot, feedback de Mj sobre la cápsula El Niño)
- **Canal:** Datos y ociosidades · @datosyociosidades · YouTube ID UCU2ZI-6pBJEr9aSFsF6bxLw. Sin números en nombres/handles.
- **Formato:** 9:16 1080x1920, 30 fps, h264/aac, **75–95 s** (QA acepta 60–95), −14 LUFS, subtítulos abajo ≤3 palabras.
- **Línea editorial:** periodismo informativo-narrativo; estructura Imaginantes gancho → ancla → relato (3 beats) → giro → cierre
  → reflexión/pregunta + firma ("Esto fue Datos y ociosidades."); solo hechos respaldados por fuentes verificadas; dramatizaciones
  solo visuales y marcadas.
- **Voz:** edge-tts es-MX-JorgeNeural, rate +8 % (rango +6/+10), pitch −2 Hz. **Narración casi continua:** pausas 0.3–0.6 s entre
  frases y entre bloques; nada de escenas mudas largas. Si falta duración, se agrega información respaldada, nunca silencio.
- **Audio:** ambiente + música bajo la voz (camas a −38/−40 LUFS vs voz −16, sidechain ducking). Audio sintético o CC0 documentado.
- **Cortinilla final (5–7 s):** "Fuentes" con citas reales (1–4), aviso IA, firma del canal.
- **Publicación:** cada cápsula genera `metadata.json` (título, descripción con fuentes, hashtags, enlace al TikTok de Mj) que usa publicar.py.
- **Estilos:** rotación automática según docs/ESTILOS_VISUALES.md.


## Actualización 2026-10-24 (10:35, Mj)
**Corrección 2026-10-24 (Mj): no se crea cuenta nueva de TikTok; no se publica en TikTok desde el sistema. Cada descripción de YouTube enlaza al TikTok existente de Mj (`CAPCOT_TIKTOK_HANDLE`, handle pendiente). TikTok desactivado por defecto en publicar.py.**
- **Monetización (meta ~5 dic 2026):** YPP exige 1,000 suscriptores + 10 M vistas válidas de Shorts en 90 días, **o** 1,000 suscriptores + 4,000 h de videos largos públicos en 12 meses (support.google.com/youtube/answer/72851, verificado 2026-10-24). Metas semanales en `scripts/metricas.py metas`.
- **Videos largos (1–2):** `scripts/compilar_largo.py` une cápsulas en 16:9 1920×1080 (fondo desenfocado, tarjetas de capítulo, `capitulos.txt`). Largo 1: «El clima en historias» (El Niño + cápsulas de clima/mar, 8–12 cápsulas ≈ 12–16 min) a mediados de noviembre. Largo 2: «Historias de la ciencia que no te contaron» (mejores cápsulas por retención, 10–15) a inicios de diciembre. Sus horas son las únicas que cuentan para la ruta de 4,000 h.
- **Orquestador:** `capsula_diaria.py` = tendencias → guion (LLM gratuito Gemini Flash/Groq o manual) → estilo (revisión **diaria** de estilos virales) → frames → QA → paquete con `guion_mj.md` y `resumen.json`. No publica.
- **Voz:** es-MX-JorgeNeural +11 % (rango +10/+12). Receta portátil: `docs/RECETA_CAPSULA.md`.


### Corrección 2026-10-24 10:46 (Mj)
- Voz por defecto: es-MX-JorgeNeural **+14%** (antes +11%). El Niño v4 = referencia.
- **Cancelado** `guion_mj.md` / versión para la voz de Mj (otro proyecto): desconectado de `capsula_diaria.py`; el script se movió a `docs/obsoleto/guion_mj.py` con nota.
- TikTok fijo: https://www.tiktok.com/@datosyociosidades (cuenta existente; CAPCOT_TIKTOK_HANDLE solo para sobreescribir).
