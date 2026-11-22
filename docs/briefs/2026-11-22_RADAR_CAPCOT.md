# Radar CAPCOT — 22 de noviembre de 2026

**Corte de investigación:** 21-nov-2026, 12:03 CDMX  
**Rama de trabajo:** `feature/capcot-video-discovery-continuity`  
**Estado:** investigación y preproducción textual; sin medios, sin promoción y sin publicación.

## Ocupación de slots

La reconciliación entre la rama de trabajo y `main` deja este estado:

| Fecha | Slot CDMX | Evidencia | Decisión |
|---|---:|---|---|
| 21-nov | 07:00 | Homo erectus, proyecto en feature | OCUPADO |
| 21-nov | 13:30 | Oxoboranos, registro de publicación en main | PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR |
| 21-nov | 17:00 | Púlsar gamma, proyecto en feature | OCUPADO |
| 21-nov | 19:00 | Robot orbital, registro de publicación en main | PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR |
| 21-nov | 23:30 | Fentale, proyecto en feature | OCUPADO |
| 22-nov | 07:00 | Voyager 1, proyecto en feature | OCUPADO |
| 22-nov | 13:30 | Sin proyecto, cola, salida ni publicación visible en ambas ramas | LIBRE; seleccionado abajo |
| 22-nov | 17:00 | Yubarta, proyecto en feature | OCUPADO |
| 22-nov | 19:00 | Sin ocupación visible en ambas ramas | LIBRE; no seleccionado |
| 22-nov | 23:30 | Sin ocupación visible en ambas ramas | LIBRE; reservado a dato del día con fuente del mismo 22-nov |

**Alcance:** `registro_editorial.py` inventaría la rama desde la que se ejecuta. La comprobación contra `main` sigue siendo una reconciliación separada y obligatoria: la copia de `data/publicaciones.json` en feature no contiene los dos registros de main del 21-nov.

## Ingesta RSS y Trends

Se intentaron los diez feeds definidos en `scripts/tendencias.py` y Google Trends RSS México. Los feeds XML/RSS no entregaron un cuerpo utilizable en esta interfaz; se registran los errores observados, sin sustituirlos por datos inventados:

| Fuente | Resultado literal / observable |
|---|---|
| ScienceDaily science | `Unsupported content-type: application/xml` |
| ScienceDaily health | `Unsupported content-type: application/xml` |
| ScienceDaily space | `Unsupported content-type: application/xml` |
| Phys.org | `Unsupported content-type: text/xml` |
| NASA RSS | `Unsupported content-type: application/rss+xml` |
| ESA Space Science RSS | `404 Not Found` |
| Nature RSS | `Unsupported content-type: application/rss+xml` |
| EurekAlert | Sin cuerpo parseable devuelto por la apertura del feed |
| Agencia SINC | Sin cuerpo parseable devuelto por la apertura del feed |
| UNAM Global | Sin cuerpo parseable devuelto por la apertura del feed |
| Google Trends RSS México | Sin cuerpo parseable devuelto por la apertura del feed |
| Respaldo de descarga de ScienceDaily | `download failed` |

Se usaron páginas oficiales y artículos primarios como respaldo. El fallo de un feed no se trató como ausencia de noticias.

## Candidatos recientes

