# Radar CAPCOT — 2026-11-26

**Corte:** 2026-11-26, 02:14 America/Mexico_City  
**Serie:** Datos y ociosidades  
**Estado editorial:** PROPUESTAS; ninguna seleccionada ni recibida por Grok.  
**Decisión de producción:** no crear storyboard en este run: la ocupación real del slot 23:30 no puede certificarse sin una lectura vigente de YouTube Studio/historial de programación.

## 1. Fuentes de tendencia y disponibilidad

Se inspeccionó `scripts/tendencias.py` y se recuperaron manualmente sus endpoints configurados. El script Python no se ejecutó en un runner del repositorio; los estados siguientes corresponden a recuperación web directa, no a excepciones de `urllib`:

| Feed configurado | Resultado observado |
|---|---|
| ScienceDaily — science.xml | Recuperado; último ítem visible 25-nov-2026 21:42 EST |
| ScienceDaily — health.xml | Recuperado; último ítem visible 25-nov-2026 21:43 EST |
| ScienceDaily — space_time.xml | Recuperado; último ítem visible 25-nov-2026 21:55 EST |
| Phys.org — rss-feed | Recuperado; último ítem visible 26-nov-2026 02:30 EST |
| NASA — news-release/feed | Recuperación correcta, pero feed desactualizado: último contenido visible 1-sep-2026 |
| UNAM Global — /feed | Recuperación correcta, pero feed desactualizado: último contenido visible 18-may-2026 |
| ESA — Space Science RSS | `CRAWL_NOT_FOUND` |
| Nature — nature.rss | `CRAWL_UNEXPECTED_CONTENT_TYPE` |
| EurekAlert — news.xml | `CRAWL_NOT_FOUND` |
| Agencia SINC — /rss | `CRAWL_NOT_FOUND` |
| Google Trends RSS México | `CRAWL_UNEXPECTED_CONTENT_TYPE` |

