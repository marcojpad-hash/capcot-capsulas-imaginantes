# Estado: 2026-11-04 dato polvo que atrapa oro (slot 23:30 CDMX)

- ChatGPT no entregó el paquete; Grok Bot escribió el guion el 4-nov ~22:05 CDMX a partir del brief de `ajustes_entre_modelos/PARA_CHATGPT_dato_del_dia.md`.
- Fuente: Zhu Z. et al. (2026), Nature Communications, DOI 10.1038/s41467-026-78532-7, publicado el 30-oct-2026. El abstract se verificó en nature.com el 4-nov: la cifra de 5082,32 mg g⁻¹ está ahí. «Cinco veces su peso» es la conversión aritmética de esa cifra.
- Ancla «¿y a mí qué?»: el oro de los aretes y del anillo, sin cifras. No se usó el ancla de celulares ni de basura electrónica porque no hubo tiempo de verificar una fuente oficial (Global E-waste Monitor).
- Guion: 8 escenas con 235 palabras y 1,29 k caracteres. Voz es-MX-JorgeNeural +7 %. La estructura es balazo → ¿y a mí qué? → oro invisible → qué pasa dentro → truco → transformación → límite de laboratorio → giro, pregunta y sello. Incluye los 6 campos narrativos por escena.
- `narrative_qa`: PENDIENTE. No hubo auditor independiente antes del slot, así que `validar_storyboard.py` marca esa falta. No se fingió un PASS.
- Frames: 1–4 se generaron con Canva generate-image (ilustración gouache cálida con una científica recurrente). La cuota de Canva se agotó después del cuarto. Los frames 5–8 son reencuadres o zoom de los frames 1–4; el 8 es un eco circular del 1. GenerateImage del bot no estaba disponible en esta sesión.
- Montaje: `scripts/montar_capsula.py`. `capsula.mp4` dura 89,87 s, 1080x1920 a 30 fps, h264/aac.
- Metadata: título «Este polvo atrapa 5 veces su peso en oro #Shorts». Hashtags: #DatosYOciosidades #curiosidades #ciencia #datosinteresantes #sabiasque #shorts #oro. `contenido_sintetico` = true.
- Fix en `scripts/metadata.py`: ahora descarta tags de más de 20 caracteres derivados de `trend_source.termino` o de los keywords. Así se evita algo como el #AmazonianRainforestBioaerosol... del 3-nov.
- YouTube: **Rv998OZDUYc**, privado, publishAt 2026-11-05T05:30:00Z (23:30 CDMX, 4-nov). La API devolvió containsSyntheticMedia=true. La miniatura del gancho (scene_001) quedó subida.
- TikTok/Facebook: NO publicados; se hacen en el paso de UI con `caption_tt_fb.txt`.
- Pendiente: verificar en Studio que «Uso de IA» = Sí.
