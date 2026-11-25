# Radar CAPCOT — 25 de noviembre de 2026

**Corte de investigación:** 2026-11-23 04:02 CDMX  
**Rama:** `feature/capcot-video-discovery-continuity`  
**Fecha objetivo examinada:** 2026-11-25  
**Resultado editorial:** cinco candidatos documentados; ninguno asignado a storyboard.  
**Estado de cupo:** `NO_SLOT_AUTORIZADO` — siete programaciones registradas para el día frente a `MAX_POR_DIA=5`.

## 1. Fuentes de tendencias y respaldo

No se ejecutó `scripts/tendencias.py`: esta sesión no dispone de un runner local con salida de red. Se intentó abrir directamente cada URL declarada en `FEEDS_CIENCIA`; los errores de lectura fueron:

| Feed | Resultado de apertura |
|---|---|
| ScienceDaily ciencia — https://www.sciencedaily.com/rss/top/science.xml | `400 Unsupported content-type: application/xml` |
| ScienceDaily salud — https://www.sciencedaily.com/rss/top/health.xml | `400 Unsupported content-type: application/xml` |
| ScienceDaily espacio — https://www.sciencedaily.com/rss/space_time.xml | `400 Unsupported content-type: application/xml` |
| Phys.org — https://phys.org/rss-feed/ | `400 Unsupported content-type: text/xml` |
| NASA — https://www.nasa.gov/news-release/feed/ | `400 Unsupported content-type: application/rss+xml` |
| ESA Space Science — https://www.esa.int/rssfeed/Our_Activities/Space_Science | `404 Not Found` |
| Nature — https://www.nature.com/nature.rss | `500 Redirected to idp.nature.com/authorize` |
| EurekAlert — https://www.eurekalert.org/rss/news.xml | `URL is not accessible via this tool` |
| SINC — https://www.agenciasinc.es/rss | `URL is not accessible via this tool` |
| UNAM Global — https://unamglobal.unam.mx/feed/ | `400 Unsupported content-type: application/rss+xml` |
| Google Trends RSS México — https://trends.google.com/trending/rss?geo=MX | `URL is not accessible via this tool` |

**Respaldo oficial:** la página HTML de Google Trends México abrió con 277 tendencias totales y 25 visibles en la vista consultada. No apareció un tema de ciencia, naturaleza, cocina, cuerpo o espacio que aportara un candidato editorial utilizable. No se trató la lista de tendencias como fuente científica.

El radar anterior del 24-nov conserva el resultado de su intento de red: `curl: (6) Could not resolve host` para los feeds y Trends. Ese error corresponde a aquel run; no se atribuye a una ejecución del script en este corte.

## 2. Candidatos recientes

Los candidatos están ordenados por potencial narrativo, no por una afirmación de selección. Las observaciones se separan de las inferencias y de los límites de evidencia.

### Candidato 1 — El oxígeno frena al ácaro Varroa

- **Estudio primario:** Wei et al., *PLOS Biology*, “Altitude-induced hypoxia suppresses Varroa mite reproduction in Tibetan honey bees”, publicado el 19-nov-2026.
- **URL:** https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3004091
- **DOI declarado por la página:** 10.1371/journal.pbio.3004091.
- **Observación:** 60 colonias se dividieron en cuatro grupos de 15 y se trasladaron a cuatro altitudes. En Lhasa (3,637 m), la infestación del brood bajó de 9.3% a 0% al año; después de dos años, 13 de las 15 colonias seguían vivas sin miticida ni manejo de apoyo aparte del monitoreo programado.
- **Experimento mecanístico:** a 88 m de altitud, cinco colmenas modificadas se mantuvieron en hipoxia de aproximadamente 13.5 kPa durante 11 días. Los ácaros produjeron en promedio 1.7 descendientes frente a 3.9 en controles.
- **Inferencia admisible:** la reducción de oxígeno afecta directamente la reproducción de *Varroa destructor*; no demuestra que trasladar colmenas sea una solución universal ni que la altitud por sí sola explique toda supervivencia.
- **Recomendación editorial:** candidato más fuerte para una cápsula; el contraste abeja/ácaro y el experimento de hipoxia permiten explicar un mecanismo concreto.
- **Compuerta:** texto primario completo consultado; DOI visible, pero Crossref/resolvedor no confirmado en este corte. `PENDIENTE_RESOLVEDOR`.

### Candidato 2 — La “Norma arm” podría ser un frente de choque

- **Estudio primario:** Davis et al., *Nature Astronomy*, “The nature of the Norma arm as a bar-driven star-forming shock front”, publicado el 20-nov-2026.
- **URL:** https://www.nature.com/articles/s41550-026-03010-5
- **DOI declarado por la página:** 10.1038/s41550-026-03010-5.
- **Observación:** las posiciones de máseres asociadas a la región Norma se comparan con un modelo hidrodinámico de la barra galáctica.
- **Interpretación de los autores:** proponen que la estructura podría ser un frente de choque generado por la barra de la Vía Láctea, y no necesariamente un brazo espiral independiente. El modelo estima una semilongitud de barra de 4.3 ± 0.2 kpc y una orientación de aproximadamente 20°.
- **Límite:** es una interpretación apoyada en la correspondencia entre observaciones y simulación; no es una reclasificación definitiva aceptada por toda la comunidad.
- **Recomendación editorial:** buen candidato visual, siempre que la narración mantenga “los autores proponen” y no convierta el modelo en hecho cerrado.
- **Compuerta:** texto primario consultado y DOI visible; resolvedor no confirmado. `PENDIENTE_RESOLVEDOR`.

### Candidato 3 — La complejidad del plancton cambia la bomba biológica

