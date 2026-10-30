# Compuerta de continuidad audiovisual — CAPCOT

Estado: política propuesta para el coordinador CAPCOT. No sustituye la receta ni autoriza publicación.

## Objetivo

Cada cápsula debe percibirse como una sola producción con una identidad audiovisual estable. No basta con que todos los planos pertenezcan a una categoría genérica (por ejemplo, "animación 3D" o "ilustración científica"). Se debe conservar la misma dirección artística concreta de principio a fin.

## Biblia audiovisual obligatoria por cápsula

El storyboard debe declarar un bloque `visual_identity` con:

- `style_id`: identificador único de estilo tomado del catálogo CAPCOT.
- `style_name`: nombre exacto del estilo.
- `prompt_base`: prompt base exacto del catálogo, sin reescrituras.
- `palette`: paleta fija y concreta.
- `lighting`: iluminación y dirección de luz.
- `texture`: materialidad, grano y acabado.
- `composition`: reglas de encuadre, escala y profundidad.
- `negative_prompt`: exclusiones explícitas (fotografía, vector, texto dentro de imagen, estilos alternos, etc., según el estilo).
- `reference_assets`: referencias visuales maestras disponibles.
- `seed_policy`: semilla fija o política documentada de continuidad.

También debe declarar `typography_identity`:

- `font_family`, `font_weight`, `title_style`, `subtitle_style`, `hierarchy`, `animation`.
- La tipografía se compone en postproducción; no se delega al generador de imágenes.
- El texto visible se renderiza en español de México. No aceptar glifos aleatorios ni texto generado dentro de imágenes.

Y `voice`:

- Motor: `edge-tts`.
- Voz: `es-MX-JorgeNeural`.
- Idioma: `es-MX`.
- Rate: `+7%`; pitch: `-2Hz`; pad: aproximadamente `0.3` s.
- No sustituir por otra voz o idioma de forma silenciosa. Si falla la voz oficial, detener el montaje de voz y reportar el bloqueo para que el proceso oficial resuelva el respaldo autorizado.

## Reglas de generación

1. Un único `style_id` por cápsula. No mezclar estilos por escena.
2. Cada `image_prompt` comienza con el `prompt_base` exacto del estilo elegido; después añade solo la descripción específica del plano.
3. Todas las imágenes se generan en 9:16 y sin texto integrado.
4. Cada escena usa solo los recursos declarados en el storyboard. No inferir permiso para agregar imágenes por ambigüedad del prompt.
5. Si una escena necesita varios planos, cada recurso debe estar declarado explícitamente en `approved_assets`; no se crean tomas adicionales por iniciativa del proveedor.
6. Reutilizar referencias, seed, personaje, objetos y rasgos visuales cuando aparezcan de nuevo.
7. No cambiar idioma, voz, tipografía, paleta, iluminación o acabado entre escenas.
8. Si un proveedor no puede mantener referencias o continuidad, usarlo solo para planos aislados que puedan igualarse en postproducción; si no se puede igualar, rechazarlo para esa cápsula.
9. Para clips de video cortos, se permite generar por segmentos y ensamblar; cada segmento hereda la misma biblia audiovisual. Se puede continuar desde el último frame o usarlo como referencia.
10. No permitir que una descripción abierta se convierta en collage, montaje de imágenes múltiples o secuencia de estilos no solicitada.

## Compuertas QA

### A. Validación estructural automática
- Existen los tres bloques: `visual_identity`, `typography_identity`, `voice`.
- Idioma `es-MX`, voz `es-MX-JorgeNeural`, rate `+7%`, pitch `-2Hz`.
- Todas las escenas usan el mismo `style_id`.
- Cada prompt comienza exactamente con el prompt base declarado.
- Recursos usados están declarados; no hay nombres de archivo duplicados ni recursos huérfanos.
- Texto de pantalla y narración declaran español de México.
- No hay sustitución silenciosa de voz o idioma.

### B. Comparación visual
- Comparar todos los frames en una hoja de contacto y revisar escenas consecutivas, no solo una muestra.
- Comparar con una referencia maestra de estilo.
- Revisar materialidad, trazos, paleta, luz, encuadre, escala, profundidad, personajes y objetos.
- Rechazar cambios de medio (por ejemplo, papel recortado → fotografía realista), estética o acabado aunque la categoría genérica coincida.
- Revisar OCR para detectar texto accidental o idioma incorrecto dentro de imágenes.

### C. Revisión audiovisual integral
- Escuchar la voz de principio a fin y verificar timbre, idioma, volumen, ritmo y pausas.
- Revisar tipografía, jerarquía, posición, animación y legibilidad en todos los cortes.
- Verificar continuidad entre clips, transiciones, música, ambiente y efectos.
- Confirmar que no se añadieron imágenes, planos, palabras o elementos no autorizados por el storyboard.

## Resultado

Cualquier incumplimiento estructural es error bloqueante. Las diferencias semánticas o estéticas requieren revisión visual/audio humana o un evaluador multimodal con evidencia; un script no puede certificar por sí solo que dos escenas "se sienten iguales".

Esta compuerta no publica ni modifica el estado de una cápsula. Solo informa PASS/FAIL y evidencia.
