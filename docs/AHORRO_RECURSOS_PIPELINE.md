# CAPCOT – Ahorro de recursos en el pipeline (2026-11-01)

> Fuente: patrones de arquitectura de bots de IA en Telegram (borrador en baja resolución + montaje modular con FFmpeg), adaptados a CAPCOT. Se descarta el modelo de paywall/desenfoque/FOMO de esos bots: no aplica al producto CAPCOT.

Reglas de operación obligatorias para **Imaginantes, Grok, ChatGPT** y cualquier modelo que produzca cápsulas.

## 1. Ruta por defecto (siempre, salvo que Mj pida clips animados)
**storyboard → frames estáticos → `scripts/montar_capsula.py` (FFmpeg: Ken Burns zoompan, subtítulos ASS quemados, cama sonora sintética).**
Se prefiere a Flow, Dreamina, Kling o HyperFrames en **todas** las cápsulas.

## 2. Compuerta de borrador (antes de gastar en HD)
1. Frames de borrador a media resolución (540×960) o placeholder:
   `python3 scripts/generar_frames.py proyectos/x/storyboard.json --proveedor placeholder --borrador`
2. Vista previa barata (540×960, preset veryfast, CRF 28):
   `python3 scripts/montar_capsula.py proyectos/x/storyboard.json -o /tmp/preview.mp4 --borrador`
   (montar escala cualquier frame vía zoompan, así que los frames de 540×960 también funcionan sin el flag; el flag solo abarata el MP4).
3. QA del storyboard (guion, orden, tiempos, textos, fuentes).
4. **Solo después del QA aprobado** se generan las imágenes finales 1080×1920 (sin `--borrador`). Una llamada HD por escena, no por iteración.

## 3. Video IA (I2V) – excepción acotada
- Créditos gratis de [CREDITOS_GRATIS_VIDEO.md](CREDITOS_GRATIS_VIDEO.md): **máximo 1–2 insertos de movimiento "héroe" por cápsula**. El resto se queda en Ken Burns sobre fijas.
- Usar las APIs gratuitas de video en la ventana de baja demanda **12:00–17:30 CDMX**, en lotes.
- HyperFrames o cualquier render de pago = **excepción**, nunca la ruta por defecto.

## 4. Gasto solo al publicar
Alta resolución e I2V se gastan únicamente para la versión que se va a publicar, nunca para borradores.

## 5. Asesinos de costo (evitar)
- Regenerar frames Full HD en cada borrador.
- I2V completo para los ~80 s de la cápsula.
- Créditos IA de CapCut.
- Cambiar la voz: **JorgeNeural (edge-tts, rate +7 %, pitch −2 Hz) es intocable.** No cambiar motor TTS ni voz.

## Documentos relacionados
- [MATRIZ_HERRAMIENTAS_GRATUITAS.md](MATRIZ_HERRAMIENTAS_GRATUITAS.md) – fallback a fijas + FFmpeg.
- [CREDITOS_GRATIS_VIDEO.md](CREDITOS_GRATIS_VIDEO.md) – planes gratis de I2V y horarios.
- [RECETA_CAPSULA.md](RECETA_CAPSULA.md)
- [PLAN_MAESTRO_AUTOMATICO.md](PLAN_MAESTRO_AUTOMATICO.md)