- **Estudio primario:** Lin et al., *Nature Communications*, “Plankton ecological complexity amplifies climate-driven weakening of the ocean biological pump”, publicado el 21-nov-2026.
- **URL:** https://www.nature.com/articles/s41467-026-79817-7
- **DOI declarado:** 10.1038/s41467-026-79817-7.
- **Observación del resumen editorial:** un mismo marco de modelo terrestre compara tres ecosistemas de plancton con complejidad creciente. Bajo SSP5-8.5, la producción comunitaria neta de finales de siglo cae 5.8%, 8.8% y 12.8% en las tres configuraciones.
- **Inferencia:** los modelos con redes alimentarias más simples podrían subestimar el debilitamiento proyectado de la exportación de carbono.
- **Límite:** son proyecciones de modelos, no mediciones de una caída futura ya observada.
- **Compuerta:** abstracto primario indexado; texto completo no verificado. `PENDING_SOURCE`; DOI/resolvedor pendiente.

### Candidato 4 — Los lagos glaciares crecen, pero no son el factor dominante

- **Estudio primario:** Zhao et al., *Nature Climate Change*, “Climate and glacier geometry dominate global glacier–lake interactions”, publicado el 20-nov-2026.
- **URL:** https://www.nature.com/articles/s41558-026-02808-5
- **DOI declarado:** 10.1038/s41558-026-02808-5.
- **Observación del resumen editorial:** entre 2000 y 2020, los lagos en contacto con hielo aumentaron en 3,567 (+35%); su área creció 604 ± 22 km² (+9%) y su volumen 66 ± 5 km³ (+12%).
- **Límite clave:** para la pérdida de masa de glaciares que terminan en lagos, el estudio atribuye mayor capacidad explicativa a geometría (46 ± 10%) y clima (43 ± 10%) que a los lagos (11 ± 7%). No decir que los lagos son la causa principal.
- **Recomendación editorial:** visualmente fuerte, pero exige explicar con cuidado la diferencia entre crecimiento de lagos y atribución de pérdida de hielo.
- **Compuerta:** abstracto primario visible; texto completo no verificado. `PENDING_SOURCE`; DOI/resolvedor pendiente.

### Candidato 5 — Una bacteria asociada a quinoa responde a la salinidad

- **Estudio primario:** Murata et al., *Scientific Reports*, “A quinoa-associated Pantoea isolate displays salinity-responsive auxin production and promotes plant growth under salt stress”, publicado el 22-nov-2026.
- **URL:** https://www.nature.com/articles/s41598-026-80573-3
- **DOI declarado:** 10.1038/s41598-026-80573-3.
- **Observación del resumen editorial:** la cepa 6PN, aislada de plántulas de quinoa, promovió elongación de raíz primaria y masa seca de *Arabidopsis thaliana* bajo estrés salino; no se observó efecto significativo en condiciones no salinas.
- **Inferencia:** la respuesta de la bacteria a la salinidad podría ayudar a entender interacciones planta-microbio bajo estrés.
- **Límite:** el ensayo no demuestra aumento de rendimiento en cultivos de quinoa en campo ni valida un producto agrícola.
- **Recomendación editorial:** candidato reciente y visual, pero necesita leer el artículo completo y mantener la distinción entre *Arabidopsis* experimental y quinoa.
- **Compuerta:** abstracto primario visible; texto completo no verificado. `PENDING_SOURCE`; DOI/resolvedor pendiente.

## 3. Verificación DOI y resolvedor

Se intentó abrir Crossref REST y los resolvedores DOI desde esta sesión. Crossref REST devolvió `URL is not accessible via this tool`; el DOI de PLOS redirigió a una ruta de PLOS One que no permitió verificar el destino correcto, y los resolvedores DOI de Nature no devolvieron una respuesta verificable. Por tanto, ningún candidato se marca `VERIFICADO_CROSSREF` en este corte. Las páginas editoriales y sus DOI declarados son evidencia primaria, pero no sustituyen la compuerta de resolvedor exigida antes de storyboard/promoción.

## 4. Cupo, rotación y slots

`scripts/rotacion.py` fija `MAX_POR_DIA=5`. Se contrastaron los registros de `main` en solo lectura:

- **25-nov:** siete programaciones registradas (7/5): cinco videos del snapshot principal —07:00 `cPNiOFeY5_k` y `W9g2tPZTpD4` (colisión, mismo `publishAt`), 13:30 `G1ByWhjfxls`, 17:00 `L6ggmPAwBOA` y 19:00 `A3JK0gYuqG8`— más dos reworks con `publishAt` local 10:00 `9RxTSifAcpo` y 15:00 `3rwo_sK1e18`.
- **26–28 nov:** cinco videos del snapshot principal más dos reworks por día (7/5 cada día). El quinto video aparece en las colisiones del mismo `publishAt`: 26-nov 17:00 `-1DRh_qj7Bg`, 27-nov 07:00 `nd0rs6iVy8E` y 28-nov 17:00 `fcSNbU809ao`.
- **29-nov:** cuatro programaciones del snapshot más un rework (5/5).

Las programaciones provienen de `main/data/miniaturas_auditoria_2026-11-21.json` y `main/data/rehechos_2026-11-22.json`. Son evidencia de programación registrada; no se canceló, reprogramó ni duplicó nada. No hay slot autorizado para un nuevo storyboard el 25-nov.

## 5. Decisión de este radar

- **Recomendación de investigación:** conservar Varroa como candidato principal y Norma arm como alternativa.
- **Selección:** ninguna.
- **Storyboard:** no creado; el día objetivo no tiene cupo disponible y los DOI no superaron la verificación del resolvedor.
- **Cola / Grok:** sin entradas nuevas; no se creó ni modificó `cola/estado`.
- **Medios:** no se generaron imágenes, frames, voz, audio, video, renders ni placeholders.
- **Estado de producción:** `approved_assets=[]`, `export.render_status=NOT_GENERATED`; no se creó ningún campo de ruta o nombre de asset.


