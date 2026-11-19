# Radar CAPCOT — 19 de noviembre de 2026

**Corte:** 2026-11-19, 07:56 America/Mexico_City.  
**Rama:** `feature/capcot-video-discovery-continuity`.  
**Ventana científica:** 12–19 de noviembre de 2026 (últimos siete días, inclusive).

## Resultado operativo y guardia anti-duplicación

- **Slot principal:** `17:00 / intermedio_1`, dentro de la ventana activa 16:30–18:00 de `data/horarios.json`. Libre al corte en `proyectos/`, `salidas/`, `cola/entrada/` y `cola/bloqueados/`; no existe proyecto del 19-nov con `slot_local=17:00`. Se creó `2026-11-19_dato-estrella-dentro-de-estrella`.
- **Slot 23:30:** `slot_cesta=dato_del_dia`, activo por `docs/CONTRATO_OPERATIVO_UNIFICADO.md` §3 y `data/horarios.json`. Libre al corte; no existe proyecto del 19-nov con `slot_local=23:30` ni `slot_cesta=dato_del_dia` en las cuatro ubicaciones. La fuente primaria del 23:30 fue publicada online el mismo 19-nov y su PDF editorial fue leído; se creó el proyecto independiente `2026-11-19_dato-dia-luz-dos-manos-oro-poroso`.
- No existe `data/horario_2026-11-19.json`; se aplicó el horario activo general y el contrato operativo. `data/temas_del_dia.json`, `data/rotacion.json` y `data/publicaciones.json` se leyeron solo para consulta; no se modificaron.
- Se contrastó la lógica de lectura combinada de `scripts/registro_editorial.py` con el inventario Git de proyectos, salidas y colas. No se reutilizó un slot de otra fecha.
- Se crearon dos storyboards independientes; ninguno se escribió en `cola/entrada/`. Ambos permanecen como borradores del investigador y sin `narrative_qa`.

## Radar científico — cinco candidatos

### 1. Recomendación principal — Una compañera se hunde dentro de una gigante en Andrómeda

**Novedad observada:** AT 2025abao mostró un periodo de brillo gradual de siete años. La interpretación que mejor explica la espectroscopía anterior y posterior al estallido es una compañera de aproximadamente 0.7 masas solares inspiralando dentro de la envoltura convectiva de una gigante AGB de aproximadamente 7 masas solares. La fusión posterior habría expulsado el 10% más externo de la envoltura a velocidades cercanas a diez veces la velocidad de escape de la estrella primaria.

**Fuente primaria:** Karambelkar, V.; De, K.; Temmink, K. D. et al. “An inspiral of a star inside a common envelope with its giant companion”. *Nature* 659, 628–633 (2026). Publicado 18-nov-2026; número fechado 19-nov-2026.  
URL editorial: https://www.nature.com/articles/s41586-026-11221-z  
DOI mostrado por la editorial: `10.1038/s41586-026-11221-z` — **PENDIENTE_RESOLVEDOR**. La página de Nature fue leída; doi.org y Crossref no fueron accesibles. No se presenta el DOI como validado.  
Contraste oficial: NASA Science, “AT 2025abao in the Andromeda Galaxy” (18-nov-2026): https://science.nasa.gov/asset/webb/at-2025abao-in-the-andromeda-galaxy/

- **Línea:** Actualidad / astronomía dentro de la ampliación temática del 25-oct; no se abre una línea nueva.
- **Tendencia:** sin señal científica clara en las primeras 25 tendencias de Google Trends México.
- **Relevancia científica:** alta; observación multibanda y espectroscópica que permite reconstruir una fase de envoltura común antes descrita sobre todo mediante modelos.
- **Oportunidad editorial:** alta; anomalía de siete años → fricción orbital → fusión → expulsión de envoltura.
- **Público/ocasión:** público general interesado en astronomía; slot principal de tarde.
- **Riesgos:** no afirmar que se fotografiaron dos estrellas dentro del gas; las masas son estimaciones del modelo; no llamarlo supernova. El mapa usa coordenadas celestes RA/Dec publicadas por NASA, no latitud/longitud terrestre.
- **Verificación:** página primaria Nature leída; página NASA oficial leída; DOI pendiente de resolver independientemente.

### 2. Homo erectus persistió en selvas tropicales del sur de China

