# RADAR CAPCOT — 2026-11-03

**Corte:** 3-nov-2026, 08:01 America/Mexico_City  
**Repositorio:** `marcojpad-hash/capcot-capsulas-imaginantes`  
**Rama:** `feature/capcot-video-discovery-continuity`  
**Ventana de investigación:** 27-oct a 3-nov-2026, inclusive  
**Resultado de staging:** `NO_DUPLICAR` — se crea únicamente este brief. No se crea storyboard porque los slots autorizados del 3-nov ya están ocupados y el slot 23:30 está excluido.

## 1. Estado de ejecución y fuente de verdad

Se leyeron los contratos operativos, plan maestro, receta, guía externa, catálogo de estilos, líneas temáticas, flujo, continuidad audiovisual, informe técnico, scripts de tendencias y registro editorial, además de los registros de datos y storyboards recientes.

La reconciliación sigue el criterio de `scripts/registro_editorial.py`: los registros de rotación/publicaciones/cola se complementan con storyboards de `proyectos/`, `cola/` y `salidas/`. Un storyboard propuesto no se cuenta como publicación por el mero hecho de existir. No se modificó ningún archivo `data/*.json`.

### Guardia anti-duplicación del 3-nov

El horario vigente asigna los cinco slots así:

| Slot CDMX | project_id asignado | Estado leído en el horario | Tratamiento |
|---|---|---|---|
| 07:00 | `2026-11-03_kids-leche-enchilado` | `programado_yt_tt_fb` | Ya cubierto por Grok Bot; no producir otro paquete kids para el 3-nov |
| 13:30 | `2026-11-03_comida-maillard` | `programado_yt_tt_fb` | Ocupado |
| 17:00 | `2026-10-29_juno-choque-proa` | `programado_yt_tt_fb` | Ocupado |
| 19:00 | `2026-10-31_smartpe-edicion-plantas` | `programado_yt_tt_fb` | Ocupado |
| 23:30 | `2026-11-03_dato-TBD-news` | `pendiente_dato_dia` | Excluido por instrucción expresa |

Inventario de material del 3-nov encontrado:

- `proyectos/2026-11-03_kids-leche-enchilado/storyboard.json`: existe; estado `EN_PRODUCCION_GROK_BOT`; estilo `crayones_infantiles`; 7 escenas. No se reescribe.
- `salidas/2026-11-03_kids-leche-enchilado/storyboard.json`: existe como material de salida.
- `salidas/2026-11-03_comida-maillard/storyboard.json` y `cola/bloqueados/2026-11-03_comida-maillard/storyboard.json`: existen; se conservan sin cambios.
- `salidas/2026-11-03_2026-11-03-kids-tiburon-groenlandia/storyboard.json` y `cola/bloqueados/2026-11-03_kids-tiburon-groenlandia/storyboard.json`: propuestas preexistentes pendientes de revisión; no equivalen a publicación ni autorizan duplicar el slot kids.
- `cola/entrada/2026-11-03_enzimas-incrustadas-oceano/storyboard.json`: existe con `fecha=2026-11-03` y estado `REWRITE_PREPARADO_PENDIENTE_GUARDADO_EN_REPO_Y_AUDITOR`, pero no contiene `fecha_objetivo` ni `slot_local` y no aparece como asignación en el horario vigente. Se conserva intacto; el investigador no modifica la cola.
- En los storyboards legacy inspeccionados faltan campos explícitos `fecha_objetivo` y `slot_local`; para la asignación horaria prevalece el registro del horario semanal, no el prefijo del directorio.

El slot del 4-nov 19:00 sigue asignado a `2026-10-29_machu-picchu-fallas-pisa` con estado `pendiente_ok_mj`. No se produce Machu Picchu ni se sustituye por otro tema en ese slot. Los doce project_id canónicos del lote 5–7 nov permanecen en `proyectos/`; no se crean copias ni se reescriben.

