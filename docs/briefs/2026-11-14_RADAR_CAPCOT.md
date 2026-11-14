# RADAR CAPCOT — 2026-11-14

Corte: 2026-11-14, 08:01, America/Mexico_City. Repositorio: marcojpad-hash/capcot-capsulas-imaginantes. Rama: feature/capcot-video-discovery-continuity.

## Resultado operativo

- Slot principal: 17:00, libre y autorizado. La ventana de tarde es 16:30–18:00 y el sábado figura como día preferente. El slot 07:00 ya había terminado al momento del corte; 17:00 es staging editorial, no programación.
- Slot 23:30 (slot_cesta=dato_del_dia): libre en los registros, pero **PENDING_SOURCE**. No se encontró fuente primaria de ciencia/naturaleza publicada el 14-nov-2026 y dentro de las 48 horas previas. No se crea storyboard adicional.
- Anti-duplicación: no había proyecto, salida, entrada ni bloqueado con fecha_objetivo 2026-11-14 antes de esta ejecución. Después del staging existe únicamente el proyecto principal 2026-11-14_dato-microplasticos-pantanal.
- Archivos base de esta fecha: este radar y proyectos/2026-11-14_dato-microplasticos-pantanal/storyboard.json. No se creó archivo *_fuentes.md.
- El informe técnico se actualizó de forma incremental por un cambio operativo relevante de Page Insights; commit técnico: 9bf9ceb187c7b8f345bcb58dc77c14e846d59ca1.
- Commit del storyboard: 7accf0d0821a91da1f6dbdc807ef57c5e73e471f.

## Fuente de verdad, rotación y ocupación

