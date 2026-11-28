# Radar CAPCOT — 28 de noviembre de 2026

**Serie:** Datos y ociosidades  
**Ventana revisada:** slot 23:30 CDMX  
**Estado actual:** storyboard textual en `proyectos/2026-11-28_llantas-hielo-albedo/storyboard.json` (7 escenas, 229 palabras, 84 s); QA PASS/90 y fuentes registradas como `VERIFICADO_CROSSREF` / `VERIFICADO_RESOLVEDOR`. **NOT_DISPATCHABLE** por conflicto con la reserva y producción preexistente de Tama en main; además, el validador estructural real no se ejecutó y el estado Grok devuelve 404.

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
- **DOI/Crossref:** SRC-001 figura `VERIFICADO_CROSSREF` en el storyboard vigente (commit `329fd501c48d3ac61f681212701fa6c50d209f0c`); SRC-002 figura `VERIFICADO_RESOLVEDOR`. No se ejecutó de nuevo `scripts/validar_storyboard.py --check-doi` en este corte.
- **Mapa:** las figuras 2–3 presentan distribución global modelada de emisiones, transporte, depósito y efectos en la criosfera. Se usa únicamente la extensión cartográfica global [-90,-180,90,180], sin pines ni puntos de muestreo inventados.
- **Estado:** borrador textual existente en proyectos/2026-11-28_llantas-hielo-albedo/storyboard.json; QA narrativo PASS/90 y fuentes con estados verificados en el JSON. No apto para handoff: el validador estructural real no se ejecutó y el mismo slot está reservado en main por Tama con render preexistente.
- **Decisión:** desarrollar solo el borrador en proyectos; no crear cola, medios ni handoff.

## Separación de evidencia

- **Observación:** fechas, títulos, DOI y accesibilidad indicados arriba proceden de registros editoriales o del PDF primario cuando se especifica.
- **Cálculo:** el paper de Denisovan fechado el 25-nov queda fuera de la ventana de 48 horas para el slot del 28-nov 23:30; el horario exacto de publicación no está disponible, por lo que no se presume elegibilidad.
- **Inferencia:** la diversidad de temas no basta para seleccionar un candidato; la falta de texto primario, coordenadas o DOI verificado impide cerrar las compuertas.
- **Recomendación:** no crear otro storyboard ni cola. Llantas ocupa el slot 28-nov 23:30 en esta rama y main también lo reserva para Tama; resolver el conflicto corresponde al operador del calendario, no al investigador. No redispatchar ninguna de las dos piezas.

## Estado de producción — lectura de vuelta 28-nov-2026 06:03 CDMX

- Storyboard textual: 1, `proyectos/2026-11-28_llantas-hielo-albedo/storyboard.json`; 7 escenas, 229 palabras, 78 s de escenas + 6 s de cortinilla = 84 s.
- QA narrativo: PASS/90 válido; la narración no cambió desde esa revisión.
- DOI `10.1038/s41558-026-02800-z`: `VERIFICADO_CROSSREF`; Zenodo `10.5281/zenodo.23299235`: `VERIFICADO_RESOLVEDOR`.
- `approved_assets=[]`; `export.render_status=NOT_GENERATED`; no se generaron medios, frames, imágenes, voz, audio, video, renders ni placeholders.
- `publicacion.status=PENDIENTE_DECISION_GROK`; sin JSON plano en `cola/entrada/`, sin estado Grok individual y sin promoción. El validador estructural real sigue pendiente.


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

## Actualización de auditoría — 2026-11-28

