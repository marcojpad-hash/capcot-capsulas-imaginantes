# Radar CAPCOT — 24 de noviembre de 2026

**Corte de investigación:** 2026-11-23 01:56, America/Mexico_City  
**Rama:** `feature/capcot-video-discovery-continuity`  
**Fecha objetivo revisada:** 2026-11-24  
**Slot fijo revisado:** 23:30 CDMX

## Resultado de disponibilidad

**NO_SLOT_POR_CUPO_DIARIO. No crear storyboard para el 24-nov.**

El snapshot de programación en `main/data/miniaturas_auditoria_2026-11-21.json` contiene cinco videos para el 24-nov:

| Hora CDMX | Video | Estado |
|---|---|---|
| 07:00 | `RBUcAeptGAU` — El púrpura NO venía de piedras preciosas | Programado |
| 13:30 | `WtuxaKrS4-Q` — El robo que hizo famosa a la Mona Lisa | Programado |
| 17:00 | `cGb7Z0ZEz8w` — El vomitorium NO era para vomitar | Programado |
| 17:00 | `_YzBY4OfUeo` — ¿Lavas el pollo crudo? Mejor no | Programado; comparte publishAt con el anterior |
| 19:00 | `9W9nn72rmfE` — ¿La reina Victoria inventó el vestido de novia? | Programado |

La parrilla fija tiene cinco ventanas y `scripts/rotacion.py` impone `MAX_POR_DIA = 5`. Aunque 23:30 no aparece ocupado por un video en ese snapshot, el día ya suma cinco publicaciones programadas. La colisión existente de 17:00 no se corrige ni cancela desde esta operación.

La función `registro_editorial.registros()` reconcilia rotación, publicaciones, cola, proyectos, bloqueados y salidas, pero no consume `miniaturas_auditoria_*.json`; por eso el conteo de publicaciones programadas externas exige esta comprobación manual. No se modificó `data/*.json`.

## Candidatos recientes

### 1. Varroa y la hipoxia de altura — candidato recomendado para el próximo slot realmente libre

- **Publicación:** 19-nov-2026, *PLOS Biology*.
- **Fuente primaria:** [Altitude-induced hypoxia suppresses Varroa mite reproduction in Tibetan honey bees](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3004091).
- **DOI:** `10.1371/journal.pbio.3004091`.
- **Observación:** el estudio siguió 60 colonias en cuatro altitudes de China. En Lhasa (3,637 m), la infestación de cría descendió de 9.3% al inicio a 3.3% a los dos meses, 1.6% a los cuatro meses y 0% al año. En un ensayo de hipoxia a baja altitud, la descendencia media fue 1.7 frente a 3.9 en los controles; después de dos años, 13 de 15 colonias de Lhasa seguían vivas sin acaricidas.
- **Cálculo:** el cambio de 9.3% a 0% equivale a −9.3 puntos porcentuales en la infestación de cría observada en ese sitio; no se extrapola a todas las colmenas ni a otras regiones.
- **Inferencia:** la hipoxia es el factor causal principal apoyado por el ensayo de control; el mecanismo fisiológico exacto que detiene el desarrollo del ácaro permanece sin resolver.
- **Recomendación:** mejor candidato narrativo por contraste entre parásito y abeja, experimento de control y límite de evidencia claro. No asignado a 24-nov por cupo agotado. Para un mapa futuro, usar únicamente centros urbanos de referencia (Lhasa y Yunjinghong/Xishuangbanna), nunca presentarlos como coordenadas exactas de apiarios.
- **Estado de verificación:** texto completo de la página primaria PLOS consultado; DOI visible. **PENDIENTE_RESOLVEDOR_CROSSREF** por fallo DNS.

### 2. Complejidad del plancton y bomba biológica de carbono

