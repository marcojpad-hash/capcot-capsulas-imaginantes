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

## Validación
7–9 escenas; 170–235 palabras; 75–90 s con cortinilla; gancho ≤6 palabras; arco completo; cierre exacto; voz correcta; mapa y dato/gráfico con fuente; source_ids válidos; estilo y prompt_base exactos; sin rutas de assets; publicación pendiente de Grok.

Plantilla: \`templates/storyboard_vertical.template.json\`. Validador: \`scripts/validar_storyboard.py\`.
