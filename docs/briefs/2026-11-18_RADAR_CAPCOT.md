# Radar CAPCOT — 18 de noviembre de 2026

**Serie:** Datos y ociosidades  
**Consulta:** 08:03, America/Mexico_City (CDMX)  
**Repositorio:** marcojpad-hash/capcot-capsulas-imaginantes  
**Rama:** feature/capcot-video-discovery-continuity  
**Base de lectura:** commit 247a4e9d25b694c4f400d2e0037b5393814c24eb

## Resultado operativo

- **Slot principal elegido:** 17:00, cesta `intermedio_1`. Está dentro de la ventana de tarde vigente (16:30–18:00), es miércoles preferente y no aparece ocupado por ningún storyboard, salida, cola ni registro de publicación/rotación para 2026-11-18.
- **07:00:** ventana ya transcurrida al momento de consulta (08:03); no se crea paquete retroactivo.
- **13:30:** permanece como prueba, no como ventana activa.
- **19:00:** permanece retirado.
- **23:30 / dato_del_dia:** slot fijo, activo y libre; **PENDING_SOURCE**. Hay un artículo primario publicado hoy sobre campos hidrotermales, pero la página editorial directa devolvió HTTP 500/redirección a idp.nature.com y Crossref/doi.org no pudieron resolverse. No se crea storyboard de 23:30 hasta completar la verificación.
- **Proyecto principal creado:** `proyectos/2026-11-18_dato-kuroshio-puente-atmosferico/storyboard.json`, commit final del storyboard: `247a4e9d25b694c4f400d2e0037b5393814c24eb`.
- **Archivos nuevos para esta fecha:** exactamente un radar y un storyboard principal. No se crea `*_fuentes.md`, no se crea storyboard 23:30 y no se toca material preexistente.

## Guardia anti-duplicación y rotación

- No existe `data/horario_2026-11-18.json`; se aplicó el contrato vigente junto con `data/horarios.json`. La política desde 2026-11-09 conserva la ventana de mañana 06:30–07:30, la ventana de tarde 16:30–18:00 y el slot fijo 23:30; 13:30 figura como prueba y 19:00 como retirado.
- Se enumeraron y revisaron los 160 storyboard.json físicos preexistentes en `proyectos/`, `salidas/`, `cola/entrada/` y `cola/bloqueados/`. Ninguno declara `fecha_objetivo=2026-11-18` ni `slot_local=17:00` o `23:30`.
- No existía archivo del 18-nov en briefs, proyectos, salidas ni colas antes de crear el storyboard principal. La ruta de radar estaba libre.
- `data/temas_del_dia.json` no contiene 2026-11-18 y su última fecha registrada es 2026-10-28; `data/rotacion.json`, `data/publicaciones.json` y `data/cola.json` llegan hasta 2026-10-31. Por eso la rotación se contrastó con la lectura combinada de `scripts/registro_editorial.py` y los storyboards recientes. El último registro editorial de proyecto es 2026-11-17.
- La lectura del script muestra que su glob cubre proyectos, salidas y entrada, pero no la subcarpeta `cola/bloqueados/`; esta última se inspeccionó por separado para duplicación y QA.
- Última cápsula anterior: 2026-11-17, estilo `papel_stop_motion`, estructura `sabias_que`, cama `circuito_neural`. El borrador nuevo usa `atlas_antiguo`, estructura `pregunta` y cama `pulso`; no repite estilo ni estructura de la cápsula anterior ni de otro proyecto del 18-nov.

## Radar científico: cinco candidatos de los últimos siete días

### 1. Recomendación principal — Corriente del Golfo y extensión de Kuroshio

- **Estudio:** Yamagami, Yoko; Tatebe, Hiroaki; Kohyama, Tsubasa; Kido, Shoichiro; Okajima, Satoru; Komuro, Yoshiki. “Kuroshio Extension warming shaped by Gulf Stream variability via the Arctic atmosphere.” *Nature Geoscience* (2026), versión de registro publicada el 17-11-2026.
- **DOI mostrado por la editorial:** 10.1038/s41561-026-02139-2. **Estado:** PENDIENTE_RESOLVEDOR; no se declara DOI validado. La página editorial primaria se abrió y mostró fecha, autores, versión de registro, abstract, resultados y DOI; Crossref y doi.org devolvieron “URL is not accessible via this tool”.
- **URL editorial:** https://www.nature.com/articles/s41561-026-02139-2
- **Novedad observada:** un estudio de modelación encuentra una teleconexión asimétrica: anomalías cálidas de la Corriente del Golfo activan una respuesta atmosférica tipo Modo Anular del Norte, debilitan la baja de las Aleutianas y desplazan la extensión de Kuroshio hacia el norte.
- **Condiciones y cifra:** control preindustrial idealizado de 100 años; diez miembros por experimento. La señal atlántica explica aproximadamente 13% de la varianza interna de TSM en la región de Kuroshio a escalas mayores que la interanual; el forzamiento del Pacífico tropical explica 4% en los experimentos comparados.
- **Tendencia:** sin señal directa de Kuroshio/Gulf Stream en las primeras 25 tendencias de México.
- **Relevancia científica:** teleconexión océano-atmósfera y variabilidad térmica del Pacífico Norte.
- **Oportunidad editorial:** explicar cómo dos corrientes separadas pueden conectarse por la atmósfera, sin que el agua cruce de un océano al otro.
- **Público/ocasión:** público general interesado en océanos y clima; ventana de tarde 17:00.
- **Riesgos:** 13% no es porcentaje del calentamiento global ni del calor total del océano; resultado de simulaciones idealizadas, no atribución causal observacional directa; no presentar influencia recíproca; la relación depende de la resolución oceánica.
- **Verificación:** URL editorial verificada; DOI pendiente de resolver. **Recomendación:** desarrollar como storyboard principal.

### 2. Candidato para 23:30 — Catorce campos hidrotermales en el Índico

