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
- **Estado de verificación:** página editorial primaria consultada y DOI visible; **PENDIENTE_RESOLVEDOR_CROSSREF**. El endpoint de Crossref y `doi.org` no resolvieron DNS en este run.

### 2. Complejidad del plancton y bomba biológica de carbono

- **Publicación:** 21-nov-2026, *Nature Communications*.
- **Fuente primaria:** [Plankton ecological complexity amplifies climate-driven weakening of the ocean biological pump](https://www.nature.com/articles/s41467-026-79817-7).
- **DOI:** `10.1038/s41467-026-79817-7`.
- **Observación/modelo:** un mismo marco de modelo de sistema terrestre comparó tres configuraciones de ecosistemas planctónicos. Bajo SSP5-8.5, la producción comunitaria neta global de fin de siglo cae 5.8%, 8.8% y 12.8% según aumenta la complejidad representada.
- **Cálculo:** la configuración más compleja proyecta una caída 7.0 puntos porcentuales mayor que la configuración por defecto (12.8 − 5.8).
- **Inferencia:** una representación demasiado simple de la red alimentaria puede subestimar el debilitamiento futuro de la exportación de carbono. Son proyecciones de modelo, no una medición de una caída observada hoy.
- **Recomendación:** conservar como candidato posterior; requiere explicar con claridad la diferencia entre producción primaria, producción comunitaria y exportación de carbono.
- **Estado de verificación:** texto completo de la página primaria PLOS consultado; DOI visible. **PENDIENTE_RESOLVEDOR_CROSSREF** por fallo DNS.

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
