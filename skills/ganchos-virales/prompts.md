# Prompts de desglose viral — listos para pegar

Fuentes: Notion "The Viral Breakdown Prompt"
(https://www.notion.so/The-Viral-Breakdown-Prompt-3041ff6639588034bb85d09b45fa9be9),
PromptSigma Explore Page Blueprint
(https://promptsigma.com/explore-page-blueprint-ai-reverse-engineer-viral-trends.html),
Creative Analytics
(https://www.creativeanalytics.cc/blog/reverse-engineer-winning-ads),
Mustafa Alfredji Hook Framework (https://www.mustafaalfredji.com/hooks/).

Regla de idioma: el desglose se corre EN EL IDIOMA DE LA TRANSCRIPCIÓN.
No se genera en inglés y se traduce: el gancho pierde ritmo y juego de
palabras. Abajo van la versión en inglés (original publicada) y la versión
en español para trabajar videos ES.

## Prompt 1 — Desarmar (Notion)

Inglés (original):

> You are a viral content strategist and script analyst. I'm going to upload
> a transcript of a viral video. Your job is to reverse-engineer the exact
> formula that made it work.
>
> Video duration: [X]s. Language: English. Respond in English.
>
> Break the transcript down, in order of appearance, into:
> 1. HOOK (first 1–3s) — exact hook type (pattern interrupt, bold claim,
>    curiosity gap, controversy, "Did you know", challenge, visual hook
>    cue), why it stops the scroll, emotion triggered (curiosity, FOMO,
>    shock, desire).
> 2. HOOK REINFORCEMENT (seconds 3–7) — secondary promise, stakes raise,
>    credibility drop.
> 3. MICRO-HOOKS — every retention loop ("but here's the thing", "it gets
>    better", "wait", "the crazy part is", "most people don't know this"),
>    its position, what it does (resets attention, builds anticipation,
>    creates open loop).
> 4. VALUE DELIVERY — core value type, structure (story-based,
>    step-by-step, problem-solution, myth-busting, comparison),
>    front/middle/end-loaded.
> 5. PROOF/CREDIBILITY — direct (stats, results) or indirect (specificity,
>    confidence).
> 6. PACING & ENERGY — shifts, speed-ups, pauses, emphasis.
> 7. CTA — what, where, soft/hard, direct/embedded, secondary CTA.
> 8. CLOSING/SIGNATURE — sign-off, share/save-ability.
> 9. OVERALL FORMULA as a fill-in-the-blank template, e.g.
>    [Hook Type] → [Reinforcement] → [Value Structure] → [Micro-hook] →
>    [More Value] → [Proof] → [CTA] → [Close].
> 10. WHY IT WENT VIRAL in 2–3 sentences.
>
> [pegar la transcripción]

Español (para videos ES):

> Eres un estratega de contenido viral y analista de guiones. Te voy a pasar
> la transcripción de un video viral. Tu trabajo es desarmar la fórmula
> exacta que lo hizo funcionar.
>
> Duración del video: [X]s. Idioma: español. Responde en español.
>
> Desglosa la transcripción, en orden de aparición, en:
> 1. GANCHO (primeros 1–3 s) — tipo exacto de gancho (interrupción de
>    patrón, afirmación fuerte, hueco de curiosidad, controversia, "¿Sabías
>    que…?", reto, gancho visual), por qué frena el scroll, emoción que
>    dispara (curiosidad, FOMO, shock, deseo).
> 2. REFUERZO DEL GANCHO (segundos 3–7) — promesa secundaria, subida de
>    apuesta, dato de credibilidad.
> 3. MICRO-GANCHOS — cada loop de retención ("pero aquí viene lo raro",
>    "espera", "lo loco es que", "casi nadie sabe esto"), su posición,
>    qué hace (resetea la atención, crea anticipación, abre un loop).
> 4. ENTREGA DE VALOR — tipo de valor central, estructura (historia,
>    paso a paso, problema-solución, mito-corrección, comparación),
>    cargada al inicio/medio/final.
> 5. PRUEBA/CREDIBILIDAD — directa (datos, resultados) o indirecta
>    (especificidad, seguridad).
> 6. RITMO Y ENERGÍA — cambios, aceleraciones, pausas, énfasis.
> 7. CTA — qué, dónde, suave/fuerte, directo/integrado, CTA secundario.
> 8. CIERRE/FIRMA — despedida, qué tan compartible/guardable es.
> 9. FÓRMULA GENERAL como plantilla para rellenar, p. ej.
>    [Tipo de gancho] → [Refuerzo] → [Estructura de valor] →
>    [Micro-gancho] → [Más valor] → [Prueba] → [CTA] → [Cierre].
> 10. POR QUÉ SE HIZO VIRAL en 2–3 frases.
>
> [pegar la transcripción]

## Prompt 2 — Recrear (Notion)

Pegar el desglose del Prompt 1 + nicho, audiencia, tono, plataforma, y pedir:

> Dame 3 opciones de gancho del mismo tipo que el original; la línea de
> refuerzo; el guion completo palabra por palabra siguiendo la fórmula
> exacta (micro-ganchos en los mismos puntos estructurales, misma
> estructura de valor, prueba equivalente, mismo CTA, cierre fuerte);
> notas de producción (ritmo, B-roll / visuales que repliquen la
> estrategia de retención, duración estimada); y 3 ideas más de temas del
> nicho que encajen en la misma fórmula, cada una con su gancho.
>
> El guion debe sentirse completamente original y auténtico, no una copia.
> Mismos huesos, otra piel.
>
> EN: "The script should feel completely original and authentic to the new
> creator not like a copy. Same bones, different skin."

Añadir SIEMPRE la restricción de Creative Analytics (adaptada a datos):

> Reemplaza cada dato con datos de la hoja de datos que te doy. No añadas
> ningún dato que no esté en la hoja de datos.
>
> EN (original): "Replace every fact with facts from the product details I
> give you. Do not add any claim that is not in the product details."

Y si el borrador sale rígido, el pase de estilo:

> Eres un experto forense de estilo. Analiza el guion original en ritmo de
> frases, densidad de puntuación y complejidad media de palabras. Luego
> reescribe el guion nuevo para que iguale las tres.
>
> EN (original): "You are a stylistic forensic expert. Analyze the original
> script for sentence rhythm, punctuation density and average word
> complexity. Then rewrite the new script so it matches all three."

## Síntesis multi-video (PromptSigma)

Darle al modelo las transcripciones de 5–10 videos virales del nicho y pedir:

> ACTÚA como analista de contenido viral. Te di las transcripciones de 10
> videos actualmente virales en el nicho de [tu nicho]. Analiza estos
> guiones e identifica: 1) la duración promedio del gancho inicial (en
> segundos), 2) el tipo de CTA más usado, 3) la estructura narrativa más
> común, 4) el número promedio de ideas distintas en un segmento de
> 60 segundos.
>
> Luego genera tres plantillas distintas de gancho de 5 segundos
> (afirmación impactante / número concreto / pregunta contraria, cada una
> con frase de apertura + indicación visual), una plantilla de ritmo/tensión
> por segmentos con objetivo emocional y duración por segmento, y aplícala
> a un tema nuevo.