**Conclusión de la guardia:** no hay slot libre y autorizado para un storyboard nuevo el 3-nov. Por la regla anti-duplicación, el único entregable aplicable que faltaba era el radar de esta fecha. Este brief registra la investigación; no es una decisión editorial ni una instrucción de publicación.

## 2. RSS científicos y Google Trends México

### RSS: fallos exactos de lectura

Se intentó abrir cada URL RSS definida en `scripts/tendencias.py`. El lector disponible rechazó los tipos de contenido XML/RSS o no pudo acceder a la URL. No se obtuvo el XML y **no se afirma que se haya parseado**.

| Fuente | URL | Respuesta exacta del lector |
|---|---|---|
| ScienceDaily | https://www.sciencedaily.com/rss/top/science.xml | `(400) Unsupported content-type: application/xml` |
| ScienceDaily Salud | https://www.sciencedaily.com/rss/top/health.xml | `(400) Unsupported content-type: application/xml` |
| ScienceDaily Espacio | https://www.sciencedaily.com/rss/space_time.xml | `(400) Unsupported content-type: application/xml` |
| Phys.org | https://phys.org/rss-feed/ | `(400) Unsupported content-type: text/xml` |
| NASA | https://www.nasa.gov/news-release/feed/ | `(400) Unsupported content-type: application/rss+xml` |
| ESA | https://www.esa.int/rssfeed/Our_Activities/Space_Science | `(400) Unsupported content-type: application/rss+xml` |
| Nature | https://www.nature.com/nature.rss | `(400) Unsupported content-type: application/rss+xml` |
| EurekAlert | https://www.eurekalert.org/rss/news.xml | `URL ... is not accessible via this tool.` |
| SINC | https://www.agenciasinc.es/rss | `URL ... is not accessible via this tool.` |
| UNAM Global | https://unamglobal.unam.mx/feed/ | `(400) Unsupported content-type: application/rss+xml` |
| Google Trends RSS MX | https://trends.google.com/trending/rss?geo=MX | `URL ... is not accessible via this tool.` |

Estos errores describen la limitación del lector usado en esta ejecución; no prueban que los servidores RSS estén caídos. Se utilizó el respaldo oficial de Google Trending Now para México.

### Trending Now — observación puntual

Fuente: https://trends.google.com/trending?geo=MX&hl=es  
Consulta: 3-nov-2026, aproximadamente 08:01 CDMX.

La página mostró 212 tendencias en el corte y una vista inicial de resultados. Entre las señales visibles:

- **«vórtice polar»**: tráfico aproximado de 2 mil+, aumento indicado de 800%, activo desde unas 7 horas antes. Es una señal atmosférica general; no es evidencia relacionada con el estudio de la ola de calor de India.
- **«aguacate»**: 2 mil+, aumento indicado de 600%, activo desde unas 19 horas antes. El tema ya está asignado al lote del 6-nov (`2026-11-06_comida-aguacate-negro`); no reutilizar.
- **«Ebola»**: 1 mil+, aumento indicado de 300%, activo desde unas 13 horas antes. Es un tema médico y no habilita una línea temática médica, que sigue figurando como futura en `docs/LINEAS_TEMATICAS.md`.
- **«mochila de emergencias»**: 10 mil+, aumento indicado de 1,000%, activo desde unas 9 horas antes. No ofrece por sí solo una oportunidad para la línea científica del canal.

**Límite:** los valores de Trending Now son aproximaciones dinámicas de búsquedas, no conteos absolutos, métricas de audiencia del canal ni una serie histórica comparable. Ninguna de las cinco investigaciones siguientes aparece como tendencia explícita en la vista observada. No se fuerza una relación entre los términos de Trends y los artículos.

## 3. Candidatos científicos — publicaciones del 27 al 31 de octubre

Los cinco candidatos tienen artículo original localizado y DOI contrastado con Crossref REST (`status=ok`, registro `source=Crossref`, DOI y fecha de publicación concordantes con la página editorial). Las afirmaciones descritas proceden del resumen del artículo original. La fecha corresponde a publicación en línea, no a la fecha de recepción del manuscrito.

