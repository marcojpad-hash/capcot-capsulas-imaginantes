# Propuestas de plantillas visuales — Datos y ociosidades (2026-10-25)

Solo propuestas: **no** se ha editado `scripts/estilos.json`. Ids verificados contra el catálogo actual (no duplican `pixel_art`, `risografia`, `pop_art_comic`, `flapjack_cartoon`, `disney_clasico`, etc.). Inspiraciones = estilos genéricos de época; no copiar personajes, logos ni IP (p. ej. nada de personajes de Cuphead).

## 1. Tabla de propuestas

| nombre_estilo_id | descripción corta | prompt_base | paleta | subtemas sugeridos | atractivo | nota |
|---|---|---|---|---|---|---|
| rubber_hose_1930s | Cartoon de manguera de goma años 20-30, ojos “pie-cut”, guantes blancos, grano de película | 1930s rubber hose cartoon animation style, hand-inked bouncy characters with pie-cut eyes and white gloves, watercolor painted backgrounds, film grain, slight vignette, sepia-tinted vintage colors, single large character centered, simple background, flat illustrated, not photorealistic, vertical 9:16, no text | sepia, rojo tomate, amarillo mostaza, negro tinta, crema | insectos/eusocial (hormigas obreras animadas), microbiología (bacterias bailarinas), sueño/antro (sueños surrealistas) | 5 | Vibe Cuphead / Fleischer genérico; personajes originales, nada de IP |
| pulp_comic_1940s | Portada pulp de aventuras, tinta gruesa, colores desgastados | 1940s pulp adventure magazine cover illustration, dramatic low angle, heavy ink hatching, worn newsprint texture, faded four-color printing, one heroic subject large in frame, simple gradient sky, illustrated not photorealistic, vertical 9:16, no text | rojo óxido, amarillo, azul petróleo, papel amarillento | paleontología (dinosaurio amenazante), exploración/historia, clima extremo | 4 | Distinto de pop_art (sin Ben-Day/primarios): textura pulp |
| ligne_claire | Cómic europeo línea clara: contorno uniforme, colores planos | ligne claire European comic illustration, clean uniform black outlines, flat bright colors, no hatching, clear readable shapes, one main subject large, minimal background, illustrated, not photorealistic, vertical 9:16, no text | azul cielo, rojo, beige, verde claro | historia de la ciencia, inventos/transportes, geografía | 4 | Tradición genérica franco-belga, sin personajes conocidos |
| neon_noir | Noche lluviosa, neones, siluetas | neo-noir digital painting, dark rainy night, glowing magenta and cyan neon rim light, strong silhouette of a single subject, wet reflections, minimal background, painterly not photorealistic, vertical 9:16, no text | negro, magenta, cian, violeta | sueño/antro (insomnio, ciudad nocturna), neurociencia, crimen/forense | 4 | Cuidar legibilidad: sujeto con contraluz fuerte |
| atlas_antiguo | Mapa/atlas grabado s. XVII-XIX, rosas de los vientos, monstruos marinos | antique engraved atlas map illustration, hand-colored copperplate, compass rose, sea monsters, aged parchment, single large central motif, not photorealistic, vertical 9:16, no text | pergamino, sepia, verde mar, rojo lacre | clima/mar (corrientes, El Niño), migraciones animales, geología | 4 | Evitar texto cartográfico (no text) |
| collage_cientifico_vintage | Láminas de naturalista recortadas + papel viejo | vintage scientific collage, cut-out 19th century natural history engravings, botanical and anatomical plates, aged paper, muted pastel accents, one large specimen centered, plain background, not photorealistic, vertical 9:16, no text | crema, sepia, verde salvia, rosa viejo | mamíferos, insectos (láminas entomológicas), botánica | 5 | Láminas genéricas tipo grabado decimonónico |
| fieltro_stop_motion | Stop-motion de fieltro y lana, puntadas visibles | stop-motion felt animation diorama, needle felted wool characters, visible stitches, soft fuzzy textures, warm studio light, one large character, simple felt backdrop, handmade, not photorealistic, vertical 9:16, no text | lana cálida: mostaza, terracota, verde musgo | mamíferos (crías, hibernación), sueño infantil, ecología de bosque | 4 | No confundir con amigurumi (crochet) ni claymation |
| pixel_16bit_isometrico | Pixel art 16-bit isométrico tipo diorama de videojuego | 16-bit isometric pixel art diorama, crisp pixels, limited palette, dithered shading, one island-like scene with large central subject, empty dark background, retro game aesthetic, vertical 9:16, no text | paleta limitada SNES: azules, verdes, ocres | microbiología (célula como mapa), insectos/eusocial (hormiguero en corte), ciudades | 4 | Variante distinta del pixel_art existente (isométrico/diorama); usar solo si pixel_art no es la línea previa |
| dibujo_cientifico_scratchboard | Esgrafiado blanco sobre negro, ultra detallado | scratchboard illustration, white lines scratched on black, fine cross-hatching, dramatic single subject filling frame, black background, not photorealistic, vertical 9:16, no text | negro, blanco, opcional un acento ámbar | paleontología (fósiles), mar profundo, insectos | 4 | Gran legibilidad móvil por contraste |
| art_deco_poster | Póster Art Déco años 20-30, geometría y dorados | 1920s art deco travel poster illustration, streamlined geometric shapes, gold and teal, airbrushed gradients, one bold central subject, minimal background, not photorealistic, vertical 9:16, no text | teal, dorado, negro, crema | clima/mar (trasatlánticos, océano), astronomía, tecnología temprana | 4 | Pareja natural de rubber_hose_1930s (misma época) — no consecutivos salvo misma sublínea |
| microscopio_psicodelico | Ilustración psicodélica 60s de formas orgánicas | 1960s psychedelic poster art, flowing organic shapes, vibrant complementary colors, microscopic organisms as large central motif, simple swirling background, illustrated, not photorealistic, vertical 9:16, no text | naranja, magenta, verde lima, violeta | microbiología, química, percepción/sueño | 3 | Riesgo de saturar: sujeto único |

