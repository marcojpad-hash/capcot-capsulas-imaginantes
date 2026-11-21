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
