# Hielo sucio alrededor de Beta Pictoris — ¿Hielo más viejo que la estrella?

project_id: `2026-11-18_hielo-sucio-beta-pictoris`
slot asignado: 23:30 del 2026-11-18 (dato del día, hueco 23:30, ver revisión diaria 18-nov)
estado: montado y QA 21/21, pendiente de subir y programar
origen: noticia científica Science 12-nov-2026 (Betti et al.), nota Phys.org

## Guion narrado completo (~61 s, 149 palabras)

> ¿Un hielo más viejo que la estrella que lo rodea? Suena imposible, pero el James Webb lo vio alrededor de Beta Pictoris. Beta Pictoris es una estrella joven a 63 años luz. Tiene un disco de escombros donde se forman planetas. El telescopio James Webb detectó por primera vez hielo de agua y dióxido de carbono en ese disco. El hielo de agua es casi todo amorfo, como vidrio, con menos del 7 por ciento cristalino. El CO2 está mezclado, una molécula por cada diez de agua. Eso significa que el hielo se formó en el frío del medio interestelar, antes incluso de que naciera la estrella. Para que esté tan uniforme, los cuerpos de hielo chocan constantemente en el disco. El hielo sucio sobrevive y se reparte. El mismo hielo que hay en nuestros cometas. ¿Cuántos sistemas heredan su agua del espacio profundo? Esto fue Datos y ociosidades.

## El dato (por escenas)

- El James Webb detectó por primera vez hielo de agua y CO2 en el disco de escombros de Beta Pictoris (63 años luz).
- El hielo de agua es casi todo amorfo (<7% cristalino), como vidrio; el CO2 está mezclado 1:10 con el agua.
- Eso significa que el hielo se formó en el frío del medio interestelar, antes de que naciera la estrella.
- Para que esté tan uniforme, los cuerpos de hielo chocan constantemente en el disco.

## Estándar vigente (Marco 16-nov)

- Voz ES (relevo: Kokoro em_santa local; storyboard pedía es-MX-JorgeNeural edge-tts, bloqueado por proxy).
- Cierre "Esto fue Datos y ociosidades."
- Primer frame con título quemado legible = mismo texto que el título (mayúsculas, amarillo/rojo).
- Hashtags: #Shorts siempre + máximo 1 de tema (#espacio) + opcional #DatosYOciosidades, máximo 3 en total.

## Chequeo anti-duplicados 2026-11-18

Buscado en data/publicaciones.json: pictoris, hielo sucio, beta pic — 0 resultados. No hay duplicado.

## Fuentes verificadas 2026-11-18

- Betti, S. K. et al. (2026). Carbon dioxide and amorphous water ices in the debris disk around β Pictoris. Science, 394(6825), 742–745. https://doi.org/10.1126/science.adw7770
- Nota de prensa: https://phys.org/news/2026-11-dirty-ice-young-star-beta.html

## Notas del relevo (Pecas)

- Voz: storyboard pide es-MX-JorgeNeural (edge-tts); edge-tts bloqueado por el proxy de salida (websocket). Relevo con Kokoro ONNX em_santa local, speed 0.93 (a 1.0 el video quedaba en ~59 s, bajo el mínimo de 60 s).
- SFX: el storyboard trae "viento", "reloj", "pluma", "campanas", "olas", que no existen en cama_sonora.SINTETICOS ni en assets/sfx; se normalizaron en el montaje a viento_fuerte, silencio, silencio, silencio, oceano (solo en memoria, sin tocar el storyboard).
- Duración final 61.27 s, loudness -14.7 LUFS, QA 21/21.
