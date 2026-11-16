# La Putiza — v1 vs v2 del piloto: cuál está más estable y cómo mejorarla

**Comparación hecha 2026-11-16, con diff real de los dos JSON y búsqueda web sobre Charín y Mateo.**

## Veredicto en una línea

**La v2 es más estable.** Es la misma estructura que v1 con solo 5 cambios medidos, y los 5 van en la misma dirección: Gerry deja de ser un gag suelto (gel antibacterial) y se vuelve un arco con callback (abre preocupado por Charín, cierra amenazando por Charín). No hay ningún cambio estructural que pueda romper la generación.

## 1. Diff exacto v1 → v2 (148 hojas del JSON, solo 5 difieren)

| # | Dónde | v1 | v2 |
|---|---|---|---|
| 1 | Escena 2, línea de Gerry | "¡Y no vayan a mencionar a Mateo que nos tumban el video!" | "¡Y no vayan a mencionar a Charín que nos desmonetizan hasta el alma!" |
| 2 | Escena 4, línea de Gerry | "¡Uno, dos, tres! ¡Corte! ¡Quedó perfecto, déjame me pongo mi gel antibacterial!" | "¡Uno, dos, tres! ¡Corte! ¡Quedó de huevos, pero el primero que le diga a Charín que mancharon el estudio va a limpiar esta plastilina con la lengua!" |
| 3 | Escena 4, delivery de Gerry | "relieved and hurried" | "stressed and threatening" |
| 4 | Escena 4, visual_action | "...Gerry counts three with his clipboard and raises Slobo's bloody arm." | "...Gerry counts three with his clipboard, threatens the crew about Charín, and raises Slobo's bloody arm." |
| 5 | Escena 4, sfx | Incluye "Hand sanitizer pump squirt" (6 sfx) | Eliminado (5 sfx) |

Personajes, voces, escenas 1 y 3, duraciones, aspect_ratio 16:9 y 180 s: **idénticos en ambas**.

## 2. Investigación: quiénes son Charín y Mateo (fuentes web, 2026-11-16)

- **Charín Ruiz** es la esposa de José Luis Slobotzky: se casaron en 2021, se conocieron en 2014 en la Universidad Anáhuac. Es influencer y diseñadora industrial originaria de Oaxaca, directora y fundadora de Galera Diseño. Es figura recurrente del lore de La Cotorrisa (los fans la conocen, hay chistes de ella como "tercera rueda" entre Slobo y Ricardo, y la anécdota de la salsa picante que se comió por educación).
- **Mateo** es el hijo de Slobotzky y Charín: nació en 2025 (anunciado el 9 de mayo de 2025 en Instagram) y es tema recurrente de las anécdotas de paternidad de Slobo en el podcast ("La rutina de loquito de Mateo").

**Qué significa para el guion:**
- La v1 mete al bebé (Mateo) en un chiste de "nos tumban el video" dentro de un video violento. No es un error grave, pero es el chiste más flojo y el más delicado de los dos.
- La v2 mete a Charín, adulta, figura pública del lore, con un chiste que los fans reconocen ("que nos desmonetizan hasta el alma" es más específico y más gracioso que "nos tumban el video"). Y el cierre de Gerry convierte la mención en callback: Charín aparece 3 veces en v2 (escena 2, escena 4 línea y escena 4 acción) contra 0 en v1.
- La "cacofonía de mencionar a Mateo" que motivó el cambio es discutible como fonética ("mencionar a Mateo" repite la m), pero el cambio se justifica por el chiste y por el arco, no por la fonética.

## 3. Estabilidad de tiempos (diálogo medido, a 150 palabras por minuto)

| Escena | Duración | Palabras | Hablado aprox. | Hueco |
|---|---|---|---|---|
| 1 (0:00-0:40) | 40 s | 135 | ~54 s | **-14 s: NO CABE.** A 150 ppm se pasa 14 s; a 180 ppm (muy rápido) se pasa 5 s. |
| 2 (0:40-1:35) | 55 s | v1 118 / v2 119 | ~47-48 s | ~7-8 s de acción. Bien. |
| 3 (1:35-2:20) | 45 s | 39 | ~16 s | ~29 s de acción muda. Mucho vacío, igual en ambas. |
| 4 (2:20-3:00) | 40 s | v1 84 / v2 99 | v1 ~34 s / v2 ~40 s | v1: 6 s libres. **v2: llena exacto los 40 s.** |
| **Total** | **180 s** | **v1 376 / v2 392** | **v1 ~150 s / v2 ~157 s** | v2 deja 23 s de aire total vs 30 s de v1. |

**Lectura:** la v2 mejora el ajuste de la escena 4 (de 6 s libres a 0) y no empeora nada más. El problema de tiempo es de la escena 1 y existe en ambas versiones por igual.

## 4. ¿Se puede mejorar el guion? Sí — 5 propuestas (propuestas, NO aplicadas)

1. **Escena 1, la más urgente:** recortar ~20 palabras o alargar la escena a 0:00-0:50 y quitarle 10 s a la escena 3. Hoy el diálogo no cabe en 40 s a velocidad natural. Candidatos a recorte: la presentación de Ricardo ("experto en darle respiración de boca a boca a la tercera edad" es larga) o la de Slobo.
2. **Escena 3, llenar el vacío de 29 s:** 1-2 líneas cortas de cabina mientras Ricardo se desinfla (Franco/La Mole comentando el desinflado). La revisión de VidoGrid ya advertía este hueco: "diálogo efectivo solo ~4 s por escena, hay que llenar con acción muda".
3. **Desinflado en dos cortes:** no pedir la transformación (jeringa → desinflado) en un solo clip; dividir en impacto de jeringa y corte a Ricardo ya flaco en la lona. La revisión de VidoGrid lo recomendaba; el guion lo mantiene en un solo bloque.
4. **Decidir el formato antes de generar:** ambas versiones dicen 16:9, pero Flow y VidoGrid son 9:16 vertical y el canal es de Shorts. Si va a Shorts/TikTok, 16:9 está mal; si va a YouTube largo horizontal, está bien. Es la decisión pendiente más grande.
5. **Voces cruzadas con VidoGrid (igual en ambas):** la nasal/gangosa aquí es Gerry y la teatral es Slobotzky; en el JSON de VidoGrid era al revés. Como el piloto es canónico, el JSON de VidoGrid queda como versión anterior, pero hay que anotarlo para no mezclarlos al generar.

## 5. Archivos

- v1 (canónica hasta ahora): `La_Putiza_Episodio_Piloto_definitivo_2026-11-16.md` + `La_Putiza_piloto.json` — en GitHub, rama `pecas/la-putiza-piloto-2026-11-16`, commit `758ccfc9`.
- v2: `La_Putiza_piloto_v2.md` + `La_Putiza_piloto_v2.json` — locales, pendientes de subir a la misma rama si Marco la adopta.
- Fuentes web: tvazteca.com (Charín Ruiz, esposa de Slobotzky, casados 2021), gluc.mx / heraldodemexico.com.mx (quién es Charín), todosloshechos.es (Mateo, hijo de la pareja), facebook.com/LaCotorrisa (rutina de Mateo).
