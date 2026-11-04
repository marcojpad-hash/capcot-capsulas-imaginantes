# Radar CAPCOT — 4 de noviembre de 2026

**Corte de investigación:** 4-nov-2026, mañana CDMX.  
**Ventana de publicaciones científicas:** 28-oct a 4-nov-2026 (últimos siete días).  
**Rama:** feature/capcot-video-discovery-continuity.

## 1. Control de rotación y guardia anti-duplicación

La vista reconciliada de scripts/registro_editorial.py une data/rotacion.json, data/publicaciones.json, data/cola.json y los storyboards de proyectos/, cola/entrada/, cola/ y salidas/. El script no recorre recursivamente cola/bloqueados/, por lo que esa carpeta se inspeccionó por separado.

**Evidencia del 4-nov:**
- salidas/2026-11-04_kids-hipo-por-que/storyboard.json: slot 07:00, según la parrilla.
- salidas/2026-11-04_comida-miel-no-caduca/storyboard.json: slot 13:30.
- salidas/2026-11-04_inter-bioluminiscencia-mar/storyboard.json: slot 17:00.
- proyectos/ no contiene otro storyboard con fecha 4-nov.
- cola/entrada/ no contiene un storyboard del 4-nov.
- cola/bloqueados/ contiene copias bloqueadas de los tres proyectos ya existentes y el candidato Machu Picchu 4-nov. Este último se excluye expresamente; no se modifica ni se promueve.
- La parrilla salidas/_ops/2026-10-31_plan_7dias_shots.md y data/horario_semana_2026-11-01_07.json asignan 19:00 a intermedio_2 y dicen expresamente que, si no hay aprobación para Machu Picchu, el respaldo es «Por qué el cielo es azul y el atardecer rojo». Ese respaldo es el único slot autorizado que se desarrolla aquí.
- Inconsistencia detectada y no corregida: la parrilla referencia el project_id 2026-10-29_machu-picchu-fallas-pisa, que no existe en proyectos/, salidas/ ni cola/entrada/; el archivo bloqueado encontrado es cola/bloqueados/2026-11-04_machu-picchu-fallas-pisa.json. Ese storyboard bloqueado no contiene fecha_objetivo ni slot_local. Se conserva intacto y no se atribuye equivalencia de IDs.
- Los tres storyboards ya existentes en salidas/ tampoco contienen fecha_objetivo ni slot_local; su asignación se toma de la parrilla, no del prefijo. El nuevo borrador sí incorpora fecha_objetivo=2026-11-04 y slot_local=19:00.
- Se excluye el slot 23:30. No se produce tema kids del 3-nov ni Machu Picchu del 4-nov.
- Los doce storyboards canónicos del lote 5–7 nov fueron leídos y permanecen intactos. No se crea una segunda copia ni se reescribe ninguno.
- data/temas_del_dia.json llega hasta el 28-oct; data/rotacion.json tiene 27 registros y no contiene entrada del 4-nov; data/publicaciones.json tiene 22 registros y no contiene entrada del 4-nov. Ninguno se modifica.

**Rotación aplicada al respaldo 19:00:** estructura mito_vs_dato (no repite la estructura pregunta de los tres slots previos ni la estructura historia del dato anterior); estilo van_gogh (no repite atlas_antiguo del dato anterior, ni crayones_infantiles, bordado o ukiyo_e de los tres slots del 4-nov, ni estilos del lote 5–7); cama arpegio (no repite pulso ni pizzicato, las dos últimas camas no vacías en la vista combinada).

## 2. Ingesta de RSS: fallos exactos

Se intentó abrir cada URL definida en scripts/tendencias.py. El lector disponible rechazó los feeds XML; no se parseó ningún XML y no se afirma que se haya leído el contenido RSS.

| Feed | URL | Resultado exacto |
|---|---|---|
| ScienceDaily ciencia | https://www.sciencedaily.com/rss/top/science.xml | HTTP 400: Unsupported content-type: application/xml |
| ScienceDaily salud | https://www.sciencedaily.com/rss/top/health.xml | HTTP 400: Unsupported content-type: application/xml |
| ScienceDaily espacio | https://www.sciencedaily.com/rss/space_time.xml | HTTP 400: Unsupported content-type: application/xml |
| Phys.org | https://phys.org/rss-feed/ | HTTP 400: Unsupported content-type: text/xml |
| NASA | https://www.nasa.gov/news-release/feed/ | HTTP 400: Unsupported content-type: application/rss+xml |
| ESA | https://www.esa.int/rssfeed/Our_Activities/Space_Science | HTTP 400: Unsupported content-type: application/rss+xml |
| Nature | https://www.nature.com/nature.rss | HTTP 400: Unsupported content-type: application/rss+xml |
| EurekAlert | https://www.eurekalert.org/rss/news.xml | URL not accessible via this tool |
| SINC | https://www.agenciasinc.es/rss | URL not accessible via this tool |
| UNAM Global | https://unamglobal.unam.mx/feed/ | HTTP 400: Unsupported content-type: application/rss+xml |
| Google Trends RSS México | https://trends.google.com/trending/rss?geo=MX | URL not accessible via this tool |

