# Estrategia viral y pipeline automatizado: micro-cápsulas científicas al estilo *Imaginantes*

> Fecha: 24 oct 2026. Convención: **[F]** = dato con fuente (enlace al final de cada sección) · **[I]** = inferencia o recomendación propia.
> Base: `ANALISIS_ESTILO_IMAGINANTES.md` (1 min, tres tiempos, prosa poética) y `ANALISIS_CLIPS_MJ.md` (la imagen narra, la voz eleva a idea, gancho paradójico, cierre filosófico, voz dosificada).

## 1. Qué funciona hoy en el short-form científico
- **Gancho inmediato.** Kurzgesagt adaptó su estilo a Shorts y TikTok así: empieza de inmediato, comprime la narrativa y diseña el loop para que el final empalme con el inicio. [F: Forbes 2024]
- **Pregunta o dato sorprendente, demostración rápida y recompensa clara.** El laboratorio de Columbia (Venkataraman/Nuckolls) documentó millones de vistas con la fórmula gancho, humor y desenlace. [F: Prindle et al., NSF PAR]
- **Duración.** Una revisión de alcance en JCOM (2025) encontró que las demostraciones funcionan bien alrededor de 30 s y los formatos de explicación alrededor de 1 min. También recomienda subtítulos y un presentador o voz reconocible. [F: JCOM]
- **La retención pesa más que la duración.** Un video de 45 s con 70 % de finalización supera a uno de 15 s con 40 %. [F: Digital Applied]
- **Por plataforma.** En YouTube Shorts conviene un título y palabras clave buscables. En TikTok importan más el entretenimiento, los trends y la personalidad. [F: Digital Applied]
- **Referentes con cifras citadas:**
  - Kurzgesagt: más de 23 M de suscriptores en YouTube. [F]
  - Zack D. Films: 29.3 M de suscriptores y 81 mil M de vistas según vidIQ. Es entretenimiento con apariencia de ciencia, con animación 3D corta y gancho "what happens if…". [F]
  - QuantumFracture (español): 2.8 M de suscriptores y 220 M de vistas, según su página de LinkedIn. [F]
- **Advertencia sobre ingresos.** En Howtown, un Short con 2.6 M de vistas generó US$272, frente a US$5,260 de un video largo. Los Shorts sirven para crecer la audiencia, no para monetizar. [F: Nieman Lab]
- **[I] Formatos en serie.** Conviene una serie con nombre y número ("Imaginantes de la ciencia #12"), una plantilla visual fija, la misma voz y la misma cortinilla. También ayudan las preguntas que invitan a comentar y partes 1 y 2 cuando la historia lo permite.