## 6. Huellas de evidencia del corte

- HEAD de main consultado: `c371aec46595b092d0b4d2f74ac38670e8897754` — cierre del día 22-nov, 23-nov 05:22 UTC.
- `main/data/miniaturas_auditoria_2026-11-21.json`: SHA `afc0a587025534eb5a338169383171bb0f38254c`.
- `main/data/rehechos_2026-11-22.json`: SHA `902a92411a516df4a3bf1046d8fec3ce1ee888c9`.
- `main/data/publicaciones.json`: SHA `9acb10035cb0d375635ec7481527d60af648ea8f`.
- `feature/scripts/rotacion.py`: SHA `f3e529e49cf825bdecc62a1d4669e5c59c6c28c3` (`MAX_POR_DIA=5`).


## Reintento de resolver — 23-nov-2026, 04:29 CDMX

Se intentó abrir Crossref REST `/works/{doi}` y `/v1/works/{doi}` para los DOI de los candidatos. El lector web devolvió `Internal Error` en ambos endpoints y no entregó una respuesta de Crossref; no se marcó ningún DOI como verificado. Se conserva `PENDIENTE_RESOLVEDOR` y no se crea storyboard sin resolver la fuente.

## Revalidación de textos primarios — 2026-11-23 18:00 CDMX

### Estado actualizado de los cinco candidatos
- **Varroa / PLOS Biology:** texto primario completo consultado. El estudio reporta experimentos de traslado de colonias y de hipoxia; el resumen de la página especifica reducción de fecundidad del ácaro por encima de 3,500 m. DOI declarado, pero el resolvedor redirigió a una ruta no accesible; `PENDIENTE_RESOLVEDOR`.
- **Brazo Norma / Nature Astronomy:** PDF primario completo consultado: https://www.nature.com/articles/s41550-026-03010-5.pdf. El trabajo usa simulaciones N-body e hidrodinámicas para proponer que los máseres trazan el frente de choque/barra y su carril de polvo; no es una observación directa que cierre el debate. DOI visible, resolvedor pendiente.
- **Plankton / Nature Communications:** PDF primario completo consultado: https://www.nature.com/articles/s41467-026-79817-7_reference.pdf. Bajo SSP5-8.5, NCP cae 5.8%, 8.8% y 12.8% en las tres configuraciones; NPP cambia poco. El efecto se relaciona con fitoplancton más pequeño y mayor pastoreo de zooplancton. DOI visible, resolvedor pendiente.
- **Glaciares y lagos / Nature Climate Change:** la página primaria deja leer el abstract y los datos globales, pero el texto completo permanece bajo suscripción. Conserva `PENDING_SOURCE`; no convertir el abstract en texto completo verificado.
- **Pantoea 6PN asociada a quinoa / Scientific Reports:** PDF primario completo consultado: https://www.nature.com/articles/s41598-026-80573-3_reference.pdf. El aislado 6PN se obtuvo de quinoa, pero los ensayos de promoción de crecimiento se realizaron en *Arabidopsis thaliana* bajo 300 mM NaCl; no demuestra aumento de rendimiento de quinoa en campo. El efecto no fue significativo sin sal. DOI visible, resolvedor pendiente.

### DOI, RSS y Google Trends
- Los intentos de Crossref REST y DOI resolver no entregaron una respuesta verificable: `URL not accessible via this tool` / `Internal Error`; el click del DOI PLOS terminó en `500 Redirected to https://journals.plos.org/plosone/doi?id=10.1371/journal.pbio.3004091`, no accesible. Ningún candidato se marca `VERIFICADO_CROSSREF`.
- Los RSS XML consultados devolvieron `400 Unsupported content-type: application/rss+xml`; Google Trends RSS devolvió `URL not accessible via this tool`. `scripts/tendencias.py` no se ejecutó en este run. El respaldo HTML México mostró 179 tendencias y ninguna señal elegible para la línea editorial.

### Cupo y decisión
- `main` HEAD `84731657f14e31f16984b95651bc4fe0c2b2c2c2`; el compare desde el HEAD anterior no muestra cambios en `data/miniaturas_auditoria_2026-11-21.json` ni `data/rehechos_2026-11-22.json`. `data/horarios.json` sí cambió y ahora documenta ventanas activas 06:30–07:30 y 16:30–18:00, más 23:30 fijo.
- El conteo 25-nov sigue **7/5** por cinco registros del snapshot más dos reworks; no hay cupo. No se crea storyboard ni cola. La disponibilidad de texto primario no equivale a selección editorial ni a DOI resuelto.


---

## Revalidación 2026-11-25 00:03 CDMX

### Fuentes de tendencia

Se reintentaron los diez feeds declarados en scripts/tendencias.py y Google Trends RSS México. El runtime local devolvió error DNS 6 para cada host:

- ScienceDaily ciencia, salud y espacio: curl (6), Could not resolve host: www.sciencedaily.com.
- Phys.org: curl (6), Could not resolve host: phys.org.
- NASA: curl (6), Could not resolve host: www.nasa.gov.
- ESA: curl (6), Could not resolve host: www.esa.int.
- Nature: curl (6), Could not resolve host: www.nature.com.
- EurekAlert: curl (6), Could not resolve host: www.eurekalert.org.
- SINC: curl (6), Could not resolve host: www.agenciasinc.es.
- UNAM Global: curl (6), Could not resolve host: unamglobal.unam.mx.
- Google Trends RSS México: curl (6), Could not resolve host: trends.google.com.

