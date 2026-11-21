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