### Candidato 1 — Microbios que cruzan el Atlántico con el polvo africano

- **Línea vigente:** Actualidad; Naturaleza / bichos; Dato científico.
- **Novedad observada:** el estudio caracteriza comunidades bacterianas, fúngicas y arqueanas en el Observatorio de Torre Alta del Amazonas, a 42 y 323 metros sobre el suelo, comparando condiciones de fondo con una intrusión de polvo del norte de África de cinco días. Durante la intrusión cambió fuertemente la comunidad bacteriana hacia microorganismos asociados a suelos secos, costras biológicas y ambientes marinos; la comunidad fúngica permaneció estable. La concentración de endotoxinas en el aire aumentó tres veces y no se enriquecieron patógenos obligados.
- **Fuente primaria:** Weber, J. et al., *Amazonian rainforest bioaerosol influenced by African dust intrusion*, Communications Earth & Environment, publicado el **27-oct-2026**. https://www.nature.com/articles/s43247-026-04119-1
- **DOI:** https://doi.org/10.1038/s43247-026-04119-1
- **Crossref:** https://api.crossref.org/works/10.1038/s43247-026-04119-1 — registro localizado.
- **Tendencia:** sin señal específica observada en Trending Now MX. No confundir con «vórtice polar».
- **Relevancia científica:** alta para transporte atmosférico de microorganismos y composición de aerosoles.
- **Oportunidad editorial:** alta. El giro es que el polvo transcontinental no transporta solo minerales: también desplaza comunidades microbianas.
- **Público/ocasión:** audiencia general interesada en naturaleza, atmósfera y conexiones entre continentes; funciona sin depender de una efeméride.
- **Riesgos y límite:** un episodio de intrusión de cinco días no representa todos los eventos de polvo. El aumento de endotoxinas no demuestra infección ni enfermedad; el artículo no encontró enriquecimiento de patógenos obligados. No titular «el polvo africano trae enfermedades».
- **Verificación:** **VERIFICADO** — artículo original y DOI Crossref localizados.

### Candidato 2 — El hollín agravó una ola de calor histórica en India

- **Línea vigente:** Actualidad; Dato científico; clima/geo-atmósfera dentro de la ampliación temática aprobada.
- **Novedad observada:** el artículo combina observaciones recientes y simulaciones de un modelo climático regional acoplado a química para estudiar la ola de calor de India de 2015. Estima que los aerosoles, especialmente el carbono negro, elevaron las máximas diarias entre **0.2 y 1.5 °C** en la región afectada; los cambios de humedad elevaron las máximas diarias de temperatura de bulbo húmedo entre **0.25 y 1.8 °C**. El estudio estima exposición adicional de unas **30 millones de personas** y **0.2 millones de km²** a estrés térmico seco y húmedo extremo.
- **Fuente primaria:** Tiwari, D. et al., *Black carbon aerosols intensified India’s 2015 mega heatwave and expanded heat stress exposure*, Communications Earth & Environment, publicado el **27-oct-2026**. https://www.nature.com/articles/s43247-026-04157-9
- **DOI:** https://doi.org/10.1038/s43247-026-04157-9
- **Crossref:** https://api.crossref.org/works/10.1038/s43247-026-04157-9 — registro localizado.
- **Tendencia:** «vórtice polar» es una señal atmosférica general, no una tendencia sobre carbono negro ni sobre la ola de calor de 2015.
- **Relevancia científica:** alta para interacciones entre contaminación, circulación atmosférica, temperatura y estrés térmico.
- **Oportunidad editorial:** media-alta. Permite explicar por qué contaminación y calor extremo pueden amplificarse en un mismo episodio.
- **Público/ocasión:** público general interesado en clima y ambiente; mejor como explicación de mecanismo que como noticia de actualidad local.
- **Riesgos y límite:** el caso analizado es India en 2015; los intervalos proceden de atribución/modelación regional. No afirmar que el carbono negro por sí solo causó la ola de calor ni trasladar los valores a México.
- **Verificación:** **VERIFICADO** — artículo original y DOI Crossref localizados.