- **Estudio:** Fuchs, Sebastian; Kuhn, Thomas; Meyn, Klaas; Kihara, Terue; Garbe-Schönberg, Dieter; Klischies, Meike; Freitag, Ralf; Schwarz-Schampera, Ulrich. “The discovery of fourteen hydrothermal vent fields and associated polymetallic massive sulfides in the central Indian Ocean.” *Scientific Reports* (2026), publicado 18-11-2026.
- **DOI mostrado en el resultado editorial:** 10.1038/s41598-026-80304-8. **Estado:** PENDING_SOURCE / PENDIENTE_RESOLVEDOR.
- **URL editorial:** https://www.nature.com/articles/s41598-026-80304-8
- **Novedad observada:** catorce campos hidrotermales alrededor de la triple unión de Rodrigues; cuatro asociados a rocas ultramáficas; sitios inactivos superan a activos en la mayoría de los campos; hay ocurrencias de sulfuros hasta 16 km fuera del eje de la dorsal. La oxidación de los montículos da una secuencia relativa de actividad, no edades absolutas.
- **Tendencia:** no hay búsqueda inequívoca de respiraderos hidrotermales; Trends muestra señales de clima extremo, no de este estudio.
- **Relevancia científica:** geología marina, sulfuros polimetálicos y actividad hidrotermal.
- **Oportunidad editorial:** contraste visual entre campos activos e inactivos y la huella química que permanece.
- **Público/ocasión:** público general interesado en océanos y geología; sería apto para el slot de noticia del día si se completa la verificación.
- **Riesgos:** artículo en early access aceptado, sujeto a sustitución por versión final; no convertir oxidación en datación absoluta; no tratar el pin regional como coordenada de un respiradero.
- **Verificación:** la página editorial directa devolvió HTTP 500/redirección a idp.nature.com; Crossref y doi.org no fueron accesibles. Aunque el resultado de búsqueda muestra el abstract y el DOI, no cumple la compuerta de verificación para 23:30. **Estado operativo: PENDING_SOURCE; no crear storyboard.**

### 3. PIC-NIC: tensión mecánica del ADN y reconocimiento de factores de transcripción

- **Estudio:** Yao, Yumi Minyi; O’Hagan, Michael P.; Onoon, Karn; Givon, Lihee; Hamer-Rogotner, Shelly; Salinas, Raul; Nithun, Raj V.; Kessler, Naama; Jbara, Muhammad; Dym, Orly; Pipatpolkai, Tanadet; Schumacher, Maria A.; Afek, Ariel. “PIC-NIC reveals that DNA mechanical strain impacts transcription factor recognition.” *Nature Structural & Molecular Biology* (2026), publicado 18-11-2026.
- **DOI mostrado por la editorial:** 10.1038/s41594-026-01919-z. **Estado:** PENDIENTE_RESOLVEDOR.
- **URL editorial:** https://www.nature.com/articles/s41594-026-01919-z
- **Novedad observada:** el estudio analiza 15 factores de transcripción de ocho familias estructurales y encuentra que cortes controlados en la cadena principal del ADN pueden cambiar el reconocimiento de sitios de unión sin alterar la identidad de las bases.
- **Tendencia:** sin señal directa en Trends México.
- **Relevancia científica:** reconocimiento molecular y efecto de la mecánica del ADN sobre regulación genética.
- **Oportunidad editorial:** “el ADN no solo se lee por letras; también importa su tensión”.
- **Público/ocasión:** público general interesado en biología; requiere una metáfora visual precisa.
- **Riesgos:** no traducir el resultado a enfermedad o tratamiento; distinguir el ensayo experimental de un resultado clínico.
- **Verificación:** resultado editorial con metadatos y abstract; la página directa y Crossref/resolvedor no completaron acceso. DOI pendiente.

### 4. Genómica poblacional de abalones del Pacífico occidental

- **Estudio:** Hirase, Shotaro; Fujii, Toyonobu; Sekino, Masashi; Hara, Motoyuki; Kikuchi, Kiyoshi. “Population genomic evidence of northern and southern subspecies of western Pacific abalones.” *Heredity* (2026), publicado 18-11-2026.
- **DOI mostrado por la editorial:** 10.1038/s41437-026-00895-w. **Estado:** PENDIENTE_RESOLVEDOR / PENDIENTE_CONTENIDO.
- **URL editorial:** https://www.nature.com/articles/s41437-026-00895-w
- **Novedad observada:** el título y el resumen indexado presentan evidencia genómica para subdivisiones norte/sur de abalones del Pacífico occidental.
- **Tendencia:** sin señal directa en Trends México.
- **Relevancia científica:** estructura poblacional y biogeografía marina.
- **Oportunidad editorial:** explicar cómo la genómica puede revelar poblaciones diferenciadas dentro de especies comercialmente conocidas.
- **Público/ocasión:** público interesado en animales marinos y conservación.
- **Riesgos:** el resumen accesible fue parcial; no afirmar adaptación local, límites taxonómicos definitivos ni consecuencias de conservación sin revisar métodos y resultados completos.
- **Verificación:** página editorial directa no accesible desde esta ejecución; DOI pendiente.

### 5. Hidrólisis de GTP por Ras sin agua nucleofílica estabilizada

- **Estudio:** Kawamura, Takashi; Fujimoto-Sakisaka, Wakako; Makino, Yoshiteru; Matsumoto, Shigeyuki; Ohyama, Tatsuya; Yoshikawa, Yoko; Watanabe, Chiduru et al. “GTP hydrolysis by Ras proceeds without a stabilized nucleophilic water molecule.” *Nature Communications* 17, 11533 (2026), publicado 18-11-2026.
- **DOI mostrado por la editorial:** 10.1038/s41467-026-79248-4. **Estado:** PENDIENTE_RESOLVEDOR.
- **URL editorial:** https://www.nature.com/articles/s41467-026-79248-4
- **Novedad observada:** cristalografía temporal con GTP fotoactivable sugiere que Ras puede pasar de un estado conformacional a GDP sin estabilizar previamente una molécula de agua nucleofílica.
- **Tendencia:** sin señal directa en Trends México.
- **Relevancia científica:** mecanismo molecular de señalización celular.
- **Oportunidad editorial:** mostrar que una reacción bioquímica puede seguir una ruta distinta de la explicación clásica.
- **Público/ocasión:** público general interesado en biología molecular; alto costo de explicación.
- **Riesgos:** resultados estructurales/cristalográficos con GTP fotoactivable; no convertirlos en afirmaciones sobre tratamientos o cáncer.
- **Verificación:** abstract indexado con resultados; página editorial directa y Crossref/resolvedor no completaron acceso. DOI pendiente.

