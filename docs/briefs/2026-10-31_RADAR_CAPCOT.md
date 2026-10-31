# Radar CAPCOT — 31 de octubre de 2026

**Repositorio:** `marcojpad-hash/capcot-capsulas-imaginantes`  
**Rama:** `feature/capcot-video-discovery-continuity`  
**Corte:** 2026-10-31, consulta de actualidad y fuentes primarias.  
**Entrega:** investigación y preproducción textual; sin imágenes, voz, video, render ni publicación.

## 1. Google Trends México

### Observado
- Página oficial Trending Now, México, ventana de últimas 24 horas.
- La captura consultada muestra **216 tendencias** en total y 25 resultados por página.
- Los primeros resultados están dominados por fútbol, celebridades, actualidad general y entretenimiento: Puebla–Pumas, San Luis–Atlas, Juárez–Querétaro, Warriors–Lakers, Inés Gómez Mont, entre otros.
- No aparece una tendencia científica inequívoca entre los primeros 25 resultados visibles.
- No se fuerza una conexión artificial entre esas búsquedas y las noticias científicas.

Fuente oficial: https://trends.google.com/trending?geo=MX&hl=es

### RSS: resultado real de la lectura
Se intentó recuperar cada URL declarada en `scripts/tendencias.py`. El lector de esta ejecución no pudo procesar varios feeds XML; no se afirma que se haya parseado su XML.

| Feed | Resultado observado |
|---|---|
| ScienceDaily — Science | `CRAWL_UNEXPECTED_CONTENT_TYPE` |
| ScienceDaily — Health | `CRAWL_UNEXPECTED_CONTENT_TYPE` |
| ScienceDaily — Space Time | `CRAWL_UNEXPECTED_CONTENT_TYPE` |
| Phys.org | `CRAWL_UNEXPECTED_CONTENT_TYPE` |
| NASA News Release | Se recuperó un fragmento cuyo ítem visible está fechado **2026-09-01**; la extracción fue parcial y no permite confirmar si el feed contiene otros ítems recientes |
| ESA Space Science | `CRAWL_UNEXPECTED_CONTENT_TYPE` |
| Nature RSS | `CRAWL_UNEXPECTED_CONTENT_TYPE` |
| EurekAlert | `CRAWL_NOT_FOUND` |
| SINC | `CRAWL_NOT_FOUND` |
| UNAM Global | `CRAWL_UNEXPECTED_CONTENT_TYPE` |
| Google Trends RSS MX | `CRAWL_UNEXPECTED_CONTENT_TYPE` |

Respaldo aplicado: se consultó la página oficial Trending Now de Google Trends. La página HTML sí fue legible. Los feeds XML no se presentan como procesados.

## 2. Candidatos científicos dentro de la ventana

Ventana editorial: publicaciones originales fechadas del **24 al 31 de octubre de 2026**. Los cuatro DOI siguientes devolvieron registros `status=ok` en la API REST de Crossref; se cotejaron título, revista y fecha con los registros editoriales o comunicados institucionales. Cuando el texto completo del editor bloqueó el acceso automatizado, se declara y se usa el comunicado oficial para las afirmaciones de detalle.