**Novedad observada:** nueve dientes homininos de dos cuevas hermanas en Guangxi; ocho identificados morfológica y genéticamente como *Homo erectus*. El artículo integra 43 edades radiométricas de cinco técnicas y sitúa la presencia entre 324 y 184 mil años. Los isótopos de tres dientes de Naxian son compatibles con recursos de bosque tropical cerrado; el tamaño de esa submuestra debe conservarse como límite.

**Fuente primaria:** Westaway, K. E.; Joannes-Boyau, R.; Liao, W. et al. “Rainforest adaptation in late Homo erectus from southern China”. *Nature* (2026), publicado 18-nov-2026.  
URL editorial: https://www.nature.com/articles/s41586-026-11155-6  
DOI mostrado por la editorial: `10.1038/s41586-026-11155-6` — **PENDIENTE_RESOLVEDOR**. El resultado editorial y el texto del artículo fueron consultados; la apertura directa y el resolvedor no completaron acceso.

- **Línea:** Actualidad / paleoantropología dentro de la ampliación temática vigente.
- **Tendencia:** sin señal clara en Google Trends México.
- **Relevancia científica:** alta; amplía el contexto temporal y ecológico conocido para poblaciones tardías de `H. erectus` en China.
- **Oportunidad editorial:** alta; contradice la idea simplificada de que `H. erectus` solo ocupó paisajes abiertos.
- **Público/ocasión:** curiosidad sobre evolución humana y paleontología.
- **Riesgos:** no generalizar a toda la especie; la inferencia isotópica directa de dieta/hábitat se limita a n=3 dientes de Naxian; no convertir movilidad potencial en migración demostrada.
- **Verificación:** resultado editorial Nature con resumen y texto consultado; DOI pendiente de resolución independiente.

### 3. Un deslizamiento submarino fue observado mientras retrocedía cuesta arriba

**Novedad observada:** monitorización directa de deslizamientos totalmente submarinos en Homathko Delta, oeste de Canadá. El retroceso lento cuesta arriba es compatible con fallo por `breaching`; el proceso puede sostener corrientes de turbidez y transportar sedimento, carbono y contaminantes mar adentro.

**Fuente primaria:** Englert, R. G.; Cartigny, M. J. B.; Baker, M. L. et al. “Direct monitoring of breaching in deltaic submarine landslides”. *Science* 394(6825), 758–762 (2026), publicado 12-nov-2026.  
URL editorial: https://www.science.org/doi/10.1126/science.aef8444  
DOI: `10.1126/science.aef8444` — **PENDIENTE_RESOLVEDOR**. Registro bibliográfico y abstract en PubMed: https://pubmed.ncbi.nlm.nih.gov/43019430/; comunicado del National Oceanography Centre: https://www.noc.ac.uk/news/scientists-capture-first-direct-observations-underwater-landslides. La página Science/resolvedor no fue accesible.

- **Línea:** Actualidad / geología y procesos marinos.
- **Tendencia:** sin señal clara en las primeras 25 tendencias.
- **Relevancia científica:** alta; valida en entorno natural un mecanismo de fallo submarino que antes no se había monitorizado directamente.
- **Oportunidad editorial:** alta; el fondo marino no colapsa necesariamente de golpe: el fallo puede migrar y sostener corrientes.
- **Público/ocasión:** curiosidad de geología, océanos e infraestructura submarina.
- **Riesgos:** no generalizar a todos los deslizamientos; el sitio observado es Homathko Delta y el mecanismo descrito corresponde a ese contexto sedimentario.
- **Verificación:** metadatos y abstract PubMed leídos; comunicado institucional leído; artículo Science/resolvedor pendientes.

### 4. El océano aumentó su absorción de carbono; la tendencia terrestre no fue robusta

**Novedad observada:** el estudio usa más de 30 años de observaciones atmosféricas de O₂ y CO₂. Para 1990–2019 estima un aumento del sumidero oceánico de 0.63 ± 0.19 Pg C año⁻¹ por década; su media fue 2.8 ± 0.4 Pg C año⁻¹. El sumidero neto terrestre no mostró una tendencia robusta, con media de 1.0 ± 0.5 Pg C año⁻¹.

