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

## Revalidación de RSS y Google Trends — 2026-11-24 06:27 CDMX

Se reintentaron las diez URL de `FEEDS_CIENCIA` de `scripts/tendencias.py` y Google Trends RSS México desde el lector web. Errores exactos:

| Fuente | Resultado |
|---|---|
| ScienceDaily ciencia | `400 Unsupported content-type: application/xml` |
| ScienceDaily salud | `400 Unsupported content-type: application/xml` |
| ScienceDaily espacio | `400 Unsupported content-type: application/xml` |
| Phys.org | `400 Unsupported content-type: text/xml` |
| NASA | `400 Unsupported content-type: application/rss+xml` |
| ESA Space Science | `404 Not Found` |
| Nature | `400 Unsupported content-type: application/rss+xml` |
| EurekAlert | `URL ... is not accessible via this tool` |
| SINC | `URL ... is not accessible via this tool` |
| UNAM Global | `400 Unsupported content-type: application/rss+xml` |
| Google Trends RSS México | `URL ... is not accessible via this tool` |

**Respaldo HTML oficial:** Google Trends México abrió correctamente en la vista «Past 24 hours»: 174 tendencias totales. La primera página (25 términos) contiene principalmente deportes, entretenimiento, trámites y consultas generales; «frío» es una señal meteorológica, no un candidato de la línea editorial. No se encontró un término elegible de ciencia, naturaleza, cocina, cuerpo o espacio. No se fuerza selección.

Los cuatro candidatos ya documentados en este radar permanecen en sus estados previos: Varroa y plankton con texto primario consultado pero DOI/resolvedor pendiente; glaciares y grafito en `PENDING_SOURCE`. No se crea storyboard: el cupo 24–29 sigue agotado y ningún candidato supera todavía la compuerta independiente de DOI.


## Actualización de ejecución — 2026-11-24 07:55 CDMX

### 1. Slot, ocupación y decisión

**Resultado: `NO_SLOT_POR_CUPO_DIARIO`; no crear storyboard principal ni storyboard `dato_del_dia` 23:30 para esta fecha.**

- La rama `feature/capcot-video-discovery-continuity` ya contiene este radar. No se creó un segundo brief.
- No existe `data/horario_2026-11-24.json` en la rama. El contrato operativo §3 conserva cinco slots diarios y `scripts/rotacion.py` fija `MAX_POR_DIA = 5`; `23:30` sigue siendo uno de los slots autorizados, no una exclusión global.
- La comprobación de solo lectura de `main/data/miniaturas_auditoria_2026-11-21.json` registra cinco IDs con `publishAt` para el 24-nov:
  - 07:00 — `RBUcAeptGAU`
  - 13:30 — `WtuxaKrS4-Q`
  - 17:00 — `cGb7Z0ZEz8w` y `_YzBY4OfUeo` (misma hora; colisión)
  - 19:00 — `9W9nn72rmfE`
- La cuenta es 5/5 IDs programados. La colisión de 17:00 permanece intacta. No se cancela, mueve ni reprograma nada. Aunque 23:30 no aparece como ID en ese snapshot, el cupo diario ya está agotado.
- La política horaria de main actualizada el 23-nov mantiene mañana y tarde, con 23:30 fijo; 19:00 figura retirado y 13:30 en prueba. Los registros preexistentes siguen contando para el límite; no se reinterpretan como ventanas nuevas.
- No se encontró proyecto, storyboard ni paquete de cola de fecha 24-nov en el árbol de main. Los dos marcadores de `main/handoffs/grok_inbox/` del 24-nov son solicitudes de series y muestran `status=pending`; no son recibos ni ocupan por sí mismos un slot editorial.
- En feature no existe proyecto, salida ni entrada de cola para 24-nov. No hay estado Grok que crear. El slot 23:30 se deja `NO_SLOT_POR_CUPO_DIARIO`; además, la fuente de fecha actual propuesta abajo conserva `PENDING_SOURCE` por resolución DOI no completada.

### 2. Ingesta RSS y Google Trends

Se intentó abrir cada uno de los diez feeds científicos declarados en `scripts/tendencias.py`, además de Google Trends RSS México. **No se descargó ni parseó XML.** Errores exactos observados:

| Feed | Error |
|---|---|
| ScienceDaily ciencia | `400 Unsupported content-type: application/xml` |
| ScienceDaily salud | `400 Unsupported content-type: application/xml` |
| ScienceDaily espacio | `400 Unsupported content-type: application/xml` |
| Phys.org | `400 Unsupported content-type: text/xml` |
| NASA | `400 Unsupported content-type: application/rss+xml` |
| ESA Space Science | `404 Not Found` |
| Nature RSS | `500 Redirected to https://idp.nature.com/authorize?response_type=cookie&client_id=grover&redirect_uri=https://www.nature.com/nature.rss`; destino no accesible |
| EurekAlert | `URL https://www.eurekalert.org/rss/news.xml is not accessible via this tool` |
| SINC | `URL https://www.agenciasinc.es/rss is not accessible via this tool` |
| UNAM Global | `400 Unsupported content-type: application/rss+xml` |
| Google Trends RSS México | `URL https://trends.google.com/trending/rss?geo=MX is not accessible via this tool` |

**Respaldo oficial:** Google Trends Trending Now, México, últimas 24 horas, muestra 179 tendencias; la primera página contiene 25. La señal `frío` registra 2K+ búsquedas, +500%, iniciada hace 11 h, relacionada con masa de aire/aviso de frente frío. El resto visible se concentra en deporte, entretenimiento, trámites y actualidad general. No aparece un término elegible de ciencia, naturaleza, cocina, cuerpo o espacio. `frío` es una señal meteorológica, no evidencia de un paper ni una oportunidad científica suficiente por sí sola.

### 3. Candidatos recientes (ventana 18–24 nov)

Todos están dentro de los últimos siete días. Las URLs son páginas editoriales primarias identificadas en la búsqueda. El resolvedor `doi.org` devolvió `URL ... is not accessible via this tool` para los cinco DOI; los intentos a Crossref REST tampoco dieron respuesta verificable. Por tanto, **ningún DOI de esta lista se declara validado**. Los resultados de Nature se obtuvieron en extractos de sus páginas editoriales; las aperturas directas de varias páginas devolvieron redirección 500 a `idp.nature.com`.

#### A. Evidencia de magnetismo p-wave en EuSi

- **Línea:** Actualidad / dato científico / materiales y tecnología.
- **Publicación:** Nature, 18-nov-2026.
- **Fuente primaria:** https://www.nature.com/articles/s41586-026-11295-9
- **DOI declarado por la página:** `10.1038/s41586-026-11295-9` — `PENDING_RESOLVEDOR`.
- **Observado:** difracción de neutrones identifica una fase espiral quiral entre 33.4 y 62 K; ARPES y spin-ARPES aportan evidencia de una textura de espín p-wave; las separaciones de energía superan 100 meV y se observan dominios magnéticos de aproximadamente 10 μm.
- **Cálculo:** no se añade cifra derivada.
- **Inferencia permitida:** EuSi es una plataforma experimental para investigar magnetismo p-wave y posibles respuestas electrónicas; no demuestra un dispositivo ni una aplicación comercial.
- **Tendencia:** sin señal directa en las primeras 25 tendencias de México.
- **Oportunidad:** alto contraste narrativo entre un metal químicamente simple y una estructura magnética no convencional.
- **Público/ocasión:** público adulto de ciencia, materiales y tecnología.
- **Riesgos:** explicar que p-wave describe simetría/textura de espín; no confundirlo con superconductividad ya demostrada ni prometer tecnología disponible.
- **Verificación:** página/abstract primario identificado; DOI sin resolver.

#### B. Interacciones virus-huésped en sedimentos de montes submarinos

