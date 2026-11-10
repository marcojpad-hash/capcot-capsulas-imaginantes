# Radar CAPCOT — 10 de noviembre de 2026

**Repositorio:** marcojpad-hash/capcot-capsulas-imaginantes  
**Rama:** feature/capcot-video-discovery-continuity  
**Corte de investigación:** 2026-11-10, 08:57 America/Mexico_City  
**Resultado operativo:** NO_DUPLICAR  
**Entregable de esta ejecución:** este brief. No se crea storyboard porque no hay un slot nuevo libre y autorizado.

## 1. Decisión de cupo y guardia anti-duplicación

Se leyó el horario diario vigente, data/horario_2026-11-10.json, actualizado a las 07:26:41 CDMX.

| Slot | Registro del día | Estado observado | Tratamiento |
|---|---|---|---|
| 07:00 | 2026-11-06_comida-aguacate-negro | publicado_yt_tt; Facebook conserva el estado programado del lote anterior | Ocupado. No crear otro proyecto ni atribuir una nueva publicación a este investigador |
| 13:30 | Sin asignación en el horario diario | No hay proyecto ni paquete asignado | No se interpreta como autorización |
| 17:00 | capsaicina-resub | programado_yt_tt; resub aprobado, aún no publicado al corte | Ocupado. No duplicar ni intervenir |
| 19:00 | Sin asignación en el horario diario | No hay proyecto ni paquete asignado | No se interpreta como autorización |
| 23:30 | dato_del_dia | sin_paquete | Excluido expresamente por la instrucción vigente |

Los cinco slots existen como capacidad general del código, pero el horario diario no asigna 13:30 ni 19:00. La ventana 23:30 está excluida. No se inventa una asignación a partir de la capacidad global.

Guardia de rutas para la fecha 2026-11-10:

- proyectos/: 78 entradas de primer nivel; ninguna contiene el prefijo 2026-11-10.
- salidas/: 58 entradas de primer nivel; ninguna contiene el prefijo 2026-11-10.
- cola/entrada/: 3 entradas; ninguna contiene el prefijo 2026-11-10.
- cola/bloqueados/: 44 entradas; ninguna contiene el prefijo 2026-11-10.
- El radar 2026-11-10_RADAR_CAPCOT.md no existía antes de esta escritura.
- El paquete de robot en órbita del 9-nov existe tanto en proyectos como en cola/entrada; ambas rutas apuntan al mismo blob SHA fac47f592abdb6f6ea129bd242095da287a53595. Se conserva como material preexistente, no se vuelve a crear.

**NO_DUPLICAR:** no hay un slot libre y autorizado. Se crea únicamente el radar faltante. No se crea proyectos/2026-11-10_*/storyboard.json, no se copia nada a cola/entrada y no se modifica material ajeno.

## 2. Rotación, memoria editorial y continuidad

