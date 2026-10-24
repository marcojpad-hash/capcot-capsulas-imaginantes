# RECETA CÁPSULA — Datos y ociosidades (autocontenida)

Pega este documento completo en cualquier modelo (Gemini, Groq/Llama, ChatGPT, Grok, Claude…) y pídele: «Hazme la cápsula de hoy sobre <TEMA>, siguiendo la receta. Devuelve SOLO el JSON storyboard_vertical y luego la descripción».

**Rol de ChatGPT (2026-10-24, Mj):** ChatGPT propone y produce la **cápsula de actualidad científica del día** (noticia ≤7 días, estudio original citado) y la deja en `cola/entrada/` como paquete (storyboard + frames o mp4 + fuentes). **ChatGPT nunca publica.** Grok Bot revisa (fuentes, DOI, receta), corre QA y publica. Detalle en docs/FLUJO_EXTERNO.md.

Canal: **Datos y ociosidades** · @datosyociosidades · YouTube UCU2ZI-6pBJEr9aSFsF6bxLw. TikTok: **@datosyociosidades** (cuenta existente, sin cuenta nueva); toda descripción de YouTube lleva la línea fija `TikTok: https://www.tiktok.com/@datosyociosidades`.

## 1. Reglas editoriales
- Periodismo informativo-narrativo estilo «Imaginantes»: una historia real con personas, lugar y momento; el dato científico es el giro, no una lista.
- Arco obligatorio (campo técnico; el contenido del gancho depende de `estructura`: pregunta, mito_vs_dato, comparacion, sabias_que o historia): `hook_medias_res` (in medias res, primera frase ≤12 palabras) → `desarrollo` (2–4 escenas) → `cierre_historia` (1–2) → `reflexion_o_pregunta` (reflexión ontológica o pregunta abierta + «Esto fue Datos y ociosidades.»).
- Cada afirmación factual tiene `source_ids`. Nada de cifras inventadas, nada de «se dice que». Si no hay fuente, no se dice.
- Lenguaje: español de México, frases cortas, verbos concretos, segunda persona ocasional. Sin clickbait falso.
- **Tema (actualizado 2026-10-24, Mj): PRIORIDAD = noticia científica o de investigación RECIENTE (últimos ~7 días)**: estudio recién publicado, descubrimiento, misión espacial, salud, clima/ambiente. Se busca en fuentes reales: Nature/Science news, EurekAlert, ScienceDaily, Phys.org, NASA/ESA/JAXA, SINC, Agencia Informativa Conacyt, UNAM Global/Gaceta UNAM (`python3 scripts/tendencias.py` ya lee estos RSS y los puntúa antes que Google Trends).
- **Siempre se cita el estudio original** (DOI o comunicado oficial de la institución/agencia) además de la nota de prensa; se verifica que el DOI resuelva (Crossref) y que el estudio diga lo que la cápsula afirma. La fecha de publicación va en `trend_source.fecha_publicacion`.
- Google Trends es señal secundaria (sirve para elegir entre noticias o enganchar con lo que se busca); backlog atemporal solo si no hay noticia científica verificable de la semana. Nada de deportes, crimen ni tragedias.
- `trend_source` para noticias: `{"tipo": "noticia_cientifica", "medio": "...", "url": "<nota>", "estudio_doi": "...", "fecha_publicacion": "AAAA-MM-DD", "termino": "<tema corto>", "fecha_consulta": "AAAA-MM-DD"}`.

## 2. Duración y ritmo
- Total **75–90 s** (QA acepta 60–95 s). **170–235 palabras** (máx. 240) con voz es-MX-JorgeNeural a **+11 %** (rango +10 a +12 %), pitch −2 Hz.
- 7–9 escenas de 6–15 s. **Todas con voz**: pausa ligera entre frases (punto 0.32 s, pregunta/exclamación/… 0.35 s, dos puntos 0.25 s), ningún hueco de subtítulos >0.9 s.
- **Estructura visual** (docs/ESTRUCTURA_VISUAL_TRENDS.md): planos de ~2.5 s con cortes secos y un movimiento distinto en cada plano. La escena 1 lleva tarjeta de gancho con `on_screen_text` desde el frame 0. Los subtítulos van en zona segura (MarginV 560). Cortinilla de 5 s.
- **Título**: campo `titulo` (gancho ≤6 palabras) como tarjeta inicial. **Subtítulos**: ASS 1080×1920 con el 100 % del guion (QA de cobertura ≥99 %).
- **SFX por plano**: `scenes[].sfx` = lista, un efecto por plano acorde a la imagen (olas, gaviotas, lluvia, campanas, reloj, pluma, madera, motor…), con grabaciones CC0/PD de Commons (scripts/sfx_manifest.json; se bajan con scripts/descargar_sfx.py).
- **Audio (legado)**: cada escena lleva el campo `ambiente` (oceano|puerto|viento|viento_fuerte|lluvia|tormenta|mercado, combinables con +). La música es `sintetico:pulso` a 92 BPM. Niveles: voz -16, música -27, ambiente -30 LUFS, con ducking por sidechain. Todo es sintetizado (scripts/cama_sonora.py), sin terceros. Si se usa un archivo externo, solo Freesound CC0 verificado.
- Si sobra tiempo: **añade un dato con fuente**, nunca silencio ni escenas mudas.
- Subtítulos de ≤3 palabras por bloque; texto en pantalla ≤6 palabras por escena.
- Al final, cortinilla de fuentes de 6 s (ver §5).

