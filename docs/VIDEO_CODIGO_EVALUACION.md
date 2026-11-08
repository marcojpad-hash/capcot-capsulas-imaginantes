# Video = código, sin modelo de video — evaluación para CAPCOT

Verificado 2026-11-07/08 en GitHub (metadatos por API + README completo de cada repo)
y con pruebas en esta VM (Node v24.22.1, ffmpeg 8.1.2, Python 3.12.3, sin Chrome,
sin GPU). No se instaló nada.

Contexto: CAPCOT necesita vertical 9:16 1080×1920, 60–90 s, español es-MX,
voz oficial es-MX-JorgeNeural, fuentes verificadas, montaje sin tokens de Muse
(límite semanal al 100%, reinicio 13 nov). Pecas no corre Claude Code; usa
Gemini/Groq por conectores. El montaje oficial lo hace Imaginantes.

## Hallazgo previo que cambia la evaluación

**edge-tts NO funciona en esta VM.** Probado dos veces (7-nov 21:57 y 8-nov 04:20):
`SSL: WRONG_VERSION_NUMBER` contra speech.platform.bing.com:443. El servicio
de voz de Microsoft no responde desde aquí. Cualquier herramienta cuya voz
dependa de edge-tts no puede sintetizar voz en esta máquina. La voz JorgeNeural
sigue estando solo en Imaginantes / el box.

**Chrome tampoco está instalado** (lo necesitan explainroo, ai-video/HyperFrames
y hyperframes). Se puede instalar (`npx playwright install chromium`), pero hoy
no está.

## 1. danbaruka/claude-code-ai-video — 1 ★, 0 forks, MIT, creado 31-oct-2026

**Qué hace:** skill de Claude Code que convierte un JSON de 60–120 líneas en
un Short vertical: voz, captions sincronizadas por palabra, 16 escenas
(título, contador, lista, pasos, versus, logos, teléfono, navegador, imagen,
chat, alerta, gráfico, terminal, cita, tarjeta), música, revisión de texto
desbordado en una sola "contact sheet" y MP4. Mezcla final a −14 LUFS.
La escena `chiffre` trae campo `source` para citar la fuente del número
(compatible con la regla CAPCOT de no inventar datos).

**Necesita:** Claude Code (el skill es Markdown; los scripts son node planos,
así que cualquier agente que lea SKILL.md puede seguirlo), Node 18+, ffmpeg,
Python 3, Chrome headless (HyperFrames). Voz: **edge-tts** (gratis, cientos de
voces incl. español; es-MX-JorgeNeural es voz edge-tts en principio).

**Español / 9:16:** sí, ambos (vertical Shorts; "muchos otros idiomas").

**Costo:** el repo afirma ~65.000 tokens por video de 60 s en una prueba ciega
con Claude (incluye leer la skill), 2–3 min por video. Plausible: el agente
solo escribe el JSON y revisa una imagen.

**Corre en esta VM:** NO tal cual — la voz (edge-tts) está bloqueada (ver arriba).
Sin voz no hay video. Alternativa: suministrar la narración grabada.

**Problemas:** 1 estrella, una semana de vida, sin adopción; estilo único
"blanco animado limpio", que NO es el estilo CAPCOT (linograbado, linea_fina);
escenas orientadas a tech/cripto aunque genéricas.

## 2. lemomo-ai/lemo-opuscar — 13.439 ★, 1.569 forks, MIT, muy activo

**Qué hace:** 66 estilos de cine hechos en código (canvas/WebGL frame por
frame, música de librerías gratuitas, narración TTS). Incluye **woodcut
(linograbado), risograph, ukiyo-e, chalkboard, whiteboard explainer, data
storytelling, caption news** y un flujo para crear un estilo propio
("Make a style your own", con frame de prueba y demo de 15–30 s).

**Necesita:** Claude Code; Node 20+, **ffmpeg 7+** (la VM tiene 8.1.2 ✓),
Python 3.11+. Salida por defecto 1920×1080 24 fps; vertical 1080×1920 a pedido.
**Aviso del README: los estilos están ajustados para Claude Opus 5.5; otros
modelos pueden no reproducirlos bien.**

**Voz:** por defecto Kokoro (local, gratis). No JorgeNeural.

**Español / 9:16:** vertical sí; español no garantizado (los estilos son
visuales; la narración depende del TTS).

**Costo:** el más caro de los seis: **30–60 min y "una buena cantidad de
tokens" por película**, según el propio README. Inviable como pipeline barato.

**Veredicto parcial:** mejor biblioteca de estilos para CAPCOT y el único con
flujo de estilo propio (se podría crear el estilo "linograbado CAPCOT"), pero
no sirve como pipeline barato: caro en tiempo/tokens y ajustado a Opus 5.5.
Útil como referencia de estilos (sus STYLE.md son prompts de estilo reusables).

