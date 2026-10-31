# Propuesta de matriz editorial, publicación y métricas — CAPCOT

Fecha: 2026-10-31  
Estado: **propuesta operativa para revisión; no sustituye la auditoría de Grok Bot ni redefine por sí sola la receta vigente.**

## 1. Decisión de arquitectura

Separar tres dimensiones que no deben confundirse:

1. **Género editorial:** qué tipo de historia contamos.
2. **Público / ocasión:** para quién o en qué contexto de consumo se diseña.
3. **Plantilla de producción:** cómo se narra y representa visualmente.

Una cápsula puede pertenecer a un género y, además, estar adaptada a una audiencia u ocasión. No conviene crear seis pipelines independientes ni seis identidades audiovisuales. Se propone un pipeline común con metadatos que permitan seleccionar guion, ritmo, vocabulario, gancho, duración y recursos visuales según la línea.

## 2. Taxonomía editorial provisional

Los nombres siguientes son una propuesta para ordenar el catálogo, no una afirmación de que las seis líneas históricas ya tuvieran exactamente estos nombres. Grok Bot debe recuperar del historial y de los archivos los nombres y contenidos realmente usados, y mapearlos a esta taxonomía sin borrar sus diferencias.

| ID | Género / línea propuesta | Núcleo narrativo | Audiencia u ocasión | Tratamiento |
|---|---|---|---|---|
| L1 | Dato del día / actualidad científica | Hallazgo, estudio o noticia científica reciente y verificable | Público general | Actualidad, urgencia moderada, fuente primaria y fecha visibles |
| L2 | Ciencia para niñas y niños | Pregunta concreta que se responde con una explicación visual | Infantil y familias | Lenguaje simple, una idea, analogías visuales; rigor idéntico |
| L3 | Ciencia a la hora de comer | Ciencia de alimentos, cocina, sabores, digestión, nutrición y fenómenos cotidianos de la mesa | Consumo en comida / sobremesa | Gancho reconocible, tono ligero; evitar consejo médico o nutricional personalizado |
| L4 | Naturaleza y vida animal | Conductas, adaptaciones, organismos, ecosistemas y relaciones sorprendentes | Público general | Asombro + explicación causal; distinguir observación de hipótesis |
| L5 | Historia de la ciencia y del mundo | Origen de objetos, descubrimientos, personajes, arqueología y episodios históricos | Público general | Relato temporal, lugar/personas, giro documentado |
| L6 | Ciencia del cuerpo y la vida cotidiana | Percepción, memoria, sueño, movimiento, materiales, tecnología y fenómenos cotidianos | Público general | Problema familiar + explicación comprobable |

**Regla de clasificación:** cada cápsula tendrá un género principal y podrá llevar hasta dos etiquetas secundarias. Infantil y hora de comida se registran como audiencia/ocasión además del género; no tienen que convertirse obligatoriamente en géneros temáticos excluyentes. Si la auditoría de Grok demuestra que las seis líneas históricas son otras, conservar los nombres reales y ajustar este mapa.

## 3. Voz y recursos: decisión propuesta

- Mantener la voz sintética estándar del pipeline como base común: `edge-tts / es-MX-JorgeNeural`, con los parámetros de la receta vigente.
- **No integrar la voz personal de Mj como dependencia general.** No aporta ahorro claro frente a TTS automatizado y añade captura, edición, privacidad, consistencia y tiempo de producción.
- Considerar voz propia únicamente como recurso opcional de una plantilla especial o cápsula excepcional, después de una prueba comparativa y con autorización expresa. No debe bloquear ni encarecer la producción diaria.
- El mayor consumo potencial está en generación/edición de imágenes y video, no en reutilizar una pista TTS. Priorizar frames + movimiento de cámara y reservar video generativo para uno o dos planos de alto impacto, si la prueba demuestra mejora suficiente.

## 4. Matriz operativa por cápsula

Cada pieza debe registrar como mínimo:

- `capsule_id`, fecha y hora CDMX de publicación.
- `line_id` (L1–L6, o el ID histórico que valide Grok).
- `genre_primary`, `tags_secondary`, `audience`, `occasion`.
- Tema, subtema y entidad principal.
- Tipo de gancho: pregunta, paradoja, afirmación sorprendente, escena narrativa o comparación.
- Estructura narrativa, duración objetivo y real, palabras del guion.
- Estilo visual, plantilla, voz/motor, música y tipo de montaje.
- Fuente primaria, DOI/URL, fecha del hecho y fecha de publicación.
- Plataforma, ID público, horario, estado de QA y publicación.
- Métricas por ventana: 1 h, 24 h, 72 h y 7 días cuando estén disponibles.
- Vistas, espectadores comprometidos / swipe-away si existe, duración media, porcentaje medio visto, finalización si está disponible, likes, comentarios, compartidos, guardados y suscriptores ganados.
- Coste de generación, minutos de producción y fallos/reintentos, cuando existan.

No mezclar métricas de edades distintas. Una cápsula de 4 horas no se compara directamente con otra de 3 días.

## 5. Métricas y análisis que debe ejecutar Grok Bot