## 3. JSON `storyboard_vertical`
```json
{
 "project_id": "AAAA-MM-DD_slug", "title": "≤60 caracteres", "language": "es-MX", "aspect_ratio": "9:16",
 "target_duration_seconds": 85,
 "trend_source": {"tipo": "google_trends_rss", "termino": "...", "fecha_consulta": "AAAA-MM-DD", "url": "..."},
 "estilo_id": "<clave de §4>", "estilo_visual": "<nombre del estilo>",
 "voice": {"engine": "edge-tts", "voice_id": "es-MX-JorgeNeural", "rate": "+7%", "pitch": "-2Hz", "pad_seconds": 0.35, "modo_pausas": "continuo"},
 "sources": [{"id": "SRC-001", "cita_corta": "Autor (año). Título. Medio.", "url": "https://...", "doi": "opcional", "accessed": "AAAA-MM-DD", "supports": ["afirmación 1", "..."], "ref_display": "texto corto"}],
 "scenes": [{"id": "scene_001", "arc": "hook_medias_res", "duration_seconds": 9.0, "narration": "...", "on_screen_text": "...",
             "visual_description": "...", "image_prompt": "<prompt_base del estilo> + escena concreta, vertical 9:16, no text", "source_ids": ["SRC-001"],
             "asset_filename": "frames/scene_001.jpg"}],
 "cortinilla_fuentes": {"duration_seconds": 6, "titulo": "Fuentes", "aviso": "Imágenes generadas con IA. Voz sintética. Audio sintetizado.", "firma": "Datos y ociosidades · @datosyociosidades"},
 "export": {"filename": "capsula.mp4", "resolution": "1080x1920", "fps": 30, "loudness_lufs": -14}
}
```

## 4. Estilos visuales y regla de elección
**Regla:** puntaje = 3·(coincidencia del tema con «Temas» del estilo) + 0.5·atractivo + 2·peso de tendencia viral del día − 2 si se usó en las últimas 5 cápsulas. **Prohibido repetir el estilo de la cápsula anterior.** Elegir por temática, no por rotación mecánica. Un mismo estilo para todas las escenas de la cápsula.

