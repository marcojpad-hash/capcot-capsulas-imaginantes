# Radar CAPCOT — 9 de noviembre de 2026

**Repositorio:** marcojpad-hash/capcot-capsulas-imaginantes  
**Rama:** `feature/capcot-video-discovery-continuity`  
**Corte:** 2026-11-09, 08:10 America/Mexico_City  
**HEAD observado antes de este commit:** `b16c71e4ea07b0787056c2c0093d53d763cdeebe`  
**Resultado operativo:** `NO_DUPLICAR`  
**Entregable de esta ejecución:** únicamente este radar. No se crea storyboard porque el horario del 9-nov no deja un slot textual libre y autorizado; el 23:30 está expresamente excluido.

## 1. Guardia anti-duplicación y cupo del día

Se enumeraron los IDs con fecha 2026-11-09 en `proyectos/`, `salidas/`, `cola/entrada/` y `cola/bloqueados/`: **ninguno**. No existe un storyboard con fecha_objetivo 2026-11-09 en esas rutas.

La fuente horaria del día, `data/horario_2026-11-09.json`, registra únicamente:

| Hora CDMX | Registro | Estado observado | Tratamiento |
|---|---|---|---|
| 07:00 | `2026-11-06_inter-ranas-congeladas` | `publicado_yt_tt` | Slot ya ocupado. El registro indica que la rana ya estaba pública en YouTube y TikTok; no se volvió a subir. |
| 23:30 | `dato_del_dia`, sin ID ni paquete | `sin_paquete` | Excluido expresamente de esta ejecución. |

No hay asignaciones de 13:30, 17:00 ni 19:00 en el horario específico del 9-nov. No se interpreta la capacidad técnica de cinco ventanas como permiso para inventar una asignación. Por tanto, **no hay slot libre y autorizado para un storyboard**.

La cápsula que ocupó 07:00 corresponde al proyecto canónico de ranas, cuyo estilo registrado es `papel_rasgado_capas`. No se asigna un estilo nuevo porque no se redacta storyboard. El lote canónico 5–7 nov y sus estilos se conservan sin cambios.

## 2. Memoria editorial y rotación

Se leyeron sin modificar:

- `data/temas_del_dia.json`: cinco fechas registradas; última fecha 2026-10-28.
- `data/rotacion.json`: 27 registros; último registro 2026-10-31.
- `data/publicaciones.json`: 22 registros; último registro 2026-10-31.
- `scripts/registro_editorial.py`: vista de lectura combinada que une registros de rotación/publicación/cola con storyboards de proyectos, cola y salidas. Se siguió su lógica para distinguir propuestas de publicaciones; no se ejecutó el script Python porque esta sesión no tiene un checkout/runtime local del repositorio. El inventario se contrastó directamente contra el árbol y los JSON de GitHub.
- `docs/briefs/2026-11-09_CONTROL_COLA.md`: confirma que no hay proyecto del 9-nov y que la rana de 07:00 ya estaba publicada en YT+TT.

Los storyboards de `proyectos/` son evidencia de temas y estilos propuestos, no de publicación. Los estados de horario y las publicaciones efectivas se mantienen separados. No se modifica ningún `data/*.json`.

## 3. RSS científicos — intentos y errores exactos

Se intentaron las diez URLs definidas en `scripts/tendencias.py`. No se ejecutó el script y **no se descargó ni parseó XML**. Resultado observado al abrir cada feed:

