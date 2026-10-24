# Estilos visuales — Datos y ociosidades

**Regla (2026-10-24, Mj):** no hay rotación mecánica. El estilo se elige **según la temática** de cada cápsula y **nunca se repite el de la cápsula anterior**.

## Selector (`scripts/rotar_estilo.py`)
`puntaje = 3·empate_tema + 0.5·atractivo + 2·peso_tendencia − 2 si se usó en las últimas 5`; se excluye el estilo de la última cápsula.
- empate_tema: reglas por etiquetas, es decir, raíces de las palabras del tema y guion contra el campo `temas` de cada estilo.
- atractivo (1–5) da prioridad a las estéticas visualmente atractivas.
- Si existe `CAPCOT_LLM_API_KEY`, un LLM puede desempatar entre los 5 primeros. Para elegir a mano: `--estilo`.
- Ver el ranking: `python3 scripts/rotar_estilo.py "texto del tema"`.

## Tendencias (`scripts/tendencias_estilos.py`)
- Frecuencia: semanal. `capsula_diaria.py` lo ejecuta si `data/tendencias_estilos.json` tiene más de 7 días.
- Fuente automática: Google News RSS con consultas sobre estéticas de animación en TikTok y Shorts de los últimos 30 días. Cuenta palabras clave por estilo y normaliza el resultado a 0–1, en mezcla 50/50 con el peso previo.
- TikTok Creative Center pide login y JS, así que no es accesible desde el script. Se puede revisar a mano.
- Semilla curada 2026-10-24: Claymation = estética #1 en TikTok 2026 (contra-tendencia al 'AI slop'); stop-motion/mixed media en auge; Ghibli/2D pintado fue 2025. Fuentes: https://www.opus.pro/blog/claymation-ai, https://vvideo.co/blog/stop-motion-tiktok-reels-comeback, https://toklytics.app/hashtag/stopmotionanimation, https://www.opus.pro/blog/viral-ai-video-styles-2026

## Catálogo

Las referencias están en `referencias_estilo/`, que no se commitea (gitignored); los nombres de archivo vienen abreviados. En las referencias solo importa el estilo, no el personaje. Contact sheet: `salidas/catalogo_estilos.jpg`.

### Papel rasgado por capas (diorama) (`papel_rasgado_capas`) — atractivo 5
- Descripción: Papel rasgado por capas (diorama)
- Prompt base: `layered torn paper collage diorama, deckled paper edges, felt and cardstock textures, muted teal, forest green, ochre and cream, soft side light with depth shadows between layers, vertical 9:16, no text`
- Referencia: imaginantes/demo-001_v2_frames/
- Temas: naturaleza, paisajes, catástrofes, geología

### Recortes de papel stop-motion / libro pop-up (`papel_recortado_popup`) — atractivo 5, tendencia 0.5
- Descripción: Recortes de papel stop-motion / libro pop-up
- Prompt base: `stop-motion paper cut-out scene inside an open pop-up book box, newsprint and sepia paper figures, red thread accents, cardboard background, warm dim lamp light, handmade feel, vertical 9:16, no text`
- Referencia: imaginantes/referencia_estilo_01.mp4
- Temas: lenguaje, semiótica, ideas abstractas

### Acuarela azul a línea (`acuarela_linea`) — atractivo 5, tendencia 0.27
- Descripción: Tinta fina con aguadas azules que se disuelven en blanco.
- Prompt base: `delicate blue watercolor wash with fine ink line drawing, monochrome indigo-blue tones fading to white paper, loose expressive brushwork, vertical 9:16, no text`
- Referencia: referencias_estilo/eb1f9964…webp, dc8d86b4…png
- Temas: música, ciudades, recuerdos, poesía

### Teatro de sombras retroiluminado (`teatro_sombras`) — atractivo 5
- Descripción: Siluetas de papel recortado frente a luz cálida, marco de teatrino.
- Prompt base: `shadow puppet theater, black paper cut silhouettes backlit by warm amber light, layered cut paper scenery, ornate wooden stage frame, vertical 9:16, no text`
- Referencia: referencias_estilo/889b5f93…webp, dc8d86b4…png
- Temas: mitos, leyendas, astronomía antigua, cuentos

### Óleo expresivo (`oleo_expresivo`) — atractivo 5
- Descripción: Pintura al óleo con empaste y pincelada visible.
- Prompt base: `expressive oil painting, thick impasto brushstrokes, dramatic chiaroscuro lighting, rich earthy palette, vertical 9:16, no text`
- Referencia: referencias_estilo/9e2b90b5…png
- Temas: biografías, drama humano, historia, filosofía

