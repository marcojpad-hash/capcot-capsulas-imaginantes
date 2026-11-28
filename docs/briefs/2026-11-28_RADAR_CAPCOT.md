# Radar CAPCOT — 28 de noviembre de 2026

**Serie:** Datos y ociosidades  
**Ventana revisada:** slot 23:30 CDMX  
**Estado:** sin candidato autorizado para storyboard. El slot aparece libre en plan_semana y rotación; no se crea storyboard hasta que una fuente primaria, su frescura, el mapa y la verificación DOI/URL sean suficientes.

## Recuperación de tendencias

Los RSS científicos de scripts/tendencias.py y Google Trends RSS México fallaron en el entorno de lectura. Los errores literales y el respaldo HTML oficial están registrados en 2026-11-27_RADAR_CAPCOT.md. La página HTML de Google Trends mostró principalmente clima, deportes y búsquedas generales; no aportó un dato científico verificable.

## Candidatos recientes

### 1. Diversidad de árboles y resiliencia forestal

- **Observación:** Nature Ecology & Evolution muestra un artículo primario publicado el 27-nov-2026, “Tree species diversity shapes forest resilience across current and future climates”.
- **Identificador:** DOI 10.1038/s41559-026-03254-4.
- **Fuente:** https://www.nature.com/articles/s41559-026-03254-4
- **Estado:** PENDING_SOURCE. El registro editorial y la fecha son visibles, pero el PDF de Springer devolvió Internal Error en este entorno; no se extrajeron métodos, claims ni coordenadas de parcelas.
- **Decisión:** no storyboard hasta leer el artículo y confirmar datos espaciales; además, revisar similitud con el candidato de biodiversidad/agricultura del radar anterior.

### 2. Cohesión cromosómica en óvulos envejecidos

- **Observación:** una noticia de Nature identifica un artículo primario de Science publicado el 26-nov-2026 sobre un sistema de cohesión diseñado para reducir errores en óvulos mamíferos envejecidos.
- **Identificador:** DOI 10.1126/science.aei5852.
- **Fuente primaria:** https://www.science.org/doi/10.1126/science.aei5852
- **Estado:** PENDING_SOURCE. La página primaria de Science devolvió 403; la noticia secundaria no sustituye la lectura del paper. No se adoptan cifras ni resultados de la noticia como claims.
- **Decisión:** candidato de tema distinto, pero sin fuente primaria leída ni coordenada contextual válida; no storyboard.

### 3. Estados conformacionales de OXA-48

- **Observación:** Nature Communications lista un artículo primario publicado el 27-nov-2026 sobre subestados conformacionales de una beta-lactamasa OXA-48.
- **Identificador:** DOI 10.1038/s41467-026-78841-x.
- **Fuente:** https://www.nature.com/articles/s41467-026-78841-x
- **Estado:** NO_DUPLICAR. La línea temática de enzimas bacterianas/antimicrobianos se solapa con PAV1 y el proyecto Bacterias de la rotación activa.
- **Decisión:** conservar como candidato observado, no ocupar un slot con un tema redundante.

### 4. Dos grupos humanos arcaicos en el sur de China

- **Observación:** artículo primario de Nature publicado el 25-nov-2026; el PDF completo fue accesible. Informa cuatro dientes de dos cuevas de Guangxi; dos dientes de Longchuandong muestran afinidad denisovana y los de Chuanshandong quedan como Homo arcaico no resuelto. Los autores califican la inferencia evolutiva como preliminar.
- **Identificador:** DOI 10.1038/s41586-026-11341-6.
- **Fuente primaria:** https://www.nature.com/articles/s41586-026-11341-6.pdf
- **Mapa:** la Figura 1 ubica aproximadamente Chuanshandong cerca de 108°E, 20°N y Longchuandong cerca de 110°E, 21°N. Son coordenadas aproximadas leídas del mapa del paper, no GPS exacto de las entradas de las cuevas.
- **Estado:** OUT_OF_WINDOW para 28-nov 23:30: el paper está fechado 25-nov y no puede acreditarse que siga dentro de las 48 horas del slot. Además, PENDING_CROSSREF: api.crossref.org devolvió Internal Error y doi.org no completó una resolución verificable en este entorno.
- **Decisión:** no usar para el dato del día 28; conservar para una ventana posterior si la regla de frescura lo permite y se completa Crossref.

## Separación de evidencia

- **Observación:** fechas, títulos, DOI y accesibilidad indicados arriba proceden de registros editoriales o del PDF primario cuando se especifica.
- **Cálculo:** el paper de Denisovan fechado el 25-nov queda fuera de la ventana de 48 horas para el slot del 28-nov 23:30; el horario exacto de publicación no está disponible, por lo que no se presume elegibilidad.
- **Inferencia:** la diversidad de temas no basta para seleccionar un candidato; la falta de texto primario, coordenadas o DOI verificado impide cerrar las compuertas.
- **Recomendación:** mantener libre el slot 28-nov 23:30. No crear storyboard, no crear cola y no marcar preparado. Revaluar con una fuente primaria publicada dentro de la ventana, claims verificables y coordenadas sustentadas.

## Estado de producción