Se leyeron data/temas_del_dia.json, data/rotacion.json, data/publicaciones.json, data/estilos_usados.json y data/tendencias_estilos.json. No se modificó ningún archivo data/*.json.

Estado de los registros canónicos:

- temas_del_dia.json llega hasta 2026-10-28.
- rotacion.json contiene 27 registros y llega hasta 2026-10-31.
- publicaciones.json contiene 22 registros y llega hasta 2026-10-31.
- estilos_usados.json llega hasta 2026-10-28.
- tendencias_estilos.json tiene corte 2026-10-31.

Se leyó scripts/registro_editorial.py. Su lógica combina rotacion.json, publicaciones.json, cola.json y storyboards de proyectos/, cola/entrada/ y salidas/, fusionando por project_id. No incluye cola/bloqueados/ ni los horarios diarios; por eso se contrastó por separado el inventario de bloqueados y data/horario_2026-11-10.json. No se afirma que el script se haya ejecutado: la vista combinada se reconstruyó mediante lectura de GitHub siguiendo su lógica.

Los candidatos de este radar no repiten literalmente los temas canónicos del lote 5–7 nov ni el radar del 9-nov. Se aplican además estas reservas de rotación:

- Se detectó el proyecto 2026-10-31_murcielagos-viroma-global en proyectos y salidas. El artículo nuevo sobre diversidad críptica de murciélagos neotropicales del 3-nov es científicamente distinto (taxonomía y conservación, no viroma), pero se deja fuera de los cinco candidatos para evitar repetir el mismo taxón con solo diez días de distancia.
- Drosophila tiene proximidad temática con los proyectos previos de abejas y mosquito. Se conserva como candidato secundario, no como recomendación principal.
- El candidato de aprendizaje sabor-nutriente tiene proximidad con la cesta comida y con aguacate, palomitas, hielo caliente y capsaicina. Se conserva por su mecanismo neurocientífico, pero no se prioriza mientras esa cesta esté tan reciente.
- Los dos candidatos de clima-geo son distintos: uno trata el balance radiativo superficial después de incendios; el otro, la retirada repetida del sector del mar de Amundsen durante interglaciares. No se presentan como un mismo fenómeno.

No se elige estilo ni estructura: al no existir slot autorizado, no se redacta storyboard. Por tanto, no se asigna ni repite un style_id en esta ejecución.

## 3. RSS científicos: resultado exacto de acceso

Se consultaron las diez URLs declaradas en scripts/tendencias.py. La herramienta de consulta no admite o no pudo recuperar estos RSS/XML. Errores exactos observados:

| Feed | URL | Resultado literal |
|---|---|---|
| ScienceDaily ciencia | https://www.sciencedaily.com/rss/top/science.xml | HTTP 400: Unsupported content-type: application/xml |
| ScienceDaily salud | https://www.sciencedaily.com/rss/top/health.xml | HTTP 400: Unsupported content-type: application/xml |
| ScienceDaily espacio | https://www.sciencedaily.com/rss/space_time.xml | HTTP 400: Unsupported content-type: application/xml |
| Phys.org | https://phys.org/rss-feed | HTTP 400: Unsupported content-type: text/xml |
| NASA | https://www.nasa.gov/news-release/feed | HTTP 400: Unsupported content-type: application/rss+xml |
| ESA | https://www.esa.int/rssfeed/Our_Activities/Space_Science | HTTP 404: Not Found |
| Nature | https://www.nature.com/nature.rss | HTTP 400: Unsupported content-type: application/rss+xml |
| EurekAlert | https://www.eurekalert.org/rss/news.xml | URL is not accessible via this tool |
| SINC | https://www.agenciasinc.es/rss | URL is not accessible via this tool |
| UNAM Global | https://unamglobal.unam.mx/feed | HTTP 400: Unsupported content-type: application/rss+xml |

El RSS de Google Trends México, https://trends.google.com/trending/rss?geo=MX, devolvió: URL is not accessible via this tool.

No se ejecutó scripts/tendencias.py ni se obtuvo ni parseó XML. Los candidatos de este radar proceden de páginas primarias de editoriales científicas y sus registros bibliográficos; no se presentan como resultado de una ingesta RSS.

## 4. Google Trends México — respaldo oficial

Se consultó la página oficial Google Trends México, ventana «Últimas 24 horas», el 10-nov-2026:
https://trends.google.com/trending?geo=MX&hl=es

**Observado:** 154 tendencias totales; 25 visibles en la primera página. Predominan búsquedas de actualidad general, entretenimiento, finanzas, deportes y asuntos locales. Entre las consultas visibles aparecen «aguinaldo claudia sheinbaum» (20 mil+), «año escolar» (10 mil+), «finanzas» (10 mil+), «glucemia» (5 mil+) y «hoy» (5 mil+). «Frente frío» aparece como consulta relacionada dentro del desglose de «hoy», no como una tendencia independiente visible.

**Lectura editorial:** «glucemia» es una señal de interés de salud, pero no identifica por sí sola una noticia científica concreta ni una línea médica aprobada. No se observó en las primeras 25 entradas una tendencia científica o natural inequívoca que justifique elegir uno de los estudios siguientes.

Ninguno de los cinco candidatos se presenta como tendencia de Google Trends. Trends se usa como contexto de atención, no como evidencia científica ni como causa de selección.

## 5. Candidatos científicos — publicaciones del 3 al 9 de noviembre

La fecha corresponde a la publicación del artículo primario, no a la fecha en que una nota secundaria lo volvió a difundir. La tendencia, la relevancia científica y la oportunidad editorial se valoran por separado. Todas las afirmaciones siguientes se limitan a lo que el artículo primario permite sostener.

### Candidato 1 — ADN que organiza un flujo en oscilaciones milimétricas

- **Fecha del artículo:** 9-nov-2026.
- **Línea:** Actualidad; Dato científico; ampliación de física/biomateriales.
- **Novedad observada:** un fluido activo de microtúbulos y motores de kinesina estira y enreda polímeros de ADN. El ADN forma una red viscoelástica que retroalimenta el flujo: el sistema pasa de turbulencia desordenada a oscilaciones sincronizadas de escala milimétrica. El trabajo informa un período característico de 25 ± 9 minutos y una longitud de correlación que alcanza aproximadamente 1.5 mm en el canal experimental.
- **Fuente primaria:** Levanon et al., Nature Physics, “Active-flow-driven DNA remodelling generates millimetre-scale mechanical oscillations”. https://www.nature.com/articles/s41567-026-03505-y
- **DOI mostrado por el editor:** 10.1038/s41567-026-03505-y — PENDIENTE_RESOLVEDOR. La página editorial muestra DOI y fecha; la consulta directa a Crossref y al resolvedor DOI no fue accesible en esta ejecución.
- **Tendencia:** no observada en Trends México.
- **Relevancia científica:** alta; muestra una transición de dinámica colectiva causada por retroalimentación mecánica entre actividad molecular y una red polimérica emergente.
- **Oportunidad editorial:** alta, con dificultad de traducción media-alta. Tiene un giro visual y causal claro: un flujo desordenado adquiere coordinación cuando el ADN forma una red que transmite esfuerzos.
- **Público/ocasión:** curiosidad de física, materiales y biología molecular; sin fecha de calendario.
- **Riesgos:** no decir que el ADN «se mueve solo», que esto ocurre dentro de una célula o que se descubrió un mecanismo biológico natural. Es un material compuesto construido en laboratorio con ADN, microtúbulos y kinesina. Las oscilaciones corresponden al flujo del sistema, no a una molécula individual. Los 25 ± 9 minutos y los 1.5 mm pertenecen a las condiciones experimentales descritas; no son constantes universales.
- **Verificación:** resumen, resultados y metadatos del artículo primario consultados; DOI pendiente de resolución independiente.

### Candidato 2 — El sector del mar de Amundsen perdió hielo repetidamente en antiguos períodos cálidos

- **Fecha del artículo:** 9-nov-2026.
- **Línea:** Actualidad; ampliación clima-geo/atmósfera.
- **Novedad observada:** el estudio analiza sedimentos del margen continental antártico que conservan señales de los últimos 800,000 años. Durante períodos interglaciares anteriores, el aporte de detritos glacigénicos procedentes de los principales glaciares del sector del mar de Amundsen cesó casi por completo. Los autores interpretan ese cambio de procedencia como evidencia de desanclaje y fuerte retroceso de las cuencas de drenaje de ese sector; relacionan el patrón con la entrada de aguas oceánicas profundas más cálidas.
- **Fuente primaria:** Hillenbrand et al., Nature Communications, “Repeated loss of the West Antarctic Ice Sheet’s Amundsen Sea sector during late Pleistocene interglacials”. https://www.nature.com/articles/s41467-026-77004-2
- **DOI mostrado por el editor:** 10.1038/s41467-026-77004-2 — PENDIENTE_RESOLVEDOR. Crossref y el resolvedor DOI no fueron accesibles.
- **Tendencia:** no observada en Trends México.
- **Relevancia científica:** alta; aporta evidencia sedimentaria directa sobre la respuesta pasada del sector del mar de Amundsen a condiciones cálidas.
- **Oportunidad editorial:** alta; el cambio de señal en los sedimentos permite construir un giro científico concreto y conectar océano, hielo y nivel del mar.
- **Público/ocasión:** público general interesado en clima y geología; sin fecha de calendario.
- **Riesgos:** no decir que colapsó toda la capa de hielo de la Antártida occidental. El estudio documenta el sector del mar de Amundsen y no determina por sí solo la extensión completa de la retirada de toda la capa. El aporte de al menos ~1.5 m al nivel medio global del mar es una interpretación de la contribución de la pérdida de hielo estudiada, no una predicción exacta para una fecha futura. Distinguir evidencia sedimentaria, reconstrucción paleoclimática y proyección.
- **Verificación:** artículo primario y resumen completo consultados; DOI pendiente de resolución independiente.

### Candidato 3 — Los incendios no cambian igual el balance radiativo de todos los ecosistemas

- **Fecha del artículo:** 4-nov-2026.
- **Línea:** Actualidad; ampliación clima-geo/atmósfera.
- **Novedad observada:** usando observaciones satelitales de incendios durante 2001–2020, el estudio encuentra respuestas distintas según el ecosistema. Después del fuego, bosques de hoja ancha y pastizales pueden aclararse porque el suelo expuesto y el rebrote vegetal superan el oscurecimiento por residuos carbonosos. En bosques de coníferas, matorrales y sabanas, la superficie puede oscurecerse y absorber más radiación de onda corta, mientras las pérdidas de onda larga asociadas al calentamiento siguen dominando el balance radiativo neto descrito por los autores.
- **Fuente primaria:** Lu et al., npj Climate and Atmospheric Science, “Responses of surface radiative balance to wildfires differ across ecosystems”. https://www.nature.com/articles/s41612-026-01589-0
- **DOI mostrado por el editor:** 10.1038/s41612-026-01589-0 — PENDIENTE_RESOLVEDOR. La página editorial muestra DOI, fecha y resumen; Crossref y el resolvedor DOI no fueron accesibles.
- **Tendencia:** no observada en Trends México.
- **Relevancia científica:** alta; utiliza dos décadas de observaciones satelitales para mostrar que el efecto radiativo superficial posterior a incendios depende del ecosistema.
- **Oportunidad editorial:** media-alta; contradice una explicación demasiado simple de «suelo quemado = superficie más oscura» y permite un giro por comparación de ecosistemas.
- **Público/ocasión:** público interesado en clima, incendios y naturaleza; sin fecha de calendario.
- **Riesgos:** no afirmar que los incendios enfrían el planeta. El resultado trata del balance radiativo de la superficie en ecosistemas y condiciones analizados; no equivale al balance climático global ni incluye por sí solo todos los efectos de humo, carbono, aerosoles y emisiones. No extrapolar la respuesta de un ecosistema a todos los incendios.
- **Verificación:** resumen y metadatos de la fuente editorial primaria consultados; DOI pendiente de resolución independiente.

### Candidato 4 — El olor del alimento coordina el cortejo de una especie de mosca

- **Fecha del artículo:** 4-nov-2026.
- **Línea:** Actualidad; Naturaleza/bichos; Dato científico.
- **Novedad observada:** en Drosophila erecta, los compuestos volátiles del alimento favorecen la agregación y activan el cortejo de los machos. El movimiento visual generado por las interacciones del grupo refuerza después esa activación, formando un circuito multisensorial que coordina el cortejo en el parche de alimento. La dependencia estricta del olor alimentario no aparece igual en D. melanogaster, especie comparada por el estudio.
- **Fuente primaria:** Brand et al., Nature, “Ecological and social cues orchestrate concerted courtship in Drosophila”. https://www.nature.com/articles/s41586-026-11209-9
- **DOI mostrado por el editor:** 10.1038/s41586-026-11209-9 — PENDIENTE_RESOLVEDOR. El enlace corto de resolución hcq7bk redirigió a la ruta correcta del artículo Nature, pero el destino devolvió una redirección a idp.nature.com y error 500; no se considera una resolución completa.
- **Tendencia:** no observada en Trends México.
- **Relevancia científica:** alta; conecta señales ecológicas, movimiento grupal y circuitos sensoriales en una conducta reproductiva.
- **Oportunidad editorial:** alta; el mecanismo puede narrarse como una secuencia causal visible: olor, agregación, movimiento y retroalimentación.
- **Público/ocasión:** público general interesado en insectos y comportamiento animal; sin fecha de calendario.
- **Riesgos:** no generalizar a todas las moscas ni a todos los insectos. El hallazgo se refiere a D. erecta y a las condiciones del estudio; la comparación con D. melanogaster muestra precisamente que la dependencia del olor es específica. No antropomorfizar ni equiparar la conducta con atracción humana. Tiene proximidad temática con los proyectos previos de abejas y mosquito, por lo que no es la primera opción de rotación.
- **Verificación:** resumen, fecha y DOI del artículo primario consultados en el resultado editorial; DOI pendiente de resolución independiente.

### Candidato 5 — El cerebro aprende qué sabores anuncian nutrientes

- **Fecha del artículo:** 4-nov-2026.
- **Línea:** Actualidad; Dato científico. La comida es el contexto cotidiano, no una línea temática nueva.
- **Novedad observada:** el estudio identifica una vía dopaminérgica que participa en el aprendizaje de asociaciones entre sabor y nutrientes posteriores a la ingestión. En ratones, las neuronas dopaminérgicas del área tegmental ventral son necesarias para asociar nutrientes con sabores; los nutrientes ingeridos desencadenan liberación de dopamina preferentemente en una región de la amígdala basolateral anterior izquierda. El artículo también informa activación preferente de esa estructura por nutrientes en humanos.
- **Fuente primaria:** Grove et al., Nature, “The neural basis of flavour–nutrient learning”. https://www.nature.com/articles/s41586-026-11229-5
- **DOI mostrado por el editor:** 10.1038/s41586-026-11229-5 — PENDIENTE_RESOLVEDOR. Crossref y el resolvedor DOI no fueron accesibles.
- **Tendencia:** no observada en Trends México.
- **Relevancia científica:** alta; propone un mecanismo neural para integrar la señal sensorial del sabor con la información nutritiva que llega después desde el intestino.
- **Oportunidad editorial:** media-alta; permite explicar por qué el cerebro aprende asociaciones entre sabor y valor nutritivo. Tiene riesgo de saturación por la cercanía de varias cápsulas de la cesta comida.
- **Público/ocasión:** público general interesado en comida, cerebro y aprendizaje; sin fecha de calendario.
- **Riesgos:** el estudio no demuestra directamente por qué las personas aprenden a amar el café amargo ni es un ensayo de preferencia por café. No decir que el café por sí mismo «libera dopamina» ni que se probó una conducta humana concreta. La evidencia causal descrita incluye experimentos en ratones; la activación de una región en humanos no equivale por sí sola a demostrar el mismo aprendizaje conductual.
- **Verificación:** resumen y metadatos del artículo primario consultados; DOI pendiente de resolución independiente.

## 6. Candidato principal recomendado — no ejecutado

**Recomendación para el próximo slot que sea asignado expresamente:** remodelación mecánica de ADN en un fluido activo.

Motivos:
1. Es el candidato más novedoso respecto de la rotación reciente; no repite el tema de un paquete del 5–9 nov.
2. Tiene una pregunta única y un giro verificable: cómo un flujo desordenado puede adquirir coordinación de escala milimétrica mediante una red de ADN que emerge dentro del propio material.
3. Permite explicar un mecanismo, no solo mostrar una cifra: microtúbulos y kinesina generan el flujo; el flujo estira y enreda el ADN; la red almacena y transmite esfuerzos; la retroalimentación organiza oscilaciones.
4. La evidencia primaria permite expresar el límite con claridad: es un compuesto experimental construido en laboratorio, no una célula ni una función genética natural.

**Límite que debe sostener cualquier futura narración:** el ADN no es el motor ni oscila de forma autónoma. La actividad la generan microtúbulos y motores de kinesina; el ADN reorganizado forma la red mecánica que retroalimenta el flujo. Los resultados dependen de longitud de polímero, concentración, geometría y actividad del sistema experimental.

La recomendación no es una decisión editorial final de Grok. No se asignan título, arco, estilo, mapa ni storyboard porque no existe slot libre y autorizado el 10-nov.

## 7. DOI y verificación bibliográfica

Se intentó verificar cada DOI con Crossref y el resolvedor DOI:

- Las cinco consultas a https://api.crossref.org/works/{DOI} devolvieron «URL is not accessible via this tool».
- Las consultas directas a https://doi.org/{DOI} tampoco completaron la resolución en esta ejecución.
- Para Drosophila, el enlace corto https://doi.org/hcq7bk reveló la ruta de destino Nature correcta, pero el destino fue bloqueado por la redirección de identidad de Nature; por prudencia también se conserva como PENDIENTE_RESOLVEDOR.
- Las páginas editoriales primarias consultadas muestran título, fecha de publicación, DOI y resumen. Eso permite contrastar las afirmaciones resumidas, pero no sustituye la resolución independiente exigida.

**Resultado:** los cinco DOI permanecen PENDIENTE_RESOLVEDOR. Ninguno se declara VERIFICADO_CROSSREF ni VERIFICADO_RESOLVEDOR. Los URLs de los artículos primarios sí fueron consultados y se conservan como fuente principal.

## 8. Seguimiento técnico: Meta Graph API, Insights y Google Trends API

Se comparó el estado de docs/INVESTIGACION_API_META_Y_GOOGLE_TRENDS.md con documentación y changelogs oficiales accesibles el 10-nov-2026.

| Referencia oficial | Resultado |
|---|---|
| Meta Graph API changelog | HTTP 429: Too Many Requests |
| Instagram Platform changelog | HTTP 429: Too Many Requests |
| Facebook Pages API | HTTP 429: Too Many Requests |
| Facebook Page Insights reference | URL is not accessible via this tool |
| Google Trends API alpha | Accesible; continúa descrita como alfa de acceso limitado |

La documentación oficial actual de Google mantiene:

- Ventana móvil de cinco años.
- Agregaciones diaria, semanal, mensual y anual.
- Desgloses por país, región y subregión.
- Datos escalados de forma consistente para comparar solicitudes; no son volúmenes absolutos de búsqueda.
- Acceso alfa limitado; Google todavía no la abre a todos los proyectos.

Fuentes oficiales:
- Google Trends API: https://developers.google.com/search/apis/trends
- Anuncio de Google Trends API alpha: https://developers.google.com/search/blog/2025/07/trends-api
- Meta Graph API changelog: https://developers.facebook.com/docs/graph-api/changelog
- Instagram Platform changelog: https://developers.facebook.com/docs/instagram-platform/changelog
- Facebook Pages API: https://developers.facebook.com/docs/pages-api/
- Page Insights: https://developers.facebook.com/docs/platform/insights/

No se encontró un cambio nuevo de Meta sustentado por una referencia oficial accesible. La página de Google Trends conserva las capacidades ya documentadas en el informe del repositorio. La actualización de Google Search Central del 9-nov sobre consultas «things to do» corresponde a otros documentos de Search y no modifica la especificación de Trends API.

**Resultado:** no se actualiza ni reescribe docs/INVESTIGACION_API_META_Y_GOOGLE_TRENDS.md. Los errores de Meta se registran como límite de verificación, no como prueba de que no haya cambios.

## 9. Estado de narrative_qa preexistente — lectura directa de los JSON

Se releen desde GitHub los doce storyboards canónicos del lote 5–7 nov y el proyecto del robot en órbita del 9-nov. No se ejecutó una nueva lectura narrativa ni se modificó ningún campo de QA.

Para los doce storyboards canónicos 5–7 nov, los valores exactos compartidos por los JSON son:

- review_basis: lectura_en_frio_solo_narracion
- reviewer_role: auditor_capcot_independiente
- reviewed_at: 2026-11-09T15:53:26-06:00
- Orden de los siete checks en cada vector: pregunta_central_reconstruible, apertura_in_medias_res, progresion_por_escena, transiciones_causales, giro_cientifico_explicado, limite_evidencia_explicito, payoff_cierre_apertura.

| project_id | fecha_objetivo / slot_local | status / score | checks en el orden exacto del JSON | critical_flags |
|---|---|---|---|---|
| 2026-11-05_kids-dia-en-venus | 2026-11-05 / 07:00 | PASS / 88 | [true,true,true,true,true,true,true] | [] |
| 2026-11-05_comida-palomitas | 2026-11-05 / 13:30 | FAIL / 82 | [true,false,false,true,true,true,true] | ["APERTURA_DEFINICIONAL_NO_IN_MEDIAS_RES","ESCENA_6_REITERA_CAUSAS_DE_GRANOS_NO_REVENTADOS_SIN_INFORMACION_NUEVA"] |
| 2026-11-05_inter-arboles-se-comunican | 2026-11-05 / 17:00 | FAIL / 78 | [true,false,true,true,true,true,true] | ["APERTURA_GENERICA_NO_IN_MEDIAS_RES"] |
| 2026-11-05_inter-rayo-globular | 2026-11-05 / 17:45 | FAIL / 81 | [true,false,true,true,true,true,true] | ["APERTURA_HISTORICA_DESCRIPTIVA_NO_IN_MEDIAS_RES"] |
| 2026-11-06_kids-ballena-azul-corazon | 2026-11-06 / 07:00 | FAIL / 80 | [true,true,true,true,true,true,false] | ["PAYOFF_SOBREAFIRMA_CASI_SE_DETIENE"] |
| 2026-11-06_comida-aguacate-negro | 2026-11-06 / 13:30 | FAIL / 79 | [true,true,false,false,true,true,true] | ["REPETICION_ESCENAS_5_6_SIN_AVANCE_CAUSAL"] |
| 2026-11-06_inter-ranas-congeladas | 2026-11-06 / 17:00 | FAIL / 83 | [true,true,false,false,true,true,true] | ["REPETICION_ESCENAS_5_6_LIMITES_DE_ESPECIE_Y_CONDICIONES"] |
| 2026-11-06_inter-arena-cantante | 2026-11-06 / 17:45 | PASS / 94 | [true,true,true,true,true,true,true] | [] |
| 2026-11-07_kids-huesos-bebe | 2026-11-07 / 07:00 | FAIL / 82 | [true,true,false,false,true,true,true] | ["ESCENA_6_REPITE_VARIACION_DE_CONTEO_Y_FUSION"] |
| 2026-11-07_comida-hielo-caliente | 2026-11-07 / 13:30 | FAIL / 81 | [true,false,true,true,true,true,true] | ["APERTURA_DE_CREENCIAS_NO_IN_MEDIAS_RES"] |
| 2026-11-07_inter-pulpo-suenos | 2026-11-07 / 17:00 | FAIL / 80 | [true,true,false,false,true,true,false] | ["REPETICION_ESCENAS_5_6_Y_PAYOFF_VAGO"] |
| 2026-11-07_inter-nubes-pesan | 2026-11-07 / 17:45 | FAIL / 78 | [true,true,false,false,true,true,false] | ["ESCENA_7_REITERA_CIFRA_Y_LIMITE_SIN_PAYOFF_DE_SUSPENSION"] |

El proyecto 2026-11-09_dato-robot-ensambla-orbita tiene un registro de QA distinto:

- status: PASS
- score: 90
- review_basis: lectura_en_frio_solo_narracion
- reviewer_role: auditor_capcot_independiente
- reviewed_at: 2026-11-09T18:45:00-06:00
- checks: {"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}
- critical_flags: []

El storyboard de robot en proyectos/ y su copia en cola/entrada/ tienen el mismo blob SHA fac47f592abdb6f6ea129bd242095da287a53595. El archivo cola/estado/2026-11-09_dato-robot-ensambla-orbita.json no existe (404), por lo que la recepción por Grok no está confirmada. No se infiere recepción por la existencia de la copia en cola.

Otros storyboards recientes leídos:

| project_id | Ruta canónica leída | Estado de narrative_qa |
|---|---|---|
| 2026-11-07_dato-clavo-te-cocina | cola/entrada/2026-11-07_dato-clavo-te-cocina/storyboard.json | PENDIENTE_AUDITOR; el campo narrative_qa no existe |
| 2026-11-04_inter-bioluminiscencia-mar | salidas/2026-11-04_inter-bioluminiscencia-mar/storyboard.json | PENDIENTE_AUDITOR; el campo narrative_qa no existe |
| 2026-11-04_kids-hipo-por-que | salidas/2026-11-04_kids-hipo-por-que/storyboard.json | PENDIENTE_AUDITOR; el campo narrative_qa no existe |
| 2026-11-04_comida-miel-no-caduca | salidas/2026-11-04_comida-miel-no-caduca/storyboard.json | PENDIENTE_AUDITOR; el campo narrative_qa no existe |

Balance de los doce canónicos 5–7 nov: 2 PASS y 10 FAIL. El robot del 9-nov añade 1 PASS. Los cuatro storyboards recientes de la tabla anterior no tienen narrative_qa y se reportan PENDIENTE_AUDITOR. No se altera ninguno.

## 10. Integridad y límites de esta ejecución

- Se crea únicamente docs/briefs/2026-11-10_RADAR_CAPCOT.md.
- No se crea storyboard porque no existe slot libre y autorizado.
- No se escribe ni modifica cola/entrada/, cola/bloqueados/, proyectos/ ni salidas/.
- No se crea archivo *_fuentes.md; las fuentes de investigación están en este brief porque no hay storyboard.
- No se escribe ni modifica narrative_qa.
- No se generan frames, imágenes, audio, voz, video ni renders.
- No se publica ni programa contenido.
- No se modifican data/*.json, main, workflows, permisos, secretos, motores canónicos ni Motor U6.
- No se consumen créditos.
- No se actualiza el informe técnico Meta/Google porque no se identificó un cambio nuevo sustentado directamente por documentación oficial.

**Conclusión:** radar guardado; NO_DUPLICAR por ausencia de slot nuevo autorizado. La recomendación principal queda disponible para el próximo slot que sea asignado expresamente; no constituye decisión editorial final de Grok.
