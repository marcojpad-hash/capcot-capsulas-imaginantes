# Radar CAPCOT — 2026-11-01

**Corte:** 2026-11-01 14:20, CDMX  
**Rama:** feature/capcot-video-discovery-continuity  
**Ventana de publicación:** 2026-10-25 a 2026-11-01 (inclusive)  
**Rol:** investigación y preproducción textual; sin medios, publicación ni decisión editorial final.

## Resultado ejecutivo

El candidato principal es **One-minute frequency disturbances from unintended synchronization in cyber–physical power systems**, publicado en Nature Energy el 30-oct-2026. La historia tiene una pregunta única, una anomalía medible, una investigación local, una causa observada en una UPS y un límite de evidencia explícito. No aparece como tendencia directa en Google Trends México; se recomienda por actualidad científica y fuerza narrativa, no por popularidad de búsqueda.

El storyboard de trabajo queda en proyectos, no en cola: el flujo vigente separa al investigador del auditor. La promoción a cola requiere QA narrativo independiente PASS. No se añadió narrative_qa ni se simuló esa revisión.

## 1. RSS y Google Trends

### RSS definidos en scripts/tendencias.py

Se intentaron las URL configuradas. El lector web no aceptó los tipos XML/RSS; no se descargó ni parseó XML. Los fallos observados fueron:

| Fuente | URL | Resultado exacto |
|---|---|---|
| ScienceDaily | https://www.sciencedaily.com/rss/top/science.xml | HTTP 400 — Unsupported content-type: application/xml |
| ScienceDaily Salud | https://www.sciencedaily.com/rss/top/health.xml | HTTP 400 — Unsupported content-type: application/xml |
| ScienceDaily Espacio | https://www.sciencedaily.com/rss/space_time.xml | HTTP 400 — Unsupported content-type: application/xml |
| Phys.org | https://phys.org/rss-feed/ | HTTP 400 — Unsupported content-type: text/xml |
| NASA | https://www.nasa.gov/news-release/feed/ | HTTP 400 — Unsupported content-type: application/rss+xml |
| ESA | https://www.esa.int/rssfeed/Our_Activities/Space_Science | HTTP 400 — Unsupported content-type: application/rss+xml |
| Nature | https://www.nature.com/nature.rss | HTTP 400 — Unsupported content-type: application/rss+xml |
| EurekAlert | https://www.eurekalert.org/rss/news.xml | URL no accesible mediante la herramienta; sin código HTTP devuelto |
| SINC | https://www.agenciasinc.es/rss | URL no accesible mediante la herramienta; sin código HTTP devuelto |
| UNAM Global | https://unamglobal.unam.mx/feed/ | HTTP 400 — Unsupported content-type: application/rss+xml |

Google Trends RSS México, https://trends.google.com/trending/rss?geo=MX, devolvió: **URL no accesible mediante la herramienta**. No se afirma que se haya leído ni parseado ese RSS.

### Respaldo oficial: Trending Now México

