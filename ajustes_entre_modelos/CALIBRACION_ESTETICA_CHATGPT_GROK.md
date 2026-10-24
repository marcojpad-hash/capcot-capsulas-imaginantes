# Calibración entre modelos: enseñar a ChatGPT la estética visual de CAPCOT

**Fecha:** 2026-10-24  
**Caso de referencia:** cápsula V7 de Grok (`capsula_v7.mp4`)  
**Propósito:** calibrar a ChatGPT para que entienda y aplique correctamente la estética del proyecto en futuras cápsulas.

## Instrucción principal para Grok

La cápsula V7 es una **referencia de trabajo**, no una cápsula acusada de tener fallos. No la clasifiques como defectuosa ni presupongas que sus imágenes, su voz o su montaje incumplen el proyecto. El objetivo es que me expliques cómo debo interpretar la estética definida por CAPCOT y cómo traducirla a instrucciones visuales que yo pueda aplicar correctamente en próximas producciones.

ChatGPT reconoce que no tiene todavía una comprensión suficientemente calibrada de la estética visual que el proyecto pretende conseguir. Necesita que Grok le enseñe esa interpretación, usando la V7 y los documentos del repositorio como contexto, sin convertir diferencias de interpretación en defectos del video.

## Qué necesito que me enseñes

Revisa las instrucciones y plantillas vigentes, en particular:
- `docs/RECETA_CAPSULA.md`
- `docs/ESTRUCTURA_VISUAL_TRENDS.md`
- `scripts/estilos.json`
- `templates/storyboard_vertical.template.json`
- Cualquier referencia visual aprobada o cápsula anterior disponible en el repositorio.

Después, explica de manera concreta y operativa:
1. **Qué significa la estética elegida.** Distingue técnica gráfica, paleta, textura, composición, encuadre, iluminación, nivel de detalle, tono narrativo y continuidad entre planos. No reduzcas la estética a una lista de colores o a una etiqueta como «linograbado».
2. **Cómo se traduce una frase narrada en una imagen.** Explica cómo decidir si una imagen debe representar literalmente un hecho, reconstruir una situación, usar una metáfora visual o establecer contexto. Describe cómo mantener la coherencia sin volver todas las escenas genéricas ni introducir motivos arbitrarios.
3. **Cómo interpretar la V7 como referencia.** Señala qué decisiones visuales de la V7 ilustran bien la estética del proyecto y cuáles me conviene estudiar para comprenderla mejor. Si algo resulta ambiguo, formula una pregunta o indica qué referencia adicional necesitarías; no lo declares un fallo.
4. **Cómo debo escribir prompts.** Da ejemplos concretos de prompts para futuras cápsulas, distinguiendo entre instrucciones formales de estilo y el contenido específico de la escena. Usa una frase real del guion solo si puedes acceder a ella; no inventes frases ni atribuyas a la V7 contenidos que no hayas verificado.
5. **Cómo debe funcionar la continuidad visual.** Explica cómo conservar una identidad reconocible a lo largo de una cápsula y, al mismo tiempo, variar planos, composición y acciones según lo narrado.
6. **Qué ejemplos de referencia faltan.** Si los documentos no bastan para fijar la estética, especifica qué hace falta para calibrarme: fotogramas aprobados, moodboard, cápsulas modelo, ejemplos positivos y negativos, reglas de composición o una descripción editorial más precisa.
7. **Cómo convertir esta explicación en una guía operativa reutilizable.** Propón una regla o lista breve que ChatGPT pueda consultar antes de generar cada imagen. Señala dónde convendría documentarla en el repositorio, pero no afirmes haber modificado archivos del repositorio si no lo has hecho.

## Límites y precisión
- No declares que la V7 tiene fallos. No hagas una auditoría correctiva ni redactes un reporte de defectos.
- No cambies ni critiques la voz: el usuario confirmó que cumple la especificación.
- Separa lo que dicen los documentos, lo que observas en la V7, tu interpretación y las preguntas que sigan abiertas.
- No presentes preferencias subjetivas como requisitos oficiales si no están documentadas.
- No publiques ni alteres el video. No modifiques el motor U6 ni otros proyectos.
- Si no puedes acceder al MP4 o a algún archivo del repositorio desde tu entorno, dilo con claridad y continúa solo con lo que puedas verificar.

## Formato de respuesta solicitado
Escribe una respuesta dirigida directamente a ChatGPT, con este encabezado:

**«ChatGPT: esto es lo que debes entender de la estética de CAPCOT y así debes aplicarla».**

Organiza la respuesta en: (1) principios de la estética; (2) lecciones de la V7 como referencia; (3) método para convertir narración en imágenes; (4) ejemplos de prompts; (5) guía operativa reutilizable para futuras cápsulas; (6) referencias o aclaraciones que faltan.

La respuesta debe enseñarme a trabajar mejor, no detener el trabajo ni limitarse a reconocer el problema. Queremos usar esta calibración para continuar produciendo las siguientes cápsulas.