### Candidato 3 — Leones marinos y lobos finos de Galápagos: dietas distintas, competencia no demostrada

- **Línea vigente:** Actualidad; Naturaleza / bichos; Dato científico.
- **Novedad observada:** el estudio utiliza metabarcoding de ADN para analizar la dieta de leones marinos de Galápagos y lobos finos en cinco contextos de coexistencia/no coexistencia y distintas biorregiones. Confirma diferencias dietarias, pero encuentra poca evidencia de que esas diferencias se deban a competencia entre especies. Los leones marinos que aparecen solos no pasan a consumir las presas típicas de los lobos finos; los autores consideran que la variación oceanográfica espacial explica mejor los patrones.
- **Muestra declarada:** leones marinos con N entre 22 y 50 según el contexto; lobos finos con N=12. No convertir estos tamaños en una estimación poblacional.
- **Fuente primaria:** Urquía, D. O. et al., *DNA metabarcoding reveals that Galapagos pinnipeds might not be competing as thought*, Scientific Reports, publicado el **31-oct-2026**. https://www.nature.com/articles/s41598-026-78512-3
- **DOI:** https://doi.org/10.1038/s41598-026-78512-3
- **Crossref:** https://api.crossref.org/works/10.1038/s41598-026-78512-3 — registro localizado.
- **Tendencia:** sin señal específica observada en Trending Now MX.
- **Relevancia científica:** alta para ecología trófica, coexistencia y lectura de dietas mediante ADN.
- **Oportunidad editorial:** alta para audiencia latinoamericana. La historia puede abrir con la aparente rivalidad y girar hacia el papel de las condiciones oceanográficas.
- **Público/ocasión:** público general de naturaleza y fauna marina; cercanía regional por tratarse de Galápagos.
- **Riesgos y límite:** «poca evidencia de competencia» no significa «se demostró que nunca compiten». El N de lobos finos es 12; hay que conservar el alcance de los cinco contextos estudiados y no universalizar el resultado.
- **Verificación:** **VERIFICADO** — artículo original y DOI Crossref localizados.

### Candidato 4 — Un canal iónico coordina señales químicas y movimiento en moscas

- **Línea vigente:** Actualidad; Naturaleza / bichos; Dato científico.
- **Novedad observada:** el artículo estudia el canal TRPγ de *Drosophila*. Mediante criomicroscopía electrónica compara estructuras nativas y unidas a alcanfor (resoluciones de 2.18 y 3.44 Å) e identifica dos módulos de detección de Ca²⁺ con efectos opuestos sobre la apertura del canal. En animales, esa regulación bidireccional participa en la cinemática locomotora, incluida la longitud de zancada y la velocidad; mutantes sin la regulación de Ca²⁺ muestran actividad locomotora alterada.
- **Fuente primaria:** Pang, P. et al., *Chemoreceptor TRPγ coordinates locomotor activity via regulating intracellular Ca²⁺ homeostasis in Drosophila*, Nature Communications, publicado el **31-oct-2026**. https://www.nature.com/articles/s41467-026-78915-w
- **DOI:** https://doi.org/10.1038/s41467-026-78915-w
- **Crossref:** https://api.crossref.org/works/10.1038/s41467-026-78915-w — registro localizado.
- **Tendencia:** sin señal específica observada en Trending Now MX.
- **Relevancia científica:** alta para estructura y función de canales iónicos y control motor.
- **Oportunidad editorial:** media. Tiene un mecanismo preciso, pero exige explicar sin jerga cómo una señal química y el calcio modulan el movimiento.
- **Público/ocasión:** audiencia general interesada en insectos y mecanismos biológicos.
- **Riesgos y límite:** no afirmar que TRPγ explica por sí solo todo el olfato o todo el movimiento de los insectos. El estudio es en *Drosophila*; el alcanfor se usó en la caracterización estructural y no debe presentarse como único estímulo natural.
- **Verificación:** **VERIFICADO** — artículo original y DOI Crossref localizados.