### Noche estrellada (Van Gogh) (`van_gogh`) — atractivo 5
- Descripción: Pinceladas en remolino, azules y amarillos.
- Prompt base: `post-impressionist painting in the style of Van Gogh's Starry Night, swirling brushstrokes, deep blues and glowing yellows, vertical 9:16, no text`
- Referencia: referencias_estilo/875e8a27…png
- Temas: astronomía, noche, arte, percepción

### Claymation / plastilina (propio) (`claymation`) — atractivo 5, tendencia 0.67
- Descripción: Personajes y escenarios de plastilina con huellas dactilares, stop-motion.
- Prompt base: `claymation stop-motion scene, plasticine characters and set with visible fingerprints, soft studio lighting, miniature handmade props, vertical 9:16, no text`
- Referencia: (propio)
- Temas: biología, cuerpo humano, animales, comida, vida cotidiana, ciencia, infancia, cocina

### Ukiyo-e (propio) (`ukiyo_e`) — atractivo 5
- Descripción: Grabado japonés en madera, líneas y planos de color.
- Prompt base: `ukiyo-e Japanese woodblock print, flat color areas, elegant outlines, stylized waves and clouds, washi paper texture, vertical 9:16, no text`
- Referencia: (propio)
- Temas: mar, terremotos, volcanes, naturaleza

### El Principito (película 2015) (`principito_2015`) — atractivo 5, tendencia 0.3
- Descripción: Mundo del principito en stop-motion de papel/cartón con texturas de papel maché, combinado con CG suave y luz cálida (Mark Osborne, 2015).
- Prompt base: `stop-motion papercraft world like The Little Prince 2015 film, paper mache and cardboard textures, tiny planet sets, soft warm CG lighting, gentle pastel palette, vertical 9:16, no text`
- Referencia: (propio; ref. película 2015)
- Temas: astronomía, filosofía, infancia, amistad, sueños, planeta, estrellas

### Animación clásica tipo Disney (`disney_clasico`) — atractivo 5, tendencia 0.15
- Descripción: Animación 2D clásica pintada a mano, fondos en gouache, personajes expresivos.
- Prompt base: `classic hand-drawn 2D animation still in the style of 1950s Disney feature films, painted gouache backgrounds, expressive characters, soft cel shading, vertical 9:16, no text`
- Referencia: (propio)
- Temas: cuentos, animales, mitos, naturaleza, historia, música

### Linograbado bitono (`linograbado`) — atractivo 4
- Descripción: Linograbado bitono
- Prompt base: `linocut print, two-tone indigo and ochre ink on cream paper, bold carved lines, visible gouge marks, high contrast, vertical 9:16 composition, no text`
- Referencia: referencias_estilo/cf63077f1c9a5cd380c5b4c5f9eaab1ce101ff40445a93a29b57846a30df793e.mp4 (cápsula El Niño)
- Temas: mar, historia, ciencia de la Tierra, oficios

### Muñecos tejidos amigurumi en miniatura (`amigurumi`) — atractivo 4, tendencia 0.25
- Descripción: Muñecos tejidos amigurumi en miniatura
- Prompt base: `miniature crochet amigurumi characters, macro photography, shallow depth of field, soft natural window light turning to warm firelight, handmade yarn texture, cozy diorama props, vertical 9:16, no text`
- Referencia: imaginantes/referencia_estilo_02.mp4
- Temas: ritos, emociones, infancia, antropología

### Cubismo con collage de periódico (`cubismo_collage`) — atractivo 4
- Descripción: Facetas geométricas tipo Picasso/Braque mezcladas con recortes de prensa.
- Prompt base: `analytical cubism painting with newspaper collage fragments, fragmented geometric planes, ochre, slate blue and brown palette, textured oil paint, vertical 9:16, no text`
- Referencia: referencias_estilo/d645dd7e…webp, abb4d20b…png
- Temas: arte, percepción, ciencia cognitiva, historia moderna

### Cómic pop art (`pop_art_comic`) — atractivo 4
- Descripción: Viñeta de cómic con puntos Ben-Day, onomatopeyas y colores primarios.
- Prompt base: `pop art comic book panel, Ben-Day halftone dots, bold black outlines, saturated primary colors, dramatic action burst background, vertical 9:16, no text`
- Referencia: referencias_estilo/abb4d20b…png
- Temas: inventos, física, superhéroes de la ciencia, explosiones

