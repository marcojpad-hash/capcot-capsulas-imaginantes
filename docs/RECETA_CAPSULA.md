# Receta de cápsula textual — Datos y ociosidades

Esta receta define el guion y storyboard que ChatGPT entrega a Grok. No autoriza generar medios ni publicar.

## Parámetros
- Serie: **Datos y ociosidades**.
- Idioma: español de México (\`es-MX\`).
- Formato vertical 9:16.
- Duración total: 75–90 s, incluidos 6 s de cortinilla.
- Narración: 170–235 palabras.
- Escenas: 7–9.
- Gancho \`titulo\`: máximo seis palabras.
- Cierre hablado exacto: **«Esto fue Datos y ociosidades.»**
- Voz declarada para producción: edge-tts \`es-MX-JorgeNeural\`, rate \`+7%\`, pitch \`-2Hz\`, pad aproximado 0.3 s.

## Contrato narrativo previo

Antes de escribir escenas, completar `narrative_contract` con una sola pregunta central, promesa, stakes, giro científico, límite de evidencia y payoff. No copiar el contrato como explicación dentro del guion; la narración debe sostenerse por sí sola. El revisor en frío no ve este objeto.
Cada escena declara `dramatic_beat`, `scene_function`, `causal_bridge_from_previous`, `question_state`, `reason_to_continue` y `new_information`; estos campos describen la progresión sin sustituir ni reescribir la narración. El investigador no añade `narrative_qa`: lo registra el auditor independiente después de la lectura en frío.

## Arco
1. \`hook_medias_res\`: imagen mental o pregunta concreta.
2. \`desarrollo\`: mecanismo/hallazgo explicado con evidencia.
3. \`cierre_historia\`: qué se demostró y qué no.
4. \`reflexion_o_pregunta\`: conexión final y cierre hablado.

No convertir una hipótesis de los autores en hecho probado.

## Fuentes
Cada fuente incluye \`id\`, \`cita_corta\`, \`url\`, DOI si existe, fecha de publicación/consulta, afirmaciones respaldadas y \`verification_status\`. Priorizar el artículo original; contrastar comunicados oficiales. Cada escena lleva \`source_ids\`. DOI pendiente no se etiqueta como verificado.

## Capas y continuidad
Incluir mapa con coordenadas reales, fuente cartográfica y nota de precisión; declarar exactamente qué representa el pin. Incluir dato/gráfico con valor, unidad, fuente y límites de interpretación. Cada escena incluye \`visual_description\`, \`image_prompt\`, \`ambiente\`, \`sfx\` y \`source_ids\`.

Un solo \`style_id\` para toda la cápsula. Cada \`image_prompt\` comienza con el \`prompt_base\` literal de \`scripts/estilos.json\`. Declarar paleta, luz, textura, composición, exclusiones y continuidad. La tipografía se añade en postproducción.

## Audio
El storyboard declara intención sonora, no archivos. Cada escena tiene ambiente y SFX; el silencio se expresa explícitamente. La música puede quedar como plan para Grok. No adjuntar audio.

## QA narrativo previo al handoff
Aplicar obligatoriamente `docs/QA_NARRATIVO_EN_FRIO.md`: un revisor distinto del redactor oculta título, resumen, arco y notas y lee solo la narración concatenada. Registra siete checks, score y flags. Solo PASS (>=85, siete checks true, flags vacíos) permite entrar a `cola/entrada/`. Sin revisión independiente, FAIL. El validador estructural no sustituye esta lectura.

## Validación
7–9 escenas; 170–235 palabras; 75–90 s con cortinilla; gancho ≤6 palabras; `narrative_contract` completo; arco completo; cierre exacto; voz correcta; mapa y dato/gráfico con fuente; source_ids válidos; estilo y prompt_base exactos; sin rutas de assets; publicación pendiente de Grok; `narrative_qa` PASS.

Plantilla: \`templates/storyboard_vertical.template.json\`. Validador: \`scripts/validar_storyboard.py\`.