**Respaldo oficial utilizado:** Google Trends, Tendencias actuales México, últimas 24 horas: https://trends.google.com/trending?geo=MX&hl=es. La página indica 215 tendencias, 25 por página; se inspeccionó sólo la primera página. No se descargó ni se parseó el RSS.

## 3. Google Trends México — observado, no inferido

En la primera página de Tendencias actuales (México, últimas 24 horas, orden por relevancia):
- «antártida»: 2 mil+ búsquedas, +500 %, activa desde hace 13 h.
- «lluvia»: 5 mil+ búsquedas, +1.000 %, activa desde hace 4 h.
- «embalse»: 2 mil+ búsquedas, +400 %, activa desde hace 22 h.
- La mayoría de los otros términos visibles pertenecen a deportes, política y entretenimiento.

**Lectura editorial:** «antártida» es el indicio ambiental más claro de la muestra; «lluvia» y «embalse» podrían relacionarse con tiempo o infraestructura, pero el listado no aporta contexto suficiente para atribuirles una causa científica. Ninguno de los cinco papers siguientes aparece directamente entre los términos visibles. No se fuerza una relación entre tendencia de búsqueda y relevancia científica.

## 4. Cinco candidatos científicos recientes

Los cinco artículos siguientes muestran fecha de publicación entre el 29-oct y el 2-nov en las páginas editoriales indexadas. Las URLs canónicas de los editores están identificadas, pero la verificación de DOI queda **PENDIENTE**: los intentos directos con doi.org y la API de Crossref devolvieron «URL not accessible via this tool»; las fichas de Nature sólo pudieron consultarse mediante resultados indexados. Por tanto, los DOI se transcriben como identificadores citados por el editor, no como DOI validados por Crossref/resolvedor. No se presenta ninguno como verificado.

### C01 — Quantum walks en un sistema Bose–Hubbard (30-oct-2026)

- **Fuente primaria:** Nature Physics, «Multiparticle quantum walks in a dipole-conserving Bose–Hubbard model». https://www.nature.com/articles/s41567-026-03512-z
- **DOI citado por el editor:** 10.1038/s41567-026-03512-z — **PENDIENTE**.
- **Línea:** Actualidad; física cuántica.
- **Novedad observada:** experimento con átomos bosónicos ultrafríos en una red óptica unidimensional; se estudian estados ligados móviles en un sistema con conservación de dipolo.
- **Tendencia:** sin coincidencia directa en la primera página de Trends.
- **Relevancia científica:** alta; resultado experimental en dinámica cuántica restringida.
- **Oportunidad editorial:** media-baja. El gancho posible es que una excitación aislada puede quedar inmóvil mientras un estado ligado sí se desplaza; requiere explicación visual cuidadosa.
- **Público/ocasión:** público general interesado en física; cápsula de curiosidad científica.
- **Riesgos:** no presentar «fractones» como partículas cotidianas ni prometer una aplicación tecnológica inmediata; el sistema es experimental y especializado.
- **Verificación:** fecha y ficha del editor visibles en resultado indexado; DOI pendiente de Crossref/resolvedor.

### C02 — Dieta, geografía y viromas de murciélagos (30-oct-2026)

- **Fuente primaria:** Nature Communications, «Host diet may shape bat RNA viromes within geographic and phylogenetic constraints at a global-scale». https://www.nature.com/articles/s41467-026-79059-7
- **DOI citado por el editor:** 10.1038/s41467-026-79059-7 — **PENDIENTE**.
- **Línea:** Actualidad + Naturaleza/bichos.
- **Novedad observada:** integración de 1.627 bibliotecas de viroma de 78 especies de murciélagos en 13 países. El artículo informa que la geografía y la historia evolutiva del hospedador explican más variación que la dieta; la dieta tiene un papel secundario.
- **Tendencia:** sin coincidencia directa en Trends.
- **Relevancia científica:** alta; comparación global de asociaciones entre ecología alimentaria y comunidades virales.
- **Oportunidad editorial:** alta. El giro narrativo es que el menú no explica tanto como el lugar y la historia evolutiva del animal.
- **Público/ocasión:** público general interesado en fauna, ecología y biología.
- **Riesgos:** no convertir el estudio en una alerta de contagio humano; «viroma» no equivale a enfermedad, y 82,74 % de las unidades virales detectadas quedaron sin clasificar. No inferir transmisión a personas.
- **Verificación:** ficha y resumen del editor visibles en resultado indexado; DOI pendiente de Crossref/resolvedor.