Fuentes: [Forbes/Kurzgesagt](https://www.forbes.com/sites/danidiplacido/2024/10/24/kurzgesagt-in-a-nutshell-creator-talks-youtube-tiktok-and-optimistic-nihilism/) · [Prindle et al.](https://par.nsf.gov/servlets/purl/10512807) · [JCOM 2025](https://jcom.sissa.it/article/pubid/JCOM_2403_2025_V01/) · [Digital Applied](https://www.digitalapplied.com/blog/short-form-video-strategy-shorts-tiktok-reels-2026) · [vidIQ Zack D. Films](https://vidiq.com/youtube-stats/channel/@zackdfilms/) · [QuantumFracture](https://linkedin.com/company/quantum-fracture) · [Nieman Lab](https://www.niemanlab.org/2025/01/what-the-creators-of-howtown-learned-in-their-first-few-months-on-youtube/) · [Computers in Human Behavior 2025, éxito de la divulgación científica por plataforma](https://doi.org/10.1016/j.chb.2025.108866) (no se pudo abrir; queda solo como referencia)

## 2. Plantilla de arco y guion (60–90 s, unas 150–210 palabras)
| Tiempo | Bloque | Qué pasa | Imagen |
|---|---|---|---|
| 0–3 s | **Gancho in medias res** | Se entra en plena acción: "1908. Siberia. Un bosque entero cae… y nadie oyó llegar nada." También sirve una paradoja como la del "perro de papel". | El frame más potente, con texto en pantalla de máximo 6 palabras |
| 3–15 s | **Contexto mínimo** | Quién, dónde y qué estaba en juego | 2–3 frames con efecto Ken Burns |
| 15–50 s | **Desarrollo y tensión** | Pistas, hipótesis y un giro con el dato científico | Un cambio de frame cada 2–4 s; la imagen cuenta y la voz eleva la idea |
| 50–70 s | **Cierre de la historia** | Lo que hoy se sabe, con una cifra citada | Plano de resolución |
| 70–80 s | **Reflexión ontológica o pregunta abierta** | "¿Y si lo que llamamos ___ fuera solo ___?" La voz baja, hay silencio y música | Imagen contemplativa que empalma con el gancho (loop) |
| 80–88 s | **Cortinilla de fuentes** | Fuentes en pantalla | Ver sección 6 |

Reglas del guion [I]:
- Una sola idea por cápsula y cero relleno.
- Metáfora y personificación, como en los clips de Mj.
- Ninguna cifra sin una fuente en la cortinilla.
- Primera frase de máximo 12 palabras.
- La pregunta final debe invitar a comentar.

## 3. Selección automática de temas con tendencias
- **API oficial de Google Trends (alfa).** Se anunció el 24 de julio de 2025 y sigue siendo alfa por invitación, con formulario de solicitud. Ofrece 5 años de datos, agregación diaria, semanal, mensual y anual, y datos por región y subregión con escala consistente. En 2026 todavía hay solicitantes sin respuesta. Conviene solicitarla, pero no depender de ella. [F]
- **pytrends.** Se archivó el 17 de abril de 2025 y da errores 429 frecuentes. **No usarla en producción.** trendspy no se actualiza desde diciembre de 2024. [F: DEV]
- **RSS "Trending now".** `https://trends.google.com/trending/rss?geo=MX` es público. Trae el título, el tráfico aproximado y las noticias relacionadas, pero no la categoría. Es la mejor opción gratuita. [F]
- **TikTok Creative Center.** No tiene API pública oficial. Se consulta a mano o con scrapers de terceros como Apify, que tienen riesgo legal y de términos de servicio. [F]
- **Algoritmo diario [I]:**
  1. Leer el RSS de MX, ES, US y AR, más Wikipedia "most read" y feeds como ScienceDaily, Phys.org y EurekAlert.
  2. Pedir a un LLM que filtre lo que tiene "ángulo científico narrable" y lo puntúe de 0 a 10 según cinco criterios: tendencia, historia con arco, posibilidad de imagen, fuentes revisadas por pares y que no sea tragedia ni tema sensible.
  3. Mezcla del día: 70 % de temas atemporales de un backlog curado y 30 % ligados a una tendencia.
  4. Guardar todo en una base de datos (SQLite o Notion).

## 4. Pipeline barato: frames, Ken Burns, TTS, subtítulos y música
1. **Guion:** LLM con la plantilla de la sección 2, que devuelve un JSON con escenas, prompts de imagen y fuentes con DOI/URL. Las fuentes se verifican automáticamente (que el DOI resuelva por HTTP); si una falla, se descarta.
2. **Imágenes:** 8–15 frames verticales 1080×1920 con estilo fijo (papel recortado o miniatura, según los clips de Mj) y una "semilla de estilo" constante.
3. **Voz (TTS):**

| Opción | Costo | Calidad en español [I salvo F] |
|---|---|---|
| edge-tts (voces neurales de Microsoft, p. ej. `es-MX-JorgeNeural`) | Gratis, sin API key [F] | Buena y clara; es la opción "tipo Loquendo" pero natural. Uso no oficial: puede romperse en cualquier momento |
| Google Cloud Chirp 3 HD | 1 M caracteres/mes gratis, luego US$30 por millón [F] | Casi humana. Una cápsula de unos 1,200 caracteres al día suma unos 36 K/mes, así que **queda gratis** |
| Google Standard/WaveNet | US$4 por millón [F] | Correcta |
| ElevenLabs | US$0.04 (Flash/Turbo) a US$0.08 (Multilingual/v3) por 1 K caracteres, es decir, unos US$0.04–0.08 por minuto [F] | La más expresiva y permite clonar la voz de Mj |

4. **Subtítulos animados:**
   - Se transcribe el audio del TTS con whisper / faster-whisper con marcas de tiempo por palabra (`word_timestamps=True`).
   - Se genera un `.ass` estilo karaoke de 1–3 palabras, centrado en el tercio medio-bajo, con resaltado de color en la palabra activa.
   - Se queman con `ffmpeg -vf ass=subs.ass`.
   - Alternativa: como el guion ya existe, se alinea el texto con el audio (forced alignment), lo que evita errores de transcripción.
5. **Ken Burns:** `zoompan` de ffmpeg por imagen (p. ej. `zoompan=z='min(zoom+0.0015,1.15)':d=125:s=1080x1920`), transiciones `xfade` y una ligera textura o grano.
6. **Música:** pistas libres (YouTube Audio Library o Pixabay) con *ducking* bajo la voz (`sidechaincompress`). Se reserva silencio para la reflexión final.
7. **Ensamblado:** script de Python con ffmpeg (más robusto y rápido que moviepy) y una plantilla fija para la cortinilla.

**Si algún día se usa video generado (precios por segundo, oct 2026) [F]:**
- Veo 3.1: US$0.40/s con audio; Fast US$0.10–0.15/s; Lite US$0.05–0.08/s.
- Kling 3.0: US$0.084/s (720p sin audio) a US$0.168/s.
- Runway Gen-4 Turbo: US$0.05/s; Gen-4.5: US$0.12/s.
- MiniMax/Hailuo H3: US$0.08/s (768p) y H3-Max desde US$0.05/s (480p).
- Wan 3.0: US$0.05/s (480p).
- Seedance 2.0 Mini: desde US$0.04/s.
- Grok Imagine Video: US$0.05–0.08/s.
- Sora 2: US$0.10–0.70/s, aunque según InVideo su API se retira el 24 sep 2026.

Un short de 80 s 100 % generado costaría entre US$3.2 y US$32. **[I] La opción híbrida** es usar solo 1–2 planos animados de 5 s (el gancho) con un modelo barato, unos US$0.25–0.80, y el resto con frames estáticos.

Fuentes: [Runway Dev pricing](https://dev.runway.com/pricing) · [modelpick](https://modelpick.dev/media-pricing/) · [InVideo](https://invideo.io/blog/ai-video-model-pricing/) · [fal Veo 3.1](https://fal.ai/models/fal-ai/veo3.1) · [Google TTS pricing](https://cloud.google.com/text-to-speech/pricing) · [ElevenLabs API pricing](https://elevenlabs.io/pricing/api)

## 5. Publicación automática
- **YouTube Data API.** `videos.insert` cuesta 1 unidad en su propio cupo: **100 subidas al día** por defecto. Los proyectos sin verificar **ya no quedan forzados a privado**: se puede publicar como público o programar con `publishAt`. Solo hace falta auditoría para pedir más cupo. Las Shorts se reconocen por formato vertical de 3 minutos o menos [I]. Se recomienda incluir #Shorts. [F: docs y Issue Tracker 572863050]
- **TikTok Content Posting API (Direct Post).**
  - Requiere el scope `video.publish` y consultar `creator_info` antes de cada publicación.
  - **Sin auditoría:** solo se puede publicar como `SELF_ONLY`, con la cuenta en privado y un máximo de 5 usuarios en 24 h.
  - **Tope:** unas 15 publicaciones al día por creador.
  - **Ojo:** las guías **prohíben** clientes que sean "utilidad para subir a cuentas que tú o tu equipo manejan", lo que hace poco probable aprobar la auditoría para un bot de uso propio. La UX exige que el usuario elija la privacidad manualmente.
  - Existe el campo `is_aigc` para marcar contenido generado con IA.
  - **[I] Alternativas:**
    - (a) Upload/draft: se sube al buzón de borradores y Mj publica con un toque desde la app.
    - (b) Un scheduler de terceros ya auditado (p. ej. Buffer, Metricool, Later, que se deben verificar).
    - (c) Subir a privado vía API y cambiar a público a mano.

Fuentes: [YT videos.insert](https://developers.google.com/youtube/v3/docs/videos/insert) · [YT quota](https://developers.google.com/youtube/data/guides/quota_and_compliance_audits) · [Issue 572863050](https://issuetracker.google.com/issues/572863050) · [TikTok guidelines](https://developers.tiktok.com/doc/content-sharing-guidelines) · [TikTok Direct Post](https://developers.tiktok.com/doc/content-posting-api-reference-direct-post)

## 6. Cortinilla de fuentes (buenas prácticas) [I]
- 4–6 s fijos, el doble del tiempo de lectura, con fondo sobrio de la marca de la serie.
- Formato corto: *Autor et al. (año). Revista. DOI*, con 2–4 fuentes como máximo, en tipografía de 36 px o más dentro de la zona segura (evitando el 15 % inferior y la columna derecha de botones en TikTok).
- Repetir las fuentes completas con enlace en la descripción y en un comentario fijado (TikTok no hace clicables los enlaces del caption).
- Priorizar artículos revisados por pares, luego agencias como NASA, OMS o INEGI, y después divulgación de calidad.
- Agregar el aviso "Imágenes generadas con IA; voz sintética" y activar la etiqueta de IA de cada plataforma (`is_aigc` en TikTok y la divulgación de "contenido alterado/sintético" en YouTube).

## 7. Flujo diario automatizado [I]
| Hora (CDMX) | Paso |
|---|---|
| 05:00 | Ingesta de tendencias (RSS de Trends, feeds científicos y backlog) y puntuación |
| 05:15 | Elección del tema, guion JSON y verificación de fuentes (los DOI deben resolver) |
| 05:30 | Generación de imágenes, TTS, subtítulos y ensamblado con ffmpeg; control de calidad automático (duración ≤ 90 s, sonoridad −14 LUFS, texto dentro de la zona segura) |
| 06:00 | **Revisión humana opcional** (recomendada el primer mes): se envía la vista previa a Mj |
| 12:00–14:00 o 19:00–21:00 | Publicación en YouTube (API) y en TikTok (borrador o scheduler); se prueban ambas franjas |
| +24 h, +72 h, +7 d | Recolección de métricas |

## 8. Ciclo de medición y ajuste
- **YouTube Analytics API:**
  - Métricas: `views`, `averageViewDuration`, `averageViewPercentage` (excluye los loops), `likes`, `comments`, `shares`, `subscribersGained`.
  - La métrica de Shorts "visto vs. deslizado" solo aparece en Studio y no está documentada en la API [F: docs de métricas].
- **TikTok:** la Display API (`video.list`) da vistas, likes, comentarios y compartidos de los videos propios. La retención detallada solo aparece en la app [I, verificar].
- **Registro por video:** tema, tipo de gancho, duración, voz, estilo visual, franja horaria, si era tendencia o atemporal, y las métricas.
- **Ajuste semanal [I]:**
  - Cálculo de puntaje = 0.4·retención% + 0.3·(compartidos+guardados)/vistas + 0.2·comentarios/vistas + 0.1·suscriptores/vistas.
  - Un *bandit* (Thompson sampling) reasigna probabilidades entre variantes de gancho, estilo, duración y horario: 80 % lo que funciona y 20 % exploración.
  - El LLM recibe el top y el bottom 5 de la semana para reescribir las reglas del guion.
  - Se cambia una sola variable por experimento.

## 9. Stack más barato recomendado [I]
- **Tendencias:** RSS de Google Trends (gratis), feeds científicos y solicitud de acceso a la API alfa.
- **Guion:** LLM más un verificador de DOI (API de Crossref, gratis).
- **Imágenes:** el modelo más barato con estilo consistente, unas 10 por día.
- **Voz:** Google Chirp 3 HD `es-US`/`es-MX`, que queda dentro de la capa gratuita; edge-tts como respaldo gratuito; ElevenLabs solo para clonar la voz de Mj.
- **Subtítulos:** faster-whisper local (gratis) con archivo `.ass` estilo karaoke.
- **Edición:** ffmpeg (zoompan, xfade, ass, sidechaincompress) en el propio equipo (box).
- **Publicación:** YouTube Data API directa; en TikTok, borrador para publicar con un toque o un scheduler auditado.
- **Métricas:** YouTube Analytics API y TikTok Display API guardadas en SQLite, con reporte semanal.
- **Costo estimado:** prácticamente solo el de las imágenes y el LLM, unos pocos dólares al mes. Agregar un gancho animado de 5 s costaría unos US$0.25–0.80 extra por día.