- **Línea:** Actualidad / naturaleza / ecología marina.
- **Publicación:** Communications Biology, 23-nov-2026.
- **Fuente primaria:** https://www.nature.com/articles/s42003-026-11405-3
- **DOI declarado:** `10.1038/s42003-026-11405-3` — `PENDING_RESOLVEDOR`.
- **Observado:** análisis metagenómico y metatranscriptómico de sedimentos del mar de China Meridional recupera 85 genomas ensamblados, 1,592 unidades virales y 610 vínculos virus-huésped predichos. El artículo informa que 527 unidades (33%) codifican genes asociados con respuesta al estrés y reparación de ADN; una parte se clasifica como genes metabólicos auxiliares putativos.
- **Cálculo:** 527 / 1,592 = 33.1%, consistente con el 33% redondeado del artículo.
- **Inferencia permitida:** los resultados sugieren posibles contribuciones virales a procesos de adaptación microbiana; los vínculos son predichos y la señal transcripcional no prueba por sí sola que los virus aumenten la supervivencia del huésped.
- **Tendencia:** sin señal directa en Trends MX visible.
- **Oportunidad:** buen conflicto narrativo — virus no solo como agentes de infección, sino como posibles moduladores de comunidades microbianas extremas.
- **Público/ocasión:** naturaleza, océano y microbiología para público general adulto.
- **Riesgos:** no personificar virus, no afirmar simbiosis beneficiosa probada; faltan coordenadas de muestreo verificadas para una futura capa de mapa.
- **Verificación:** abstract de la fuente primaria identificado; DOI sin resolver; mapa pendiente.

#### C. Comparación global de eficiencias para retirar CO₂ mediante perturbaciones geoquímicas oceánicas

- **Línea:** Actualidad / clima-geología / dato científico.
- **Publicación:** Nature Communications, 24-nov-2026.
- **Fuente primaria:** https://www.nature.com/articles/s41467-026-78856-4
- **DOI declarado:** `10.1038/s41467-026-78856-4` — `PENDING_RESOLVEDOR`.
- **Observado:** el estudio construye un marco con un modelo biogeoquímico oceánico global para comparar aumento de alcalinidad (OAE), extracción de carbono inorgánico disuelto (DOR) y adición combinada (ADA). Las simulaciones de 15 años muestran variación espacial y estacional; la eficiencia DOR es mayor en verano que en invierno en el modelo, con respuesta inicial más rápida en regiones ecuatoriales y subpolares y menor en zonas de formación de aguas profundas.
- **Cálculo:** no se deriva una cifra adicional del extracto consultado.
- **Inferencia permitida:** el resultado cuestiona tratar la retirada de CO₂ oceánica como una eficiencia uniforme: ubicación, estación y química de fondo importan.
- **Tendencia:** sin señal directa en las primeras 25 tendencias de México.
- **Oportunidad:** **recomendación principal para un próximo slot libre**, por mecanismo explicable y cartografía global/estacional compatible con mapa y gráfico.
- **Público/ocasión:** público general adulto interesado en clima, océanos y soluciones climáticas.
- **Riesgos:** es modelación, no ensayo de campo; no convertir eficiencia simulada en toneladas retiradas en el mundo real ni presentar una técnica como solución ya escalada.
- **Verificación:** extracto de página editorial primaria con resultados; DOI sin resolver. No se redacta storyboard por el cupo agotado y por la compuerta DOI pendiente.

#### D. Mapa de pausas de la replicación de ADN a escala de molécula individual

- **Línea:** Actualidad / dato científico / cuerpo y biología molecular.
- **Publicación:** Nature Communications, 24-nov-2026.
- **Fuente primaria:** https://www.nature.com/articles/s41467-026-79296-w
- **DOI declarado:** `10.1038/s41467-026-79296-w` — `PENDING_RESOLVEDOR`.
- **Observado:** en levadura de gemación, el equipo analizó 330,000 trayectorias de replisomas e identificó alrededor de 17,000 pausas; la duración media estimada fue 4.4 ± 1.6 minutos. La técnica usa incorporación de BrdU y secuenciación de lectura larga para inferir ubicación, dirección y duración aproximada de las pausas.
- **Cálculo:** 17,000 / 330,000 ≈ 5.15% de las trayectorias analizadas; el artículo lo resume como aproximadamente una pausa por cada 20 trayectorias. No extrapolar ese porcentaje a células humanas.
- **Inferencia permitida:** los conflictos entre transcripción y replicación contribuyen a pausas; los conflictos de frente a frente son más problemáticos que los codireccionales en el sistema estudiado.
- **Tendencia:** sin señal directa en Trends MX visible.
- **Oportunidad:** visualización microscópica clara de una maquinaria que se detiene y reanuda; buen candidato para público adulto interesado en genética.
- **Público/ocasión:** ciencia/cuerpo, público general adulto.
- **Riesgos:** organismo de estudio = levadura; la duración es aproximada y depende de supuestos sobre velocidad de horquilla; no afirmar que cada pausa produce mutación o enfermedad.
- **Verificación:** texto de la fuente primaria recuperado en extracto editorial amplio; DOI sin resolver.

