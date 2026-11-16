# RADAR CAPCOT — 2026-11-16

Rama: `feature/capcot-video-discovery-continuity`  
Serie: **Datos y ociosidades**  
Consulta: **lunes 16 de noviembre de 2026, 08:15 CDMX** (America/Mexico_City).  
Alcance: investigación, documentación y staging textual; no generación de medios, no QA oficial, no publicación.

## Resultado operativo

- **Slot principal:** 17:00, libre en el repositorio y dentro de la ventana activa 16:30–18:00. El lunes no figura entre los días preferentes, pero no está excluido. Se creó un único borrador.
- **Slot 23:30 / dato_del_dia:** activo y libre. Hay un artículo publicado hoy sobre el genoma de la liebre italiana, pero la URL editorial directa devolvió `DisabledError` y Crossref/doi.org no fueron accesibles. Resultado **PENDING_SOURCE**; no se creó storyboard para 23:30.
- **07:00:** la ventana 06:30–07:30 ya había terminado al consultar. No se creó un paquete retrospectivo.
- **13:30:** ventana en prueba, no activa en la política vigente.
- **19:00:** retirado desde el ajuste del 9-nov.
- No existe `data/horario_2026-11-16.json` ni archivo de estado operativo del 16-nov. Se aplicó `data/horarios.json` actualizado el 9-nov y el contrato operativo. La búsqueda del árbol confirmó que no había proyecto, salida ni paquete de cola fechado 2026-11-16 antes de esta ejecución.

### Entregables aplicables

1. `proyectos/2026-11-16_dato-polen-desenreda-nanotubos/storyboard.json` — slot 17:00; commit final `8a31a8e131cd3d16ee6015d093134066f92582b9` (creación `37ea4181a72da5cac82c044189e3a8608f5ee570`).
2. `docs/briefs/2026-11-16_RADAR_CAPCOT.md` — este radar.

No se creó `*_fuentes.md`. El candidato 23:30 quedó `PENDING_SOURCE`; no se inventó ni se adelantó noticia.

## Candidatos científicos — ventana 10–16 nov

Todos están dentro de los últimos siete días. Para los DOI se intentó abrir el resolvedor `doi.org` y el endpoint de Crossref `api.crossref.org/works/{DOI}`; ambos devolvieron `URL is not accessible via this tool` para los cinco registros. **Ningún DOI se declara validado por Crossref o resolvedor.** Cuando se pudo, se contrastó el artículo o PDF primario del editor. Los estados distinguen acceso a la fuente editorial de resolución DOI.

### 1. Microgeles de polen de girasol para dispersar nanotubos — principal, 17:00

