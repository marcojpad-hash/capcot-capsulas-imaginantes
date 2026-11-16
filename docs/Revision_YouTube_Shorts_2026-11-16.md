# YouTube Datos y ociosidades — Revisión de Shorts: repeticiones y estandarización (2026-11-16)

**Revisión en vivo de la pestaña Shorts de https://www.youtube.com/@datosyociosidades/shorts, 16-nov-2026, solo lectura. Canal: 85 suscriptores, 81 vídeos en total, 48 Shorts visibles en la cuadrícula (orden "Más recientes", recorrida hasta el final).**
**Cruce con el repo:** `data/publicaciones.json` (44 entradas) y línea editorial (`docs/BIBLIA_LINEA_EDITORIAL.md`, `docs/ESTRUCTURA_VISUAL_TRENDS.md`).

## Veredicto en una línea

Tienes razón, amor: **no está estandarizado**. El patrón dominante existe (42 de 48), pero hay 6 Shorts sin él, 4 grupos de duplicados (9 entradas) y el título quemado en la miniatura muchas veces no dice lo mismo que el título de la cuadrícula. Los ya publicados se dejan como están, como pediste; lo que viene debe salir con el estándar de abajo.

## 1. El patrón dominante (42 de 48)

Título quemado en **mayúsculas negras sobre fondo amarillo/beige, con subrayado rojo en la última línea**. Es el estándar de facto del canal. Ejemplos: "EL SARAMPIÓN VOLVIÓ A MÉXICO DESPUÉS DE 30 AÑOS", "DE BEBÉ TENÍAS MÁS HUESOS", "¿LOS ÁRBOLES HABLAN?".

## 2. Excepciones: 6 Shorts sin el patrón

Sin título grande quemado, solo subtítulo blanco pequeño en minúsculas o solo ilustración:

| # | Título en cuadrícula | Vistas | Qué se ve en la miniatura |
|---|---|---|---|
| 2 | El pulpo reparte el trabajo entre tres corazones | 50 | Solo ilustración del pulpo naranja, sin título |
| 3 | ¿Se va la luz el 17 de noviembre por una IA? | 8 | Subtítulo blanco "17 de noviembre: solo una prueba / pero en Estados" |
| 4 | El agua que baila sobre el sartén | 607 | Subtítulo blanco "si la gota", acuarela |
| 6 | El mapa 3D del cerebro fetal que revela el origen de la esquizofrenia | 45 | Subtítulo blanco "287 mil células / primera vez la" |
| 10 | El colibrí que se enfría casi como una piedra | 36 | Subtítulo blanco "punto veintiséis grados" |
| 23 | El agua caliente se congela más rápido que la fría | 966 | Subtítulo blanco en minúsculas "El agua caliente se congela antes que la fría." — es el Short más visto de la cuadrícula |

Ojo: el #23 (Mpemba, 966 vistas) es el más visto y es justo uno de los que NO trae el título quemado. El patrón no es lo que hace el éxito, pero la cuadrícula se ve dispareja.

## 3. Duplicados y casi idénticos: 4 grupos, 9 entradas, 43 contenidos únicos

| Grupo | Entradas | Detalle |
|---|---|---|
| Apagón 17-nov | #3 (8 vistas), #5 (4), #8 (0) | Tres videos del mismo tema. #5 y #8 comparten la miniatura idéntica (televisor con casa, "¿APAGÓN EL 17 DE NOVIEMBRE?"). #8 trae el título en minúsculas en la cuadrícula ("se fugo la ia"), sin #Shorts. |
| Ratas topo | #17 (15 vistas), #19 (285) | Miniatura idéntica "RATAS TOPO: MÁS TRABAJO TRAS EL NACIMIENTO", títulos distintos en la cuadrícula. |
| Hipo | #26 (8 vistas), #36 (1) | Título en cuadrícula y miniatura idénticos "¿QUIÉN DISPARA ESE HIC?". |
| Capsaicina | #24 (23 vistas), #40 (20) | Título en cuadrícula y miniatura idénticos "¿AGUA O LECHE AL ENCHILARTE?". |

**Cruce con el repo (`data/publicaciones.json`, 44 entradas):** ningún `yt_id` repetido (no se subió dos veces el mismo archivo), pero el título "Un ave de hace 150 millones de años con dientes de dinosaurio… y sin vuelo" aparece **3 veces con 3 yt_id distintos** (IzWU_1BXq3Q, GHxm9dDUMmM, YKldyldCeiQ), y el project_id `2026-10-25_ave-jurasica-sin-vuelo` aparece 2 veces; el tema aves-mujeres también va 2 veces ("Las aves huyen antes de las mujeres" y "¿Aves que temen a mujeres?"). El registro no marca estos como duplicados: es el mismo hueco de siempre (registro incompleto, 44 entradas vs ~80 videos).