### A. Inventario y trazabilidad
1. Recuperar todas las publicaciones de la ventana histórica disponible y el registro de las últimas siete jornadas.
2. Cruzar `data/publicaciones.json`, storyboards/salidas, `data/rotacion.json`, `data/temas_del_dia.json`, snapshots de YouTube Studio/API, SQLite y cualquier exportación disponible.
3. Resolver cada publicación con su storyboard y asignar tema, género, audiencia, formato, gancho, estilo, duración y hora.
4. Marcar explícitamente campos ausentes. No inferir retención, audiencia o guardados a partir de vistas y likes.

### B. Comparaciones
- Por género y subtema.
- Por horario y día de la semana.
- Por cantidad de publicaciones del día y separación entre ellas.
- Por duración, gancho, estructura, estilo visual y plantilla.
- Por audiencia disponible en Analytics (edad, sexo, geografía), sin inferir datos no proporcionados.
- Por ventana de vida del video (1 h / 24 h / 72 h / 7 d).
- Por rendimiento por hora de producción y por coste, cuando existan datos.

### C. Indicadores
Priorizar:
1. Retención / porcentaje medio visto y duración media.
2. Espectadores que eligieron ver frente a quienes deslizaron, si Analytics lo ofrece.
3. Compartidos y guardados por cada 1.000 vistas.
4. Suscriptores ganados por cada 1.000 vistas.
5. Comentarios por cada 1.000 vistas.
6. Vistas por hora desde publicación y vistas por hora de trabajo/coste.

No declarar un ganador por vistas brutas solamente. Presentar tamaño de muestra, mediana, dispersión y excepciones. Si una línea tiene pocas piezas, etiquetar el resultado como preliminar.

### D. Diagnóstico de frecuencia
Evaluar si publicar varias veces al día aumenta el alcance total sin reducir el rendimiento por pieza. Separar:
- rendimiento individual por cápsula;
- suma diaria del canal;
- rendimiento de la siguiente publicación según el tiempo desde la anterior;
- posibles efectos de día, tema y hora.

No atribuir causalidad a una sola jornada. Usar una prueba escalonada y comparable.

## 6. Prueba operativa inicial (propuesta, no resultado)

Durante los próximos 7–14 días, mantener un máximo inicial de **tres publicaciones al día**, coherente con el límite ya documentado en `scripts/rotacion.py` (dos propias + una externa). No aumentar a seis por intuición.

- Probar 2 y 3 publicaciones en días comparables, con separación suficiente entre horarios.
- Rotar líneas editoriales entre franjas para no confundir tema con horario.
- Mantener constantes, en lo posible, plantilla, calidad de fuente y duración durante cada comparación.
- Registrar hora exacta y snapshots a 1 h, 24 h, 72 h y 7 días.
- Evaluar total diario y mediana por cápsula. Si 3 publicaciones elevan el total diario y no hunden de forma persistente la mediana por pieza, mantener 3. Si no, ajustar horarios o frecuencia.
- No concluir que un día está muerto por una sola jornada; distinguir distribución inicial, respuesta del público y ventana de medición.

Los horarios concretos deben salir del análisis de publicaciones reales y audiencia activa; no fijarlos por intuición antes de la auditoría.

## 7. Limitaciones conocidas del registro actual

En la versión inspeccionada de `scripts/metricas.py`:
- La tabla de cápsulas guarda tema, estilo, gancho y duración.
- La tabla de métricas contempla retención, compartidos, guardados y suscriptores, pero la ruta `vistas` solo inserta vistas, likes y comentarios.
- La ruta `recolectar` todavía contiene un TODO para YouTube Analytics y TikTok.
- Por tanto, el análisis histórico debe indicar qué métricas están efectivamente disponibles y qué campos están vacíos; no presentar la estructura de la base como si ya contuviera datos.

Dato histórico ya registrado fuera de esta auditoría: el 26-oct-2026, los snapshots públicos de YouTube mostraron crecimiento del canal de 5.599 a 10.023 vistas y de 15 a 31 suscriptores entre 08:07 y 20:06 CDMX. Es un dato agregado de canal, no demuestra por sí solo qué formato causó el crecimiento. Se había observado además crecimiento destacado de Pimiento y Papel picado P1 en la franja intermedia; Grok debe reconstruir los snapshots por video y sus edades antes de atribuir rendimiento.

## 8. Entrega requerida de Grok Bot

Grok Bot debe devolver un informe con:
1. Inventario exacto de las seis líneas realmente usadas, con evidencias de archivo/publicación.
2. Mapa de equivalencia entre nombres históricos y taxonomía provisional L1–L6; corregirla si no encaja.
3. Matriz por cápsula con los campos del §4.
4. Ranking por género, subtema, horario, día, audiencia, duración, gancho y plantilla, siempre indicando n y ventana.
5. Análisis de días con varias publicaciones frente a días con menos publicaciones.
6. Horarios recomendados y separación entre publicaciones, respaldados por datos.
7. Recomendación de frecuencia y capacidad de producción sin degradar calidad ni disparar costes.
8. Inventario de métricas faltantes y plan mínimo para recolectarlas automáticamente.
9. Cambios concretos sugeridos a los archivos del repositorio, separados de la auditoría. No editar la receta, límites ni datos históricos hasta presentar hallazgos.

## 9. Límites

- Esta propuesta no publica ni programa cápsulas.
- No modifica el motor U6.
- No integra clonación de voz ni sube muestras de voz personal.
- No gasta créditos de generación.
- No cambia `main`; queda en la rama de trabajo para revisión.
- Los resultados de Grok deben separar dato observado, cálculo, inferencia y recomendación.