- **Autoría/año:** Changdan Gao, Di Yang, Jingwen Liang, Zongyu Wang, Mingyu Zhao, Ze Zhao y Hongbing Deng (2026).
- **Estudio:** *Sunflower pollen microgels enable sonication-free dispersion of carbon nanotubes for bio-based conductive inks*, *Nature Communications*.
- **Fecha editorial:** 14-nov-2026.
- **DOI:** `10.1038/s41467-026-79607-1` — **PENDIENTE_RESOLVEDOR**.
- **Fuente primaria:** [página editorial](https://www.nature.com/articles/s41467-026-79607-1) · [PDF editorial abierto](https://www.nature.com/articles/s41467-026-79607-1_reference.pdf).
- **Novedad observada:** microgeles de polen de girasol en estado granular nativo ayudan a deshacer agregados de nanotubos mediante captura-colisión-fricción con agitación suave; el alginato proporciona estabilización electrostática. La tinta PAC presenta tixotropía y alta viscoelasticidad, y se probó en extrusión 3D y serigrafía. El artículo reporta estabilidad acuosa superior a seis meses en su sistema experimental.
- **Tendencia:** Google Trends México no mostró señal inequívoca de ciencia o naturaleza en los primeros 25 resultados.
- **Relevancia científica:** alta; propone un dispersante natural y un proceso sin sonicación para tintas conductoras.
- **Oportunidad editorial:** muy alta; el giro visual es que el polen no conduce, sino que ayuda a dispersar el material que sí conduce.
- **Público/ocasión:** público general interesado en botánica, materiales, impresión y tecnología; ventana de tarde.
- **Riesgos:** no decir que el polen es conductor; no convertir “sin sonicación” en una afirmación de impacto ambiental total; la estabilidad de laboratorio no es vida útil comercial; no atribuir el resultado a una aplicación comercial ya desplegada.
- **Verificación:** **PDF primario abierto y contrastado; DOI PENDIENTE_RESOLVEDOR**.
- **Recomendación:** desarrollar el borrador de 17:00. El pin cartográfico representa una coordenada georreferenciada dentro de Wuhan University, afiliación institucional de los autores; no se presenta como sitio experimental.

### 2. Primer genoma de la liebre italiana — candidato 23:30, PENDING_SOURCE

- **Autoría/año:** Maria Buglione, Giovanni Scala, Eleonora Rivieccio, Gabriele de Filippo, Rosie Drinkwater, Sabatino Rosario Troisi y Domenico Fulgione (2026).
- **Estudio:** *The first genome of the Italian hare (Lepus corsicanus) and new insights into Lepus phylogenesis*, *Scientific Reports*.
- **Fecha editorial:** 16-nov-2026; cumple la fecha del slot.
- **DOI:** `10.1038/s41598-026-80066-3` — **PENDIENTE_RESOLVEDOR**.
- **Fuente primaria localizada:** [registro editorial de Scientific Reports](https://www.nature.com/articles/s41598-026-80066-3).
- **Novedad observada en el registro editorial:** primer ensamblaje de novo de alta calidad de la liebre italiana; la especie se describe como endémica mediterránea, restringida al centro y sur de Italia y Sicilia, introducida históricamente en Córcega y clasificada como Vulnerable. El resumen indica secuenciación Oxford Nanopore de lecturas largas y coensamblaje apoyado por una referencia existente.
- **Tendencia:** sin señal de ciencia/naturaleza en el top 25 de Trends México.
- **Relevancia científica:** alta para genética de conservación y filogenia.
- **Oportunidad editorial:** alta; “la liebre vulnerable recibe su primer genoma” permite una historia de herramienta científica y límite de conservación.
- **Público/ocasión:** público general interesado en fauna, biodiversidad y conservación; slot fijo 23:30.
- **Riesgos:** un genoma no equivale a recuperación poblacional; completitud del ensamblaje no mide abundancia; no presentar la filogenia preliminar como certeza final.
- **Verificación:** el resultado de búsqueda devolvió el registro editorial oficial con fecha, resumen y DOI, pero la apertura directa devolvió `DisabledError`; Crossref y doi.org no fueron accesibles. **PENDING_SOURCE** para 23:30.
- **Decisión:** no crear storyboard 23:30 hasta resolver URL/DOI mediante Crossref o resolvedor. No se adelanta ni se inventa una fuente.

### 3. Alelo de soya silvestre para entrenudos cortos y siembra densa

- **Autoría/año:** Li, H.; Chen, D.; Zhang, G. et al. (2026).
- **Estudio:** *Identification and deployment of a wild soybean FD allele for high-density planting and increased yield*, *Nature Communications*.
- **Fecha editorial:** 16-nov-2026.
- **DOI:** `10.1038/s41467-026-79322-x` — **PENDIENTE_RESOLVEDOR**.
- **Fuente primaria localizada:** [registro editorial](https://www.nature.com/articles/s41467-026-79322-x).
- **Novedad observada:** identifica el locus RIN2 y el factor de transcripción FDc1; el alelo de soya silvestre reduce elongación de entrenudos y se asocia con mayor rendimiento por planta y parcela en las ubicaciones de campo y densidades probadas.
- **Tendencia:** no se observa señal científica directa; el término no figura en el top 25 de Trends.
- **Relevancia científica:** alta para arquitectura vegetal y mejoramiento de cultivos.
- **Oportunidad editorial:** alta; una variante silvestre modifica la arquitectura de la planta.
- **Público/ocasión:** público interesado en alimentos, botánica y agricultura.
- **Riesgos:** no generalizar el aumento de rendimiento a todos los cultivares, densidades o ambientes; no simplificar la ruta RIN2–STF1/2–giberelinas.
- **Verificación:** el registro oficial de Nature muestra fecha, resumen y DOI; apertura directa redirigió a IDP/HTTP 500 y Crossref/doi.org no fueron accesibles. **PENDIENTE_RESOLVEDOR**.

### 4. Crecimiento radial y heterogeneidad estructural de los bosques

- **Autoría/año:** Yuan Yao, Shumiao Shu, Jian Feng, Hanying Hu, Wenzheng Yang, Ruixuan Liu, Xiaodan Wang y Sheng Zhang (2026).
- **Estudio:** *Global patterns of radial growth-structural heterogeneity relationships in forests*, *Nature Communications*.
- **Fecha editorial:** 14-nov-2026.
- **DOI:** `10.1038/s41467-026-79442-4` — **PENDIENTE_RESOLVEDOR**.
- **Fuente primaria:** [registro editorial](https://www.nature.com/articles/s41467-026-79442-4).
- **Novedad observada:** conjunto global de anillos de árboles con más de 900 sitios y más de 55,000 núcleos; la relación entre crecimiento y heterogeneidad cambia a lo largo del gradiente de estrés. En la meseta tibetana, condiciones más cálidas y húmedas se asocian con homogeneización estructural.
- **Tendencia:** sin señal inequívoca de bosques o dendrocronología en el top 25 de Trends.
- **Relevancia científica:** alta para ecología forestal y respuesta al clima.
- **Oportunidad editorial:** alta; los anillos permiten visualizar cómo el estrés ambiental se relaciona con la desigualdad de tamaños.
- **Público/ocasión:** público general interesado en naturaleza, clima y bosques.
- **Riesgos:** no convertir asociaciones y modelos de mediación en causalidad directa; no afirmar que todos los bosques se vuelven homogéneos con el calentamiento.
- **Verificación:** registro editorial primario consultado; DOI **PENDIENTE_RESOLVEDOR**.

### 5. Metamateriales de redes con escalas múltiples

- **Autoría/año:** Csaba Both, Andrew Yen-Jong Chen, Ting-Ting Gao, Niek Mooij, Mohammad Charara, Jayna Wadhwa, Carlos M. Portela y Albert-László Barabási (2026).
- **Estudio:** *Scale-rich network-based metamaterials*, *Nature* 659, 345–356.
- **Fecha editorial:** 11-nov-2026.
- **DOI:** `10.1038/s41586-026-11191-2` — **PENDIENTE_RESOLVEDOR**.
- **Fuente primaria:** [PDF editorial de Nature](https://www.nature.com/articles/s41586-026-11191-2.pdf) · [página editorial](https://www.nature.com/articles/s41586-026-11191-2).
- **Novedad observada:** propone una arquitectura de metamaterial mecánico con heterogeneidad de conexiones y longitudes a múltiples escalas, inspirada en redes naturales y tecnológicas; contrasta con materiales diseñados con celdas repetitivas homogéneas.
- **Tendencia:** sin señal inequívoca de metamateriales en Trends México.
- **Relevancia científica:** alta para física, materiales y diseño de redes.
- **Oportunidad editorial:** media-alta; visualmente puede explicarse la diferencia entre una malla repetitiva y una red multiescala.
- **Público/ocasión:** público curioso por física y tecnología.
- **Riesgos:** no prometer aplicaciones comerciales ni generalizar propiedades fuera de los prototipos y ensayos descritos.
- **Verificación:** PDF primario editorial consultado; DOI **PENDIENTE_RESOLVEDOR**.

## Google Trends México

- **RSS:** `https://trends.google.com/trending/rss?geo=MX` devolvió `URL is not accessible via this tool`; no se parseó XML.
- **Respaldo oficial:** [Google Trends — Trending Now México, últimas 24 horas](https://trends.google.com/trending?geo=mx). En los primeros 25 resultados visibles dominaron fútbol/deportes y entretenimiento: Jamaica–México (1M+), Portugal–Dinamarca (200K+), Lions–Patriots (20K+), América–Red Bull (20K+), además de vivienda, AO3, Tesla y noticias generales.
- **Lectura:** no se observó una señal clara de ciencia o naturaleza que explique los candidatos. No se atribuye popularidad a los artículos.

## RSS científicos — fallos exactos

Las URL son las definidas en `scripts/tendencias.py`. La herramienta no admitió los tipos MIME; **no se afirma haber leído ni parseado XML**.

| Feed | URL | Resultado |
|---|---|---|
| ScienceDaily Science | `https://www.sciencedaily.com/rss/top/science.xml` | HTTP 400 — Unsupported content-type: application/xml |
| ScienceDaily Health | `https://www.sciencedaily.com/rss/top/health.xml` | HTTP 400 — Unsupported content-type: application/xml |
| ScienceDaily Space | `https://www.sciencedaily.com/rss/space_time.xml` | HTTP 400 — Unsupported content-type: application/xml |
| Phys.org | `https://phys.org/rss-feed` | HTTP 400 — Unsupported content-type: text/xml |
| NASA News Releases | `https://www.nasa.gov/news-release/feed` | HTTP 400 — Unsupported content-type: application/rss+xml |
| ESA Space Science | `https://www.esa.int/rssfeed/Our_Activities/Space_Science` | HTTP 404 — Not Found |
| Nature | `https://www.nature.com/nature.rss` | HTTP 400 — Unsupported content-type: application/rss+xml |
| EurekAlert | `https://www.eurekalert.org/rss/news.xml` | URL is not accessible via this tool |
| Agencia SINC | `https://www.agenciasinc.es/rss` | URL is not accessible via this tool |
| UNAM Global | `https://unamglobal.unam.mx/feed` | HTTP 400 — Unsupported content-type: application/rss+xml |
| Google Trends RSS México | `https://trends.google.com/trending/rss?geo=MX` | URL is not accessible via this tool |

## Rotación, estructura y estilos

- Últimos storyboards existentes: 15-nov `van_gogh` + estructura `pregunta` (17:00) y `rubber_hose_1930s` + estructura `historia` (23:30); 14-nov `paper_rasgado_capas`; 13-nov `dibujo_cientifico_scratchboard`.
- Nuevo storyboard 17:00: `collage_cientifico_vintage`, prompt_base literal del catálogo, estructura `paradoja_mecanica`. No repite estilo ni estructura de los dos storyboards del 15-nov.
- La rotación se reconstruyó siguiendo `scripts/registro_editorial.py`: merge por `project_id`, prioridad de campos no vacíos y preservación de origen externo. `data/rotacion.json` y `data/publicaciones.json` no contienen registros posteriores al 8-nov; `data/temas_del_dia.json` no llega a 16-nov. No se modificó ningún `data/*.json`.

## QA preexistente — lectura de storyboards canónicos

Se revisaron los 174 archivos `storyboard.json` del árbol en `proyectos/`, `salidas/`, `cola/entrada/` y `cola/bloqueados/`. Se releyó el archivo canónico priorizando `proyectos/` y, cuando no existía, la copia disponible en las colas o salidas. Se encontraron **29 registros con `narrative_qa` (12 PASS, 17 FAIL)** y **61 entradas sin la clave: PENDIENTE_AUDITOR**, enumeradas abajo. `scripts/registro_editorial.py` se leyó y se usó como referencia para la consolidación por `project_id`; el script no se ejecutó porque esta conexión no ofrece runtime del repositorio, por lo que los 61 rótulos de la lista son identificadores/rutas leídos y no se afirma un conteo adicional de IDs únicos. No se ejecutó QA nuevo, no se escribió `narrative_qa`, no se interpretó `salidas/qa.json` como autorización y no se promovió ningún proyecto.

En los 29 registros, `review_basis` aparece exactamente como `lectura_en_frio_solo_narracion`. Los siete checks y `critical_flags` se reproducen tal como aparecen. `AUSENTE_EN_JSON` significa que el campo `reviewed_at` no existe en el objeto leído.

| project_id | status | score | review_basis | reviewed_at | checks | critical_flags |
|---|---:|---:|---|---|---|---|
| `2026-10-31_murcielagos-viroma-global` | FAIL | 72 | `lectura_en_frio_solo_narracion` | AUSENTE_EN_JSON | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":false,"progresion_por_escena":true,"transiciones_causales":false,"giro_cientifico_explicado":false,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `["APERTURA_ESTATICA_Y_ESCENARIO_NO_DOCUMENTADO","TRANSICIONES_GENERICAS","CIFRA_300000_SIN_UNIDAD_DE_ANALISIS","GIRO_COMPARATIVO_NO_EXPLICADO"]` |
| `2026-10-31_sequias-energia-renovable` | FAIL | 56 | `lectura_en_frio_solo_narracion` | AUSENTE_EN_JSON | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":false,"progresion_por_escena":false,"transiciones_causales":false,"giro_cientifico_explicado":false,"limite_evidencia_explicito":true,"payoff_cierre_apertura":false}` | `["GANCHO_DEFINICIONAL","CIFRAS_SIN_DIRECCION_INTERPRETABLE","GIRO_SOLO_NOMBRADO","PAYOFF_NO_DERIVADO_DE_LA_EVIDENCIA"]` |
| `2026-11-01_dato-cambio-horario-corazon` | FAIL | 84 | `lectura_en_frio_solo_narracion` | 2026-11-01T18:08:00-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `["CIERRE_PRESELLO_INFERIOR_A_110_CARACTERES"]` |
| `2026-11-01_llorar-cebolla-quimica` | FAIL | 79 | `lectura_en_frio_solo_narracion` | 2026-11-01T15:09:29-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":false,"payoff_cierre_apertura":false}` | `["CIERRE_ATRIBUYE_INTENCION_EVOLUTIVA_NO_DEMOSTRADA","LIMITE_DE_EVIDENCIA_NO_EXPLICITO"]` |
| `2026-11-01_pulpo-tres-corazones` | FAIL | 72 | `lectura_en_frio_solo_narracion` | 2026-11-01T15:09:29-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":false,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":false,"payoff_cierre_apertura":true}` | `["APERTURA_HIPOTETICA_NO_IN_MEDIAS_RES","ANALOGIA_BRANQUIAS_SACAR_AIRE_DEL_AGUA_IMPRECISA","AFIRMACION_CORAZONES_NO_SUSTITUIBLES_SIN_RESPALDO"]` |
| `2026-11-01_red-electrica-pulso-minuto` | PASS | 89 | `lectura_en_frio_solo_narracion` | 2026-11-01T15:09:29-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `[]` |
| `2026-11-02_camaron-mantis` | PASS | 90 | `lectura_en_frio_solo_narracion` | AUSENTE_EN_JSON | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `[]` |
| `2026-11-02_comida-pan-duro` | FAIL | 84 | `lectura_en_frio_solo_narracion` | AUSENTE_EN_JSON | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `["CIERRE_SOBREAFIRMA_Y_CONTRADICE_LIMITE_DE_SECADO"]` |
| `2026-11-04_cielo-azul-atardecer-rojo` | PASS | 94 | `lectura_en_frio_solo_narracion` | 2026-11-04T15:58:40-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `[]` |
| `2026-11-05_comida-palomitas` | FAIL | 82 | `lectura_en_frio_solo_narracion` | 2026-11-15T15:51:23-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":false,"progresion_por_escena":false,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `["APERTURA_DEFINICIONAL_NO_IN_MEDIAS_RES","ESCENA_6_REITERA_CAUSAS_DE_GRANOS_NO_REVENTADOS_SIN_INFORMACION_NUEVA"]` |
| `2026-11-05_inter-arboles-se-comunican` | FAIL | 78 | `lectura_en_frio_solo_narracion` | 2026-11-15T15:51:23-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":false,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `["APERTURA_GENERICA_NO_IN_MEDIAS_RES"]` |
| `2026-11-05_inter-rayo-globular` | FAIL | 81 | `lectura_en_frio_solo_narracion` | 2026-11-15T15:51:23-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":false,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `["APERTURA_HISTORICA_DESCRIPTIVA_NO_IN_MEDIAS_RES"]` |
| `2026-11-05_kids-dia-en-venus` | PASS | 88 | `lectura_en_frio_solo_narracion` | 2026-11-15T15:51:23-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `[]` |
| `2026-11-06_comida-aguacate-negro` | FAIL | 79 | `lectura_en_frio_solo_narracion` | 2026-11-15T15:51:23-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":false,"transiciones_causales":false,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `["REPETICION_ESCENAS_5_6_SIN_AVANCE_CAUSAL"]` |
| `2026-11-06_inter-arena-cantante` | PASS | 94 | `lectura_en_frio_solo_narracion` | 2026-11-15T15:51:23-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `[]` |
| `2026-11-06_inter-ranas-congeladas` | FAIL | 83 | `lectura_en_frio_solo_narracion` | 2026-11-15T15:51:23-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":false,"transiciones_causales":false,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `["REPETICION_ESCENAS_5_6_LIMITES_DE_ESPECIE_Y_CONDICIONES"]` |
| `2026-11-06_kids-ballena-azul-corazon` | FAIL | 80 | `lectura_en_frio_solo_narracion` | 2026-11-15T15:51:23-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":false}` | `["PAYOFF_SOBREAFIRMA_CASI_SE_DETIENE"]` |
| `2026-11-07_comida-hielo-caliente` | FAIL | 81 | `lectura_en_frio_solo_narracion` | 2026-11-15T15:51:23-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":false,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `["APERTURA_DE_CREENCIAS_NO_IN_MEDIAS_RES"]` |
| `2026-11-07_inter-nubes-pesan` | FAIL | 78 | `lectura_en_frio_solo_narracion` | 2026-11-15T15:51:23-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":false,"transiciones_causales":false,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":false}` | `["ESCENA_7_REITERA_CIFRA_Y_LIMITE_SIN_PAYOFF_DE_SUSPENSION"]` |
| `2026-11-07_inter-pulpo-suenos` | FAIL | 72 | `lectura_en_frio_solo_narracion` | 2026-11-15T15:51:23-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":false,"transiciones_causales":false,"giro_cientifico_explicado":false,"limite_evidencia_explicito":false,"payoff_cierre_apertura":false}` | `["FUENTE_PRIMARIA_CORRESPONDE_A_OCTOPUS_LAQUEUS_NO_INSULARIS","REPETICION_ESCENAS_5_6_Y_PAYOFF_VAGO"]` |
| `2026-11-07_kids-huesos-bebe` | FAIL | 82 | `lectura_en_frio_solo_narracion` | 2026-11-15T15:51:23-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":false,"transiciones_causales":false,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `["ESCENA_6_REPITE_VARIACION_DE_CONTEO_Y_FUSION"]` |
| `2026-11-09_dato-robot-ensambla-orbita` | PASS | 90 | `lectura_en_frio_solo_narracion` | 2026-11-09T18:45:00-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `[]` |
| `2026-11-10_comida-aprendizaje-sabor-nutriente` | PASS | 92 | `lectura_en_frio_solo_narracion` | 2026-11-10T15:47:50-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `[]` |
| `2026-11-10_dato-adn-sincroniza-flujo` | PASS | 91 | `lectura_en_frio_solo_narracion` | 2026-11-10T16:16:00-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `[]` |
| `2026-11-12_dato-pedorreta-chimpances` | PASS | 91 | `lectura_en_frio_solo_narracion` | 2026-11-12T15:38:50-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `[]` |
| `2026-11-13_dato-caracol-16-embriones` | PASS | 91 | `lectura_en_frio_solo_narracion` | 2026-11-13T15:42:39-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `[]` |
| `2026-11-14_dato-microplasticos-pantanal` | PASS | 88 | `lectura_en_frio_solo_narracion` | 2026-11-14T15:04:13-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `[]` |
| `2026-11-15_dato-dia-diapausa-lestes-sponsa` | PASS | 90 | `lectura_en_frio_solo_narracion` | 2026-11-15T15:51:23-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `[]` |
| `2026-11-15_dato-quasar-pareja-cosmic-dawn` | FAIL | 82 | `lectura_en_frio_solo_narracion` | 2026-11-15T15:51:23-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":false,"transiciones_causales":false,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `["ESCENA_002_REITERA_GEMINI_NORTH_Y_NO_AVANZA_LA_PREGUNTA","TRANSICION_002_003_NO_CAUSAL"]` |

### Proyectos sin narrative_qa — PENDIENTE_AUDITOR

`2026-10-24_abejas-bullying`, `2026-10-24_aves-temen-mas-a-mujeres`, `2026-10-24_fenomeno-el-nino`, `2026-10-24_ideonella-pet`, `2026-10-24_osedax-comehuesos`, `2026-10-24_serpientes-que-ruedan`, `2026-10-25_ave-jurasica-sin-vuelo`, `2026-10-25_corales-contacto`, `2026-10-25_reina-olor`, `2026-10-25_sueno-electricidad-qom`, `2026-10-26_baffin-bay-ice-shelf`, `2026-10-26_catrina-posada-monerismo`, `2026-10-26_hongo-gente-diminuta`, `2026-10-26_papel-picado-dia-muertos`, `2026-10-26_papel-picado-dia-muertos_parte2`, `2026-10-26_pimiento-verde-rojo`, `ddm-parte3-pomuch`, `2026-10-28_ddm-parte4-templo-mayor`, `2026-10-28_familia-voyager-disco-oro`, `2026-10-28_kids-titanoboa`, `2026-10-28_monarca-almas`, `2026-10-28_mosquito-fruitless-audicion`, `2026-10-28_noct-lince-milanos`, `2026-10-28_pan-de-muerto-huesos`, `2026-10-29_juno-choque-proa`, `2026-10-29_muralismo-cu`, `2026-10-30_arqueas-origen-eucariotas`, `2026-10-30_kromdraai-primera-fecha`, `2026-10-31_pardelas-jetlag-solar`, `2026-10-31_smartpe-edicion-plantas`, `2026-11-01_dato-xolo-mictlan`, `2026-11-03_comida-maillard`, `2026-11-03_dato-polvo-africano-microbios`, `2026-11-03_enzimas-incrustadas-oceano`, `2026-11-03_kids-leche-enchilado`, `2026-11-03_kids-tiburon-groenlandia`, `2026-11-04_comida-miel-no-caduca`, `2026-11-04_inter-bioluminiscencia-mar`, `2026-11-04_kids-hipo-por-que`, `2026-11-04_machu-picchu-fallas-pisa`, `2026-11-05_comida-palomitas-explotan`, `2026-11-05_inter-arboles-mito-respiran`, `2026-11-05_inter-venus-dia-largo`, `2026-11-06_inter-corazon-ballena-azul`, `2026-11-07_dato-clavo-te-cocina`, `2026-11-07_inter-mpemba-mito`, `2026-11-07_inter-suenos-pulpo`, `2026-11-11_dato-ratas-topo-damaraland`, `2026-11-xx_kids-flamencos-rosas`, `cempasuchil-ciencia`, `corneja-decision-rapida`, `demo-001`, `familia-ajolote`, `guiones_lote_01`, `kids-serpiente-voladora`, `lote01-01-el-nino`, `lote01-02-petroleo`, `lote01-03-balon-curva`, `lote01-04-tardigrado`, `lote01-05-chicxulub`, `noct-anfibio-marino`

El nuevo borrador `2026-11-16_dato-polen-desenreda-nanotubos` tampoco contiene `narrative_qa`: queda **PENDIENTE_AUDITOR**. La revisión en frío corresponde al auditor independiente.

## Seguimiento técnico Meta / Google

- El informe `docs/INVESTIGACION_API_META_Y_GOOGLE_TRENDS.md` ya registra la discrepancia entre el overview de Graph API que muestra v27.0 y la tabla de versiones que aún muestra v26.0. No apareció evidencia nueva que justifique reescribirlo.
- El changelog de Graph API, Page Insights y la documentación de Instagram Insights devolvieron HTTP 429 Too Many Requests; no se infieren cambios desde páginas inaccesibles.
- La página oficial [Google Trends API Alpha](https://developers.google.com/search/apis/trends) sigue indicando acceso temprano limitado a testers, ventana móvil de cinco años, agregación diaria/semanal/mensual/anual y datos consistentes escalados. No se observó un cambio nuevo del contrato alfa.
- Resultado: **sin actualización técnica**. El informe no se reescribió.

## Compuerta de staging — lectura previa a commit

- Proyecto principal: 8 escenas; 78 s de escenas + 6 s de cortinilla = 84 s; 196 palabras y 1,255 caracteres de narración; gancho de 4 palabras.
- Arco: `hook_medias_res → desarrollo → cierre_historia → reflexion_o_pregunta`.
- `narrative_contract`: seis campos no vacíos.
- `source_ids`: todos resuelven a `sources`; el mapa usa coordenadas georreferenciadas reales y declara que el pin es afiliación institucional, no sitio experimental.
- Capa de dato: `>6 meses`, con condiciones e interpretación de laboratorio.
- Voz: `edge-tts`, `es-MX-JorgeNeural`, rate `+7%`, pitch `-2Hz`.
- Estilo: `collage_cientifico_vintage`, prompt_base literal del catálogo.
- `approved_assets=[]`.
- `export.render_status=NOT_GENERATED`.
- No existe `export.filename`, `asset_filename`, `asset_type` ni rutas de medios.
- `publicacion.status=PENDIENTE_DECISION_GROK`.
- No existe `narrative_qa`; el estado es `BORRADOR_EN_PROYECTOS_PENDIENTE_AUDITOR`.
- 23:30: `PENDING_SOURCE`; no se creó storyboard.

No se generaron frames, imágenes, audio, voz, video ni renders. No se publicó ni programó contenido. No se modificaron `data/*.json`, `main`, workflows, motores canónicos ni Motor U6. No se consumieron créditos.