Lectura hecha en el orden prescrito: PLAN MAESTRO, RECETA, GUÍA, ESTILOS, catálogo scripts/estilos.json, temas_del_dia.json, rotacion.json, publicaciones.json; después líneas temáticas, flujo externo, continuidad audiovisual, investigación técnica, template y briefs/storyboards recientes. Se leyó también scripts/registro_editorial.py y se aplicó su reconciliación por project_id, sin escribir en data/*.json.

- data/horario_2026-11-14.json: no existe (GitHub respondió 404). Se aplicó el contrato vigente y data/horarios.json.
- data/horarios.json: ventanas generales 06:30–07:30 y 16:30–18:00; sábado es día preferente para la ventana de tarde. El contrato mantiene 17:00 como slot autorizado y 23:30 como slot fijo dato_del_dia.
- data/temas_del_dia.json: contiene fechas antiguas (24–28 oct); no aporta registro para 14-nov.
- data/rotacion.json: 27 registros, ninguno del 14-nov.
- data/publicaciones.json: 22 registros, ninguno del 14-nov.
- data/cola.json: un registro, ninguno del 14-nov.
- Vista de archivos: 170 registros storyboard/cola enumerados en proyectos (69), salidas (55), cola/entrada (3) y cola/bloqueados (43). Ninguno ocupaba 14-nov antes de crear el proyecto principal. La vista reconciliada de registro_editorial une por project_id; propuestas en proyectos/ no se cuentan como publicaciones.

## RSS científicos y Google Trends México

No se pudo recuperar el XML de los feeds definidos en scripts/tendencias.py. Se registran los errores de lectura de la herramienta web; no se ejecutó el parser del script ni se afirma que se haya parseado XML:

| Feed | URL | Fallo observado |
|---|---|---|
| ScienceDaily Science | https://www.sciencedaily.com/rss/top/science.xml | HTTP 400: Unsupported content-type application/xml |
| ScienceDaily Health | https://www.sciencedaily.com/rss/top/health.xml | HTTP 400: Unsupported content-type application/xml |
| ScienceDaily Space | https://www.sciencedaily.com/rss/space_time.xml | HTTP 400: Unsupported content-type application/xml |
| Phys.org | https://phys.org/rss-feed/ | HTTP 400: Unsupported content-type text/xml |
| NASA News Release | https://www.nasa.gov/news-release/feed/ | HTTP 400: Unsupported content-type application/rss+xml |
| ESA Space Science | https://www.esa.int/rssfeed/Our_Activities/Space_Science | HTTP 404: Not Found |
| Nature | https://www.nature.com/nature.rss | HTTP 400: Unsupported content-type application/rss+xml |
| EurekAlert | https://www.eurekalert.org/rss/news.xml | URL not accessible |
| Agencia SINC | https://www.agenciasinc.es/rss | URL not accessible |
| UNAM Global | https://unamglobal.unam.mx/feed/ | HTTP 400: Unsupported content-type application/rss+xml |
| Google Trends RSS México | https://trends.google.com/trending/rss?geo=MX | URL not accessible |

Respaldo: Google Trends Trending Now oficial México (https://trends.google.com/trending?geo=MX&hl=es). En el corte visible había 191 tendencias; las primeras 25 estaban dominadas por deportes y entretenimiento. Señal próxima a ciencia/espacio: Starship, 5 mil+ búsquedas, aumento de 400%, activa alrededor de 13 horas. Es una señal de interés de búsqueda, no un estudio ni una fuente científica. No se detectó tendencia clara relacionada con microplásticos en fauna.

## Candidatos publicados entre 2026-11-07 y 2026-11-14

Los cuatro DOI siguen **PENDIENTE_RESOLVEDOR**: las páginas editoriales muestran los identificadores, pero los intentos de doi.org y Crossref no completaron resolución independiente. No se presentan como DOI validados. Se conserva el enlace editorial directo de cada estudio.

### 1. Microplásticos en fauna terrestre — candidato principal

- **Estudio:** Marcia de Almeida Monteiro Melo Ferraz, Arnaud L. J. Desbiez, Mario Henrique Alves et al. (2026), “Human land use drives microplastic abundance in terrestrial wildlife”, Nature, publicado 11-nov-2026.
- **DOI mostrado por la página editorial:** 10.1038/s41586-026-11285-x — PENDIENTE_RESOLVEDOR.
- **Enlace editorial:** https://www.nature.com/articles/s41586-026-11285-x
- **Novedad observada:** 47 muestras de sangre de tapires de tierras bajas y osos hormigueros gigantes; 40 animales con datos GPS suficientes. De 17,165 partículas con HQI >75, 2,815 (16.4%) fueron identificadas como microplásticos. Se detectaron en 43 de 47 animales. Todos los individuos muestreados en el Pantanal tenían microplásticos pese a vivir a más de 65 km del desarrollo más cercano y a más de 112 km de la instalación de manejo de residuos más cercana.
- **Tendencia:** sin señal directa en Google Trends México.
- **Relevancia científica:** alta; conecta muestras biológicas, movimiento GPS y huella humana.
- **Oportunidad editorial:** alta; anomalía clara, conteo explicable y giro remoto que puede resolverse en una sola historia.
- **Público/ocasión:** público general, slot de tarde 17:00.
- **Riesgos:** asociación no equivale a causalidad; no se rastreó el origen de cada partícula; no se midieron efectos clínicos; no confundir 16.4% de partículas con porcentaje de animales.
- **Verificación:** artículo primario Nature abierto y consultado; DOI pendiente de resolver independientemente.

### 2. Estructura de la clorofila sintasa — alternativa técnica

- **Estudio:** D. Shvarev, A. M. Wysocka, F. S. Morey-Burrows et al. (2026), “Structure of chlorophyll synthase in complex with the LHC-like protein HliD”, Nature Chemical Biology, publicado 09-nov-2026.
- **DOI mostrado en el registro editorial:** 10.1038/s41589-026-02357-0 — PENDIENTE_RESOLVEDOR.
- **Enlace editorial:** https://www.nature.com/articles/s41589-026-02357-0
- **Novedad:** el título y los metadatos del artículo primario aparecen indexados; el acceso directo a la página editorial no permitió completar la lectura del artículo en esta pasada.
- **Tendencia:** sin señal específica.
- **Relevancia científica:** alta para comprender el ensamblaje de pigmentos fotosintéticos.
- **Oportunidad editorial:** media; mecanismo molecular visualizable, pero exige no convertir una estructura en una explicación completa de la fotosíntesis.
- **Público/ocasión:** público general de ciencia/plantas.
- **Riesgos:** no presentar como mecanismo completo ni atribuir funciones que el artículo no haya demostrado.
- **Verificación:** PENDING_SOURCE para afirmaciones sustantivas; metadatos indexados, DOI sin resolución independiente. No se recomienda para el storyboard de hoy.

### 3. Transitorio de radio con compañera similar al Sol

- **Estudio:** S. J. McSweeney et al. (2026), “A long-period transient with a Sun-like companion”, Nature Astronomy, publicado 12-nov-2026.
- **DOI mostrado por la página del artículo:** 10.1038/s41550-026-03016-z — PENDIENTE_RESOLVEDOR.
- **Enlace editorial:** https://www.nature.com/articles/s41550-026-03016-z
- **Comunicado institucional:** ICRAR, 12-nov-2026; la señal corresponde a un sistema binario con una enana blanca y una compañera de tipo G; el periodo de pulsos es de unos 7.9 minutos y el periodo orbital es de alrededor de 1.3 días.
- **Tendencia:** Starship aparece en Trending Now, pero no es el mismo fenómeno.
- **Relevancia científica:** alta para sistemas binarios y transitorios de radio.
- **Oportunidad editorial:** alta; buen gancho temporal y visual astronómico.
- **Público/ocasión:** público general interesado en espacio.
- **Riesgos:** no insinuar comunicación extraterrestre; no atribuir los pulsos a una causa distinta de la que el artículo estudia.
- **Verificación:** metadatos del artículo y comunicado institucional consultados; DOI pendiente de resolver independientemente.

### 4. Riesgo poblacional en fauna mesopelágica del Golfo de México

- **Estudio:** Pedro A. Peres, Keith Sellers, Tracey T. Sutton, Heather Bracken-Grissom et al. (2026), “Extinction risks in deep-sea populations revealed by genomic data and ecological niche modeling”, Nature Communications, publicado 12-nov-2026.
- **DOI mostrado por la página editorial:** 10.1038/s41467-026-79098-0 — PENDIENTE_RESOLVEDOR.
- **Enlace editorial:** https://www.nature.com/articles/s41467-026-79098-0
- **Novedad observada:** datos genómicos de cinco especies mesopelágicas del Golfo de México, con muestreo de 2011–2023; los autores describen tamaños efectivos de población bajos, señales de reducción de diversidad en algunas especies y modelos de idoneidad de hábitat bajo escenarios climáticos.
- **Tendencia:** sin señal directa.
- **Relevancia científica:** alta para conservación de fauna profunda.
- **Oportunidad editorial:** media-alta; buen tema de océano profundo, pero necesita explicar diferencia entre riesgo modelado y extinción observada.
- **Público/ocasión:** público general interesado en océano y conservación.
- **Riesgos:** no afirmar que las cinco especies ya están extintas ni extrapolar el resultado a todo el océano; los modelos son proyecciones y el estudio se limita a especies y región definidos.
- **Verificación:** artículo primario consultado; DOI pendiente de resolver independientemente.

### Recomendación editorial

Usar el candidato 1, microplásticos en fauna terrestre. Es el único que combina evidencia primaria accesible, una pregunta central clara, cifras explicables, geografía de campo y un límite de causalidad explícito. Se preparó el storyboard para el slot interno 17:00 con estilo papel_rasgado_capas, estructura comparacion y cama circuito_neural. No se reutiliza el estilo scratchboard del 13-nov ni la estructura historia del 13-nov.

## Slot 23:30 — dato_del_dia

**PENDING_SOURCE.** El slot fijo está libre, pero no se creó storyboard porque no se encontró una fuente primaria apta publicada el 14-nov-2026 dentro de las 48 horas previas. Un artículo secundario del 14-nov sobre el vínculo entre un toro y un burro remite a un estudio y comunicado institucional del 02-nov-2026; no cumple la fecha del slot. El hallazgo sobre relojes circadianos de mejillones de aguas profundas también corresponde a una publicación del 02-nov. No adelantar ni reciclar esos temas.

## Compuerta narrativa y estado del storyboard principal

- Proyecto: 2026-11-14_dato-microplasticos-pantanal.
- Archivo: proyectos/2026-11-14_dato-microplasticos-pantanal/storyboard.json.
- 9:16; 8 escenas; 194 palabras; 78 segundos de escenas + 6 segundos de cortinilla = 84 segundos.
- Arco: hook_medias_res → desarrollo → cierre_historia → reflexion_o_pregunta.
- Gancho: “El plástico llegó al Pantanal” (5 palabras).
- Fuentes por escena: SRC-001 en todas las escenas.
- Voz: edge-tts, es-MX-JorgeNeural, rate +7%, pitch -2Hz.
- Estilo único: papel_rasgado_capas; prompt_base literal en todos los prompts.
- Cama musical rotada: circuito_neural; ambientes y SFX por escena.
- Mapa: Baía das Pedras Ranch, Nhecolândia, Aquidauana, Mato Grosso do Sul; par numérico reportado -19.33, -55.72. El artículo imprime sufijos N/E con signos negativos; el borrador conserva los números firmados, omite sufijos y no infiere datum geodésico. El pin es regional, no GPS animal. El artículo cita Natural Earth y geobr como fuentes cartográficas.
- Gráfico: 2,815 / 17,165 partículas con HQI >75 = 16.4%; métrica secundaria 43/47 animales con detección.
- narrative_contract: los seis campos están completos.
- No se escribió narrative_qa; estado PENDIENTE_AUDITOR. El auditor independiente decide PASS/FAIL.
- Compuerta de assets: approved_assets exactamente []; export.render_status NOT_GENERATED; export.filename ausente; sin asset_filename, asset_type ni rutas de medios; publicacion.status PENDIENTE_DECISION_GROK.
- No se creó storyboard para 23:30.

## Seguimiento técnico Meta y Google Trends

Actualización incremental guardada en docs/INVESTIGACION_API_META_Y_GOOGLE_TRENDS.md, commit 9bf9ceb187c7b8f345bcb58dc77c14e846d59ca1.

- Page Insights v27.0: la documentación oficial indica que las interacciones de Reels no están incluidas en Page Insights; página con al menos 100 likes; actualización habitual cada 24 h; retención de dos años; máximo 90 días por consulta; métricas demográficas con mínimo de 100 personas; permisos read_insights y pages_read_engagement y tarea ANALYZE.
- Instagram User Insights v27.0: la referencia enumera reach, views, content_views, total_interactions y métricas Threads; se registra como inventario de referencia, no como incorporación automática de Threads a CAPCOT.
- La página general de changelog/anuncio de Meta devolvió HTTP 429; no se atribuye un cambio adicional no verificable.
- Google Trends API continúa en alpha con acceso limitado; no apareció anuncio oficial nuevo.
- No se ejecutaron llamadas autenticadas ni se usaron credenciales.

## QA preexistente — proyectos canónicos

Se releen los 69 storyboards canónicos bajo proyectos/. Hay 26 con narrative_qa: 10 PASS y 16 FAIL; los otros 43 están PENDIENTE_AUDITOR. En los 26 QA presentes, review_basis es exactamente lectura_en_frio_solo_narracion. reviewed_at se indica tal como aparece; “—” significa que el campo no está presente en el JSON. Los siete checks se conservan en el orden de QA_NARRATIVO_EN_FRIO.md.

| project_id | status | score | review_basis | reviewed_at | pregunta_central_reconstruible | apertura_in_medias_res | progresion_por_escena | transiciones_causales | giro_cientifico_explicado | limite_evidencia_explicito | payoff_cierre_apertura | critical_flags |
|---|---:|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 2026-10-31_murcielagos-viroma-global | FAIL | 72 | lectura_en_frio_solo_narracion | — | true | false | true | false | false | true | true | ["APERTURA_ESTATICA_Y_ESCENARIO_NO_DOCUMENTADO","TRANSICIONES_GENERICAS","CIFRA_300000_SIN_UNIDAD_DE_ANALISIS","GIRO_COMPARATIVO_NO_EXPLICADO"] |
| 2026-10-31_sequias-energia-renovable | FAIL | 56 | lectura_en_frio_solo_narracion | — | true | false | false | false | false | true | false | ["GANCHO_DEFINICIONAL","CIFRAS_SIN_DIRECCION_INTERPRETABLE","GIRO_SOLO_NOMBRADO","PAYOFF_NO_DERIVADO_DE_LA_EVIDENCIA"] |
| 2026-11-01_dato-cambio-horario-corazon | FAIL | 84 | lectura_en_frio_solo_narracion | 2026-11-01T18:08:00-06:00 | true | true | true | true | true | true | true | ["CIERRE_PRESELLO_INFERIOR_A_110_CARACTERES"] |
| 2026-11-01_llorar-cebolla-quimica | FAIL | 79 | lectura_en_frio_solo_narracion | 2026-11-01T15:09:29-06:00 | true | true | true | true | true | false | false | ["CIERRE_ATRIBUYE_INTENCION_EVOLUTIVA_NO_DEMOSTRADA","LIMITE_DE_EVIDENCIA_NO_EXPLICITO"] |
| 2026-11-01_pulpo-tres-corazones | FAIL | 72 | lectura_en_frio_solo_narracion | 2026-11-01T15:09:29-06:00 | true | false | true | true | true | false | true | ["APERTURA_HIPOTETICA_NO_IN_MEDIAS_RES","ANALOGIA_BRANQUIAS_SACAR_AIRE_DEL_AGUA_IMPRECISA","AFIRMACION_CORAZONES_NO_SUSTITUIBLES_SIN_RESPALDO"] |
| 2026-11-01_red-electrica-pulso-minuto | PASS | 89 | lectura_en_frio_solo_narracion | 2026-11-01T15:09:29-06:00 | true | true | true | true | true | true | true | [] |
| 2026-11-02_camaron-mantis | PASS | 90 | lectura_en_frio_solo_narracion | — | true | true | true | true | true | true | true | [] |
| 2026-11-02_comida-pan-duro | FAIL | 84 | lectura_en_frio_solo_narracion | — | true | true | true | true | true | true | true | ["CIERRE_SOBREAFIRMA_Y_CONTRADICE_LIMITE_DE_SECADO"] |
| 2026-11-04_cielo-azul-atardecer-rojo | PASS | 94 | lectura_en_frio_solo_narracion | 2026-11-04T15:58:40-06:00 | true | true | true | true | true | true | true | [] |
| 2026-11-05_comida-palomitas | FAIL | 82 | lectura_en_frio_solo_narracion | 2026-11-13T15:42:39-06:00 | true | false | false | true | true | true | true | ["APERTURA_DEFINICIONAL_NO_IN_MEDIAS_RES","ESCENA_6_REITERA_CAUSAS_DE_GRANOS_NO_REVENTADOS_SIN_INFORMACION_NUEVA"] |
| 2026-11-05_inter-arboles-se-comunican | FAIL | 78 | lectura_en_frio_solo_narracion | 2026-11-13T15:42:39-06:00 | true | false | true | true | true | true | true | ["APERTURA_GENERICA_NO_IN_MEDIAS_RES"] |
| 2026-11-05_inter-rayo-globular | FAIL | 81 | lectura_en_frio_solo_narracion | 2026-11-13T15:42:39-06:00 | true | false | true | true | true | true | true | ["APERTURA_HISTORICA_DESCRIPTIVA_NO_IN_MEDIAS_RES"] |
| 2026-11-05_kids-dia-en-venus | PASS | 88 | lectura_en_frio_solo_narracion | 2026-11-13T15:42:39-06:00 | true | true | true | true | true | true | true | [] |
| 2026-11-06_comida-aguacate-negro | FAIL | 79 | lectura_en_frio_solo_narracion | 2026-11-13T15:42:39-06:00 | true | true | false | false | true | true | true | ["REPETICION_ESCENAS_5_6_SIN_AVANCE_CAUSAL"] |
| 2026-11-06_inter-arena-cantante | PASS | 94 | lectura_en_frio_solo_narracion | 2026-11-13T15:42:39-06:00 | true | true | true | true | true | true | true | [] |
| 2026-11-06_inter-ranas-congeladas | FAIL | 83 | lectura_en_frio_solo_narracion | 2026-11-13T15:42:39-06:00 | true | true | false | false | true | true | true | ["REPETICION_ESCENAS_5_6_LIMITES_DE_ESPECIE_Y_CONDICIONES"] |
| 2026-11-06_kids-ballena-azul-corazon | FAIL | 80 | lectura_en_frio_solo_narracion | 2026-11-13T15:42:39-06:00 | true | true | true | true | true | true | false | ["PAYOFF_SOBREAFIRMA_CASI_SE_DETIENE"] |
| 2026-11-07_comida-hielo-caliente | FAIL | 81 | lectura_en_frio_solo_narracion | 2026-11-13T15:42:39-06:00 | true | false | true | true | true | true | true | ["APERTURA_DE_CREENCIAS_NO_IN_MEDIAS_RES"] |
| 2026-11-07_inter-nubes-pesan | FAIL | 78 | lectura_en_frio_solo_narracion | 2026-11-13T15:42:39-06:00 | true | true | false | false | true | true | false | ["ESCENA_7_REITERA_CIFRA_Y_LIMITE_SIN_PAYOFF_DE_SUSPENSION"] |
| 2026-11-07_inter-pulpo-suenos | FAIL | 80 | lectura_en_frio_solo_narracion | 2026-11-13T15:42:39-06:00 | true | true | false | false | true | true | false | ["REPETICION_ESCENAS_5_6_Y_PAYOFF_VAGO"] |
| 2026-11-07_kids-huesos-bebe | FAIL | 82 | lectura_en_frio_solo_narracion | 2026-11-13T15:42:39-06:00 | true | true | false | false | true | true | true | ["ESCENA_6_REPITE_VARIACION_DE_CONTEO_Y_FUSION"] |
| 2026-11-09_dato-robot-ensambla-orbita | PASS | 90 | lectura_en_frio_solo_narracion | 2026-11-09T18:45:00-06:00 | true | true | true | true | true | true | true | [] |
| 2026-11-10_comida-aprendizaje-sabor-nutriente | PASS | 92 | lectura_en_frio_solo_narracion | 2026-11-10T15:47:50-06:00 | true | true | true | true | true | true | true | [] |
| 2026-11-10_dato-adn-sincroniza-flujo | PASS | 91 | lectura_en_frio_solo_narracion | 2026-11-10T16:16:00-06:00 | true | true | true | true | true | true | true | [] |
| 2026-11-12_dato-pedorreta-chimpances | PASS | 91 | lectura_en_frio_solo_narracion | 2026-11-12T15:38:50-06:00 | true | true | true | true | true | true | true | [] |
| 2026-11-13_dato-caracol-16-embriones | PASS | 91 | lectura_en_frio_solo_narracion | 2026-11-13T15:42:39-06:00 | true | true | true | true | true | true | true | [] |

### PENDIENTE_AUDITOR (43)

- 2026-10-24_abejas-bullying: PENDIENTE_AUDITOR
- 2026-10-24_ideonella-pet: PENDIENTE_AUDITOR
- 2026-10-24_osedax-comehuesos: PENDIENTE_AUDITOR
- 2026-10-24_serpientes-que-ruedan: PENDIENTE_AUDITOR
- 2026-10-25_ave-jurasica-sin-vuelo: PENDIENTE_AUDITOR
- 2026-10-25_corales-contacto: PENDIENTE_AUDITOR
- 2026-10-25_reina-olor: PENDIENTE_AUDITOR
- 2026-10-25_sueno-electricidad-qom: PENDIENTE_AUDITOR
- 2026-10-26_baffin-bay-ice-shelf: PENDIENTE_AUDITOR
- 2026-10-26_catrina-posada-monerismo: PENDIENTE_AUDITOR
- 2026-10-26_hongo-gente-diminuta: PENDIENTE_AUDITOR
- 2026-10-26_papel-picado-dia-muertos: PENDIENTE_AUDITOR
- 2026-10-26_papel-picado-dia-muertos_parte2: PENDIENTE_AUDITOR
- 2026-10-26_pimiento-verde-rojo: PENDIENTE_AUDITOR
- 2026-10-27_cempasuchil-ciencia: PENDIENTE_AUDITOR
- 2026-10-27_corneja-decision-rapida: PENDIENTE_AUDITOR
- 2026-10-27_ddm-parte3-pomuch: PENDIENTE_AUDITOR
- 2026-10-27_familia-ajolote: PENDIENTE_AUDITOR
- 2026-10-27_kids-serpiente-voladora: PENDIENTE_AUDITOR
- 2026-10-27_noct-anfibio-marino: PENDIENTE_AUDITOR
- 2026-10-28_ddm-parte4-templo-mayor: PENDIENTE_AUDITOR
- 2026-10-28_familia-voyager-disco-oro: PENDIENTE_AUDITOR
- 2026-10-28_kids-titanoboa: PENDIENTE_AUDITOR
- 2026-10-28_monarca-almas: PENDIENTE_AUDITOR
- 2026-10-28_mosquito-fruitless-audicion: PENDIENTE_AUDITOR
- 2026-10-28_noct-lince-milanos: PENDIENTE_AUDITOR
- 2026-10-28_pan-de-muerto-huesos: PENDIENTE_AUDITOR
- 2026-10-29_juno-choque-proa: PENDIENTE_AUDITOR
- 2026-10-29_muralismo-cu: PENDIENTE_AUDITOR
- 2026-10-30_arqueas-origen-eucariotas: PENDIENTE_AUDITOR
- 2026-10-30_kromdraai-primera-fecha: PENDIENTE_AUDITOR
- 2026-10-31_pardelas-jetlag-solar: PENDIENTE_AUDITOR
- 2026-10-31_smartpe-edicion-plantas: PENDIENTE_AUDITOR
- 2026-11-03_dato-polvo-africano-microbios: PENDIENTE_AUDITOR
- 2026-11-03_kids-leche-enchilado: PENDIENTE_AUDITOR
- 2026-11-xx_kids-flamencos-rosas_RESPALDO: PENDIENTE_AUDITOR
- demo-001: PENDIENTE_AUDITOR
- guiones_lote_01: PENDIENTE_AUDITOR
- lote01-01-el-nino: PENDIENTE_AUDITOR
- lote01-02-petroleo: PENDIENTE_AUDITOR
- lote01-03-balon-curva: PENDIENTE_AUDITOR
- lote01-04-tardigrado: PENDIENTE_AUDITOR
- lote01-05-chicxulub: PENDIENTE_AUDITOR

## Límites de ejecución

No se modificaron main, data/*.json, scripts de rotación/tendencias, workflows, motores canónicos ni Motor U6. No se escribió narrative_qa, no se promovió a cola/entrada, no se creó storyboard para 23:30, no se generaron medios, no se publicó ni programó contenido y no se consumieron créditos.