### Caricatura tipo Flapjack (`flapjack_cartoon`) — atractivo 4
- Descripción: Cartoon de Cartoon Network con texturas sucias y colores ácidos.
- Prompt base: `2000s Cartoon Network style cartoon, grotesque whimsical characters, textured painted backgrounds, sickly acid greens and pinks, nautical whimsy, vertical 9:16, no text`
- Referencia: referencias_estilo/19b20fd9…jpg, cdd8a76b…png
- Temas: mar, aventuras, humor, curiosidades absurdas

### Pixel art (`pixel_art`) — atractivo 4
- Descripción: Sprite de videojuego de 16 bits.
- Prompt base: `16-bit pixel art scene, limited retro palette, crisp pixels, side view video game style, dithering, vertical 9:16, no text`
- Referencia: referencias_estilo/92cb79c8…png
- Temas: tecnología, videojuegos, matemáticas, computación

### Pintura rupestre (`pintura_rupestre`) — atractivo 4
- Descripción: Ocres y manos estampadas sobre roca de cueva.
- Prompt base: `prehistoric cave painting on rough rock wall, red ochre and charcoal pigments, hand stencils, primitive figures, torchlight, vertical 9:16, no text`
- Referencia: referencias_estilo/416b6221…webp, 992c8247…png
- Temas: prehistoria, evolución, origen de ideas, astronomía antigua

### Cartel de propaganda vintage (`cartel_propaganda`) — atractivo 4
- Descripción: Póster de época con tipografía grande y heroísmo.
- Prompt base: `vintage 1940s propaganda poster, heroic pose, bold flat colors red cream and navy, aged printed paper texture, vertical 9:16, no text`
- Referencia: referencias_estilo/992c8247…png
- Temas: salud pública, guerras, campañas, ciencia y sociedad

### Figuras de cartón recortado (`carton_recortado`) — atractivo 4, tendencia 0.5
- Descripción: Figuras de cartón corrugado con bordes crudos, fotografiadas.
- Prompt base: `handmade figures cut from corrugated cardboard, raw torn edges, marker details, photographed on a table with soft light, vertical 9:16, no text`
- Referencia: referencias_estilo/46a2586c…png
- Temas: reciclaje, ingeniería, maquetas, oficios

### Retrato collage de papel cosido (`collage_papel_cosido`) — atractivo 4
- Descripción: Papeles y recortes de texto cosidos con hilo, relieve.
- Prompt base: `mixed media collage of stitched paper scraps and newspaper word cutouts, visible thread stitches, layered relief, muted denim and kraft tones, vertical 9:16, no text`
- Referencia: referencias_estilo/9f8eedbd…jpg
- Temas: literatura, mitos, identidad, viajes

### Póster de cine japonés de los 60 (`poster_cine_japones`) — atractivo 4
- Descripción: Cartel de película japonesa con tipografía y fotografía pintada.
- Prompt base: `1960s Japanese movie poster, painted photographic portraits, bold vertical typography blocks, retro print colors, worn paper, vertical 9:16, no text`
- Referencia: referencias_estilo/4d89af9a…jpg
- Temas: historias de grupo, cine, tecnología japonesa, aventuras

### Sketch de línea fina (tipo referencia bartending) (`linea_fina`) — atractivo 4
- Descripción: Dibujo a lápiz/tinta fino y limpio sobre blanco.
- Prompt base: `fine line pencil illustration on white paper, precise thin strokes, subtle graphite shading, minimal composition, vertical 9:16, no text`
- Referencia: referencias_estilo/66fca9e1…jpg (sketch bartending)
- Temas: objetos, química, diseño, anatomía, comida, bebidas, oficios, cocina

### Risografía (propio) (`risografia`) — atractivo 4
- Descripción: Impresión riso de 2–3 tintas con desregistro y grano.
- Prompt base: `risograph print, two-color fluorescent pink and teal overprint, misregistration, grainy texture, flat shapes, vertical 9:16, no text`
- Referencia: (propio)
- Temas: tecnología, datos curiosos modernos, cultura joven

### Vitral (propio) (`vitral`) — atractivo 4
- Descripción: Vidrio de colores con plomo, luz que atraviesa.
- Prompt base: `stained glass window, colorful glass pieces with thick black lead lines, light shining through, gothic arch, vertical 9:16, no text`
- Referencia: (propio)
- Temas: historia medieval, religión y ciencia, luz y óptica