#### E. Huella de biodiversidad de la alimentación y crecimiento económico

- **Línea:** Actualidad / naturaleza / alimentación y ambiente.
- **Publicación:** Nature Food, 23-nov-2026.
- **Fuente primaria:** https://www.nature.com/articles/s43016-026-01465-3
- **DOI declarado:** `10.1038/s43016-026-01465-3` — `PENDING_RESOLVEDOR`.
- **Observado:** el estudio cuantifica huellas de biodiversidad basadas en uso de suelo para consumo alimentario en 158 países entre 1995 y 2020. El desacoplamiento con el crecimiento económico es más probable a ingresos per cápita altos; es más fuerte para alimentos vegetales que animales y más débil para carne de rumiantes. Parte de la mejora doméstica de países de altos ingresos queda compensada por impactos desplazados mediante comercio internacional.
- **Cálculo:** no se añade cifra derivada.
- **Inferencia permitida:** reducir impactos locales no garantiza reducir la huella total si la producción se desplaza a otros países.
- **Tendencia:** sin señal directa en Trends MX visible.
- **Oportunidad:** conectar una decisión cotidiana de alimentación con la geografía invisible de su producción.
- **Público/ocasión:** público general, alimentación y naturaleza.
- **Riesgos:** el indicador se basa en uso de suelo; no cubre por sí solo todos los impulsores de pérdida de biodiversidad. No decir que los países ricos resolvieron el problema.
- **Verificación:** abstract de la fuente primaria identificado; DOI sin resolver.

**Candidato excluido por fecha:** la nota ScienceDaily del 24-nov sobre impermeabilizantes de un naufragio romano remite a un artículo original de *Frontiers in Materials* fechado 24-abr-2026, fuera de la ventana de siete días. No se cuenta como publicación nueva del 24-nov.

### 4. Recomendación y límites de staging

- **Recomendación editorial, no selección final:** reservar el estudio de eficiencia oceánica de CO₂ para el siguiente slot que realmente se libere. Ofrece un mecanismo único, un contraste estacional/latitudinal y una capa de mapa basada en resultados globales; antes de storyboard deben resolverse DOI/URL y leerse la fuente primaria completa.
- El candidato de ADN ofrece una segunda ruta fuerte, pero la cartografía debe resolverse con coordenadas genómicas verificables; no sustituirlas por un mapa geográfico ficticio.
- **23:30:** no crear proyecto separado para 24-nov. Motivo operativo: cupo diario 5/5. Motivo de fuente adicional: DOI de la fuente publicada hoy sigue `PENDING_RESOLVEDOR`. No se crea `narrative_qa`, no se promueve y no se deja nada en cola.
- No se crea storyboard principal para el 24-nov: no existe slot/cupo libre. Se conserva el radar único existente y no se modifica ningún proyecto ajeno.

### 5. Seguimiento técnico — sin cambio documental

Revisión de documentación oficial al corte 07:55 CDMX:

- **Graph API:** el changelog canónico oficial declara v27.0 como la versión más reciente, introducida el 4-nov-2026; ya está registrada en §9.9–9.10 de este informe técnico.
- **Facebook Page Insights:** la referencia oficial v27.0 mantiene el aviso genérico de deprecación para el 15-jun-2026, junto con límites de 100 likes, actualización aproximada cada 24 h, retención de dos años, ventana de consulta de 90 días, umbral demográfico de 100 personas y exclusión de interacciones de Reels. La discrepancia de la lista detallada ya está documentada en §9.11; no apareció una lista reconciliada nueva.
- **Instagram Insights:** la guía confirma las rutas Unified Login, Instagram Login y Facebook Login, además de 90 días de retención y respuestas vacías cuando un dato no existe. El changelog de Instagram no muestra una entrada posterior al 30-jul-2026; las notas de AI label y `link_clicks` ya están documentadas.
- **Google Trends API alfa:** continúa limitada por solicitud, con ventana de cinco años, agregaciones diaria/semanal/mensual/anual, regiones/subregiones y escala consistente. No se observó cambio de contrato.
- **Decisión:** no reescribir `docs/INVESTIGACION_API_META_Y_GOOGLE_TRENDS.md`; no apareció cambio nuevo relevante sustentado para el MVP.