## 2. Ids propuestos
`rubber_hose_1930s`, `pulp_comic_1940s`, `ligne_claire`, `neon_noir`, `atlas_antiguo`, `collage_cientifico_vintage`, `fieltro_stop_motion`, `pixel_16bit_isometrico`, `dibujo_cientifico_scratchboard`, `art_deco_poster`, `microscopio_psicodelico` (11).

## 3. Mapa sublínea → estilos (nuevos + existentes)
- **Paleontología:** dibujo_cientifico_scratchboard, pulp_comic_1940s, pintura_rupestre
- **Insectos / eusocial:** rubber_hose_1930s, pixel_16bit_isometrico, collage_cientifico_vintage
- **Mamíferos:** fieltro_stop_motion, collage_cientifico_vintage, claymation
- **Microbiología:** microscopio_psicodelico, rubber_hose_1930s, pixel_16bit_isometrico
- **Sueño / antropología:** neon_noir, rubber_hose_1930s, amigurumi, teatro_sombras
- **Clima / mar:** atlas_antiguo, art_deco_poster, linograbado, ukiyo_e
- **Historia de la ciencia / inventos:** ligne_claire, art_deco_poster, cartel_propaganda

## 4. Reglas de asignación
1. **Nunca** repetir el estilo de la cápsula inmediatamente anterior.
2. Mismo estilo **solo** si la cápsula pertenece a la misma sublínea/serie (p. ej. parte 2 de hormigas). No basta “biología” genérica.
3. Evitar estilos “hermanos” consecutivos (rubber_hose ↔ flapjack_cartoon/disney_clasico; pixel_art ↔ pixel_16bit; art_deco ↔ rubber_hose) salvo misma sublínea.
4. Legibilidad móvil: un sujeto grande (≥40 % del cuadro), fondo simple, alto contraste, sin texto generado; los rótulos van en postproducción.
5. Todos los prompts anti-fotorreales (“illustrated / not photorealistic”) y 9:16.
6. Respetar IP: inspiración de época sí; personajes, logos o escenas reconocibles no.
7. Antes de añadir a `estilos.json`: generar 1 frame de prueba por estilo y que Mj apruebe (atractivo provisional hasta entonces).

## 5. Añadido Mj 27-oct-2026 — acuarela japonesa
Id: `acuarela_japonesa`. Ref visual de Mj (story: gato + máscara, estética acuarela japonesa). Entrar al catálogo como plantilla posible: solo look (aguadas/washi), sin gag ni IP ajena. Pendiente frame de prueba antes de meter a `scripts/estilos.json`.
