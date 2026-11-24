# Radar CAPCOT — 23 de noviembre de 2026

**Corte:** 23-nov-2026, 00:27 CDMX  
**Rama de trabajo:** `feature/capcot-video-discovery-continuity`  
**Estado:** investigación y borrador textual en `proyectos/`; sin medios, sin promoción, sin programación y sin publicación.

## Decisión de slot

| Fecha | Slot CDMX | Evidencia consultada | Decisión |
|---|---:|---|---|
| 23-nov | 07:00 | `data/miniaturas_auditoria_2026-11-21.json`: `IQEU2Bqy3v0` y `tmOji99zGPE` comparten `publishAt=2026-11-23T13:00:00Z` | COLISION_PUBLISHAT; no tocar |
| 23-nov | 13:30 | Feature: `2026-11-23_tropical-biodiversity-turnover`; main: Rosetta `p5PM4xZfDyc` en `data/miniaturas_auditoria_2026-11-21.json` | CONFLICTO_DE_SLOT_ENTRE_RAMAS; no promover |
| 23-nov | 23:30 | Main sin ocupación en el snapshot disponible; feature asignado a `2026-11-23_supersequias-722-eventos/storyboard.json` | OCUPADO_EN_FEATURE; no redispatch; Studio externo no verificado |

El snapshot de programación de main en `data/miniaturas_auditoria_2026-11-21.json` confirma 07:00 (dos IDs con el mismo `publishAt`), Rosetta a 13:30 (`p5PM4xZfDyc`), Pirámides a 17:00 (`gWJxoGjWQeM`) y Gutenberg a 19:00 (`i3SpxSQglm4`). Por tanto, el borrador tropical de feature a 13:30 tiene `CONFLICTO_DE_SLOT_ENTRE_RAMAS`. El slot 23:30 no aparece ocupado en main, pero ya está asignado en feature a supersequías. No se verificó Studio externo. No se afirma disponibilidad externa de YouTube Studio.

## Ingesta RSS y Trends

Se leyó `scripts/tendencias.py` para identificar los diez feeds configurados. No se pudo ejecutar el script dentro de esta sesión; se intentó abrir cada feed directamente y se conservan los errores observados:

| Feed | Error observado |
|---|---|
| ScienceDaily science | `400 Unsupported content-type: application/xml` |
| ScienceDaily health | `400 Unsupported content-type: application/xml` |
| ScienceDaily space | `400 Unsupported content-type: application/xml` |
| Phys.org | `400 Unsupported content-type: text/xml` |
| NASA RSS | `400 Unsupported content-type: application/rss+xml` |
| ESA Space Science RSS | `404 Not Found` |
| Nature RSS | `500 Redirected to idp.nature.com/authorize; destino no accesible mediante esta interfaz` |
| EurekAlert | `URL is not accessible via this tool` |
| Agencia SINC | `URL is not accessible via this tool` |
| UNAM Global | `400 Unsupported content-type: application/rss+xml` |
| Google Trends RSS México | `URL is not accessible via this tool` |
| Descarga alternativa de ScienceDaily | `download failed` |

**Respaldo oficial:** la página de Google Trends México abrió y mostró 264 tendencias, con 25 visibles en la primera página. Las búsquedas internas de esa página para NASA, espacio, ciencia, temperatura y superluna no devolvieron coincidencias en el contenido visible. Esto solo describe la primera página, no las 264 tendencias completas. Se usaron páginas editoriales primarias como respaldo; un fallo de RSS no se trató como ausencia de noticias.

## Cinco candidatos recientes

### 1. Supersequías compuestas — SELECCIONADO PARA BORRADOR 23:30

