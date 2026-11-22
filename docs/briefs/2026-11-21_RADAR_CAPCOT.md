# RADAR CAPCOT — 2026-11-21

Repositorio: `marcojpad-hash/capcot-capsulas-imaginantes`  
Rama: `feature/capcot-video-discovery-continuity`  
Corte: 2026-11-21, America/Mexico_City  
HEAD consultado antes de este registro: `41ed5025eebbff79a618665b55296f5349e28bfb`  
Tipo: investigación documental + contraste de slots. No se generaron medios ni se publicaron cápsulas.

## 1. RSS y tendencias: resultado de la consulta

Se leyó `scripts/tendencias.py` y se intentaron las diez fuentes RSS declaradas más Google Trends México. No se ejecutó el script Python ni se parseó XML: los errores siguientes son los devueltos por el lector web de esta sesión, no una afirmación de que los servidores de origen estén caídos.

| Fuente | Resultado exacto del lector web |
|---|---|
| ScienceDaily Science | `(400) Unsupported content-type: application/xml` |
| ScienceDaily Health | `(400) Unsupported content-type: application/xml` |
| ScienceDaily Space | `(400) Unsupported content-type: application/xml` |
| Phys.org | `(400) Unsupported content-type: text/xml` |
| NASA News Release | `(400) Unsupported content-type: application/rss+xml` |
| ESA Space Science | `(404) Not Found` |
| Nature RSS | `(500) Redirected to idp.nature.com/authorize` |
| EurekAlert | `URL https://www.eurekalert.org/rss/news.xml is not accessible via this tool.` |
| SINC | `URL https://www.agenciasinc.es/rss is not accessible via this tool.` |
| UNAM Global | `(400) Unsupported content-type: application/rss+xml` |
| Google Trends RSS MX | `URL https://trends.google.com/trending/rss?geo=MX is not accessible via this tool.` |