**Discrepancia con tu captura:** en la captura que mandaste, el Short del dibujo en la tele ("cincuenta y cinco") aparece dos veces en la cuadrícula (5 vistas y Sin vistas). En la revisión en vivo de hoy ese video **no aparece entre los 48** — puede que se haya eliminado, que sea un video programado que ya no se ve, o que la captura sea de otro momento. No lo puedo confirmar sin entrar a la cuenta; lo dejo anotado, no inventado.

## 4. El título quemado no dice lo mismo que el título de la cuadrícula

En muchos casos el quemado es una paráfrasis del título, no el mismo texto:

| # | Título en cuadrícula | Título quemado en la miniatura |
|---|---|---|
| 7 | Microbioma intestinal y cerebro en autismo | ¿EL INTESTINO HABLA AL CEREBRO? |
| 11 | Un aminoácido cambia el virus Andes | UN SOLO AMINOÁCIDO |
| 13 | ¿Los árboles hablan bajo tierra? | ¿LOS ÁRBOLES HABLAN? |
| 16 | El pez que mira a través de su cabeza | PEZ DE CABEZA TRANSPARENTE |
| 18 | Esa nube puede cargar quinientas toneladas | ESA NUBE PESA MÁS DE LO QUE CREES |
| 20 | ¿El arroz de ayer puede enfermarte? | ¿EL ARROZ DE AYER? |
| 21 | La corneja decide en 235 milisegundos | LA CORNEJA DECIDE ANTES DEL PICOTAZO |
| 48 | El hielo que sostuvo tres mantos | ¿QUÉ SOSTUVO TRES MANTOS? |

Además: #28 trae "#shorts" en minúsculas en la cuadrícula (el resto "#Shorts"), y #3 trae "#inteligenciaartificial" en vez de "#Shorts".

## 5. Qué dice la línea editorial del repo (y por qué no se cumple)

- `docs/ESTRUCTURA_VISUAL_TRENDS.md` (regla de gancho): el texto en pantalla desde el frame 1 debe ser **la afirmación sorprendente (el gancho), no el título**. Y el `on_screen_text` de la escena 1 va en tarjeta grande (92 px, fondo ocre) desde el frame 0.
- `docs/BIBLIA_LINEA_EDITORIAL.md`: "9:16 con sujeto grande y **sin texto dentro de la imagen**" (eso es para el frame/ilustración, el texto va en postproducción).
- Realidad: 42 de 48 queman el título en la miniatura/primer frame, y en 8+ casos ese texto ni siquiera es el título. O sea: el canal usa el título quemado como estándar de facto, pero la regla escrita dice otra cosa (gancho, no título) y nadie la está aplicando igual.

## 6. Estándar propuesto para lo que viene (no tocar lo ya publicado)

1. **Primer frame / miniatura:** título quemado en mayúsculas negras sobre fondo amarillo/beige, subrayado rojo en la última línea, máximo 3 líneas. Es el patrón que ya siguen 42 de 48: se vuelve regla, no costumbre.
2. **El quemado dice EXACTAMENTE lo mismo que el título de la cuadrícula** (mismas palabras, en mayúsculas). Nada de paráfrasis: si el video se llama "El pez que mira a través de su cabeza", el quemado dice eso, no "PEZ DE CABEZA TRANSPARENTE".
3. **Título de la cuadrícula:** frase en formato oración (como ya se hace: "El sarampión volvió a México después de 30 años"), siempre con "#Shorts" (con S mayúscula), sin minúsculas sueltas ni hashtags raros.
4. **Antes de montar:** chequeo anti-duplicados en `data/publicaciones.json` + en la cuadrícula (título, tema y miniatura). Un tema = un Short; si ya existe, no se vuelve a montar con otro título.
5. **Excepciones:** las 6 sin título quemado se quedan como están (publicadas, no se tocan). El #23 es el más visto: no se toca nada que funcione.

## 7. Lista completa de la cuadrícula (48, orden "Más recientes")