## 3. vincentsch/explainroo — 1.017 ★, 96 forks, MIT, activo (último push 20-oct)

**Qué hace:** videos explicativos narrados. El agente escribe dos archivos:
`script.md` (lo que dice la voz) y `scenes.js` (dibujos en JavaScript, cada uno
puede aparecer en una palabra del guion). Voz local **Kokoro** (54 voces,
español incluido, sin cuenta ni API key), timing de palabras con **Whisper**,
renderer canvas en Chrome, música propia, efectos, ffmpeg a MP4. Además:
subtítulos .srt/.vtt, portada, capítulos de YouTube, 6 looks
(paper, clean, chalk, blueprint, midnight, editorial), tamaño TikTok 9:16 con
captions palabra por palabra y texto fuera de la zona de botones. Watermark
desactivable.

**Necesita:** Node 20.11+, ffmpeg, **Chrome/Chromium (no instalado, instalable)**,
primera instalación descarga ~400 MB de modelos de voz y timing. Sin GPU.
Desarrollado en Linux, con tests en Linux/macOS/Windows. **Funciona con Claude
Code, Codex, Pi y otros agentes** — no es exclusivo de Claude Code.

**Voz:** Kokoro en español (requiere espeak-ng para español). NO es
JorgeNeural. Alternativas del propio README: ElevenLabs o grabar la narración.
Para borradores, la voz Kokoro en español sirve; la voz oficial seguiría en
Imaginantes.

**Español / 9:16:** sí, ambos, verificados en el README.

**Costo:** sin cifra declarada. El agente escribe guion + código de escenas
(más tokens que el JSON de ai-video, mucho menos que un video HTML completo).
Render local, sin tokens de Muse. Sin API keys, todo local.

**Corre en esta VM:** sí con dos instalaciones (Chromium + modelos ~400 MB).
Es el más maduro y el único pensado para varios agentes.

## 4. TheOneTrueNiz/animate — 0 ★, 0 forks, MIT

**Qué hace:** animación procedural en un solo `<canvas>`: 7 estilos
(cut paper, crosshatch ink, **riso**, sketchbook, math, pixel, isometric),
storyboard con aprobación por panel, 9:16/1:1/4:5/16:9 desde una sola pieza,
ejemplo completo de 60 s incluido. Render con navegador headless + ffmpeg.

**Necesita:** Claude Code, Node 18+, Playwright + Chromium, ffmpeg. Voz:
**ElevenLabs (de pago)** o grabación propia. **No hay TTS gratuito.**

**Español / 9:16:** 9:16 sí; español no documentado (depende de la voz).

**Costo:** no declarado. El agente escribe código de escenas (más tokens que
un JSON).

**Veredicto:** estilos interesantes (riso), pero sin voz gratuita y con cero
adopción. Descartado; solo vale la idea del estilo riso.

## 5. kelano86/what-if-animation — 272 ★, 71 forks, MIT

**Qué hace:** episodios animados 2D estilo "What If" (muñecos de palitos):
guion con fórmula de 7 beats, voz y efectos con ElevenLabs, SVG + Remotion,
master a −14 LUFS. **Es el único que documenta correr con un modelo gratis**
(OpenCode + GLM-5.3-Flash Free, $0 de modelo).

**Necesita:** Claude Code u OpenCode, Node 18+, ffmpeg, Python 3.9+,
**clave de ElevenLabs** (152 créditos por episodio; plan gratis 10.000
créditos/mes ≈ 40 episodios, uso no comercial y hay que acreditar a
ElevenLabs).

**Español / 9:16:** no documentados; **duración 15–25 s por episodio**,
demasiado corto para cápsulas de 60–90 s. Un solo estilo, ajeno a CAPCOT.
El propio README advierte: los estilos pintados/texturizados "no son realistas
en puro código; necesitan un modelo de imagen".

**Veredicto:** descartado — duración, estilo y voz de pago no encajan.

## 6a. Sunwood-ai-labs/hyperframes-motion-reel-skill — 179 ★, 24 forks, MIT

**Qué hace:** motion graphics de showreel con HyperFrames (HTML + GSAP + SVG +
Canvas, Apache-2.0), 120 BPM / 60 FPS, transiciones con morphing, audio
generado en código. Vertical 1080×1920 soportado. Duración por defecto 15 s.

**Necesita:** Node LTS, Chrome, ffmpeg + instalar las skills de dominio de
HyperFrames aparte. **No tiene pipeline de narración/TTS: la voz debe
suministrarse como archivo.** Repo de un solo día (29-sep), sin actividad
después.