## Google Trends México

- **RSS:** https://trends.google.com/trending/rss?geo=MX — el lector web devolvió “URL is not accessible via this tool”; no se parseó XML.
- **Respaldo oficial:** Trending Now México, https://trends.google.com/trending?geo=MX&hl=es-419, consulta 08:03 CDMX. La página mostró **222 tendencias** y el rango 1–25 de 222.
- **Observado:** predominio de deportes, entretenimiento y conversación pública. Entre señales ambientales aparecieron “inundaciones en Veracruz” (100 mil+) y “ciclón extratropical” (5 mil+).
- **Interpretación:** hay atención coyuntural a fenómenos meteorológicos, pero no una tendencia inequívoca sobre Kuroshio, la Corriente del Golfo, respiraderos hidrotermales, ADN, abalones o Ras. No se fuerza relación entre tendencias y los artículos.

## RSS científicos: fallos de lectura

Se intentó consultar por HTTP los diez feeds científicos declarados en `scripts/tendencias.py` y el RSS de Google Trends México. La resolución DNS falló antes de recibir respuesta HTTP; **no se descargó ni se parseó XML**. Los errores exactos de `curl -I --max-time 6` fueron:

- ScienceDaily Top Science: `curl: (6) Could not resolve host: www.sciencedaily.com`.
- ScienceDaily Health: `curl: (6) Could not resolve host: www.sciencedaily.com`.
- ScienceDaily Space & Time: `curl: (6) Could not resolve host: www.sciencedaily.com`.
- Phys.org: `curl: (6) Could not resolve host: phys.org`.
- NASA News Release: `curl: (6) Could not resolve host: www.nasa.gov`.
- ESA Space Science: `curl: (6) Could not resolve host: www.esa.int`.
- Nature RSS: `curl: (6) Could not resolve host: www.nature.com`.
- EurekAlert: `curl: (6) Could not resolve host: www.eurekalert.org`.
- Agencia SINC: `curl: (6) Could not resolve host: www.agenciasinc.es`.
- UNAM Global: `curl: (6) Could not resolve host: unamglobal.unam.mx`.
- Google Trends RSS México: `curl: (6) Could not resolve host: trends.google.com`.

El fallo es de resolución DNS del entorno de ejecución y no demuestra que los servidores de origen estén caídos. Como respaldo, se consultó Trending Now oficial de México; no se inventaron titulares procedentes de RSS.
## Observado, cálculo, inferencia y recomendación

- **Observado:** el artículo de Kuroshio presenta un resultado de modelación, las condiciones del experimento y los límites de resolución; la página editorial es accesible y contiene la fecha y el DOI.
- **Cálculo:** el storyboard conserva las cifras 13% y 4% tal como aparecen en el estudio; no calcula porcentajes nuevos ni extrapola al calentamiento global.
- **Inferencia editorial:** la “conexión por la atmósfera” es el giro más comprensible; no significa que el agua cruce de un océano al otro.
- **Recomendación:** usar Kuroshio para el slot 17:00. Mantener hydrothermal vents como candidato de 23:30 en PENDING_SOURCE hasta resolver DOI/URL y recuperar el texto primario.

## Seguimiento técnico: Meta y Google Trends

Se compararon las páginas oficiales y changelogs con `docs/INVESTIGACION_API_META_Y_GOOGLE_TRENDS.md`:

- Graph API: el overview y Page Insights siguen mostrando referencias a v27.0, mientras la tabla de versiones todavía identifica v26.0. Esta discrepancia ya está documentada en el informe técnico; no es un cambio nuevo de esta ejecución.
- Instagram Insights: no se encontró un cambio nuevo de métricas de Insights. El changelog de Instagram Messaging del 28-10-2026 no es un cambio de Insights y no se mezcla con esa API.
- Facebook Pages Insights: continúan las restricciones y deprecaciones de métricas ya registradas; no se encontró un cambio nuevo sustentado.
- Google Trends API: continúa en alfa limitada; no se identificó cambio oficial que altere la conclusión vigente.
- **Acción:** no reescribir `docs/INVESTIGACION_API_META_Y_GOOGLE_TRENDS.md`. No se modificaron conectores, credenciales ni integraciones.

## QA preexistente — lectura de solo lectura

Se inspeccionaron **160 storyboard.json físicos preexistentes** en `proyectos/`, `salidas/`, `cola/entrada/` y `cola/bloqueados/`. Las copias repetidas se conservan por ruta; no se consolidaron ni modificaron.

- 39 archivos contienen `narrative_qa`: **17 PASS, 20 FAIL, 2 PENDIENTE**.
- 121 archivos no contienen `narrative_qa`: cada uno queda como **PENDIENTE_AUDITOR**.
- El valor común de `review_basis` en los 39 registros existentes es `lectura_en_frio_solo_narracion`.
- Para los registros con fecha de revisión ausente en el JSON, `reviewed_at` se omite; no se inventa. Los dos objetos PENDIENTE tampoco contienen score, checks ni critical_flags, por lo que esos campos no se completan artificialmente.
- El storyboard nuevo de Kuroshio queda **PENDIENTE_AUDITOR**; no se añadió `narrative_qa`, no se hizo lectura de QA en frío, no se promovió a cola.

### Registros existentes que sí contienen narrative_qa

Los siguientes objetos reproducen status, score, review_basis, reviewed_at (si existe), los siete checks y critical_flags leídos de cada JSON. Orden de checks: pregunta_central_reconstruible; apertura_in_medias_res; progresion_por_escena; transiciones_causales; giro_cientifico_explicado; limite_evidencia_explicito; payoff_cierre_apertura.