- **Linograbado bitono** (`linograbado`) — Linograbado bitono Paleta: índigo, ocre, crema. Temas: mar, historia, ciencia de la Tierra, oficios. Prompt base: `linocut print, two-tone indigo and ochre ink on cream paper, bold carved lines, visible gouge marks, high contrast, vertical 9:16 composition, no text`
- **Papel rasgado por capas (diorama)** (`papel_rasgado_capas`) — Papel rasgado por capas (diorama) Paleta: verde bosque, turquesa apagado, ocre, crema. Temas: naturaleza, paisajes, catástrofes, geología. Prompt base: `layered torn paper collage diorama, deckled paper edges, felt and cardstock textures, muted teal, forest green, ochre and cream, soft side light with depth shadows between layers, vertical 9:16, no text`
- **Recortes de papel stop-motion / libro pop-up** (`papel_recortado_popup`) — Recortes de papel stop-motion / libro pop-up Paleta: sepia, cartón, negro, acentos rojos. Temas: lenguaje, semiótica, ideas abstractas. Prompt base: `stop-motion paper cut-out scene inside an open pop-up book box, newsprint and sepia paper figures, red thread accents, cardboard background, warm dim lamp light, handmade feel, vertical 9:16, no text`
- **Muñecos tejidos amigurumi en miniatura** (`amigurumi`) — Muñecos tejidos amigurumi en miniatura Paleta: cálida → oscura con luz de fuego. Temas: ritos, emociones, infancia, antropología. Prompt base: `miniature crochet amigurumi characters, macro photography, shallow depth of field, soft natural window light turning to warm firelight, handmade yarn texture, cozy diorama props, vertical 9:16, no text`
- **Cubismo con collage de periódico** (`cubismo_collage`) — Facetas geométricas tipo Picasso/Braque mezcladas con recortes de prensa. Paleta: . Temas: arte, percepción, ciencia cognitiva, historia moderna. Prompt base: `analytical cubism painting with newspaper collage fragments, fragmented geometric planes, ochre, slate blue and brown palette, textured oil paint, vertical 9:16, no text`
- **Cómic pop art** (`pop_art_comic`) — Viñeta de cómic con puntos Ben-Day, onomatopeyas y colores primarios. Paleta: . Temas: inventos, física, superhéroes de la ciencia, explosiones. Prompt base: `pop art comic book panel, Ben-Day halftone dots, bold black outlines, saturated primary colors, dramatic action burst background, vertical 9:16, no text`
- **Acuarela azul a línea** (`acuarela_linea`) — Tinta fina con aguadas azules que se disuelven en blanco. Paleta: . Temas: música, ciudades, recuerdos, poesía. Prompt base: `delicate blue watercolor wash with fine ink line drawing, monochrome indigo-blue tones fading to white paper, loose expressive brushwork, vertical 9:16, no text`
- **Teatro de sombras retroiluminado** (`teatro_sombras`) — Siluetas de papel recortado frente a luz cálida, marco de teatrino. Paleta: . Temas: mitos, leyendas, astronomía antigua, cuentos. Prompt base: `shadow puppet theater, black paper cut silhouettes backlit by warm amber light, layered cut paper scenery, ornate wooden stage frame, vertical 9:16, no text`
- **TV vieja con estática (tipo Coraje)** (`tv_estatica`) — Imagen en blanco y negro dentro de un televisor viejo, cuarto oscuro y ruido. Paleta: . Temas: misterios, miedos, medios de comunicación, paranormal explicado. Prompt base: `black and white cartoon image displayed on an old CRT television in a dark dusty room, scan lines, static noise, eerie vintage mood, vertical 9:16, no text`
- **Crayones infantiles** (`crayones_infantiles`) — Dibujo de niño con crayones de cera sobre papel. Paleta: . Temas: infancia, aprendizaje, biología básica, preguntas simples. Prompt base: `child's wax crayon drawing on white paper, naive shapes, bright colors, visible crayon strokes, cheerful sun, vertical 9:16, no text`
- **Stencil constructivista ruso** (`constructivista_ruso`) — Fotomontaje en rojo y negro con diagonales y tipografía soviética. Paleta: . Temas: historia del s. XX, industria, revoluciones, semiótica. Prompt base: `Russian constructivist propaganda photomontage, red and black on aged paper, bold diagonals, stencil shapes, grainy halftone photo, vertical 9:16, no text`
- **Caricatura tipo Flapjack** (`flapjack_cartoon`) — Cartoon de Cartoon Network con texturas sucias y colores ácidos. Paleta: . Temas: mar, aventuras, humor, curiosidades absurdas. Prompt base: `2000s Cartoon Network style cartoon, grotesque whimsical characters, textured painted backgrounds, sickly acid greens and pinks, nautical whimsy, vertical 9:16, no text`
- **Sátira de periódico en tinta** (`satira_periodico`) — Caricatura editorial en tinta con viñetas de diario. Paleta: . Temas: política pública, economía, medio ambiente, noticias. Prompt base: `editorial satirical newspaper cartoon, black ink crosshatching on newsprint, caricatured figures, newspaper columns layout, vertical 9:16, no text`
- **Pixel art** (`pixel_art`) — Sprite de videojuego de 16 bits. Paleta: . Temas: tecnología, videojuegos, matemáticas, computación. Prompt base: `16-bit pixel art scene, limited retro palette, crisp pixels, side view video game style, dithering, vertical 9:16, no text`
- **Pintura rupestre** (`pintura_rupestre`) — Ocres y manos estampadas sobre roca de cueva. Paleta: . Temas: prehistoria, evolución, origen de ideas, astronomía antigua. Prompt base: `prehistoric cave painting on rough rock wall, red ochre and charcoal pigments, hand stencils, primitive figures, torchlight, vertical 9:16, no text`
- **Cartel de propaganda vintage** (`cartel_propaganda`) — Póster de época con tipografía grande y heroísmo. Paleta: . Temas: salud pública, guerras, campañas, ciencia y sociedad. Prompt base: `vintage 1940s propaganda poster, heroic pose, bold flat colors red cream and navy, aged printed paper texture, vertical 9:16, no text`
- **Óleo expresivo** (`oleo_expresivo`) — Pintura al óleo con empaste y pincelada visible. Paleta: . Temas: biografías, drama humano, historia, filosofía. Prompt base: `expressive oil painting, thick impasto brushstrokes, dramatic chiaroscuro lighting, rich earthy palette, vertical 9:16, no text`
- **Stencil grafiti tipo Banksy** (`stencil_banksy`) — Esténcil negro sobre muro con un acento rojo. Paleta: . Temas: crítica social, consumo, ecología, urbanismo. Prompt base: `Banksy-style street stencil art on a weathered concrete wall, black spray paint with a single red accent, drips, vertical 9:16, no text`
- **Garabato en cuaderno** (`garabato_cuaderno`) — Dibujo a lápiz en hoja rayada con anotaciones. Paleta: . Temas: ideas, inventos, procesos mentales, estudio. Prompt base: `pencil doodle sketch on lined notebook paper, hand-drawn arrows and small notes, graphite shading, spiral binding edge, vertical 9:16, no text`
- **Noche estrellada (Van Gogh)** (`van_gogh`) — Pinceladas en remolino, azules y amarillos. Paleta: . Temas: astronomía, noche, arte, percepción. Prompt base: `post-impressionist painting in the style of Van Gogh's Starry Night, swirling brushstrokes, deep blues and glowing yellows, vertical 9:16, no text`
- **Figuras de cartón recortado** (`carton_recortado`) — Figuras de cartón corrugado con bordes crudos, fotografiadas. Paleta: . Temas: reciclaje, ingeniería, maquetas, oficios. Prompt base: `handmade figures cut from corrugated cardboard, raw torn edges, marker details, photographed on a table with soft light, vertical 9:16, no text`
- **Crayón en nube de pensamiento** (`crayon_nube`) — Escena dibujada con crayón dentro de una nube de pensamiento. Paleta: . Temas: imaginación, sueños, psicología, hipótesis. Prompt base: `crayon drawing inside a cartoon thought bubble floating over a soft paper background, dreamy, hand-colored, vertical 9:16, no text`
- **Retrato collage de papel cosido** (`collage_papel_cosido`) — Papeles y recortes de texto cosidos con hilo, relieve. Paleta: . Temas: literatura, mitos, identidad, viajes. Prompt base: `mixed media collage of stitched paper scraps and newspaper word cutouts, visible thread stitches, layered relief, muted denim and kraft tones, vertical 9:16, no text`
- **Póster de cine japonés de los 60** (`poster_cine_japones`) — Cartel de película japonesa con tipografía y fotografía pintada. Paleta: . Temas: historias de grupo, cine, tecnología japonesa, aventuras. Prompt base: `1960s Japanese movie poster, painted photographic portraits, bold vertical typography blocks, retro print colors, worn paper, vertical 9:16, no text`
- **Sketch de línea fina (tipo referencia bartending)** (`linea_fina`) — Dibujo a lápiz/tinta fino y limpio sobre blanco. Paleta: . Temas: objetos, química, diseño, anatomía, comida, bebidas, oficios, cocina. Prompt base: `fine line pencil illustration on white paper, precise thin strokes, subtle graphite shading, minimal composition, vertical 9:16, no text`
- **Grafiti urbano colorido** (`grafiti_colorido`) — Mural de spray saturado con personajes. Paleta: . Temas: ciudades, juventud, cultura popular, música. Prompt base: `colorful urban graffiti mural, saturated spray paint, playful cartoon characters, thick outlines, wildstyle accents, vertical 9:16, no text`
- **Claymation / plastilina (propio)** (`claymation`) — Personajes y escenarios de plastilina con huellas dactilares, stop-motion. Paleta: . Temas: biología, cuerpo humano, animales, comida, vida cotidiana, ciencia, infancia, cocina. Prompt base: `claymation stop-motion scene, plasticine characters and set with visible fingerprints, soft studio lighting, miniature handmade props, vertical 9:16, no text`
- **Ukiyo-e (propio)** (`ukiyo_e`) — Grabado japonés en madera, líneas y planos de color. Paleta: . Temas: mar, terremotos, volcanes, naturaleza. Prompt base: `ukiyo-e Japanese woodblock print, flat color areas, elegant outlines, stylized waves and clouds, washi paper texture, vertical 9:16, no text`
- **Risografía (propio)** (`risografia`) — Impresión riso de 2–3 tintas con desregistro y grano. Paleta: . Temas: tecnología, datos curiosos modernos, cultura joven. Prompt base: `risograph print, two-color fluorescent pink and teal overprint, misregistration, grainy texture, flat shapes, vertical 9:16, no text`
- **Vitral (propio)** (`vitral`) — Vidrio de colores con plomo, luz que atraviesa. Paleta: . Temas: historia medieval, religión y ciencia, luz y óptica. Prompt base: `stained glass window, colorful glass pieces with thick black lead lines, light shining through, gothic arch, vertical 9:16, no text`
- **Bordado (propio)** (`bordado`) — Escena bordada a mano en tela con hilos. Paleta: . Temas: tradiciones, textiles, genética (hilos), México. Prompt base: `hand embroidery on linen fabric, colorful thread stitches, satin and french knots, embroidery hoop edge visible, vertical 9:16, no text`
- **Stop-motion de papel (propio)** (`papel_stop_motion`) — Recortes de papel planos animados sobre fondo de cartulina. Paleta: . Temas: explicaciones paso a paso, procesos, historia. Prompt base: `flat paper cut-out stop-motion animation frame, colored construction paper pieces, slight shadows, top-down view, vertical 9:16, no text`
- **El Principito (película 2015)** (`principito_2015`) — Mundo del principito en stop-motion de papel/cartón con texturas de papel maché, combinado con CG suave y luz cálida (Mark Osborne, 2015). Paleta: . Temas: astronomía, filosofía, infancia, amistad, sueños, planeta, estrellas. Prompt base: `stop-motion papercraft world like The Little Prince 2015 film, paper mache and cardboard textures, tiny planet sets, soft warm CG lighting, gentle pastel palette, vertical 9:16, no text`
- **Animación clásica tipo Disney** (`disney_clasico`) — Animación 2D clásica pintada a mano, fondos en gouache, personajes expresivos. Paleta: . Temas: cuentos, animales, mitos, naturaleza, historia, música. Prompt base: `classic hand-drawn 2D animation still in the style of 1950s Disney feature films, painted gouache backgrounds, expressive characters, soft cel shading, vertical 9:16, no text`

