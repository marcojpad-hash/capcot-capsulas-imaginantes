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