El lector web tampoco pudo consumir varios XML por su tipo MIME. Google Trends HTML sí abrió como respaldo: 214 tendencias; las primeras 25 no aportaron un tema científico verificable. “Marte” y “fenómeno” no se promovieron sin una fuente científica primaria.

### DOI y candidatos

Crossref no se pudo consultar: curl (6), Could not resolve host: api.crossref.org. El resolvedor doi.org agotó el límite de cinco segundos: curl (28), Resolving timed out after 5000 milliseconds. Por tanto, ningún DOI queda marcado como verificado por Crossref/resolvedor.

Revalidación de páginas editoriales: PLOS Biology y Nature Climate Change abrieron; las páginas de Nature Astronomy, Nature Communications y Scientific Reports devolvieron error 500 en el paso de autorización por cookies. Se conserva el estado documental previo de los cinco candidatos, sin elevar ninguno a seleccionado. El candidato de Nature Climate Change continúa PENDING_SOURCE para una narración que requiera más que el resumen.

### Cupo y decisión

La ocupación registrada sigue en 7/5 para el 25–28 de noviembre y 5/5 para el 29. No hay slot libre. No se creó storyboard ni se seleccionó candidato. El corte de este radar corresponde a feature HEAD 1bce9a7a200073d0a4286d0d69f027b7ea45ea93 y main HEAD 7b50235a1a46b4d759796253e0d036fb147c4401. La revisión de cola y producción preexistente queda en 2026-11-25_CONTROL_COLA_00H.md.


## Revalidación de feeds — 2026-11-25 04:06 CDMX

Se repitió el acceso directo a los diez feeds configurados y a Google Trends RSS México. Errores exactos:
- `curl: (6) Could not resolve host`: `https://www.sciencedaily.com/rss/top/science.xml`, `https://www.sciencedaily.com/rss/top/health.xml`, `https://www.esa.int/rssfeed/Our_Activities/Space_Science`, `https://www.agenciasinc.es/rss`, `https://unamglobal.unam.mx/feed/` y `https://trends.google.com/trending/rss?geo=MX`.
- `curl: (28) Resolving timed out after 6000 milliseconds`: `https://www.sciencedaily.com/rss/space_time.xml`, `https://phys.org/rss-feed/`, `https://www.nasa.gov/news-release/feed/`, `https://www.nature.com/nature.rss` y `https://www.eurekalert.org/rss/news.xml`.
- Crossref API y el resolvedor `doi.org` también terminaron con `curl: (28) Resolving timed out after 6000 milliseconds`.

Como respaldo se abrió el HTML oficial de Google Trends México: mostró 210 tendencias. La primera página no aporta un candidato científico apto sin una fuente primaria adicional. Se mantienen los cinco candidatos ya registrados; no se declara DOI verificado por Crossref/resolvedor y no se agrega storyboard. La ocupación sigue en 7/5 del 25 al 28 y 5/5 el 29, por lo que no existe slot autorizado.


## Actualización de verificación — 2026-11-25 08:30 CDMX

### Ingesta RSS y Google Trends

No se ejecutó localmente `scripts/tendencias.py`: este entorno no dispone de un checkout ejecutable con red. Se hizo una lectura alternativa directa de las URLs declaradas en el script mediante un fetch externo, sin alterar el repositorio.