**Respaldo oficial de Trends:** se consultó la página HTML [Google Trends — Trending Now, México](https://trends.google.com/trending?geo=MX). La última actualización visible fue 25-nov-2026 20:49. Los primeros 25 temas estaban dominados por deportes, entretenimiento y conversación general; no apareció una tendencia científica/natural/cósmica apta para convertirla en dato del día. Trends se usa como señal secundaria, no como fuente de claims.

Los errores `CRAWL_*` describen la respuesta del recuperador; no prueban que el servidor de origen esté caído. Se usaron páginas primarias oficiales y Crossref como respaldo.

## 2. Candidatos recientes

### C1 — Comunicación gravitacional a través de un muro

- **Estado:** PROPUESTA; prioridad alta; no seleccionada.
- **Fuente primaria:** *Science Advances*, “Unblockable communication with gravity”, DOI [10.1126/sciadv.aee0802](https://doi.org/10.1126/sciadv.aee0802).
- **Verificación:** [Crossref REST](https://api.crossref.org/works/10.1126/sciadv.aee0802) respondió `status=ok` y devolvió el mismo DOI/título; metadatos sitúan la publicación el 20-nov-2026. La página de Science.org respondió `403 Forbidden`; Crossref y el registro bibliográfico de PubMed se usaron como respaldo de metadatos.
- **Observación:** el experimento codificó información mediante el movimiento de masa y detectó una señal gravitacional a 0.7 m, al otro lado de una pared de ladrillo, a una tasa de aproximadamente un bit por minuto.
- **Cálculo:** un bit/min equivale a 60 bits/h; no implica una tasa práctica de comunicación.
- **Inferencia y límite:** es una demostración de laboratorio, no una alternativa operativa a radio, fibra o redes convencionales. Las proyecciones a distancias mayores no son resultados medidos.
- **Recomendación:** mejor candidato para el siguiente slot confirmado. Gancho posible: “El mensaje cruzó el muro”, siempre contextualizando distancia, tasa y condición experimental.

### C2 — Hera observa el cráter del impacto DART

- **Estado:** PROPUESTA; prioridad alta; no seleccionada.
- **Fuente primaria:** [ESA — Hera reveals stadium-sized asteroid crater left after spacecraft impact](https://www.esa.int/articles/about-us/directorates/operations/space-safety/hera/hera-reveals-stadium-sized-asteroid-crater-left-after-spacecraft-impact), 25-nov-2026.
- **Verificación:** URL oficial ESA recuperada; no se declara DOI porque es una actualización primaria de misión.
- **Observación:** la nota describe el cráter en Dimorphos, una luna de unos 151 m, dentro del sistema Didymos (unos 730 m); también informa de bloques alrededor del sistema y del cambio orbital producido tras el impacto de DART.
- **Cálculo:** no se añade cálculo propio. La reducción orbital publicada por ESA se conserva como cifra atribuida a la misión.
- **Inferencia y límite:** Hera está caracterizando la estructura y las consecuencias del impacto; no debe afirmarse que una sola imagen demuestra por sí misma la eficacia general de cualquier técnica de desvío.
- **Recomendación:** candidato visual fuerte, distinto de los temas recientes de Voyager y púlsares.

### C3 — Electrolito que se endurece bajo impacto

- **Estado:** PROPUESTA; prioridad media-alta; no seleccionada.
- **Fuente primaria:** Nature Communications, “Nanofriction strengthened mechanically adaptive electrolytes for safe lithium metal batteries”, DOI [10.1038/s41467-026-78955-2](https://doi.org/10.1038/s41467-026-78955-2).
- **Verificación:** [Crossref REST](https://api.crossref.org/works/10.1038/s41467-026-78955-2) respondió `status=ok`; publicación fechada 20-nov-2026.
- **Observación:** el trabajo describe un aumento de viscosidad inducido por impacto de hasta 160 veces y una atenuación de fuerza de impacto del 73.1% en las condiciones ensayadas; también informa pruebas en celdas pouch de laboratorio.
- **Cálculo:** no se extrapolan porcentajes a baterías comerciales ni a otros diseños.
- **Inferencia y límite:** los resultados pertenecen a una química y un protocolo experimental concretos; no equivalen a una certificación de seguridad de baterías comerciales.
- **Recomendación:** visualmente atractivo, pero revisar rotación porque el 19-nov se trabajó otro tema de materiales.

### C4 — Pantalla de imagen del genoma en la periferia nuclear

- **Estado:** PROPUESTA; prioridad media; no seleccionada.
- **Fuente primaria:** Nature Communications, “A genome-wide imaging screen reveals epigenetic and mechanistic partitioning of lamina-associated chromatin”, DOI [10.1038/s41467-026-79468-8](https://doi.org/10.1038/s41467-026-79468-8).
- **Verificación:** [Crossref REST](https://api.crossref.org/works/10.1038/s41467-026-79468-8) respondió `status=ok`; publicación fechada 20-nov-2026.
- **Observación:** el estudio presenta un cribado de imagen de más de cien genes implicados en la organización de regiones cromatínicas asociadas a la lámina nuclear; identifica a hnRNPK como necesario para posicionar una fracción cercana a dos tercios de esas regiones en el sistema celular estudiado.
- **Cálculo:** no se convierte “cerca de dos tercios” en una proporción universal de todas las células.
- **Inferencia y límite:** resultado de biología celular; no es una explicación clínica ni una terapia.
- **Recomendación:** candidato científicamente sólido, pero rotación cautelosa por el tema genético del 22-nov.

### C5 — Dragonfly integra sus siete cámaras

- **Estado:** PROPUESTA; prioridad media; no seleccionada.
- **Fuente primaria:** [NASA — NASA's Titan-Bound Dragonfly Rotorcraft Gets Its Eyes](https://science.nasa.gov/missions/dragonfly/nasas-titan-bound-dragonfly-rotorcraft-gets-its-eyes/), 24-nov-2026.
- **Verificación:** página oficial NASA recuperada; actualización de misión, sin DOI.
- **Observación:** NASA informa de la integración de siete cámaras en el rotorcraft Dragonfly, destinado a Titán; la misión afrontará temperaturas cercanas a −290 °F y una noche de unos ocho días terrestres.
- **Cálculo:** el total de siete cámaras se obtiene del inventario de cámaras descrito por NASA; no se presentan imágenes de sala limpia como si fueran fotografías de Titán.
- **Inferencia y límite:** es un hito de integración previo al lanzamiento, no un resultado científico obtenido en Titán. La llegada está prevista para la década de 2030.
- **Recomendación:** buen respaldo visual, pero menor prioridad por saturación reciente de temas espaciales.

## 3. Candidatos descartados o relegados

- **Lagos salinos bajo el mar Rojo:** la nota reciente de ScienceDaily remite a un estudio de 2022; no es una investigación nueva de esta semana.
- **Trampa de positrones/antimateria:** la noticia apareció en el feed reciente, pero el artículo primario se publicó en octubre; fuera de la ventana de investigación de siete días.
- **Cometa observado por Euclid:** la noticia de difusión es posterior, pero el descubrimiento/confirmación citados son anteriores a esta ventana.
- **Erupción de Iwo Jima:** se relega para evitar proximidad temática con el proyecto de Fentale del 21-nov.

## 4. Slot y decisión

- `data/horarios.json` fija 23:30 como slot del dato del día, pero el archivo se actualizó por última vez el 9-nov.
- En `proyectos/`, `cola/entrada/`, `publicaciones` y los registros consultados no aparece un proyecto del 26-nov a las 23:30.
- En `main` sí hay reworks del 26-nov a las 10:00 y 15:00 y una colisión de dos IDs a las 17:00. No aparece una entrada de 23:30 en los snapshots consultados.
- No hay un `historial_youtube` vigente ni lectura actual de YouTube Studio para descartar IDs antiguos todavía programados.

**Resultado:** `OCUPACION_23_30_NO_CONCILIADA`. No se asigna el slot, no se crea storyboard y no se marca ningún candidato como seleccionado. C1 queda recomendado para el siguiente slot cuya ocupación se pueda verificar.


## Addendum de radar y fuentes — 2026-11-26 05:55 CDMX

### Relectura de feeds configurados

La relectura de los RSS a través del lector web no pudo procesar los XML/RSS. Esto describe la limitación del lector, no demuestra que los servidores de origen estén caídos.

| Feed | Error exacto observado en esta relectura |
|---|---|
| ScienceDaily science.xml | HTTP 400 — Unsupported content-type (XML) |
| ScienceDaily health.xml | HTTP 400 — Unsupported content-type (XML) |
| ScienceDaily space_time.xml | HTTP 400 — Unsupported content-type (XML) |
| Phys.org rss-feed | HTTP 400 — Unsupported content-type (XML) |
| NASA news-release/feed | HTTP 400 — Unsupported content-type (RSS/XML) |
| ESA Space Science RSS | HTTP 404 — Not Found |
| Nature nature.rss | HTTP 400 — Unsupported content-type (RSS/XML) |
| EurekAlert news.xml | URL not accessible via the web tool |
| Agencia SINC /rss | URL not accessible via the web tool |
| UNAM Global /feed | HTTP 400 — Unsupported content-type (RSS/XML) |
| Google Trends RSS México | URL not accessible via the web tool |

La página HTML de Google Trends sí fue consultable: https://trends.google.com/trending?geo=MX. En el corte de las últimas 24 horas aparece “eclipse solar del 2 de agosto de 2027” (2K+, 13 h) y “bienestar de los animales” (10K+, 21 h). Son señales de interés, no fuentes de afirmaciones científicas.

### Cinco candidatos priorizados para el siguiente slot realmente libre

1. **Hera / Dimorphos — 25-nov.** Fuente primaria: ESA, https://www.esa.int/articles/about-us/directorates/operations/space-safety/hera/hera-reveals-stadium-sized-asteroid-crater-left-after-spacecraft-impact. Observación: la ESA publicó las primeras imágenes del estado de Dimorphos tras el impacto DART y describe el cráter como de escala comparable al cuerpo. No añadir medidas propias ni afirmar que la caracterización está cerrada. Recomendación: candidato visual y muy reciente.
2. **Dragonfly — 24-nov.** Fuente primaria de misión: NASA, https://science.nasa.gov/missions/dragonfly/nasas-titan-bound-dragonfly-rotorcraft-gets-its-eyes/. Observación: NASA informa de siete cámaras integradas en el rotorcraft. Límite: no confundirlas con las cámaras de navegación adicionales ni presentar las pruebas terrestres como imágenes de Titán. Recomendación: candidato visual.
3. **Comunicación gravitatoria — 20-nov.** Fuente primaria: Science Advances, “Unblockable communication with gravity”, DOI 10.1126/sciadv.aee0802; registro bibliográfico PubMed: https://pubmed.ncbi.nlm.nih.gov/43050522/. Observación: demostración de transmisión a través de un muro de ladrillo de 0.7 m a 1 bit/min. Límite: prueba de laboratorio extremadamente lenta, no una tecnología práctica de comunicación. Recomendación: mejor gancho contraintuitivo, siempre con la tasa y la distancia en contexto.
4. **Guías electrónicas 1D en MoS2 — 21-nov.** Fuente primaria: Nature Communications, “Localized strain-engineered 1D electron guides in 2D MoS2 devices with synaptic memory and high-mobility transistor functionalities”, DOI 10.1038/s41467-026-79577-4; https://www.nature.com/articles/s41467-026-79577-4. Observación: ingeniería de deformación localizada para crear guías electrónicas unidimensionales en dispositivos de MoS2. Límite: resultado de dispositivo/material, no producto comercial. Recomendación: candidato técnico de reserva si se logra explicar sin inflar su madurez.
5. **Organización de cromatina — 20-nov.** Fuente primaria: Nature Communications, “A genome-wide imaging screen reveals epigenetic and mechanistic partitioning of lamina-associated chromatin”, DOI 10.1038/s41467-026-79468-8; https://www.nature.com/articles/s41467-026-79468-8. Observación: cribado de más de cien genes y papel de hnRNPK en el posicionamiento de una fracción cercana a dos tercios de las regiones estudiadas. Límite: no extrapolar directamente el sistema celular a enfermedad humana. Recomendación: científicamente sólido, pero exige explicación visual cuidadosa.

**Reserva no contada entre los cinco:** “Nanofriction strengthened mechanically adaptive electrolytes for safe lithium metal batteries”, Nature Communications, DOI 10.1038/s41467-026-78955-2. La verificación Crossref OK de la lectura anterior permanece en el radar; no se prioriza por ser más técnico que Hera/Dragonfly.

### DOI y Crossref

Los registros de PubMed y las páginas editoriales muestran título, fecha y DOI de los artículos anteriores. En esta relectura, el endpoint REST de Crossref y el resolvedor doi.org no fueron accesibles mediante el lector web; por tanto, no se declara una nueva verificación Crossref para el DOI de MoS2. Se conserva como histórica la verificación Crossref OK de los tres DOI ya comprobados en el radar original (gravedad, nanofriction y cromatina). Para MoS2: PENDING_CROSSREF_RECHECK antes de usarlo en un storyboard.

### Decisión de producción corregida

El slot fijo 23:30 del 26-nov no está libre: main contiene el expediente main-only 2026-11-23_dato-thanksgiving-washington con publishAt_utc=2026-11-27T05:30:00Z y render previo. Además, los snapshots conservan ocupación en 07:00 y 13:30, y una colisión de dos IDs en 17:00. El horario vigente no autoriza 19:00. No se crea storyboard ni se marca candidato como seleccionado; los cinco quedan como radar para el siguiente slot que se confirme libre.


### Relectura adicional de feeds y Trends — 2026-11-26 06:37 CDMX

Se intentó consumir de nuevo cada URL configurada en `scripts/tendencias.py`. Los errores siguientes pertenecen al lector utilizado en esta pasada; no prueban por sí solos que el servidor de origen esté caído:

| Feed | Resultado exacto |
|---|---|
| ScienceDaily ciencia, salud y espacio | HTTP 400 — Unsupported content-type: application/xml |
| Phys.org | HTTP 400 — Unsupported content-type: text/xml |
| NASA news-release | HTTP 400 — Unsupported content-type: application/rss+xml |
| ESA Space Science | HTTP 404 — Not Found |
| Nature nature.rss | HTTP 400 — Unsupported content-type: application/rss+xml |
| EurekAlert | URL not accessible via this tool |
| SINC | URL not accessible via this tool |
| UNAM Global | HTTP 400 — Unsupported content-type: application/rss+xml |
| Google Trends RSS México | URL not accessible via this tool |

Se probó además una descarga directa de ScienceDaily mediante el contenedor: `ERROR: download failed` (sin cuerpo HTTP ni código de respuesta disponible). No se atribuye una caída general de los feeds a ese error.

**Respaldo oficial de Trends:** la página HTML [Google Trends — Trending Now, México](https://trends.google.com/trending?geo=MX) sí abrió. El corte mostraba 248 tendencias en las últimas 24 horas; los primeros resultados estaban dominados por fútbol, entretenimiento y conversación general. Señales científicas/naturales potenciales: “eclipse solar del 2 de agosto de 2027” (2K+, 14 h) y “bienestar de los animales” (10K+, 22 h). Son señales de interés, no fuentes de afirmaciones ni candidatos seleccionados.

Los cinco candidatos documentados arriba permanecen como radar. No se añadió ni seleccionó otro: el slot 23:30 sigue ocupado en `main` y no hay otro slot libre autorizado tras la conciliación horaria. No se creó storyboard.


### Aclaración de horario — 2026-11-26

La presencia de un registro a las 13:30 en el snapshot histórico no lo convierte en ventana vigente. La política de `main/data/horarios.json` fechada 23-nov solo mantiene 06:30–07:30 y 16:30–18:00, más 23:30 fijo. Por tanto, 13:30 se conserva como **registro legado/ocupación histórica**, no como slot activo para nuevas asignaciones. 07:00 sigue dentro de ventana activa y ocupado; 17:00 conserva la colisión; 23:30 está ocupado; 19:00 no está autorizado.


### Relectura adicional de respaldo — 2026-11-26 08:27 CDMX

Se repitió la consulta de las fuentes configuradas en `scripts/tendencias.py`. Los errores del lector no cambiaron: ScienceDaily (ciencia, salud y espacio), Phys.org, NASA, Nature y UNAM devuelven `HTTP 400 — Unsupported content-type` para XML/RSS; ESA Space Science devuelve `HTTP 404 — Not Found`; EurekAlert, SINC y Google Trends RSS siguen como `URL not accessible via the web tool`. Esto no demuestra que los servidores de origen estén caídos.

**Respaldo oficial de Google Trends:** la página HTML México abrió con 259 tendencias en las últimas 24 horas. La señal científica/natural visible fue “eclipse solar del 2 de agosto de 2027” (5K+, 15 h). Se conserva solo como señal de interés; no es fuente científica ni candidato por sí misma.

**Dos fuentes primarias nuevas para reserva, sin ampliar el top-5 activo:**

- **Batería de estado sólido a baja presión — 25-nov.** Nature Communications, “Low-pressure operation of all-solid-state batteries enabled by an organic electrode”, DOI [10.1038/s41467-026-79379-8](https://www.nature.com/articles/s41467-026-79379-8). La página editorial informa operación a 1 MPa y 80.3% de capacidad tras 100 ciclos a 0.5C; es un resultado de celda experimental, no una prestación comercial. DOI visible en la página editorial; Crossref REST y doi.org no fueron accesibles en esta relectura: `PENDING_CROSSREF_RECHECK`.

- **Microscopía MINSTED 3D — 24-nov.** Nature Communications, “3D-MINSTED nanoscopy and protein tracking in densely labelled living cells”, DOI [10.1038/s41467-026-79580-9](https://www.nature.com/articles/s41467-026-79580-9). La página editorial informa precisión de localización subnanométrica y seguimiento de pasos de kinesina de 16 nm. DOI visible en la página editorial; Crossref REST y doi.org no fueron accesibles en esta relectura: `PENDING_CROSSREF_RECHECK`.

Ambos quedan como `PROPUESTA_RESERVA`, no seleccionados. No sustituyen todavía a los cinco candidatos priorizados ni habilitan storyboard: falta la compuerta independiente de Crossref/resolvedor y no existe slot autorizado libre el 26-nov. La verificación Crossref anterior de gravedad, nanofriction y cromatina se conserva como antecedente histórico, no como revalidación de hoy.


## Revalidación de señales — 26-nov-2026, 09:39 CDMX

La página oficial de Google Trends México volvió a responder por HTML: 262 tendencias visibles. Predominan fútbol y entretenimiento; «eclipse solar» aparece como señal secundaria (≈5 mil búsquedas, tendencia de ≈16 h). No se selecciona un tema editorial a partir de esa señal.

La lectura directa de RSS no fue consumible desde el navegador en este run; se conserva el error del lector registrado en la corrida anterior y se usa la página HTML oficial como respaldo de Trends. Se cribaron titulares nuevos del 25–26-nov contra la fecha de publicación del estudio primario, no contra la fecha de republicación de la noticia:

- Cuevas bajo Australia — DOI https://doi.org/10.1038/s43247-026-04016-7; el estudio original figura publicado el 17-sep-2026, fuera de la ventana móvil de siete días.
- Lagos de salmuera del mar Rojo — DOI https://doi.org/10.1038/s43247-022-00482-x; estudio de 2022, republicación no elegible.
- Campos hidrotermales del Índico — DOI https://doi.org/10.1038/s41598-026-80304-8; publicación 18-nov-2026, ocho días antes del corte.
- Ensayo de reemplazo robótico de rodilla — DOI https://doi.org/10.1016/S0140-6736(26)00986-4; estudio publicado el 5-sep-2026.
- Micotoxinas en alimentos vegetales — DOI https://doi.org/10.1016/j.foodcont.2025.111910; publicación primaria anterior al periodo.
- Soledad y medicalización — DOI https://doi.org/10.1093/socpro/spag034; publicación primaria anterior al periodo y fuera del alcance temático de esta serie.

Ninguno de esos titulares añade un estudio primario elegible a la ventana de siete días. Se conserva el conjunto de cinco candidatos ya documentado en este radar; no se añade un sexto, no se selecciona candidato y no se crea storyboard porque la conciliación de parrilla del mismo día no deja slot libre.


### Nota de integridad — DOI de titulares excluidos

Los DOI de la lista de exclusiones se identificaron por búsqueda, pero Crossref REST y el resolvedor DOI no fueron accesibles en esta relectura. Por tanto, no se etiquetan como `DOI_VERIFIED`; las fechas asociadas son indicios bibliográficos y no una verificación Crossref de este run. Esos titulares permanecen excluidos y no se usaron para guion ni para seleccionar un candidato. Las dos reservas ya documentadas conservan `PENDING_CROSSREF_RECHECK`.


---

## Revalidación 2026-11-26 · 11:58 CDMX

### Tendencias y feeds

Se revisaron los feeds definidos en `scripts/tendencias.py`: ScienceDaily (science, health, space), Phys.org, NASA, ESA Space Science, Nature RSS, EurekAlert, Agencia SINC y UNAM Global, además de Google Trends RSS México. La lectura directa de los feeds no devolvió cuerpo utilizable ni código HTTP/exception visible en esta sesión; no se simula una ejecución de `scripts/tendencias.py`.

Respaldo oficial: Google Trends Trending Now México sí mostró señales del día, entre ellas **Día de Acción de Gracias 2026** (20K+), **eclipse solar del 2 de agosto de 2027** (10K+) y **mar** (2K+). El trend de Thanksgiving coincide con un paquete preexistente en el slot 23:30 del 26-nov; no se reutiliza ese tema.

### Candidatos primarios recientes

| Prioridad | Hallazgo | Fuente primaria y fecha | Observación verificable | Límite que debe conservarse |
|---|---|---|---|---|
| 1 | Rescate de registros intermareales de los años cincuenta | *Scientific Data*, 26-nov-2026. DOI 10.1038/s41597-026-08947-w. https://www.nature.com/articles/s41597-026-08947-w | Cuatro publicaciones históricas; 6,925 registros en 272 localidades de Francia, España, Portugal y Marruecos; datos de presencia/ausencia. | No es un inventario completo ni contiene abundancias comparables; no atribuye cambios al clima. |

| 2 | Dos linajes arcaicos en el sur de China | *Nature*, 25-nov-2026. DOI 10.1038/s41586-026-11341-6. https://www.nature.com/articles/s41586-026-11341-6 | Evidencia proteómica en cuatro dientes; uno muestra afinidad denisovana y otro permanece como Homo arcaico no resuelto. | Muestra pequeña; no declarar una nueva especie ni convertir afinidad proteómica en genoma completo. |
| 3 | Mapa unicelular de variantes reguladoras de enfermedad coronaria | *Nature*, 25-nov-2026. DOI 10.1038/s41586-026-11275-z. https://www.nature.com/articles/s41586-026-11275-z | Mapa de cromatina accesible y enlaces variante-potenciador-gen en tejido coronario humano. | Mapa molecular; no es predicción clínica ni demuestra que cada variante cause enfermedad. |
| 4 | Clasificador de variantes SARS-CoV-2 por secuencia de espícula | *Scientific Reports*, 26-nov-2026. DOI 10.1038/s41598-026-80097-w. https://www.nature.com/articles/s41598-026-80097-w | Trabajo computacional de clasificación con alta exactitud reportada en el conjunto evaluado. | Versión de acceso anticipado; no presentar exactitud interna como desempeño clínico o validación externa. |

**Verificación DOI:** los DOI aparecen en las páginas editoriales primarias, pero las consultas directas a Crossref y `doi.org` no devolvieron respuesta utilizable desde esta sesión. Los cinco candidatos permanecen con `verification_status=PENDIENTE` hasta ejecutar el validador con `--check-doi`; no se afirma verificación Crossref.

### Rotación y slots

- **26-nov 23:30:** ocupado en `main` por `2026-11-23_dato-thanksgiving-washington`; no duplicar.
- **27-nov 23:30:** libre en `main` y en la rama de trabajo al corte de esta revisión. En `data/rehechos_2026-11-22.json` hay publicaciones a las 10:00 y 15:00, pero ninguna a las 23:30; el límite de cinco piezas/día no se rebasa.
- Estilo elegido para el borrador: `atlas_antiguo`, no aparece en el registro de estilos usados y no está asignado a los proyectos recientes revisados.

### Borrador creado

`proyectos/2026-11-27_dato-registros-intermareales-1950s/storyboard.json`

- 174 palabras; 8 escenas; 78 s de escenas + 6 s de cortinilla = 84 s.
- Mapa con dos bounding boxes publicados por GBIF (costa atlántica francesa y norte ibérico); no se dibujan estaciones puntuales ni se inventa el límite del tercer dataset.
- `approved_assets=[]`; `export.render_status=NOT_GENERATED`; `publicacion.status=PENDIENTE_DECISION_GROK`.
- No se creó `narrative_qa`, `ESTADO_EJECUCION.md), `fuentes.md), cola ni medios. El DOI/Crossref sigue pendiente; el borrador no es apto para promoción.


### Corrección de verificación de candidatos · 12:06 CDMX

Se retiró el candidato provisional de control de unidades motoras: el DOI citado no resolvió a esa publicación y no se encontró una página primaria coincidente. No usarlo. Permanecen cuatro candidatos con páginas editoriales primarias localizadas (biodiversidad intermareal, Denisovanos, mapa unicelular de enfermedad coronaria y clasificador SARS-CoV-2). La selección para el borrador 27-nov sigue siendo el rescate de registros intermareales.

Corrección cronológica del borrador: las cuatro publicaciones francesas fueron publicadas entre 1956 y 1963 y describen observaciones de 1949–1957. El método incluyó digitalización/OCR, corrección, traducción y cotejo con los originales. El guion se actualizó a 174 palabras. El DOI de la fuente primaria aparece en Nature; la compuerta Crossref/doi.org sigue pendiente y bloquea promoción.


---

## Actualización de radar — 2026-11-26, 13:56 CDMX

### Consulta de feeds y respaldo Trends

Se consultaron los endpoints definidos en `scripts/tendencias.py` mediante recuperación web. El script Python no se ejecutó en esta sesión; estos resultados acreditan consulta de endpoints, no ejecución local del script.

| Fuente | Resultado | Observación |
|---|---|---|
| ScienceDaily `science.xml`, `health.xml`, `space_time.xml` | RECUPERADO | Se contrastó la fecha del estudio primario antes de aceptar candidatos |
| Phys.org RSS | RECUPERADO | Radar secundario, no fuente primaria |
| NASA News Release RSS | RECUPERADO | Último elemento observado: 2026-09-01; fuera de ventana |
| UNAM Global RSS | RECUPERADO | Último elemento observado: 2026-05-18; fuera de ventana |
| ESA Space Science RSS | `CRAWL_NOT_FOUND` | Búsqueda oficial como respaldo |
| EurekAlert RSS | `CRAWL_NOT_FOUND` | Búsqueda de fuente primaria como respaldo |
| Agencia SINC RSS | `CRAWL_NOT_FOUND` | Sin candidato respaldado por ese feed |
| Nature RSS | `CRAWL_UNEXPECTED_CONTENT_TYPE` | No se pudo procesar el RSS |
| Google Trends RSS México | `CRAWL_UNEXPECTED_CONTENT_TYPE` | Se usó la página oficial Trending Now como respaldo |

La página oficial de Google Trends México devolvió 25 tendencias en la consulta del 2026-11-25 a las 20:49; en ese primer bloque no apareció una tendencia de ciencia, naturaleza o espacio que justificara un dato CAPCOT. Trends no se usó como evidencia científica.

### Candidatos primarios vigentes

Se conservan cuatro candidatos dentro de la ventana 2026-11-20 a 2026-11-26. Los cuatro DOI devolvieron `status=ok` en Crossref:

1. **Biodiversidad intermareal histórica** — 2026-11-26 — `10.1038/s41597-026-08947-w`. Fuente primaria: *Scientific Data*; 6,925 registros y 272 localidades.
2. **Denisovanos** — 2026-11-25 — `10.1038/s41586-026-11341-6`. Fuente primaria: *Nature*.
3. **Mapa unicelular de enfermedad coronaria** — 2026-11-25 — `10.1038/s41586-026-11275-z`. Fuente primaria: *Nature*.
4. **Clasificación computacional de variantes SARS-CoV-2** — 2026-11-26 — `10.1038/s41598-026-80097-w`. Fuente primaria: *Scientific Reports*; tratar como clasificación computacional, no como validación clínica.

Se excluyeron tres resultados que aparecían como novedades en feeds, pero cuyo trabajo primario quedaba fuera de los siete días: fósil de *Westlothiana* (estudio primario del 2026-09-30), piscinas de salmuera del mar Rojo (estudio primario del 2026-09-02) y cometa detectado por Euclid (publicación primaria del 2026-10-19). La fecha de una noticia o reemisión no sustituye la fecha de publicación del estudio.

### Estado del storyboard intermareal del 27-nov

El storyboard se actualizó y leyó de vuelta en el commit `01f0815756ddbd8d2a7d408199b5e5925a28d6bb`:

- SRC-001: Crossref `status=ok`.
- SRC-002, SRC-003 y SRC-004: DOI resuelto a los datasets GBIF; se corrigieron sus fechas de creación y se conservó la fecha de modificación 2026-11-02.
- 8 escenas, 173 palabras de narración, 78 segundos de escenas + 6 segundos de cortinilla = 84 segundos.
- Voz y prompt base coinciden con el contrato y catálogo.
- El mapa contiene dos bounding boxes de datasets GBIF y una tarjeta de datos de 6,925 registros / 272 localidades. No representa estaciones puntuales ni la cobertura completa de los cuatro países.
- `approved_assets=[]`, `render_status=NOT_GENERATED`, sin rutas ni medios.

La verificación de DOI fue manual por Crossref/resolvedor; no se ejecutó `scripts/validar_storyboard.py --check-doi`. Tampoco se ejecutó el validador estructural Python. `narrative_qa` quedó `FAIL/0` con `REVISION_INDEPENDIENTE_AUSENTE`: no hubo una lectura ciega separada de solo la narración. No hay PASS ni autorización de promoción.