Consulta de respaldo: [Google Trends — Tendencias actuales México](https://trends.google.com/trending?geo=MX&hl=es), vista de últimas 24 horas, corte aproximado 14:20 CDMX.

Observado en la primera página:
- América–Toluca: 500 mil+ búsquedas.
- Monterrey–Tijuana: 200 mil+.
- Día de los Muertos: 200 mil+.
- Pachuca–Tigres: 200 mil+.
- “1 de noviembre”: 20 mil+.
- “hora cd juarez”: 20 mil+; entre consultas relacionadas aparece “cambio de horario”.

La primera página está dominada por fútbol y Día de Muertos. No aparece una consulta científica o energética que valide directamente el candidato principal. “Cambio de horario” es una consulta relacionada con hora local, no evidencia de interés por oscilaciones de red. Los buckets de Trends son rangos aproximados, no conteos absolutos ni métricas de audiencia de CAPCOT.

## 2. Candidatos publicados en los últimos siete días

**Regla de verificación:** los artículos originales del editor muestran título, fecha, DOI y contenido bibliográfico en sus páginas indexadas. La apertura directa de Nature redirigió a idp.nature.com y devolvió HTTP 500; los intentos a doi.org y Crossref REST tampoco fueron accesibles en esta consulta. Por tanto, todos los DOI se mantienen **PENDIENTES**, no validados. Se conservan las URL primarias del editor para revisión. En el candidato principal, el comunicado institucional de Forschungszentrum Jülich sí se abrió y contrasta los datos locales.

| Candidato / fecha | Novedad y fuente primaria | Tendencia MX | Relevancia científica | Oportunidad editorial y público | Riesgos / verificación |
|---|---|---|---|---|---|
| **1. One-minute frequency disturbances from unintended synchronization in cyber–physical power systems** — 30-oct-2026. [Nature Energy](https://www.nature.com/articles/s41560-026-02144-0). DOI reportado: 10.1038/s41560-026-02144-0 (**PENDIENTE**). [Comunicado oficial de Forschungszentrum Jülich](https://www.fz-juelich.de/en/news/archive/press-release/2026/mystery-of-60-second-fluctuations-in-power-grids-solved). | Identifica un patrón de un minuto en doce redes de cinco continentes; el equipo rastrea una fuente concreta en una UPS y demuestra cómo el pulso llega hasta la conexión de 110 kV. El fabricante confirmó la autoprueba periódica como origen de los picos de corriente de esa UPS. | Sin señal directa. | Alta: conecta control digital, almacenamiento y estabilidad de redes eléctricas con mediciones y mecanismo identificable. | **Alta.** Público general interesado en ciencia/tecnología. Misterio causal y payoff claro; se puede explicar sin jerga extensa. | No afirmar que todas las oscilaciones globales sean causadas por UPS ni que exista peligro inminente de apagón. El patrón global se observa en doce redes; la UPS se rastrea en un campus. DOI pendiente; URL primaria indexada y comunicado institucional abierto. |
| **2. Low-voltage avalanche heterojunction phototransistor for infrared-to-visible upconversion** — 30-oct-2026. [Nature Photonics](https://www.nature.com/articles/s41566-026-02046-3). DOI reportado: 10.1038/s41566-026-02046-3 (**PENDIENTE**). | Un fototransistor InGaAs/InP con realimentación interna acciona directamente un LED ámbar a partir de infrarrojo débil; el artículo reporta emisión visible 17.000 veces más brillante que la luz infrarroja incidente a 6,4 nW/cm² y tensión de ruptura de 1,4 V. | Sin señal directa. | Alta: conversión infrarrojo-visible en estado sólido con baja tensión. | Alta-media. Público general con interés en tecnología y visión nocturna; imagen muy clara. | No decir que crea energía ni que el dispositivo ya sea unas gafas de visión nocturna. El cociente de brillo no equivale a eficiencia energética; es un prototipo. DOI pendiente. |
| **3. Durable reactive CO₂ capture exceeding 1,000 h via self-reinforcing molecular catalysts** — 30-oct-2026. [Nature Energy](https://www.nature.com/articles/s41560-026-02159-7). DOI reportado: 10.1038/s41560-026-02159-7 (**PENDIENTE**). | Un catalizador molecular de cobalto, tras una pérdida inicial de cerca de la mitad del Co, forma vacantes que contraen sitios vecinos y refuerzan la coordinación; el sistema opera más de 1.000 h a 50 mA/cm², con ~80 % de eficiencia faradaica hacia CO y 39 % de eficiencia energética a 2,9 V. | Sin señal directa. | Alta: aborda la durabilidad, un cuello de botella de captura y conversión electroquímica de CO₂. | Media. Público adulto interesado en clima/tecnología; el giro “pierde cobalto y se estabiliza” es narrable, pero exige explicación química. | Es una celda de laboratorio, no una planta industrial ni una solución ya escalada para retirar CO₂ atmosférico. No ocultar la eficiencia energética de 39 %. DOI pendiente. |
| **4. Declining spring production in the Barents Sea ice zone under climate forcing** — 26-oct-2026. [Nature Communications](https://www.nature.com/articles/s41467-026-79272-4). DOI reportado: 10.1038/s41467-026-79272-4 (**PENDIENTE**). | Con datos satelitales, informa una caída del 45 % en la producción primaria de primavera (abril–mayo) dentro de la zona de hielo del mar de Barents, entre 1998 y 2023; el mecanismo incluye menor disponibilidad de nitrato y luz. | Sin señal directa. | Alta: conecta nutrientes, hielo, calentamiento y base de la red alimentaria ártica. | Media-alta. Público de naturaleza/ciencia; visualmente fuerte, aunque requiere explicar producción primaria y nitrato. | No convertir el 45 % en una caída anual de todo el mar de Barents. El resultado es estacional y regional; las consecuencias tróficas son implicaciones, no un colapso ya observado. DOI pendiente. |
| **5. Overcoming circularity bias reveals a hidden linear DNA and RNA virosphere** — 26-oct-2026. [Nature Communications](https://www.nature.com/articles/s41467-026-79285-z). DOI reportado: 10.1038/s41467-026-79285-z (**PENDIENTE**). | Corrige un sesgo de herramientas metagenómicas que favorecía genomas circulares; recupera y valida 1.585 genomas virales lineales completos, un aumento de 21 veces en la completitud lineal reconocida por el método. | Sin señal directa. | Alta: revela diversidad viral que los criterios de calidad anteriores subestimaban. | Media. Público interesado en biología; giro metodológico atractivo, pero técnico. | El factor 21× no significa 21 veces más virus en la naturaleza. **Colisión editorial:** se acerca al tema de viroma de murciélagos propuesto para 31-oct/2-nov; no es la primera elección. DOI pendiente. |

## 3. Recomendación

**Candidato principal: el pulso de un minuto en redes eléctricas.**

La pregunta única es: ¿qué provoca una oscilación de un minuto en redes distintas? La promesa es mostrar cómo una autoprueba de UPS puede dejar una huella en la red. El stake real es el desgaste de equipos de regulación, no un apagón inminente. El giro es que una rutina de software, elegida para revisar baterías, puede coincidir con la de otros dispositivos. El límite es esencial: doce redes muestran el patrón, pero el rastreo causal detallado se realiza sobre una UPS concreta en Jülich.

**Alternativa:** el fototransistor infrarrojo-visible ofrece una visual más inmediata, pero el riesgo de confundir brillo con energía y prototipo con producto es mayor. El candidato de Barents es la alternativa de naturaleza, con el cuidado de no convertir un dato de primavera y una zona de hielo en un dato anual de todo el mar.

## 4. Rotación y colisiones editoriales

Lectura combinada de data/temas_del_dia.json, data/rotacion.json, data/publicaciones.json, data/cola.json, scripts/registro_editorial.py y los proyectos/colas/salidas recientes:

- La última cápsula del 31-oct, slot 23:30, usó papel_rasgado_capas y estructura historia.
- Los paquetes ya programados/propuestos para 1-nov incluyen Xolo, pulpo, cebolla, Baffin y tiburón; no se cuentan como publicaciones nuevas por esta ejecución.
- En el día 1-nov aparecen estilos teatro_sombras, carton_recortado, papel_recortado_popup, art_deco_poster y crayones_infantiles; la estructura registrada para esos paquetes es pregunta.
- Se selecciona risografia (propio), con prompt_base literal del catálogo, y estructura comparación. No repite el estilo de la cápsula anterior ni los estilos/estructura de los paquetes del día.
- El tema principal pertenece a actualidad científica/tecnología de redes; no duplica un título existente. Hay proximidad de categoría con sequías/energía renovable programada para 2-nov, pero el mecanismo es distinto: sincronización de autopruebas, no generación renovable ni sequía. La auditoría editorial puede decidir si conviene espaciar ambas piezas.
- data/cola.json conserva una entrada fallida de pardelas del 31-oct (rc=1, paquete nulo); no se interpreta como publicación ni se modifica.

## 5. Estado del storyboard de trabajo

Archivo de trabajo: proyectos/2026-11-01_red-electrica-pulso-minuto/storyboard.json

- Ocho escenas; narración concatenada: 190 palabras.
- Escenas: 78 s + cortinilla de fuentes: 6 s = 84 s.
- Arco: hook_medias_res → desarrollo → cierre_historia → reflexion_o_pregunta.
- Voz: edge-tts / es-MX-JorgeNeural / +7 % / -2 Hz / pausas continuas.
- Estilo: risografia (propio), prompt_base literal del catálogo; biblia visual y tipográfica fija.
- Mapa: pin contextual de Forschungszentrum Jülich en 50.905, 6.411944; representa el centro institucional, no los medidores ni la UPS.
- Capas: dato (12 redes/5 continentes; cuatro edificios; 110 kV) y mapa con fuente de coordenadas.
- Sin medios: approved_assets = []; export.render_status = NOT_GENERATED; no filename ni rutas de frames/audio/video/render.
- publicacion.status = PENDIENTE_DECISION_GROK.
- El borrador permanece en proyectos. La revisión narrativa independiente corresponde al auditor; sin PASS no se promueve a cola ni se declara preparado.

## 6. Seguimiento técnico Meta / Google Trends

Consulta de documentación oficial y comparación con docs/INVESTIGACION_API_META_Y_GOOGLE_TRENDS.md:

- Meta Graph API v26.0 changelog: la URL oficial no fue accesible mediante la herramienta.
- Instagram Insights: la página oficial devolvió HTTP 429 Too Many Requests; la referencia IG User Insights no fue accesible.
- Facebook Pages Insights: la página oficial devolvió HTTP 429 Too Many Requests.
- IG Media Insights: la referencia oficial no fue accesible.
- No se obtuvo evidencia oficial nueva suficiente para cambiar nombres de métricas, endpoints o permisos. No se usa un resumen secundario como contrato técnico.
- Google Trends API oficial continúa en alfa de acceso limitado; la documentación conserva ventana móvil de cinco años, agregaciones diarias/semanales/mensuales/anuales, regiones/subregiones y escalado consistente. No se encontró una apertura general ni un cambio relevante frente al informe vigente.

**Decisión técnica:** no reescribir docs/INVESTIGACION_API_META_Y_GOOGLE_TRENDS.md. El seguimiento de Meta queda pendiente de acceso a las páginas oficiales; el RSS y Trending Now son rutas de detección, no sustituyen Insights privados.

## 7. Observado, cálculo, inferencia y recomendación

- **Observado:** fechas y afirmaciones de los artículos originales; patrón de 60 s en doce redes; autoprueba confirmada por el fabricante para una UPS; cuatro edificios con UPS; comunicado institucional con 80 ubicaciones; Trends MX dominado por fútbol y Día de Muertos; errores RSS consignados arriba.
- **Cálculo:** 78 s de escenas + 6 s de cortinilla = 84 s; 190 palabras de narración. No se derivan métricas científicas nuevas.
- **Inferencia:** rutinas digitales sincronizadas pueden sumar picos de demanda; no se atribuye toda oscilación de red a UPS.
- **Recomendación:** priorizar el candidato principal por cadena causal y claridad narrativa, conservando los límites de evidencia y el estado pendiente del DOI.

## 8. Límites y próximos pasos

1. El RSS no pudo ser leído por esta vía; no se afirma parseo. Si el entorno de ejecución del script puede leerlo directamente, debe conservar su propio resultado y error.
2. Los DOI de los cinco candidatos quedan PENDIENTES hasta una consulta exitosa a Crossref o al resolvedor. No presentarlos como validados.
3. El auditor debe realizar lectura en frío independiente del storyboard, ocultando título, resumen, arco y notas. El investigador no añade narrative_qa ni se autoevalúa.
4. Solo con narrative_qa PASS podrá promoverse una copia a cola/entrada. Este borrador no está preparado, no está en cola y no ha sido aceptado por Grok.
5. No se modificaron data/*.json, el informe técnico de Meta/Google Trends, main, motores, ni se generaron medios o publicaciones.