### 6. QA narrativo preexistente — relectura de 32 storyboards canónicos

Se releen los 32 JSON existentes en `proyectos/`. Los 32 contienen `narrative_qa`; **12 PASS y 20 FAIL**. En todos, `review_basis` aparece literalmente como `lectura_en_frio_solo_narracion`. La columna `checks` codifica los siete booleanos en este orden exacto:

1. `pregunta_central_reconstruible` (P)
2. `apertura_in_medias_res` (IM)
3. `progresion_por_escena` (PR)
4. `transiciones_causales` (TC)
5. `giro_cientifico_explicado` (GC)
6. `limite_evidencia_explicito` (LE)
7. `payoff_cierre_apertura` (PA)

`1=true`; `0=false`. `reviewed_at=NO_PRESENTE_EN_JSON` significa que el campo no aparece en el JSON leído, no que se haya inferido una fecha.

| project_id | status/score | reviewed_at | checks P-IM-PR-TC-GC-LE-PA | critical_flags |
|---|---:|---|---|---|
| 2026-11-05_comida-palomitas | FAIL/82 | 2026-11-18T15:00:00-06:00 | 1001111 | [`APERTURA_DEFINICIONAL_NO_IN_MEDIAS_RES`, `ESCENA_6_REITERA_CAUSAS_DE_GRANOS_NO_REVENTADOS_SIN_INFORMACION_NUEVA`] |
| 2026-11-05_inter-arboles-se-comunican | FAIL/78 | 2026-11-18T15:00:00-06:00 | 1011111 | [`APERTURA_GENERICA_NO_IN_MEDIAS_RES`] |
| 2026-11-05_inter-rayo-globular | FAIL/81 | 2026-11-18T15:00:00-06:00 | 1011111 | [`APERTURA_HISTORICA_DESCRIPTIVA_NO_IN_MEDIAS_RES`] |
| 2026-11-05_kids-dia-en-venus | PASS/88 | 2026-11-18T15:00:00-06:00 | 1111111 | [] |
| 2026-11-06_comida-aguacate-negro | FAIL/79 | 2026-11-18T15:00:00-06:00 | 1100111 | [`REPETICION_ESCENAS_5_6_SIN_AVANCE_CAUSAL`] |
| 2026-11-06_inter-arena-cantante | PASS/94 | 2026-11-18T15:00:00-06:00 | 1111111 | [] |
| 2026-11-06_inter-ranas-congeladas | FAIL/83 | 2026-11-18T15:00:00-06:00 | 1100111 | [`REPETICION_ESCENAS_5_6_LIMITES_DE_ESPECIE_Y_CONDICIONES`] |
| 2026-11-06_kids-ballena-azul-corazon | FAIL/80 | 2026-11-18T15:00:00-06:00 | 1111110 | [`PAYOFF_SOBREAFIRMA_CASI_SE_DETIENE`] |
| 2026-11-07_comida-hielo-caliente | FAIL/81 | 2026-11-18T15:00:00-06:00 | 1011111 | [`APERTURA_DE_CREENCIAS_NO_IN_MEDIAS_RES`] |
| 2026-11-07_inter-nubes-pesan | FAIL/78 | 2026-11-18T15:00:00-06:00 | 1100110 | [`ESCENA_7_REITERA_CIFRA_Y_LIMITE_SIN_PAYOFF_DE_SUSPENSION`] |
| 2026-11-07_inter-pulpo-suenos | FAIL/72 | 2026-11-18T15:00:00-06:00 | 1100000 | [`FUENTE_PRIMARIA_CORRESPONDE_A_OCTOPUS_LAQUEUS_NO_INSULARIS`, `REPETICION_ESCENAS_5_6_Y_PAYOFF_VAGO`] |
| 2026-11-07_kids-huesos-bebe | FAIL/82 | 2026-11-18T15:00:00-06:00 | 1100111 | [`ESCENA_6_REPITE_VARIACION_DE_CONTEO_Y_FUSION`] |
| 2026-11-14_dato-microplasticos-pantanal | PASS/88 | 2026-11-14T15:04:13-06:00 | 1111111 | [] |
| 2026-11-15_dato-dia-diapausa-lestes-sponsa | PASS/90 | 2026-11-15T15:51:23-06:00 | 1111111 | [] |
| 2026-11-15_dato-quasar-pareja-cosmic-dawn | FAIL/0 | 2026-11-23T04:02:29-06:00 | 0000000 | [`REVISION_INDEPENDIENTE_AUSENTE`] |
| 2026-11-16_dato-polen-desenreda-nanotubos | PASS/91 | 2026-11-16T15:45:46-06:00 | 1111111 | [] |
| 2026-11-17_dato-suelo-dos-relojes | PASS/89 | 2026-11-17T15:35:22-06:00 | 1111111 | [] |
| 2026-11-18_dato-catorce-campos-hidrotermales | FAIL/68 | 2026-11-19T15:04:50-06:00 | 0100010 | [`PREGUNTA_CENTRAL_NO_RECONSTRUIBLE`, `SECUENCIA_DE_HALLAZGOS_SIN_PROGRESION_CAUSAL`, `GIRO_CIENTIFICO_NOMBRADO_PERO_NO_EXPLICADO`, `CIERRE_RESUMEN_SIN_PAYOFF`] |
| 2026-11-18_dato-kuroshio-puente-atmosferico | PASS/90 | 2026-11-18T15:00:00-06:00 | 1111111 | [] |
| 2026-11-19_dato-dia-luz-dos-manos-oro-poroso | PASS/91 | 2026-11-19T15:04:50-06:00 | 1111111 | [] |
| 2026-11-19_dato-estrella-dentro-de-estrella | PASS/90 | 2026-11-19T15:04:50-06:00 | 1111111 | [] |
| 2026-11-20_dato-dia-atlantico-humedad-sapropeles | PASS/91 | NO_PRESENTE_EN_JSON | 1111111 | [] |
| 2026-11-20_dato-marea-cerebral-en-sueno | FAIL/82 | 2026-11-23T06:23:43-06:00 | 1111111 | [`STAKES_NO_EXPLICADOS`] |
| 2026-11-21_fentale-metano-sin-erupcion | PASS/90 | 2026-11-20T16:11:24-06:00 | 1111111 | [] |
| 2026-11-21_homo-erectus-selva-tropical | FAIL/83 | 2026-11-20T22:06:10-06:00 | 1111011 | [`GIRO_CIENTIFICO_NOMBRADO_PERO_NO_EXPLICADO`] |
| 2026-11-21_pulsar-gamma-reticulo | FAIL/83 | 2026-11-20T15:41:24-06:00 | 1111011 | [`GIRO_CIENTIFICO_NOMBRADO_PERO_NO_EXPLICADO`] |
| 2026-11-22_bao-estrella-fusion-andromeda | FAIL/84 | 2026-11-21T13:56:37-06:00 | 1111111 | [`STAKES_NO_EXPLICADOS`] |
| 2026-11-22_genes-estatura-etapas | FAIL/72 | 2026-11-22T15:54:03-06:00 | 1000011 | [`APERTURA_DEFINICIONAL_NO_IN_MEDIAS_RES`, `MAPA_DE_INSTITUCIONES_ROMPE_CONTINUIDAD_NARRATIVA`, `GIRO_CIENTIFICO_NOMBRADO_SIN_MECANISMO_EXPLICADO`] |
| 2026-11-22_voyager-1-un-dia-luz | FAIL/83 | NO_PRESENTE_EN_JSON | 1111111 | [`FECHA_DE_HITO_Y_CONFIRMACION_CONFUNDIDAS`] |
| 2026-11-22_yubarta-genoma-soplo | PASS/90 | NO_PRESENTE_EN_JSON | 1111111 | [] |
| 2026-11-23_supersequias-722-eventos | FAIL/82 | 2026-11-23T00:57:16-06:00 | 1111111 | [`STAKES_NO_EXPLICADOS`] |
| 2026-11-23_tropical-biodiversity-turnover | FAIL/82 | 2026-11-21T14:24:25-06:00 | 1111111 | [`STAKES_NO_EXPLICADOS`] |