### 1. AT 2025abao — fusión dentro de una envoltura común
- **Fuente primaria:** Nature, *An inspiral of a star inside a common envelope with its giant companion*, 18-nov-2026.
- **DOI:** [10.1038/s41586-026-11221-z](https://doi.org/10.1038/s41586-026-11221-z).
- **Respaldo oficial:** [NASA Science — Data Clinches First-of-Its-Kind Stellar Merger](https://science.nasa.gov/missions/webb/nasa-data-clinches-first-of-its-kind-stellar-merger/).
- **Coordenadas:** NASA publica RA 00:38:48.60 y Dec +40:46:08.23 para AT 2025abao. La conversión directa es RA 9.70250°, Dec +40.76895°; se conservan como coordenadas celestes, no geográficas.
- **Observación:** el brillo aumentó gradualmente durante unos siete años; Webb observó el polvo 47 días después del pico.
- **Cálculo:** 0.7 M☉ / 7 M☉ ≈ 0.10; la compañera tiene aproximadamente una décima parte de la masa estimada de la gigante.
- **Inferencia:** las observaciones multibanda respaldan la interpretación de evolución de envoltura común y fusión; no son una grabación directa del instante.
- **Recomendación:** SELECCIONADO para 22-nov, 13:30. El DOI resolver redirigió a la página Nature; el acceso a la página final quedó limitado por el intermediario. Crossref API no entregó respuesta utilizable en esta sesión.


### 2. Intensificación del uso agrícola tropical y multidiversidad
- **Fuente primaria:** Nature, *Tropical land-use intensification restructures biodiversity*, publicado 18-nov-2026.
- **DOI:** [10.1038/s41586-026-11298-6](https://doi.org/10.1038/s41586-026-11298-6).
- **Datos asociados:** Figshare, [10.6084/m9.figshare.31784410](https://doi.org/10.6084/m9.figshare.31784410), publicado 19-nov-2026.
- **Observación:** 24 grupos taxonómicos, 40.049 especies/OTU, 32 parcelas en dos paisajes de Jambi, Sumatra, comparando bosque, agroforestería de caucho, caucho y palma aceitera.
- **Cálculo publicado:** la multidiversidad de paisaje cae aproximadamente 78% en monocultivos y la multidiversidad local cerca de 50%. Son índices compuestos estandarizados, no porcentajes de especies individuales desaparecidas.
- **Inferencia:** la intensificación reorganiza la composición; el paper no encuentra una homogeneización consistente para todos los grupos.
- **Mapa:** Extended Data Fig. 1 muestra las 32 parcelas y los paisajes Bukit Duabelas y Harapan, pero la figura no publica coordenadas numéricas. El dataset Figshare fue identificado, pero su inventario de archivos no pudo recuperarse en esta sesión.
- **Decisión:** CANDIDATO prioritario para 22-nov 19:00 si se recuperan coordenadas de parcela verificables. Estado actual `PENDING_MAP_COORDINATES`; no crear storyboard ni sustituir parcelas por centroides.

### 3. Egoviruses — parientes cercanos de los poxvirus en metagenomas intestinales
- **Fuente primaria:** Nature, *Closest relatives of poxviruses prevail in human and animal guts worldwide*, 18-nov-2026.
- **DOI:** [10.1038/s41586-026-11283-z](https://doi.org/10.1038/s41586-026-11283-z).
- **Observación:** el estudio describe linajes virales relacionados con poxvirus en conjuntos de datos intestinales.
- **Límite:** la predicción de hospedadores no equivale a demostrar infección humana; la distribución publicada no proporciona puntos geográficos precisos aptos para el mapa exigido.
- **Decisión:** CANDIDATO; `PENDING_MAP_COORDINATES`. No crear storyboard ni convertir presencia en metagenomas en afirmación de enfermedad.

### 4. Hielo antiguo más allá de Neptuno
- **Fuente primaria:** Science Advances, DOI [10.1126/sciadv.aeg1602](https://doi.org/10.1126/sciadv.aeg1602), publicado 11-nov-2026.
- **Respaldo oficial:** NASA publicó la explicación el 18-nov-2026.
- **Observación:** el trabajo analiza partículas de polvo interplanetario y proporciones isotópicas compatibles con material formado en regiones frías del Sistema Solar exterior.
- **Límite:** el paper tiene diez días al corte y no se obtuvo una coordenada puntual de origen para un mapa sin inventar ubicación.
- **Decisión:** CANDIDATO NO SELECCIONADO; no usar para 23:30 y no crear storyboard sin mapa respaldado.

### 5. BepiColombo — fase de inserción orbital en Mercurio
- **Fuente oficial:** ESA, *Quick look at Mercury orbit insertion*.
- **Observación:** la página de misión identifica el 21-nov-2026 como fecha de la fase de inserción; al corte de 12:03 CDMX no se encontró confirmación oficial de resultado final.
- **Decisión:** `PENDING_EVENT_CONFIRMATION`. No narrar éxito antes de confirmación; tampoco es candidato para el dato del día del 22-nov sin una publicación del propio 22-nov.

### 6. Sonificación de estrellas bebé por Chandra
- **Fuente oficial:** NASA/Chandra, publicación 17-nov-2026.
- **Observación:** paquete de sonificación de datos astronómicos, no un hallazgo nuevo independiente.
- **Decisión:** NO SELECCIONADO; material audiovisual de divulgación, no una historia científica nueva con evidencia y mapa suficientes.

## Paquete desarrollado

- **Proyecto:** `2026-11-22_bao-estrella-fusion-andromeda`
- **Fecha objetivo / slot:** 2026-11-22 / 13:30 CDMX
- **Estilo:** `art_deco_poster`, prompt_base copiado literalmente del catálogo.
- **Narración:** 192 palabras; 8 escenas; 78 s de escenas + 6 s de cortinilla = 84 s.
- **Gancho:** “Bao llevaba años cambiando de brillo” (6 palabras).
- **Mapa:** punto celeste AT 2025abao con RA/Dec publicados por NASA y conversión explícita a grados.
- **Dato/gráfico:** masas estimadas de 7 M☉ y 0.7 M☉; observación de Webb 47 días después del pico.
- **Voz:** es-MX-JorgeNeural, rate +7%, pitch -2Hz.
- **Cierre hablado:** “Esto fue Datos y ociosidades.”
- **Estado:** borrador en `proyectos/`; `approved_assets=[]`; `export.render_status=NOT_GENERATED`; `publicacion.status=PENDIENTE_DECISION_GROK`.
- **QA:** no se creó `narrative_qa`; falta la pasada independiente en frío. No se creó entrada de cola ni estado Grok.

## Pendientes de compuerta
1. Auditor distinto del redactor: leer solo la narración concatenada y registrar los siete checks; hasta entonces FAIL/score 0 por revisión independiente ausente.
2. Ejecutar validador estructural real y verificación DOI independiente en un entorno con acceso al repositorio.
3. Reconciliar siempre `main` y feature antes de considerar libre un slot; no usar el inventario de una sola rama como fuente completa.
4. Revisar 22-nov 19:00 y 23:30 en el siguiente corte; 23:30 requiere dato publicado el mismo día y dentro de 48 horas.

## Separación de hechos
- **Observación:** brillo gradual, erupción, polvo infrarrojo y coordenadas publicadas.
- **Cálculo:** conversión RA/Dec a grados y razón aproximada de masas 0.10.
- **Inferencia:** la envoltura común y la fusión son la interpretación del equipo del paper.
- **Recomendación editorial:** usar AT 2025abao en 22-nov 13:30; mantener libres los demás slots hasta tener mapa y fuente temporalmente aptos.


---

## Corrección de ocupación desde main — 2026-11-21, corte 15:55 CDMX

La tabla original de este radar no había reconciliado los tres horarios de main. El plan de producción de main, `docs/briefs/2026-11-21_PRODUCCION_SEMANA_23-28nov.md`, registra para el domingo 22 de noviembre: Salem 07:00, Gutenberg 13:30 y Ada 17:00 (programación reportada desde YouTube). Por tanto, los tres slots de la rama feature quedan bloqueados:

- 07:00 — Voyager 1: `CONFLICTO_DE_SLOT_ENTRE_RAMAS` + `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`.
- 13:30 — Bao: `CONFLICTO_DE_SLOT_ENTRE_RAMAS` + `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`.
- 17:00 — Yubarta: `CONFLICTO_DE_SLOT_ENTRE_RAMAS` + `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`.

No se reasigna ninguno a otra hora. El slot 19:00 permanece libre en el plan consultado; 23:30 sigue reservado para dato del día, sin candidato seleccionado. La programación de 22-nov está documentada en main, pero los IDs de plataforma de esos tres slots no aparecen en `data/publicaciones.json`; se conserva el bloqueo preventivo y no se afirma una verificación independiente de plataforma.

Para el 23-nov, main registra Nudillos a las 07:00; el proyecto de biodiversidad a las 13:30 no comparte ese slot. Sigue `NOT_DISPATCHABLE` por QA narrativo FAIL/82 y fuente suplementaria `PENDING_SOURCE`.


## Corrección de auditoría — 2026-11-21 19:56 CDMX

Esta sección supersede cualquier nota anterior de este radar que indicara que aún no existía `narrative_qa` para los tres proyectos del 22-nov.

| Proyecto | Slot | QA actual | Estado de promoción |
|---|---:|---|---|
| `2026-11-22_voyager-1-un-dia-luz` | 07:00 | FAIL 83; `FECHA_DE_HITO_Y_CONFIRMACION_CONFUNDIDAS` | NOT_DISPATCHABLE |
| `2026-11-22_bao-estrella-fusion-andromeda` | 13:30 | FAIL 84; `STAKES_NO_EXPLICADOS` | NOT_DISPATCHABLE |
| `2026-11-22_yubarta-genoma-soplo` | 17:00 | PASS 90; siete checks true y flags vacías | NOT_DISPATCHABLE por conflicto de slot |

La rama `main` contiene el plan de producción del 22-nov con Salem 07:00, Gutenberg 13:30 y Ada 17:00. Los tres slots de esta rama chocan con esa programación: `CONFLICTO_DE_SLOT_ENTRE_RAMAS`. No se duplica, cancela ni promueve ninguno.

La propuesta de 22-nov 19:00 tampoco queda autorizada: la política vigente en `main/data/horarios.json` retiró el slot 19:00 el 2026-11-02 y, desde el 2026-11-16, define ventanas 06:30–07:30 y 13:00–14:30, más el fijo 23:30 para dato del día. El slot 23:30 exige fuente publicada el mismo día y dentro de 48 horas; se espera la fecha del 22-nov para seleccionar ese dato.

Para los tres proyectos, `cola/estado/<project_id>.json` devolvió 404: `RECEPCION_GROK_NO_CONFIRMADA`. No hay copias planas en `cola/entrada/`; el selector del workflow no toma storyboards anidados de `proyectos/`. No se disparó el workflow ni se envió payload.


## Actualización de radar — 2026-11-22 01:58 CDMX

Esta actualización supersede las notas anteriores que dejaban 19:00 como slot libre o consideraban libre el 23-nov 13:30. El snapshot más reciente de main ocupa 23-nov 13:30 con Rosetta; 19:00 fue retirado de la política. No se altera programación preexistente.

### Recuperación de feeds

Se intentó consultar por HTTP directo las ocho fuentes RSS de `scripts/tendencias.py` y Google Trends México. Los nueve endpoints devolvieron:

`URLError: <urlopen error [Errno -3] Temporary failure in name resolution>`

El script no se ejecutó dentro del repositorio; este es el error de las solicitudes directas de la sesión. Se usaron páginas oficiales como respaldo. Crossref API y resolvedor también quedaron inaccesibles por el mismo fallo de resolución DNS; ningún DOI se marcó como verificado por Crossref en este corte.

### Candidatos recientes

| Candidato | Fuente primaria / fecha | Dato y límite | Estado |
|---|---|---|---|
| Nubes crepusculares de Curiosity | NASA Photojournal, 20-nov-2026 — https://science.nasa.gov/resource/curiosity-spots-drifting-twilight-clouds/ | Imagen tomada el 31-oct-2026, sol 5061. NASA indica que estas nubes aparecen durante un periodo corto cada otoño sobre Gale Crater. Coordenada de referencia del aterrizaje: 4.6°S, 137.4°E; no representa la posición exacta de la nube. | Candidato para slot regular futuro; no usar como noticia del 22-nov |
| Floración del desierto de Atacama | NASA Earth Observatory, 19-nov-2026 — https://earthobservatory.nasa.gov/ | Comparación Landsat 8/9 de 14-sep y 24-oct-2026. NASA compara el episodio con 13 floraciones detectadas entre 1981–2015 y lo describe como posiblemente el más extenso de la era satelital. | Candidato; falta slot regular confirmado |
| Agua antigua más allá de Neptuno | NASA Science, 18-nov-2026; artículo en Science Advances, 11-nov-2026 — https://doi.org/10.1126/sciadv.aeg1602 | Doce partículas de polvo estratosférico; el origen en el cinturón de Kuiper se infiere por huellas de partículas energéticas, no por muestreo directo del cinturón. | PENDING_CROSSREF; no crear storyboard |
| Dos especies de tardígrados marinos | Senckenberg / ZooKeys, 20-nov-2026 — https://doi.org/10.3897/zookeys.1295.205902 | Dos especies descritas en el monte submarino Senghor. | NO_DUPLICAR: ya existe una cápsula de tardígrados en salidas del 24-oct |
| Colores de Júpiter en APOD | NASA APOD, 22-nov-2026 — https://apod.nasa.gov/apod/ap261122.html | Publicación del día sobre una imagen Juno del paso 14 de 2018; no es una observación nueva de 2026. | NO_DUPLICAR: ya existe proyecto/salida Juno del 29-oct |

### Decisión de slots

- 22-nov 23:30 no aparece ocupado en el snapshot de main, pero el APOD de Juno es la única pieza oficial encontrada con fecha de publicación del día y duplica la línea Juno ya trabajada. No se selecciona.
- Los slots regulares 07:00 y 13:30 del 22–29 nov aparecen ocupados en el snapshot de main.
- 1-dic no se considera libre: main todavía no contiene un plan que confirme ese horizonte.
- No se creó storyboard ni se promovió nada. El control de cola y la auditoría de los 19 proyectos quedan en `docs/briefs/2026-11-22_CONTROL_COLA.md`.


## Actualización de shortlist — 2026-11-22, 04:00 CDMX

### Candidato nuevo de respaldo (sin slot)

**Intermediarios de amiloide-β con funciones distintas**  
- Fuente primaria: Urbanek et al., *Nature Communications*, publicado en línea el 9-nov-2026. DOI indicado por el editor: `10.1038/s41467-026-79028-0`.  
- URL editorial/PDF: https://www.nature.com/articles/s41467-026-79028-0.pdf  
- Resultado observado: el estudio identifica dos poblaciones funcionalmente distintas de intermediarios Aβ42 en ensayos con péptido recombinante, un modelo knock-in de Alzheimer en ratón y tejido cerebral humano post mortem. Ambas pueden dañar membranas; solo una se convierte en placas. La intervención farmacológica que redujo placas y mejoró cognición se probó en ratones, no demuestra eficacia terapéutica en personas.  
- Cálculo: no se añadió ningún cálculo independiente ni porcentaje derivado.  
- Inferencia editorial: el giro potencial es que “intermediario tóxico” y “placa” no son la misma etapa; requiere explicar con cuidado el límite entre observación en tejido humano y prueba de intervención en ratones.  
- Estado: `CANDIDATO_SIN_SLOT`; `PENDING_CROSSREF`. El endpoint Crossref y el resolvedor DOI no quedaron accesibles en esta sesión. No redactar storyboard hasta verificar DOI y disponer de slot libre.

### Exclusiones recientes
- Voyager 1 a un día-luz: fuente NASA del 19-nov confirma el hito del 18-nov, pero ya existe el proyecto `2026-11-22_voyager-1-un-dia-luz`; `NO_DUPLICAR`.
- Kilonova Catcher: iniciativa de ciencia ciudadana lanzada en 2019, no noticia ni descubrimiento reciente; descartada para el radar actual.

### Shortlist activa consolidada

1. Curiosity y las nubes crepusculares — NASA, 20-nov-2026; candidato para slot regular futuro.
2. Floración del desierto de Atacama — NASA Earth Observatory, 19-nov-2026; candidato, no apto como dato del día 22-nov.
3. Indicios de hielo antiguo más allá de Neptuno — NASA Science, 18-nov-2026 + *Science Advances*, 11-nov-2026; `PENDING_CROSSREF`.
4. Intermediarios Aβ — *Nature Communications*, 9-nov-2026; `PENDING_CROSSREF`.

Tardígrados marinos y APOD de Júpiter permanecen en el registro de descartes por duplicación. No se creó storyboard ni se reservó slot.

## Revisión adicional de actualidad — 22 nov 2026, corte 05:55 CDMX

### RSS y Google Trends — intento de esta ejecución

Se consultaron las URL definidas por `scripts/tendencias.py` y el RSS de Google Trends México. La lectura RSS directa no fue posible con el lector web; errores exactos observados:

- ScienceDaily ciencia, salud y espacio: `Unsupported content-type: application/xml`.
- Phys.org: `Unsupported content-type: text/xml`.
- NASA RSS: `Unsupported content-type: application/rss+xml`.
- Nature RSS: `Unsupported content-type: application/rss+xml`.
- UNAM Global RSS: `Unsupported content-type: application/rss+xml`.
- ESA Space Science RSS: `404 Not Found`.
- EurekAlert y Agencia SINC: `URL not accessible via this tool`.
- Google Trends RSS México: `URL not accessible via this tool`.
- Crossref REST API: `URL not accessible via this tool`.

No se ejecutó localmente `scripts/tendencias.py`: el clon shallow por GitHub falló con `fatal: unable to access 'https://github.com/marcojpad-hash/capcot-capsulas-imaginantes.git/': Could not resolve host: github.com`. Se usaron páginas oficiales y artículos primarios como respaldo; no se marcaron como consultados los feeds que no entregaron XML.

### Noticias indexadas con fecha 22-nov: comprobación de la fuente original

Las siguientes páginas aparecen fechadas el 22-nov en ScienceDaily, pero su fuente institucional o artículo primario es anterior. No cumplen el corte editorial de noticia del mismo día para el slot 23:30:

1. **Timina y daño UV en ADN.** ScienceDaily fecha la nota el 22-nov, pero el artículo PNAS DOI [10.1073/pnas.2615278123](https://doi.org/10.1073/pnas.2615278123) se publicó el 3-ago-2026 y el comunicado original de Texas A&M es del 10-oct-2026 ([comunicado](https://news.engineering.tamu.edu/news/2026/10/10/electrical-engineering-research-unlocks-dna-mystery/)). El experimento compara nucleobases bajo UVC controlado; no demuestra por sí solo supervivencia de organismos en la Tierra primitiva. **DESCARTADO_POR_FECHA_ORIGINAL**.
2. **Colapso estelar sin supernova.** La nota de ScienceDaily tiene fecha 22-nov, pero Caltech publicó el comunicado el 10-nov y *Physical Review D* publicó el artículo DOI [10.1103/mnzq-w1b5](https://doi.org/10.1103/mnzq-w1b5) el 10-nov-2026 ([Caltech](https://www.caltech.edu/about/news/astronomers-find-hints-of-star-population-that-failed-to-explode), [APS](https://journals.aps.org/prd/abstract/10.1103/mnzq-w1b5)). El artículo primario usa 153 observaciones de GWTC-4.0; no usar las 257 fusiones del resumen secundario como si fueran el tamaño de muestra del artículo. La hipótesis de supernovas fallidas es compatible con la distribución, no una observación directa de una estrella que colapsó sin explotar. **DESCARTADO_POR_FECHA_ORIGINAL**.
3. **Longevidad de Jonathan, la tortuga.** ScienceDaily fecha la nota el 22-nov, pero Cambridge publicó el comunicado y *Science Advances* el 7-oct-2026; DOI [10.1126/sciadv.adw8887](https://doi.org/10.1126/sciadv.adw8887) ([Cambridge](https://www.cam.ac.uk/research/news/genetic-analysis-of-the-worlds-oldest-land-animal-reveals-secret-of-living-194-years), [PubMed](https://pubmed.ncbi.nlm.nih.gov/42842650/)). **DESCARTADO_POR_FECHA_ORIGINAL**.
4. **Degeneración retiniana EFEMP1.** ScienceDaily muestra fecha 22-nov, pero Penn Medicine publicó el comunicado el 11-sep y *JAMA Ophthalmology* publicó el artículo el 10-sep-2026; DOI [10.1001/jamaophthalmol.2026.3828](https://doi.org/10.1001/jamaophthalmol.2026.3828) ([Penn Medicine](https://www.pennmedicine.org/news/new-disease-causes-night-blindness-peripheral-vision-loss), [JAMA](https://jamanetwork.com/journals/jamaophthalmology/fullarticle/2853776)). El estudio es una serie de tres familias no relacionadas más una familia comparadora; la prevalencia poblacional sigue desconocida. **DESCARTADO_POR_FECHA_ORIGINAL**.

El APOD oficial NASA del 22-nov presenta remolinos y colores de nubes jovianas en una imagen de Juno tomada durante el 14.º sobrevuelo cercano de 2018; la explicación reconoce que las moléculas responsables del color siguen sin identificarse con certeza ([NASA APOD](https://science.nasa.gov/image-article/apod-2026-november-22-swirls-and-colors-on-jupiter-from-juno/)). La fecha de la página es del día, pero no es un hallazgo nuevo. En rotación/publicaciones ya existe `2026-10-29_juno-choque-proa` (choque de proa de Juno en Júpiter): no es un duplicado científico exacto de los colores atmosféricos, aunque repite misión y planeta. Se descarta por falta de resultado nuevo y riesgo de reiteración editorial; no se etiqueta como duplicado exacto. No se encontró otra noticia primaria nueva del 22-nov que satisfaga fecha, rotación, fuente y mapa verificable.

### Decisión editorial

- Se conservan los cuatro candidatos del radar previo; no se añadió un quinto candidato solo por una republicación de una nota antigua.
- El slot 22-nov 23:30 permanece sin storyboard: no hay candidato que cumpla noticia primaria del mismo día y no duplicación.
- No se adelantó contenido al 23-nov. No se creó storyboard, QA, entrada de cola ni medio.
- Los DOI anteriores se verificaron en páginas editoriales/resolvedores cuando fue posible; **Crossref sigue PENDIENTE** porque la API no fue accesible. La verificación de un DOI en el editor no se presenta como respuesta de Crossref.


## Corte 08:05 CDMX — revalidación de slots, fuentes y QA

### RSS y tendencias
Se reintentaron las diez URL de `FEEDS_CIENCIA` en `scripts/tendencias.py` y el RSS de Google Trends México. No se obtuvo XML y no se ejecutó localmente el script. Errores del lector: ScienceDaily ciencia/salud/espacio `Unsupported content-type: application/xml`; Phys.org `Unsupported content-type: text/xml`; NASA y Nature `Unsupported content-type: application/rss+xml`; ESA `404 Not Found`; EurekAlert y SINC `URL not accessible via this tool`; UNAM Global `Unsupported content-type: application/rss+xml`; Trends RSS y Crossref REST `URL not accessible via this tool`. Son fallos del lector de esta sesión, no prueba de caída de todos los servidores.

Respaldo oficial: [Google Trends México, últimas 24 h](https://trends.google.com/trending?geo=MX&hl=es), 263 tendencias (25 por página). La primera página está dominada por fútbol y entretenimiento. Entre las primeras 25: `superluna` 2 mil+ (+1.000 %) y `desierto de Atacama` 1 mil+ (+200 %). Son bandas de búsqueda, no métricas CAPCOT; Atacama coincide con una nota previa, no con un hallazgo publicado hoy.

### Cinco candidatos publicados del 18 al 22 de noviembre

1. **Estatura y genética por etapa del desarrollo — 22-nov.** [Nature Communications, PDF primario](https://www.nature.com/articles/s41467-026-79465-x_reference.pdf), DOI impreso `10.1038/s41467-026-79465-x`. Hasta 72.704 niños MoBa y 574.580 mediciones desde nacimiento a 8 años; heredabilidad SNP 0,16 al nacer y 0,41 a los 8 años; tres grupos de señales con trayectorias diferentes. Relevancia alta; oportunidad alta. Riesgos: no convertir heredabilidad poblacional en porcentaje de la estatura individual; muestra de ascendencia europea y límites de generalización. URL editorial accesible; Crossref/resolvedor no respondió: `PENDING_RESOLVER`.
2. **Fenología foliar amazónica — 18-nov.** [Nature](https://www.nature.com/articles/s41586-026-11284-y), [PubMed 43052430](https://pubmed.ncbi.nlm.nih.gov/43052430/), DOI `10.1038/s41586-026-11284-y`. Sentinel-2 a 10 m; en 70,0 % del área amazónica analizada, la caída de hojas precede al reverdecimiento por al menos tres meses. Relevancia y oportunidad altas por la figura espacial. Riesgo: 70 % del área, no de árboles o especies; asociación ambiental no equivale a causalidad.
3. **Egovirus, parientes evolutivos de poxvirus — 18-nov.** [Nature](https://www.nature.com/articles/s41586-026-11283-z), DOI `10.1038/s41586-026-11283-z`. 85.123 ensamblajes metagenómicos, 12 genomas completos y 864 ensamblajes positivos; los autores proponen el orden Egovirales y predicen vínculos con eucariotas unicelulares digestivos. Relevancia alta; oportunidad alta. Riesgo: no afirmar infección de células humanas ni enfermedad; la relación con hospedadores es inferida.
4. **Código neural de la producción del habla en Wernicke — 19-nov.** [PubMed 43056455](https://pubmed.ncbi.nlm.nih.gov/43056455/), DOI `10.1126/science.aef8963`. Registros intracraneales, estimulación cortical y análisis de lesiones; la región temporal superior posterior izquierda participa antes del habla y codifica rasgos de palabras completas. Relevancia alta; oportunidad media-alta. Riesgo: no llamarlo lectura general de pensamientos ni tecnología clínica disponible.
5. **var2csa y malaria cerebral — 20-nov.** [Nature Communications](https://www.nature.com/articles/s41467-026-78682-8), DOI `10.1038/s41467-026-78682-8`. RNA-seq en 13 pares emparejados y conjuntos de 25 casos/55 controles. La transcripción de var2csa se asocia con malaria cerebral entre sitios; los autores aclaran que la asociación está medida a nivel de transcrito y no demuestra necesariamente traducción a antígeno. Relevancia alta; oportunidad media. Riesgo: muestra y contexto clínico específicos; no es prueba diagnóstica ni demuestra por sí sola causalidad clínica.

Estado por candidato: las cinco URL de fuente primaria o registro bibliográfico están accesibles; los cinco DOI quedan `PENDING_RESOLVER` porque Crossref/resolvedor no respondió en este corte. Ninguno se declara validado por Crossref. Tendencia, relevancia científica y oportunidad editorial se mantienen separadas.

### Ocupación y decisión de 23:30
- Feature: 07:00 Voyager 1; 13:30 fusión estelar BAO; 17:00 genoma de yubarta. Main confirma Salem 07:00, Gutenberg 13:30 y Ada 17:00. Se registra `CONFLICTO_DE_SLOT_ENTRE_RAMAS` y `NO_DUPLICAR`; no se reescriben los tres proyectos.
- 19:00 no es ventana activa en la política vigente; no se reasigna.
- 23:30 sigue activo como `slot_fijo_dato` en `main/data/horarios.json`, y no aparece ocupado en proyectos, salidas, cola, handoffs, programaciones ni publicaciones de ambas ramas. No existe `data/horario_2026-11-22.json` en feature ni main.
- El artículo de estatura es del 22-nov y el PDF primario está accesible, pero el DOI no pudo resolverse por Crossref/resolvedor. Además, los métodos identifican regiones de cohortes, no coordenadas exactas de participantes o reclutamiento; las anclas regionales no se han verificado. Estado 23:30: **`PENDING_SOURCE`**. No se crea storyboard adicional.
- La programación principal de main para el día ya tiene Salem/Gutenberg/Ada; las resubidas 14:30 y 21:00 no ocupan 23:30.

### QA narrativo preexistente — lectura literal
Los tres JSON sí contienen `narrative_qa`; no se modificaron.

| Proyecto | Estado | review_basis y fecha | Checks | critical_flags |
|---|---|---|---|---|
| `2026-11-22_voyager-1-un-dia-luz` | FAIL / 83 | `lectura_en_frio_solo_narracion`; `reviewed_at` ausente | Los siete checks son `true` | [`FECHA_DE_HITO_Y_CONFIRMACION_CONFUNDIDAS`] |
| `2026-11-22_bao-estrella-fusion-andromeda` | FAIL / 84 | `lectura_en_frio_solo_narracion`; `reviewed_at=2026-11-21T13:56:37-06:00` | Los siete checks son `true` | [`STAKES_NO_EXPLICADOS`] |
| `2026-11-22_yubarta-genoma-soplo` | PASS / 90 | `lectura_en_frio_solo_narracion`; `reviewed_on=2026-11-21`; `reviewed_at` ausente | Los siete checks son `true` | [] |

Los tres indican `reviewer_role=auditor_capcot_independiente`. Los tres `cola/estado/<project_id>.json` devolvieron HTTP 404: `RECEPCION_GROK_NO_CONFIRMADA`. No se escribieron estados ni se promovió ningún paquete.

### Seguimiento técnico
Graph API v27.0 frente a tabla heredada v26.0 y el estado alfa limitado de Google Trends ya están documentados; no cambiaron. La referencia actual de Page Insights muestra un aviso de deprecación para el 15-jun-2026, pero su página enlazada solo enumera fechas 2025 y 2024; el blog enlazado devolvió HTTP 429. La discrepancia quedó registrada en el informe técnico §9.11, sin inferir nombres de métricas ni cambiar integraciones.

**Decisión:** `NO_DUPLICAR` en los slots regulares ocupados; `PENDING_SOURCE` en 23:30. Se actualiza este radar existente. No se crea storyboard, no se escribe en cola, no se genera QA ni se producen medios.


### Corrección de precisión — 08:10 CDMX
Se ajustó la síntesis del candidato var2csa para distinguir asociación de transcripción y presencia de proteína/antígeno: el artículo informa asociación a nivel de transcrito y no demuestra necesariamente traducción a antígeno. También se hizo explícito el estado común de los cinco DOI: `PENDING_RESOLVER`; las URL primarias o bibliográficas están accesibles, pero no se declara validación Crossref.

## Reconsulta operativa — 22-nov-2026, 11:55 CDMX

### Feeds y respaldo

Se reintentaron los endpoints definidos en `scripts/tendencias.py` y Google Trends RSS México. El lector devolvió:

- ScienceDaily science, health y space: `(400) Unsupported content-type: application/xml`.
- Phys.org: `(400) Unsupported content-type: text/xml`.
- NASA News Release y Nature RSS: `(400) Unsupported content-type: application/rss+xml`.
- ESA Space Science RSS: `(404) Not Found`.
- EurekAlert, Agencia SINC y Google Trends RSS México: `URL ... is not accessible via this tool`.
- UNAM Global RSS: `(400) Unsupported content-type: application/rss+xml`.

Estos errores describen la limitación del lector RSS, no demuestran que las fuentes estén caídas. Como respaldo se consultó la página oficial de Google Trends México; las tendencias visibles estaban dominadas por fútbol/deportes y entretenimiento, sin una señal científica utilizable para seleccionar tema.

### Candidato primario y borrador

La página primaria de Nature Communications para **“The genetic and proteomic determinants of pediatric stature development and their link to adult height and type 2 diabetes”** está accesible y marca publicación el 22-nov-2026. El resumen respalda 72,704 niñas y niños noruegos, 574,580 mediciones, datos de UK Biobank, tres agrupaciones temporales, 106 proteínas asociadas con estatura prepuberal y el análisis de aleatorización mendeliana sobre diabetes tipo 2.

El DOI `10.1038/s41467-026-79465-x` permanece `PENDING_RESOLVER`: Crossref API y doi.org devolvieron `URL ... is not accessible via this tool`. La URL editorial primaria sí abre. El artículo se presenta como versión temprana de investigación aceptada y puede recibir ediciones.

Se creó el borrador `proyectos/2026-11-22_genes-estatura-etapas/storyboard.json` para el slot fijo 23:30, que no aparece ocupado en main ni en los registros de publicación del 22-nov. Tiene 8 escenas, 229 palabras y 84 s totales (78 s de escenas + 6 s de cortinilla). Usa `papel_stop_motion`, ausente de las 39 entradas de rotación consultadas y de los proyectos activos. El mapa marca únicamente sedes institucionales/administrativas en Oslo y Manchester; no representa ubicaciones de participantes.

Estado: `BORRADOR_EN_PROYECTOS`, no seleccionado, sin `narrative_qa`, sin medios, `approved_assets=[]`, `export.render_status=NOT_GENERATED` y `publicacion.status=PENDIENTE_DECISION_GROK`. No promover hasta verificar DOI/Crossref y completar la auditoría narrativa independiente.