## 5. Tarjeta de fuentes
- Solo fuentes **reales y verificables** (artículo con DOI, agencia oficial —NOAA, NASA, INEGI, UNAM—, revista o medio reconocido). Comprobar que la URL/DOI abre y respalda la frase.
- 1–4 fuentes en pantalla, formato `Autor (año) · medio` + `ref_display`. Aviso de IA obligatorio y firma del canal.

## 6. Descripción de YouTube (con hashtags y TikTok)
```
<frase gancho>

<Título>. Una cápsula de Datos y ociosidades: datos verificados contados como historia.

Fuentes:
• <cita_corta> <url o https://doi.org/DOI>

Imágenes generadas con IA · voz sintética · audio sintetizado.
Suscríbete: @datosyociosidades
TikTok: https://www.tiktok.com/@datosyociosidades

#DatosYOciosidades #Shorts #datos #ciencia #difusión #difusióncientífica #ia #<Tema> (hasta 4 de tema)
```
Título YouTube = título + « #Shorts» (≤100 caracteres, sin `<` `>`; en URLs se codifican %3C/%3E). Descripción ≤5000 bytes; tags ≤500 caracteres.
Hashtags base FIJOS en todas las plataformas: `#datos #ciencia #difusión #difusióncientífica #ia` + hashtags del tema. Solo YouTube añade `#DatosYOciosidades #Shorts`.
Descripción completa en YouTube y TikTok. **Caption TikTok** (≤2200): gancho + resumen (`"resumen"` opcional en el storyboard) + «Fuentes en YouTube @datosyociosidades» + hashtags base y de tema.
Publicación automática solo vía `capsula_diaria.py --publicar` cuando QA pasa. Máximo 3 al día (2 propias + 1 externa por cola/, ver docs/FLUJO_EXTERNO.md), en ventanas distintas; ningún tema repetido el mismo día (data/temas_del_dia.json).