1. El sarampión volvió a México después de 30 años — 59 — EL SARAMPIÓN VOLVIÓ A MÉXICO DESPUÉS DE 30 AÑOS
2. El pulpo reparte el trabajo entre tres corazones #Shorts — 50 — sin título quemado (ilustración pulpo)
3. ¿Se va la luz el 17 de noviembre por una IA? #inteligenciaartificial — 8 — subtítulo "17 de noviembre: solo una prueba / pero en Estados" [duplicado apagón]
4. El agua que baila sobre el sartén — 607 — subtítulo "si la gota"
5. No habrá apagón el 17 de noviembre — 4 — ¿APAGÓN EL 17 DE NOVIEMBRE? [duplicado, miniatura = #8]
6. El mapa 3D del cerebro fetal que revela el origen de la esquizofrenia #Shorts — 45 — subtítulo "287 mil células / primera vez la"
7. Microbioma intestinal y cerebro en autismo #Shorts — 19 — ¿EL INTESTINO HABLA AL CEREBRO?
8. se fugo la ia — 0 — ¿APAGÓN EL 17 DE NOVIEMBRE? [duplicado, miniatura = #5; título en minúsculas]
9. Agua que une imanes lejanos #Shorts — 46 — AGUA UNE IMANES
10. El colibrí que se enfría casi como una piedra #Shorts — 36 — subtítulo "punto veintiséis grados"
11. Un aminoácido cambia el virus Andes #Shorts — 139 — UN SOLO AMINOÁCIDO
12. El rosa del flamenco viene de su comida #Shorts — 2 — EL ROSA VIENE DE SU COMIDA
13. ¿Los árboles hablan bajo tierra? #Shorts — 749 — ¿LOS ÁRBOLES HABLAN?
14. De bebé tenías más huesos que ahora #Shorts — 919 — DE BEBÉ TENÍAS MÁS HUESOS
15. ¿Aves que temen a mujeres? — 528 — ¿AVES QUE TEMEN A MUJERES?
16. El pez que mira a través de su cabeza #Shorts — 24 — PEZ DE CABEZA TRANSPARENTE
17. ¿Por qué trabajan más las ratas topo cuando nacen sus crías? #Shorts — 15 — RATAS TOPO: MÁS TRABAJO TRAS EL NACIMIENTO [duplicado, miniatura = #19]
18. Esa nube puede cargar quinientas toneladas #Shorts — 11 — ESA NUBE PESA MÁS DE LO QUE CREES
19. Ratas topo: más trabajo tras el nacimiento #Shorts — 285 — miniatura = #17 [duplicado]
20. ¿El arroz de ayer puede enfermarte? #Shorts — 300 — ¿EL ARROZ DE AYER?
21. La corneja decide en 235 milisegundos #Shorts — 0 — LA CORNEJA DECIDE ANTES DEL PICOTAZO
22. Esta ballena bajó a dos latidos por minuto #Shorts — 208 — DOS LATIDOS POR MINUTO
23. El agua caliente se congela más rápido que la fría #Shorts — 966 — sin título grande; subtítulo "El agua caliente se congela antes que la fría."
24. Capsaicina: ¿agua, refresco o leche? — 23 — ¿AGUA O LECHE AL ENCHILARTE? [duplicado, = #40]
25. El hueso no salva tu guacamole #Shorts — 132 — EL HUESO NO SALVA TU GUACAMOLE
26. ¿Por qué tenemos hipo? #Shorts — 8 — ¿QUIÉN DISPARA ESE HIC? [duplicado, = #36]
27. Esta rana se congela y vuelve a saltar #Shorts — 110 — SE CONGELA Y VUELVE A SALTAR
28. ¿Qué queda en tu cocina después de limpiar? #shorts — 134 — ¿QUÉ QUEDA EN TU COCINA TRAS LIMPIAR? (#shorts en minúsculas)
29. Tus palomitas explotan por dentro #Shorts — 141 — PALOMITAS: UNA OLLA POR DENTRO
30. El refri puede endurecer tu pan más rápido #Shorts — 101 — EL REFRI ENDURECE TU PAN
31. En Venus el año acaba antes de dos días #Shorts — 94 — VENUS: UN AÑO EN MENOS DE DOS DÍAS
32. Esta arena canta sin una sola bocina #Shorts — 48 — LA ARENA QUE CANTA
33. Este polvo atrapa 5 veces su peso en oro #Shorts — 123 — ESTE POLVO ATRAPA 5 VECES SU PESO EN ORO
34. El mar que fabrica luz #Shorts — 58 — EL OCÉANO TAMBIÉN BRILLA
35. ¿La miel nunca se echa a perder? #Shorts — 59 — LA MIEL DESAFÍA AL TIEMPO
36. ¿Por qué tenemos hipo? #Shorts — 1 — = #26 [duplicado]
37. El polvo de África no viaja solo #Shorts — 273 — EL POLVO DE ÁFRICA NO VIAJA SOLO
38. SmartPE: edición genética más precisa en plantas #Shorts — 72 — EDITAR PLANTAS CON PRECISIÓN
39. La frontera invisible de Júpiter #Shorts — 59 — LA FRONTERA INVISIBLE
40. Capsaicina: ¿agua, refresco o leche? — 20 — = #24 [duplicado]
41. La química del dorado #Shorts — 91 — ¿POR QUÉ SE DORA?
42. Cuando el viento y el Sol fallan juntos #Shorts — 27 — ¿Y SI FALTAN AMBOS?
43. Los murciélagos y sus virus #Shorts — 103 — ¿QUÉ DEFINE SUS VIRUS?
44. El pan no solo se seca #Shorts — 44 — EL PAN NO SOLO SE SECA
45. Un golpe bajo el agua #Shorts — 153 — UN GOLPE BAJO EL AGUA
46. La química detrás de las lágrimas — 274 — LA QUÍMICA DETRÁS DE LAS LÁGRIMAS
47. El tiburón que vive siglos #Shorts — 216 — UN TIBURÓN DE SIGLOS
48. El hielo que sostuvo tres mantos #Shorts — 80 — ¿QUÉ SOSTUVO TRES MANTOS?
