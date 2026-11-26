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