## 7. (Eliminado) Versión para la voz de Mj
Cancelada por Mj el 2026-10-24 (pertenece a otro proyecto). La cápsula usa solo la voz sintética es-MX-JorgeNeural a +7%.

## 8. Ejemplo completo: «El mar que llegó en Navidad: El Niño» (86.0 s, QA OK, estilo linograbado)
Narración:
1. [hook_medias_res] Navidad, costa de Sudamérica. El agua que debería estar fría llega tibia. Cada tantos años, el mar se calienta justo por estas fechas.
2. [desarrollo] Los pescadores lo bautizaron por la fiesta: El Niño, como el niño de Navidad.
3. [desarrollo] Lejos de ahí, Sir Gilbert Walker estudiaba la presión del aire. Descubrió un vaivén enorme entre Indonesia y el Pacífico tropical: la Oscilación del Sur.
4. [desarrollo] Pero no vio que estaba ligado al mar. Él tenía media historia; los pescadores, la otra mitad.
5. [desarrollo] A finales de los sesenta, Jacob Bjerknes y otros unieron las piezas: océano y atmósfera estaban conectados. Así nació el nombre ENSO.
6. [cierre_historia] Durante El Niño, se calienta la superficie del Pacífico tropical. Los vientos que soplan de este a oeste se debilitan, y a veces se invierten. Su fase opuesta, cuando el mar se enfría, se llama La Niña.
7. [cierre_historia] La lluvia se muda: baja en Indonesia y sube en el Pacífico. Y al cambiar la circulación de la atmósfera, cambian el calor y la lluvia en todo el planeta. Por eso los científicos lo vigilan: a menudo pueden anticipar su llegada con varias estaciones de ventaja.
8. [reflexion_o_pregunta] Un nombre de pescadores terminó describiendo un pulso del clima de la Tierra entera. ¿Cuántos gigantes más se esconden en lo que hoy llamamos costumbre? Esto fue Datos y ociosidades.