### C03 — Material poroso para capturar oro (30-oct-2026)

- **Fuente primaria:** Nature Communications, «Hydrogen-bond-mediated quasi-two-dimensional covalent organic frameworks for ultrahigh gold extraction». https://www.nature.com/articles/s41467-026-78532-7
- **DOI citado por el editor:** 10.1038/s41467-026-78532-7 — **PENDIENTE**.
- **Línea:** Actualidad; química de materiales.
- **Novedad observada:** una estructura orgánica covalente cuasi-2D expone sitios de unión para capturar y reducir iones de oro; el artículo reporta una capacidad de 5.082,32 mg/g bajo condiciones experimentales con estimulación térmica y vibratoria.
- **Tendencia:** sin coincidencia directa en Trends.
- **Relevancia científica:** alta para química de materiales y recuperación selectiva de metales.
- **Oportunidad editorial:** media. Visualmente claro y con dato fuerte, pero necesita explicar qué mide mg/g y bajo qué condiciones.
- **Público/ocasión:** público general interesado en química, materiales y recuperación de recursos.
- **Riesgos:** no presentarlo como proceso industrial disponible ni como solución demostrada para residuos electrónicos; es un resultado de laboratorio. La versión consultada es publicación temprana aceptada y puede recibir cambios editoriales.
- **Verificación:** ficha y resumen del editor visibles en resultado indexado; DOI pendiente de Crossref/resolvedor.

### C04 — Atlas celular de cáncer colorrectal de inicio temprano (29-oct-2026)

- **Fuente primaria:** Nature Medicine, «Insights into early-onset colorectal cancer from a single-nucleus RNA-seq atlas of colorectal cancer across the age continuum». https://www.nature.com/articles/s41591-026-04721-y
- **DOI citado por el editor:** 10.1038/s41591-026-04721-y — **PENDIENTE**.
- **Línea:** Actualidad. La línea médica sigue siendo futura/propuesta; no se crea una línea temática nueva.
- **Novedad observada:** atlas de secuenciación de núcleo único de 189 tumores primarios: 54 de inicio temprano y 135 de inicio promedio; 850.222 núcleos analizados. El resumen informa diferencias de composición celular en tumores MSS de pacientes más jóvenes y una validación externa.
- **Tendencia:** sin coincidencia directa en Trends.
- **Relevancia científica:** alta; aporta resolución celular a una pregunta de biología tumoral.
- **Oportunidad editorial:** media, con prioridad inferior a los candidatos de fauna/materiales por la carga médica y la necesidad de contexto.
- **Público/ocasión:** adultos interesados en investigación biomédica y alfabetización científica.
- **Riesgos:** no atribuir causalidad a la edad, dieta o hábitos; no extrapolar riesgo individual ni dar consejos de tamizaje. El estudio analiza muestras tumorales, no una encuesta poblacional de riesgo.
- **Verificación:** ficha y resumen del editor visibles en resultado indexado; DOI pendiente de Crossref/resolvedor.

### C05 — Ensayo fase 2 UNICORN en cáncer de colon (2-nov-2026)

- **Fuente primaria:** Nature Medicine, «Neoadjuvant botensilimab with or without balstilimab in pMMR and dMMR colon cancer: the phase 2 UNICORN trial». https://www.nature.com/articles/s41591-026-04710-1
- **DOI citado por el editor:** 10.1038/s41591-026-04710-1 — **PENDIENTE**.
- **Línea:** Actualidad. La línea médica sigue siendo futura/propuesta; no se crea una línea temática nueva.
- **Novedad observada:** ensayo fase 2 con 56 pacientes y cuatro cohortes secuenciales según estado de reparación de errores de ADN y régimen. El grupo dMMR con combinación BOT+BAL registró respuesta patológica mayor en 14/14 pacientes; 13/14 tuvieron respuesta patológica completa. El resultado no se extiende a todos los grupos.
- **Tendencia:** sin coincidencia directa en Trends.
- **Relevancia científica:** alta para investigación clínica; resultado preliminar de una estrategia neoadyuvante.
- **Oportunidad editorial:** baja-media para el canal general: el interés público es alto, pero el contexto clínico requerido excede una cápsula breve.
- **Público/ocasión:** adultos interesados en investigación clínica; no es material de orientación médica.
- **Riesgos:** fase 2, grupos pequeños y asignación secuencial; no presentarlo como cura, estándar de atención ni recomendación terapéutica. No omitir eventos adversos inmunitarios ni intervalos de confianza.
- **Verificación:** ficha y resumen del editor visibles en resultado indexado; DOI pendiente de Crossref/resolvedor.