**Fuente primaria:** Morgan, E. J.; Jin, Y.; Kozlova, E. et al. “Atmospheric O2 reveals a strengthening ocean carbon sink and a stagnant net land sink since 1990”. *Science* 394(6825), 799–803 (2026), publicado 12-nov-2026.  
URL editorial: https://www.science.org/doi/10.1126/science.aed9544  
DOI: `10.1126/science.aed9544` — **PENDIENTE_RESOLVEDOR**. Registro bibliográfico y abstract en PubMed: https://pubmed.ncbi.nlm.nih.gov/43019429/. La página Science/resolvedor y Crossref no fueron accesibles.

- **Línea:** Actualidad / clima y ciencia de la Tierra.
- **Tendencia:** sin señal clara en Google Trends México.
- **Relevancia científica:** alta; aporta una estimación observacional de largo plazo de la evolución de los sumideros.
- **Oportunidad editorial:** media; dato importante, pero requiere explicar unidad, periodo y diferencia entre océano y tierra.
- **Público/ocasión:** público general interesado en clima.
- **Riesgos:** no decir que el océano “compensa” las emisiones; el periodo estudiado termina en 2019; “sin tendencia robusta” no significa absorción cero.
- **Verificación:** metadatos y abstract PubMed leídos; DOI/resolvedor pendientes.

### 5. Oro poroso y una plantilla tipo shuriken amplifican la quiralidad óptica — fuente apta para 23:30

**Novedad observada:** el artículo combina una plantilla quiral de seis brazos tipo shuriken con una red electrodepositada de oro nanoporoso. La interferencia entre ambos componentes produce hotspots superquirales. El trabajo informa detección en rango de attomoles y fotocleavage enantioselectivo de metalaxil racémico, con exceso enantiomérico superior al 25% bajo luz continua linealmente polarizada.

**Fuente primaria:** Guselnikova, O. et al. “Chiral SERS and photochemistry via collective hotspot asymmetry in metasurface-templated gold networks with disordered nanoscale porosity”. *Nature Communications* (2026), Article in Press, publicado online 19-nov-2026.  
PDF editorial primario: https://www.nature.com/articles/s41467-026-78158-9_reference.pdf  
DOI mostrado en el PDF: `10.1038/s41467-026-78158-9` — **PENDIENTE_RESOLVEDOR**. El PDF editorial primario fue leído y confirma fecha, autores, afiliaciones, método y resultados; doi.org y Crossref no fueron accesibles.

- **Línea:** Dato científico / química y óptica experimental; ampliación provisional de la marca, sin abrir una línea tecnológica nueva.
- **Tendencia:** sin señal clara en las primeras 25 tendencias.
- **Relevancia científica:** alta en óptica quiral y materiales plasmónicos; el trabajo combina dos componentes que por separado no generan el mismo campo superquiral.
- **Oportunidad editorial:** media-alta; el patrón tipo shuriken y el oro poroso son visualmente claros, y el giro depende de la interferencia entre ambos.
- **Público/ocasión:** curiosidad de química, óptica y materiales; dato del día 23:30.
- **Riesgos:** el exceso enantiomérico >25% corresponde a metalaxil racémico bajo condiciones específicas (10⁻⁴ M, 780 nm, luz continua linealmente polarizada, N=3 muestras); no afirmar un sensor clínico ni rendimiento universal. El mapa del storyboard muestra ciudades de afiliación, no ubicaciones de experimento.
- **Verificación:** PDF editorial primario leído; URL verificada; DOI pendiente de resolución independiente.

## Google Trends México — respaldo oficial

- RSS de Google Trends México: URL no accesible desde esta herramienta; no se parseó XML.
- Respaldo usado: Trending Now oficial, México, últimas 24 horas: https://trends.google.com/trending?geo=MX&hl=es-419
- La página muestra **148 tendencias**; la primera página contiene 25. Entre las consultas visibles aparecen terremoto, GTA VI, partidos de básquet/fútbol, entretenimiento y búsquedas locales. No se observa una señal clara de ciencia/naturaleza en esas primeras 25.
- **Límite:** la ausencia en las primeras 25 no demuestra ausencia de interés científico en toda la plataforma; solo describe el corte consultado.

## RSS científicos — fallos exactos de lectura

