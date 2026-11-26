# Skill: ganchos virales — desarmar videos virales y reproducir su estructura

Fecha: 2026-11-26. Origen: investigación de herramientas y métodos de
desglose viral (nov 2026). Verificado en vivo 26-nov-2026: TransClipper
(página del analizador) y los prompts publicados enlazados abajo.
Estado: vigente. Se usa ANTES de escribir guiones nuevos, no después.

## Para qué sirve

Copiar la estructura de un video viral (gancho, ritmo, retención, cierre)
sin copiar sus palabras ni sus datos. "Mismos huesos, otra piel."

Nació del flop de Barco Blanco (25-nov-2026, 12 vistas, 1 like): los
hashtags estaban bien y el video sí llegaba a la gente — el fallo era el
gancho. La lección quedó en `~/AGENTS.md` (Pecas): si el video ya recibió
aunque sea un like, el fallo es el gancho, no la distribución; y si el tema
no atrae ni a Marco, no va, por importante que sea el hecho.

## Herramientas

### Analizar un video (pegar URL → desglose)

| Herramienta | Qué hace | Costo (nov 2026) |
|---|---|---|
| **TransClipper — Viral Video Analyzer** (https://transclipper.ai/viral-video-analyzer) | Pega URL de TikTok/Reel/Short → transcripción (del audio, 50+ idiomas incl. español), línea exacta de apertura, arquetipo de gancho, progresión narrativa, CTA y puntaje viral 0–100. También: generador de ganchos y de guiones (Pro). | Gratis: 3/día sin cuenta, 5/día con cuenta, videos hasta 2 min. Pro $4.08/mes facturado anual ($49/año) según su sitio, verificado 26-nov-2026. OJO: otro review reporta Pro $9.99/mes o $7.42/mes anual — re-checar el precio en la página antes de pagar. |
| **SortViral** (https://www.sortviral.com/) | Extensión gratis: ordena los videos de un canal por outlier (vistas vs mediana del canal). Así se encuentran los videos que de verdad rindieron, no los de canales grandes. | Gratis, sin registro. |
| **1of10** | Buscador de outliers por nicho, sin conocer canales antes. | Gratis 60 créditos/mes. |
| **vidIQ / Viewstats / Faceless.so** | Señales de outlier, vistas por hora, seguimiento de competidores. | Tiers gratis. |

### Pagar solo si el volumen es el cuello de botella

- **Viral Outliers** $17/mes — búsqueda de outliers por nicho + convertirlos en ganchos/guiones.
- **Runwave AI** $19/mes (primer mes $5) — desglose de un video → guion listo.
- **Sandcastles AI** $49/mes, **Virlo** $49/mes — investigación + guion en una sola herramienta.
- No se compra una herramienta para arreglar un solo video flojo: primero se
  corre el flujo gratis sobre ese mismo video (su transcripción + su gráfica
  de retención) para ver si falló el gancho, el refuerzo o un payoff
  demasiado temprano.

## Método: los prompts

El detalle completo, con los prompts listos para pegar, está en
`prompts.md` en esta misma carpeta. Resumen:

1. **Viral Breakdown Prompt (Notion, gratis)** — Prompt 1 desarma la
   transcripción en: gancho (1–3 s), refuerzo (3–7 s), micro-ganchos,
   entrega de valor, prueba, ritmo, CTA, cierre, fórmula en blanco y por
   qué se hizo viral. Prompt 2 recrea esa fórmula exacta con otro tema:
   3 opciones de gancho, guion completo y notas de producción.
   Fuente: https://www.notion.so/The-Viral-Breakdown-Prompt-3041ff6639588034bb85d09b45fa9be9
2. **Explore Page Blueprint (PromptSigma)** — se le dan 5–10 transcripciones
   del nicho y se extraen los patrones comunes (duración del gancho, CTA,
   estructura, ideas por minuto). Antídoto contra sacar conclusiones de
   un solo video.
3. **Rebuild + style pass (Creative Analytics)** — "Keep the structure, the
   number of reasons, the order and the length of each beat. Replace every
   fact with facts from the product details I give you. Do not add any claim
   that is not in the product details." Aquí "product details" = la hoja de
   datos verificada del tema. Luego el pase de estilo (ritmo, puntuación,
   complejidad de palabras) para que el guion no salga rígido.
4. **Hook → Tension → Payoff (Mustafa Alfredji)** — todo gancho abre un
   loop que el video debe cerrar con MÁS de lo prometido. Si no se puede
   cerrar, es clickbait y no va. Fuente: https://www.mustafaalfredji.com/hooks/

## Flujo gratis, paso a paso (para Shorts de datos de 60–90 s)

0. **Preparar (una vez).** Hoja de fórmulas (ver
   `plantilla-hoja-formulas.md`) y hojas de datos: un documento por tema,
   cada dato con su fuente, escrito ANTES de cualquier prompt de guion.
1. **Buscar outliers (gratis).** 10–15 canales de datos/historia/ciencia/
   animales en ES y en EN. Ordenar por outlier con SortViral o Faceless.so.
   Quedarse solo con videos ≥5× la mediana del canal (mejor 10×),
   publicados en los últimos 90 días, de 45–100 s. Meta: 5–10 por idioma.
   NO elegir por vistas brutas: un video de 2M en un canal de 5M de
   suscriptores puede ser 1×, o sea, nada.
2. **Sacar la transcripción (gratis).** YouTube: panel "Mostrar
   transcripción" del video, o YouTubeToTranscript / Tactiq. TikTok/Reels:
   TransClipper gratis (transcribe el audio). Si el video es solo música o
   texto en pantalla, se descarta: el método necesita palabras habladas.
3. **Verlo una vez con cronómetro (5 min/video).** Anotar lo que la
   transcripción NO muestra: primer frame, texto en pantalla en los
   primeros 3 s, frecuencia de cortes, B-roll, y en qué segundo exacto cae
   el payoff.
4. **Correr el Prompt 1** en ChatGPT/Claude/Gemini (tiers gratis) sobre
   cada transcripción, añadiendo arriba: "Duración del video: [X]s.
   Idioma: español/inglés. Responde en el mismo idioma de la transcripción."
   Guardar la fórmula (sección 9) en la hoja de fórmulas.
5. **Sintetizar una fórmula por idioma (30 min).** Darle los 5–10 desgloses
   al modelo con el prompt de PromptSigma. Quedarse SOLO con patrones que
   aparezcan en al menos 3 de los 5–10 videos; lo demás se descarta.
6. **Generar el guion desde datos verificados.** Primero la hoja de datos,
   luego el Prompt 2 + la restricción de Creative Analytics (no añadir
   ningún dato que no esté en la hoja). Pedir 3 opciones de gancho, guion
   completo al presupuesto de palabras y notas de producción.
7. **Verificación humana + prueba del gancho (15 min).** Cada número,
   nombre y fecha se coteja con la hoja de datos; lo no verificado se corta.
   Leer el gancho en voz alta: si tarda >3 s en decirse o necesita el resto
   de la frase para entenderse, se reescribe. Producir 3 variantes de gancho
   para el mismo guion y probarlas como videos separados (mismo cuerpo,
   distintos primeros 3 s): la variable es el gancho, no el tema.
8. **Medir lo que las herramientas no pueden.** En Studio / TikTok
   Analytics: retención a 3 s y duración media por variante, no solo vistas.
   Un gancho que sube la retención a 3 s pero flojea el payoff es clickbait:
   el payoff debe cerrar el loop. Retirar fórmulas cuyos ganchos dejen de
   funcionar tras 2–3 usos en la misma cuenta.
9. **Repetir cada semana, en tandas.** Una sesión de ~2 h por semana
   (5–10 outliers nuevos) alimenta los guiones de la semana siguiente.

## Esqueleto de 75 s (guía de tiempos; manda la regla CAPCOT de 190–210 palabras)

| Beat | Tiempo (video 75 s) | Palabras | Trabajo |
|---|---|---|---|
| Gancho | 0:00–0:03 | 8–12 | Una afirmación fuerte / corrección / loop abierto. Sin saludo, sin intro, sin "en este video". |
| Refuerzo | 0:03–0:08 | ~15 | Segunda promesa o por qué importa. |
| Contexto mínimo | 0:08–0:18 | ~25 | Solo lo necesario para que el payoff caiga. |
| Cuerpo — beat 1 + re-gancho | 0:18–0:38 | ~45 | Dato 1 + micro-gancho ("pero aquí viene lo raro…"). |
| Cuerpo — beat 2 + re-gancho | 0:38–0:55 | ~40 | Dato 2 / giro que cambia el cuadro. |
| Payoff | 0:55–1:08 | ~25 | Cierra el loop del gancho — tarde, y con MÁS de lo prometido. |
| Cierre / CTA | 1:08–1:15 | ~10 | Una línea: callback al gancho, O un solo CTA suave. Nunca los dos. |

Presupuesto: ~2.4 palabras/s → 60 s ≈ 140–170 palabras, 75 s ≈ 180,
90 s ≈ 210–260. Regla CAPCOT vigente: guion adulto 190–210 palabras.
Re-gancho cada 8–10 s. Cambio visual al menos cada 3 s (corte, zoom,
B-roll, texto en pantalla).

## Reglas CAPCOT que mandan sobre este método

- El gancho es **afirmación, no pregunta**. Así lo dice
  `docs/ESTRATEGIA_GANCHOS_Y_RETENCION.md` (91% de ads ganadores abren
  con algo negativo/declarativo; 82% con afirmación, no pregunta). Y un
  estudio de 2,421 TikToks (ClipSpeed, 2026) encontró que los ganchos de
  pregunta rindieron mal en cuentas de más de 1,000 seguidores: el
  "¿Sabías que…?" queda como UNA variante en prueba, nunca como estilo
  de la casa. Estructuras que sí mapean a datos: curiosidad con payoff
  demorado, mito-corrección, afirmación fuerte + prueba, cold-open de
  historia. La de problema-solución es de ventas y no aplica.
- **Hoja de datos primero, guion después.** Ninguna herramienta verifica
  datos; todas inventan datos plausibles si se les deja. Cada dato con su
  fuente antes del prompt, y verificación humana al final.
- **ES y EN por separado.** No traducir fórmulas palabra por palabra: se
  traduce la ESTRUCTURA ("afirmación fuerte → demora → payoff a 0:50")
  y el gancho se reescribe nativo en cada idioma. Dos hojas de fórmulas.
- **Un solo dato fuerte por escena, con su fuente.** Sin listas.
- **Sin texto dentro de la imagen** (solo título-gancho y subtítulos),
  como manda la skill de cápsula.

## Advertencias (no negociar)

- **Ningún desglose de IA puede probar por qué un video se hizo viral.**
  No ve el timing, quién lo compartió, la audiencia que ya tenía la
  cuenta, ni la suerte. Describe lo visible y puede atribuirle al gancho
  lo que en realidad hizo el tema. Prueba: abrir la misma cuenta y ver
  sus otros videos con ese gancho — si no despegaron, el gancho no era
  la razón. **Una fórmula se confía solo cuando gana en varias cuentas.**
- El puntaje viral 0–100 es diagnóstico de señales observables, no
  pronóstico: ninguna fuente lo validó contra rendimiento futuro.
- La calidad de salida en español de Sandcastles / Virlo / Viral Outliers /
  Runwave no está verificada (se asumen en inglés primero): probar con
  trial antes de pagar si importa el español.
