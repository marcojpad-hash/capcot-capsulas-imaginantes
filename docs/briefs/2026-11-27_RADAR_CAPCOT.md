# RADAR CAPCOT — 2026-11-27

**Corte:** 27 de noviembre de 2026, 00:02 CDMX.  
**Estado:** investigación documental; ningún candidato cruza todavía todas las compuertas para storyboard.

## Método y fuentes

Se consultaron los feeds definidos en `scripts/tendencias.py` y Google Trends RSS México. Los feeds no entregaron cuerpos XML utilizables en esta ejecución:

| Feed | Resultado observado |
|---|---|
| ScienceDaily Science, Health y Space | HTTP 400 — Unsupported content-type |
| Phys.org | HTTP 400 — Unsupported content-type |
| NASA | HTTP 400 — Unsupported content-type |
| Nature RSS | HTTP 400 — Unsupported content-type |
| UNAM Global | HTTP 400 — Unsupported content-type |
| ESA Space Science | HTTP 404 |
| EurekAlert | URL not accessible |
| Agencia SINC | URL not accessible |
| Google Trends RSS México | URL not accessible |

**Respaldo oficial de tendencias:** la página HTML de Google Trends México mostró 252 tendencias en la ventana consultada. Las primeras 25 estaban dominadas por deportes, actualidad, clima y personalidades; no apareció una señal científica/natural clara para seleccionar un tema.

**DOI y resolvedor:** se consultaron páginas editoriales y se intentó acceso directo a Crossref y `doi.org`. El acceso al resolvedor no quedó disponible en esta ejecución. Los DOI que aparecen en páginas editoriales se conservan como referencias, pero **ninguno se marca VERIFICADO_CROSSREF**. `--check-doi` no se ejecutó.

## Candidatos

### 1. Drenaje histórico de turberas y forzamiento climático