### Candidato 5 — Un mineral del manto podría debilitar el interior de supertierras

- **Línea vigente:** Actualidad; Dato científico; espacio/planetas dentro de la ampliación temática aprobada.
- **Novedad observada:** experimentos con celdas de yunque de diamante calentadas con láser, difracción de rayos X, análisis químico y cálculos de primeros principios muestran que la ferropericlasa puede separarse en dominios de óxidos ricos y pobres en hierro cerca de **200 GPa**. Los experimentos alcanzaron hasta **3300 K**. Los autores proponen que, en planetas rocosos de más de aproximadamente **1.5 masas terrestres**, esta separación podría favorecer una capa profunda enriquecida en FeO y de viscosidad muy baja.
- **Fuente primaria:** Lv, C. et al., *Ferropericlase breakdown drives mantle weakening in super-Earths*, Nature Communications, publicado el **31-oct-2026**. https://www.nature.com/articles/s41467-026-79163-8
- **DOI:** https://doi.org/10.1038/s41467-026-79163-8
- **Crossref:** https://api.crossref.org/works/10.1038/s41467-026-79163-8 — registro localizado.
- **Tendencia:** sin señal específica observada en Trending Now MX.
- **Relevancia científica:** alta para mineralogía a alta presión y modelos de interiores planetarios.
- **Oportunidad editorial:** media-alta si se centra en el giro «un planeta más grande que la Tierra no necesariamente tiene un interior igual, solo ampliado».
- **Público/ocasión:** audiencia general interesada en planetas y espacio.
- **Riesgos y límite:** no se observó directamente el interior de una supertierra. La capa de baja viscosidad es una implicación propuesta a partir de experimentos y modelos; no presentarla como una estructura ya medida en un exoplaneta.
- **Verificación:** **VERIFICADO** — artículo original y DOI Crossref localizados.

## 4. Comparación y recomendación de radar

| Candidato | Tendencia MX observada | Relevancia científica | Oportunidad editorial | Riesgo principal |
|---|---|---|---|---|
| Polvo africano y bioaerosol amazónico | Sin tendencia directa | Alta | Alta | Confundir endotoxinas con patógenos o enfermedad |
| Carbono negro y ola de calor india | Solo señal atmosférica general, no específica | Alta | Media-alta | Trasladar causalidad o cifras fuera del caso de 2015 |
| Dietas de pinnípedos de Galápagos | Sin tendencia directa | Alta | Alta | Convertir «poca evidencia» en «ausencia de competencia» |
| Canal TRPγ en moscas | Sin tendencia directa | Alta | Media | Sobregeneralizar el papel de un canal en el movimiento |
| Ferropericlasa en supertierras | Sin tendencia directa | Alta | Media-alta | Presentar una inferencia planetaria como observación directa |

**Recomendación de investigación principal:** candidato 3, pinnípedos de Galápagos. Combina proximidad latinoamericana, una pregunta narrativa clara y un giro sustentado: las diferencias de dieta no prueban competencia y el patrón observado se explica mejor por variación oceanográfica. El límite de muestra y el lenguaje «poca evidencia» deben permanecer visibles.

**Alternativa de mayor fuerza visual:** candidato 1, transporte de comunidades microbianas por polvo africano. Tiene una secuencia causal clara entre intrusión, altura de muestreo, cambio bacteriano y estabilidad fúngica; el cierre debe enfatizar que no se detectó enriquecimiento de patógenos obligados.

Esta recomendación no selecciona el tema final ni reserva un horario. Grok conserva la decisión editorial. No se asignó estilo, estructura ni prompt visual porque la guardia impide crear un storyboard para el 3-nov.