- Google Trends HTML oficial (México, últimas 24 h): 254 tendencias indexadas; «agujero de la capa de ozono» aparece con 2K+ búsquedas y actividad reciente. La mayoría del listado está dominada por deportes, clima y consultas generales; no se incorpora otro tema sin fuente científica primaria reciente. <https://trends.google.com/trending?geo=MX&hl=es>
- Los endpoints RSS se intentaron consultar desde el lector web, pero este no procesa sus respuestas XML: ScienceDaily devolvió 400 Unsupported content-type: application/xml; Phys.org 400 text/xml; NASA, Nature y UNAM 400 application/rss+xml; ESA 404; Google Trends RSS, EurekAlert y SINC no fueron accesibles mediante esta herramienta. Esto no demuestra por sí solo que urllib/feedparser falle. La ejecución local de tendencias.py no se realizó: curl a raw.githubusercontent.com devolvió «Could not resolve host: raw.githubusercontent.com».
- El registro Zenodo 23299235 está accesible y expone el DOI 10.5281/zenodo.23299235. El artículo primario de Nature Climate Change aparece indexado con DOI 10.1038/s41558-026-02800-z y publicación del 27-nov-2026; Crossref API y doi.org no fueron accesibles en esta ejecución, por lo que SRC-001 continúa PENDING_CROSSREF. No se declara verificación DOI.
- Revisión narrativa independiente posterior, leyendo solo la narración concatenada: PASS, score 90/100, siete checks true, critical_flags vacías. El registro quedó en narrative_qa; la narración y sus claims no se modificaron.
- Inspección estructural estática: 225 palabras, 7 escenas, 78 s de escenas + 6 s de cortinilla = 84 s; voz, prompt_base, mapa con bounds globales, capa de dato, fuentes por escena, ambiente/SFX, approved_assets=[] y export NOT_GENERATED presentes; no se encontraron rutas ni nombres de assets. Esto NO sustituye ejecutar scripts/validar_storyboard.py.
- El workflow de validación disponible ejecutó solo el proyecto Kuroshio (run 46078959750) y no incluye --check-doi; no valida este storyboard. El validador real para llantas y la compuerta Crossref quedan pendientes.
- El slot 2026-11-28 23:30 no está libre en main: `proyectos/2026-11-23_animal-tama/metadata.json` reserva ese hueco y `render.log` registra producción de 85.11 s. El borrador sigue en proyectos; cola/estado devuelve 404, no existe entrada plana y no se crea handoff. Clasificación: NOT_DISPATCHABLE.
- Estado final del borrador: QA narrativo PASS; estructura formal y DOI todavía no verificados por sus compuertas independientes; sin promoción, sin medios y sin publicación.



## Verificación DOI independiente — 2026-11-28 04:11 CDMX

- **SRC-001 — artículo primario:** `VERIFICADO_CROSSREF`. La consulta REST de Crossref a `https://api.crossref.org/works/10.1038/s41558-026-02800-z` devolvió `status=ok`, tipo `journal-article`, título coincidente y `published-online=2026-11-27`; el DOI y el editor Springer Nature coinciden con la ficha.
- **SRC-002 — dataset:** `VERIFICADO_RESOLVEDOR`. `https://doi.org/10.5281/zenodo.23299235` resolvió al registro Zenodo 23299235, publicado el 11-oct-2026. La consulta de metadatos Crossref para este DOI no devolvió un registro utilizable en esta comprobación; por eso se conserva el nivel de verificación por resolvedor, no Crossref.
- Se actualizaron únicamente los campos `verification_status` de ambas fuentes en el storyboard. Narración, claims, cifras y QA no cambiaron.
- La inspección estática que replica las comprobaciones estructurales del validador encontró cero errores: 225 palabras según la expresión del script, 7 escenas, 78 s de escenas + 6 s de cortinilla = 84 s, cuatro arcos, voz, prompt_base, mapa con bounds válidos, capa de dato, source_ids, assets vacíos y render NOT_GENERATED. **No equivale a ejecutar** `scripts/validar_storyboard.py`; esa ejecución sigue pendiente por fallo DNS del entorno local.
- La verificación DOI independiente ya está resuelta; la compuerta estructural real sigue pendiente. No se promueve el paquete ni se crea entrada de cola.


## Revalidación RSS, tendencias y Crossref — 2026-11-28 04:11 CDMX

### Cinco candidatos recientes: DOI verificados

Las cinco referencias primarias del radar quedaron contrastadas contra Crossref REST. Los metadatos devueltos coinciden con DOI y título; las fechas primarias se encuentran entre el 26 y el 27 de noviembre:

1. **Bosques y resiliencia:** `10.1038/s41559-026-03254-4`, `published-online=2026-11-27`, Nature Ecology & Evolution. Artículo primario accesible; 0.7 millones de parcelas, asociación positiva en 51.5% de bosques y negativa en 48.5%. La relación no es universal; conservar la diferencia entre asociación observada y proyección de escenarios.
2. **Cohesión cromosómica en óvulos envejecidos:** `10.1126/science.aei5852`, `published-print=2026-11-26`, Science. Artículo primario accesible; el sistema artificial reduce PSSC en óvulos de ratón envejecidos y se adaptó como prueba de principio a cromosomas humanos. No presentarlo como tratamiento clínico.
3. **Evolución funcional de OXA-48:** `10.1038/s41467-026-78841-x`, `published-online=2026-11-27`, Nature Communications. Artículo primario accesible; el resultado central es un intercambio funcional entre subestados catalíticos. Mantener pendiente la decisión editorial por proximidad temática con cápsulas antimicrobianas previas.
4. **Partículas de llantas y criósfera:** `10.1038/s41558-026-02800-z`, `published-online=2026-11-27`, Nature Climate Change. DOI Crossref verificado; dataset `10.5281/zenodo.23299235` verificado por resolvedor a Zenodo. Es el candidato desarrollado para 28-nov 23:30.
5. **Genoma del tucán toco:** `10.1038/s41597-026-08658-2`, `published-online=2026-11-27`, Scientific Data. Artículo primario accesible; ensamblaje cromosómico de 1.47 Gb, 57 scaffolds cromosómicos y BUSCO 99.5%. Sigue `PENDING_MAP`: la ficha no vincula de forma inequívoca el individuo usado para el ensamblaje con una procedencia cartografiable.

La verificación DOI no sustituye la lectura completa de métodos ni resuelve las compuertas editoriales o cartográficas pendientes.

### Reintento de feeds y descarte de falsos recientes

- Consulta alternativa de RSS mediante Exa: ScienceDaily ciencia/salud/espacio, Phys.org, NASA y UNAM Global devolvieron contenido. UNAM Global no aportó un ítem reciente; el feed visible estaba desactualizado.
- Errores exactos de la alternativa: Nature RSS `CRAWL_UNEXPECTED_CONTENT_TYPE`; ESA RSS `CRAWL_NOT_FOUND`; EurekAlert RSS `CRAWL_NOT_FOUND`; SINC RSS `CRAWL_NOT_FOUND`; Google Trends RSS `CRAWL_UNEXPECTED_CONTENT_TYPE`.
- El script `scripts/tendencias.py` no se ejecutó en este entorno: la alternativa local de red falló con `Temporary failure in name resolution`. No se atribuye a ese script el resultado de Exa.
- Tres titulares recientes resultaron ser reanuncios de trabajos primarios antiguos: narval (`10.1038/s41467-026-75689-z`, artículo primario publicado 18-ago-2026), PVC a lubricante (`10.1038/s41586-026-10867-z`, artículo primario publicado 05-ago-2026) y jet de 3C 279 (`10.1051/0004-6361/202660360`, publicado en septiembre de 2026). No califican como investigación nueva para el dato del día.
- El artículo de tiempo de pantalla se publicó el 26-nov y queda fuera de la ventana de 48 h para 28-nov 23:30; el prototipo smartJAN se apoya en un artículo de 2025; el cometa de Euclid se publicó el 25-nov y también queda fuera de esa ventana.
- Respaldo oficial de Google Trends HTML, México, últimas 24 h: 173 tendencias; la primera página no mostró una tendencia científica. `epicentro temblor hoy` apareció con 5 mil+ búsquedas y 13 h, pero no se usó como afirmación científica ni como noticia de sismo sin fuente oficial.

No se abrió un nuevo storyboard: el slot de 28-nov 23:30 ya está ocupado por el borrador de llantas y los slots de 29-nov y 30-nov se encontraron reservados en main o fuera de rotación preferente.


## Estado vigente — 2026-11-28 04:11 CDMX