- **Fuente primaria:** Nature Scientific Data, *Event inventory dataset of super drought under global warming*, publicado 23-nov-2026.
- **DOI publicado:** [10.1038/s41597-026-08886-6](https://doi.org/10.1038/s41597-026-08886-6).
- **URL editorial:** https://www.nature.com/articles/s41597-026-08886-6
- **Observación:** el inventario identifica 722 eventos entre 1961 y 2024; duración media reportada de 6.9 meses. La definición exige CMI ≤ −1.8 simultáneamente en ventanas de 3, 6 y 12 meses.
- **Ejemplos cartografiables publicados:** Europa 2003, centroide 47°N, 15°E, mayo–noviembre; suroeste de China 2006, centroide 30°N, 104°E, julio–octubre. Son centroides de validación, no límites de los eventos.
- **Validación:** 139 de 234 registros GDIS coinciden (59.4%); la tasa llega a 71% después de excluir África interior y zonas costeras con limitaciones de datos.
- **Cálculo reproducible:** 139 ÷ 234 = 0.5940, equivalente a 59.4%. El 71% es condicional al subconjunto excluido; no es la tasa global.
- **Inferencia permitida:** el catálogo formaliza eventos que coinciden en tres escalas temporales. No demuestra que cada evento haya sido causado por el calentamiento global.
- **Recomendación editorial:** contar la idea de los «tres relojes» con dos centroides históricos y el límite de validación. Evitar presentar todos los periodos secos como supersequías.
- **Verificación:** la página editorial primaria apareció con título, fecha, DOI y contenido del artículo. La apertura directa de doi.org y el endpoint Crossref no fueron accesibles en esta sesión. El DOI queda `PENDIENTE_RESOLVEDOR`; no promover hasta resolverlo.
- **Borrador creado:** `proyectos/2026-11-23_supersequias-722-eventos/storyboard.json`.
- **Preflight del borrador:** 8 escenas, 220 palabras, 78 s de escenas + 6 s de cortinilla = 84 s, 9:16, voz es-MX-JorgeNeural +7% / −2 Hz, estilo `collage_cientifico_vintage`, mapa con centroides publicados y dos capas de dato.
- **Estado:** `BORRADOR_EN_PROYECTOS_NO_APTO_PARA_PROMOCION`. `narrative_qa` independiente registrado: FAIL 82/100, siete checks true, `critical_flags=[STAKES_NO_EXPLICADOS]`. DOI/resolvedor pendiente; la cifra 139/234 (59.4%) no se confirmó en el texto primario accesible. No hay copia en cola.

### 2. Microbiomas de esponjas de aguas profundas

- **Fuente primaria:** Nature Scientific Data, *Metagenome-assembled genomes and viral sequences from deep-sea sponges*, publicado 23-nov-2026.
- **DOI:** [10.1038/s41597-026-08711-0](https://doi.org/10.1038/s41597-026-08711-0).
- **Observación:** 1,719 genomas ensamblados a partir de 27 metagenomas de 17 especies de esponjas, además de secuencias virales putativas.
- **Límite:** es un descriptor de datos; no demuestra por sí solo infección activa ni interacciones virus-hospedador. El archivo `metagenomes_metadata.xlsx` de Zenodo no pudo descargarse en esta sesión; no se recuperaron coordenadas de muestreo verificables.
- **Decisión:** `PENDING_MAP_COORDINATES`; no crear storyboard ni sustituir sitios de muestreo por afiliaciones de autores.

### 3. Microplásticos dietarios en tilapia

- **Fuente primaria:** Scientific Reports, artículo publicado 23-nov-2026, DOI [10.1038/s41598-026-65376-w](https://doi.org/10.1038/s41598-026-65376-w).
- **Observación:** ensayo de 49 días con juveniles de tilapia y dietas experimentales con 3% y 6% de PVC, además de controles con caolín.
- **Cálculo contextual:** 3% y 6% del peso de la dieta equivalen a 30,000 y 60,000 mg/kg de alimento; son conversiones de las dosis experimentales, no concentraciones ambientales.
- **Límite:** no extrapolar a peces silvestres ni a riesgo humano; algunos efectos también aparecen en grupos con caolín.
- **Decisión:** `NO_DUPLICAR`; el tema de microplásticos en fauna ya se trató en `2026-11-14_dato-microplasticos-pantanal`. No crear storyboard.

### 4. Interacción entre glaciares y lagos proglaciares
- Fuente primaria: Nature Climate Change, DOI `10.1038/s41558-026-02808-5`, publicado el 20-nov-2026.
- URL editorial: https://www.nature.com/articles/s41558-026-02808-5
- Estado: CANDIDATO_PARA_SLOT_FUTURO; falta verificar DOI con Crossref/resolvedor y comprobar coordenadas aptas para el mapa.

### 5. Varroa y la hipoxia de altura

- **Fuente primaria:** PLOS Biology, publicado 19-nov-2026, DOI [10.1371/journal.pbio.3004091](https://doi.org/10.1371/journal.pbio.3004091).
- **Observación:** ensayo en colmenas a distintas altitudes y simulación de baja presión parcial de oxígeno; el estudio reporta menor reproducción del ácaro bajo hipoxia.
- **Límite:** el mecanismo exacto sigue sin resolverse; no es una receta de manejo apícola y no se publicó el 23-nov.
- **Decisión:** candidato para fecha posterior, no para el slot de hoy.

**Filtro adicional:** el artículo de pulsar gamma de Physical Review Letters (DOI 10.1103/vlt2-xzgk) sí resolvió a la página del editor, pero queda `NO_DUPLICAR`: el tema ya aparece en `2026-11-21_pulsar-gamma-reticulo` y en la entrada heredada `2026-11-22_pulsar-criptografia`.

## Auditoría de proyectos actuales y backlog 18–23 nov

- `2026-11-23_tropical-biodiversity-turnover`: `FAIL/82`, flag `STAKES_NO_EXPLICADOS`; 13:30 en feature; sin entrada plana, sin salida y sin archivo individual de estado Grok. Clasificación `NOT_DISPATCHABLE`.
- Main sí registra Rosetta `p5PM4xZfDyc` a 13:30 en `data/miniaturas_auditoria_2026-11-21.json`; el borrador tropical de feature tiene `CONFLICTO_DE_SLOT_ENTRE_RAMAS`.
- `2026-11-22_genes-estatura-etapas` corresponde al 22-nov 23:30; no ocupa el 23-nov 23:30.
- El resto de los storyboards 18–22 nov conserva sus hashes y QA registrados en la rama; no se repitió un PASS válido ni se reescribieron narraciones.

## Lote interdiario de 12 IDs — 5 a 7 de noviembre

Todos los archivos individuales `cola/estado/<project_id>.json` devolvieron 404; además, el directorio `cola/estado/` no existe en la rama. Se registra `RECEPCION_GROK_NO_CONFIRMADA` para los doce. Los slots ya pasaron; no se promueve ninguno.

| Project ID canónico | QA vigente | Evidencia de cola/salida | Decisión |
|---|---:|---|---|
| `2026-11-05_kids-dia-en-venus` | PASS / 88 | Sin entrada ni salida; hay un alias heredado distinto en bloqueados (`inter-venus-dia-largo`) | No reabrir slot pasado |
| `2026-11-05_comida-palomitas` | FAIL / 82 | JSON y carpeta heredados duplicados en bloqueados | Mantener bloqueado; no borrar |
| `2026-11-05_inter-arboles-se-comunican` | FAIL / 78 | Alias heredado `inter-arboles-mito-respiran` en bloqueados | Mantener bloqueado; no renombrar |
| `2026-11-05_inter-rayo-globular` | FAIL / 81 | JSON heredado en bloqueados | Mantener bloqueado |
| `2026-11-06_kids-ballena-azul-corazon` | FAIL / 80 | Alias heredado `inter-corazon-ballena-azul` en bloqueados | Mantener bloqueado; no renombrar |
| `2026-11-06_comida-aguacate-negro` | FAIL / 79 | JSON y carpeta heredados duplicados en bloqueados | Mantener bloqueado; no borrar |
| `2026-11-06_inter-ranas-congeladas` | FAIL / 83 | JSON y carpeta heredados duplicados en bloqueados | Mantener bloqueado; no borrar |
| `2026-11-06_inter-arena-cantante` | PASS / 94 | JSON heredado en bloqueados; sin salida | No reabrir slot pasado |
| `2026-11-07_kids-huesos-bebe` | FAIL / 82 | JSON y carpeta heredados duplicados en bloqueados | Mantener bloqueado; no borrar |
| `2026-11-07_comida-hielo-caliente` | FAIL / 81 | Entrada heredada y salida completa en main, con storyboard, QA y metadatos | `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR` |
| `2026-11-07_inter-pulpo-suenos` | FAIL / 72 | Flag de especie: la fuente corresponde a *Octopus laqueus*, no *O. insularis*; escenas 5–6 repetidas y payoff vago | Mantener fuera de cola |
| `2026-11-07_inter-nubes-pesan` | FAIL / 78 | JSON heredado en bloqueados; alias de carpeta `extra-nubes-pesan` | Mantener bloqueado |

No se modificaron las copias heredadas, no se borraron duplicados y no se repitió QA de narraciones sin cambios. Los dos PASS existentes se conservan como PASS histórico, pero no se promueven por fecha vencida y falta de recepción verificable.

## Cola, handoff y workflow Grok

- `cola/entrada/` en feature contiene `.gitkeep` y una carpeta anidada de 9-nov; no hay JSON plano para los proyectos 18–23 ni para el borrador nuevo.
- `cola/estado/` devuelve 404 como directorio; no hay recibos individuales.
- `handoffs/grok_inbox/` contiene únicamente el marcador heredado de `2026-11-09_dato-robot-ensambla-orbita`; no acredita recepción de Grok.
- `salidas/` no contiene salidas 18–23 nov. La salida heredada de `2026-11-07_comida-hielo-caliente` está en main y no debe redispatcharse.
- `.github/workflows/capcot-grok-dispatch.yml` escucha JSON planos en `cola/entrada/*.json` o ejecución manual; las carpetas anidadas y los borradores en `proyectos/` no disparan el flujo.
- No se ejecutó workflow, no se envió payload y no se creó ni editó ningún estado Grok. La presencia de secretos no pudo comprobarse mediante una herramienta de solo lectura disponible; no se inspeccionaron ni expusieron valores.
- El borrador nuevo queda `NOT_DISPATCHABLE`: vive únicamente en `proyectos/`, carece de narrative QA independiente y mantiene DOI pendiente.

## Historial de YouTube y programación heredada

- `data/cola.json` está vacío.
- `data/vistas_historico.json` conserva como último corte visible el 22-nov-2026, 13:50 CDMX; no hay lectura posterior a la hora de Cleopatra/Oxoboranos en los archivos consultados.
- `data/miniaturas_auditoria_2026-11-21.json` registra la colisión de `publishAt` para 23-nov-2026 07:00 CDMX: `IQEU2Bqy3v0` y `tmOji99zGPE`, ambos `2026-11-23T13:00:00Z`. La referencia anterior a `data/resubidas_2026-11-21.md` era incorrecta. No se cambió ni canceló ninguno.
- `data/cierre_diario/2026-11-22.md` y `data/tt_fb_alineacion_2026-11-22.json` conservan registros de Cleopatra, Oxoboranos, Gutenberg y Ada; el estado posterior a la hora no quedó verificado en YouTube Studio dentro de esta sesión.
- No se afirma publicación ni fallo a partir de un `publishAt` pasado. No se cambió privacidad, programación ni etiquetas.

## CI y Actions

- En main, el run `45117327158` de Semgrep falló con 34 findings sobre 1,103 archivos; Gitleaks pasó y el flujo de push terminó. No se obtuvo un SARIF utilizable para revisar reglas individuales.
- No hay ejecución reciente de `capcot-grok-dispatch`; los commits de este trabajo usan `[skip ci]`.
- `capcot-descubrimiento.yml` es un flujo semanal de descubrimiento de generadores de video (lunes 14:30 UTC), no el ingestor científico de RSS; no se ejecutó manualmente.

## Resultado material de este run

- **Creado y leído de vuelta:** `proyectos/2026-11-23_supersequias-722-eventos/storyboard.json`.
- **Preflight verificado:** 220 palabras, 8 escenas, 84 s totales, 9:16, voz configurada, mapa con centroides publicados, capas de dato, `approved_assets=[]`, `export.render_status=NOT_GENERATED`, `publicacion.status=PENDIENTE_DECISION_GROK`.
- **No creado:** `ESTADO_EJECUCION.md`, entrada de cola, estado Grok, medios o archivos de publicación. `narrative_qa` sí se registró como FAIL 82/100.
- **No modificados:** `data/*.json`, main, bloqueados heredados, permisos, secretos y programación.
- **Siguiente compuerta mínima:** resolver DOI por Crossref/resolvedor, verificar la cifra 139/234 en la fuente primaria y ejecutar el validador estructural real. La revisión narrativa ya quedó registrada como FAIL; no repetirla mientras la narración no cambie. No se autoriza despacho en este estado.

## Correcciones y verificaciones del run — 2026-11-23 00:57 CDMX

- **Inventario de slots:** 07:00 colisiona entre `IQEU2Bqy3v0` y `tmOji99zGPE` según `data/miniaturas_auditoria_2026-11-21.json`; la referencia anterior a `data/resubidas_2026-11-21.md` era incorrecta. 13:30 está ocupado por Rosetta en main y por el borrador tropical en feature: `CONFLICTO_DE_SLOT_ENTRE_RAMAS`. Main también registra Pirámides 17:00 y Gutenberg 19:00. 23:30 no aparece ocupado en el snapshot de main y queda asignado en feature al borrador de supersequías.
- **QA supersequías:** FAIL 82, `STAKES_NO_EXPLICADOS`; la narración no se reescribió. DOI editorial `10.1038/s41597-026-08886-6` aparece en Nature, pero Crossref/resolvedor no pudo verificarse por DNS. La cifra 139/234 (59.4%) no aparece en el texto primario accesible y queda `PENDING_SOURCE`.
- **RSS/Trends:** se ejecutó el contenido vigente de `scripts/tendencias.py` en runtime temporal. Los diez feeds (ScienceDaily general/salud/espacio, Phys.org, NASA, ESA, Nature, EurekAlert, SINC y UNAM Global) y Google Trends RSS México fallaron con `<urlopen error [Errno -3] Temporary failure in name resolution>`. No se escribió ningún JSON. Respaldo oficial consultado: Nature Scientific Data, Nature Climate Change, Scientific Reports y PLOS Biology.
- **Candidato corregido:** se sustituyó el lead de W2246-0526, cuyo DOI `10.1126/sciadv.aek9035` no pudo localizarse en fuente primaria, por el artículo de glaciares-lagos de Nature Climate Change. W2246 queda `PENDING_SOURCE`, fuera de los cinco candidatos.
- **Promoción:** no se creó entrada de cola. Supersequías no supera QA ni DOI; tropical no supera QA y además tiene conflicto de slot. No se ejecutó workflow ni se envió payload.


## Relectura de fuentes — 23-nov-2026, 06:23 CDMX

Se reintentó la lectura directa de los diez feeds configurados y Google Trends RSS México. Los errores observados en esta relectura fueron:

| Feed | Resultado de esta relectura |
|---|---|
| ScienceDaily science | `400 Unsupported content-type: application/xml` |
| ScienceDaily health | `400 Unsupported content-type: application/xml` |
| ScienceDaily space | `400 Unsupported content-type: application/xml` |
| Phys.org | `400 Unsupported content-type: text/xml` |
| NASA RSS | `400 Unsupported content-type: application/rss+xml` |
| ESA Space Science RSS | `404 Not Found` |
| Nature RSS | `400 Unsupported content-type: application/rss+xml` |
| EurekAlert | `URL is not accessible via this tool` |
| Agencia SINC | `URL is not accessible via this tool` |
| UNAM Global | `400 Unsupported content-type: application/rss+xml` |
| Google Trends RSS México | `URL is not accessible via this tool` |

La página HTML oficial de Google Trends México sí abrió: **274 tendencias** en las últimas 24 horas y 25 visibles en la primera página. Los términos visibles estuvieron dominados por fútbol, NFL, entretenimiento, clima y búsquedas generales; no apareció un tema científico/natural utilizable en esa primera página. No se extrapola esa observación a las 274 tendencias completas.

Se reabrieron fuentes editoriales primarias para respaldar los candidatos ya listados, sin asignarles un slot nuevo:

- PLOS Biology, *Altitude-induced hypoxia suppresses Varroa mite reproduction in Tibetan honey bees*, publicado 19-nov-2026; DOI visible en la página primaria: `10.1371/journal.pbio.3004091`.
- Nature Astronomy, *The nature of the Norma arm as a bar-driven star-forming shock front*, publicado 20-nov-2026; DOI visible: `10.1038/s41550-026-03010-5`.
- Nature Communications, *Plankton ecological complexity amplifies climate-driven weakening of the ocean biological pump*, publicado 21-nov-2026; DOI visible: `10.1038/s41467-026-79817-7`.
- Nature Climate Change, *Climate and glacier geometry dominate global glacier–lake interactions*, publicado 20-nov-2026; DOI visible: `10.1038/s41558-026-02808-5`.

El endpoint de Crossref y los resolutores `doi.org` no fueron accesibles en esta relectura; los cuatro DOI quedan `PENDIENTE_RESOLVEDOR` aunque la página primaria muestre el identificador. No se promovió ni se marcó un DOI como verificado por Crossref. El quinto candidato de esta fecha permanece `PENDING_MAP_COORDINATES`. No se creó otro storyboard: la parrilla registrada del 23 al 29-nov no ofrece un slot libre confirmado.


## Corrección de ocupación de main — 23-nov-2026, 07:58 CDMX

La tabla inicial de este radar indicaba que el slot 23:30 no aparecía ocupado en main. Esa observación quedó superada por la lectura posterior de main HEAD `20fa76409a620d909d690d3c04a87bb34f4b42c6` y de `data/tt_fb_alineacion_2026-11-23.json` (blob `3d44386a12298ee06b222ccabfaefb65fe61a6e8`): el registro de YouTube incluye Oso Wojtek a las 23:30. Por tanto, **supersequías 23:30 = CONFLICTO_DE_SLOT_ENTRE_RAMAS**, además de su FAIL narrativo y DOI/resolvedor pendiente. No está disponible para promoción.

El mismo registro confirma Rosetta a las 13:30, que mantiene el conflicto con tropical. Main muestra ocho horarios distintos y diez video_id del día frente al límite documentado de cinco; se registra la discrepancia de capacidad sin intervenir en main ni en la programación. Todo procesamiento/ID preexistente bloquea redispatch. No se modificaron `data/*.json`, storyboards, estados Grok ni decisiones editoriales.


## Reintento de fuentes RSS y respaldo oficial — 2026-11-23

Se reintentó la lectura de los endpoints definidos en `scripts/tendencias.py` y Google Trends RSS México. Errores exactos del lector web:

- ScienceDaily ciencia, salud y espacio: `400 Unsupported content-type: application/xml`.
- Phys.org: `400 Unsupported content-type: text/xml`.
- NASA: `400 Unsupported content-type: application/rss+xml`.
- ESA Space Science: `404 Not Found`.
- Nature RSS: `400 Unsupported content-type: application/rss+xml`.
- EurekAlert y Agencia SINC: `URL ... is not accessible via this tool`.
- UNAM Global: `400 Unsupported content-type: application/rss+xml`.
- Google Trends RSS México: `URL https://trends.google.com/trending/rss?geo=MX is not accessible via this tool`.
- Crossref API y `doi.org` para el DOI del candidato de sequías: `URL ... is not accessible via this tool`; el resolvedor sigue sin verificación independiente en este entorno.

**Respaldo oficial disponible:** la página HTML de Google Trends para México sí abrió: últimas 24 horas, **271 tendencias** y 25 visibles en la primera página. Predominan deportes, entretenimiento y búsquedas sociales; “temperatura” y “electrificación” aparecen sin contexto suficiente para formular un dato científico verificable. No se convierten en candidatos CAPCOT por inferencia.

Se conservan los cinco candidatos documentados previamente desde fuentes oficiales/primarias; no se agrega otro sin afirmación primaria fechada. No hay slot libre: 13:30 y 23:30 tienen conflicto entre ramas y el registro de main supera el cupo diario. Resultado de investigación de este corte: **sin storyboard nuevo**; no se inventa una fuente, DOI, coordenada ni decisión editorial.


---

## Addendum de relectura y verificación — 2026-11-23 08:02 CDMX

Este addendum actualiza la evidencia de la misma ejecución sin crear un segundo radar ni reescribir los storyboards existentes. El archivo de radar ya existía en la rama; se conserva su historial y se añade esta lectura incremental.

### 1. RSS y Google Trends

**No se parseó XML en esta ejecución.** Se intentó abrir cada URL configurada en `scripts/tendencias.py`; los errores devueltos fueron:

| Feed | Resultado literal de acceso |
|---|---|
| ScienceDaily — science.xml | `400 Unsupported content-type: application/xml` |
| ScienceDaily — health.xml | `400 Unsupported content-type: application/xml` |
| ScienceDaily — space_time.xml | `400 Unsupported content-type: application/xml` |
| Phys.org | `400 Unsupported content-type: text/xml` |
| NASA News Release | `400 Unsupported content-type: application/rss+xml` |
| ESA Space Science | `404 Not Found` |
| Nature RSS | `400 Unsupported content-type: application/rss+xml` |
| EurekAlert | `URL is not accessible via this tool` |
| SINC | `URL is not accessible via this tool` |
| UNAM Global | `400 Unsupported content-type: application/rss+xml` |
| Google Trends RSS México | `URL is not accessible via this tool` |

Estos errores describen el acceso desde la herramienta de lectura; no demuestran por sí solos que los servidores RSS estén caídos.

**Fallback oficial:** [Google Trends — Trending Now México](https://trends.google.com/trending?geo=MX), ventana «Past 24 hours». Dos lecturas de la página durante esta ejecución mostraron 280 y después 269 tendencias; el contador es dinámico. La segunda lectura mostraba 1–25 de 269. La primera página estaba dominada por deporte, entretenimiento y consultas meteorológicas; «electrificación» aparecía con 1K+ búsquedas y +200%, pero sin noticia científica primaria asociada. La búsqueda de texto en esa página no encontró «ciencia», «NASA» ni «espacio». No se infiere que las 269 tendencias carezcan de temas científicos: solo se afirma que no apareció uno verificable en el contenido visible de la primera página.

### 2. Actualización de los cinco candidatos

Los DOI que aparecen en las páginas editoriales no se marcan como verificados por Crossref/resolvedor. Se intentaron las rutas directas `doi.org`, `api.crossref.org` y `search.crossref.org`; el resolvedor no fue accesible desde esta herramienta y la API de Crossref devolvió «URL is not accessible via this tool». Por tanto, el estado de resolución sigue pendiente en los cinco casos.

1. **Supersequías — candidato ya desarrollado, no duplicar.** *Scientific Data*, publicado el 23-11-2026. La página primaria confirma 722 eventos para 1961–2024, definidos con CMI ≤ −1.8 simultáneamente en escalas de 3, 6 y 12 meses; duración media de 6.9 meses. La validación GDIS compara 234 eventos físicos con 139 coincidencias (59.4%); el 71% solo corresponde al subconjunto de regiones interiores no africanas. Los 95 no coincidentes se concentran en África interior y zonas costeras, donde el artículo describe diferencias de vulnerabilidad y limitaciones del dato climático. No presentar 71% como tasa global ni equiparar sequía física con desastre socioeconómico. DOI visible en la página editorial: `10.1038/s41597-026-08886-6`; **PENDING_RESOLVEDOR**. Fuente primaria: https://www.nature.com/articles/s41597-026-08886-6

2. **Microbiomas de esponjas profundas.** *Scientific Data*, publicado el 23-11-2026. La ficha primaria accesible en el índice editorial informa 1,719 genomas ensamblados desde metagenomas, 27 metagenomas y 17 especies. El descriptor abre un recurso genómico para estudiar capacidad funcional y posibles interacciones virus-hospedador; no demuestra por sí mismo fijación de carbono activa ni infección viral. DOI mostrado por la página editorial: `10.1038/s41597-026-08711-0`; **PENDING_RESOLVEDOR**. La apertura directa de la página fue redirigida a autenticación de Nature; falta comprobar el texto completo y la geometría de muestreo antes de considerar un mapa. Fuente primaria: https://www.nature.com/articles/s41597-026-08711-0

3. **Microplásticos dietarios en tilapia.** *Scientific Reports*, publicado el 23-11-2026. El artículo primario describe un ensayo controlado de 49 días con dietas control, 3% y 6% de caolín, y 3% y 6% de PVC; informa diferencias en crecimiento, conducta alimentaria e histología. No equivale a exposición ambiental real ni permite extrapolar directamente a salud humana o poblaciones silvestres. Además, el tema se solapa con el proyecto del 14-11-2026 sobre microplásticos del Pantanal: **NO_DUPLICAR** salvo novedad editorial distinta y justificada. DOI visible: `10.1038/s41598-026-65376-w`; **PENDING_RESOLVEDOR**. Fuente primaria: https://www.nature.com/articles/s41598-026-65376-w

4. **Interacción global entre glaciares y lagos.** *Nature Climate Change*, publicado el 20-11-2026. El resumen editorial informa, para 2000–2020, 3,567 lagos en contacto con hielo adicionales (+35%), +604 ± 22 km² de área (+9%) y +66 ± 5 km³ de volumen (+12%). En el análisis de pérdida de masa, el aporte de lagos se estima en 11 ± 7%, frente a 43 ± 10% de forzamiento climático y 46 ± 10% de geometría glaciar. No atribuir toda la pérdida a los lagos. La fuente organiza el análisis en 18 regiones RGI; la apertura directa del artículo fue redirigida a autenticación, así que faltan texto completo y geometrías cartográficas utilizables. DOI consignado por el radar: `10.1038/s41558-026-02808-5`; **PENDING_RESOLVEDOR / PENDING_FULLTEXT_ACCESS**. Fuente primaria: https://www.nature.com/articles/s41558-026-02808-5

5. **Hipoxia y reproducción del ácaro Varroa.** *PLOS Biology*, publicado el 19-11-2026. El artículo primario informa experimentos de traslado entre cuatro altitudes; las condiciones hipóxicas por encima de 3,500 m redujeron la fecundidad del ácaro y detuvieron el desarrollo de parte de su descendencia. En una prueba controlada a 88 m, las colmenas hipóxicas alcanzaron aproximadamente 13.5 kPa de presión parcial de oxígeno frente a 20.4 kPa en controles; tras 11 días, el promedio fue 1.7 descendientes frente a 3.9 en controles. Los autores señalan que la base fisiológica requiere investigación adicional: no convertir el resultado en recomendación apícola inmediata. DOI visible: `10.1371/journal.pbio.3004091`; **PENDING_RESOLVEDOR**. Fuente primaria: https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3004091

**Recomendación editorial actualizada:** conservar supersequías como el proyecto ya abierto, sin reescribirlo durante la auditoría. Para el siguiente slot realmente libre, Varroa ofrece el mecanismo más narrable con texto primario completo, condicionado a resolver DOI y verificar coordenadas de los sitios en material suplementario. Glaciares-lagos queda como segunda opción, condicionada a recuperar el artículo completo y geometrías publicadas. Es una recomendación de investigación, no selección editorial de Grok.

### 3. Guardia de ocupación por slot: feature y main

`data/horario_2026-11-23.json` no existe. El contrato operativo §3 conserva los cinco slots autorizados; `data/horarios.json` (actualizado el 09-11) distingue ventanas activas 06:30–07:30 y 16:30–18:00, más 23:30 fijo; 13:30 permanece como ventana de prueba y 19:00 aparece retirada. No se inventa un horario diario ausente.

**Feature:** los únicos dos proyectos con fecha objetivo 23-11 son:
- `2026-11-23_tropical-biodiversity-turnover`, `slot_local=13:30`.
- `2026-11-23_supersequias-722-eventos`, `slot_local=23:30`, `slot_cesta=dato_del_dia`.

`data/publicaciones.json`, `data/rotacion.json`, `data/temas_del_dia.json` y `data/cola.json` no contienen registros del 23-11; sus coberturas terminan antes de esta fecha. `salidas/` y `cola/entrada/` no aportan otro paquete de esta fecha. No existe `data/horario_2026-11-23.json`.

**Main — consulta solo de lectura:** se encontraron identificadores y/o evidencia de programación para los cinco slots:
- 07:00: `IQEU2Bqy3v0` y `tmOji99zGPE`.
- 13:30: Rosetta, `p5PM4xZfDyc`.
- 17:00: Pirámides, `gWJxoGjWQeM`, y Mitraísmo, `6OuHVN5dbbs`.
- 19:00: Gutenberg, `i3SpxSQglm4`.
- 23:30: Oso Wojtek, `pTmQgkchC68`.

La evidencia procede de `data/tt_fb_alineacion_2026-11-23.json`, `data/miniaturas_auditoria_2026-11-21.json`, `data/publicaciones.json` y los `programacion.json` existentes. Hay dos elementos listados a las 07:00 y dos a las 17:00 en main; se registra la ocupación, no se intenta resolver ni reprogramar ese posible solapamiento.

**Decisión de duplicación:** 13:30 y 23:30 tienen conflicto entre ramas; 07:00, 17:00 y 19:00 ya muestran evidencia de main. Resultado: `CONFLICTO_DE_SLOT_ENTRE_RAMAS / NO_DUPLICAR`. No se crea storyboard principal nuevo ni segundo storyboard 23:30. La fuente de supersequías sí cumple la fecha del día; la razón para no crear otra versión es la ocupación, no `PENDING_SOURCE`.

No existen `cola/estado/2026-11-23_tropical-biodiversity-turnover.json` ni `cola/estado/2026-11-23_supersequias-722-eventos.json`: `RECEPCION_GROK_NO_CONFIRMADA` para ambos. El marker antiguo de `handoffs/grok_inbox/` no se interpreta como recepción. No se escribió ni modificó ningún estado de Grok.

Los dos storyboards existentes se releen y conservan: ambos tienen `approved_assets=[]`, `export.render_status=NOT_GENERATED`, no tienen `export.filename` ni rutas/keys de assets, y `publicacion.status=PENDIENTE_DECISION_GROK`. Ambos mantienen `narrative_qa.status=FAIL`, score 82, los siete checks true y `critical_flags=["STAKES_NO_EXPLICADOS"]`. No se modificaron ni promovieron.

### 4. Relectura completa de QA preexistente en proyectos/

Se releyeron los 90 archivos `proyectos/*/storyboard.json` presentes en la rama. Resultado: **20 PASS, 27 FAIL, 1 PENDIENTE y 42 PENDIENTE_AUDITOR**. No se interpretó ningún `salidas/qa.json` como `narrative_qa`. En el registro siguiente, `checks` usa exactamente este orden de claves del JSON: `pregunta_central_reconstruible`, `apertura_in_medias_res`, `progresion_por_escena`, `transiciones_causales`, `giro_cientifico_explicado`, `limite_evidencia_explicito`, `payoff_cierre_apertura`. `reviewed_at: null` significa que la propiedad no existe en el JSON fuente; no es una fecha inferida.

```json
{
  "qa_records": [
    {"id":"2026-10-31_murcielagos-viroma-global","status":"FAIL","score":72,"review_basis":"lectura_en_frio_solo_narracion","reviewed_at":null,"checks":[true,false,true,false,false,true,true],"critical_flags":["APERTURA_ESTATICA_Y_ESCENARIO_NO_DOCUMENTADO","TRANSICIONES_GENERICAS","CIFRA_300000_SIN_UNIDAD_DE_ANALISIS","GIRO_COMPARATIVO_NO_EXPLICADO"]},
    {"id":"2026-10-31_sequias-energia-renovable","status":"FAIL","score":56,"review_basis":"lectura_en_frio_solo_narracion","reviewed_at":null,"checks":[true,false,false,false,false,true,false],"critical_flags":["GANCHO_DEFINICIONAL","CIFRAS_SIN_DIRECCION_INTERPRETABLE","GIRO_SOLO_NOMBRADO","PAYOFF_NO_DERIVADO_DE_LA_EVIDENCIA"]},
    {"id":"2026-10-31_smartpe-edicion-plantas","status":"FAIL","score":80,"review_basis":"lectura_en_frio_solo_narracion","reviewed_at":null,"checks":[true,false,true,true,false,true,true],"critical_flags":["APERTURA_DEFINICIONAL_NO_IN_MEDIAS_RES","GIRO_CIENTIFICO_NOMBRADO_SIN_EXPLICAR_MECANISMO"]},
    {"id":"2026-11-01_dato-cambio-horario-corazon","status":"FAIL","score":84,"review_basis":"lectura_en_frio_solo_narracion","reviewed_at":"2026-11-01T18:08:00-06:00","checks":[true,true,true,true,true,true,true],"critical_flags":["CIERRE_PRESELLO_INFERIOR_A_110_CARACTERES"]},
    {"id":"2026-11-01_llorar-cebolla-quimica","status":"FAIL","score":79,"review_basis":"lectura_en_frio_solo_narracion","reviewed_at":"2026-11-01T15:09:29-06:00","checks":[true,true,true,true,true,false,false],"critical_flags":["CIERRE_ATRIBUYE_INTENCION_EVOLUTIVA_NO_DEMOSTRADA","LIMITE_DE_EVIDENCIA_NO_EXPLICITO"]},
    {"id":"2026-11-01_pulpo-tres-corazones","status":"FAIL","score":72,"review_basis":"lectura_en_frio_solo_narracion","reviewed_at":"2026-11-01T15:09:29-06:00","checks":[true,false,true,true,true,false,true],"critical_flags":["APERTURA_HIPOTETICA_NO_IN_MEDIAS_RES","ANALOGIA_BRANQUIAS_SACAR_AIRE_DEL_AGUA_IMPRECISA","AFIRMACION_CORAZONES_NO_SUSTITUIBLES_SIN_RESPALDO"]},
    {"id":"2026-11-01_red-electrica-pulso-minuto","status":"PASS","score":89,"review_basis":"lectura_en_frio_solo_narracion","reviewed_at":"2026-11-01T15:09:29-06:00","checks":[true,true,true,true,true,true,true],"critical_flags":[]},
    {"id":"2026-11-02_camaron-mantis","status":"PASS","score":90,"review_basis":"lectura_en_frio_solo_narracion","reviewed_at":null,"checks":[true,true,true,true,true,true,true],"critical_flags":[]},
    {"id":"2026-11-02_comida-pan-duro","status":"FAIL","score":84,"review_basis":"lectura_en_frio_solo_narracion","reviewed_at":null,"checks":[true,true,true,true,true,true,true],"critical_flags":["CIERRE_SOBREAFIRMA_Y_CONTRADICE_LIMITE_DE_SECADO"]},
    {"id":"2026-11-04_cielo-azul-atardecer-rojo","status":"PASS","score":94,"review_basis":"lectura_en_frio_solo_narracion","reviewed_at":"2026-11-04T15:58:40-06:00","checks":[true,true,true,true,true,true,true],"critical_flags":[]},
    {"id":"2026-11-04_dato-polvo-atrapa-oro","status":"PENDIENTE","review_basis":"lectura_en_frio_solo_narracion","reviewed_at":null,"score":null,"checks":null,"critical_flags":null},
    {"id":"2026-11-05_kids-dia-en-venus","status":"PASS","score":88,"review_basis":"lectura_en_frio_solo_narracion","reviewed_at":"2026-11-18T15:00:00-06:00","checks":[true,true,true,true,true,true,true],"critical_flags":[]},
    {"id":"2026-11-05_comida-palomitas","status":"FAIL","score":82,"review_basis":"lectura_en_frio_solo_narracion","reviewed_at":"2026-11-18T15:00:00-06:00","checks":[true,false,false,true,true,true,true],"critical_flags":["APERTURA_DEFINICIONAL_NO_IN_MEDIAS_RES","ESCENA_6_REITERA_CAUSAS_DE_GRANOS_NO_REVENTADOS_SIN_INFORMACION_NUEVA"]},
    {"id":"2026-11-05_inter-arboles-se-comunican","status":"FAIL","score":78,"review_basis":"lectura_en_frio_solo_narracion","reviewed_at":"2026-11-18T15:00:00-06:00","checks":[true,false,true,true,true,true,true],"critical_flags":["APERTURA_GENERICA_NO_IN_MEDIAS_RES"]},
    {"id":"2026-11-05_inter-rayo-globular","status":"FAIL","score":81,"review_basis":"lectura_en_frio_solo_narracion","reviewed_at":"2026-11-18T15:00:00-06:00","checks":[true,false,true,true,true,true,true],"critical_flags":["APERTURA_HISTORICA_DESCRIPTIVA_NO_IN_MEDIAS_RES"]},
    {"id":"2026-11-06_kids-ballena-azul-corazon","status":"FAIL","score":80,"review_basis":"lectura_en_frio_solo_narracion","reviewed_at":"2026-11-18T15:00:00-06:00","checks":[true,true,true,true,true,true,false],"critical_flags":["PAYOFF_SOBREAFIRMA_CASI_SE_DETIENE"]},
    {"id":"2026-11-06_comida-aguacate-negro","status":"FAIL","score":79,"review_basis":"lectura_en_frio_solo_narracion","reviewed_at":"2026-11-18T15:00:00-06:00","checks":[true,true,false,false,true,true,true],"critical_flags":["REPETICION_ESCENAS_5_6_SIN_AVANCE_CAUSAL"]},
    {"id":"2026-11-06_inter-ranas-congeladas","status":"FAIL","score":83,"review_basis":"lectura_en_frio_solo_narracion","reviewed_at":"2026-11-18T15:00:00-06:00","checks":[true,true,false,false,true,true,true],"critical_flags":["REPETICION_ESCENAS_5_6_LIMITES_DE_ESPECIE_Y_CONDICIONES"]},
    {"id":"2026-11-06_inter-arena-cantante","status":"PASS","score":94,"review_basis":"lectura_en_frio_solo_narracion","reviewed_at":"2026-11-18T15:00:00-06:00","checks":[true,true,true,true,true,true,true],"critical_flags":[]},
    {"id":"2026-11-07_kids-huesos-bebe","status":"FAIL","score":82,"review_basis":"lectura_en_frio_solo_narracion","reviewed_at":"2026-11-18T15:00:00-06:00","checks":[true,true,false,false,true,true,true],"critical_flags":["ESCENA_6_REPITE_VARIACION_DE_CONTEO_Y_FUSION"]},
    {"id":"2026-11-07_comida-hielo-caliente","status":"FAIL","score":81,"review_basis":"lectura_en_frio_solo_narracion","reviewed_at":"2026-11-18T15:00:00-06:00","checks":[true,false,true,true,true,true,true],"critical_flags":["APERTURA_DE_CREENCIAS_NO_IN_MEDIAS_RES"]},
    {"id":"2026-11-07_inter-pulpo-suenos","status":"FAIL","score":72,"review_basis":"lectura_en_frio_solo_narracion","reviewed_at":"2026-11-18T15:00:00-06:00","checks":[true,true,false,false,false,false,false],"critical_flags":["FUENTE_PRIMARIA_CORRESPONDE_A_OCTOPUS_LAQUEUS_NO_INSULARIS","REPETICION_ESCENAS_5_6_Y_PAYOFF_VAGO"]},
    {"id":"2026-11-07_inter-nubes-pesan","status":"FAIL","score":78,"review_basis":"lectura_en_frio_solo_narracion","reviewed_at":"2026-11-18T15:00:00-06:00","checks":[true,true,false,false,true,true,false],"critical_flags":["ESCENA_7_REITERA_CIFRA_Y_LIMITE_SIN_PAYOFF_DE_SUSPENSION"]},
    {"id":"2026-11-09_dato-robot-ensambla-orbita","status":"PASS","score":90,"review_basis":"lectura_en_frio_solo_narracion","reviewed_at":"2026-11-09T18:45:00-06:00","checks":[true,true,true,true,true,true,true],"critical_flags":[]},
    {"id":"2026-11-10_comida-aprendizaje-sabor-nutriente","status":"PASS","score":92,"review_basis":"lectura_en_frio_solo_narracion","reviewed_at":"2026-11-10T15:47:50-06:00","checks":[true,true,true,true,true,true,true],"critical_flags":[]},
    {"id":"2026-11-10_dato-adn-sincroniza-flujo","status":"PASS","score":91,"review_basis":"lectura_en_frio_solo_narracion","reviewed_at":"2026-11-10T16:16:00-06:00","checks":[true,true,true,true,true,true,true],"critical_flags":[]},
    {"id":"2026-11-12_dato-pedorreta-chimpances","status":"PASS","score":91,"review_basis":"lectura_en_frio_solo_narracion","reviewed_at":"2026-11-12T15:38:50-06:00","checks":[true,true,true,true,true,true,true],"critical_flags":[]},
    {"id":"2026-11-13_dato-caracol-16-embriones","status":"PASS","score":91,"review_basis":"lectura_en_frio_solo_narracion","reviewed_at":"2026-11-13T15:42:39-06:00","checks":[true,true,true,true,true,true,true],"critical_flags":[]},
    {"id":"2026-11-14_dato-microplasticos-pantanal","status":"PASS","score":88,"review_basis":"lectura_en_frio_solo_narracion","reviewed_at":"2026-11-14T15:04:13-06:00","checks":[true,true,true,true,true,true,true],"critical_flags":[]},
    {"id":"2026-11-15_dato-dia-diapausa-lestes-sponsa","status":"PASS","score":90,"review_basis":"lectura_en_frio_solo_narracion","reviewed_at":"2026-11-15T15:51:23-06:00","checks":[true,true,true,true,true,true,true],"critical_flags":[]},
    {"id":"2026-11-15_dato-quasar-pareja-cosmic-dawn","status":"FAIL","score":0,"review_basis":"lectura_en_frio_solo_narracion","reviewed_at":"2026-11-23T04:02:29-06:00","reviewer_role":"control_compuerta_chatgpt_no_independiente","checks":[false,false,false,false,false,false,false],"critical_flags":["REVISION_INDEPENDIENTE_AUSENTE"]},
    {"id":"2026-11-16_dato-polen-desenreda-nanotubos","status":"PASS","score":91,"review_basis":"lectura_en_frio_solo_narracion","reviewed_at":"2026-11-16T15:45:46-06:00","checks":[true,true,true,true,true,true,true],"critical_flags":[]},
    {"id":"2026-11-17_dato-suelo-dos-relojes","status":"PASS","score":89,"review_basis":"lectura_en_frio_solo_narracion","reviewed_at":"2026-11-17T15:35:22-06:00","checks":[true,true,true,true,true,true,true],"critical_flags":[]},
    {"id":"2026-11-18_dato-catorce-campos-hidrotermales","status":"FAIL","score":68,"review_basis":"lectura_en_frio_solo_narracion","reviewed_at":"2026-11-19T15:04:50-06:00","checks":[false,true,false,false,false,true,false],"critical_flags":["PREGUNTA_CENTRAL_NO_RECONSTRUIBLE","SECUENCIA_DE_HALLAZGOS_SIN_PROGRESION_CAUSAL","GIRO_CIENTIFICO_NOMBRADO_PERO_NO_EXPLICADO","CIERRE_RESUMEN_SIN_PAYOFF"]},
    {"id":"2026-11-18_dato-kuroshio-puente-atmosferico","status":"PASS","score":90,"review_basis":"lectura_en_frio_solo_narracion","reviewed_at":"2026-11-18T15:00:00-06:00","checks":[true,true,true,true,true,true,true],"critical_flags":[]},
    {"id":"2026-11-19_dato-dia-luz-dos-manos-oro-poroso","status":"PASS","score":91,"review_basis":"lectura_en_frio_solo_narracion","reviewed_at":"2026-11-19T15:04:50-06:00","checks":[true,true,true,true,true,true,true],"critical_flags":[]},
    {"id":"2026-11-19_dato-estrella-dentro-de-estrella","status":"PASS","score":90,"review_basis":"lectura_en_frio_solo_narracion","reviewed_at":"2026-11-19T15:04:50-06:00","checks":[true,true,true,true,true,true,true],"critical_flags":[]},
    {"id":"2026-11-20_dato-dia-atlantico-humedad-sapropeles","status":"PASS","score":91,"review_basis":"lectura_en_frio_solo_narracion","reviewed_at":null,"checks":[true,true,true,true,true,true,true],"critical_flags":[]},
    {"id":"2026-11-20_dato-marea-cerebral-en-sueno","status":"FAIL","score":82,"review_basis":"lectura_en_frio_solo_narracion","reviewed_at":"2026-11-23T06:23:43-06:00","checks":[true,true,true,true,true,true,true],"critical_flags":["STAKES_NO_EXPLICADOS"]},
    {"id":"2026-11-21_fentale-metano-sin-erupcion","status":"PASS","score":90,"review_basis":"lectura_en_frio_solo_narracion","reviewed_at":"2026-11-20T16:11:24-06:00","checks":[true,true,true,true,true,true,true],"critical_flags":[]},
    {"id":"2026-11-21_homo-erectus-selva-tropical","status":"FAIL","score":83,"review_basis":"lectura_en_frio_solo_narracion","reviewed_at":"2026-11-20T22:06:10-06:00","checks":[true,true,true,true,false,true,true],"critical_flags":["GIRO_CIENTIFICO_NOMBRADO_PERO_NO_EXPLICADO"]},
    {"id":"2026-11-21_pulsar-gamma-reticulo","status":"FAIL","score":83,"review_basis":"lectura_en_frio_solo_narracion","reviewed_at":"2026-11-20T15:41:24-06:00","checks":[true,true,true,true,false,true,true],"critical_flags":["GIRO_CIENTIFICO_NOMBRADO_PERO_NO_EXPLICADO"]},
    {"id":"2026-11-22_bao-estrella-fusion-andromeda","status":"FAIL","score":84,"review_basis":"lectura_en_frio_solo_narracion","reviewed_at":"2026-11-21T13:56:37-06:00","checks":[true,true,true,true,true,true,true],"critical_flags":["STAKES_NO_EXPLICADOS"]},
    {"id":"2026-11-22_genes-estatura-etapas","status":"FAIL","score":72,"review_basis":"lectura_en_frio_solo_narracion","reviewed_at":"2026-11-22T15:54:03-06:00","checks":[true,false,false,false,false,true,true],"critical_flags":["APERTURA_DEFINICIONAL_NO_IN_MEDIAS_RES","MAPA_DE_INSTITUCIONES_ROMPE_CONTINUIDAD_NARRATIVA","GIRO_CIENTIFICO_NOMBRADO_SIN_MECANISMO_EXPLICADO"]},
    {"id":"2026-11-22_voyager-1-un-dia-luz","status":"FAIL","score":83,"review_basis":"lectura_en_frio_solo_narracion","reviewed_at":null,"checks":[true,true,true,true,true,true,true],"critical_flags":["FECHA_DE_HITO_Y_CONFIRMACION_CONFUNDIDAS"]},
    {"id":"2026-11-22_yubarta-genoma-soplo","status":"PASS","score":90,"review_basis":"lectura_en_frio_solo_narracion","reviewed_at":null,"reviewed_on":"2026-11-21","checks":[true,true,true,true,true,true,true],"critical_flags":[]},
    {"id":"2026-11-23_supersequias-722-eventos","status":"FAIL","score":82,"review_basis":"lectura_en_frio_solo_narracion","reviewed_at":"2026-11-23T00:57:16-06:00","checks":[true,true,true,true,true,true,true],"critical_flags":["STAKES_NO_EXPLICADOS"]},
    {"id":"2026-11-23_tropical-biodiversity-turnover","status":"FAIL","score":82,"review_basis":"lectura_en_frio_solo_narracion","reviewed_at":"2026-11-21T14:24:25-06:00","checks":[true,true,true,true,true,true,true],"critical_flags":["STAKES_NO_EXPLICADOS"]}
  ],
  "pending_auditor": [
    "2026-10-24_abejas-bullying",
    "2026-10-24_ideonella-pet",
    "2026-10-24_osedax-comehuesos",
    "2026-10-24_serpientes-que-ruedan",
    "2026-10-25_ave-jurasica-sin-vuelo",
    "2026-10-25_corales-contacto",
    "2026-10-25_reina-olor",
    "2026-10-25_sueno-electricidad-qom",
    "2026-10-26_baffin-bay-ice-shelf",
    "2026-10-26_catrina-posada-monerismo",
    "2026-10-26_hongo-gente-diminuta",
    "2026-10-26_papel-picado-dia-muertos",
    "2026-10-26_papel-picado-dia-muertos_parte2",
    "2026-10-26_pimiento-verde-rojo",
    "2026-10-27_cempasuchil-ciencia",
    "2026-10-27_corneja-decision-rapida",
    "2026-10-27_ddm-parte3-pomuch",
    "2026-10-27_familia-ajolote",
    "2026-10-27_kids-serpiente-voladora",
    "2026-10-27_noct-anfibio-marino",
    "2026-10-28_ddm-parte4-templo-mayor",
    "2026-10-28_familia-voyager-disco-oro",
    "2026-10-28_kids-titanoboa",
    "2026-10-28_monarca-almas",
    "2026-10-28_mosquito-fruitless-audicion",
    "2026-10-28_noct-lince-milanos",
    "2026-10-28_pan-de-muerto-huesos",
    "2026-10-29_juno-choque-proa",
    "2026-10-29_muralismo-cu",
    "2026-10-30_arqueas-origen-eucariotas",
    "2026-10-30_kromdraai-primera-fecha",
    "2026-10-31_pardelas-jetlag-solar",
    "2026-11-03_dato-polvo-africano-microbios",
    "2026-11-03_kids-leche-enchilado",
    "2026-11-xx_kids-flamencos-rosas_RESPALDO",
    "demo-001",
    "guiones_lote_01",
    "lote01-01-el-nino",
    "lote01-02-petroleo",
    "lote01-03-balon-curva",
    "lote01-04-tardigrado",
    "lote01-05-chicxulub"
  ],
  "inventory": {"project_storyboards_read":90,"qa_present":48,"pass":20,"fail":27,"pending_status":1,"pending_auditor":42}
}
```

### 5. Seguimiento técnico

Se releyó `docs/INVESTIGACION_API_META_Y_GOOGLE_TRENDS.md` (corte 2026-11-22, §9.11) y se contrastó con documentación oficial actual:
- La referencia de versionado de Meta declara Graph API v27.0 como versión actual; la ruta heredada `/docs/graph-api/changelog/versions/` aún muestra v26.0. Esta discrepancia ya está registrada en §9.8–9.10; no es un cambio nuevo en esta pasada.
- Page Insights sigue mostrando el aviso de deprecación de métricas con fecha 15-06-2026 y las restricciones ya registradas en §9.11.
- Instagram Insights mantiene referencias v27.0 y las métricas de vistas/interacciones ya documentadas; no apareció una entrada nueva de changelog posterior al corte registrado.
- Google Trends API sigue en alfa limitada, con ventana móvil de cinco años, agregaciones diaria/semanal/mensual/anual, regiones/subregiones y escala consistente entre consultas.
  
**Resultado técnico:** no se encontró un cambio nuevo relevante y sustentado. No se reescribió `docs/INVESTIGACION_API_META_Y_GOOGLE_TRENDS.md`.

### 6. Resultado de staging de esta ejecución

- Se conserva exactamente un radar para 2026-11-23: este archivo, actualizado mediante addendum.
- No se crea storyboard nuevo: todos los slots aplicables muestran ocupación o conflicto entre ramas.
- No se reescriben los dos storyboards existentes, no se crea copia en `cola/entrada/`, no se escribe `narrative_qa`, no se crea estado Grok, no se generan medios y no se programa publicación.
- No se modifican `main`, `data/*.json`, motores ni Motor U6.


## Corrección de verificación primaria — 2026-11-23 22:00 CDMX

La lectura completa de la fuente primaria de *Scientific Data*, sección de validación GDIS y Fig. 10, sí confirma el dato que antes quedó marcado como pendiente por falta de acceso al cuerpo del artículo:

- **Observación:** el conjunto compara 234 eventos independientes con GDIS; 139 coinciden con los clusters del estudio.
- **Cálculo reportado por el artículo:** 139/234 = **59.4%**.
- **Resultado condicional:** la coincidencia sube a aproximadamente **71%** al restringir el análisis a regiones interiores no africanas; no es la tasa global.
- **Validación inversa:** 74% de 96 eventos en cuatro regiones densamente pobladas tuvieron corroboración GDIS.
- **Límite:** GDIS registra desastres con impacto socioeconómico, no intensidad/duración física; el artículo atribuye parte de las discrepancias a vulnerabilidad socioeconómica en África interior y limitaciones de datos costeros.

Esto **sustituye** las notas anteriores de este radar que dejaban 139/234 y 59.4% como `PENDING_SOURCE`. La fuente primaria respalda el claim y el storyboard ya conserva `verification_status=VERIFICADO_FUENTE_PRIMARIA`; no se cambió su narración, claims ni `narrative_qa`. El DOI sigue en `PENDIENTE_RESOLVEDOR`: los endpoints de Crossref y doi.org no entregaron respuesta verificable. Por tanto, no se habilita promoción. El storyboard conserva FAIL/82, `STAKES_NO_EXPLICADOS`, y su slot está ocupado/conflictivo según la última evidencia de programación.

Fuente primaria: https://www.nature.com/articles/s41597-026-08886-6 (Fig. 10 y sección GDIS, párrafos sobre los 234 eventos, 139 coincidencias y 71% condicional).