| Feed | URL | Error literal observado |
|---|---|---|
| ScienceDaily ciencia | https://www.sciencedaily.com/rss/top/science.xml | `HTTP 400: Unsupported content-type: application/xml` |
| ScienceDaily salud | https://www.sciencedaily.com/rss/top/health.xml | `HTTP 400: Unsupported content-type: application/xml` |
| ScienceDaily espacio | https://www.sciencedaily.com/rss/space_time.xml | `HTTP 400: Unsupported content-type: application/xml` |
| Phys.org | https://phys.org/rss-feed/ | `HTTP 400: Unsupported content-type: text/xml` |
| NASA | https://www.nasa.gov/news-release/feed/ | `HTTP 400: Unsupported content-type: application/rss+xml` |
| ESA Space Science | https://www.esa.int/rssfeed/Our_Activities/Space_Science | `HTTP 404: Not Found` |
| Nature | https://www.nature.com/nature.rss | `HTTP 400: Unsupported content-type: application/rss+xml` |
| EurekAlert | https://www.eurekalert.org/rss/news.xml | `URL ... is not accessible via this tool` |
| SINC | https://www.agenciasinc.es/rss | `URL ... is not accessible via this tool` |
| UNAM Global | https://unamglobal.unam.mx/feed/ | `TimeoutError` |

La búsqueda científica de esta ejecución se realizó mediante páginas y resultados indexados de los editores, no mediante una ingesta RSS. No se presenta como resultado de `scripts/tendencias.py`.

## 4. Google Trends México — respaldo oficial

