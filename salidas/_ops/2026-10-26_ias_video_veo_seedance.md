# IAs de video del Reel «dominio digital» vs pipeline CAPCOT (2026-10-26)

**Lead.** Ninguna de estas herramientas reemplaza nuestro pipeline (frames estáticos + edge-tts + ffmpeg `montar_capsula`): todas generan clips cortos (≈5–15 s por toma), cobran por segundo, y mantener un estilo ilustrado (mosaico, códice, chicha) igual en 60–90 s es difícil sin image-to-video. Lo que sí suman es **animar 2–4 frames clave** que ya hicimos (image-to-video, 5 s cada uno) e intercalarlos en el montaje. Costo de un Short con 4 tomas de 5 s: ~$0.60–$3 USD según modelo. Narración sigue siendo edge-tts (o el audio nativo, si conviene).

Precios: API oficial, 720p, por segundo, octubre 2026 (fuentes: docs.x.ai/developers/pricing, llms.blog comparativa oct-2026, modelpick.dev). Pueden cambiar.

- **Veo 3.1 (Google)** — Calidad y audio nativo de primer nivel; fuerte en live-action/cine. Lite $0.05/s, Fast $0.10/s, Standard $0.40/s. Ojo: los modelos preview de Veo 3.1 en Gemini API se dieron de baja el 22-oct-2026 → sucesor Gemini Omni Flash (~$0.10/s). Estilo ilustrado: correcto con imagen de referencia, pero tiende a "realistizar". **Solo prueba** (vía Omni Flash).
- **Seedance 2.0/2.5 (ByteDance)** — Muy bueno en movimiento, multi-toma y consistencia con referencias; buen respeto a estilos 2D. BytePlus por tokens: 2.5 ≈ $0.103/s 480p, $0.231/s 720p; 2.0 Mini ≈ $0.04/s, 2.0 Fast ≈ $0.06/s (480p). **Suma — candidato 1.**
- **Kling 3.0 (Kuaishou)** — Image-to-video sólido, buen control de cámara. $0.084/s 720p sin audio, $0.126 con audio. Licencia comercial con restricción (no productos competidores). **Solo prueba** (respaldo si Seedance falla).
- **Pika 2.5** — Efectos/estilización ligera, rápido; API desde $0.04/s. App: plan Creator $35/mes con licencia comercial (Free/Starter sin licencia comercial). Calidad por debajo de los otros. **No suma** (salvo efectos puntuales).
- **Grok Imagine Video 1.5 (xAI)** — Image/audio→video, barato. 1.5: $0.08/s 480p, $0.14/s 720p; 1.5 Lite: $0.03/s 720p. Buen precio para animar frames ilustrados en volumen. **Suma — candidato 2.**

**Comparación con nuestro pipeline:** frames estáticos = control total de estilo, texto y costo ~0; video IA = movimiento, pero riesgo de deriva de estilo, glitches de texto y 5–15 s por clip. Modelo híbrido: 80% frames + 2–4 tomas animadas.

**Recomendación (probar ya):** 1) **Seedance 2.0 Fast/Mini** image-to-video sobre 3 frames de una cápsula estilo códice; 2) **Grok Imagine 1.5 Lite** con los mismos 3 frames. Criterio: consistencia de estilo, sin texto deformado, costo < $2 por Short.