**Nota de integridad histórica:** `2026-11-05_inter-arboles-se-comunican` sigue bloqueado por desajuste de tema: su storyboard trata respiración nocturna, mientras el horario canónico pide red micorrícica/wood-wide web y Karst et al. 2023. No se presenta como equivalente ni se modifica. La variante extra de nubes no se recrea.

### 7. Confirmación de recepción Grok

Se consultaron los 32 paths `cola/estado/<project_id>.json` de estos proyectos; los 32 devolvieron HTTP 404 `Not Found`. Estado para cada uno: `RECEPCION_GROK_NO_CONFIRMADA`. No se creó ni editó ningún archivo de estado. Los marcadores de `handoffs/grok_inbox/` no sustituyen ese recibo.


## Corte complementario de investigación — 2026-11-24 10:00 CDMX

### Ingesta y señal de tendencias
- Se releó `scripts/tendencias.py` y su lista de 10 feeds científicos: ScienceDaily (ciencia, salud y espacio), Phys.org, NASA, ESA, Nature, EurekAlert, SINC y UNAM Global; también Google Trends RSS México.
- No se ejecutó el script Python en este entorno. Los intentos de lectura RSS mediante el lector web devolvieron: ScienceDaily (tres feeds) HTTP 400 `Unsupported content-type: application/xml`; Phys.org HTTP 400 `Unsupported content-type: text/xml`; NASA y Nature HTTP 400 `Unsupported content-type: application/rss+xml`; ESA HTTP 404 `Not Found`; EurekAlert, SINC y Google Trends RSS: URL no accesible por el lector. UNAM Global devolvió HTTP 400 `Unsupported content-type: application/rss+xml`. Estos errores describen el lector web, no una ejecución fallida del script.
- Respaldo oficial: la página HTML de Google Trends México sí abrió. Muestra 167 tendencias de las últimas 24 h; la primera página (25 términos) está dominada por deportes, entretenimiento, noticias y comercio. No se encontró en esa primera página un tema admisible de ciencia/naturaleza/cocina/cuerpo/espacio. No se seleccionó tema a partir de Trends.