JSON completo:
```json
{
 "project_id": "2026-10-24_fenomeno-el-nino",
 "serie": "Imaginantes de la ciencia (prueba)",
 "title": "El mar que llegó en Navidad: El Niño",
 "language": "es-MX",
 "aspect_ratio": "9:16",
 "target_duration_seconds": 88,
 "trend_source": {
  "tipo": "google_trends_rss",
  "rss_geo": "MX",
  "url": "https://trends.google.com/trending/rss?geo=MX",
  "termino": "el niño fenomeno",
  "trafico": "500+",
  "fecha_consulta": "2026-10-24"
 },
 "estilo_visual": "Linograbado (linocut) bitono índigo y ocre sobre papel crema",
 "voice": {
  "engine": "edge-tts",
  "voice_id": "es-MX-JorgeNeural",
  "rate": "+7%",
  "pitch": "-2Hz",
  "pad_seconds": 0.35,
  "modo_pausas": "continuo"
 },
 "sources": [
  {
   "id": "SRC-001",
   "cita_corta": "L'Heureux, M. (2014). What is ENSO in a nutshell? NOAA Climate.gov.",
   "url": "https://www.climate.gov/news-features/blogs/enso/what-el-nino-southern-oscillation-enso-nutshell",
   "accessed": "2026-10-24",
   "supports": [
    "pescadores sudamericanos, Navidad",
    "Walker y la Oscilación del Sur",
    "Bjerknes, finales de los 60",
    "ENSO influye temperatura y lluvia en todo el globo",
    "El Niño: calentamiento superficial del Pacífico tropical central y oriental",
    "vientos del este se debilitan o invierten",
    "lluvia baja en Indonesia y sube en el Pacífico tropical",
    "Walker no reconoció el vínculo con el océano",
    "La Niña: enfriamiento, fase opuesta",
    "se puede predecir con varias estaciones de anticipación"
   ],
   "ref_display": "climate.gov › ENSO in a nutshell"
  },
  {
   "id": "SRC-002",
   "cita_corta": "Bjerknes, J. (1969). Monthly Weather Review 97, 163-172.",
   "doi": "10.1175/1520-0493(1969)097<0163:ATFTEP>2.3.CO;2",
   "url": "https://doi.org/10.1175/1520-0493(1969)097%3C0163:ATFTEP%3E2.3.CO;2",
   "accessed": "2026-10-24",
   "supports": [
    "acoplamiento océano-atmósfera"
   ]
  },
  {
   "id": "SRC-003",
   "cita_corta": "McPhaden, Zebiak & Glantz (2006). Science 314, 1740-1745.",
   "doi": "10.1126/science.1132588",
   "url": "https://doi.org/10.1126/science.1132588",
   "accessed": "2026-10-24",
   "supports": [
    "ENSO con impactos globales"
   ]
  }
 ],
 "scenes": [
  {
   "id": "scene_001",
   "arc": "hook_medias_res",
   "duration_seconds": 9.0,
   "narration": "Navidad, costa de Sudamérica. El agua que debería estar fría llega tibia. Cada tantos años, el mar se calienta justo por estas fechas.",
   "on_screen_text": "Navidad: el mar, tibio",
   "visual_description": "ver prompt",
   "image_prompt": "linocut indigo/ocre (ver registro)",
   "source_ids": [
    "SRC-001"
   ],
   "asset_filename": "frames/scene_001.jpg",
   "arc_imaginantes": "gancho"
  },
  {
   "id": "scene_002",
   "arc": "desarrollo",
   "duration_seconds": 5.7,
   "narration": "Los pescadores lo bautizaron por la fiesta: El Niño, como el niño de Navidad.",
   "on_screen_text": "Le llamaron El Niño",
   "visual_description": "ver prompt",
   "image_prompt": "linocut indigo/ocre (ver registro)",
   "source_ids": [
    "SRC-001"
   ],
   "asset_filename": "frames/scene_002.jpg",
   "arc_imaginantes": "ancla"
  },
  {
   "id": "scene_003",
   "arc": "desarrollo",
   "duration_seconds": 9.7,
   "narration": "Lejos de ahí, Sir Gilbert Walker estudiaba la presión del aire. Descubrió un vaivén enorme entre Indonesia y el Pacífico tropical: la Oscilación del Sur.",
   "on_screen_text": "La Oscilación del Sur",
   "visual_description": "ver prompt",
   "image_prompt": "linocut indigo/ocre (ver registro)",
   "source_ids": [
    "SRC-001"
   ],
   "asset_filename": "frames/scene_003.jpg",
   "arc_imaginantes": "relato_beat1"
  },
  {
   "id": "scene_004",
   "arc": "desarrollo",
   "duration_seconds": 6.8,
   "narration": "Pero no vio que estaba ligado al mar. Él tenía media historia; los pescadores, la otra mitad.",
   "on_screen_text": "La mitad de la historia",
   "visual_description": "ver prompt",
   "image_prompt": "linocut indigo/ocre (ver registro)",
   "source_ids": [
    "SRC-001"
   ],
   "asset_filename": "frames/scene_004.jpg",
   "arc_imaginantes": "relato_beat2"
  },
  {
   "id": "scene_005",
   "arc": "desarrollo",
   "duration_seconds": 8.6,
   "narration": "A finales de los sesenta, Jacob Bjerknes y otros unieron las piezas: océano y atmósfera estaban conectados. Así nació el nombre ENSO.",
   "on_screen_text": "Océano + atmósfera",
   "visual_description": "ver prompt",
   "image_prompt": "linocut indigo/ocre (ver registro)",
   "source_ids": [],
   "asset_filename": "frames/scene_005.jpg",
   "arc_imaginantes": "relato_beat3"
  },
  {
   "id": "scene_006",
   "arc": "cierre_historia",
   "duration_seconds": 14.1,
   "narration": "Durante El Niño, se calienta la superficie del Pacífico tropical. Los vientos que soplan de este a oeste se debilitan, y a veces se invierten. Su fase opuesta, cuando el mar se enfría, se llama La Niña.",
   "on_screen_text": "Vientos que se invierten",
   "visual_description": "ver prompt",
   "image_prompt": "linocut indigo/ocre (ver registro)",
   "source_ids": [
    "SRC-001"
   ],
   "asset_filename": "frames/scene_006.jpg",
   "arc_imaginantes": "giro"
  },
  {
   "id": "scene_007",
   "arc": "cierre_historia",
   "duration_seconds": 17.7,
   "narration": "La lluvia se muda: baja en Indonesia y sube en el Pacífico. Y al cambiar la circulación de la atmósfera, cambian el calor y la lluvia en todo el planeta. Por eso los científicos lo vigilan: a menudo pueden anticipar su llegada con varias estaciones de ventaja.",
   "on_screen_text": "ENSO",
   "visual_description": "ver prompt",
   "image_prompt": "linocut indigo/ocre (ver registro)",
   "source_ids": [
    "SRC-001",
    "SRC-003"
   ],
   "asset_filename": "frames/scene_007.jpg",
   "arc_imaginantes": "cierre"
  },
  {
   "id": "scene_008",
   "arc": "reflexion_o_pregunta",
   "duration_seconds": 11.5,
   "narration": "Un nombre de pescadores terminó describiendo un pulso del clima de la Tierra entera. ¿Cuántos gigantes más se esconden en lo que hoy llamamos costumbre? Esto fue Datos y ociosidades.",
   "on_screen_text": "",
   "visual_description": "ver prompt",
   "image_prompt": "linocut indigo/ocre (ver registro)",
   "source_ids": [
    "SRC-001"
   ],
   "asset_filename": "frames/scene_008.jpg",
   "arc_imaginantes": "reflexion_firma"
  }
 ],
 "cortinilla_fuentes": {
  "duration_seconds": 6,
  "titulo": "Fuentes",
  "aviso": "Imágenes generadas con IA. Voz sintética (edge-tts). Ambiente y música sintetizados con ffmpeg.",
  "bg_rgb": [
   20,
   28,
   52
  ],
  "firma": "Datos y ociosidades · @datosyociosidades"
 },
 "audio": {
  "ambiente": "oceano+viento",
  "music_asset": "sintetico:menor_calma",
  "music_license": "Sintetizado con ffmpeg (aevalsrc/anoisesrc) por el pipeline: obra propia, sin derechos de terceros",
  "ducking": "sidechaincompress thr 0.02 ratio 6; camas a -38/-40 LUFS vs voz -16 LUFS"
 },
 "export": {
  "filename": "capsula_v3.mp4",
  "resolution": "1080x1920",
  "fps": 30,
  "subtitle_max_words": 3
 },
 "estado": "STORYBOARD_VALIDADO",
 "version": "v2",
 "canal": {
  "nombre": "Datos y ociosidades",
  "handle": "@datosyociosidades",
  "youtube_channel_id": "UCU2ZI-6pBJEr9aSFsF6bxLw"
 },
 "estilo_id": "linograbado"
}
```