- Lectura obtenida: ScienceDaily (science, health y space_time) y Phys.org.
- Lectura obtenida pero desactualizada para este corte: NASA (último ítem visible 2026-09-01) y UNAM Global (2026-05-18).
- Errores exactos de la alternativa: ESA RSS `CRAWL_NOT_FOUND`; Nature RSS `CRAWL_UNEXPECTED_CONTENT_TYPE`; EurekAlert RSS `CRAWL_UNEXPECTED_CONTENT_TYPE`; SINC RSS `CRAWL_NOT_FOUND`; Google Trends RSS México `CRAWL_NOT_FOUND`.
- Respaldo oficial: [Google Trends México — página Trending Now](https://trends.google.com/trending?geo=MX), consultada en este corte. Mostró 25 tendencias; ninguna correspondió a ciencia, naturaleza o espacio con fuente primaria apta. “epicentro” apareció como tendencia, pero sin identificar un evento oficial concreto; no se convirtió en candidato.

### Verificación DOI/Crossref

Se consultó directamente la API de Crossref y el resolvedor DOI para los cinco candidatos originales:

- Varroa — [Crossref](https://api.crossref.org/works/10.1371/journal.pbio.3004091) / [DOI](https://doi.org/10.1371/journal.pbio.3004091): `status=ok`; título resuelto coincide.
- Norma — [Crossref](https://api.crossref.org/works/10.1038/s41550-026-03010-5) / [DOI](https://doi.org/10.1038/s41550-026-03010-5): `status=ok`; título resuelto coincide.
- Plankton — [Crossref](https://api.crossref.org/works/10.1038/s41467-026-79817-7) / [DOI](https://doi.org/10.1038/s41467-026-79817-7): `status=ok`; título resuelto coincide.
- Glaciares — [Crossref](https://api.crossref.org/works/10.1038/s41558-026-02808-5) / [DOI](https://doi.org/10.1038/s41558-026-02808-5): `status=ok`; título resuelto coincide. El texto completo sigue sin estar disponible en el acceso consultado; conserva `PENDING_SOURCE`.
- Pantoea — [Crossref](https://api.crossref.org/works/10.1038/s41598-026-80573-3) / [DOI](https://doi.org/10.1038/s41598-026-80573-3): `status=ok`; título resuelto coincide.

### Shortlist de investigación vigente (5)

1. **Varroa / hipoxia** — publicación 2026-11-19; texto primario completo; Crossref y resolvedor verificados. Mantener el límite entre respuesta metabólica medida y cualquier inferencia sobre supervivencia de la colonia.
2. **Brazo de Norma** — publicación 2026-11-20; fuente primaria de *Nature Astronomy*; Crossref y resolvedor verificados. Separar observación de rayos X, modelo geométrico e interpretación física.
3. **Complejidad del plancton** — publicación 2026-11-21; fuente primaria de *Nature Communications*; Crossref y resolvedor verificados. Mantener las proyecciones como resultados del modelo, no como observaciones actuales.
4. **Pantoea asociada a quinoa** — publicación 2026-11-22; texto primario completo; Crossref y resolvedor verificados. Límite obligatorio: el ensayo de crecimiento bajo estrés salino se realizó en *Arabidopsis thaliana*; no demuestra mayor rendimiento de quinoa en campo.
5. **Saltamontes acuáticos del Mesozoico** — [Crossref](https://api.crossref.org/works/10.1098/rspb.2026.0751) `status=ok`; DOI `10.1098/rspb.2026.0751`; publicación impresa 2026-11-18 e indexación del registro 2026-11-25. El resumen primario atribuye locomoción sobre la superficie del agua a morfología funcional y análisis hidrodinámicos de fósiles en ámbar. El resolvedor y la página completa del editor agotaron tiempo de consulta (`CRAWL_LIVECRAWL_TIMEOUT`); por tanto permanece `PENDING_SOURCE` hasta recuperar el texto primario completo. No narrar como conducta observada en animales vivos.

El candidato de glaciares pasa a reserva por texto completo inaccesible. Se conservan como reservas, no como candidatos de esta ventana de siete días: fotoluminiscencia de puercoespines (artículo primario 2026-11-16), rivalidad de hormigas invasoras (publicación primaria 2026-11-11), PET-trazador (2026-08-13), positrón (2026-10-21), cometa de Euclid (2026-10-18) y capa de agua sobre hielo (2026-11-03). La fecha de una nota RSS reciente no sustituye la fecha de publicación del estudio primario.

**Decisión operativa:** el shortlist queda en investigación, no seleccionado. El corte del 25 de noviembre continúa sin slot libre; no se crea storyboard ni se cambia `ESTADO_EJECUCION`, `narrative_qa`, `cola/entrada` o `cola/estado`.


## Revalidación adicional — 2026-11-25 09:01 CDMX

### RSS y Google Trends

Se reintentó la lectura directa de todas las URL declaradas en `scripts/tendencias.py` y Google Trends RSS México. Este lector devolvió:

- ScienceDaily ciencia, salud y espacio: `400 Unsupported content-type: application/xml`.
- Phys.org: `400 Unsupported content-type: text/xml`.
- NASA: `400 Unsupported content-type: application/rss+xml`.
- ESA Space Science: `404 Not Found`.
- Nature: `500 Redirected to idp.nature.com/authorize`.
- EurekAlert y SINC: `URL is not accessible via this tool`.
- UNAM Global: `400 Unsupported content-type: application/rss+xml`.
- Google Trends RSS México: `URL is not accessible via this tool`.

No se declara que el script local se haya ejecutado: este corte fue una lectura externa de las URL. Como respaldo, la página HTML oficial de Google Trends México abrió y mostró 231 tendencias totales, con 25 visibles. La tendencia visible «fenómeno» (5K+) es demasiado genérica para convertirse en candidato sin una fuente científica identificable; las demás señales visibles no aportan un tema apto para la línea editorial. No se selecciona ningún tema por tendencia sola.

### Candidato 5 — nueva fuente institucional

Se localizó el comunicado de investigación del **Nanjing Institute of Geology and Palaeontology, Chinese Academy of Sciences**, fechado 2026-11-24: https://english.nigpas.cas.cn/new/hs/rp/202611/t20261124_1220626.html

El comunicado identifica el artículo de Xu, Luo y Beutel, *Extreme morphological specialization in Mesozoic water-walking grasshoppers*, *Proceedings of the Royal Society B* (2026), DOI `10.1098/rspb.2026.0751`. Describe fósiles en ámbar de Kachin de aproximadamente 100 millones de años, una base morfo-ecológica de 195 especies y análisis filogenéticos, de morfoespacio e hidrodinámicos. Los cálculos publicados comparan fuerzas de curvatura de aproximadamente 222.78 y 157.46 dynes con pesos estimados de 3.20 y 2.03 dynes en dos especímenes. También informa al menos nueve individuos en una pieza de ámbar.

**Límite:** la locomoción sobre el agua es una reconstrucción apoyada en morfología y análisis, no una conducta observada directamente. La fuente institucional mejora la trazabilidad del hallazgo, pero no sustituye el texto íntegro del artículo ni una respuesta verificable del resolvedor. Se conserva `PENDING_SOURCE` para storyboard; no se eleva a seleccionado.

### Reintento DOI/resolvedor

A las 09:01, el lector externo no pudo abrir los diez endpoints Crossref/doi.org correspondientes a los cinco DOI (`URL is not accessible via this tool`). Esto no invalida la verificación positiva registrada a las 08:30 para Varroa, Norma, plancton y Pantoea; tampoco añade una verificación nueva. El DOI del saltamontes conserva su estado pendiente de resolvedor. No se cambia ningún estado a partir de una respuesta de acceso fallida.

### Decisión

La ocupación documentada sigue en 7/5 para el 25–28 de noviembre y 5/5 el 29. No existe slot autorizado. No se crea storyboard, no se promueve cola, no se modifican `data/*.json`, no se crean estados Grok ni se generan medios.

## Revalidación adicional — 2026-11-25 10:02 CDMX

### RSS y Google Trends México

Se intentó abrir cada URL configurada en `scripts/tendencias.py` y el RSS de Google Trends México. El lector web devolvió estos errores exactos:

- ScienceDaily ciencia, salud y espacio: `400 Unsupported content-type: application/xml`.
- Phys.org: `400 Unsupported content-type: text/xml`.
- NASA RSS: `400 Unsupported content-type: application/rss+xml`.
- ESA Space Science: `404 Not Found`.
- Nature RSS: `500 Redirected to idp.nature.com/authorize`.
- EurekAlert y SINC: `URL is not accessible via this tool`.
- UNAM Global: `400 Unsupported content-type: application/rss+xml`.
- Google Trends RSS México: `URL is not accessible via this tool`.

No se declara ejecución local de `scripts/tendencias.py`. Como respaldo se abrió la página oficial HTML de Google Trends México: 237 tendencias totales, 25 visibles. Entre las señales visibles aparecen «marte» (5K+), «fenómeno» (5K+) y «bienestar de los animales» (1K+); ninguna identifica por sí sola un hallazgo científico verificable. No se selecciona tema por tendencia sola.

### Sustitución del quinto candidato — Europa Clipper

Se incorpora como quinto candidato activo, en sustitución del saltamontes acuático que pasa a reserva `PENDING_SOURCE`:

- **Tema:** asistencia gravitatoria terrestre de Europa Clipper antes de continuar hacia Júpiter.
- **Fuente primaria institucional:** NASA Jet Propulsion Laboratory, 25-nov-2026: https://www.jpl.nasa.gov/news/nasas-europa-clipper-zooming-by-earth-on-way-to-jupiters-icy-moon/
- **Observación publicada:** sobrevuelo terrestre previsto para el 3-dic-2026; aproximación de 3,140–3,450 km, punto más cercano al oeste de África a las 3:14 p. m. EST; masa aproximada de 6,000 kg. La asistencia gravitatoria cambia la trayectoria y aumenta la velocidad hacia Júpiter. Los nueve instrumentos recogerán datos durante el paso para calibración.
- **Límite:** es una actualización oficial de misión, no un nuevo artículo de investigación ni una observación de Europa. No afirmar que el sobrevuelo confirma el océano o vida; la misión investigará esos aspectos al llegar al sistema joviano.
- **Posible eje narrativo:** la Tierra funciona como una honda gravitatoria que cambia la trayectoria de una nave sin combustible adicional para ese impulso.
- **Estado de fuente:** URL primaria abierta y consultada; no hay DOI. La comprobación automática de URL del validador `--check-doi` no se ejecutó en este entorno, por lo que queda `VALIDACION_AUTOMATICA_PENDIENTE`.

El buscador del repositorio no encontró «Europa Clipper» en los artefactos indexados; no se detectó duplicado textual. El tema queda como candidato de investigación, no seleccionado.

### Candidato de antimateria descartado para esta ventana

ScienceDaily publicó el 25-nov una nota sobre el ciclotrón cuántico de un positrón. La fuente primaria de *Physical Review Letters* confirma que el artículo «One-Positron Quantum Cyclotron» fue publicado el 21-oct-2026. La nota es reciente, pero el estudio no está dentro de la ventana de siete días; queda en reserva y no se presenta como descubrimiento de hoy. El experimento habilita una comparación futura de momentos magnéticos; no demuestra una diferencia materia-antimateria ni explica ya la asimetría cósmica.

### Estado del shortlist y del cupo

Shortlist activo: Varroa/hipoxia, brazo Norma, complejidad del plancton, Pantoea asociada a quinoa y Europa Clipper. Los cuatro primeros conservan la verificación positiva de Crossref/resolvedor registrada a las 08:30; este corte no pudo repetir el acceso a esos endpoints. Europa Clipper queda con URL primaria accesible y validación automática pendiente. Saltamontes acuáticos permanece en reserva hasta recuperar el texto primario completo y el resolvedor.

La ocupación continúa en 7/5 del 25 al 28 de noviembre y 5/5 el 29. No existe slot autorizado. No se crea storyboard ni se promueve cola.

## Exploración complementaria — 25 de noviembre, 14:09 CDMX

### Fuentes de tendencia y errores de lectura

Se leyó la lista de feeds de scripts/tendencias.py y se probaron directamente sus diez URLs. El lector no pudo consumir los XML/RSS; estos errores describen la limitación del lector, no demuestran que los servidores de origen estén caídos:

- ScienceDaily ciencia, salud y espacio: HTTP 400, Unsupported content-type: application/xml.
- Phys.org: HTTP 400, Unsupported content-type: text/xml.
- NASA News Release: HTTP 400, Unsupported content-type: application/rss+xml.
- ESA Space Science: HTTP 404, Not Found.
- Nature RSS: HTTP 400, Unsupported content-type: application/rss+xml.
- EurekAlert: URL not accessible via this tool.
- Agencia SINC: URL not accessible via this tool.
- UNAM Global: HTTP 400, Unsupported content-type: application/rss+xml.
- Google Trends RSS México: URL not accessible via this tool.

Respaldo oficial: Google Trends México, vista HTML de últimas 24 horas. Muestra 240 tendencias y 25 por página. En las primeras 25 no aparece un hallazgo científico identificable; «bienestar de los animales» (5 mil+) y «primera tormenta invernal» (10 mil+) son señales temáticas generales, no evidencia científica ni candidatos por sí solas.

### Cuatro candidatos nuevos — no seleccionados

1. **Un agujero negro de 6.500 millones de masas solares cuando el universo tenía 1.300 millones de años**
   - Fecha: 20 nov 2026. Objeto: W2246-0526, cuásar oscurecido a z=4,6.
   - Observación: ALMA resolvió movimientos de gas de carbono ionizado y CO en escalas de unos 700 años luz; el patrón de velocidades es coherente con la influencia gravitacional del agujero negro.
   - Cálculo publicado: masa dinámica estimada de 6.500 millones de masas solares.
   - Inferencia de los autores: la capa densa de polvo podría proteger trazadores gaseosos de la radiación X y permitir medir el entorno más cercano.
   - Límite: no convertir la hipótesis de protección por polvo en mecanismo demostrado ni presentar la masa como medición directa del horizonte.
   - Fuente institucional y enlace al artículo primario: https://www.almaobservatory.org/es/comunicados-de-prensa/alma-observa-la-esfera-de-influencia-gravitacional-de-un-agujero-negro-en-el-universo-temprano/
   - Artículo: «Resolving the black hole sphere of influence in a hyperluminous obscured quasar at redshift 4.6», Science Advances, DOI 10.1126/sciadv.aek9035. DOI/resolvedor: PENDING_RESOLVER (Science.org respondió 403 en esta lectura).

2. **La maquinaria de transcripción del poxvirus ya está empacada dentro de su cápside**
   - Fecha: 23 nov 2026. Modelo estudiado: vaccinia, un poxvirus usado como modelo experimental.
   - Observación: crio-tomografía electrónica reconstruyó dentro del núcleo viral la ARN-polimerasa en pares y el complejo de portal por el que se cree que sale el ARNm.
   - Inferencia: el virus lleva un sistema de transcripción preparado para activarse después de entrar en la célula.
   - Límite: no afirmar que el hallazgo ya sea un antiviral ni extrapolar sin matiz a todos los poxvirus; el estudio ofrece posibles blancos para investigación futura.
   - Fuente institucional: https://www.ist.ac.at/en/news/inside-the-poxvirus-headquarters/
   - Artículo: «Architecture of the poxvirus early-transcription machinery and portal complex», Nature, DOI 10.1038/s41586-026-11458-8. DOI/resolvedor: PENDING_RESOLVER (doi.org redirigió a una pantalla de autorización de Nature no accesible).

3. **Una interfaz de batería con relieve tipo huevera retrasa diez veces el inicio de vacíos**
   - Fecha: 23 nov 2026. Sistema: litio / electrolito cerámico Li6PS5Cl en baterías de estado sólido.
   - Observación: una topografía 3D tipo egg-box elevó de 0,2 a 2 mA cm−2 la corriente de descarga a la que comienza el vaciado, a 2 MPa y 30 °C. El artículo aclara que no elimina los vacíos: reduce su crecimiento y la polarización.
   - Cálculo: mejora de 10× bajo esas condiciones concretas; también se probaron pulsos y un perfil de conducción WLTP.
   - Inferencia: la geometría de contacto puede mejorar el transporte de litio sin añadir una nueva composición de materiales.
   - Límite: celdas y condiciones de laboratorio; no afirmar que ya sea una batería comercial ni que resuelva todos los modos de fallo.
   - Artículo primario: https://www.nature.com/articles/s41560-026-02172-w — DOI 10.1038/s41560-026-02172-w. DOI/resolvedor: PENDING_RESOLVER; la página de Nature sí declara el DOI.

4. **Síntesis continua de péptidos de N a C sin aislar cada intermedio**
   - Fecha: 23 nov 2026. Método: NCPS con aminoácidos o fragmentos sin proteger ambos extremos.
   - Observación: el artículo informa rendimiento promedio ≥95 % por acoplamiento, epimerización ≤1,0 % y siete acoplamientos consecutivos; demuestra fragmento de tirzepatida, degarelix, un macrociclo de 14 residuos y semaglutida.
   - Cálculo publicado: aproximadamente 10× menos aislamientos y hasta 100× menos residuos.
   - Inferencia: puede reducir etapas de proceso y desperdicio en síntesis de péptidos.
   - Límite: demostración de química de proceso; no demuestra adopción comercial ni cambios en eficacia, seguridad o disponibilidad clínica de esos medicamentos.
   - Artículo primario: https://www.nature.com/articles/s41586-026-11448-w — DOI 10.1038/s41586-026-11448-w. DOI/resolvedor: PENDING_RESOLVER; el resultado de Nature declara DOI permanente, pero el resolvedor no fue accesible.

### Compuertas

- Crossref REST y los resolvedores DOI se intentaron; las respuestas fueron errores internos, 403 o redirecciones de autorización. Ninguno de estos cuatro candidatos queda con DOI verificado por Crossref/resolvedor en este corte.
- No se asigna fecha_objetivo ni slot_local. La ocupación del 25–29 nov supera la capacidad y hay colisiones documentadas; no hay slot libre autorizado.
- No se crea storyboard. Los cuatro permanecen como candidatos de radar, no recibidos, seleccionados ni preparados.

## Revalidación adicional — 25-nov-2026 16:01 CDMX

### RSS y Google Trends México

No se ejecutó localmente `scripts/tendencias.py`: esta sesión no dispone de un checkout ejecutable con red. Se intentó abrir directamente cada URL configurada y Google Trends RSS México. Errores exactos del lector:

- ScienceDaily ciencia, salud y espacio: `400 Unsupported content-type: application/xml`.
- Phys.org: `400 Unsupported content-type: text/xml`.
- NASA News Release: `400 Unsupported content-type: application/rss+xml`.
- ESA Space Science: `404 Not Found`.
- Nature RSS: `400 Unsupported content-type: application/rss+xml`.
- EurekAlert y Agencia SINC: `URL ... is not accessible via this tool`.
- UNAM Global: `400 Unsupported content-type: application/rss+xml`.
- Google Trends RSS México: `URL ... is not accessible via this tool`.

Respaldo oficial: [Google Trends México — Trending Now](https://trends.google.com/trending?geo=MX), vista HTML de últimas 24 horas. La página muestra 221 tendencias y 25 visibles. La mayoría de las primeras 25 son consultas deportivas o de actualidad general; «bienestar de los animales» aparece con 5K+, pero no identifica un hallazgo concreto. No se convirtió ninguna tendencia en candidato sin fuente científica primaria.

### Revalidación de los cuatro candidatos del corte 14:09

**1. W2246-0526 — esfera de influencia de un agujero negro temprano**

- Fuente institucional primaria: [ALMA Observatory, 20-nov-2026](https://www.almaobservatory.org/es/comunicados-de-prensa/alma-observa-la-esfera-de-influencia-gravitacional-de-un-agujero-negro-en-el-universo-temprano/).
- Registro bibliográfico: [PubMed PMID 43063285](https://pubmed.ncbi.nlm.nih.gov/43063285/), que identifica el artículo de *Science Advances* y el DOI `10.1126/sciadv.aek9035`.
- Observación/cálculo publicado: movimientos de gas trazados con [C II] y CO; masa dinámica estimada de aproximadamente 6.5 mil millones de masas solares, en W2246-0526 a z=4.6, cuando el universo tenía cerca de 1.3 mil millones de años. La resolución citada por ALMA alcanza escalas de unos 700 años luz.
- Inferencia de autores: el polvo denso podría proteger los trazadores gaseosos de parte de la radiación X. No presentarlo como mecanismo demostrado.
- Límite: es una medición dinámica estimada a partir de gas, no una observación del horizonte ni una medición directa de la masa del horizonte.
- DOI/resolvedor: `PENDING_RESOLVER`.

**2. Vaccinia — maquinaria de transcripción dentro del núcleo del poxvirus**

- Fuente primaria: [Nature, 23-nov-2026](https://www.nature.com/articles/s41586-026-11458-8).
- Registro bibliográfico: [PubMed PMID 43072752](https://pubmed.ncbi.nlm.nih.gov/43072752/); DOI declarado `10.1038/s41586-026-11458-8`.
- Respaldo institucional: [Institute of Science and Technology Austria](https://www.ist.ac.at/en/news/inside-the-poxvirus-headquarters/).
- Observación: crio-tomografía y promediado de sub-tomogramas en núcleos de vaccinia revelan una ARN-polimerasa viral en dímero de reposo de 1.8 MDa, asociada con VETF; se describen además componentes VPK2/L4 y un complejo de portal de salida de ARNm.
- Límite: el sistema experimental es vaccinia, usado como modelo; no generalizar cada detalle a todos los poxvirus ni presentarlo como antiviral disponible.
- DOI/resolvedor: `PENDING_RESOLVER`.

**3. Interfaz tipo huevera — vaciado en baterías de estado sólido**

- Fuente primaria: [Nature, «Contouring mitigates voiding at the lithium/ceramic electrolyte interface on discharging solid-state batteries»](https://www.nature.com/articles/s41560-026-02172-w), DOI declarado `10.1038/s41560-026-02172-w`.
- La discusión del artículo confirma el resultado de diez veces: con 2 MPa y 30 °C, la interfaz contorneada eleva la corriente de descarga a la que comienza el vaciado de 0.2 a 2 mA cm⁻² frente a una interfaz plana.
- Condiciones que no deben mezclarse: el artículo también estudia pulsos de 3 mA cm⁻² a 2 MPa/30 °C y 8 mA cm⁻² a 2 MPa/60 °C; el perfil WLTP llega a pulsos de hasta 9 mA cm⁻² bajo 2 MPa/60 °C. No atribuir esos 9 mA cm⁻² al ensayo constante de 30 °C.
- Límite: celdas y protocolos experimentales; no equivale a una batería comercial ni demuestra que se hayan eliminado todos los modos de fallo.
- DOI/resolvedor: `PENDING_RESOLVER`.

**4. Síntesis continua de péptidos de N a C**

- Fuente primaria: [Nature, 23-nov-2026](https://www.nature.com/articles/s41586-026-11448-w).
- Registro bibliográfico: [PubMed PMID 43072754](https://pubmed.ncbi.nlm.nih.gov/43072754/); DOI declarado `10.1038/s41586-026-11448-w`.
- Observación del artículo: síntesis continua con aminoácidos o fragmentos sin proteger ambos extremos; rendimiento promedio ≥95 % por acoplamiento, epimerización ≤1.0 % y siete acoplamientos consecutivos. Se reportan ejemplos con fragmento de tirzepatida, degarelix, macrociclo de 14 residuos y semaglutida.
- Cálculo reportado por los autores: alrededor de 10 veces menos aislamientos y hasta 100 veces menos residuos.
- Límite: demostración de química de proceso; no demuestra adopción comercial ni cambios en eficacia, seguridad o disponibilidad clínica de esos fármacos.
- DOI/resolvedor: `PENDING_RESOLVER`.

### Compuerta DOI/Crossref

Se intentó abrir `api.crossref.org/works/{doi}` y los cuatro enlaces `doi.org/{doi}`. El lector devolvió `URL ... is not accessible via this tool` en todos los casos. Las páginas editoriales y los registros PubMed confirman los DOI declarados en tres candidatos; la página editorial confirma el del estudio de baterías. Eso no sustituye la compuerta exigida de Crossref/resolvedor. Ninguno se eleva a `VERIFICADO_CROSSREF`; los cuatro conservan `PENDING_RESOLVER`.

### Decisión

- Se mantienen cuatro candidatos recientes en el radar; ninguno queda seleccionado.
- La ocupación del 25–28 nov continúa en 7/5 y el 29 nov en 5/5 según los registros de programación ya auditados. No hay `fecha_objetivo + slot_local` libre y autorizado.
- No se crea storyboard, no se promueve cola, no se modifica `data/*.json`, no se crea/edita estado Grok y no se generan medios.