## 5. Falsos recientes descartados por fecha del estudio original

No se contaron como candidatos de los últimos siete días aunque circularon en notas recientes:
- Betelgeuse: comunicado de ALMA del 30-oct, pero el preprint original fue enviado a arXiv el 3-ago-2026; la fecha de publicación de la versión de revista no quedó verificada. No se cuenta como paper reciente.
- Misterio de los anfibios/quitridiomicosis: el artículo de Molecular Ecology fue publicado el 14-oct; queda fuera de la ventana.
- Oxígeno excedente en magma: National Science Review publicó el artículo el 25-ago; la nota de octubre no lo vuelve reciente.
- Galaxia anular GS18660: Astronomy & Astrophysics publicó el artículo el 8-sep; fuera de ventana.
- Respuesta cerebral infantil a ultraprocesados: el artículo de JAMA Network Open es del 23-oct; fuera de la ventana de siete días.

## 6. Recomendación editorial

**Para futuros slots de Actualidad:** C02 (viromas de murciélagos) es la mejor oportunidad narrativa del radar: contraste claro entre dieta y geografía/historia evolutiva, con una advertencia explícita contra extrapolar a contagio humano. C03 (captura de oro) queda como segunda opción si el guion explica la capacidad de laboratorio sin prometer despliegue industrial. C01 requiere simplificación conceptual. C04 y C05 se retienen por riesgo de simplificación médica.

**Para el slot 19:00 del 4-nov:** no se elige uno de esos cinco papers porque la parrilla ya contiene un respaldo específico y explícito: «Por qué el cielo es azul y el atardecer rojo». Se desarrolla ese respaldo evergreen como Dato científico; no se presenta como noticia reciente ni como paper de la ventana.

## 7. Seguimiento técnico Meta / Google Trends

- **Google Trends API alpha:** la documentación oficial sigue describiendo acceso alfa limitado a solicitantes, ventana móvil de cinco años, agregaciones diarias/semanales/mensuales/anuales y comparaciones por países/subregiones. No se encontró una nueva versión pública ni un cambio que justifique modificar docs/INVESTIGACION_API_META_Y_GOOGLE_TRENDS.md.
- **Meta Graph API / Instagram Insights / Facebook Pages Insights:** las rutas oficiales consultadas tuvieron estos resultados: Graph API changelog v25/v26, referencia de Instagram Insights y Page Insights devolvieron «URL not accessible via this tool»; Instagram Platform changelog devolvió HTTP 429 Too Many Requests. Sin evidencia oficial nueva verificable, el documento técnico se deja intacto.

## 8. Contexto de radar de YouTube heredado (corte 3-nov, ~22:00 CDMX)

Este bloque se conserva como evidencia histórica del brief anterior; no se reconsultó ni se presenta como tendencia nueva de esta corrida.
1. «¿Qué pasa dentro de…?» en el cuerpo y en objetos: Shorts en español con 583K, 446K y 371K vistas.
2. «Cómo funciona» lo cotidiano: bolígrafo (1,16 M) y planta que rompe el cemento (1,35 M).
3. Ballena azul: noticia en Chile reportada por NMás (~11K); sólo como contexto para el slot del 6-nov.
4. Palomitas: conversación viral alrededor de la cubeta de Dune 3; sólo como contexto para el slot del 5-nov.
5. Débiles en ese corte: Venus, animales récord y tips de cocina en español; el «sabías que» estaba dominado por celebridades.

## 9. Límites y estado de preproducción

- Ningún RSS XML se parseó. Google Trends se consultó sólo mediante la página oficial Trending Now, primera página de 25 resultados.
- Los cinco DOI permanecen pendientes de Crossref/resolvedor; no se presentan como validados.
- El storyboard de respaldo queda únicamente en proyectos/2026-11-04_cielo-azul-atardecer-rojo/storyboard.json. No se copia a cola/entrada/, no se marca preparado y no contiene narrative_qa.
- El borrador tiene 8 escenas, 210 palabras narradas y 86 segundos totales (80 de escenas + 6 de cortinilla). Incluye mapa con coordenadas de referencia, dato/gráfico, fuentes por escena, voz y prompts de un único estilo literal del catálogo.
- El QA narrativo en frío queda pendiente del auditor independiente. No se declara PASS ni aceptación de Grok.
- No se generaron imágenes, frames, audio, voz, video ni renders. approved_assets permanece vacío; export.render_status es NOT_GENERATED; publicacion.status es PENDIENTE_DECISION_GROK.
- No se modificaron data/*.json, scripts, el informe técnico, main, motores ni otros proyectos.
