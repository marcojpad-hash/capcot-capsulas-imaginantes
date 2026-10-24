<!-- copia corregida de referencias_estilo/128353f2….md (2026-10-24) -->
# CAPCOT – Comparativa de herramientas (24 oct 2026)

Supuestos: cápsula de 75 s, vertical 9:16, 720p. Costo = precio API de lista × 75 s, **sin repeticiones**. En la práctica, cuenta ×2 a ×3 en video por las tomas descartadas. "NV" = no verificado en esta revisión.

## Repo GitHub
`marcojpad-hash/capcot-capsulas-imaginantes` → **404 Not Found** con el conector GitHub (user-GitHub-xai). O el nombre es otro o el conector no tiene acceso al repo privado. No se leyó nada.

## Video IA
| Herramienta | $/s (API) | ~75 s | Clip máx. | API | Notas / límites |
|---|---|---|---|---|---|
| Grok Imagine Video 1.5-lite | 0.03 (720p) | $2.25 | NV | Sí (xAI) | Imagen de entrada a $0.01; 10 req/s en el modelo 1.5 [xAI] |
| Grok Imagine Video 1.5 | 0.14 (720p) / 0.08 (480p) | $10.50 / $6 | NV | Sí | Audio con voces preestablecidas gratis [xAI] |
| Hailuo 2.3 Fast / 2.3 | 0.0317 / 0.0467 (768p) | $2.38 / $3.50 | 6 s | Sí (MiniMax) | Sin audio nativo [aivideocosts, pixo] |
| Veo 3.1 Lite / Fast / Std | 0.05 / 0.10 / 0.40 (720p) | $3.75 / $7.50 / $30 | ~8 s | Sí (Gemini) | Siempre con audio; marca SynthID (NV en detalle) [viralfaceless, pixo] |
| Kling 3.0 | 0.084 sin audio / 0.126 con audio (720p) | $6.30 / $9.45 | 15 s | Sí | Buena estilización y movimiento humano [Kling, aivideocosts] |
| Runway Gen-4.5 | 0.12 | $9.00 | 5–10 s | Sí | Plan app desde $15/mes [Runway dev, pixo] |
| Seedance 2.0 | NV | NV | 4–15 s | BytePlus | [pixo] |
| Sora 2 | — | — | — | API cerrada el 24 sep 2026 [pixo] | Descartar |
| Luma, Pika | NV | NV | NV | NV | No verificados en esta revisión |

Uso comercial y marca de agua: con las API de pago normalmente no hay marca visible, pero Google usa SynthID (marca invisible). **NV**: revisar los términos de cada proveedor antes de monetizar. TikTok pide `is_aigc=true` y YouTube `containsSyntheticMedia` para contenido IA.

## Imagen con personaje consistente
| Herramienta | Precio | Consistencia | Fuente |
|---|---|---|---|
| Nano Banana 2.1 (Google) | $0.0336/img 1K; batch $0.0168 | Imagen de referencia + instrucción de edición | tech-insider (oct 2026) |
| Nano Banana Pro | $0.134/img | Alta (NV) | ídem |
| Grok Imagine Image | $0.02/img (2.0: $0.04–0.08) | Edición con imagen de entrada | docs.x.ai |
Una historia de ~15 imágenes fijas cuesta entre $0.30 y $0.60.

## Voz en español
| Herramienta | Precio | Por cápsula (~1,100 caracteres) | Límite por petición | Fuente |
|---|---|---|---|---|
| ElevenLabs v4 / v3 / Multilingual v2 | $0.08/1k caracteres | ~$0.09 | v4 10k, v3 3k–5k, v2 10k | elevenlabs.io/pricing/api |
| ElevenLabs v4 Turbo / Flash | $0.04/1k caracteres | ~$0.045 | Flash 40k | ídem |
| ElevenLabs Scribe (transcripción para subtítulos) | $0.22/h | <$0.01 | | ídem |
Todos los modelos listados soportan español. El costo de clonar la voz de Mj depende del plan (NV).

## Subtítulos y edición
| Herramienta | Costo | API | Notas |
|---|---|---|---|
| ffmpeg + subtítulos ASS (estilo CapCut) | $0 | Script local | Máxima automatización |
| HeyGen HyperFrames | Open source Apache 2.0, render local gratis; existe render en la nube (`POST /v3/hyperframes/renders`, precio NV) | Sí | Plantillas HTML que se renderizan a video |
| Submagic | Incluye 10 min API/mes (Starter/Pro); paquete de 500 min $75 (~$0.15/min) | Sí | Subtítulos estilo viral |
| CapCut | App gratis o Pro | Sin API pública documentada | Solo manual |

## Publicación
**TikTok:** **Corrección 2026-10-24 (Mj): no se crea cuenta nueva de TikTok; no se publica en TikTok desde el sistema. Cada descripción de YouTube enlaza al TikTok existente de Mj (`CAPCOT_TIKTOK_HANDLE`, handle pendiente). TikTok desactivado por defecto en publicar.py.** (La info de Content Posting API queda fuera de alcance.)

**YouTube (Data API v3)**
- Crear un proyecto en Google Cloud, habilitar YouTube Data API v3 y configurar la pantalla de consentimiento OAuth con el scope `youtube.upload`. Guardar el refresh token.
- `videos.insert` cuesta 1 unidad de una cuota propia: 100 subidas/día por defecto. Otros endpoints: 10,000 unidades/día (por ejemplo, `thumbnails.set` cuesta 50).
- Ya **no** se obliga a subir en privado desde proyectos no verificados (Google, issue 572902667, 13 oct 2026). Se puede programar con `publishAt`.
- Si la app OAuth queda en modo "testing", el refresh token caduca a los 7 días (NV para 2026; conviene publicarla en producción).

## Flujos recomendados
**Barato (~$0.6–6 por cápsula)**
1. Guion y versos (LLM).
2. Voz con ElevenLabs v4 Turbo (~$0.05).
3. Elegir entre:
   - (a) Historia con imágenes fijas: Nano Banana 2.1 o Grok Image con referencia del personaje, ~15 imágenes (~$0.5), más efecto Ken Burns en ffmpeg. Total ≈ **$0.6**.
   - (b) Animación: Grok Imagine 1.5-lite 720p o Hailuo 2.3 Fast desde esas imágenes, 75 s ≈ $2.3, ×2 por repeticiones ≈ **$5**.
4. Subtítulos: Scribe o Whisper, luego ASS + ffmpeg o HyperFrames ($0).
5. Publicación: subida a YouTube (privado hasta aprobación); descripción con enlace al TikTok de Mj.

**Premium (~$20–40 por cápsula)**
- Imágenes clave con Nano Banana Pro.
- Video con Kling 3.0 (15 s, buena consistencia) o Veo 3.1 Fast, ~$7–10, ×2–3 por repeticiones.
- Voz con ElevenLabs v4 o la voz clonada de Mj.
- Subtítulos con Submagic API.
- Publicación igual que en el flujo barato (sin TikTok).

## Fuentes
docs.x.ai/developers/pricing · aivideocosts.fyi (act. 23-oct-2026) · kling.ai/document-api/pricing · dev.runway.com/pricing · pixo.video/blog/best-ai-video-generators · viralfaceless.io · tech-insider.org (Nano Banana 2.1) · elevenlabs.io/pricing/api · submagic.co/api · developers.tiktok.com/docs/en/content-sharing-guidelines · outstand.so/blog/tiktok-content-posting-api · developers.google.com/youtube/v3 (videos/insert, quota) · issuetracker.google.com/issues/572902667