~~~json
{"path":"cola/bloqueados/2026-11-01_llorar-cebolla-quimica/storyboard.json","project_id":"2026-11-01_llorar-cebolla-quimica","narrative_qa":{"status":"FAIL","review_basis":"lectura_en_frio_solo_narracion","score":79,"reviewed_at":"2026-11-01T15:09:29-06:00","checks":{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":false,"payoff_cierre_apertura":false},"critical_flags":["CIERRE_ATRIBUYE_INTENCION_EVOLUTIVA_NO_DEMOSTRADA","LIMITE_DE_EVIDENCIA_NO_EXPLICITO"]}}
{"path":"cola/bloqueados/2026-11-01_pulpo-tres-corazones/storyboard.json","project_id":"2026-11-01_pulpo-tres-corazones","narrative_qa":{"status":"FAIL","review_basis":"lectura_en_frio_solo_narracion","score":72,"reviewed_at":"2026-11-01T15:09:29-06:00","checks":{"pregunta_central_reconstruible":true,"apertura_in_medias_res":false,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":false,"payoff_cierre_apertura":true},"critical_flags":["APERTURA_HIPOTETICA_NO_IN_MEDIAS_RES","ANALOGIA_BRANQUIAS_SACAR_AIRE_DEL_AGUA_IMPRECISA","AFIRMACION_CORAZONES_NO_SUSTITUIBLES_SIN_RESPALDO"]}}
{"path":"cola/bloqueados/2026-11-02_camaron-mantis/storyboard.json","project_id":"2026-11-02_camaron-mantis","narrative_qa":{"status":"PASS","review_basis":"lectura_en_frio_solo_narracion","score":90,"checks":{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true},"critical_flags":[]}}
{"path":"cola/bloqueados/2026-11-02_comida-pan-duro/storyboard.json","project_id":"2026-11-02_comida-pan-duro","narrative_qa":{"status":"FAIL","review_basis":"lectura_en_frio_solo_narracion","score":84,"checks":{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true},"critical_flags":["CIERRE_SOBREAFIRMA_Y_CONTRADICE_LIMITE_DE_SECADO"]}}
{"path":"cola/bloqueados/2026-11-15_dato-dia-diapausa-lestes-sponsa/storyboard.json","project_id":"2026-11-15_dato-dia-diapausa-lestes-sponsa","narrative_qa":{"status":"PASS","review_basis":"lectura_en_frio_solo_narracion","score":90,"reviewed_at":"2026-11-15T15:51:23-06:00","checks":{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true},"critical_flags":[]}}
{"path":"cola/entrada/2026-11-09_dato-robot-ensambla-orbita/storyboard.json","project_id":"2026-11-09_dato-robot-ensambla-orbita","narrative_qa":{"status":"PASS","review_basis":"lectura_en_frio_solo_narracion","score":90,"reviewed_at":"2026-11-09T18:45:00-06:00","checks":{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true},"critical_flags":[]}}
{"path":"proyectos/2026-10-31_murcielagos-viroma-global/storyboard.json","project_id":"2026-10-31_murcielagos-viroma-global","narrative_qa":{"status":"FAIL","review_basis":"lectura_en_frio_solo_narracion","score":72,"checks":{"pregunta_central_reconstruible":true,"apertura_in_medias_res":false,"progresion_por_escena":true,"transiciones_causales":false,"giro_cientifico_explicado":false,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true},"critical_flags":["APERTURA_ESTATICA_Y_ESCENARIO_NO_DOCUMENTADO","TRANSICIONES_GENERICAS","CIFRA_300000_SIN_UNIDAD_DE_ANALISIS","GIRO_COMPARATIVO_NO_EXPLICADO"]}}
{"path":"proyectos/2026-10-31_sequias-energia-renovable/storyboard.json","project_id":"2026-10-31_sequias-energia-renovable","narrative_qa":{"status":"FAIL","review_basis":"lectura_en_frio_solo_narracion","score":56,"checks":{"pregunta_central_reconstruible":true,"apertura_in_medias_res":false,"progresion_por_escena":false,"transiciones_causales":false,"giro_cientifico_explicado":false,"limite_evidencia_explicito":true,"payoff_cierre_apertura":false},"critical_flags":["GANCHO_DEFINICIONAL","CIFRAS_SIN_DIRECCION_INTERPRETABLE","GIRO_SOLO_NOMBRADO","PAYOFF_NO_DERIVADO_DE_LA_EVIDENCIA"]}}
{"path":"proyectos/2026-11-01_dato-cambio-horario-corazon/storyboard.json","project_id":"2026-11-01_dato-cambio-horario-corazon","narrative_qa":{"status":"FAIL","review_basis":"lectura_en_frio_solo_narracion","score":84,"reviewed_at":"2026-11-01T18:08:00-06:00","checks":{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true},"critical_flags":["CIERRE_PRESELLO_INFERIOR_A_110_CARACTERES"]}}
{"path":"proyectos/2026-11-01_llorar-cebolla-quimica/storyboard.json","project_id":"2026-11-01_llorar-cebolla-quimica","narrative_qa":{"status":"FAIL","review_basis":"lectura_en_frio_solo_narracion","score":79,"reviewed_at":"2026-11-01T15:09:29-06:00","checks":{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":false,"payoff_cierre_apertura":false},"critical_flags":["CIERRE_ATRIBUYE_INTENCION_EVOLUTIVA_NO_DEMOSTRADA","LIMITE_DE_EVIDENCIA_NO_EXPLICITO"]}}
{"path":"proyectos/2026-11-01_pulpo-tres-corazones/storyboard.json","project_id":"2026-11-01_pulpo-tres-corazones","narrative_qa":{"status":"FAIL","review_basis":"lectura_en_frio_solo_narracion","score":72,"reviewed_at":"2026-11-01T15:09:29-06:00","checks":{"pregunta_central_reconstruible":true,"apertura_in_medias_res":false,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":false,"payoff_cierre_apertura":true},"critical_flags":["APERTURA_HIPOTETICA_NO_IN_MEDIAS_RES","ANALOGIA_BRANQUIAS_SACAR_AIRE_DEL_AGUA_IMPRECISA","AFIRMACION_CORAZONES_NO_SUSTITUIBLES_SIN_RESPALDO"]}}
{"path":"proyectos/2026-11-01_red-electrica-pulso-minuto/storyboard.json","project_id":"2026-11-01_red-electrica-pulso-minuto","narrative_qa":{"status":"PASS","review_basis":"lectura_en_frio_solo_narracion","score":89,"reviewed_at":"2026-11-01T15:09:29-06:00","checks":{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true},"critical_flags":[]}}
{"path":"proyectos/2026-11-02_camaron-mantis/storyboard.json","project_id":"2026-11-02_camaron-mantis","narrative_qa":{"status":"PASS","review_basis":"lectura_en_frio_solo_narracion","score":90,"checks":{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true},"critical_flags":[]}}
{"path":"proyectos/2026-11-02_comida-pan-duro/storyboard.json","project_id":"2026-11-02_comida-pan-duro","narrative_qa":{"status":"FAIL","review_basis":"lectura_en_frio_solo_narracion","score":84,"checks":{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true},"critical_flags":["CIERRE_SOBREAFIRMA_Y_CONTRADICE_LIMITE_DE_SECADO"]}}
{"path":"proyectos/2026-11-04_cielo-azul-atardecer-rojo/storyboard.json","project_id":"2026-11-04_cielo-azul-atardecer-rojo","narrative_qa":{"status":"PASS","review_basis":"lectura_en_frio_solo_narracion","score":94,"reviewed_at":"2026-11-04T15:58:40-06:00","checks":{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true},"critical_flags":[]}}
{"path":"proyectos/2026-11-04_dato-polvo-atrapa-oro/storyboard.json","project_id":"2026-11-04_dato-polvo-atrapa-oro","narrative_qa":{"status":"PENDIENTE","review_basis":"lectura_en_frio_solo_narracion"}}
{"path":"proyectos/2026-11-05_comida-palomitas/storyboard.json","project_id":"2026-11-05_comida-palomitas","narrative_qa":{"status":"FAIL","review_basis":"lectura_en_frio_solo_narracion","score":82,"reviewed_at":"2026-11-17T15:35:22-06:00","checks":{"pregunta_central_reconstruible":true,"apertura_in_medias_res":false,"progresion_por_escena":false,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true},"critical_flags":["APERTURA_DEFINICIONAL_NO_IN_MEDIAS_RES","ESCENA_6_REITERA_CAUSAS_DE_GRANOS_NO_REVENTADOS_SIN_INFORMACION_NUEVA"]}}
{"path":"proyectos/2026-11-05_inter-arboles-se-comunican/storyboard.json","project_id":"2026-11-05_inter-arboles-se-comunican","narrative_qa":{"status":"FAIL","review_basis":"lectura_en_frio_solo_narracion","score":78,"reviewed_at":"2026-11-17T15:35:22-06:00","checks":{"pregunta_central_reconstruible":true,"apertura_in_medias_res":false,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true},"critical_flags":["APERTURA_GENERICA_NO_IN_MEDIAS_RES"]}}
{"path":"proyectos/2026-11-05_inter-rayo-globular/storyboard.json","project_id":"2026-11-05_inter-rayo-globular","narrative_qa":{"status":"FAIL","review_basis":"lectura_en_frio_solo_narracion","score":81,"reviewed_at":"2026-11-17T15:35:22-06:00","checks":{"pregunta_central_reconstruible":true,"apertura_in_medias_res":false,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true},"critical_flags":["APERTURA_HISTORICA_DESCRIPTIVA_NO_IN_MEDIAS_RES"]}}
{"path":"proyectos/2026-11-05_kids-dia-en-venus/storyboard.json","project_id":"2026-11-05_kids-dia-en-venus","narrative_qa":{"status":"PASS","review_basis":"lectura_en_frio_solo_narracion","score":88,"reviewed_at":"2026-11-17T15:35:22-06:00","checks":{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true},"critical_flags":[]}}
{"path":"proyectos/2026-11-06_comida-aguacate-negro/storyboard.json","project_id":"2026-11-06_comida-aguacate-negro","narrative_qa":{"status":"FAIL","review_basis":"lectura_en_frio_solo_narracion","score":79,"reviewed_at":"2026-11-17T15:35:22-06:00","checks":{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":false,"transiciones_causales":false,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true},"critical_flags":["REPETICION_ESCENAS_5_6_SIN_AVANCE_CAUSAL"]}}
{"path":"proyectos/2026-11-06_inter-arena-cantante/storyboard.json","project_id":"2026-11-06_inter-arena-cantante","narrative_qa":{"status":"PASS","review_basis":"lectura_en_frio_solo_narracion","score":94,"reviewed_at":"2026-11-17T15:35:22-06:00","checks":{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true},"critical_flags":[]}}
{"path":"proyectos/2026-11-06_inter-ranas-congeladas/storyboard.json","project_id":"2026-11-06_inter-ranas-congeladas","narrative_qa":{"status":"FAIL","review_basis":"lectura_en_frio_solo_narracion","score":83,"reviewed_at":"2026-11-17T15:35:22-06:00","checks":{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":false,"transiciones_causales":false,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true},"critical_flags":["REPETICION_ESCENAS_5_6_LIMITES_DE_ESPECIE_Y_CONDICIONES"]}}
{"path":"proyectos/2026-11-06_kids-ballena-azul-corazon/storyboard.json","project_id":"2026-11-06_kids-ballena-azul-corazon","narrative_qa":{"status":"FAIL","review_basis":"lectura_en_frio_solo_narracion","score":80,"reviewed_at":"2026-11-17T15:35:22-06:00","checks":{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":false},"critical_flags":["PAYOFF_SOBREAFIRMA_CASI_SE_DETIENE"]}}
{"path":"proyectos/2026-11-07_comida-hielo-caliente/storyboard.json","project_id":"2026-11-07_comida-hielo-caliente","narrative_qa":{"status":"FAIL","review_basis":"lectura_en_frio_solo_narracion","score":81,"reviewed_at":"2026-11-17T15:35:22-06:00","checks":{"pregunta_central_reconstruible":true,"apertura_in_medias_res":false,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true},"critical_flags":["APERTURA_DE_CREENCIAS_NO_IN_MEDIAS_RES"]}}
{"path":"proyectos/2026-11-07_inter-nubes-pesan/storyboard.json","project_id":"2026-11-07_inter-nubes-pesan","narrative_qa":{"status":"FAIL","review_basis":"lectura_en_frio_solo_narracion","score":78,"reviewed_at":"2026-11-17T15:35:22-06:00","checks":{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":false,"transiciones_causales":false,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":false},"critical_flags":["ESCENA_7_REITERA_CIFRA_Y_LIMITE_SIN_PAYOFF_DE_SUSPENSION"]}}
{"path":"proyectos/2026-11-07_inter-pulpo-suenos/storyboard.json","project_id":"2026-11-07_inter-pulpo-suenos","narrative_qa":{"status":"FAIL","review_basis":"lectura_en_frio_solo_narracion","score":72,"reviewed_at":"2026-11-17T15:35:22-06:00","checks":{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":false,"transiciones_causales":false,"giro_cientifico_explicado":false,"limite_evidencia_explicito":false,"payoff_cierre_apertura":false},"critical_flags":["FUENTE_PRIMARIA_CORRESPONDE_A_OCTOPUS_LAQUEUS_NO_INSULARIS","REPETICION_ESCENAS_5_6_Y_PAYOFF_VAGO"]}}
{"path":"proyectos/2026-11-07_kids-huesos-bebe/storyboard.json","project_id":"2026-11-07_kids-huesos-bebe","narrative_qa":{"status":"FAIL","review_basis":"lectura_en_frio_solo_narracion","score":82,"reviewed_at":"2026-11-17T15:35:22-06:00","checks":{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":false,"transiciones_causales":false,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true},"critical_flags":["ESCENA_6_REPITE_VARIACION_DE_CONTEO_Y_FUSION"]}}
{"path":"proyectos/2026-11-09_dato-robot-ensambla-orbita/storyboard.json","project_id":"2026-11-09_dato-robot-ensambla-orbita","narrative_qa":{"status":"PASS","review_basis":"lectura_en_frio_solo_narracion","score":90,"reviewed_at":"2026-11-09T18:45:00-06:00","checks":{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true},"critical_flags":[]}}
{"path":"proyectos/2026-11-10_comida-aprendizaje-sabor-nutriente/storyboard.json","project_id":"2026-11-10_comida-aprendizaje-sabor-nutriente","narrative_qa":{"status":"PASS","review_basis":"lectura_en_frio_solo_narracion","score":92,"reviewed_at":"2026-11-10T15:47:50-06:00","checks":{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true},"critical_flags":[]}}
{"path":"proyectos/2026-11-10_dato-adn-sincroniza-flujo/storyboard.json","project_id":"2026-11-10_dato-adn-sincroniza-flujo","narrative_qa":{"status":"PASS","review_basis":"lectura_en_frio_solo_narracion","score":91,"reviewed_at":"2026-11-10T16:16:00-06:00","checks":{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true},"critical_flags":[]}}
{"path":"proyectos/2026-11-12_dato-pedorreta-chimpances/storyboard.json","project_id":"2026-11-12_dato-pedorreta-chimpances","narrative_qa":{"status":"PASS","review_basis":"lectura_en_frio_solo_narracion","score":91,"reviewed_at":"2026-11-12T15:38:50-06:00","checks":{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true},"critical_flags":[]}}
{"path":"proyectos/2026-11-13_dato-caracol-16-embriones/storyboard.json","project_id":"2026-11-13_dato-caracol-16-embriones","narrative_qa":{"status":"PASS","review_basis":"lectura_en_frio_solo_narracion","score":91,"reviewed_at":"2026-11-13T15:42:39-06:00","checks":{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true},"critical_flags":[]}}
{"path":"proyectos/2026-11-14_dato-microplasticos-pantanal/storyboard.json","project_id":"2026-11-14_dato-microplasticos-pantanal","narrative_qa":{"status":"PASS","review_basis":"lectura_en_frio_solo_narracion","score":88,"reviewed_at":"2026-11-14T15:04:13-06:00","checks":{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true},"critical_flags":[]}}
{"path":"proyectos/2026-11-15_dato-dia-diapausa-lestes-sponsa/storyboard.json","project_id":"2026-11-15_dato-dia-diapausa-lestes-sponsa","narrative_qa":{"status":"PASS","review_basis":"lectura_en_frio_solo_narracion","score":90,"reviewed_at":"2026-11-15T15:51:23-06:00","checks":{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true},"critical_flags":[]}}
{"path":"proyectos/2026-11-15_dato-quasar-pareja-cosmic-dawn/storyboard.json","project_id":"2026-11-15_dato-quasar-pareja-cosmic-dawn","narrative_qa":{"status":"FAIL","review_basis":"lectura_en_frio_solo_narracion","score":82,"reviewed_at":"2026-11-15T15:51:23-06:00","checks":{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":false,"transiciones_causales":false,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true},"critical_flags":["ESCENA_002_REITERA_GEMINI_NORTH_Y_NO_AVANZA_LA_PREGUNTA","TRANSICION_002_003_NO_CAUSAL"]}}
{"path":"proyectos/2026-11-16_dato-polen-desenreda-nanotubos/storyboard.json","project_id":"2026-11-16_dato-polen-desenreda-nanotubos","narrative_qa":{"status":"PASS","review_basis":"lectura_en_frio_solo_narracion","score":91,"reviewed_at":"2026-11-16T15:45:46-06:00","checks":{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true},"critical_flags":[]}}
{"path":"proyectos/2026-11-17_dato-suelo-dos-relojes/storyboard.json","project_id":"2026-11-17_dato-suelo-dos-relojes","narrative_qa":{"status":"PASS","review_basis":"lectura_en_frio_solo_narracion","score":89,"reviewed_at":"2026-11-17T15:35:22-06:00","checks":{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true},"critical_flags":[]}}
{"path":"salidas/2026-11-04_dato-polvo-atrapa-oro/storyboard.json","project_id":"2026-11-04_dato-polvo-atrapa-oro","narrative_qa":{"status":"PENDIENTE","review_basis":"lectura_en_frio_solo_narracion"}}
~~~

### Sin narrative_qa — PENDIENTE_AUDITOR

- `cola/bloqueados/2026-10-25_corales-contacto/storyboard.json` — PENDIENTE_AUDITOR
- `cola/bloqueados/2026-10-26_baffin-bay-ice-shelf/storyboard.json` — PENDIENTE_AUDITOR
- `cola/bloqueados/2026-10-27_corneja-decision-rapida/storyboard.json` — PENDIENTE_AUDITOR
- `cola/bloqueados/2026-10-28_mosquito-fruitless-audicion/storyboard.json` — PENDIENTE_AUDITOR
- `cola/bloqueados/2026-10-29_juno-choque-proa/storyboard.json` — PENDIENTE_AUDITOR
- `cola/bloqueados/2026-11-03_comida-maillard/storyboard.json` — PENDIENTE_AUDITOR
- `cola/bloqueados/2026-11-03_enzimas-incrustadas-oceano/storyboard.json` — PENDIENTE_AUDITOR
- `cola/bloqueados/2026-11-03_kids-tiburon-groenlandia/storyboard.json` — PENDIENTE_AUDITOR
- `cola/bloqueados/2026-11-04_comida-miel-no-caduca/storyboard.json` — PENDIENTE_AUDITOR
- `cola/bloqueados/2026-11-04_inter-bioluminiscencia-mar/storyboard.json` — PENDIENTE_AUDITOR
- `cola/bloqueados/2026-11-04_kids-hipo-por-que/storyboard.json` — PENDIENTE_AUDITOR
- `cola/bloqueados/2026-11-05_comida-palomitas-explotan/storyboard.json` — PENDIENTE_AUDITOR
- `cola/bloqueados/2026-11-05_inter-arboles-mito-respiran/storyboard.json` — PENDIENTE_AUDITOR
- `cola/bloqueados/2026-11-05_inter-venus-dia-largo/storyboard.json` — PENDIENTE_AUDITOR
- `cola/bloqueados/2026-11-06_comida-aguacate-negro/storyboard.json` — PENDIENTE_AUDITOR
- `cola/bloqueados/2026-11-06_inter-corazon-ballena-azul/storyboard.json` — PENDIENTE_AUDITOR
- `cola/bloqueados/2026-11-06_inter-ranas-congeladas/storyboard.json` — PENDIENTE_AUDITOR
- `cola/bloqueados/2026-11-07_extra-nubes-pesan/storyboard.json` — PENDIENTE_AUDITOR
- `cola/bloqueados/2026-11-07_inter-mpemba-mito/storyboard.json` — PENDIENTE_AUDITOR
- `cola/bloqueados/2026-11-07_inter-suenos-pulpo/storyboard.json` — PENDIENTE_AUDITOR
- `cola/bloqueados/2026-11-07_kids-huesos-bebe/storyboard.json` — PENDIENTE_AUDITOR
- `cola/bloqueados/2026-11-11_dato-ratas-topo-damaraland/storyboard.json` — PENDIENTE_AUDITOR
- `cola/entrada/2026-11-07_dato-clavo-te-cocina/storyboard.json` — PENDIENTE_AUDITOR
- `proyectos/2026-10-24_abejas-bullying/storyboard.json` — PENDIENTE_AUDITOR
- `proyectos/2026-10-24_ideonella-pet/storyboard.json` — PENDIENTE_AUDITOR
- `proyectos/2026-10-24_osedax-comehuesos/storyboard.json` — PENDIENTE_AUDITOR
- `proyectos/2026-10-24_serpientes-que-ruedan/storyboard.json` — PENDIENTE_AUDITOR
- `proyectos/2026-10-25_ave-jurasica-sin-vuelo/storyboard.json` — PENDIENTE_AUDITOR
- `proyectos/2026-10-25_corales-contacto/storyboard.json` — PENDIENTE_AUDITOR
- `proyectos/2026-10-25_reina-olor/storyboard.json` — PENDIENTE_AUDITOR
- `proyectos/2026-10-25_sueno-electricidad-qom/storyboard.json` — PENDIENTE_AUDITOR
- `proyectos/2026-10-26_baffin-bay-ice-shelf/storyboard.json` — PENDIENTE_AUDITOR
- `proyectos/2026-10-26_catrina-posada-monerismo/storyboard.json` — PENDIENTE_AUDITOR
- `proyectos/2026-10-26_hongo-gente-diminuta/storyboard.json` — PENDIENTE_AUDITOR
- `proyectos/2026-10-26_papel-picado-dia-muertos/storyboard.json` — PENDIENTE_AUDITOR
- `proyectos/2026-10-26_papel-picado-dia-muertos_parte2/storyboard.json` — PENDIENTE_AUDITOR
- `proyectos/2026-10-26_pimiento-verde-rojo/storyboard.json` — PENDIENTE_AUDITOR
- `proyectos/2026-10-27_cempasuchil-ciencia/storyboard.json` — PENDIENTE_AUDITOR
- `proyectos/2026-10-27_corneja-decision-rapida/storyboard.json` — PENDIENTE_AUDITOR
- `proyectos/2026-10-27_ddm-parte3-pomuch/storyboard.json` — PENDIENTE_AUDITOR
- `proyectos/2026-10-27_familia-ajolote/storyboard.json` — PENDIENTE_AUDITOR
- `proyectos/2026-10-27_kids-serpiente-voladora/storyboard.json` — PENDIENTE_AUDITOR
- `proyectos/2026-10-27_noct-anfibio-marino/storyboard.json` — PENDIENTE_AUDITOR
- `proyectos/2026-10-28_ddm-parte4-templo-mayor/storyboard.json` — PENDIENTE_AUDITOR
- `proyectos/2026-10-28_familia-voyager-disco-oro/storyboard.json` — PENDIENTE_AUDITOR
- `proyectos/2026-10-28_kids-titanoboa/storyboard.json` — PENDIENTE_AUDITOR
- `proyectos/2026-10-28_monarca-almas/storyboard.json` — PENDIENTE_AUDITOR
- `proyectos/2026-10-28_mosquito-fruitless-audicion/storyboard.json` — PENDIENTE_AUDITOR
- `proyectos/2026-10-28_noct-lince-milanos/storyboard.json` — PENDIENTE_AUDITOR
- `proyectos/2026-10-28_pan-de-muerto-huesos/storyboard.json` — PENDIENTE_AUDITOR
- `proyectos/2026-10-29_juno-choque-proa/storyboard.json` — PENDIENTE_AUDITOR
- `proyectos/2026-10-29_muralismo-cu/storyboard.json` — PENDIENTE_AUDITOR
- `proyectos/2026-10-30_arqueas-origen-eucariotas/storyboard.json` — PENDIENTE_AUDITOR
- `proyectos/2026-10-30_kromdraai-primera-fecha/storyboard.json` — PENDIENTE_AUDITOR
- `proyectos/2026-10-31_pardelas-jetlag-solar/storyboard.json` — PENDIENTE_AUDITOR
- `proyectos/2026-10-31_smartpe-edicion-plantas/storyboard.json` — PENDIENTE_AUDITOR
- `proyectos/2026-11-03_dato-polvo-africano-microbios/storyboard.json` — PENDIENTE_AUDITOR
- `proyectos/2026-11-03_kids-leche-enchilado/storyboard.json` — PENDIENTE_AUDITOR
- `proyectos/2026-11-xx_kids-flamencos-rosas_RESPALDO/storyboard.json` — PENDIENTE_AUDITOR
- `proyectos/demo-001/storyboard.json` — PENDIENTE_AUDITOR
- `proyectos/guiones_lote_01/storyboard.json` — PENDIENTE_AUDITOR
- `proyectos/lote01-01-el-nino/storyboard.json` — PENDIENTE_AUDITOR
- `proyectos/lote01-02-petroleo/storyboard.json` — PENDIENTE_AUDITOR
- `proyectos/lote01-03-balon-curva/storyboard.json` — PENDIENTE_AUDITOR
- `proyectos/lote01-04-tardigrado/storyboard.json` — PENDIENTE_AUDITOR
- `proyectos/lote01-05-chicxulub/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-10-24_2026-10-24-ideonella-pet/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-10-24_2026-10-24-osedax-comehuesos/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-10-24_2026-10-24-serpientes-que-ruedan/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-10-24_abejas-bullying/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-10-24_aves-temen-mas-a-mujeres/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-10-24_fenomeno-el-nino/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-10-24_ideonella-pet/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-10-24_lote01-04-tardigrado/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-10-24_lote01-05-chicxulub/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-10-25-reina-olor/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-10-25_2026-10-25-ave-jurasica-sin-vuelo.bak_v1/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-10-25_2026-10-25-ave-jurasica-sin-vuelo/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-10-25_2026-10-25-sueno-electricidad-qom/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-10-25_ave-jurasica-REMAKE/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-10-25_corales-contacto/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-10-26_2026-10-26-hongo-gente-diminuta/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-10-26_2026-10-26-pimiento-verde-rojo/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-10-26_baffin-bay-ice-shelf/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-10-26_catrina-posada-monerismo/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-10-26_papel-picado-dia-muertos/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-10-26_papel-picado-dia-muertos_parte2/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-10-27_cempasuchil-ciencia/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-10-27_corneja-decision-rapida/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-10-27_ddm-parte3-pomuch/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-10-27_familia-ajolote/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-10-27_kids-serpiente-voladora/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-10-27_noct-anfibio-marino/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-10-28_ddm-parte4-templo-mayor/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-10-28_familia-voyager-disco-oro/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-10-28_kids-titanoboa/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-10-28_monarca-almas/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-10-28_mosquito-fruitless-audicion/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-10-28_noct-lince-milanos/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-10-28_pan-de-muerto-huesos/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-10-29_juno-choque-proa/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-10-29_muralismo-cu/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-10-30_arqueas-origen-eucariotas/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-10-30_kromdraai-primera-fecha/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-10-31_murcielagos-viroma-global/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-10-31_pardelas-jetlag-solar/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-10-31_sequias-energia-renovable/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-10-31_smartpe-edicion-plantas/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-11-01_dato-xolo-mictlan/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-11-01_llorar-cebolla-quimica/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-11-01_pulpo-tres-corazones/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-11-02_camaron-mantis/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-11-02_comida-pan-duro/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-11-03_2026-11-03-kids-tiburon-groenlandia/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-11-03_comida-maillard/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-11-03_dato-polvo-africano-microbios/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-11-03_kids-leche-enchilado/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-11-03_kids-tiburon-groenlandia/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-11-04_comida-miel-no-caduca/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-11-04_inter-bioluminiscencia-mar/storyboard.json` — PENDIENTE_AUDITOR
- `salidas/2026-11-04_kids-hipo-por-que/storyboard.json` — PENDIENTE_AUDITOR

## Validación del storyboard nuevo

- Ruta: `proyectos/2026-11-18_dato-kuroshio-puente-atmosferico/storyboard.json`.
- Commit final del storyboard: `247a4e9d25b694c4f400d2e0037b5393814c24eb`.
- JSON releído desde GitHub y parseado.
- 8 escenas; 222 palabras de narración; 78 s de escenas + 6 s de cortinilla = 84 s.
- Gancho: 5 palabras; cierre exacto: “Esto fue Datos y ociosidades.”
- Arco: hook_medias_res → desarrollo → cierre_historia → reflexion_o_pregunta.
- Los seis campos de narrative_contract están completos.
- Todos los source_ids resuelven a SRC-001; el prompt_base literal de atlas_antiguo encabeza las ocho image_prompt.
- Mapa con las dos cajas de análisis publicadas en el artículo (35–45°N, 140–170°E y 35–45°N, 50–80°W); no se inventan estaciones ni trayectorias.
- Gráfico 13% vs 4% con variable, condiciones e interpretación explícitas.
- Voz: edge-tts es-MX-JorgeNeural, rate +7%, pitch -2Hz.
- approved_assets exactamente []; export.render_status exactamente NOT_GENERATED; no existe export.filename ni ruta de medios; publicacion.status exactamente PENDIENTE_DECISION_GROK; no existe narrative_qa.
- No se crearon frames, imágenes, audio, voz, video ni renders.

## Límites y seguridad

No se solicitaron ni registraron credenciales. No se modificaron `data/*.json`, `main`, workflows, motores canónicos ni Motor U6. No hubo merge, publicación, programación ni consumo de créditos. El auditor independiente conserva la decisión narrativa y Grok conserva selección editorial, generación audiovisual, QA oficial y publicación.