### Tres candidatos científicos adicionales — fuentes primarias
Los tres artículos siguientes aparecen como manuscritos aceptados de *Monthly Notices of the Royal Astronomical Society*, publicados en línea el 23-nov-2026. Sus DOI resuelven a la página editorial de Oxford Academic. No son storyboards ni selecciones; se conservan como candidatos para un slot futuro.

1. **Dos ráfagas rápidas de radio muy dispersas.** Joscha N. Jahns-Schindler y colaboradores, DOI [10.1093/mnras/stag2241](https://doi.org/10.1093/mnras/stag2241), [artículo primario](https://academic.oup.com/mnras/advance-article/doi/10.1093/mnras/stag2241/9116689). El artículo informa dos FRB con tiempos de dispersión de 34 ± 6 ms y 300 ± 48 ms a 1 GHz. Para FRB 240312D, la pantalla dispersora se acota a unos 10 pc de la fuente; una nebulosa de viento de púlsar es la explicación más probable, pero los autores indican que el modelo no resulta completamente satisfactorio y requiere una orientación afinada. **Límite:** son dos eventos; no presentar el origen como resuelto.

2. **Contaminación metálica que se hunde y se extiende en enanas blancas magnéticas.** Elad Shiftan y Sivan Ginzburg, DOI [10.1093/mnras/stag2245](https://doi.org/10.1093/mnras/stag2245), [artículo primario](https://academic.oup.com/mnras/advance-article/doi/10.1093/mnras/stag2245/9116670). El modelo obtiene (t_{\downarrow}/t_{\leftrightarrow}\propto T^{8/3}) para comparar hundimiento gravitacional y dispersión horizontal de metales; incorpora campos magnéticos en la estructura estelar. **Límite:** el propio artículo dice que el mecanismo calculado no basta para explicar las enanas blancas frías que muestran parches; la variación de acreción en escalas de una década es una posible solución, no una conclusión demostrada.

3. **El corte ionosférico como posible tecnofirma de radio.** Michael A. Garrett, DOI [10.1093/mnras/stag2244](https://doi.org/10.1093/mnras/stag2244), [artículo primario](https://academic.oup.com/mnras/advance-article/doi/10.1093/mnras/stag2244/9116669). El modelo estima cortes de 5–40 MHz para la mayoría de planetas terrestres en zona habitable, potencialmente cerca de 100 MHz en entornos extremos; la frecuencia de semiescape podría variar alrededor de 40–50 % durante la órbita. **Límite:** es un diagnóstico teórico propuesto, no una detección de tecnología extraterrestre; un corte de baja frecuencia aislado no sería único.

### Orden de investigación
- Potencial narrativo más claro: FRB 240312D, por la distancia estimada de la pantalla dispersora y la hipótesis de un entorno cercano a la fuente; mantener explícita la incertidumbre del modelo.
- Mejor visualización de mecanismo: metales que se hunden frente a los que se dispersan sobre una enana blanca; explicar que el modelo todavía no resuelve los casos fríos observados.
- Gancho más llamativo, con mayor riesgo de sobreinterpretación: tecnofirma ionosférica; el guion tendría que empezar por la física del plasma y dejar claro que no se detectó ninguna señal extraterrestre.
- Ninguno se selecciona: el calendario 24–29 nov no tiene cupo libre y presenta sobrecapacidad/conflictos ya documentados. No se creó storyboard ni se marcó producción.

### Verificación DOI
- DOI resolver: confirmado para `stag2241`, `stag2244` y `stag2245` mediante las rutas DOI que redirigen a Oxford Academic.
- Crossref REST no fue accesible desde el lector web durante este corte; la verificación se apoya en el resolvedor DOI y la ficha editorial primaria.
- Las páginas de Oxford identifican los tres como *accepted manuscript*; pueden existir cambios menores en la versión final tipográfica.


## Actualización de señal de tendencia — 2026-11-24 10:28 CDMX

### Candidato adicional: prueba formal de la hipótesis de Riemann

**Señal de demanda:** la vista HTML oficial de Google Trends México muestra hipótesis de Riemann con más de 1,000 búsquedas y actividad aproximada de seis horas. Es una señal de interés, no evidencia científica.

**Observación primaria:**
- El comunicado conjunto de Lean y Mathlib, fechado 21-nov-2026, afirma que la comunidad certifica tanto el enunciado como la prueba formal de la hipótesis de Riemann. Describe una biblioteca Lean de unos 17 millones de líneas, dependiente directamente de Mathlib, y verificaciones con el kernel oficial de Lean y varios comprobadores independientes.
- La página del Clay Mathematics Institute todavía muestra el problema como Active.
- Las reglas oficiales del premio exigen publicación en un medio calificante, al menos dos años desde esa publicación y aceptación general en la comunidad matemática antes de que el instituto considere una solución para el premio.

**Lectura editorial:** el ángulo no debe ser «la IA resolvió y ya ganó el millón». La distinción útil es entre la certificación formal comunicada por Lean/Mathlib y el procedimiento separado del premio Clay. No afirmar que el premio fue otorgado ni que Clay ya cambió el estado del problema. Tampoco presentar la falta de una explicación humana completa como refutación de la comprobación formal.

**Fuentes primarias / URLs comprobadas:**
- Lean community, comunicado conjunto Lean FRO + Mathlib Initiative (21-nov-2026): https://leanprover-community.github.io/blog/posts/riemann-hypothesis/
- Clay Mathematics Institute, ficha oficial de Riemann: https://www.claymath.org/millennium/riemann-hypothesis/
- Clay Mathematics Institute, reglas oficiales: https://www.claymath.org/millennium-problems/rules/
- Google Trends México, señal de búsqueda: https://trends.google.com/trending?geo=MX

**Estado editorial:** CANDIDATO_RECOMENDADO_PARA_EVALUAR_EN_FUTURO_SLOT; no seleccionado y sin storyboard. El calendario 24–29 nov continúa sin cupo autorizado.

### RSS y límites de lectura de este corte

Se reintentó la lectura directa de los feeds de scripts/tendencias.py. La herramienta lectora no procesa los tipos XML: ScienceDaily (tres feeds), Phys.org, NASA, Nature y UNAM devolvieron errores de tipo de contenido o redirección; ESA devolvió 404; EurekAlert y SINC no fueron accesibles. Google Trends RSS México tampoco fue accesible. Se usó la vista HTML oficial de Trends como respaldo de señal, nunca como fuente científica. Los tres DOI MNRAS 10.1093/mnras/stag2241, stag2244 y stag2245 permanecen registrados como resueltos por DOI resolver en el corte anterior; Crossref REST no fue accesible en esta lectura.