Se consultaron las diez URL definidas en `scripts/tendencias.py`. La herramienta no admitió los tipos XML/RSS o no pudo abrir el recurso; **no se afirma que se haya descargado ni parseado XML**.

| Feed | Resultado observado |
|---|---|
| ScienceDaily Top Science | HTTP 400: `Unsupported content-type: application/xml` |
| ScienceDaily Top Health | HTTP 400: `Unsupported content-type: application/xml` |
| ScienceDaily Space & Time | HTTP 400: `Unsupported content-type: application/xml` |
| Phys.org RSS | HTTP 400: `Unsupported content-type: text/xml` |
| NASA News Release RSS | HTTP 400: `Unsupported content-type: application/rss+xml` |
| ESA Space Science RSS | HTTP 404: `Not Found` |
| Nature RSS | HTTP 500; redirige a `idp.nature.com/authorize` y el recurso no es accesible por la herramienta |
| EurekAlert RSS | URL no accesible por la herramienta; sin código HTTP disponible |
| Agencia SINC RSS | URL no accesible por la herramienta; sin código HTTP disponible |
| UNAM Global RSS | HTTP 400: `Unsupported content-type: application/rss+xml` |
| Google Trends RSS México | URL no accesible por la herramienta; sin código HTTP disponible |

## Observado, cálculo, inferencia y recomendación

- **Observado:** fecha de publicación y resultados en las páginas primarias/editoriales accesibles; metadatos y abstracts PubMed para los dos artículos Science; coordenadas NASA para AT 2025abao; fecha y resultados del PDF Nature Communications; 148 tendencias de Google Trends México; errores RSS listados arriba.
- **Cálculo:** los dos guiones concatenados tienen 197 y 188 palabras, respectivamente. Cada storyboard contiene ocho escenas con 78 s de escena más 6 s de cortinilla = 84 s.
- **Inferencia:** la fase de envoltura común explica mejor la secuencia de brillo de AT 2025abao que una explosión instantánea; la sinergia shuriken–oro poroso explica la respuesta superquiral reportada. Son interpretaciones de los autores, no observaciones visuales directas de los campos o de las estrellas dentro del gas.
- **Recomendación editorial:** usar AT 2025abao en el slot principal de 17:00 por su arco causal y su mapa celeste verificable. Usar el estudio de SERS para 23:30 porque su PDF primario está publicado el mismo día, fue leído y ofrece un mecanismo visual distinto.

## Seguimiento técnico — Meta y Google Trends

Se comparó la documentación oficial con `docs/INVESTIGACION_API_META_Y_GOOGLE_TRENDS.md`.

- **Graph API:** la ruta canónica https://developers.facebook.com/documentation/development/graph-api/changelog muestra v27.0, introducida 4-nov-2026. La ruta heredada https://developers.facebook.com/docs/graph-api/changelog/versions/ sigue mostrando v26.0 como última fila. La referencia Page Insights muestra encabezado v27.0.
- **Page Insights:** siguen visibles los límites ya documentados: mínimo de 100 likes para la Page, actualización de la mayoría de métricas aproximadamente cada 24 h, retención de hasta dos años, ventanas `since/until` de hasta 90 días, umbral de 100 personas para demografía y ausencia de interacciones de Reels en Page Insights. No se detectó un cambio nuevo de métrica.
- **Instagram Insights:** la guía vigente documenta Unified Login, Instagram Login y Facebook Login con hosts, tokens y permisos distintos; algunas métricas no están disponibles por debajo de 100 seguidores, retención de 90 días, una cuenta por solicitud y conjunto vacío en vez de cero cuando no hay dato. El changelog visible no tiene entradas posteriores al 30-jul-2026 sobre Insights.
- **Google Trends API alfa:** continúa con acceso alfa limitado, ventana móvil de cinco años, agregación diaria/semanal/mensual/anual, regiones/subregiones y datos escalados consistentemente. No se observó cambio nuevo del contrato alfa.
- Se añadió una nota correctiva §9.10 al informe técnico para distinguir la ruta canónica v27.0 de la ruta heredada que sigue mostrando v26.0. No se modificaron adaptadores, conectores, permisos ni credenciales.

## QA preexistente — solo lectura

