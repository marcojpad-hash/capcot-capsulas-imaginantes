# Radar CAPCOT — 28 de noviembre de 2026

**Serie:** Datos y ociosidades  
**Ventana revisada:** slot 23:30 CDMX  
**Estado:** borrador de investigación creado en proyectos para el slot libre 23:30 CDMX; no apto para promoción hasta completar DOI/Crossref, validador estructural y QA narrativo independiente.

## Recuperación de tendencias

Los RSS científicos de scripts/tendencias.py y Google Trends RSS México fallaron en el lector de esta ejecución. El respaldo HTML oficial de Google Trends sí mostró 254 tendencias; “agujero de la capa de ozono” apareció con 2K+ búsquedas y actividad de hace 13 h. Es una señal secundaria, no evidencia científica. La fuente ESA asociada está fechada 26-nov sin hora verificable; no se puede garantizar que siga dentro de 48 h para el slot 28-nov 23:30, por lo que no se selecciona.

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

### 4. Partículas de desgaste de neumáticos oscurecen la criosfera

- **Observación:** artículo primario de Nature Climate Change publicado el 27-nov-2026. El texto indexado de la página de Nature expone el resumen, las figuras globales 1–3 y la disponibilidad de datos. El estudio combina mediciones ópticas de partículas individuales, cálculos de transferencia radiativa en nieve y simulaciones globales del sistema terrestre.
- **Resultados reportados:** a 550 nm, las partículas absorben aproximadamente la mitad de la radiación por unidad de masa que el carbono negro; el modelo estima 1.22 ± 0.91 ng/g de concentración media anual en la criosfera, reducción de albedo de 0.16 ± 0.12%, forzamiento radiativo de 0.015 ± 0.012 W/m² (~17.4% del carbono negro) y aceleración de fusión de 0.19 ± 0.14 mm de equivalente de agua por día.
- **Identificador:** DOI 10.1038/s41558-026-02800-z.
- **Datos primarios:** Zenodo, registro 23299235, publicado 11-oct-2026; contiene source data de figuras 1–3, tablas y código. URL del registro accesible: https://zenodo.org/records/23299235.
- **Frescura:** publicado 27-nov-2026; para el slot 28-nov 23:30, la edad máxima compatible con la fecha editorial es 47.5 h.
- **DOI/Crossref:** PENDING_CROSSREF. La apertura directa de Nature devolvió HTTP 500 con redirección a idp.nature.com; api.crossref.org y doi.org no fueron accesibles en este entorno. El artículo primario sí quedó recuperado desde el índice de Nature, pero no se atribuye verificación Crossref.
- **Mapa:** las figuras 2–3 presentan distribución global modelada de emisiones, transporte, depósito y efectos en la criosfera. Se usa únicamente la extensión cartográfica global [-90,-180,90,180], sin pines ni puntos de muestreo inventados.
- **Estado:** candidato seleccionado para borrador textual en proyectos/2026-11-28_llantas-hielo-albedo/storyboard.json; no apto para promoción hasta completar DOI/Crossref, validador estructural y QA narrativo independiente.
- **Decisión:** desarrollar solo el borrador en proyectos; no crear cola, medios ni handoff.

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


## Reintento RSS y Trends — 27-nov-2026, cierre del día

- Se inspeccionó scripts/tendencias.py y se intentó abrir cada URL FEEDS_CIENCIA y el RSS de Google Trends México. Errores literales del lector web:
- ScienceDaily ciencia, salud y espacio: HTTP 400, Unsupported content-type: application/xml.
- Phys.org: HTTP 400, Unsupported content-type: text/xml.
- NASA: HTTP 400, Unsupported content-type: application/rss+xml.
- ESA: HTTP 404, Not Found.
- Nature: HTTP 400, Unsupported content-type: application/rss+xml.
- EurekAlert: URL no accesible mediante esta herramienta.
- SINC: URL no accesible mediante esta herramienta.
- UNAM Global: HTTP 400, Unsupported content-type: application/rss+xml.
- Google Trends RSS (geo=MX): URL no accesible mediante esta herramienta.
- Respaldo oficial: https://trends.google.com/trending?hl=es-MX; el índice devolvió 254 tendencias y “agujero de la capa de ozono” con 2K+ búsquedas, activo desde hace 13 h. La tendencia no acredita la hora de publicación de la nota ESA del 26-nov.
- La ejecución local de scripts/tendencias.py no pudo realizarse porque el intento de sparse clone falló: Could not resolve host: github.com. No se atribuye una corrida del script.

## Backlog fuera de la ventana del slot

- Dos grupos humanos arcaicos en el sur de China, DOI 10.1038/s41586-026-11341-6, publicado 25-nov-2026. Se conserva como backlog, no como candidato del slot 28-nov 23:30: no puede acreditarse frescura ≤48 h; Crossref sigue pendiente y las coordenadas de la figura son aproximadas, no GPS de las cuevas.

## Revalidación final del slot 28-nov-2026 23:30

- La programación/main sigue sin ocupar ese slot; el último commit de main revisado solo cambió data/endscreens_rotacion.json.
- Borrador textual creado: 2026-11-28_llantas-hielo-albedo/storyboard.json. Siete escenas, 225 palabras de narración, 78 s de escenas + 6 s de cortinilla = 84 s; estilo stencil_banksy, sin assets.
- Estado: BORRADOR_EN_PROYECTOS_NO_APTO_PARA_PROMOCION. DOI del artículo PENDING_CROSSREF; validador estructural real no ejecutado por fallo DNS; narrative_qa ausente por separación de funciones. No se creó cola ni se disparó workflow.
- Storyboard commit verificado: fea121c6ef2412f4385ef92f83cdb796c55ce9c6; lectura de vuelta confirma 7 escenas, 225 palabras, 84 s totales, approved_assets=[], render NOT_GENERATED y ausencia de narrative_qa.


## Verificación de handoff del borrador 2026-11-28_llantas-hielo-albedo

- cola/estado/2026-11-28_llantas-hielo-albedo.json: HTTP 404 (GitHub Contents API, NOT_FOUND). Estado operativo registrado: RECEPCION_GROK_NO_CONFIRMADA. No se creó ni editó estado Grok.
- Clasificación: NOT_DISPATCHABLE. Evidencia: el único archivo del proyecto está en proyectos/2026-11-28_llantas-hielo-albedo/storyboard.json; cola/entrada contiene .gitkeep y el directorio anidado 2026-11-09_dato-robot-ensambla-orbita, sin archivo plano 2026-11-28_llantas-hielo-albedo.json. El workflow solo selecciona JSON planos de primer nivel.
- cola/bloqueados no contiene este project_id; salidas no contiene este project_id; el directorio publicaciones/ devuelve 404 y data/publicaciones.json en main no contiene el proyecto. No hay procesamiento/publicación previa detectada para este borrador.
- No hay medios referenciados: approved_assets=[] y export.render_status=NOT_GENERATED; MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO no aplica porque no se declara ningún medio.
- No se promueve ni se crea cola/entrada. El borrador queda exclusivamente en proyectos hasta resolver DOI, validador estructural y QA narrativo independiente.


## Actions automáticas — CodeQL no sustituye las compuertas editoriales

- El análisis CodeQL automático del commit del storyboard terminó SUCCESS (run 46115595793; jobs Analyze actions/python). Los runs 46115611009 y 46115666229 de commits posteriores de documentación seguían in_progress al último chequeo.
- CodeQL no ejecuta validar_storyboard.py ni --check-doi; el estado del borrador no cambia. No hubo dispatch Grok ni handoff.