El RSS público `https://trends.google.com/trending/rss?geo=MX` devolvió `URL ... is not accessible via this tool`. Se consultó como respaldo la página oficial [Trending Now — México](https://trends.google.com/trending?geo=MX&hl=es), con ventana de últimas 24 horas.

**Observado en la página:**
- 288 tendencias en total; 25 visibles en la primera página.
- Predominan deportes y entretenimiento: «león - guadalajara» (1 M+), «atlético madrid - barcelona» (500 mil+) y otros partidos.
- Entre las consultas no deportivas aparecen «jornada laboral» (20 mil+), «construcción» (20 mil+), «telefonía móvil» (20 mil+) y «el niño» (10 mil+, activa hace 12 h).
- «El niño» es una señal potencialmente relacionada con clima, pero el término y sus consultas relacionadas no permiten atribuir por sí solos interés específico en el fenómeno climático.

**Interpretación editorial:** no se observa una tendencia científica inequívoca que justifique forzar uno de los candidatos. Trends se registra como contexto de atención, no como evidencia científica ni como causa de selección.

## 5. Candidatos científicos publicados entre el 2 y el 9 de noviembre

Se eligieron cinco artículos originales publicados entre el 4 y el 6 de noviembre. Ninguno repite los temas del radar del 8-nov (HCl en Alba Mons, arquea en condiciones marcianas, moléculas derivadas del hemo en dinosaurio, ruido antropogénico o cavidad de ondas de materia). La tendencia, la relevancia científica y la oportunidad editorial se puntúan por separado.

### Candidato 1 — Un smartwatch busca señales de hipertensión sin manguito

- **Fecha editorial:** 5-nov-2026.
- **Línea:** Actualidad; cuerpo/tecnología. La sublínea médica/IA es futura y provisional; no se declara como nueva línea aprobada.
- **Novedad observada:** el estudio combina señales de fotopletismografía (PPG) y acelerometría de un smartwatch de consumo con un modelo de IA, sin calibración con manguito, para identificar señales compatibles con hipertensión.
- **Fuente primaria:** Di Achille et al., Nature, “Opportunistically Detecting Signs of Hypertension on a Consumer Smartwatch”. https://www.nature.com/articles/s41586-026-11336-3
- **DOI mostrado por el editor:** `10.1038/s41586-026-11336-3` — **PENDIENTE_RESOLVEDOR**. El artículo del editor muestra este DOI y la fecha; la consulta directa al resolvedor DOI y a Crossref no fue accesible en esta ejecución. No se declara validación independiente.
- **Datos observados en el resumen primario:** estudio prospectivo multicéntrico con 196 participantes diversos, sin enfermedad cardiovascular conocida ni medicación antihipertensiva; comparación con monitorización ambulatoria de presión arterial de 24 horas; siete días de monitorización en condiciones reales. Sensibilidad 65.8% (IC 95%: 54.0–76.3), especificidad 90.0% (83.2–94.7) y valor predictivo positivo 80.6% (68.6–89.6). El cribado inicial de consultorio tuvo sensibilidad 55.3% y especificidad 90.0%.
- **Tendencia:** no se observó una tendencia inequívoca de smartwatch/hipertensión en la primera página de Google Trends México.
- **Relevancia científica:** alta; evalúa un método de cribado oportunista contra una referencia clínica establecida.
- **Oportunidad editorial:** alta; mecanismo visual claro (pulso óptico + movimiento) y una pregunta que puede resolverse sin convertir el dispositivo en un diagnóstico.
- **Público/ocasión:** curiosidad sobre cuerpo y tecnología; sin fecha de calendario.
- **Riesgos:** sensibilidad de 65.8% significa que el método no identifica todos los casos; no afirmar que el reloj mide la presión como un tensiómetro, diagnostica hipertensión ni sustituye una medición con manguito. El propio resumen plantea detección oportunista que debe llevar a evaluación clínica y confirmación con métodos establecidos. El equipo incluye autores de Google Research; describir el estudio y sus límites, no convertirlo en aval comercial.
- **Verificación:** resumen del artículo primario del editor consultado; DOI pendiente de resolución independiente; no se leyó el texto completo porque la página directa de Nature redirigió a un proveedor de identidad y devolvió error 500 al abrirse.

### Candidato 2 — Una sola intervención CRISPR intenta apagar ANGPTL3 en el hígado

- **Fecha editorial:** 6-nov-2026.
- **Línea:** Actualidad; cuerpo/biotecnología. La sublínea médica es futura/provisional.
- **Novedad observada:** el trabajo describe una estrategia de edición de bases adenina CRISPR dirigida al hígado para inactivar ANGPTL3, una proteína relacionada con LDL-C y lipoproteínas ricas en triglicéridos. El editor se entrega mediante una infusión de ARN guía y ARNm encapsulados en una nanopartícula lipídica con GalNAc.
- **Fuente primaria:** Mizoguchi et al., Nature, “In Vivo CRISPR Base Editing of ANGPTL3 for Durable Lipid Lowering”. https://www.nature.com/articles/s41586-026-11233-9
- **DOI mostrado por el editor:** `10.1038/s41586-026-11233-9` — **PENDIENTE_RESOLVEDOR**. El DOI aparece en el registro editorial; Crossref y el resolvedor DOI no fueron accesibles en esta ejecución.
- **Datos observados en el resumen primario:** en células hepáticas humanas in vitro se confirmó el cambio de base en el locus ANGPTL3 sin edición fuera de objetivo detectable en aproximadamente 3,000 sitios candidatos. En primates no humanos, la inactivación redujo más de 90% la proteína ANGPTL3 media y se observó persistencia hasta tres años después de una dosis. En modelos de ratón y primates no humanos con hiperlipidemia, se asociaron reducciones de aproximadamente 40–50% en LDL-C y 50–70% en triglicéridos. El artículo indica que estos resultados sustentan un ensayo first-in-human que está en curso.
- **Tendencia:** no observada en Trends México.
- **Relevancia científica:** muy alta; edición genética in vivo con datos de durabilidad preclínica.
- **Oportunidad editorial:** alta; el contraste entre una dosis y un cambio biológico duradero ofrece un arco claro.
- **Público/ocasión:** curiosidad sobre genética y cuerpo; sin ocasión de calendario.
- **Riesgos:** no decir que ya es tratamiento aprobado ni que los porcentajes se observaron en pacientes. Los resultados de reducción de lípidos citados corresponden a modelos animales; el ensayo en humanos está en curso. No sugerir tratamientos ni decisiones médicas. Los autores incluyen afiliación a Verve Therapeutics, filial propiedad de Eli Lilly; registrar la participación empresarial como contexto de interés.
- **Verificación:** resumen y metadatos de la fuente editorial primaria consultados; DOI pendiente de resolución independiente; no se accedió al texto completo por la redirección de Nature.

### Candidato 3 — Un simulador cuántico muestra fases que tardan en deshacerse

- **Fecha editorial:** 4-nov-2026.
- **Línea:** Actualidad; dato científico/física cuántica.
- **Novedad observada:** un simulador programable de átomos neutros explora dinámicas de modelos de espín con hasta 180 qubits. El equipo observa estados pretermales de larga duración, su ruptura resonante y una transición dinámica de primer orden en dos dimensiones.
- **Fuente primaria:** Darbha et al., Nature, “Observation of prethermal dynamical phase transitions and resonant melting”. https://www.nature.com/articles/s41586-026-11225-9
- **DOI mostrado por el editor:** `10.1038/s41586-026-11225-9` — **PENDIENTE_RESOLVEDOR**. Crossref y el resolvedor DOI no fueron accesibles.
- **Datos observados en el resumen y datos extendidos:** hasta 180 qubits en el simulador de átomos neutros; los datos experimentales descritos usan 100 muestras por evolución temporal para la geometría de 180 átomos. La colaboración incluye a QuEra Computing y el simulador Aquila.
- **Tendencia:** no observada en Trends México.
- **Relevancia científica:** alta; evidencia experimental de regímenes dinámicos y de una transición que no se hereda simplemente del equilibrio.
- **Oportunidad editorial:** media; visualmente potente, pero el mecanismo exige traducción rigurosa para no convertirlo en una explicación falsa de una computadora cuántica general.
- **Público/ocasión:** curiosidad de física y tecnología; sin ocasión de calendario.
- **Riesgos:** no afirmar que el experimento es una computadora cuántica de uso general, que resolvió una tarea cotidiana ni que los átomos se «derritieron» literalmente. «Pretermal» requiere explicar que es un estado transitorio de larga duración, no un nuevo estado permanente. Hay autores afiliados a QuEra; la página declara interés financiero de uno de los autores.
- **Verificación:** resumen, fecha, DOI y datos extendidos del editor consultados en resultados indexados; DOI pendiente de resolvedor. La página directa de Nature devolvió redirección/error 500.

### Candidato 4 — Luz visible activa una ruta para generar radicales de carbono

- **Fecha editorial:** 4-nov-2026.
- **Línea:** Actualidad; dato científico/química.
- **Novedad observada:** complejos de cobre con sulfonas heteroarílicas absorben luz visible y sufren transferencia irreversible de carga metal-ligando; la ruptura del enlace C–S genera radicales centrados en carbono. El trabajo demuestra aplicaciones en funcionalización C–H de arenos y alquinos y en funcionalización radicalaria de alquenos.
- **Fuente primaria:** Wei et al., Nature, “Carbon radical generation by irreversible metal-to-ligand charge transfer”. https://www.nature.com/articles/s41586-026-11368-9
- **DOI mostrado por el editor:** `10.1038/s41586-026-11368-9` — **PENDIENTE_RESOLVEDOR**. Crossref y el resolvedor DOI no fueron accesibles.
- **Tendencia:** no observada en Trends México.
- **Relevancia científica:** alta para química sintética; propone una forma de generar radicales alquilo bajo irradiación visible.
- **Oportunidad editorial:** media-baja; el mecanismo es especializado y necesita una traducción visual muy cuidada.
- **Público/ocasión:** curiosidad de química y luz; sin ocasión de calendario.
- **Riesgos:** no confundir radicales de carbono de química sintética con radicales libres del cuerpo ni sugerir una reacción doméstica. No decir que la luz por sí sola rompe cualquier enlace; la reacción usa complejos de cobre y ligandos concretos.
- **Verificación:** resumen, fecha y DOI mostrados por el editor consultados; DOI pendiente de resolución independiente; texto completo no accesible por la redirección de Nature.

### Candidato 5 — Un modelo energético calcula rutas de hidrógeno para China

- **Fecha editorial:** 5-nov-2026.
- **Línea:** Actualidad; ciencia de energía/modelado de sistemas. Ajuste editorial bajo: incluye una dimensión económica y de política energética que no debe convertirse en comentario social.
- **Novedad observada:** el estudio modela rutas de transición energética con hidrógeno y derivados, considerando operación eléctrica horaria en 29 regiones provinciales y más de 46,000 rutas de transporte ferroviario, carretero, marítimo y por ductos.
- **Fuente primaria:** Chen et al., Nature, “Hydrogen Derivatives Enable Cost-Effective Carbon Neutrality in China”. https://www.nature.com/articles/s41586-026-11351-4
- **DOI mostrado por el editor:** `10.1038/s41586-026-11351-4` — **PENDIENTE_RESOLVEDOR**. Crossref y el resolvedor DOI no fueron accesibles.
- **Cálculo/modelo reportado por autores:** el escenario con hidrógeno y derivados estima un costo de transición 10.7 billones de dólares menor que las rutas comparadas de renovables y electrificación, y un costo de abatimiento de carbono de -6.15 dólares por tonelada. Son resultados de un modelo de escenarios, no ahorros observados ni resultados ya realizados.
- **Tendencia:** no observada en Trends México.
- **Relevancia científica:** media-alta para sistemas energéticos; depende de supuestos y escenarios.
- **Oportunidad editorial:** baja para el canal principal; el resultado requiere demasiada explicación metodológica y el foco puede derivar hacia política/economía.
- **Público/ocasión:** público interesado en energía y tecnología; sin ocasión de calendario.
- **Riesgos:** no extrapolar el modelo chino a México ni presentar las cifras como ahorro ya obtenido. No convertir el artículo en análisis de política o economía. Mantenerlo como escenario modelado.
- **Verificación:** resumen y metadatos del editor consultados; DOI pendiente de resolución independiente; texto completo no accesible por redirección de Nature.

## 6. Recomendación editorial — no ejecutada

**Candidato principal para el próximo slot que sea asignado expresamente: smartwatch e hipertensión (candidato 1).**

Motivos:
1. La pregunta se entiende de inmediato y el mecanismo (luz reflejada en la piel + movimiento) puede representarse sin inventar protagonistas.
2. El estudio usa una referencia clínica explícita y reporta sensibilidad/especificidad; el límite puede formar parte de la historia, no ocultarse.
3. La narración puede girar sobre la diferencia entre detectar una señal y diagnosticar una condición.

**Límite que debe sostener la historia:** el dispositivo no reemplaza el manguito ni diagnostica. La sensibilidad reportada fue 65.8%; el resultado se plantea como cribado oportunista que lleva a confirmación clínica.

**Alternativa de mayor novedad y mayor riesgo:** CRISPR-ANGPTL3. Es un hallazgo preclínico con ensayo first-in-human en curso, pero la diferencia entre resultados animales y humanos debe permanecer explícita y la afiliación empresarial merece contexto.

No se asigna estilo, arco, mapa ni storyboard en esta ejecución porque no hay slot autorizado. La recomendación no constituye decisión editorial final de Grok.

## 7. Seguimiento técnico: Meta Graph API, Insights y Google Trends API

Se revisaron las referencias oficiales indicadas en `docs/INVESTIGACION_API_META_Y_GOOGLE_TRENDS.md`:

| Referencia oficial | Resultado de esta consulta |
|---|---|
| Graph API changelog | `HTTP 429: Too Many Requests` |
| Instagram Platform changelog | `HTTP 429: Too Many Requests` |
| Facebook Pages API | `HTTP 429: Too Many Requests` |
| Facebook Page Insights reference | URL no accesible mediante esta herramienta |
| Instagram Media Insights reference | URL no accesible mediante esta herramienta |
| Google Trends API alfa | Accesible; sigue anunciando acceso alfa limitado, ventana móvil de cinco años, agregaciones diaria/semanal/mensual/anual, regiones/subregiones y datos escalados de forma consistente (no volúmenes absolutos). |

Fuentes oficiales Google:
- https://developers.google.com/search/apis/trends
- https://developers.google.com/search/blog/2025/07/trends-api

No se identificó un cambio nuevo de Meta verificable directamente en sus referencias oficiales. La documentación de Google Trends mantiene las capacidades ya descritas en el informe del repositorio. **No se actualiza ni reescribe `docs/INVESTIGACION_API_META_Y_GOOGLE_TRENDS.md`.** Los errores 429/no accesible se registran como límite de consulta, no como evidencia de que no existan cambios.

## 8. Estado de narrative_qa preexistente — lectura directa de GitHub

Se releyeron los doce storyboards canónicos de `proyectos/` del lote 5–7 nov. En los doce JSON:

- `review_basis`: `lectura_en_frio_solo_narracion`
- `reviewed_at`: `2026-11-08T15:27:31-06:00`
- Orden exacto de los siete checks en los vectores siguientes: `pregunta_central_reconstruible`, `apertura_in_medias_res`, `progresion_por_escena`, `transiciones_causales`, `giro_cientifico_explicado`, `limite_evidencia_explicito`, `payoff_cierre_apertura`.

| project_id | fecha_objetivo / slot_local | status / score | checks en orden JSON | critical_flags |
|---|---|---|---|---|
| `2026-11-05_kids-dia-en-venus` | 2026-11-05 / 07:00 | PASS / 88 | [true,true,true,true,true,true,true] | [] |
| `2026-11-05_comida-palomitas` | 2026-11-05 / 13:30 | FAIL / 82 | [true,false,false,true,true,true,true] | [`APERTURA_DEFINICIONAL_NO_IN_MEDIAS_RES`, `ESCENA_6_REITERA_CAUSAS_DE_GRANOS_NO_REVENTADOS_SIN_INFORMACION_NUEVA`] |
| `2026-11-05_inter-arboles-se-comunican` | 2026-11-05 / 17:00 | FAIL / 78 | [true,false,true,true,true,true,true] | [`APERTURA_GENERICA_NO_IN_MEDIAS_RES`] |
| `2026-11-05_inter-rayo-globular` | 2026-11-05 / 17:45 | FAIL / 81 | [true,false,true,true,true,true,true] | [`APERTURA_HISTORICA_DESCRIPTIVA_NO_IN_MEDIAS_RES`] |
| `2026-11-06_kids-ballena-azul-corazon` | 2026-11-06 / 07:00 | FAIL / 80 | [true,true,true,true,true,true,false] | [`PAYOFF_SOBREAFIRMA_CASI_SE_DETIENE`] |
| `2026-11-06_comida-aguacate-negro` | 2026-11-06 / 13:30 | FAIL / 79 | [true,true,false,false,true,true,true] | [`REPETICION_ESCENAS_5_6_SIN_AVANCE_CAUSAL`] |
| `2026-11-06_inter-ranas-congeladas` | 2026-11-06 / 17:00 | FAIL / 83 | [true,true,false,false,true,true,true] | [`REPETICION_ESCENAS_5_6_LIMITES_DE_ESPECIE_Y_CONDICIONES`] |
| `2026-11-06_inter-arena-cantante` | 2026-11-06 / 17:45 | PASS / 94 | [true,true,true,true,true,true,true] | [] |
| `2026-11-07_kids-huesos-bebe` | 2026-11-07 / 07:00 | FAIL / 82 | [true,true,false,false,true,true,true] | [`ESCENA_6_REPITE_VARIACION_DE_CONTEO_Y_FUSION`] |
| `2026-11-07_comida-hielo-caliente` | 2026-11-07 / 13:30 | FAIL / 81 | [true,false,true,true,true,true,true] | [`APERTURA_DE_CREENCIAS_NO_IN_MEDIAS_RES`] |
| `2026-11-07_inter-pulpo-suenos` | 2026-11-07 / 17:00 | FAIL / 80 | [true,true,false,false,true,true,false] | [`REPETICION_ESCENAS_5_6_Y_PAYOFF_VAGO`] |
| `2026-11-07_inter-nubes-pesan` | 2026-11-07 / 17:45 | FAIL / 78 | [true,true,false,false,true,true,false] | [`ESCENA_7_REITERA_CIFRA_Y_LIMITE_SIN_PAYOFF_DE_SUSPENSION`] |

Balance literal de los doce JSON: **2 PASS y 10 FAIL**. No se volvió a ejecutar QA narrativo, no se escribió `narrative_qa`, no se corrigió ni promovió ningún storyboard.

Otros storyboards recientes releídos:
- `cola/entrada/2026-11-07_dato-clavo-te-cocina/storyboard.json`: sin `narrative_qa` → `PENDIENTE_AUDITOR`; fecha_objetivo 2026-11-07, slot 23:30.
- `salidas/2026-11-04_inter-bioluminiscencia-mar/storyboard.json`: sin `narrative_qa` → `PENDIENTE_AUDITOR`.
- `salidas/2026-11-04_kids-hipo-por-que/storyboard.json`: sin `narrative_qa` → `PENDIENTE_AUDITOR`.
- `salidas/2026-11-04_comida-miel-no-caduca/storyboard.json`: sin `narrative_qa` → `PENDIENTE_AUDITOR`.

La carpeta heredada de clavo no se convierte a la ruta plana de handoff ni se redispatcha: no tiene QA narrativo independiente PASS ni estado de recepción de Grok.

## 9. Integridad de esta ejecución

- Se crea únicamente `docs/briefs/2026-11-09_RADAR_CAPCOT.md`; no existe slot libre y autorizado para crear `proyectos/YYYY-MM-DD_slug/storyboard.json`.
- No se escribe en `cola/entrada/` ni en `cola/bloqueados/`.
- No se crea `*_fuentes.md`; las fuentes están dentro de este brief.
- No se escribe `narrative_qa`, no se ejecuta QA narrativo y no se declara aceptación de Grok.
- No se generan frames, imágenes, audio, voz, video ni renders.
- No se publica ni programa contenido; no se consumen créditos.
- No se modifican `data/*.json`, `main`, workflows, motores ni Motor U6.
- No se modifica el informe técnico de Meta/Google porque no apareció un cambio nuevo sustentado directamente por documentación oficial.

## 10. Actualización de slot — 9-nov-2026, 16:41 CDMX

**Cambio de instrucción:** después del corte de las 08:10, Mj asignó expresamente el slot `2026-11-09 23:30 CDMX` al dato del día. La tabla del horario sigue indicando `dato_del_dia / sin_paquete`; no se modifica `data/horario_2026-11-09.json`.

**Tema preparado como borrador:** demostración ASTRA de ensamblaje robótico en órbita. El anuncio primario de Caltech es del 5-nov-2026; la investigación de actualidad realizada hoy encontró además la cobertura de ScienceDaily fechada 9-nov. No se presenta como paper académico ni se inventa DOI: la evidencia primaria consultada es institucional (Caltech y DARPA).

- Fuente principal: https://www.caltech.edu/about/news/caltech-robotic-space-demo-successfully-builds-in-space
- Contraste institucional: https://www.darpa.mil/news/2026/nom4d-program-demonstrates-automated-in-space-assembly
- Fuente cartográfica para pin aproximado de Vandenberg: https://ntrs.nasa.gov/api/citations/19910012870/downloads/19910012870.pdf
- Hecho central: ASTRA llevaba dos tramos prefabricados y un manipulador; el sistema ensambló un tercer tramo en órbita. El diseño completo prevé once; no se completó la antena de 1.4 m. El equipo en tierra enviaba comandos y revisaba fotografías.
- Estilo elegido: `art_deco_poster`, distinto de `papel_rasgado_capas` (ranas, slot 07:00) y `amigurumi` (clavo, slot 23:30 anterior). Estructura: `historia`, no `pregunta`.
- Storyboard creado en `proyectos/2026-11-09_dato-robot-ensambla-orbita/storyboard.json`; 8 escenas, 205 palabras, 78 s de escenas + 6 s de cortinilla = 84 s; gancho de 5 palabras. Fuentes y estado están dentro del JSON, conforme al contrato vigente; no se creó `fuentes.md` separado.
- Estado del borrador: `BORRADOR_EN_PROYECTOS_NO_APTO_PARA_PROMOCION`. No contiene `narrative_qa`: corresponde al auditor independiente hacer lectura en frío. Por tanto, todavía no se copia a `cola/entrada/` ni se afirma que está recibido por Grok.
- No se crearon estados de Grok, no se modificó `data/*.json`, no se disparó Actions y no se generaron medios.