**Veredicto:** no es una herramienta de cápsulas — es un motor de motion
graphics sin voz ni estructura de historia. Solo sirve como referencia de
motion (y es el renderer que usa ai-video por debajo).

## 6b. charlie947/motion-graphics-skills — 602 ★, 75 forks, MIT, 15 skills

**Qué hace:** pack de motion graphics para Claude Code/Codex en Opus 5.5:
brand-intake → brief → launch-video, apple-launch-film, **vox-explainer
(explicador documental 30–60 s)**, animated-chart, milestone-reveal,
reel-export a 1080×1920, etc. Reglas de casa que encajan con CAPCOT:
**"Facts first: cada nombre, fecha y número en pantalla viene de una lista
que tú apruebas. Nada inventado."** Revisión de un frame por plano antes de
exportar.

**Necesita:** Claude Code en Opus 5.5; export MP4 con HyperFrames o
ffmpeg + Chrome. Sin API keys. La voz no está definida como pipeline (el
ejemplo de vox-explainer "añadió una voz" sin decir cómo).

**Español / 9:16:** reel-export a 1080×1920 sí; español no garantizado.

**Veredicto:** referencia, no pipeline completo. Lo aprovechable: la
estructura de vox-explainer y las reglas de motion (las mismas que la skill de
Emil Kowalski: revisar un frame por plano, hechos aprobados antes de dibujar).

## Ranking para CAPCOT

| # | Herramienta | Por qué |
|---|---|---|
| 1 | **explainroo** | Probar primero. Maduro, gratis de verdad, multi-agente (no exige Claude Code), español, 9:16, subtítulos, Linux. La voz es Kokoro, no JorgeNeural — aceptable para borradores. |
| 2 | **ai-video (danbaruka)** | Mejor economía de tokens (~65k/video), pero la voz edge-tts está bloqueada en esta VM y tiene 1 estrella y estilo único blanco. Segunda prueba solo si se resuelve la voz. |
| 3 | **lemo-opuscar** | Mejor biblioteca de estilos (woodcut/riso) + flujo de estilo propio. No como pipeline barato (30–60 min, muchos tokens, ajustado a Opus 5.5). Referencia de estilos. |
| 4 | **motion-graphics-skills** | Referencia: vox-explainer y reglas de motion. Sin pipeline de voz definido. |
| 5 | animate | Descartado: sin voz gratuita, 0 estrellas. |
| 6 | what-if-animation | Descartado: 15–25 s, estilo ajeno, voz de pago. |
| 7 | hyperframes-motion-reel | Descartado como cápsula: sin voz ni historia; solo motor de motion. |

## Honestidad sobre el límite común

Ninguna de estas herramientas dibuja ilustraciones estilo linograbado: dibujan
gráficos vectoriales/canvas en código. Lo que reemplazan es la **generación de
video** (movimiento + captions + voz + MP4), no la ilustración. El look
ilustrado de CAPCOT seguiría necesitando un modelo de imagen o los frames
actuales. El QA oficial y el montaje oficial siguen siendo de Imaginantes;
esto sería pipeline de borradores sin tokens.

## Plan concreto para probar explainroo (el #1)

Material de prueba: la cápsula Barreleye (narraciones ya verificadas contra
MBARI, 7 escenas, 69 s, proyecto 2026-11-07_barreleye-4k).

1. Instalar (una vez, sin tokens de Muse):
   `git clone https://github.com/vincentsch/explainroo.git && cd explainroo && npm install && node bin/explainroo.js doctor --fetch`
   (descarga ~400 MB de modelos de voz/timing) + `npx playwright install chromium`
   + `sudo apt install espeak-ng` (para español).
2. El agente (Gemini/Groq por conectores, siguiendo AGENTS.md de explainroo)
   escribe `videos/barreleye/script.md` con las 7 narraciones en español y
   `videos/barreleye/scenes.js` con un dibujo por escena, `video.json` con
   `"size": "tiktok"` (9:16) y look `"paper"`.
3. Render: `explainroo render videos/barreleye --size tiktok` → MP4 + .srt/.vtt
   + portada. Revisar con los stills y el chequeo de layout que da la
   herramienta.
4. Resultado esperado: borrador de 69 s con voz Kokoro en español (no
   JorgeNeural), captions palabra por palabra, sin gastar tokens de Muse en
   el render. Si el borrador convence, el montaje oficial con voz JorgeNeural
   sigue siendo de Imaginantes.

Nota para el padre: Marco tiene razón en que esta familia ("video = código")
no se había propuesto antes — las evaluaciones previas cubrieron montaje
(OpenMontage), capas (Clayzo) y agentes (ECC, dsh), pero no estas skills de
video-por-código. La corrección es este informe, no una promesa nueva.