| Prioridad | Estudio original y fecha | Línea CAPCOT | Novedad científica observada | Señal Trends | Oportunidad editorial y riesgo |
|---|---|---|---|---|---|
| **1 — principal** | **Rapid longitudinal flights cause time shifts and Sun compass error**, *Science*, 29-oct. DOI [10.1126/science.adz2542](https://doi.org/10.1126/science.adz2542). Crossref: `status=ok`; título y DOI coinciden; registro creado 29-oct. | Naturaleza / bichos; actualidad científica; comportamiento animal. | 20 años de GPS de 1,045 pardelas pichonetas y 3,688 viajes. En vuelos rápidos hacia el este, el reloj interno puede quedar hasta una hora detrás del tiempo solar local; las desviaciones observadas concuerdan con errores de brújula solar. | No detectada en los primeros 25 resultados. | Gancho claro por analogía con jet lag y visualización de navegación. No afirmar síntomas humanos ni que las aves se pierden inevitablemente. |
| 2 | **Cometary impacts an unlikely pathway towards the origins of life on Earth**, *Scientific Reports*, 28-oct. DOI [10.1038/s41598-026-74214-y](https://doi.org/10.1038/s41598-026-74214-y). Crossref: `status=ok`; publicación online 28-oct. | Origen de la vida; astronomía; química prebiótica. | Modelos de impactos y dinámica cometaria indican que entregar moléculas prebióticas en concentraciones útiles habría sido un evento extremadamente raro; los compuestos orgánicos frágiles pueden destruirse en impactos hiperveloces. El análisis se centra, entre otros elementos, en HCN. | No detectada. | Gran gancho contra una idea conocida. No decir que ningún cometa aportó moléculas ni que el origen terrestre de la vida quedó resuelto. |
| 3 | **A Martian meteorite that formed ≥4.1 billion years ago samples Mars’ early crust and mantle**, *Science*, 29-oct. DOI [10.1126/science.adz5646](https://doi.org/10.1126/science.adz5646). Crossref: `status=ok`; título/DOI coinciden; registro creado 29-oct. | Ciencia planetaria; geología; historia de Marte. | Teghaza 001 es una roca ígnea marciana de al menos 4.1 mil millones de años. Minerales alterados por agua y mediciones isotópicas apuntan a interacción con fluidos enriquecidos en oxígeno-18 antes de que la roca fuera expulsada al espacio. | No detectada. | Muestra excepcional para contar la geología temprana de Marte. Es una sola roca; no prueba vida ni demuestra que todo Marte fuera húmedo. |
| 4 | **Boredom in the museum: levels, antecedents, and consequences**, *Scientific Reports*, 27-oct. DOI [10.1038/s41598-026-74062-w](https://doi.org/10.1038/s41598-026-74062-w). Crossref: `status=ok`; publicación online 27-oct. | Línea social/educación (futura); psicología del aprendizaje informal. | Tres estudios, 1,269 participantes de 18–91 años; aburrimiento medio de 1.74/5. Tanto la sobrecarga como la falta de estímulo se relacionaron con más aburrimiento; quienes se aburrían aprendían menos durante la visita. | No detectada. | Ángulo cercano a experiencias cotidianas y diseño de museos. Muestra centrada en dos museos de Viena; no generalizar a todos los museos o públicos. |

### Candidatos revisados y no contados
- **Lumina / simulación cosmológica**, difundida por MIT el 26-oct.: el registro Crossref consultado muestra fecha impresa 13-oct. y no se confirmó una fecha de publicación online dentro de la ventana. No se cuenta como publicación original reciente hasta resolver esa discrepancia.
- **Flujo de falla antiguo**, difundido en prensa el 27-oct.: el DOI corresponde a un artículo publicado en junio de 2026. La fecha de la nota no convierte al paper en nuevo.
- **Herramienta de evacuación por tsunami**, difundida el 26-oct.: el paper tiene fecha 23-oct., fuera del corte conservador 24–31 oct.
- **Quantum skyrmions**, difundido en prensa el 30-oct.: el registro bibliográfico consultado no confirma una publicación original dentro de la ventana; no se usa como candidato elegible.

## 3. Candidato principal: pardelas y desfase de la brújula solar

### Observado
- *Science* publicó el estudio de Patrick Lewin y colaboradores el 29-oct-2026. Crossref devuelve `status=ok` para el DOI y coincide el título.
- El comunicado de University of Oxford, fechado 30-oct en la página, informa 20 años de GPS de 1,045 pardelas y 3,688 viajes de alimentación.
- En regresos rápidos hacia el este, el reloj interno puede quedar retrasado hasta alrededor de una hora respecto al tiempo solar local.
- Las trayectorias mostraron desviaciones sistemáticas compatibles con la hipótesis del compás solar; Oxford comunica desviaciones de hasta aproximadamente 15°.
- El estudio no demuestra efectos equivalentes al jet lag humano sobre salud o supervivencia. Oxford pide más investigación.
- El comunicado estima, como ejemplo modelado, unos 5 km extra para un regreso desde 1,000 km con error medio de 7° y corrección continua; no se usa como cifra universal en el guion.

### Cartografía
- Pin de Skomer Island: **51.7375 N, -5.2967 W**, ficha Getty Research Institute TGN 1009194.
- Skomer es una colonia conocida de pardelas pichonetas; el pin es contexto geográfico, no una ruta GPS individual ni la ubicación de todos los sujetos.
- El mapa muestra región amplia del Atlántico nororiental y un punto real. No dibuja trayectorias individuales inventadas.

### Inferencia narrativa
«Jet lag» es una analogía útil para explicar la diferencia entre reloj interno y hora solar local. No implica que las aves tengan todos los síntomas humanos.

### Recomendación
Mantener el paquete ya existente de pardelas como candidato principal: el mecanismo es comprensible, hay una serie larga de datos GPS, un giro visual claro y un riesgo editorial controlable. El guion conserva la cautela sobre la analogía y la capacidad de corrección de las aves adultas.

## 4. Paquete en cola y comprobaciones

Archivo: [`cola/entrada/2026-10-31_pardelas-jetlag-solar.json`](../../cola/entrada/2026-10-31_pardelas-jetlag-solar.json)  
Fuentes: [`cola/entrada/2026-10-31_pardelas-jetlag-solar_fuentes.md`](../../cola/entrada/2026-10-31_pardelas-jetlag-solar_fuentes.md)

- Estructura: `historia`.
- Estilo: `papel_rasgado_capas`; prompt base literal del catálogo.
- 8 escenas, 218 palabras, 78 s de escenas + 6 s de cortinilla = **84 s**.
- Voz declarada: edge-tts `es-MX-JorgeNeural`, +7 %, −2 Hz.
- Se añadieron metadatos `style_id`, idioma y voz por escena; capa mapa con coordenadas Getty TGN y capas de dato.
- Los ocho nombres de frame se declaran como **pendientes de generación por Grok**. No existen frames en esta entrega.
- La comprobación estructural de esta ejecución confirma 8 escenas, 218 palabras, duración dentro del rango, arcos obligatorios, prompts con prompt_base literal, source_ids resolubles y presencia de mapa/dato. Esto no equivale al QA oficial.

### Rotación y cupo
`data/temas_del_dia.json` y `data/rotacion.json` disponibles en la rama llegan hasta **2026-10-28**; `data/publicaciones.json` llega hasta **2026-10-26**. Se inspeccionaron, pero no se modificaron. Por eso no puede certificarse que estructura, estilo, música y tema sean únicos frente a todas las cápsulas del 29–31 oct. El estilo y la estructura elegidos sí difieren de las dos cápsulas externas conocidas del 30-oct, pero falta el registro completo del 31-oct.

## 5. Seguimiento técnico: Meta y Google Trends

Se comparó con `docs/INVESTIGACION_API_META_Y_GOOGLE_TRENDS.md` (corte 2026-10-31).

- **Meta Graph API / Instagram Insights / Facebook Pages Insights:** no se encontró un cambio nuevo verificable que justifique modificar el informe. Las páginas oficiales del changelog de Instagram y Page Insights devolvieron 429 o no estuvieron disponibles para el lector. Se conserva el último estado documentado: nombres de métricas y disponibilidad deben probarse contra la versión y cuenta autorizadas.
- **Google Trends API:** la documentación oficial sigue presentando acceso alfa limitado, ventana móvil de cinco años, agregaciones diaria/semanal/mensual/anual, regiones/subregiones y escala consistente entre solicitudes. No se observó una nueva apertura general ni un cambio de capacidades. El RSS MX sigue siendo la señal diaria gratuita, pero esta ejecución no pudo leer su XML.

**Decisión:** no reescribir el informe técnico porque no se verificó un cambio nuevo sustentado.

## 6. Handoff

- **ChatGPT:** investigación, verificación bibliográfica, brief, guion y storyboard textual.
- **Grok Bot:** cotejar la rotación completa, correr `scripts/validar_storyboard.py --check-doi`, generar frames/voz/música, ejecutar QA oficial y decidir si publica.
- No se publicó ni programó contenido. No se tocaron `main`, motor U6, archivos canónicos ni `data/*.json`.