**Respaldo oficial:** [Google Trends — Tendencias actuales, México](https://trends.google.com/trending?geo=MX&hl=es), filtro “Últimas 24 horas”. La página devolvió 185 tendencias, 25 por página. En las primeras 25 predominan fútbol, entretenimiento, búsquedas locales y actualidad; aparece “ola de frío”, pero no una tendencia científica con fuente primaria validada. No se convirtió volumen de búsquedas en estimación de audiencia CAPCOT.

## 2. Cinco candidatos recientes ya presentes en proyectos

Los cinco candidatos siguientes ya tienen storyboard en `proyectos/`. Se documentan para evitar duplicados; no son publicaciones, recepciones Grok ni promociones a cola.

### A — Metano sin erupción en Fentale

- **Observación:** artículo de *Nature Geoscience*, publicado 2026-11-19. Estima más de 38.2 ± 3.9 kt de CH₄ entre el 19-ene y el 9-abr-2025; aproximadamente 90% salió durante el primer mes y el pico estimado fue 157 ± 41 t/h. El artículo describe una intrusión magmática y liberación de gas sin erupción.
- **Fuente primaria:** [Nature Geoscience](https://www.nature.com/articles/s41561-026-02137-4). DOI `10.1038/s41561-026-02137-4`.
- **Verificación:** página editorial indexada; `doi_verification_status=PENDIENTE_RESOLVEDOR`. La consulta directa a Crossref/doi.org no completó. La ficha oficial del Smithsonian Global Volcanism Program respalda el localizador cartográfico de Fentale.
- **Cálculo:** no se recalcularon las emisiones; las cifras se conservan como estimaciones reportadas por los autores.
- **Inferencia editorial:** el giro “metano sin erupción” es fuerte, pero no debe convertirse en “el magma produjo todo el metano”: el artículo señala que no hay mediciones isotópicas directas del metano en Fentale.
- **Proyecto existente:** `2026-11-21_fentale-metano-sin-erupcion`, 23:30; narrative QA PASS 90/100; 8 escenas, 170 palabras, 84 s totales. El artículo es del 19-nov y no se dispone de hora editorial que permita confirmar la frescura del slot del 21-nov.
- **Recomendación:** conservar en proyectos. No promover hasta resolver DOI y frescura.

### B — Homo erectus y selva tropical en el sur de China

- **Observación:** artículo de *Nature*, publicado 2026-11-18. Analiza dientes de homininos de dos cuevas de Guangxi, restos faunísticos y dataciones radiométricas; la muestra humana isotópica es limitada y la movilidad se presenta como inferencia, no como ruta observada.
- **Fuente primaria:** [Nature](https://www.nature.com/articles/s41586-026-11155-6). DOI `10.1038/s41586-026-11155-6`; el registro de PubMed confirma DOI y fecha.
- **Cálculo:** no se recalcularon edades ni proporciones.
- **Inferencia editorial:** el material permite explicar adaptación a un entorno de dosel cerrado, pero no generalizar el resultado a todos los individuos de la especie.
- **Proyecto existente:** `2026-11-21_homo-erectus-selva-tropical`, 07:00; narrative QA FAIL 83/100; 8 escenas, 196 palabras, 84 s.
- **Recomendación:** no promover; la compuerta narrativa permanece FAIL.

### C — Púlsar gamma PSR J1622−7204

- **Observación:** *Physical Review Letters*, publicado 2026-11-19. El trabajo reporta un púlsar aislado de 261 Hz identificado con 15 años de datos Fermi-LAT y un método basado en retículas; el presupuesto computacional informado es de unas 10 horas frente a una búsqueda semicoherente previa de alrededor de 600 años de CPU.
- **Fuente primaria:** [Physical Review Letters](https://journals.aps.org/prl/abstract/10.1103/vlt2-xzgk). DOI `10.1103/vlt2-xzgk`; el enlace DOI redirige a la página editorial APS.
- **Cálculo:** no se recalcularon los presupuestos de CPU; se conservan como cifras del artículo, no como comparación de dos ejecuciones idénticas.
- **Inferencia editorial:** el contraste computacional es visualizable, pero no debe llamarse “IA” ni prometer que el método encontrará todos los púlsares.
- **Proyecto existente:** `2026-11-21_pulsar-gamma-reticulo`, 17:00; narrative QA FAIL 83/100; 8 escenas, 209 palabras, 84 s. 17:00 cae en ventana de prueba, no en una ventana regular.
- **Recomendación:** no promover; QA FAIL y slot en prueba.

### D — Voyager 1 alcanza un día-luz

- **Observación:** NASA/JPL publicó 2026-11-19 que Voyager 1 cruzó el umbral de un día-luz el 18-nov-2026: aproximadamente 25.9 mil millones de km; una señal tarda cerca de 24 horas en un sentido y unas 48 horas en ida y vuelta.
- **Fuente primaria:** [NASA/JPL](https://www.jpl.nasa.gov/news/nasas-voyager-1-makes-history-reaching-one-light-day-from-earth/). No aplica DOI.
- **Cálculo:** no se recalculó la distancia; se conservan los valores reportados por NASA/JPL.
- **Inferencia editorial:** la escala temporal funciona bien para una cápsula; no decir que la nave viaja a la velocidad de la luz.
- **Proyecto existente:** `2026-11-22_voyager-1-un-dia-luz`, 07:00; narrative QA FAIL 83/100; 8 escenas, 180 palabras, 84 s.
- **Recomendación:** no promover hasta que la narración supere QA independiente.

### E — Genoma de yubarta obtenido desde muestras de soplo

- **Observación:** *Molecular Ecology Resources*, publicado 2026-11-17. El artículo informa 58 muestras de soplo de 26 yubartas del Pacífico nororiental, promedio de 84% de ADN endógeno y coberturas medias de 2.3× nuclear y 94× mitocondrial.
- **Fuente primaria:** [Wiley / Molecular Ecology Resources](https://onlinelibrary.wiley.com/doi/10.1111/1755-0998.70219). DOI `10.1111/1755-0998.70219`; el enlace DOI resolvió a la página editorial.
- **Cálculo:** no se recalcularon porcentajes ni coberturas.
- **Inferencia editorial:** es una vía de muestreo no invasiva prometedora; la aplicabilidad puede variar por especie y condiciones de muestreo.
- **Proyecto existente:** `2026-11-22_yubarta-genoma-soplo`, 17:00; narrative QA PASS 90/100; 8 escenas, 180 palabras, 84 s. 17:00 es una ventana en prueba.
- **Recomendación:** conservar PASS; no promover hasta resolver la decisión editorial sobre la ventana de prueba y la recepción Grok.

## 3. Leads nuevos no promovidos

### Subsurface marine heat surge — posible candidato para 22-nov 13:30

- **Observación:** artículo de *Communications Earth & Environment*, publicado 2026-11-20, describe dos pulsos de calor subsuperficial en el Pacífico norteoriental (2009 y 2013) y su transporte hacia los trópicos, con impactos climáticos retardados.
- **Fuente primaria:** [Nature Communications Earth & Environment](https://www.nature.com/articles/s43247-026-04223-2). DOI `10.1038/s43247-026-04223-2`.
- **Cálculo:** no se recalcularon anomalías ni tiempos de tránsito.
- **Inferencia:** podría servir para explicar cómo el océano almacena y transporta calor antes de que aparezca una señal atmosférica; no debe atribuirse causalidad más fuerte que la del artículo.
- **Bloqueo:** el lector web no pudo abrir el texto completo ni verificar el DOI por Crossref/resolvedor; tampoco se extrajeron coordenadas de las figuras/datos del estudio.
- **Estado:** `PENDING_SOURCE`. El 22-nov 13:30 no presenta ocupación en `main/data/publicaciones.json` al corte, pero no se crea storyboard hasta resolver DOI y geografía.

### Plankton ecological complexity — NO_DUPLICAR

- **Fuente primaria:** [Nature Communications](https://www.nature.com/articles/s41467-026-79817-7), publicado 2026-11-21; DOI `10.1038/s41467-026-79817-7`.
- **Motivo:** se solapa temáticamente con `2026-11-05_sinergia-algas` (plankton/algae y exportación de carbono). Se conserva como observación de radar, no se crea otra cápsula: `NO_DUPLICAR`.

## 4. Ocupación y recomendación editorial

- **21-nov:** 07:00 tiene el borrador Homo erectus; 13:30 está ocupado en `main` por `2026-11-02_oxoboranos-estables`; 17:00 tiene el borrador del púlsar y es ventana de prueba; 19:00 está ocupado por la programación preexistente del robot; 23:30 tiene el borrador Fentale, con DOI/frescura pendientes.
- **22-nov:** 07:00 tiene el borrador Voyager; 17:00 tiene Yubarta en ventana de prueba. 13:30 aparece libre en `main` al corte, pero el nuevo candidato de calor subsuperficial sigue `PENDING_SOURCE`; 23:30 no tiene candidato nuevo con verificación completa.
- **Decisión:** no se crea storyboard nuevo en este corte. No hay candidato nuevo con DOI/resolvedor y geografía respaldados que además evite la rotación temática; los slots actuales ya tienen borradores o conflictos.

## 5. Estado del trabajo

- Investigación: 5 candidatos recientes documentados y 2 leads nuevos clasificados.
- Fuentes primarias: URLs editoriales/NASA identificadas; Fentale y el lead de calor subsuperficial conservan DOI pendiente de resolución independiente.
- Google Trends: respaldo oficial consultado; ninguna tendencia científica visible justificó alterar la selección.
- Storyboards nuevos: ninguno.
- Medios: no generados.
- Publicación/programación: no ejecutada.
- Créditos: no consumidos.
- `data/*.json`: solo lectura.


## 6. Reconsulta de feeds — 21-nov-2026

Se reintentaron las diez URL declaradas en `scripts/tendencias.py` desde el lector web de esta sesión. No se ejecutó el script Python ni se parseó XML; estos errores describen al lector, no necesariamente la disponibilidad de los servidores:

| Feed | Resultado exacto |
|---|---|
| ScienceDaily Science | `(400) Unsupported content-type: application/xml` |
| ScienceDaily Salud | `(400) Unsupported content-type: application/xml` |
| ScienceDaily Espacio | `(400) Unsupported content-type: application/xml` |
| Phys.org | `(400) Unsupported content-type: text/xml` |
| NASA News Release | `(400) Unsupported content-type: application/rss+xml` |
| ESA Space Science | `(404) Not Found` |
| Nature RSS | `(400) Unsupported content-type: application/rss+xml` |
| EurekAlert | `URL https://www.eurekalert.org/rss/news.xml is not accessible via this tool.` |
| SINC | `URL https://www.agenciasinc.es/rss is not accessible via this tool.` |
| UNAM Global | `(400) Unsupported content-type: application/rss+xml` |
| Google Trends RSS MX | `URL https://trends.google.com/trending/rss?geo=MX is not accessible via this tool.` |

**Respaldo oficial consultado:** [Google Trends — Tendencias actuales, México](https://trends.google.com/trending?geo=MX&hl=es), últimas 24 horas. La página muestra 185 tendencias; las primeras 25 están dominadas por fútbol, entretenimiento y actualidad. “Ola de frío” aparece activa con 10 mil+ búsquedas, pero no aporta por sí sola una fuente científica primaria. No se crea storyboard a partir de esa tendencia.

**Fentale:** la página editorial de Nature es accesible y confirma la publicación del 19-nov-2026 y el DOI `10.1038/s41561-026-02137-4`. Las consultas directas a Crossref REST y al resolver `doi.org` no pudieron abrirse en el lector web; por eso se conserva `PENDIENTE_RESOLVEDOR` y no se habilita promoción. No se cambió el storyboard ni su estado.


## 7. Revalidación de slots, QA y radar de candidatos — 2026-11-21

Corte de esta pasada: rama feature HEAD 047275244d7c34430cec37fe4d9ad5e8cae3f203; main HEAD 8ceba2a913806acb665c5491fca8a76f93fab2ba. Se actualiza este RADAR existente; no se crea un segundo RADAR para la fecha.

### 7.1 Inventario de la fecha y rotación

- En proyectos/ hay exactamente tres storyboards con fecha_objetivo=2026-11-21: Fentale (23:30), Homo erectus (07:00) y púlsar gamma (17:00).
- No hay storyboards del 21-nov en salidas/, cola/entrada/ ni cola/bloqueados/.
- data/horario_2026-11-21.json no existe. El contrato operativo §3 autoriza cinco slots; scripts/rotacion.py declara las ventanas 07:00, 13:30, 17:00, 19:00 y 23:30. scripts/registro_editorial.py recorre recursivamente storyboards de proyectos, cola, bloqueados y salidas; se contrastó además main por separado.
- Los JSON de rotación siguen atrasados: temas_del_dia.json termina el 28-oct; rotacion.json el 31-oct; estilos_usados.json el 28-oct; publicaciones.json de feature no registra el día 21. data/cola.json conserva solo el fallo del 31-oct. Se trataron como históricos, no como inventario completo.
- handoffs/grok_inbox/ solo contiene el marker histórico del robot del 9-nov (status=pending), no markers de los tres proyectos del 21. Los tres cola/estado/<project_id>.json devuelven 404: RECEPCION_GROK_NO_CONFIRMADA. El marker antiguo no acredita recepción.

### 7.2 Ocupación cruzada de los cinco slots

| Slot CDMX | Evidencia encontrada | Estado operativo |
|---|---|---|
| 07:00 | Feature: 2026-11-21_homo-erectus-selva-tropical | NO_DUPLICAR; storyboard existente, QA FAIL |
| 13:30 | Main: 2026-11-02_oxoboranos-estables, programacion.json, YouTube K4qNkx2f4RI, TikTok y Facebook programados para 13:30 | CONFLICTO_DE_SLOT_ENTRE_RAMAS / NO_DUPLICAR |
| 17:00 | Feature: 2026-11-21_pulsar-gamma-reticulo; ventana identificada como prueba | NO_DUPLICAR; storyboard existente, QA FAIL |
| 19:00 | Main: 2026-11-09_dato-robot-ensambla-orbita, programacion.json, YouTube ZG4iQgmWrLI, TikTok y Facebook programados para 19:00 | CONFLICTO_DE_SLOT_ENTRE_RAMAS / NO_DUPLICAR |
| 23:30 | Feature: 2026-11-21_fentale-metano-sin-erupcion | NO_DUPLICAR; storyboard existente, QA PASS, pero la fuente es del 19-nov y no satisface la regla de publicación del mismo día para dato_del_dia |

Para 13:30, publish_at=2026-11-21T19:30:00Z; para 19:00, publish_at=2026-11-22T01:00:00Z. Ambos paquetes de main conservan evidencia de programación multiplataforma y no se cancelan ni reprograman. Los cinco slots están ocupados; no hay storyboard nuevo autorizado para el 21-nov. El slot 23:30 está activo, pero su paquete preexistente no cumple la condición de fuente publicada el mismo día. No se crea una segunda versión ni se promueve la existente por esta revisión.

### 7.3 Relectura estructural de los tres storyboards del día

Conteo aplicado con la misma expresión de palabras de scripts/validar_storyboard.py, sin ejecutar el validador oficial:

| Proyecto | Palabras | Escenas | Duración con cortinilla | Mapa / dato | Estilo del catálogo |
|---|---:|---:|---:|---|---|
| 2026-11-21_fentale-metano-sin-erupcion | 170 | 8 | 84 s | 1 mapa WGS84 / 2 capas de dato | pulp_comic_1940s, prompt_base literal |
| 2026-11-21_homo-erectus-selva-tropical | 196 | 8 | 84 s | 1 mapa WGS84 / 1 capa de dato | dibujo_cientifico_scratchboard, prompt_base literal |
| 2026-11-21_pulsar-gamma-reticulo | 209 | 8 | 84 s | 1 mapa celeste ICRS / 2 capas de dato | pixel_art, prompt_base literal |

Los tres conservan narrative_contract con sus seis campos no vacíos, arco por escenas en el orden requerido, fuentes y source_ids válidos, voz edge-tts / es-MX-JorgeNeural / +7% / -2Hz, ambiente y SFX en las ocho escenas, cortinilla de seis segundos, approved_assets=[], export.render_status=NOT_GENERATED, ausencia de export.filename y rutas de medios, y publicacion.status=PENDIENTE_DECISION_GROK. No se modificaron los storyboards ni se ejecutó QA narrativo nuevo.

### 7.4 Estado de QA narrativo preexistente — transcripción de los JSON

**2026-11-21_fentale-metano-sin-erupcion**
- status: PASS
- score: 90
- review_basis: lectura_en_frio_solo_narracion
- reviewed_at: 2026-11-20T16:11:24-06:00
- checks: pregunta_central_reconstruible=true; apertura_in_medias_res=true; progresion_por_escena=true; transiciones_causales=true; giro_cientifico_explicado=true; limite_evidencia_explicito=true; payoff_cierre_apertura=true.
- critical_flags: [].
- Nota de elegibilidad separada del QA: la fuente primaria está fechada 19-nov, no 21-nov; por ello no satisface la regla especial de frescura para el slot 23:30.

**2026-11-21_homo-erectus-selva-tropical**
- status: FAIL
- score: 83
- review_basis: lectura_en_frio_solo_narracion
- reviewed_at: 2026-11-20T22:06:10-06:00
- checks: pregunta_central_reconstruible=true; apertura_in_medias_res=true; progresion_por_escena=true; transiciones_causales=true; giro_cientifico_explicado=false; limite_evidencia_explicito=true; payoff_cierre_apertura=true.
- critical_flags: ["GIRO_CIENTIFICO_NOMBRADO_PERO_NO_EXPLICADO"].

**2026-11-21_pulsar-gamma-reticulo**
- status: FAIL
- score: 83
- review_basis: lectura_en_frio_solo_narracion
- reviewed_at: 2026-11-20T15:41:24-06:00
- checks: pregunta_central_reconstruible=true; apertura_in_medias_res=true; progresion_por_escena=true; transiciones_causales=true; giro_cientifico_explicado=false; limite_evidencia_explicito=true; payoff_cierre_apertura=true.
- critical_flags: ["GIRO_CIENTIFICO_NOMBRADO_PERO_NO_EXPLICADO"].

Los tres estados se copiaron del JSON; no se reescribió narrative_qa, no se repitió la lectura en frío y no se promovió ningún paquete.

### 7.5 Shortlist científica vigente (publicación dentro de los últimos siete días)

| Candidato | Fuente primaria, fecha y DOI/URL | Tendencia / relevancia / oportunidad | Público y riesgo | Verificación |
|---|---|---|---|---|
| Intensificación del uso agrícola tropical y multidiversidad | Guerrero-Ramírez et al., Nature, 18-nov-2026. https://www.nature.com/articles/s41586-026-11298-6. DOI 10.1038/s41586-026-11298-6. | Tendencia: sin señal directa en Trends MX. Relevancia: alta. Oportunidad: alta; 24 grupos taxonómicos y 40,049 especies; pérdidas aproximadas de multidiversidad de 78% a escala de paisaje y 50% local en monocultivos. | Público de naturaleza y conservación. No traducir 78%/50% a porcentaje de especies extintas; son métricas de multidiversidad y el estudio cubre paisajes indonesios. | Página primaria indexada; PENDIENTE_RESOLVEDOR. Coordenadas exactas de las parcelas no verificadas; no está listo para storyboard. |
| Descarga de metano en Fentale sin erupción | Dualeh et al., Nature Geoscience, 19-nov-2026. https://www.nature.com/articles/s41561-026-02137-4. DOI 10.1038/s41561-026-02137-4. | Tendencia: baja/no específica. Relevancia: alta. Oportunidad: alta por el mecanismo magma–sedimento. | Público de ciencias de la Tierra y clima. El evento medido ocurrió en 2025; el origen termogénico es propuesto y no se midieron isótopos locales de CH4. | Fuente primaria consultada; PENDIENTE_RESOLVEDOR. |
| Adaptación de Homo erectus a selva tropical | Westaway et al., Nature, 18-nov-2026. https://www.nature.com/articles/s41586-026-11155-6. DOI 10.1038/s41586-026-11155-6. | Tendencia: baja/no específica. Relevancia: alta. Oportunidad: alta para evolución humana y paleoecología. | Público de evolución y naturaleza. Nueve dientes, ocho identificados como H. erectus; no generalizar a toda la especie. | VERIFICADO_RESOLVEDOR en el registro de fuente del storyboard existente. |
| Descubrimiento del púlsar gamma PSR J1622−7204 | Pook-Kolb et al., Physical Review Letters 137, 211201, 19-nov-2026. https://journals.aps.org/prl/abstract/10.1103/vlt2-xzgk. DOI 10.1103/vlt2-xzgk. | Tendencia: baja/no específica. Relevancia: alta. Oportunidad: alta para astronomía y métodos computacionales. | Público de espacio y tecnología. La comparación de 10 horas de CPU frente a 600 años de CPU usa métodos distintos; no llamarlo IA ni tiempo de calendario. | Página primaria APS y VERIFICADO_RESOLVEDOR en el storyboard existente. |
| Genomas de yubartas desde el soplo | O'Mahony et al., Molecular Ecology Resources, 17-nov-2026. https://onlinelibrary.wiley.com/doi/10.1111/1755-0998.70219. DOI 10.1111/1755-0998.70219. | Tendencia: baja/no específica. Relevancia: alta. Oportunidad: alta para conservación marina. | Público de océanos y biodiversidad. Son 58 muestras de 26 yubartas del Pacífico nororiental; la aplicabilidad puede variar por especie y condiciones. | VERIFICADO_RESOLVEDOR en el storyboard existente y página primaria Wiley consultada. |

Recomendación para el siguiente slot que realmente quede libre: conservar como primer candidato el estudio de multidiversidad tropical, condicionado a resolver DOI y obtener del artículo/suplemento una localización cartográfica que no invente coordenadas. No se redacta hoy porque los cinco slots están ocupados. El proyecto Voyager del 22-nov permanece como propuesta preexistente separada y no se cuenta en esta shortlist del 21-nov.

**Control de fecha:** el artículo de hormigas recolectoras sobre negative senescence tiene publicación/primera versión el 9-nov-2026, aunque hubo noticias secundarias esta semana; queda fuera de la ventana de siete días. No se reutiliza como candidato reciente.

### 7.6 RSS y Google Trends — reintento de esta pasada

Se reintentaron los diez RSS definidos por scripts/tendencias.py y el RSS MX. No se ejecutó el script Python ni se parseó XML. Resultados exactos del lector web:
- ScienceDaily Science, Health y Space: (400) Unsupported content-type: application/xml.
- Phys.org: (400) Unsupported content-type: text/xml.
- NASA News Release y UNAM Global: (400) Unsupported content-type: application/rss+xml.
- ESA Space Science: (404) Not Found.
- Nature RSS: (400) Unsupported content-type: application/rss+xml.
- EurekAlert y SINC: URL no accesible mediante esta herramienta.
- Google Trends RSS MX: URL no accesible mediante esta herramienta.

**Respaldo oficial:** https://trends.google.com/trending?geo=MX&hl=es, últimas 24 horas. La página muestra 184 tendencias, 25 por página. En la primera página dominan fútbol, entretenimiento, actualidad y búsquedas locales. Entre las consultas visibles aparecen ola de frío (10 mil+), volcán (5 mil+) y tormenta (2 mil+); ninguna aporta por sí sola una fuente científica primaria ni prueba demanda por una cápsula específica.

### 7.7 Seguimiento técnico

Se releyó el informe técnico y se contrastaron las referencias oficiales:
- Graph API: la página canónica mantiene v27.0 como última versión, introducida el 4-nov-2026.
- Page Insights: siguen visibles el umbral de 100 likes, actualización aproximada cada 24 h, retención de dos años, consultas de hasta 90 días y exclusión de interacciones de Reels.
- Instagram Insights: siguen documentadas Unified Login, Instagram Login y Facebook Login; el changelog visible no muestra una entrada de Insights posterior a las ya registradas y la última entrada relevante de media_url sigue fechada 30-jul-2026.
- Google Trends API: continúa en alfa de acceso limitado, con ventana móvil de cinco años, agregaciones periódicas y regiones/subregiones.

No se encontró un cambio técnico nuevo que justifique actualizar docs/INVESTIGACION_API_META_Y_GOOGLE_TRENDS.md. El informe técnico queda intacto.

### 7.8 Resultado de la pasada

- Radar único de la fecha: actualizado en su ruta existente.
- Storyboards nuevos: 0, por ocupación de los cinco slots.
- Storyboards existentes del día: 3/3 releídos y parseados; compuertas estructurales estáticas verificadas; QA existente preservado.
- NO_DUPLICAR: 07:00, 13:30, 17:00, 19:00 y 23:30.
- Recepción Grok: no confirmada para los tres proyectos de feature.
- QA nuevo, promoción, cola, medios, publicación y programación: no ejecutados.
- data/*.json, main, workflows, motores y Motor U6: sin modificaciones.
- Créditos: no consumidos.


## 4. Corrección posterior de ocupación de slot — 2026-11-21

La comprobación inicial del lead “Subsurface marine heat surge” solo encontró libre el 22-nov 13:30 en `main/data/publicaciones.json`. Una relectura posterior del documento de programación `main/docs/briefs/2026-11-21_PRODUCCION_SEMANA_23-28nov.md` muestra **Gutenberg programado el domingo 22-nov a las 13:30 CDMX**. La consulta de publicaciones JSON no era suficiente para declarar el slot libre.

- Estado corregido del lead para 22-nov 13:30: **NO_DUPLICAR / SLOT_OCUPADO_EN_MAIN**.
- No crear storyboard ni promover ese lead.
- El proyecto distinto `2026-11-23_tropical-biodiversity-turnover` apunta a 23-nov 13:30; esa hora no coincide con los slots listados en el plan semanal (23-nov 07:00 nudillos). Sigue sujeto a sus propias compuertas de QA y fuente.
- El storyboard Bao de 22-nov 13:30 queda marcado `CONFLICTO_DE_SLOT_ENTRE_RAMAS` en `risk_notes`.

Esta corrección no modifica `data/*.json`, publicaciones, horarios ni decisiones editoriales.


---

## Reconsulta de respaldo oficial — 2026-11-21, 15:57 CDMX

El RSS de Google Trends México no fue accesible mediante el lector de esta ejecución; se consultó la página oficial HTML de Tendencias actuales, México, últimas 24 horas. Mostró 229 tendencias, 25 por página. La primera página estuvo dominada por fútbol y entretenimiento; no apareció un candidato de ciencia o naturaleza entre los primeros 25. Esto no se usa como inferencia de audiencia ni sustituye fuentes científicas primarias.

Errores observados al reintentar los RSS configurados en `scripts/tendencias.py`:
- Google Trends RSS: URL no accesible mediante esta herramienta.
- ScienceDaily (science, health y space): HTTP 400, tipo `application/xml` no admitido por el lector.
- Phys.org: HTTP 400, tipo `text/xml` no admitido.
- NASA News Release: HTTP 400, tipo `application/rss+xml` no admitido.
- ESA Space Science: HTTP 404 Not Found.
- Nature: HTTP 400, tipo `application/rss+xml` no admitido.
- EurekAlert, SINC y UNAM Global: URL no accesible mediante esta herramienta.

Estos son errores del lector/conector observado, no prueba de que los servidores de origen estén caídos. Se reutilizan los candidatos y fuentes primarias ya documentados en este radar; no se inventa un candidato ni se abre un slot ocupado.


## Reconsulta de RSS y Google Trends — 2026-11-21, 18:35 CDMX

Se repitió la lectura de los diez feeds definidos en `scripts/tendencias.py` y del RSS de Google Trends México. Errores exactos del lector web en esta pasada:
- ScienceDaily Science, Health y Space: HTTP 400, `Unsupported content-type: application/xml`.
- Phys.org: HTTP 400, `Unsupported content-type: text/xml`.
- NASA News Release: HTTP 400, `Unsupported content-type: application/rss+xml`.
- ESA Space Science: HTTP 404, `Not Found`.
- Nature RSS: HTTP 400, `Unsupported content-type: application/rss+xml`.
- EurekAlert y SINC: URL no accesible mediante esta herramienta.
- UNAM Global: HTTP 400, `Unsupported content-type: application/rss+xml`.
- Google Trends RSS MX: URL no accesible mediante esta herramienta.

**Respaldo oficial:** la página HTML de Google Trends México sí abrió: 236 tendencias, 25 por página, últimas 24 horas. La primera página está dominada por fútbol, entretenimiento y búsquedas generales. “Perú” aparece con 10 mil+ y la consulta relacionada “terremoto peru”, pero no ofrece por sí sola un estudio primario ni un ángulo científico verificable para cápsula. Fuente: https://trends.google.com/trending?geo=MX&hl=es

No se añadió candidato ni storyboard: se conservan los candidatos ya documentados en este radar y los cinco slots de la fecha siguen ocupados. Los errores son del lector/conector observado; no prueban caída de los servidores de origen.


---

## 8. Escaneo adicional de artículos publicados el 21-nov — Crossref

Esta lista complementa los cinco candidatos ya documentados en las secciones 2 y 7. No reemplaza la rotación ni autoriza un nuevo storyboard. Los cinco DOI se consultaron en Crossref REST y devolvieron `status=ok`, título coincidente y publicación en línea el 2026-11-21.

### 8.1 Biosíntesis de alcaloides de iboga

- **Observación:** dos enzimas adicionales permiten reconstruir la biosíntesis de voacangina en un huésped heterólogo; cuatro enzimas más convierten un intermediario en ibophyllidine.
- **Cálculo:** ninguno.
- **Inferencia:** el trabajo completa partes de dos rutas biosintéticas; no demuestra eficacia clínica ni seguridad de un compuesto.
- **Recomendación:** prioridad alta por el giro bioquímico. No desarrollar hasta obtener localidad de origen de la muestra y coordenadas cartográficas respaldadas.
- **Fuente primaria:** https://www.nature.com/articles/s41467-026-79750-9
- **DOI:** 10.1038/s41467-026-79750-9 — Crossref `status=ok`: https://api.crossref.org/works/10.1038/s41467-026-79750-9
- **Estado:** `PENDING_MAP_SOURCE`.

### 8.2 Firma metabólica de estrés por cadmio

- **Observación:** metabolómica en células de mamífero y larvas de pez cebra; el estudio reporta reducción de glutamato/aspartato, acumulación de poliaminas y asociación con respuesta integrada al estrés y actividad de LAT1.
- **Cálculo:** no se recalcularon dosis ni tamaños de efecto.
- **Inferencia:** resultado en los modelos experimentales del artículo; no extrapolar a enfermedad ni a efectos individuales en humanos.
- **Recomendación:** prioridad media. No desarrollar hasta verificar una localización experimental cartografiable y una pregunta narrativa concreta.
- **Fuente primaria:** https://www.nature.com/articles/s41420-026-03456-6
- **DOI:** 10.1038/s41420-026-03456-6 — Crossref `status=ok`: https://api.crossref.org/works/10.1038/s41420-026-03456-6
- **Estado:** `PENDING_MAP_SOURCE`.

### 8.3 Genoma y transcriptoma de *Pelodera strongyloides*

- **Observación:** recurso de 177.6 Mb ensamblado en 11 cromosomas, 16,767 genes codificantes y transcriptómica de siete etapas; el aislado se reporta de Guangzhou.
- **Cálculo:** ninguno.
- **Inferencia:** recurso para estudios comparativos de parasitismo; no demuestra por sí mismo el mecanismo ni la transición evolutiva.
- **Recomendación:** prioridad media-baja. Falta coordenada de recolección más precisa que la ciudad y un giro narrativo no técnico.
- **Fuente primaria:** https://www.nature.com/articles/s41597-026-08770-3
- **DOI:** 10.1038/s41597-026-08770-3 — Crossref `status=ok`: https://api.crossref.org/works/10.1038/s41597-026-08770-3
- **Estado:** `PENDING_COLLECTION_COORDINATES`.

### 8.4 Genoma y anotación de veneno de *Crotalus viridis*

- **Observación:** Crossref confirma el artículo de *Scientific Data* “An improved genome and venom gene annotation for the Prairie Rattlesnake (*Crotalus viridis*)”, publicado en línea el 21-nov.
- **Cálculo:** ninguno; no se atribuyen cifras ni funciones sin leer el artículo completo.
- **Inferencia:** recurso genómico y de anotación, no evidencia automática de una función nueva de toxinas.
- **Recomendación:** prioridad baja. Falta localidad exacta del espécimen y un hallazgo funcional narrable.
- **Fuente primaria:** https://www.nature.com/articles/s41597-026-08647-5
- **DOI:** 10.1038/s41597-026-08647-5 — Crossref `status=ok`: https://api.crossref.org/works/10.1038/s41597-026-08647-5
- **Estado:** `PENDING_FULLTEXT_AND_SAMPLE_LOCALITY`.

### 8.5 Ensamblaje genómico de *Squalidus argentatus*

- **Observación:** Crossref confirma el artículo de *Scientific Data* “Chromosome-Level Genome Assembly and Annotation of *Squalidus argentatus*”, publicado en línea el 21-nov.
- **Cálculo:** ninguno.
- **Inferencia:** recurso de genoma; no se presenta como hallazgo funcional o adaptación demostrada.
- **Recomendación:** prioridad baja. Falta localidad de muestreo y un ángulo narrativo distinto de enumerar métricas de ensamblaje.
- **Fuente primaria:** https://www.nature.com/articles/s41597-026-08885-7
- **DOI:** 10.1038/s41597-026-08885-7 — Crossref `status=ok`: https://api.crossref.org/works/10.1038/s41597-026-08885-7
- **Estado:** `PENDING_SAMPLE_LOCALITY`.

## 9. Monitor espacial — BepiColombo

La página oficial de Quick Look de ESA mostraba la inserción orbital en Mercurio programada para el 21-nov; el corte recuperado estaba fechado 17:34 UTC, anterior a la maniobra programada. No se encontró confirmación oficial posterior al encendido en las fuentes consultadas. No afirmar éxito ni captura orbital hasta una actualización de ESA/JAXA. Fuente: https://bepicolombo.esac.esa.int/bscs-qla/home. Estado: `PENDING_EVENT_CONFIRMATION`. No cuenta como candidato de investigación ni como storyboard.

## 10. Reconciliación final de slots — 2026-11-21 19:56 CDMX

- 22-nov 07:00, 13:30 y 17:00: ocupados en main por Salem, Gutenberg y Ada; no duplicar.
- 22-nov 19:00: retirado por la política vigente desde 2026-11-02; no es slot autorizado.
- 22-nov 23:30: reservado para dato del día, que debe publicarse el propio 22-nov y cumplir la ventana de hasta 48 horas.
- 23-nov 07:00: Nudillos ya programado en main.
- 23-nov 13:30: lunes no es día preferente para mediodía; el proyecto de biodiversidad existente sigue FAIL/82, con SRC-002 `PENDING_SOURCE` y coordenadas no verificadas.
- 21-nov 23:30 Fentale: DOI actualizado a `VERIFICADO_CROSSREF` en el storyboard, pero el artículo es del 19-nov y no cumple la regla de dato del día para el 21-nov. No promover.

**Decisión:** no hay slot libre y autorizado con candidato, fuente primaria, mapa real y QA suficiente. No se creó storyboard nuevo, no se escribió en cola y no se disparó el workflow.