## 5. Seguimiento técnico: Meta y Google Trends

### Meta Graph API / Instagram Insights / Facebook Pages Insights

Se contrastaron las referencias oficiales enlazadas en el informe técnico vigente:

- Graph API changelog v26.0: https://developers.facebook.com/docs/graph-api/changelog/version26.0/
- Graph API changelog: https://developers.facebook.com/docs/graph-api/changelog/
- Instagram Platform changelog: https://developers.facebook.com/docs/instagram-platform/changelog/
- Page Insights: https://developers.facebook.com/docs/platform/insights/reference/page-insights/

**Resultado de acceso:** el changelog general de Graph API y el de Instagram Platform respondieron `429 Too Many Requests`; las rutas versionadas v26.0 y Page Insights no fueron accesibles por el lector utilizado. Por tanto, no se certifica en esta ejecución el texto oficial de cambios nuevos.

Hay resúmenes secundarios que indican que cambios de Graph API v26.0 se extendieron a versiones anteriores el 27-oct-2026, incluyendo retirada de comportamientos de protocolo heredados y cambios de Commerce/Marketing API. No se elevan a especificación de CAPCOT: la documentación oficial no pudo leerse en esta ejecución y los cambios de Commerce/Marketing no modifican por sí mismos las métricas orgánicas de Insights. Antes de implementar cualquier cambio se requiere contraste directo con Meta.

El informe técnico ya documenta la migración de métricas legacy de Page Insights a media views/viewers, la separación de los flujos de Instagram Login y Facebook Login, y las métricas de Stories `link_clicks` y la etiqueta `is_ai_generated`. No se encontró evidencia oficial accesible de una nueva métrica orgánica de Instagram Insights o Page Insights que justifique modificar esa especificación.

### Google Trends API alfa

La documentación oficial continúa describiendo una alfa de acceso limitado, con ventana móvil de cinco años, agregaciones diaria/semanal/mensual/anual, desglose geográfico y escala consistente entre solicitudes. La escala representa interés de búsqueda, no volumen absoluto. No se observó una apertura general ni un cambio de especificación que justifique actualizar el informe.

- Documentación: https://developers.google.com/search/apis/trends
- Anuncio oficial de la alfa, 24-jul-2025: https://developers.google.com/search/blog/2025/07/trends-api
- Trending Now México: https://trends.google.com/trending?geo=MX&hl=es

**Decisión técnica:** no se reescribe `docs/INVESTIGACION_API_META_Y_GOOGLE_TRENDS.md`. La falta de acceso al changelog de Meta queda registrada aquí como límite de consulta, no como evidencia de que no haya habido cambios.

## 6. Límites y estado de entrega

- **Observado:** cinco artículos originales publicados entre el 27 y el 31-oct-2026; registros DOI encontrados en Crossref; snapshot de Trending Now; asignaciones de slots en el horario vigente; propuestas existentes en proyectos, salidas, cola y bloqueados.
- **Cálculo:** ventana de siete días definida como 27-oct a 3-nov inclusive; no se calculan métricas propias ni tasas de audiencia.
- **Inferencia:** la mejor oportunidad narrativa regional es la investigación de pinnípedos; el polvo africano es la alternativa con mecanismo visual más claro.
- **Recomendación:** conservar ambos candidatos en radar y esperar un slot nuevo autorizado antes de redactar storyboard.
- **Pendiente:** lectura directa de los changelogs oficiales de Meta cuando el acceso deje de responder 429/no disponible; lectura de RSS XML mediante un lector que admita los tipos de contenido devueltos.

**Entregable creado en esta ejecución:** únicamente `docs/briefs/2026-11-03_RADAR_CAPCOT.md`.

**No creado:** storyboard, copia en `cola/entrada/`, archivo `*_fuentes.md`, frames, imágenes, audio, voz, video o render. No se escribió `narrative_qa`, no se marcó paquete preparado, no se alteró el horario ni se tomó decisión de publicación.
