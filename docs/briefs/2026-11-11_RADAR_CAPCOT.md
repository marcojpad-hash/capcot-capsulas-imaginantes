# Radar CAPCOT — 11 de noviembre de 2026

**Corte:** 2026-11-11, 08:05 America/Mexico_City  
**Repositorio:** marcojpad-hash/capcot-capsulas-imaginantes  
**Rama:** feature/capcot-video-discovery-continuity  
**Resultado operativo:** NO_DUPLICAR — radar solamente; no hay slot libre y autorizado para storyboard.  
**Entregables de esta ejecución:** este radar. No se creó storyboard porque la guardia de horario encontró ocupados todos los slots utilizables.  
**Seguimiento técnico:** se actualizó el informe existente de Meta/Google Trends por un cambio relevante de Graph API v27.0; commit 80c29b04c31c4e337c6c0bfa9cc397d991296213.

## 1. Guardia anti-duplicación y cupo del 11-nov

Se enumeraron las rutas completas antes de proponer un storyboard:

| Ruta | Entradas de primer nivel | Entradas con fecha 2026-11-11 |
|---|---:|---:|
| proyectos/ | 80 | 0 |
| salidas/ | 58 | 0 |
| cola/entrada/ | 3 | 0 |
| cola/bloqueados/ | 44 | 0 |
| docs/briefs/ | 26 | 0 |

El radar 2026-11-11 no existía antes de esta escritura. No hay storyboard del 11-nov en ninguna de las cuatro rutas de proyectos/producción/cola. Además de revisar los nombres de directorio, se inspeccionaron fecha_objetivo y slot_local en los 67 storyboards de proyectos/ y en los 16 registros únicos adicionales de salidas/, cola/entrada/ y cola/bloqueados/: ninguno declara fecha_objetivo 2026-11-11. En varios históricos ambos campos están ausentes; en esos casos no se inventó fecha ni slot y se contrastó el horario diario vigente.

### Horario diario observado

Fuente: data/horario_2026-11-11.json, actualizado 07:35:14 CDMX; contrastado con data/horarios.json, actualización 9-nov.

| Slot | Registro | Estado del horario | Decisión |
|---|---|---|---|
| 07:00 | 2026-11-06_kids-ballena-azul-corazon | publicado_yt_tt | Ocupado. No volver a subir ni crear otro paquete para ese slot. |
| 13:30 | 2026-11-07_comida-hielo-caliente (extra Mpemba) | programado_yt_tt_fb | Ocupado. YouTube conserva publishAt 13:30 CDMX; TikTok y Facebook figuran programados. |
| 17:00 | corneja-resub | programado_yt_tt | Ocupado. Es una resubida aprobada; Facebook no forma parte de ese resub. |
| 19:00 | sin asignación | ventana retirada desde 5-nov; solo con OK explícito | No autorizado. |
| 23:30 | dato_del_dia | sin_paquete_en_esta_ventana | Excluido expresamente por las instrucciones vigentes. |

La ventana 13:30–15:00 sigue en prueba, pero hoy está ocupada por el extra Mpemba. La ventana de tarde 16:30–18:00 está ocupada por la resub de las 17:00; no se interpreta el resto de la ventana como una segunda autorización. La ventana 19:00 está retirada y 23:30 no se usa.

**Resultado de la guardia:** no hay slot libre y autorizado. Se registra NO_DUPLICAR. No se creó, copió ni reescribió storyboard; no se eligió estilo ni estructura; no se escribió en cola/entrada.

## 2. Rotación, memoria editorial y deduplicación temática

Se leyeron los registros canónicos y la fuente de lectura combinada:

