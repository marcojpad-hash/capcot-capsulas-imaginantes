# Estilos visuales — catálogo y rotación

El estilo es de la **serie**, no de un personaje: cada cápsula usa un estilo distinto y el pipeline los rota.
Fuente de datos para el código: `scripts/estilos.json` · rotación: `scripts/rotar_estilo.py` (elige el menos usado
según `data/estilos_usados.json`; `capsula_diaria.py --estilo <id>` lo fuerza).

Búsqueda de plantillas (2026-10-24): en /workspace/imaginantes y /workspace/capcot **no hay imágenes llamadas
"niño pino", "niño árbol" ni similares** (búsqueda por nombre en todo el disco). Los estilos se catalogaron a partir
de los clips de referencia de Mj, del demo-001 y de la cápsula El Niño. Si Mj comparte esas plantillas, agregarlas aquí.

| id | Estilo | Origen | Paleta | Audio sugerido |
|---|---|---|---|---|
| linograbado | Linograbado bitono | Cápsula El Niño (aprobado por Mj) | índigo, ocre, crema | océano+viento, pad sintético |
| papel_rasgado_capas | Papel rasgado por capas (diorama) | demo-001 v2 (Tunguska) | verde bosque, turquesa, ocre, crema | viento, pad |
| papel_recortado_popup | Recortes de papel stop-motion / pop-up | referencia_estilo_01 "El perro de papel" | sepia, cartón, acentos rojos | caja de música |
| amigurumi | Muñecos tejidos en miniatura | referencia_estilo_02 "Muñecos tejidos" | cálida → oscura con luz de fuego | piano melancólico |

## Prompts base (se anteponen como `Style:` a cada `image_prompt`)
- **linograbado:** linocut print, two-tone indigo and ochre ink on cream paper, bold carved lines, visible gouge marks, high contrast, vertical 9:16 composition, no text
- **papel_rasgado_capas:** layered torn paper collage diorama, deckled paper edges, felt and cardstock textures, muted teal, forest green, ochre and cream, soft side light with depth shadows between layers, vertical 9:16, no text
- **papel_recortado_popup:** stop-motion paper cut-out scene inside an open pop-up book box, newsprint and sepia paper figures, red thread accents, cardboard background, warm dim lamp light, handmade feel, vertical 9:16, no text
- **amigurumi:** miniature crochet amigurumi characters, macro photography, shallow depth of field, soft natural window light turning to warm firelight, handmade yarn texture, cozy diorama props, vertical 9:16, no text

## Reglas
- Mismo estilo en todas las escenas de una cápsula; distinto entre cápsulas consecutivas.
- Sin texto dentro de la imagen (la IA deforma letras; el texto va como `on_screen_text`/subtítulos).
- Para agregar un estilo: nueva entrada en `scripts/estilos.json` + fila aquí.
