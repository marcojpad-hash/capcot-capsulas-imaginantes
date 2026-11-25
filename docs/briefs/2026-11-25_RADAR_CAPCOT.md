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