- data/temas_del_dia.json: el último día registrado es 2026-10-28.
- data/rotacion.json: 27 registros; corte 2026-10-31.
- data/publicaciones.json: 22 registros; corte 2026-10-31.
- data/cola.json: un registro histórico de cola con estado fallo.
- data/horarios.json: ventanas actuales, ventana de mediodía en prueba, 19:00 retirado y 23:30 fijo pero excluido por instrucción.
- scripts/registro_editorial.py: se leyó su lógica. Une rotacion.json, publicaciones.json, cola.json y storyboards de proyectos/, cola/entrada/, cola/ y salidas/, fusionando por project_id. No incluye cola/bloqueados/ ni los horarios diarios; estos dos inventarios se contrastaron por separado.
- No se afirma que scripts/registro_editorial.py se haya ejecutado: la vista combinada se reconstruyó leyendo el script y contrastando sus fuentes y storyboards desde GitHub.
- No se modificó ningún archivo data/*.json.

Se revisaron los títulos y términos de los storyboards de proyectos para evitar repetir temas ya propuestos. Ninguno de los cinco candidatos de este radar coincide con los temas registrados de abejas, Oedax, serpientes, corales, murciélagos, pardelas, anfibios, mosquitos, arqueas, Kromdraai, pulpos, ranas, ballena, nubes, ADN, robot en órbita, aprendizaje sabor-nutriente, etc. La coincidencia de línea amplia (Naturaleza/bichos) no se trata como duplicación temática.

## 3. RSS científicos — fallos exactos

Se consultaron las diez URLs declaradas en scripts/tendencias.py. La herramienta no pudo entregar los feeds XML/RSS. No se ejecutó el script ni se afirma haber parseado XML.

| Feed | URL | Resultado literal |
|---|---|---|
| ScienceDaily ciencia | https://www.sciencedaily.com/rss/top/science.xml | HTTP 400: Unsupported content-type: application/xml |
| ScienceDaily salud | https://www.sciencedaily.com/rss/top/health.xml | HTTP 400: Unsupported content-type: application/xml |
| ScienceDaily espacio | https://www.sciencedaily.com/rss/space_time.xml | HTTP 400: Unsupported content-type: application/xml |
| Phys.org | https://phys.org/rss-feed/ | HTTP 400: Unsupported content-type: text/xml |
| NASA | https://www.nasa.gov/news-release/feed/ | HTTP 400: Unsupported content-type: application/rss+xml |
| ESA | https://www.esa.int/rssfeed/Our_Activities/Space_Science | HTTP 404: Not Found |
| Nature | https://www.nature.com/nature.rss | HTTP 400: Unsupported content-type: application/rss+xml |
| EurekAlert | https://www.eurekalert.org/rss/news.xml | URL is not accessible via this tool |
| SINC | https://www.agenciasinc.es/rss | URL is not accessible via this tool |
| UNAM Global | https://unamglobal.unam.mx/feed/ | HTTP 400: Unsupported content-type: application/rss+xml |

Google Trends RSS México: https://trends.google.com/trending/rss?geo=MX  
Resultado literal: URL is not accessible via this tool.

Los candidatos se obtuvieron directamente de páginas primarias de editoriales científicas; no se presentan como resultado de una ingesta RSS.

## 4. Google Trends México — respaldo oficial

Se consultó Trending Now oficial para México, ventana Últimas 24 horas, a las 08:05 CDMX:

https://trends.google.com/trending?geo=MX&hl=es

**Observado:** 154 tendencias totales; 25 aparecen en la primera página. Entre las consultas visibles: “instituto del fondo nacional de la vivienda para los trabajadores” (100 mil+), “invierno” (5 mil+), “jorge duran” (10 mil+), “parabrisas” (5 mil+), “pumas - tigres uanl” (10 mil+), “guatemala” (5 mil+) y búsquedas de entretenimiento/deportes.

**Clasificación:** “invierno” es una señal estacional amplia, no una tendencia científica específica. En las primeras 25 entradas no se observa una consulta inequívoca de ciencia, naturaleza o comportamiento animal que respalde alguno de los cinco artículos.

**Inferencia:** Trends no aporta una razón para priorizar un candidato concreto. No se usa como evidencia científica ni se atribuye causalidad editorial a la tendencia.

## 5. Candidatos científicos — artículos publicados del 4 al 10 de noviembre

Ventana solicitada: últimos siete días, 4–11 nov inclusive. Los cinco candidatos son artículos primarios publicados dentro de la ventana. La fecha consignada es la fecha de publicación del artículo, no la fecha de una noticia secundaria.

**Estado general de DOI:** las páginas editoriales primarias consultadas muestran el DOI y la fecha de publicación. Sin embargo, las solicitudes directas a Crossref no fueron accesibles y los intentos con doi.org devolvieron HTTP 500 después de redirigir a la página editorial. Por tanto, ningún DOI se declara validado por Crossref/resolvedor: todos quedan como PENDIENTE_RESOLVEDOR. Las URLs primarias sí fueron abiertas y contrastadas con el resumen del artículo original.

### Candidato 1 — Los ayudantes de las ratas topo no hacen guardería: trabajan más

- **Fecha:** 10-nov-2026.
- **Líneas:** Actualidad; Naturaleza/bichos; Dato científico.
- **Novedad observada:** el estudio analiza aproximadamente 24,000 horas de observaciones de ratas topo de Damaraland cautivas (Fukomys damarensis) a lo largo de periodos reproductivos. Tras el nacimiento de las crías, los individuos no reproductores de ambos sexos y los machos reproductores redujeron el tiempo en el nido y aumentaron el esfuerzo de trabajo; las hembras reproductoras pasaron más tiempo en el nido y aumentaron su actividad de alimentación.
- **Fuente primaria:** Thorley et al., Behavioral Ecology, “Helpers at the nest? The activity patterns of Damaraland mole-rats across reproductive periods”. https://academic.oup.com/beheco/advance-article/doi/10.1093/beheco/arag140/9026235
- **DOI mostrado por el editor:** 10.1093/beheco/arag140 — PENDIENTE_RESOLVEDOR. https://doi.org/10.1093/beheco/arag140
- **Tendencia:** no observada en Google Trends México.
- **Relevancia científica:** alta. Distingue cuidado parental directo de cooperación mediante excavación y trabajo.
- **Oportunidad editorial:** muy alta. El giro es visual y causal: nacen las crías, pero los ayudantes no aumentan la permanencia en el nido; aumentan el trabajo que sostiene el acceso a recursos.
- **Público/ocasión:** público general interesado en animales sociales y comportamiento; sin fecha de calendario.
- **Riesgos:** no decir que “abandonan” a las crías ni que no ayudan. El artículo no encuentra evidencia de cuidado directo mediante mayor asistencia al nido por los no reproductores; propone que el mayor esfuerzo de trabajo puede apoyar a las hembras y facilitar el acceso a alimento cuando las crías salen del nido. La muestra es cautiva; no generalizar sin matices a todas las colonias silvestres.
- **Verificación:** página editorial primaria, fecha y abstract consultados; manuscrito aceptado, no versión final tipográfica. DOI pendiente de resolución independiente.

### Candidato 2 — Dos especies de ratones de Mindoro surgieron dentro de la misma isla

- **Fecha:** 06-nov-2026.
- **Líneas:** Actualidad; Naturaleza/bichos; Dato científico; biogeografía.
- **Novedad observada:** el artículo describe dos especies de Crunomys a partir de dos poblaciones de zonas montañosas de Mindoro. El trabajo de campo que produjo 40 especímenes ocurrió en 2013; los análisis morfológicos y genéticos (citocromo b y elementos ultraconservados) respaldan que son unidades distintas. El artículo estima divergencia respecto de parientes de la plataforma de Sunda hace unos 5.7 millones de años y especiación dentro de Mindoro hace unos 1.3 millones de años.
- **Fuente primaria:** Heaney et al., Journal of Mammalogy, “Two new Crunomys (Muridae): a second case of speciation within Mindoro, an oceanic Philippine island”. https://academic.oup.com/jmammal/advance-article/doi/10.1093/jmammal/gyag094/9011594
- **DOI mostrado por el editor:** 10.1093/jmammal/gyag094 — PENDIENTE_RESOLVEDOR. https://doi.org/10.1093/jmammal/gyag094
- **Tendencia:** no observada en Google Trends México.
- **Relevancia científica:** alta. Es un segundo caso de especiación de mamíferos dentro de Mindoro; junto con el caso previo de Apomys, los cuatro linajes adicionales representan 22% de los 18 mamíferos nativos no voladores actuales de la isla, según el artículo.
- **Oportunidad editorial:** alta, con dificultad media. El mapa de Mindoro y las dos zonas montañosas pueden explicar aislamiento y diversificación.
- **Público/ocasión:** curiosidad de biodiversidad, evolución e islas; sin fecha de calendario.
- **Riesgos:** no presentarlo como dos animales recién encontrados en una expedición de 2026. Los especímenes de campo son de 2013; lo reciente es la publicación. No decir que una isla “crea especies” por sí sola: la inferencia depende de morfología y genética. No inventar coordenadas de localidades montañosas que el abstract no proporciona.
- **Verificación:** página editorial primaria, fecha y abstract consultados; texto completo restringido. DOI pendiente de resolución independiente.

### Candidato 3 — Cabras de tres especies amamantan crías que no son suyas

- **Fecha:** 05-nov-2026.
- **Líneas:** Actualidad; Naturaleza/bichos; comportamiento animal.
- **Novedad observada:** el estudio documenta allonursing en tres especies de Capra (Western Tur, íbice siberiano y markhor). Durante cuatro años (2018–2021), se observaron 44 hembras y 81 crías en tres zoológicos. Se registraron 1,841 episodios de lactancia, 103 no filiales (5.6%), y 390 intentos de succión, 58 no filiales (14.9%). La frecuencia varió entre especies: el comportamiento fue más común en markhor (61.5% de hembras) y menos común en Western Tur (18.8%).
- **Fuente primaria:** Gloneková et al., Journal of Mammalogy, “Old goats: wise goats—allonursing in 3 caprine species”. https://academic.oup.com/jmammal/advance-article/doi/10.1093/jmammal/gyag090/9013689
- **DOI mostrado por el editor:** 10.1093/jmammal/gyag090 — PENDIENTE_RESOLVEDOR. https://doi.org/10.1093/jmammal/gyag090
- **Tendencia:** no observada en Google Trends México.
- **Relevancia científica:** media-alta. El artículo contrasta hipótesis sobre lactancia no filial; sus datos apoyan las hipótesis de evacuación de leche y crianza, pero no las de selección de parentesco ni robo de leche.
- **Oportunidad editorial:** alta por la anomalía comprensible: una hembra alimenta a una cría ajena. Puede explicarse sin atribuir altruismo humano.
- **Público/ocasión:** público general y curiosidad de comportamiento animal; sin fecha de calendario.
- **Riesgos:** muestra de zoológicos, no de poblaciones silvestres. No atribuir intención consciente ni afirmar una sola explicación universal; los autores describen motivaciones complejas y posibles diferencias por edad/experiencia.
- **Verificación:** página editorial primaria, fecha y abstract consultados; texto completo restringido. DOI pendiente de resolución independiente.

### Candidato 4 — Dos arañas comedoras de hormigas usan estrategias distintas para acercarse y evitar depredadores

- **Fecha:** 04-nov-2026.
- **Líneas:** Actualidad; Naturaleza/bichos; ecología y comportamiento.
- **Novedad observada:** dos especies hermanas de la península ibérica, Zodarion alacre y Z. andalusiacum, comen hormigas pero difieren en tamaño, coloración y actividad. Z. alacre caza hormigas mayores, es principalmente diurna y parece imitar a hormigas Messor en movimiento, color, forma y tamaño. Z. andalusiacum es principalmente nocturna, se parece al color de la arena y se mueve menos; los autores interpretan que probablemente usa camuflaje de fondo.
- **Fuente primaria:** Pekár e Ilgová, Behavioral Ecology, “Differentiation in ant-eating spiders based on offensive and defensive exploitation of ants”. https://academic.oup.com/beheco/advance-article/doi/10.1093/beheco/arag137/9011385
- **DOI mostrado por el editor:** 10.1093/beheco/arag137 — PENDIENTE_RESOLVEDOR. https://doi.org/10.1093/beheco/arag137
- **Tendencia:** no observada en Google Trends México.
- **Relevancia científica:** alta. El estudio compara dieta, actividad circadiana, similitud mimética y percepción visual de depredadores.
- **Oportunidad editorial:** muy alta por contraste visual entre imitación de hormiga y coincidencia con el sustrato.
- **Público/ocasión:** público general interesado en arañas, camuflaje y evolución; sin fecha de calendario.
- **Riesgos:** no decir que las arañas “se convierten” en hormigas ni que cambian de color. El artículo usa “parecen imitar” y “probablemente usan coincidencia con el fondo”; la hipótesis de diversificación por explotación ofensiva/defensiva es una interpretación de los autores, no una demostración de toda la historia evolutiva.
- **Verificación:** artículo primario abierto, fecha, DOI editorial y abstract consultados; acceso abierto. DOI pendiente de resolución independiente.

### Candidato 5 — En algunos peces, los machos que comen parte de la puesta pueden tener una ventaja reproductiva futura

- **Fecha:** 06-nov-2026.
- **Líneas:** Actualidad; Naturaleza/bichos; comportamiento y evolución.
- **Novedad observada:** un análisis comparativo de peces teleósteos encuentra que los machos sometidos a selección sexual más intensa —inferida a partir del dimorfismo de tamaño— consumen una proporción mayor de su descendencia. En especies con mayor riesgo de canibalismo paterno, las hembras muestran preferencia por desovar con machos que ya cuidan una puesta; añadir huevos a una puesta existente puede diluir el riesgo de que los huevos nuevos sean consumidos.
- **Fuente primaria:** Goldberg et al., Behavioral Ecology, “Patterns of filial cannibalism and mate choice in fishes point to sexual conflict over infanticide”. https://academic.oup.com/beheco/advance-article/doi/10.1093/beheco/arag136/9015820
- **DOI mostrado por el editor:** 10.1093/beheco/arag136 — PENDIENTE_RESOLVEDOR. https://doi.org/10.1093/beheco/arag136
- **Tendencia:** no observada en Google Trends México.
- **Relevancia científica:** alta. Compara explicaciones de canibalismo parcial de la puesta y estrategias reproductivas de hembras.
- **Oportunidad editorial:** media-alta; el giro puede ser potente, pero requiere explicar la comparación sin antropomorfismo.
- **Público/ocasión:** público general interesado en reproducción y comportamiento animal; sin fecha de calendario.
- **Riesgos:** no decir que todos los peces machos comen a sus crías ni atribuirles una intención consciente. El resultado es comparativo y la presión de selección sexual se infiere del dimorfismo de tamaño. No presentarlo como experimento causal ni como una regla para todos los peces.
- **Verificación:** página editorial primaria, fecha y abstract consultados; texto completo restringido. DOI pendiente de resolución independiente.

## 6. Recomendación editorial — sin staging

**Candidato principal para el próximo slot realmente libre y autorizado:** ratas topo de Damaraland.

Motivo: es el artículo más reciente (10-nov), tiene una pregunta narrativa clara y un giro respaldado por aproximadamente 24,000 horas de observación: los ayudantes reducen su tiempo en el nido y aumentan el trabajo. El cierre debe distinguir cooperación indirecta de cuidado parental directo. La limitación de cautividad debe estar en el relato, no relegada a una nota.

**Alternativa visual:** arañas Zodarion. El contraste entre imitación de hormiga y coincidencia con arena es más visual, pero el lenguaje debe conservar los matices “parece imitar” y “probablemente usa camuflaje de fondo”.

No se redactó narrative_contract ni storyboard porque no hay slot autorizado. No se seleccionó estilo del catálogo. No se generaron imágenes, frames, audio, video ni renders.

## 7. Seguimiento técnico Meta / Google Trends

Se comparó el corte anterior de docs/INVESTIGACION_API_META_Y_GOOGLE_TRENDS.md con las fuentes actuales.

**Cambio nuevo registrado:** Graph API v27.0 y Marketing API v27.0, anuncio fechado 4-nov-2026. El informe técnico existente se actualizó en la misma rama:

- Archivo: docs/INVESTIGACION_API_META_Y_GOOGLE_TRENDS.md
- Commit: 80c29b04c31c4e337c6c0bfa9cc397d991296213
- Se documentaron: campo opcional is_ai_generated para editar Page posts en v27; aviso de retirada de total_video_consumption_rate a principios de noviembre sin reemplazo directo (el tracker la marca Planned/Tentative, por lo que la fecha debe tratarse como tentativa); seis funciones legacy que las apps nuevas ya no pueden usar desde 4-nov y que no deben introducirse en integraciones nuevas.
- **Caveat:** el anuncio oficial de Meta y las referencias de Graph API/Instagram/Page Insights devolvieron HTTP 429. El cambio se registra con la URL del anuncio oficial y contraste de trackers/cobertura técnica independiente; no se implementa nada hasta poder revalidar directamente en Meta.
- Instagram Insights: no se encontró una métrica nueva posterior al corte 31-oct. El changelog incremental consultado muestra actualización 29-oct; el cambio 28-oct es de webhooks/handoff, no de Insights.
- Facebook Pages Insights: no se confirmó un cambio Page-specific nuevo; no confundir la retirada general de video insights con un reemplazo de Page Insights.
- Google Trends API: la documentación oficial sigue describiendo alfa de acceso limitado, ventana móvil de cinco años, agregaciones diaria/semanal/mensual/anual, regiones/subregiones y escala consistente. No se encontró cambio oficial nuevo.

Fuentes técnicas:
- Meta anuncio v27.0: https://developers.facebook.com/blog/post/2026/11/04/introducing-graph-api-v27-and-marketing-api-v27/
- Meta Graph API changelog: https://developers.facebook.com/docs/graph-api/changelog/
- Meta Instagram Platform changelog: https://developers.facebook.com/docs/instagram-platform/changelog/
- Meta Page Insights: https://developers.facebook.com/docs/platform/insights/reference/page-insights/
- Tracker Meta Graph API: https://adstackwatch.com/platforms/meta/
- Registro de Instagram Platform: https://releasebot.io/updates/meta/instagram-platform
- Google Trends API alfa: https://developers.google.com/search/apis/trends

## 8. Estado de QA narrativo preexistente — lectura exclusiva

Se revisó el storyboard canónico de cada proyecto con storyboard en proyectos/, y los registros únicos de salidas/, cola/entrada/ y cola/bloqueados/, deduplicando por project_id conforme a scripts/registro_editorial.py.

**Inventario:**
- proyectos/: 80 directorios; 67 storyboard.json presentes; 13 directorios sin storyboard.
- salidas/: 58 directorios; 8 project_id adicionales únicos sin narrative_qa; las demás copias se deduplicaron por project_id.
- cola/entrada/: dos proyectos; el robot en órbita es la misma copia/blob que el proyecto canónico y conserva PASS; el clavo de cocina no contiene narrative_qa.
- cola/bloqueados/: 44 entradas; 7 project_id adicionales únicos sin narrative_qa. La carpeta extra-nubes se deduplicó contra 2026-11-07_inter-nubes-pesan.
- Total de storyboards canónicos únicos revisados: 83.
- Con narrative_qa: 24 (8 PASS, 16 FAIL).
- Sin narrative_qa: 59 PENDIENTE_AUDITOR.
- Directorios de proyectos sin storyboard: 13; no se inventa QA para una carpeta sin storyboard.

### 8.1 QA existente — metadatos y critical_flags

review_basis es exactamente lectura_en_frio_solo_narracion en los 24 registros. AUSENTE_EN_JSON significa que el campo reviewed_at no existe en ese storyboard; no es una fecha inferida.

| project_id | status | score | review_basis | reviewed_at | critical_flags |
|---|---|---:|---|---|---|
| 2026-10-31_murcielagos-viroma-global | FAIL | 72 | lectura_en_frio_solo_narracion | AUSENTE_EN_JSON | [APERTURA_ESTATICA_Y_ESCENARIO_NO_DOCUMENTADO, TRANSICIONES_GENERICAS, CIFRA_300000_SIN_UNIDAD_DE_ANALISIS, GIRO_COMPARATIVO_NO_EXPLICADO] |
| 2026-10-31_sequias-energia-renovable | FAIL | 56 | lectura_en_frio_solo_narracion | AUSENTE_EN_JSON | [GANCHO_DEFINICIONAL, CIFRAS_SIN_DIRECCION_INTERPRETABLE, GIRO_SOLO_NOMBRADO, PAYOFF_NO_DERIVADO_DE_LA_EVIDENCIA] |
| 2026-11-01_dato-cambio-horario-corazon | FAIL | 84 | lectura_en_frio_solo_narracion | 2026-11-01T18:08:00-06:00 | [CIERRE_PRESELLO_INFERIOR_A_110_CARACTERES] |
| 2026-11-01_llorar-cebolla-quimica | FAIL | 79 | lectura_en_frio_solo_narracion | 2026-11-01T15:09:29-06:00 | [CIERRE_ATRIBUYE_INTENCION_EVOLUTIVA_NO_DEMOSTRADA, LIMITE_DE_EVIDENCIA_NO_EXPLICITO] |
| 2026-11-01_pulpo-tres-corazones | FAIL | 72 | lectura_en_frio_solo_narracion | 2026-11-01T15:09:29-06:00 | [APERTURA_HIPOTETICA_NO_IN_MEDIAS_RES, ANALOGIA_BRANQUIAS_SACAR_AIRE_DEL_AGUA_IMPRECISA, AFIRMACION_CORAZONES_NO_SUSTITUIBLES_SIN_RESPALDO] |
| 2026-11-01_red-electrica-pulso-minuto | PASS | 89 | lectura_en_frio_solo_narracion | 2026-11-01T15:09:29-06:00 | [] |
| 2026-11-02_camaron-mantis | PASS | 90 | lectura_en_frio_solo_narracion | AUSENTE_EN_JSON | [] |
| 2026-11-02_comida-pan-duro | FAIL | 84 | lectura_en_frio_solo_narracion | AUSENTE_EN_JSON | [CIERRE_SOBREAFIRMA_Y_CONTRADICE_LIMITE_DE_SECADO] |
| 2026-11-04_cielo-azul-atardecer-rojo | PASS | 94 | lectura_en_frio_solo_narracion | 2026-11-04T15:58:40-06:00 | [] |
| 2026-11-05_comida-palomitas | FAIL | 82 | lectura_en_frio_solo_narracion | 2026-11-10T15:47:50-06:00 | [APERTURA_DEFINICIONAL_NO_IN_MEDIAS_RES, ESCENA_6_REITERA_CAUSAS_DE_GRANOS_NO_REVENTADOS_SIN_INFORMACION_NUEVA] |
| 2026-11-05_inter-arboles-se-comunican | FAIL | 78 | lectura_en_frio_solo_narracion | 2026-11-10T15:47:50-06:00 | [APERTURA_GENERICA_NO_IN_MEDIAS_RES] |
| 2026-11-05_inter-rayo-globular | FAIL | 81 | lectura_en_frio_solo_narracion | 2026-11-10T15:47:50-06:00 | [APERTURA_HISTORICA_DESCRIPTIVA_NO_IN_MEDIAS_RES] |
| 2026-11-05_kids-dia-en-venus | PASS | 88 | lectura_en_frio_solo_narracion | 2026-11-10T15:47:50-06:00 | [] |
| 2026-11-06_comida-aguacate-negro | FAIL | 79 | lectura_en_frio_solo_narracion | 2026-11-10T15:47:50-06:00 | [REPETICION_ESCENAS_5_6_SIN_AVANCE_CAUSAL] |
| 2026-11-06_inter-arena-cantante | PASS | 94 | lectura_en_frio_solo_narracion | 2026-11-10T15:47:50-06:00 | [] |
| 2026-11-06_inter-ranas-congeladas | FAIL | 83 | lectura_en_frio_solo_narracion | 2026-11-10T15:47:50-06:00 | [REPETICION_ESCENAS_5_6_LIMITES_DE_ESPECIE_Y_CONDICIONES] |
| 2026-11-06_kids-ballena-azul-corazon | FAIL | 80 | lectura_en_frio_solo_narracion | 2026-11-10T15:47:50-06:00 | [PAYOFF_SOBREAFIRMA_CASI_SE_DETIENE] |
| 2026-11-07_comida-hielo-caliente | FAIL | 81 | lectura_en_frio_solo_narracion | 2026-11-10T15:47:50-06:00 | [APERTURA_DE_CREENCIAS_NO_IN_MEDIAS_RES] |
| 2026-11-07_inter-nubes-pesan | FAIL | 78 | lectura_en_frio_solo_narracion | 2026-11-10T15:47:50-06:00 | [ESCENA_7_REITERA_CIFRA_Y_LIMITE_SIN_PAYOFF_DE_SUSPENSION] |
| 2026-11-07_inter-pulpo-suenos | FAIL | 80 | lectura_en_frio_solo_narracion | 2026-11-10T15:47:50-06:00 | [REPETICION_ESCENAS_5_6_Y_PAYOFF_VAGO] |
| 2026-11-07_kids-huesos-bebe | FAIL | 82 | lectura_en_frio_solo_narracion | 2026-11-10T15:47:50-06:00 | [ESCENA_6_REPITE_VARIACION_DE_CONTEO_Y_FUSION] |
| 2026-11-09_dato-robot-ensambla-orbita | PASS | 90 | lectura_en_frio_solo_narracion | 2026-11-09T18:45:00-06:00 | [] |
| 2026-11-10_comida-aprendizaje-sabor-nutriente | PASS | 92 | lectura_en_frio_solo_narracion | 2026-11-10T15:47:50-06:00 | [] |
| 2026-11-10_dato-adn-sincroniza-flujo | PASS | 91 | lectura_en_frio_solo_narracion | 2026-11-10T16:16:00-06:00 | [] |

### 8.2 Los siete checks — valores exactos del JSON

Orden de columnas: pregunta_central_reconstruible; apertura_in_medias_res; progresion_por_escena; transiciones_causales; giro_cientifico_explicado; limite_evidencia_explicito; payoff_cierre_apertura.

| project_id | pregunta_central_reconstruible | apertura_in_medias_res | progresion_por_escena | transiciones_causales | giro_cientifico_explicado | limite_evidencia_explicito | payoff_cierre_apertura |
|---|---|---|---|---|---|---|---|
| 2026-10-31_murcielagos-viroma-global | true | false | true | false | false | true | true |
| 2026-10-31_sequias-energia-renovable | true | false | false | false | false | true | false |
| 2026-11-01_dato-cambio-horario-corazon | true | true | true | true | true | true | true |
| 2026-11-01_llorar-cebolla-quimica | true | true | true | true | true | false | false |
| 2026-11-01_pulpo-tres-corazones | true | false | true | true | true | false | true |
| 2026-11-01_red-electrica-pulso-minuto | true | true | true | true | true | true | true |
| 2026-11-02_camaron-mantis | true | true | true | true | true | true | true |
| 2026-11-02_comida-pan-duro | true | true | true | true | true | true | true |
| 2026-11-04_cielo-azul-atardecer-rojo | true | true | true | true | true | true | true |
| 2026-11-05_comida-palomitas | true | false | false | true | true | true | true |
| 2026-11-05_inter-arboles-se-comunican | true | false | true | true | true | true | true |
| 2026-11-05_inter-rayo-globular | true | false | true | true | true | true | true |
| 2026-11-05_kids-dia-en-venus | true | true | true | true | true | true | true |
| 2026-11-06_comida-aguacate-negro | true | true | false | false | true | true | true |
| 2026-11-06_inter-arena-cantante | true | true | true | true | true | true | true |
| 2026-11-06_inter-ranas-congeladas | true | true | false | false | true | true | true |
| 2026-11-06_kids-ballena-azul-corazon | true | true | true | true | true | true | false |
| 2026-11-07_comida-hielo-caliente | true | false | true | true | true | true | true |
| 2026-11-07_inter-nubes-pesan | true | true | false | false | true | true | false |
| 2026-11-07_inter-pulpo-suenos | true | true | false | false | true | true | false |
| 2026-11-07_kids-huesos-bebe | true | true | false | false | true | true | true |
| 2026-11-09_dato-robot-ensambla-orbita | true | true | true | true | true | true | true |
| 2026-11-10_comida-aprendizaje-sabor-nutriente | true | true | true | true | true | true | true |
| 2026-11-10_dato-adn-sincroniza-flujo | true | true | true | true | true | true | true |

### 8.3 PENDIENTE_AUDITOR — storyboards sin narrative_qa

No se encontró narrative_qa en los siguientes 59 storyboards únicos. Se conserva exactamente el estado PENDIENTE_AUDITOR; no se ejecutó QA ni se promovió ningún archivo.

**Proyectos (43):**

- 2026-10-24_abejas-bullying
- 2026-10-24_ideonella-pet
- 2026-10-24_osedax-comehuesos
- 2026-10-24_serpientes-que-ruedan
- 2026-10-25_ave-jurasica-sin-vuelo
- 2026-10-25_corales-contacto
- 2026-10-25_reina-olor
- 2026-10-25_sueno-electricidad-qom
- 2026-10-26_baffin-bay-ice-shelf
- 2026-10-26_catrina-posada-monerismo
- 2026-10-26_hongo-gente-diminuta
- 2026-10-26_papel-picado-dia-muertos
- 2026-10-26_papel-picado-dia-muertos_parte2
- 2026-10-26_pimiento-verde-rojo
- 2026-10-27_cempasuchil-ciencia
- 2026-10-27_corneja-decision-rapida
- 2026-10-27_ddm-parte3-pomuch
- 2026-10-27_familia-ajolote
- 2026-10-27_kids-serpiente-voladora
- 2026-10-27_noct-anfibio-marino
- 2026-10-28_ddm-parte4-templo-mayor
- 2026-10-28_familia-voyager-disco-oro
- 2026-10-28_kids-titanoboa
- 2026-10-28_monarca-almas
- 2026-10-28_mosquito-fruitless-audicion
- 2026-10-28_noct-lince-milanos
- 2026-10-28_pan-de-muerto-huesos
- 2026-10-29_juno-choque-proa
- 2026-10-29_muralismo-cu
- 2026-10-30_arqueas-origen-eucariotas
- 2026-10-30_kromdraai-primera-fecha
- 2026-10-31_pardelas-jetlag-solar
- 2026-10-31_smartpe-edicion-plantas
- 2026-11-03_dato-polvo-africano-microbios
- 2026-11-03_kids-leche-enchilado
- 2026-11-xx_kids-flamencos-rosas_RESPALDO
- demo-001
- guiones_lote_01
- lote01-01-el-nino
- lote01-02-petroleo
- lote01-03-balon-curva
- lote01-04-tardigrado
- lote01-05-chicxulub

**Salidas únicas (8):**

- 2026-10-24_aves-temen-mas-a-mujeres
- 2026-10-24_fenomeno-el-nino
- 2026-11-01_dato-xolo-mictlan
- 2026-11-03_kids-tiburon-groenlandia
- 2026-11-03_comida-maillard
- 2026-11-04_comida-miel-no-caduca
- 2026-11-04_inter-bioluminiscencia-mar
- 2026-11-04_kids-hipo-por-que

**Cola de entrada única (1):**

- 2026-11-07_dato-clavo-te-cocina

**Bloqueados únicos (7):**

- 2026-11-03_enzimas-incrustadas-oceano
- 2026-11-04_machu-picchu-fallas-pisa
- 2026-11-05_comida-palomitas-explotan
- 2026-11-05_inter-arboles-mito-respiran
- 2026-11-05_inter-venus-dia-largo
- 2026-11-06_inter-corazon-ballena-azul
- 2026-11-07_inter-mpemba-mito

### 8.4 Directorios sin storyboard

Se encontraron 13 directorios de proyectos sin storyboard.json. No se infiere QA para carpetas vacías ni se sustituyen por otros temas:

- 2026-10-29_machu-picchu-fallas-pisa
- 2026-xx_kids_camaron-mantis-punetazo
- 2026-xx_kids_pulpo-tres-corazones
- 2026-xx_kids_tiburon-groenlandia-400-anos
- 2026-xx_parking_curitiba-urbanismo
- 2026-xx_parking_herculano-papiros
- 2026-xx_parking_londres-gran-hedor
- 2026-xx_parking_quipus-incas
- 2026-xx_parking_te-chai-palabra
- 2026-xx_parking_tecuanillo-mar-devolvio
- 2026-xx_parking_teteles-observatorio-solar
- 2026-xx_parking_tren-mx-qro-arqueologia
- 2026-xx_parking_voyager-disco-oro

## 9. Cierre y límites de esta ejecución

- **NO_DUPLICAR:** no existe slot libre y autorizado el 11-nov; por eso no se crea storyboard.
- **Solo un archivo nuevo:** este radar. La regla normal de dos entregables no se fuerza cuando la guardia anti-duplicación prohíbe el storyboard.
- **Un archivo existente actualizado:** docs/INVESTIGACION_API_META_Y_GOOGLE_TRENDS.md, solo por el cambio relevante de Graph API v27.0.
- No se escribió narrative_qa, no se hizo QA narrativo, no se promovió ni movió material a cola/entrada.
- No se modificó main, workflows, motores canónicos, Motor U6 ni data/*.json.
- No se crearon medios, assets, renders ni archivos *_fuentes.md.
- No se publicó ni programó contenido.
- No se consumieron créditos de generación ni se usaron credenciales.