- **Publicación:** 21-nov-2026, *Nature Communications*.
- **Fuente primaria:** [Plankton ecological complexity amplifies climate-driven weakening of the ocean biological pump](https://www.nature.com/articles/s41467-026-79817-7).
- **DOI:** `10.1038/s41467-026-79817-7`.
- **Observación/modelo:** un mismo marco de modelo de sistema terrestre comparó tres configuraciones de ecosistemas planctónicos. Bajo SSP5-8.5, la producción comunitaria neta global de fin de siglo cae 5.8%, 8.8% y 12.8% según aumenta la complejidad representada.
- **Cálculo:** la configuración más compleja proyecta una caída 7.0 puntos porcentuales mayor que la configuración por defecto (12.8 − 5.8).
- **Inferencia:** una representación demasiado simple de la red alimentaria puede subestimar el debilitamiento futuro de la exportación de carbono. Son proyecciones de modelo, no una medición de una caída observada hoy.
- **Recomendación:** conservar como candidato posterior; requiere explicar con claridad la diferencia entre producción primaria, producción comunitaria y exportación de carbono.
- **Estado de verificación:** resultado editorial indexado de Nature localizado; la apertura directa de la página completa no quedó disponible en esta sesión. Claims limitados al abstract indexado. **PENDING_SOURCE** para cualquier storyboard hasta lectura directa; resolver Crossref también pendiente por DNS.

### 3. Lagos glaciares, clima y geometría de los glaciares

- **Publicación:** 20-nov-2026, *Nature Climate Change*.
- **Fuente primaria:** [Climate and glacier geometry dominate global glacier–lake interactions](https://www.nature.com/articles/s41558-026-02808-5).
- **DOI:** `10.1038/s41558-026-02808-5`.
- **Observación:** el inventario global 2000–2020 identifica 3,567 lagos de contacto con hielo adicionales (+35%), un aumento de área de 604 ± 22 km² (+9%) y de volumen de 66 ± 5 km³ (+12%).
- **Cálculo:** el estudio atribuye 11 ± 7% de la pérdida de masa de los glaciares terminados en lagos a los lagos; clima explica 43 ± 10% y geometría glaciar 46 ± 10%.
- **Inferencia:** el crecimiento de lagos importa, pero no es el impulsor dominante de la pérdida de masa en la comparación global del estudio.
- **Recomendación:** candidato visual fuerte por mapas y barras regionales; conservar la distinción entre número, área, volumen y pérdida de masa.
- **Estado de verificación:** resultado editorial indexado de Nature localizado; la apertura directa de la página completa no quedó disponible en esta sesión. Claims limitados al abstract indexado. **PENDING_SOURCE** para cualquier storyboard hasta lectura directa; resolver Crossref también pendiente por DNS.

### 4. Grafito de carga rápida mediante síntesis flash asistida por metales

- **Publicación:** 20-nov-2026, *Advanced Materials*.
- **Metadatos localizados:** [PubMed](https://pubmed.ncbi.nlm.nih.gov/43059198/); DOI `10.1002/adma.75785`.
- **Estado:** **PENDING_SOURCE**. Se localizó el registro bibliográfico, pero la página primaria de Wiley no fue accesible en este run. No se incorporan claims de rendimiento, tiempos ni capacidad de carga al guion hasta leer la fuente primaria.

## Ingesta RSS y respaldo

Se consultaron las diez URL definidas en `scripts/tendencias.py` y Google Trends RSS México. Todas fallaron en la resolución DNS del entorno; no se interpretó HTTP 000 como ausencia de noticias.

| Fuente | URL | Error exacto |
|---|---|---|
| ScienceDaily ciencia | `https://www.sciencedaily.com/rss/top/science.xml` | `curl: (6) Could not resolve host: www.sciencedaily.com` |
| ScienceDaily salud | `https://www.sciencedaily.com/rss/top/health.xml` | `curl: (6) Could not resolve host: www.sciencedaily.com` |
| ScienceDaily espacio | `https://www.sciencedaily.com/rss/space_time.xml` | `curl: (6) Could not resolve host: www.sciencedaily.com` |
| Phys.org | `https://phys.org/rss-feed/` | `curl: (6) Could not resolve host: phys.org` |
| NASA | `https://www.nasa.gov/news-release/feed/` | `curl: (6) Could not resolve host: www.nasa.gov` |
| ESA | `https://www.esa.int/rssfeed/Our_Activities/Space_Science` | `curl: (6) Could not resolve host: www.esa.int` |
| Nature RSS | `https://www.nature.com/nature.rss` | `curl: (6) Could not resolve host: www.nature.com` |
| EurekAlert | `https://www.eurekalert.org/rss/news.xml` | `curl: (6) Could not resolve host: www.eurekalert.org` |
| SINC | `https://www.agenciasinc.es/rss` | `curl: (6) Could not resolve host: www.agenciasinc.es` |
| UNAM Global | `https://unamglobal.unam.mx/feed/` | `curl: (6) Could not resolve host: unamglobal.unam.mx` |
| Google Trends México | `https://trends.google.com/trending/rss?geo=MX` | `curl: (6) Could not resolve host: trends.google.com` |

**Respaldo utilizado:** texto completo de la fuente primaria PLOS Biology. Para Nature Communications y Nature Climate Change solo se consultaron resultados editoriales indexados; no se afirma lectura del texto completo y ambos candidatos quedan en **PENDING_SOURCE** para storyboard. PubMed se usó solo para identificar el registro bibliográfico del candidato de grafito, no como sustituto de la fuente primaria.

## Compuertas y decisión

- **DOI/Crossref:** no verificados por DNS; no declarar resuelto ningún DOI en este radar.
- **Slot:** 24-nov 23:30 no autorizado por cupo diario 5/5; la colisión 17:00 permanece intacta.
- **Storyboard:** no creado. No hay `proyectos/<id>/storyboard.json` para el 24-nov.
- **Narrative QA:** no aplica; no se redactó storyboard ni se creó `narrative_qa`.
- **Grok:** no se creó entrada, no se disparó workflow, no se envió payload y no se consultaron valores de secretos.
- **Medios:** no se generaron imágenes, audio, voz, video, frames, renders ni placeholders; no se consumieron créditos.

**Siguiente paso mínimo:** cuando se libere un slot dentro del cupo diario, volver a comprobar el inventario y el resolvedor DOI. Varroa queda como candidato recomendado, no seleccionado ni preparado.

## Revalidación de fuentes y señales — 2026-11-23 18:00 CDMX

### Actualización de fuente primaria
- El PDF de Nature Communications para «Plankton ecological complexity amplifies climate-driven weakening of the ocean biological pump» ya está accesible y fue leído: https://www.nature.com/articles/s41467-026-79817-7_reference.pdf. El texto completo confirma que, bajo SSP5-8.5, la producción comunitaria neta (NCP) cae 5.8%, 8.8% y 12.8% en las tres configuraciones; no son caídas de NPP. El mecanismo descrito es el cambio hacia fitoplancton más pequeño y mayor pastoreo de zooplancton, que retiene más carbono en la capa superior. Publicado en línea el 21-nov-2026.
- El candidato pasa de `PENDING_SOURCE` por falta de texto a `TEXTO_PRIMARIO_COMPLETO_VERIFICADO`; permanece `PENDIENTE_RESOLVEDOR_CROSSREF`. No se autoriza storyboard mientras DOI/resolvedor siga pendiente.
- El artículo PLOS Biology de Varroa mantiene texto primario completo accesible y DOI declarado en la página: https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3004091. El click al DOI falló con `500 Redirected to https://journals.plos.org/plosone/doi?id=10.1371/journal.pbio.3004091`, destino no accesible desde este lector. No se marca `VERIFICADO_CROSSREF`.

### Resolvedor y tendencias
- Los intentos directos a `api.crossref.org/works/{doi}` y `doi.org/{doi}` no entregaron respuesta verificable; errores observados: `URL not accessible via this tool` / `Internal Error`. Los DOI visibles en las páginas/PDF no sustituyen el resolvedor.
- El lector web no pudo consumir los RSS: `400 Unsupported content-type: application/rss+xml` en los feeds XML consultados y `URL not accessible via this tool` para Google Trends RSS. Esto no es una ejecución de `scripts/tendencias.py`; se conserva como limitación del lector. El último run del investigador ya había registrado los errores de DNS del runtime.
- Respaldo HTML Google Trends México: 179 tendencias en la vista consultada; no se identificó tema dentro del alcance editorial. No se añade candidato por la señal matemática «hipótesis de Riemann».

### Cupo y decisión
- La evidencia de ocupación del 24-nov no cambió: cinco IDs para `MAX_POR_DIA=5`, con colisión a las 17:00. La política activa de `main/data/horarios.json` desde el 23-nov es 06:30–07:30 y 16:30–18:00, más el slot fijo 23:30; 13:00–14:30 sigue siendo prueba. El cupo diario ya está agotado.
- No se creó storyboard ni entrada de cola. El candidato de plankton queda investigado, no seleccionado ni preparado. `data/*.json` y `main` permanecen solo lectura.

## Revalidación de ingesta, resolvedor y cupo — 2026-11-24 04:00 CDMX

### RSS científicos y Google Trends

Se intentaron las diez URL definidas en `scripts/tendencias.py` y Google Trends RSS México. El lector no pudo ingerir los XML; errores exactos:

| Fuente | Error observado |
|---|---|
| ScienceDaily ciencia | `400 Unsupported content-type: application/xml` |
| ScienceDaily salud | `400 Unsupported content-type: application/xml` |
| ScienceDaily espacio | `400 Unsupported content-type: application/xml` |
| Phys.org | `400 Unsupported content-type: text/xml` |
| NASA | `400 Unsupported content-type: application/rss+xml` |
| ESA Space Science | `404 Not Found` |
| Nature RSS | `400 Unsupported content-type: application/rss+xml` |
| EurekAlert | `URL https://www.eurekalert.org/rss/news.xml is not accessible via this tool` |
| SINC | `URL https://www.agenciasinc.es/rss is not accessible via this tool` |
| UNAM Global | `400 Unsupported content-type: application/rss+xml` |
| Google Trends RSS México | `URL https://trends.google.com/trending/rss?geo=MX is not accessible via this tool` |

**Respaldo oficial:** se abrió la vista HTML de Google Trends México (`https://trends.google.com/trending?geo=MX`): 163 tendencias en la vista; las primeras 25 no aportaron un tema admisible para ciencia, naturaleza, cocina, cuerpo o espacio. No se forzó selección desde tendencias ajenas a la línea editorial.

### Revalidación de candidatos

- **Varroa / PLOS Biology:** se volvió a abrir la página primaria y se leyó el texto. El DOI `10.1371/journal.pbio.3004091` aparece en el artículo, pero Crossref REST devolvió `URL ... is not accessible via this tool`; `doi.org` devolvió `500 Redirected to https://journals.plos.org/plosone/doi?id=10.1371/journal.pbio.3004091`, destino no accesible. Se conserva `PENDIENTE_RESOLVEDOR`; la página primaria no sustituye Crossref/resolvedor.
- **Plankton ecological complexity / Nature Communications:** el PDF editorial primario localizado en la revalidación del 23-nov sigue siendo la fuente de texto completo. DOI `10.1038/s41467-026-79817-7` continúa `PENDIENTE_RESOLVEDOR`; no se declara DOI resuelto.
- **Glacial lakes / Nature Climate Change:** la página primaria no quedó accesible en esta revalidación; conserva `PENDING_SOURCE`.
- **Grafito / Advanced Materials:** solo se conserva el registro bibliográfico de PubMed; sin lectura de la página primaria de Wiley, conserva `PENDING_SOURCE`.

### Cupo y decisión

- Ocupación de `main` consultada en solo lectura: 24-nov **5/5**; 25–28-nov **7/5** por día; 29-nov **5/5**. Las nueve reprogramaciones de `data/rehechos_2026-11-22.json` son procesamiento preexistente, no nuevos slots libres.
- No se creó storyboard ni entrada de cola. No se creó `narrative_qa`, no se disparó workflow, no se generaron medios ni placeholders y no se consumieron créditos.
- `data/*.json` y `main` permanecen solo lectura. Varroa y plankton siguen como candidatos investigados, no seleccionados ni preparados.