- Cinco candidatos del radar con DOI Crossref verificado; el candidato de llantas está desarrollado en `proyectos/2026-11-28_llantas-hielo-albedo/storyboard.json` con narrative_qa PASS90 y SRC-001/SRC-002 verificados por Crossref/resolvedor.
- La compuerta estructural Python real sigue pendiente. El espejo estático no la sustituye.
- El respaldo HTML oficial de Google Trends más reciente mostró 173 tendencias sin señal científica en la primera página; el snapshot anterior de 254 tendencias queda como histórico.
- Los titulares recientes de narval, PVC y EHT son reanuncios de papers primarios de agosto/septiembre; no son candidatos nuevos de 48 h. Los demás feeds fallidos y la no ejecución local de `scripts/tendencias.py` están documentados más abajo.
- No se crea un segundo storyboard: el 28-nov 23:30 ya está reservado por Llantas; 29-nov tiene slots ocupados en main y 30-nov 23:30 está reservado por Cher Ami.


## Radar complementario — candidatos publicados el 28-nov para ventanas posteriores

Corte de investigación: 2026-11-28 04:40 CDMX. Los cinco registros siguientes son artículos primarios con DOI contrastado contra Crossref REST. Se separa el dato observado de la interpretación y de los requisitos pendientes para un storyboard.