- Storyboards nuevos: ninguno.
- approved_assets: no aplica; no se creó proyecto.
- Medios, frames, audio, voz, renders y placeholders: no generados.
- Publicación/programación: ninguna.


## Actualización de candidatos — 27-nov-2026 22:37 CDMX

### 5. Primer genoma cromosómico de un tucán

- **Observación primaria:** Scientific Data publicó el 27-nov-2026 un Data Descriptor con el primer ensamblaje de referencia a nivel cromosómico para la familia Ramphastidae. El ensamblaje mide 1.467 Gb; contiene 266 scaffolds, de los cuales 57 son de escala cromosómica (55 autosomas y cromosomas sexuales Z/W). El análisis citogenético confirma 2n=112; BUSCO recupera 99.5% de genes completos. Se anotaron 19,606 genes, incluidos 17,193 codificantes.
- **Fuente primaria:** https://www.nature.com/articles/s41597-026-08658-2
- **DOI:** 10.1038/s41597-026-08658-2.
- **Frescura:** publicado el 27-nov; para el slot 28-nov 23:30, la edad máxima compatible con la fecha editorial es 47.5 h. La hora exacta de publicación no está indicada.
- **Mapa:** el paper informa ocho individuos cautivos y selecciona RT01 para el ensamblaje, pero el texto recuperable no asigna RT01 a una institución ni aporta coordenadas de origen. Los agradecimientos nombran tres zoológicos, sin vincular cada muestra con uno. La Tabla 1 no pudo recuperarse desde la página directa; no se asignan coordenadas ni se usa el rango continental como sustituto del origen de las muestras.
- **DOI/Crossref:** PENDING_CROSSREF. El artículo primario aparece indexado con DOI y fecha; la apertura directa de api.crossref.org/doi.org devolvió Internal Error o no completó la redirección en este entorno.
- **Estado:** candidato observado, no seleccionado; PENDING_MAP + PENDING_CROSSREF.
- **Decisión:** no crear storyboard. Sin asignación verificable de muestra a lugar no existe mapa de investigación defendible, y la compuerta DOI sigue pendiente.

## Reintento de tendencias — 27-nov-2026 22:37 CDMX

- Google Trends HTML oficial para México abrió en ventana de 24 h y mostró 181 tendencias (25 visibles en la página). Las primeras posiciones fueron clima, deportes, entretenimiento, actualidad y búsquedas generales; no apareció una señal científica/natural admisible. No se convirtió popularidad de búsqueda en evidencia científica.
- Google Trends RSS México siguió sin ser accesible mediante el lector. El reintento directo de Nature RSS devolvió literalmente: Failed to fetch https://www.nature.com/nature.rss: (400) Unsupported content-type: application/rss+xml. Los errores previos de los demás feeds permanecen detallados en 2026-11-27_RADAR_CAPCOT.md; no se afirma que los servidores RSS estén caídos globalmente.
- **Recomendación:** mantener libre el slot 28-nov 23:30. Cinco candidatos observados no equivalen a un candidato autorizado; ninguno supera simultáneamente fuente primaria utilizable, mapa sustentado y DOI/Crossref. No storyboard, cola, medios ni programación.


## Verificación complementaria — 27-nov-2026, cierre del día

- La indexación del artículo primario de Scientific Data permitió recuperar más texto de métodos que en el corte anterior. El artículo describe ocho individuos cautivos de Ramphastos toco: RT01 (hembra adulta) se eligió para el ensamblaje; RT02 se usó para tejidos y citogenética; RT03–RT08 aportaron sangre para lecturas cortas. La fuente primaria también confirma que RT01 fue la muestra usada para ONT y Hi-C.
- Los agradecimientos nombran Animalia Park, Bauru Municipal Zoo y Zoo das Aves, pero el texto recuperado no asigna RT01/RT02/RT03–RT08 a una institución concreta. La tabla 1 —que contiene la metadata de especímenes— no quedó accesible. Por tanto, sigue sin existir una coordenada defendible para la muestra del ensamblaje; no se sustituye por una coordenada de zoológico ni por el rango continental de la especie.
- Acceso directo a Nature: Failed to fetch https://www.nature.com/articles/s41597-026-08658-2: (500) Redirected to https://idp.nature.com/authorize?response_type=cookie&client_id=grover&redirect_uri=https://www.nature.com/articles/s41597-026-08658-2 which is not accessible via this tool.
- Crossref REST: URL https://api.crossref.org/works/10.1038%2Fs41597-026-08658-2 is not accessible via this tool. El DOI aparece en la ficha editorial primaria, pero esto no equivale a verificación Crossref.
- Estado sin cambio: PENDING_MAP + PENDING_CROSSREF. El candidato sigue observado, no seleccionado. El slot 2026-11-28 23:30 continúa libre según el último cruce de ocupación; el commit más reciente de main (ec466b5e08bf2d0668a9535fb3ed7fe65c64bda9) solo cambió data/endscreens_rotacion.json, sin modificar proyectos, cola, publicaciones ni programación.
- Decisión: no storyboard, no handoff, no medios. La falta de asignación muestra→institución y de verificación Crossref mantiene cerradas las compuertas.