### Bordado (propio) (`bordado`) — atractivo 4
- Descripción: Escena bordada a mano en tela con hilos.
- Prompt base: `hand embroidery on linen fabric, colorful thread stitches, satin and french knots, embroidery hoop edge visible, vertical 9:16, no text`
- Referencia: (propio)
- Temas: tradiciones, textiles, genética (hilos), México

### Stop-motion de papel (propio) (`papel_stop_motion`) — atractivo 4, tendencia 0.8
- Descripción: Recortes de papel planos animados sobre fondo de cartulina.
- Prompt base: `flat paper cut-out stop-motion animation frame, colored construction paper pieces, slight shadows, top-down view, vertical 9:16, no text`
- Referencia: (propio)
- Temas: explicaciones paso a paso, procesos, historia

### TV vieja con estática (tipo Coraje) (`tv_estatica`) — atractivo 3
- Descripción: Imagen en blanco y negro dentro de un televisor viejo, cuarto oscuro y ruido.
- Prompt base: `black and white cartoon image displayed on an old CRT television in a dark dusty room, scan lines, static noise, eerie vintage mood, vertical 9:16, no text`
- Referencia: referencias_estilo/7a88399c…webp
- Temas: misterios, miedos, medios de comunicación, paranormal explicado

### Crayones infantiles (`crayones_infantiles`) — atractivo 3
- Descripción: Dibujo de niño con crayones de cera sobre papel.
- Prompt base: `child's wax crayon drawing on white paper, naive shapes, bright colors, visible crayon strokes, cheerful sun, vertical 9:16, no text`
- Referencia: referencias_estilo/a0e10c96…png
- Temas: infancia, aprendizaje, biología básica, preguntas simples

### Stencil constructivista ruso (`constructivista_ruso`) — atractivo 3
- Descripción: Fotomontaje en rojo y negro con diagonales y tipografía soviética.
- Prompt base: `Russian constructivist propaganda photomontage, red and black on aged paper, bold diagonals, stencil shapes, grainy halftone photo, vertical 9:16, no text`
- Referencia: referencias_estilo/701bc164…png, 4289a904…png
- Temas: historia del s. XX, industria, revoluciones, semiótica

### Sátira de periódico en tinta (`satira_periodico`) — atractivo 3
- Descripción: Caricatura editorial en tinta con viñetas de diario.
- Prompt base: `editorial satirical newspaper cartoon, black ink crosshatching on newsprint, caricatured figures, newspaper columns layout, vertical 9:16, no text`
- Referencia: referencias_estilo/c9fa9cd0…webp, 92cb79c8…png
- Temas: política pública, economía, medio ambiente, noticias

### Stencil grafiti tipo Banksy (`stencil_banksy`) — atractivo 3
- Descripción: Esténcil negro sobre muro con un acento rojo.
- Prompt base: `Banksy-style street stencil art on a weathered concrete wall, black spray paint with a single red accent, drips, vertical 9:16, no text`
- Referencia: referencias_estilo/9e2b90b5…png
- Temas: crítica social, consumo, ecología, urbanismo

### Garabato en cuaderno (`garabato_cuaderno`) — atractivo 3
- Descripción: Dibujo a lápiz en hoja rayada con anotaciones.
- Prompt base: `pencil doodle sketch on lined notebook paper, hand-drawn arrows and small notes, graphite shading, spiral binding edge, vertical 9:16, no text`
- Referencia: referencias_estilo/18fd32b7…webp
- Temas: ideas, inventos, procesos mentales, estudio

### Crayón en nube de pensamiento (`crayon_nube`) — atractivo 3
- Descripción: Escena dibujada con crayón dentro de una nube de pensamiento.
- Prompt base: `crayon drawing inside a cartoon thought bubble floating over a soft paper background, dreamy, hand-colored, vertical 9:16, no text`
- Referencia: (identificado por el agente padre; no aislado en las capturas)
- Temas: imaginación, sueños, psicología, hipótesis

### Grafiti urbano colorido (`grafiti_colorido`) — atractivo 3
- Descripción: Mural de spray saturado con personajes.
- Prompt base: `colorful urban graffiti mural, saturated spray paint, playful cartoon characters, thick outlines, wildstyle accents, vertical 9:16, no text`
- Referencia: referencias_estilo/695b8137…webp
- Temas: ciudades, juventud, cultura popular, música