## Reglas contra el contenido «no auténtico» o «en serie» (vigentes desde el 24 de octubre de 2026)
Base:
- YouTube, «Contenido no auténtico» (support.google.com/youtube/answer/1311392; se llamaba «contenido repetitivo» hasta el 15 de julio de 2025). Ahí se señalan el contenido hecho con plantillas, el repetitivo o producido en masa, los videos de IA con plantillas genéricas y las presentaciones de diapositivas o textos en movimiento con poco valor. Se permite repetir la misma intro y el mismo cierre si el núcleo de cada video es distinto. Los revisores miran la sección «Información» del canal.
- YouTube, política de spam (support.google.com/youtube/answer/2801973). Pone como ejemplo «la misma música de fondo y las mismas imágenes repetitivas generadas por IA en muchos vídeos, en los que además se lee un guion generado por IA».
- YouTube, aviso de contenido generado por IA (support.google.com/youtube/answer/14328491).

Reglas:
1. **Duración variable de 60 a 90 s o más, nunca menos de 60.** `rotacion.duracion_objetivo(tema, n_fuentes)` da entre 62 y 95 s según el tema y varía respecto de la cápsula anterior. Se guarda en `target_duration_seconds` y se pasa al guionista. montar_capsula y QA aceptan de 60 a 120 s.
2. **La estructura rota.** El campo `estructura` toma uno de estos valores: `mito_vs_dato`, `pregunta`, `historia`, `comparacion` o `sabias_que`. Nunca se repite dos veces seguidas: el registro está en `data/rotacion.json` y lo vigila el check de QA `estructura_no_repite_anterior`. Si un storyboard manual repite la estructura, capsula_diaria aborta.
3. **El estilo depende del tema y no se repite en dos cápsulas seguidas.** Lo hace `rotar_estilo.ranking()`, que salta el último estilo usado (`if u and e == u[-1]: continue`) y penaliza los 5 anteriores. Está verificado.
4. **La música rota.** Hay 5 camas propias en `cama_sonora.CAMAS`: pulso, marimba, pizzicato, arpegio y tambor. Cambian el tempo, la progresión, el timbre y la batería. `rotacion.elegir_cama` evita las 2 últimas; el resultado va en `audio.music_asset = "sintetico:<cama>"` y `audio.cama_musical`. Si se usa la YouTube Audio Library, Mj descarga la pista a mano, la pone en `music_asset=<archivo>` y anota `music_origen` y `music_licencia`. Además, montar_capsula escribe en cada cápsula un **`licencias.json`** con la música, los SFX (URL, autor y licencia de Commons), las imágenes, la voz, el mapa base y las fuentes de datos.
5. **Capas informativas, no solo Ken Burns.** El campo `scenes[].capa` admite tres tipos: `mapa` (Natural Earth 110m, de dominio público, con puntos y flechas animadas), `grafico` (una línea que se dibuja) o `dato` (una cifra grande con su etiqueta). Las genera `scripts/capas_datos.py` con matplotlib y ocupan un plano de la escena (`plano`, por defecto el último). Cada cápsula lleva al menos un mapa y un gráfico o dato, con cifras **reales** tomadas de las fuentes citadas (checks de QA `capa_mapa` y `capa_grafico_o_dato`). El mapa base se descarga con `scripts/descargar_geo.sh`.
6. **«Acerca de» del canal**: el borrador está en `docs/ACERCA_DE_CANAL.md` (investigación y verificación humanas con herramientas de IA, fuentes visibles). Mj lo aplica a mano.
7. **Etiqueta de contenido sintético.** `metadata.etiqueta_sintetica(sb)` marca `contenido_sintetico=true` **solo** si algo parece real (`parece_real`, un estilo realista o `persona_real_recreada`) o si la música generada por IA es el elemento central (`audio.music_ia` y `music_protagonista`). La ilustración estilizada, la voz TTS genérica, el guion asistido y las infografías no requieren etiqueta (14328491). publicar.py envía `status.containsSyntheticMedia` con ese valor; si falta metadata.json, envía true por precaución. La descripción sigue declarando siempre «Imágenes generadas con IA · voz sintética».
8. **Límite duro vigente: 3 cápsulas por día = 2 propias + 1 externa.** `scripts/rotacion.py` define `MAX_POR_DIA = 3` y `MAX_ORIGEN = {"propia": 2, "externa": 1}`. Esta regla sustituye la referencia antigua a 1 cápsula diaria; no se debe cambiar el cupo saltándose el validador.