- **Fuente primaria:** Nature, 25-11-2026. DOI: [10.1038/s41586-026-11339-0](https://doi.org/10.1038/s41586-026-11339-0). [Artículo editorial](https://www.nature.com/articles/s41586-026-11339-0).
- **Observación:** reconstrucción global de drenaje de turberas para 1800–2020. El estudio estima un forzamiento radiativo de 73 mW m⁻² (intervalo informado: 48–99 mW m⁻²), asociado a una superficie drenada de aproximadamente 0.4–0.5% de la superficie terrestre.
- **Cálculo CAPCOT:** ninguno. Las cifras anteriores son resultados reportados por el artículo, no cálculos independientes.
- **Inferencia:** una fracción pequeña de superficie puede tener un efecto climático desproporcionado por las emisiones asociadas al drenaje. No equivale a una predicción meteorológica local ni a una medición directa de cada turbera.
- **Recomendación:** prioridad alta. Tiene un arco visual claro —poca superficie, efecto grande— y permite cartografía global si se valida el dataset suplementario.
- **Estado de fuente:** `PENDING_CROSSREF`.

### 2. Producción de cemento mediante una ruta de plasma de carbono y microondas

- **Fuente primaria:** Nature, 25-11-2026. DOI: [10.1038/s41586-026-11313-w](https://doi.org/10.1038/s41586-026-11313-w). [Artículo editorial](https://www.nature.com/articles/s41586-026-11313-w).
- **Observación:** el trabajo presenta una ruta de calentamiento por plasma de carbono asistido por microondas, con temperaturas reportadas de hasta 2,400 °C, para transformar pasta de cemento hidratada de desecho en clínker que cumple especificaciones de cemento Portland ordinario. El artículo describe un reactor de lotes de hasta 100 kg.
- **Cálculo CAPCOT:** ninguno.
- **Inferencia:** la ruta puede acortar el tiempo de proceso y valorizar pasta hidratada residual; el resultado experimental no demuestra por sí solo adopción comercial ni balance neto de emisiones a escala industrial.
- **Recomendación:** prioridad alta, condicionada a explicar la diferencia entre reactor experimental y planta comercial. El sitio experimental exacto debe verificarse antes de fijar un mapa.
- **Estado de fuente:** `PENDING_CROSSREF`.

### 3. Complejidad vertical de copas forestales y enfriamiento local

- **Fuente primaria:** Nature Communications, 25-11-2026. DOI: [10.1038/s41467-026-79796-9](https://doi.org/10.1038/s41467-026-79796-9). [Artículo editorial](https://www.nature.com/articles/s41467-026-79796-9).
- **Observación:** el estudio relaciona la complejidad vertical de la estructura de las copas con el enfriamiento local. Reporta enfriamiento local en la gran mayoría de los bosques y estima una reducción potencial cercana a 0.25 °C en temperatura superficial terrestre de bosques gestionados si su complejidad se aproxima a la de bosques intactos de referencia.
- **Cálculo CAPCOT:** ninguno.
- **Inferencia:** conservar/restaurar estructura vertical puede ser una palanca de adaptación local. La cifra corresponde a temperatura superficial terrestre modelada, no a una reducción equivalente de temperatura media del aire.
- **Recomendación:** prioridad alta. El mapa debe distinguir bosques gestionados, referencias intactas y escala local.
- **Estado de fuente:** `PENDING_CROSSREF`.

### 4. Reutilización de materia orgánica de algas para gestionar floraciones

- **Fuente primaria:** Nature Communications, 25-11-2026. DOI: [10.1038/s41467-026-79713-0](https://doi.org/10.1038/s41467-026-79713-0). [Artículo editorial](https://www.nature.com/articles/s41467-026-79713-0).
- **Observación:** el trabajo estudia el uso de materia orgánica algal recuperada como coagulante. Reporta eficiencias de eliminación de células algales de 82–95%, reducción de turbidez de 86–95% y recuperación de 45–79% de materia orgánica algal en un proceso de aproximadamente dos minutos. El análisis reporta reducciones de huella de carbono frente al tratamiento convencional.
- **Cálculo CAPCOT:** ninguno; no se recalcularon los porcentajes.
- **Inferencia:** parte del material retirado puede reutilizarse como insumo del propio tratamiento. No debe presentarse como solución ya desplegada a escala de lago o cuenca.
- **Recomendación:** prioridad media-alta por su giro circular. Antes de storyboard deben confirmarse escala experimental, origen de muestras y lugar de ensayo para no inventar un mapa.
- **Estado de fuente:** `PENDING_CROSSREF`.

### 5. Beneficios climáticos de productos de madera según uso y escenario

- **Fuente primaria disponible:** preprint de Research Square, DOI [10.21203/rs.3.rs-8591788/v1](https://doi.org/10.21203/rs.3.rs-8591788/v1). **Registro de artículo final:** Environmental Science & Technology, DOI [10.1021/acs.est.6c10525](https://doi.org/10.1021/acs.est.6c10525).
- **Observación:** el análisis compara 81 variantes de productos de madera, seis categorías de uso y tres escenarios de descarbonización para 2020–2070. Los factores de desplazamiento varían ampliamente entre usos; el beneficio no es uniforme y el desplazamiento asociado a energía disminuye hacia 2070.
- **Cálculo CAPCOT:** ninguno. No se extrapolan los factores a una cifra universal de “madera carbono-negativa”.
- **Inferencia:** el beneficio depende del producto sustituido, su vida útil y la descarbonización del sistema energético/material.
- **Recomendación:** prioridad media. Requiere lectura de la versión final del artículo y verificación de los límites del análisis antes de convertirlo en guion.
- **Estado de fuente:** `PENDING_PRIMARY_ACCESS` para la versión final editorial y `PENDING_CROSSREF`.

## Vigilancia, no selección

Frontiers in Materials aceptó el 26-11-2026 un artículo sobre compensación de velocidad de impresión en pinzas bilaminares impresas en 4D, DOI [10.3389/fmats.2026.2016303](https://doi.org/10.3389/fmats.2026.2016303). La página editorial indica que la versión final formateada aparecerá después. Se conserva como vigilancia, no como candidato listo para storyboard.

## Decisión editorial del corte

1. No se creó storyboard nuevo para el 28-11-2026 23:30: el slot no muestra ocupación en los registros consultados, pero no hay DOI/Crossref verificado para ninguno de los candidatos.
2. El storyboard de rapaces del 30-11-2026 07:00 sigue en `proyectos/`; no está preparado ni promovido.
3. No se generaron medios, frames, voz, audio, video, renders ni placeholders.
4. Ningún candidato se marca como recibido por Grok, seleccionado, producido, aprobado o publicado.


## Revalidación de fuentes y tendencias — 27-11-2026 02:04 CDMX

**Alcance de esta reconsulta:** se intentó abrir directamente cada URL RSS definida en `scripts/tendencias.py`; no se ejecutó el script Python en un runtime del repositorio. Los resultados exactos fueron:

| Fuente | Error de acceso |
|---|---|
| ScienceDaily Science | `400 Unsupported content-type: application/xml` |
| ScienceDaily Health | `400 Unsupported content-type: application/xml` |
| ScienceDaily Space | `400 Unsupported content-type: application/xml` |
| Phys.org | `400 Unsupported content-type: text/xml` |
| NASA | `400 Unsupported content-type: application/rss+xml` |
| ESA Space Science | `404 Not Found` |
| Nature RSS | `400 Unsupported content-type: application/rss+xml` |
| EurekAlert | `URL ... is not accessible via this tool` |
| Agencia SINC | `URL ... is not accessible via this tool` |
| UNAM Global | `400 Unsupported content-type: application/rss+xml` |
| Google Trends RSS México | `URL ... is not accessible via this tool` |

El respaldo HTML oficial de [Google Trends México](https://trends.google.com/trending?geo=MX) mostró **253 tendencias**. Las primeras 25 siguieron dominadas por deportes, clima, actualidad, figuras públicas y entretenimiento; no se identificó una señal científica/natural admisible.

### Vigilancia adicional — PAV1 y el patógeno de la agalla de la corona

- **Fuente primaria:** Sabri et al., *Frontiers in Plant Science*, Original Research, publicado el 26-11-2026. DOI declarado por la página editorial: [10.3389/fpls.2026.2008228](https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2026.2008228/full).
- **Observación:** el artículo describe PAV1 como el primer bacteriófago identificado que infecta *Allorhizobium vitis*. Reporta inhibición del crecimiento bacteriano superior al 98% en 48 h in vitro. En plantas de tomate, a los 25 días, la incidencia fue 83.3% en controles sin tratar y 46.7%/50.0% tras aplicaciones preventivas por inyección del tallo/aspersión foliar.
- **Observación de procedencia:** el fago se aisló de una muestra de aguas residuales tomada en noviembre de 2025 en la entrada de la planta municipal de tratamiento de Bari, Italia (41.1081° N, 16.2606° E). Esa coordenada corresponde al punto de aislamiento, no al lugar de los ensayos en tomate.
- **Límite:** el ensayo de biocontrol descrito es en tomate; no demuestra eficacia de campo en viñedos ni control de agalla en plantas de vid. No convertir los porcentajes en una promesa de tratamiento comercial.
- **Cálculo CAPCOT:** ninguno.
- **Inferencia:** candidato con giro visual fuerte —un virus bacteriano aislado de aguas residuales que reduce una enfermedad vegetal en condiciones experimentales—, pero requiere explicar la diferencia entre actividad in vitro y ensayo preventivo en tomate.
- **Recomendación:** conservar como vigilancia, no añadirlo a los cinco candidatos principales ni crear storyboard todavía. No se identificó una ubicación publicada para los ensayos en tomate; el único pin verificable es el sitio de aislamiento en Bari.
- **Estado DOI:** `PENDING_CROSSREF`. La apertura directa de Crossref y `doi.org` devolvió `Internal Error ()` y “URL ... is not accessible via this tool”; la página editorial primaria sí está accesible. No marcar el DOI como verificado.

Los cinco candidatos principales del corte permanecen sin cambios y con Crossref pendiente. No se creó storyboard para el 28-11-2026 23:30 ni para otro slot.
