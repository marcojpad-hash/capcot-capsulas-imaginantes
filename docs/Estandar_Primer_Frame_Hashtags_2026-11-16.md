# Estándar de primer frame y hashtags — Datos y ociosidades (2026-11-16)

**Decisión de Marco 2026-11-16:** lo único que se cambia es que **todos los Shorts aparezcan con el primer frame donde se lea el título**, y queda **estandarizado en la línea editorial el uso de hashtags que funcionen y atrapen**. Lo ya publicado se deja como está en contenido; solo se les puede cambiar la miniatura (ver §3). Esto es la regla para todo lo que viene.

## 1. Primer frame (obligatorio en todo Short nuevo)

- El frame 0:00–0:03 lleva el **título quemado, legible a tamaño de miniatura**: mayúsculas negras sobre fondo amarillo/beige, subrayado rojo en la última línea, máximo 3 líneas.
- El quemado dice **exactamente el mismo texto que el título de la cuadrícula** (mismas palabras, en mayúsculas). Nada de paráfrasis.
- El título se lee sin abrir el video. Si en la miniatura no se alcanza a leer, el Short no sale.
- Esto ya lo cumplen 42 de 48. Los 6 que no lo traen son la excepción que se corrige en miniatura (§3), no el estándar.

## 2. Título de la cuadrícula

- Frase en formato oración, como ya se hace ("El sarampión volvió a México después de 30 años").
- Siempre con los hashtags del §3 al final.
- Sin títulos en minúsculas sueltas ("se fugo la ia"), sin hashtags raros en lugar de #Shorts.

## 3. Hashtags (estándar)

**Regla base — siempre #Shorts (con S mayúscula) al final del título.** Es el clasificador de Shorts de YouTube. Evidencia del canal (revisión 2026-11-16, 48 Shorts): 43 lo traen; los más vistos (Mpemba 966, bebé huesos 919, árboles 749) lo traen. Los que no lo traen o lo traen mal: #4 (agua sartén, sin hashtag), #8 ("se fugo la ia", sin hashtag), #28 ("#shorts" en minúsculas), #3 (trae "#inteligenciaartificial" en lugar de #Shorts).

**Fórmula por Short (máximo 3 hashtags en total):**

1. `#Shorts` — siempre, al final.
2. **1 hashtag de tema** — solo si el tema se busca o es tendencia, en minúsculas, una palabra: `#ciencia`, `#historia`, `#espacio`, `#salud`, `#animales`, `#mitooverdad`, `#inteligenciaartificial` (este último ya se usó en el apagón, el tema que más jaló en TikTok).
3. Opcional: `#DatosYOciosidades` como marca del canal, solo cuando el título queda corto.

**Prohibido:** más de 3 hashtags; hashtags en medio del título; "#shorts" en minúsculas; sustituir #Shorts por un hashtag de tema; hashtags genéricos que no aportan búsqueda (#video, #viral, #fyp, #parati).

**Por plataforma:** en YouTube va la fórmula de arriba. En TikTok se usa el mismo hashtag de tema + #Shorts no aplica igual; ahí mandan el tema y la tendencia del momento (el apagón jaló con el tema, no con el hashtag).

## 4. Los 6 publicados sin título en el primer frame (solo cambio de miniatura, no se re-sube nada)

| # | Título | Vistas (16-nov) | Acción |
|---|---|---|---|
| 2 | El pulpo reparte el trabajo entre tres corazones | 50 | Cambiar miniatura por tarjeta de título |
| 3 | ¿Se va la luz el 17 de noviembre por una IA? | 8 | Cambiar miniatura por tarjeta de título |
| 4 | El agua que baila sobre el sartén | 607 | Cambiar miniatura por tarjeta de título |
| 6 | El mapa 3D del cerebro fetal que revela el origen de la esquizofrenia | 45 | Cambiar miniatura por tarjeta de título |
| 10 | El colibrí que se enfría casi como una piedra | 36 | Cambiar miniatura por tarjeta de título |
| 23 | El agua caliente se congela más rápido que la fría | 966 | Cambiar miniatura por tarjeta de título |

Cambiar la miniatura en YouTube Studio no toca el video ni borra las vistas. Requiere entrar a Studio con la cuenta dueña (marcosabines@gmail.com, aprobación en el teléfono de Marco). Pendiente de que Marco diga cuándo hacerlo; no se hace solo.

## 5. Chequeo antes de montar (para que no se filtre)

Antes de montar cualquier Short nuevo, verificar: (1) primer frame con título legible, quemado = título de cuadrícula; (2) título con #Shorts + máximo 1 de tema; (3) anti-duplicados en `data/publicaciones.json` y en la cuadrícula (título, tema y miniatura); (4) sin "#shorts" en minúsculas. Esto se suma al chequeo pre-publicación que ya existe (`capsule_prepublish_checks`).