1. **Elefantes africanos juveniles huérfanos — SELECCIONADO COMO BORRADOR PARA 2026-12-01 07:00.** Oduor et al., *Scientific Reports*, first online 28-nov-2026, DOI [10.1038/s41598-026-81354-8](https://doi.org/10.1038/s41598-026-81354-8). El estudio compara metabolitos fecales de glucocorticoides y triyodotironina tres años después de la liberación gradual; las concentraciones entre huérfanos y controles fueron comparables, mientras que vínculos sociales más fuertes se asociaron con menor fGCM y mayor fT3. **Límite:** early access, una conservancy y asociaciones observacionales; no prueba causalidad. Sitio geográfico respaldado por SRC-002. [Fuente primaria](https://www.nature.com/articles/s41598-026-81354-8).

2. **Haloxylon ammodendron en el desierto de Badain Jaran.** *Scientific Reports*, 28-nov-2026, DOI [10.1038/s41598-026-82098-1](https://doi.org/10.1038/s41598-026-82098-1). Tres censos (2015, 2020 y 2025) describen cambios en diámetro basal y estructura de tamaños; la frecuencia estandarizada cae marcadamente entre clases de tamaño, sin que eso equivalga a una caída idéntica de toda la población. **Pendiente:** extraer del artículo los límites cartográficos exactos y revisar la definición de las clases antes de desarrollar. [Fuente primaria](https://www.nature.com/articles/s41598-026-82098-1).

3. **Muestreo de estomas para reconstruir CO₂ antiguo.** *Scientific Reports*, 28-nov-2026, DOI [10.1038/s41598-026-82302-2](https://doi.org/10.1038/s41598-026-82302-2). El artículo propone un estándar de muestreo; el conteo manual resulta más preciso que el automatizado en el material evaluado y considerar la variación espacial dentro de la hoja reduce errores de reconstrucción de pCO₂ hasta 16%. **Pendiente:** verificar coordenadas de las localidades fósiles y contextualizar el porcentaje sin presentarlo como mejora universal. [Fuente primaria](https://www.nature.com/articles/s41598-026-82302-2).

4. **Ciclo de molibdeno y otros metales traza en sedimentos del Pacífico.** *Communications Earth & Environment*, 28-nov-2026, DOI [10.1038/s43247-026-04210-7](https://doi.org/10.1038/s43247-026-04210-7). En los primeros cinco metros de sedimento de dos áreas de contrato de la Zona Clarion-Clipperton, el Mo alcanza alrededor de 250 nmol/kg en un área BGR y rara vez supera 100 nmol/kg en el área GSR. **Pendiente:** leer la figura de estaciones y sus coordenadas; no atribuir la diferencia solo al estado redox. [Fuente primaria](https://www.nature.com/articles/s43247-026-04210-7).

5. **Desarrollo minero y PM₂.₅ regional.** *Scientific Reports*, 28-nov-2026, DOI [10.1038/s41598-026-81164-y](https://doi.org/10.1038/s41598-026-81164-y). El análisis cubre más de 35,000 sitios mineros en 119 países; estima descensos locales de PM₂.₅ de hasta 4.4% dentro de 100 km en el promedio, pero aumentos en países de ingreso medio-alto. **Límite:** el desarrollo minero se aproxima con pérdida forestal y el resultado varía por nivel de ingreso; no resumirlo como “la minería limpia el aire”. [Fuente primaria](https://www.nature.com/articles/s41598-026-81164-y).

### RSS y Google Trends — fallback de esta ejecución

- El lector web rechazó feeds XML/RSS con `HTTP 400: Unsupported content-type` (ScienceDaily, Phys.org, NASA, Nature y UNAM) y devolvió `HTTP 404` para ESA; la ruta directa también devolvió `Could not resolve host: raw.githubusercontent.com` al intentar recuperar el script.
- Fallback Exa: ScienceDaily ciencia/salud/espacio y Phys.org devolvieron feeds hasta 27-nov; NASA devolvió entradas hasta 28-nov 05:05Z; UNAM Global permanece en 18-may-2026 y se clasifica STALE. Nature, ESA, EurekAlert y SINC no fueron recuperables por Exa (`CRAWL_UNEXPECTED_CONTENT_TYPE` o `CRAWL_NOT_FOUND`). No se atribuyen a esos feeds artículos que no aparecieron en sus respuestas.
- Google Trends RSS devolvió `CRAWL_UNEXPECTED_CONTENT_TYPE`. Respaldo HTML oficial México: “agujero de la capa de ozono”, 2K+ búsquedas y actividad reciente (~8 h). Es señal de interés, no fuente científica. La referencia ESA disponible es del 26-nov y no se usa para un slot de dato-día que exija publicación dentro de 48 h.
- Para el slot fijo 2026-11-28 23:30, el borrador de llantas ya ocupa la propuesta y no se crea duplicado. El candidato de elefantes se reserva solo como borrador textual para 2026-12-01 07:00, ventana matutina preferente del martes; no es dato-día de 23:30.


## Revisión RSS y respaldo de fuentes primarias — 28-nov-2026 06:03 CDMX

### Acceso a feeds

- Se leyó `scripts/tendencias.py`: ScienceDaily (ciencia/salud/espacio), Phys.org, NASA, ESA, Nature, EurekAlert, SINC, UNAM Global y Google Trends RSS México.
- Reintento directo de ScienceDaily ciencia y Google Trends RSS `geo=MX`: ambos devolvieron exactamente `URLError(gaierror(-3, 'Temporary failure in name resolution'))`. Esto demuestra un fallo DNS del entorno de ejecución, no una caída global de los feeds.
- Respaldo: búsqueda en páginas oficiales de Nature y Phys.org mediante Exa; Crossref REST y resolvedor DOI respondieron para los candidatos listados abajo. Google Trends RSS no aportó una señal verificable en este corte.

### Candidatos de respaldo (no sustituyen el shortlist activo de cinco)

1. **Chemical gradients turn bacterial aggregates inside out** — Nature Physics, 27-nov-2026 09:22Z. DOI `10.1038/s41567-026-03531-w`. El artículo primario describe que, al crecer el agregado de *Neisseria gonorrhoeae*, la adhesión celular más débil en el núcleo privado de oxígeno impulsa a las células interiores hacia fuera y produce eversión de la colonia. Crossref `status=ok`; el resolvedor DOI abrió la página primaria. Frescura calculada al corte: ~26 h 40 min. **Candidato biológico para un slot posterior; PENDING_MAP** hasta contar con localización de laboratorio/muestra sustentada, sin inventar coordenadas.
2. **Cell-autonomous inflammation in VEXAS is mediated by ERAD failure and cGAS–STING** — Nature Cell Biology, open access, 27-nov-2026 10:54Z. DOI `10.1038/s41556-026-02122-4`. El paper primario relaciona pérdida de actividad citoplasmática de UBA1 con fallo ERAD, alteración mitocondrial, señalización cGAS–STING e inflamación. Crossref `status=ok`; resolvedor DOI abrió el artículo primario. Frescura calculada: ~25 h 09 min. **Candidato de biología/cuerpo; PENDING_MAP** y requiere simplificación narrativa sin convertir mecanismo experimental en consejo médico.
3. **Lower central dark matter densities in nearby galaxies than predicted by simulations** — Nature Astronomy, 26-nov-2026 10:02Z. DOI `10.1038/s41550-026-03017-y`. El estudio combina trazadores estelares e hidrógeno neutro en 136 galaxias; informa densidades centrales de materia oscura inferiores a las predichas por varias simulaciones en sistemas masivos. Crossref `status=ok`; resolvedor DOI abrió la página primaria. Frescura calculada: ~50 h 01 min: **fuera de la ventana de 48 h para dato-día 23:30**; conservar solo como backlog espacial, PENDING_MAP.
4. **PM2.5 air pollution weakens global spring greening** — Nature Plants, 27-nov-2026 18:20Z. DOI `10.1038/s41477-026-02464-9`; Crossref `status=ok` y resolvedor DOI confirmado. Aunque es primario y reciente, se clasifica `NO_DUPLICAR` en esta rotación por solapamiento temático con los candidatos actuales de estomas, partículas y contaminación.

### Separación de evidencia y decisión

- **Observación:** títulos, fechas, DOI, resúmenes y resultados anteriores proceden de las páginas editoriales primarias y de Crossref; la nota Phys.org identifica el estudio de PM2.5 de Nature Plants, pero el DOI se verificó contra la ficha primaria.
- **Cálculo:** las edades de publicación se calcularon contra el corte 28-nov-2026 06:03 CDMX; el artículo de materia oscura supera 48 h, los de bacterias y VEXAS permanecen dentro de esa ventana.
- **Inferencia:** los candidatos de bacterias y VEXAS son temáticamente distintos de llantas/albedo, liquen y rapaces; no se afirma que sus coordenadas de investigación estén verificadas.
- **Recomendación:** no crear otro storyboard: el 28-nov 23:30 ya está asignado a llantas/albedo y los slots restantes de hoy tienen ocupación histórica. Conservar bacterias y VEXAS como alternativas para una fecha futura, sujetas a mapa sustentado y slot libre; no promoverlas ahora.


## Corrección de auditoría — 2026-11-28 08:03 CDMX

- **Slot 28-nov 23:30:** la rama main sí contiene una reserva concurrente para `2026-11-23_animal-tama`. Evidencia: metadata `hueco=2026-11-28 23:30` (blob `091b10c0e51cf19dcc0f69073cfdcdd2a495e4d3`) y guion con el mismo hueco (blob `455e98fbe46a9ba03d468374a9e08ffe770d5da1`). Quedan supersedidas las notas previas que afirmaban que main estaba libre.
- Tama tiene procesamiento preexistente: `render.log` registra 85.11 s y `qa_es.json` contiene checks audiovisuales en true. El árbol GitHub no contiene el MP4 al que apunta la metadata; por tanto, para llantas/albedo se registra `CONFLICTO_DE_SLOT_ENTRE_RAMAS`, `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR` y `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`. `publishAt_utc=null`; no se afirma publicación ni programación.
- El storyboard de llantas sigue con 229 palabras, 7 escenas, 78 s + 6 s de cortinilla, título/gancho de 5 palabras, mapa global con bounds y fuente, capa de dato, voz y prompt_base correctos; narrativa PASS/90, SRC-001 `VERIFICADO_CROSSREF`, SRC-002 `VERIFICADO_RESOLVEDOR`. Estado `BORRADOR_EN_PROYECTOS_NO_APTO_PARA_PROMOCION`.
- `cola/entrada/<project_id>.json` y `cola/estado/<project_id>.json` devuelven 404. No se creó estado Grok, entrada plana ni handoff. El validador estructural Python real no se ejecutó; no promover.
- En este corte, el lector web rechazó los RSS XML de ScienceDaily/Phys.org/NASA por `400 Unsupported content-type` y no pudo abrir Google Trends RSS México. Se usó búsqueda de respaldo; no se seleccionó ni desarrolló otro candidato.