El radar del 18-nov registró 160 storyboard.json físicos: 39 con `narrative_qa` (17 PASS, 20 FAIL, 2 PENDIENTE) y 121 sin `narrative_qa` (`PENDIENTE_AUDITOR`). Se comprobó el historial de commits posterior y se releyeron los dos storyboards añadidos/modificados el 18-nov; los 39 registros anteriores permanecen sin cambios. El estado actual previo a los dos borradores de hoy es 162 storyboards: **41 con `narrative_qa` (18 PASS, 20 FAIL, 3 PENDIENTE) y 121 sin `narrative_qa`**.

### Relecturas recientes — valores literales del JSON

- `2026-11-18_dato-kuroshio-puente-atmosferico`: `status=PASS`, `score=90`, `review_basis=lectura_en_frio_solo_narracion`, `reviewed_at=2026-11-18T15:00:00-06:00`; los siete checks son `true`; `critical_flags=[]`.
- `2026-11-18_dato-catorce-campos-hidrotermales`: `status=PENDING_INDEPENDENT_COLD_READ`, `score=null`, `review_basis=pendiente_lectura_en_frio_solo_narracion`, `reviewed_at=null`; los siete checks son `false`; `critical_flags=["QA narrativa independiente pendiente"]`.
- `2026-11-17_dato-suelo-dos-relojes`: `status=PASS`, `score=89`, `review_basis=lectura_en_frio_solo_narracion`, `reviewed_at=2026-11-17T15:35:22-06:00`; los siete checks son `true`; `critical_flags=[]`.
- `2026-11-16_dato-polen-desenreda-nanotubos`: `status=PASS`, `score=91`, `review_basis=lectura_en_frio_solo_narracion`; el JSON no contiene `reviewed_at`; los siete checks son `true`; `critical_flags=[]`.
- `2026-11-15_dato-dia-diapausa-lestes-sponsa`: `status=PASS`, `score=90`, `review_basis=lectura_en_frio_solo_narracion`, `reviewed_at=2026-11-15T15:51:23-06:00`; los siete checks son `true`; `critical_flags=[]`.
- `2026-11-14_dato-robot-polinizador-colibri`: el path de storyboard consultado devuelve 404; no se reconstruyó ni se sustituyó.
- Los otros 39 registros detallados y los 121 proyectos sin `narrative_qa` se conservan exactamente como en [el radar del 18-nov](2026-11-18_RADAR_CAPCOT.md); no se modificaron.

Los dos borradores del 19-nov no contienen `narrative_qa` y quedan **PENDIENTE_AUDITOR**. No se autoevaluó la narración, no se promovió ningún archivo a `cola/entrada/` y no se creó estado Grok.

## Compuerta estructural de los dos borradores

| Control | 17:00 — AT 2025abao | 23:30 — SERS |
|---|---:|---:|
| JSON parseable desde GitHub | PASS | PASS |
| Palabras de narración | 197 | 188 |
| Escenas | 8 | 8 |
| Duración de escenas | 78 s | 78 s |
| Cortinilla | 6 s | 6 s |
| Duración total | 84 s | 84 s |
| Gancho ≤6 palabras | PASS | PASS |
| Arco completo | PASS | PASS |
| Contrato narrativo, seis campos | PASS | PASS |
| source_ids existentes y por escena | PASS | PASS |
| Voz edge-tts es-MX-JorgeNeural, +7%, -2Hz | PASS | PASS |
| Estilo único y prompt_base literal | PASS | PASS |
| Mapa con coordenadas y nota de precisión | PASS | PASS |
| Dato/gráfico con condiciones y fuente | PASS | PASS |
| approved_assets exactamente [] | PASS | PASS |
| export.render_status = NOT_GENERATED | PASS | PASS |
| export.filename y rutas de medios ausentes | PASS | PASS |
| publicacion.status = PENDIENTE_DECISION_GROK | PASS | PASS |
| narrative_qa ausente | PASS | PASS |

**No se creó** `*_fuentes.md`, frame, imagen, audio, video, render ni copia en cola. Las fuentes están dentro de cada JSON. El estado de los dos proyectos sigue siendo borrador del investigador.

## Seguridad y límites

No se solicitaron ni copiaron credenciales. No se consumieron créditos. No se modificaron `main`, workflows, `data/*.json`, motores canónicos ni Motor U6. No se publicó ni programó contenido. Grok conserva selección editorial, producción audiovisual, QA oficial y publicación.
