# Radar CAPCOT — 8 de noviembre de 2026

**Repositorio:** marcojpad-hash/capcot-capsulas-imaginantes  
**Rama:** feature/capcot-video-discovery-continuity  
**Corte:** 2026-11-08, CDMX  
**Resultado operativo:** NO_DUPLICAR  
**Entregables de esta ejecución:** este brief. No se creó storyboard porque no existe un slot libre y autorizado para el 8-nov.

## 1. Decisión de cupo y guardia anti-duplicación

No hay un slot nuevo autorizado para producir hoy:

| Registro en data/horario_2026-11-08.json | Project ID | Fecha/slot del storyboard original | Estado del 8-nov | Tratamiento |
|---|---|---|---|---|
| 07:00 | 2026-11-05_comida-palomitas | 2026-11-05 / 13:30 | publicado_yt_tt_fb | Slot ocupado. Es una publicación de un proyecto preexistente, no un storyboard nuevo del 8-nov |
| 23:30 | 2026-11-07_dato-clavo-te-cocina | 2026-11-07 / 23:30 | programado_yt_tt | Excluido expresamente; no se usa como cupo ni se modifica |

El archivo horario fue actualizado a las 07:53 CDMX. No asigna slots 13:30, 17:00 ni 17:45 para hoy. La ventana 19:00 está retirada desde el 5-nov. En data/horarios.json, las ventanas generales de mediodía y tarde tampoco señalan el domingo como día preferente. Por tanto, no se interpreta una ventana general como autorización para inventar una asignación diaria.

Inventario de IDs con prefijo 2026-11-08: ninguno en proyectos/, salidas/, cola/entrada/ ni cola/bloqueados/. Los doce storyboards canónicos del lote 5–7 nov conservan fecha_objetivo y slot_local de esas fechas; ninguno corresponde al 8-nov.

La carpeta cola/entrada/2026-11-07_dato-clavo-te-cocina/ existe en el árbol actual y contiene storyboard.json, ESTADO_EJECUCION.md y fuentes.md. Su storyboard declara fecha_objetivo=2026-11-07 y slot_local=23:30; no tiene narrative_qa. Se conserva como material preexistente, fuera del cupo de hoy y sin intervención. El control de cola del 7-nov que describía cola/entrada/ como vacía quedó superado por este estado posterior del árbol.

**NO_DUPLICAR:** no se crea proyectos/2026-11-08_*/storyboard.json, no se promueve ni mueve nada a cola/entrada/, no se reescriben proyectos ajenos. Se crea únicamente el radar diario para dejar registro de la investigación y de la razón por la que no se produce storyboard.

## 2. Lectura de rotación y continuidad

Se leyeron data/temas_del_dia.json, data/rotacion.json, data/publicaciones.json y data/estilos_usados.json sin modificarlos:

- temas_del_dia.json llega hasta 2026-10-28; no contiene una entrada para 2026-11-08.
- rotacion.json contiene 27 registros y su último registro es del 2026-10-31.
- publicaciones.json contiene 22 registros y su último registro es del 2026-10-31.
- estilos_usados.json llega hasta 2026-10-28.

Se inspeccionó scripts/registro_editorial.py como vista combinada de rotación, publicaciones, cola, proyectos y salidas. Su lógica incorpora los storyboards de esas rutas, pero no incluye cola/bloqueados/ ni el horario diario específico. No se ejecutó el script porque no hay runtime local del repositorio en esta sesión; la conciliación se hizo leyendo las fuentes del árbol y el horario diario, y revisando bloqueados por separado. No se atribuyeron como publicadas las propuestas de proyectos/ ni las variantes bloqueadas.

Los storyboards del 5–7 nov consultados cubren Venus, palomitas, red micorrícica, rayo globular, corazón de ballena, aguacate negro, ranas congeladas, arena cantante, huesos de bebé, hielo caliente, sueños de pulpo y masa de nubes. Ninguno de los candidatos del radar repite esos temas. No se eligió estilo ni estructura porque no se creó storyboard y no existe un slot autorizado para asignarlos.

## 3. RSS científicos: resultado exacto de acceso

Se inspeccionaron las diez URLs definidas en scripts/tendencias.py. La herramienta de consulta web no admite la lectura directa de estos tipos XML/RSS en esta ejecución. Errores observados:

| Feed | URL | Resultado literal |
|---|---|---|
| ScienceDaily ciencia | https://www.sciencedaily.com/rss/top/science.xml | HTTP 400: Unsupported content-type application/xml |
| ScienceDaily salud | https://www.sciencedaily.com/rss/top/health.xml | HTTP 400: Unsupported content-type application/xml |
| ScienceDaily espacio | https://www.sciencedaily.com/rss/space_time.xml | HTTP 400: Unsupported content-type application/xml |
| Phys.org | https://phys.org/rss-feed/ | HTTP 400: Unsupported content-type text/xml |
| NASA | https://www.nasa.gov/news-release/feed/ | HTTP 400: Unsupported content-type application/rss+xml |
| ESA | https://www.esa.int/rssfeed/Our_Activities/Space_Science | HTTP 404: Not Found |
| Nature | https://www.nature.com/nature.rss | HTTP 400: Unsupported content-type application/rss+xml |
| EurekAlert | https://www.eurekalert.org/rss/news.xml | URL is not accessible via this tool |
| SINC | https://www.agenciasinc.es/rss | URL is not accessible via this tool |
| UNAM Global | https://unamglobal.unam.mx/feed/ | HTTP 400: Unsupported content-type application/rss+xml |

No se ejecutó scripts/tendencias.py ni se parseó XML. Los candidatos siguientes proceden de búsquedas y páginas editoriales/primarias accesibles; no se presentan como resultado de una ingesta RSS.

## 4. Google Trends México — respaldo oficial

El RSS público https://trends.google.com/trending/rss?geo=MX devolvió: URL is not accessible via this tool. Se usó como respaldo la página oficial Google Trends México, ventana “Últimas 24 horas”, consultada el 8-nov-2026: https://trends.google.com/trending?geo=MX&hl=es

**Observado en la página:** 255 tendencias en total, 25 visibles en la primera página. Predominan partidos de fútbol y entretenimiento. Entre los términos visibles aparecen “Japón” (2 mil+; con la consulta relacionada “terremoto Japón”), “tormenta” (2 mil+) y “aguacate” (2 mil+). “Aguacate” se solapa con el proyecto 2026-11-06_comida-aguacate-negro. “Japón” y “tormenta” no constituyen por sí solos una tendencia científica verificada. No se observó un término científico/natural claramente utilizable en las primeras 25 entradas.

**Lectura editorial:** Trends no aporta una señal científica que justifique forzar un tema. Se usa como contexto de atención, no como evidencia científica ni como causa de selección.

## 5. Candidatos científicos — publicaciones del 1 al 8 de noviembre

La tendencia, la relevancia científica y la oportunidad editorial se valoran por separado. Ningún candidato se presenta como tendencia de Google Trends.

### Candidato 1 — HCl sobre las fracturas de Alba Mons, Marte

- **Fecha del artículo:** 4-nov-2026 (Science Advances; el comunicado de ESA apareció el 5-nov).
- **Línea:** Actualidad; geología planetaria/espacio.
- **Novedad observada:** el equipo reporta detecciones de HCl durante la estación fría de afelio, localizadas en la región de Alba Mons, y fracturas frescas y estrechas (<1 m) que interpreta como posibles vías de salida de gas desde cuerpos magmáticos profundos.
- **Fuente primaria:** Trokhimovskiy et al., “Enigmatic HCl detections as a potential signature of igneous activity on Mars”, Science Advances. https://www.science.org/doi/10.1126/sciadv.aeb9422
- **Registro bibliográfico consultado:** PubMed PMID 42981399, con resumen y DOI: https://pubmed.ncbi.nlm.nih.gov/42981399/
- **Contraste oficial:** ESA, “European orbiter detects hints of volcanic activity on Mars”, 5-nov-2026: https://www.esa.int/ro/articles/news-media/news/european-orbiter-detects-hints-of-volcanic-activity-on-mars
- **DOI:** 10.1126/sciadv.aeb9422 — **PENDIENTE_RESOLVEDOR**. La página Science.org devolvió HTTP 403 y el resolvedor DOI no fue accesible en esta consulta. El título, la fecha y el resumen se contrastaron con el registro bibliográfico y el comunicado oficial de ESA; no se declara el DOI validado por resolvedor.
- **Público/ocasión:** curiosidad espacial general; no depende de un evento de calendario.
- **Tendencia:** no observada en las primeras 25 tendencias de México.
- **Relevancia científica:** alta; aporta una señal atmosférica localizada y una interpretación geológica comprobable con nuevas observaciones.
- **Oportunidad editorial:** alta; anomalía estacional, localización concreta y una pregunta narrativa clara.
- **Riesgos:** no afirmar que se observó una erupción; ESA indica que no se han observado nuevos flujos de lava ni erupciones. No convertir la hipótesis magmática en certeza. No afirmar que hay vida en Marte. Separar este patrón frío y localizado de las detecciones más extendidas de HCl de la estación cálida, atribuidas a procesos atmosféricos/aerosoles.
- **Ancla cartográfica posible si se autoriza un storyboard:** centro oficial USGS/IAU de Alba Mons: 41.08° N, 249.29° E, sistema planetocéntrico +East 0–360. https://planetarynames.wr.usgs.gov/Feature/14306. Ese punto ubica el volcán; no son coordenadas de las fracturas individuales. No simular precisión a nivel de fisura.
- **Verificación global:** resumen del artículo y comunicado oficial contrastados; DOI pendiente de resolución independiente.

### Candidato 2 — Una arquea terrestre crece bajo condiciones simuladas del subsuelo marciano

- **Fecha del artículo:** 5-nov-2026.
- **Línea:** Actualidad; dato científico/biología de extremófilos y astrobiología.
- **Novedad observada:** Haloferax volcanii mostró crecimiento y metabolismo activo durante 160 días a 24 mbar, en condiciones anóxicas enriquecidas con CO₂ y medio hipersalino con nitrato o perclorato. Se observaron biofilms y persistencia de señales carotenoides; la pérdida de líquido quedó por debajo del 4% en los tratamientos.
- **Fuente primaria completa:** Robinson et al., Applied and Environmental Microbiology. https://journals.asm.org/doi/full/10.1128/aem.01749-26
- **DOI:** 10.1128/aem.01749-26 — **VERIFICADO**: el resolvedor DOI redirigió a la página editorial ASM, y se leyó el artículo primario.
- **Público/ocasión:** curiosidad espacial y límites de la vida; sin ocasión de calendario.
- **Tendencia:** no observada en Trends México.
- **Relevancia científica:** alta; diferencia supervivencia de crecimiento y metabolismo activo bajo una combinación definida de condiciones.
- **Oportunidad editorial:** alta, aunque cercana temáticamente al candidato 1.
- **Riesgos:** no decir que se encontró vida en Marte. Es una arquea terrestre cultivada en laboratorio; el crecimiento fue menor que en los controles a presión terrestre. El medio nutritivo no reproduce toda la química marciana y el experimento no incluyó el conjunto completo de radiación ni ciclos de congelación/deshielo. No combinar con el candidato 1 como si ambos fueran una sola prueba o un mismo lugar.
- **Verificación global:** fuente primaria completa y DOI resuelto.

### Candidato 3 — Firmas moleculares de hemo en un hueso de dinosaurio de 115 millones de años

- **Fecha del artículo:** 2-nov-2026.
- **Línea:** Actualidad; paleontología.
- **Novedad observada:** el estudio informa tetrapirroles derivados del hemo en huesos de Aratasaurus museunacionali y señales localizadas en microestructuras elipsoidales dentro de canales vasculares, interpretadas como eritrocitos mineralizados. Se usaron HPLC-MS, Raman y microscopía electrónica de transmisión.
- **Fuente primaria:** Grice et al., PNAS. https://www.pnas.org/doi/10.1073/pnas.2614248123
- **DOI:** 10.1073/pnas.2614248123 — **VERIFICADO**: el resolvedor DOI redirigió al artículo oficial de PNAS; se leyó título, fecha y resumen.
- **Público/ocasión:** curiosidad sobre dinosaurios y conservación molecular; sin ocasión de calendario.
- **Tendencia:** no observada en Trends México.
- **Relevancia científica:** alta; aporta evidencia química y espacial a una discusión de larga duración sobre biomoléculas fósiles.
- **Oportunidad editorial:** alta; el contraste entre “hueso mineralizado” y “moléculas derivadas del hemo” ofrece un giro narrativo.
- **Riesgos:** no decir “sangre líquida intacta” ni que se recuperaron células vivas. Las microestructuras se interpretan como glóbulos rojos mineralizados; el hallazgo se refiere a firmas moleculares derivadas del hemo. La preservación de biomoléculas fósiles tiene antecedentes de debate sobre contaminación y diagénesis; el artículo argumenta origen endógeno mediante la diferencia entre la señal del hueso y la matriz circundante.
- **Verificación global:** artículo primario y DOI resueltos.

### Candidato 4 — El ruido antropogénico altera rasgos de animales en la mayoría de las especies estudiadas

- **Fecha del artículo:** 5-nov-2026.
- **Línea:** Actualidad; Naturaleza/bichos y ecología.
- **Novedad observada:** metaanálisis filogenético de 214 estudios experimentales y 177 especies acuáticas y terrestres, distribuidas en seis continentes. En el 80% de las especies estudiadas, el ruido afectó al menos un rasgo fisiológico, de desarrollo o de conducta.
- **Fuente primaria:** Kunc y Schmidt, “Echoes of the Anthropocene: Noise pollution as a global threat”, Science. https://www.science.org/doi/10.1126/science.adu9593
- **Contraste secundario consultado:** Phys.org, 6-nov-2026: https://phys.org/news/2026-11-noise-pollution-biology-behavior-animal.html
- **DOI:** 10.1126/science.adu9593 — **PENDIENTE_RESOLVEDOR_Y_ARTICULO_PRIMARIO**. Science.org devolvió HTTP 403; el DOI y la fecha aparecen en los registros bibliográficos consultados y el resumen se contrastó con la cobertura de Phys.org, pero no se declara validación por resolvedor ni lectura del artículo primario completo.
- **Público/ocasión:** público general interesado en fauna, sonido y vida cotidiana; sin ocasión de calendario.
- **Tendencia:** no observada en Trends México.
- **Relevancia científica:** alta; sintetiza evidencia experimental a escala multiespecie.
- **Oportunidad editorial:** media-alta; permite conectar sonido cotidiano y conducta animal, pero exige un ejemplo concreto respaldado por el artículo.
- **Riesgos:** “80%” significa 80% de las especies incluidas, no 80% de todas las especies del planeta. Las respuestas no fueron uniformemente negativas; hay ganadores y perdedores ecológicos. No afirmar que todo ruido produce el mismo efecto ni generalizar a cualquier hábitat.
- **Verificación global:** pendiente de acceso al artículo primario y resolución independiente del DOI; no usar como fuente final de storyboard hasta completar ambos.

### Candidato 5 — Una cavidad de ondas de materia reproduce dinámicas análogas a horizontes de evento

- **Fecha del artículo:** 4-nov-2026.
- **Línea:** Actualidad; dato científico/física.
- **Novedad observada:** el equipo confinó una onda de materia con dispersión cuasirrelativista entre barreras de luz, moviendo periódicamente una de ellas. Observó trayectorias fijas brillantes y oscuras predichas por el modelo.
- **Fuente primaria:** Tanlimco et al., Physical Review Letters. https://journals.aps.org/prl/abstract/10.1103/44mq-jfp1
- **DOI:** 10.1103/44mq-jfp1 — **PENDIENTE_RESOLVEDOR**; la página editorial APS es accesible y muestra DOI, resumen y fecha, pero el resolvedor DOI no respondió en esta consulta.
- **Público/ocasión:** público curioso por física y analogías con agujeros negros; sin ocasión de calendario.
- **Tendencia:** no observada en Trends México.
- **Relevancia científica:** alta; realiza experimentalmente una plataforma de dinámica de cavidad en régimen de conducción ultrastrong.
- **Oportunidad editorial:** media; el símil visual con un horizonte de evento es potente, pero el mecanismo es abstracto.
- **Riesgos:** no decir que se creó un agujero negro, que se observó un horizonte astrofísico real ni que la luz se comportó literalmente como en un agujero negro. Es un sistema análogo con ondas de materia y barreras ópticas.
- **Verificación global:** fuente primaria editorial accesible; DOI pendiente de resolución independiente.

## 6. Recomendación editorial — no ejecutada

**Candidato principal para el próximo slot que sí esté asignado:** HCl localizado sobre Alba Mons (candidato 1).

Motivos: alta narrabilidad, anomalía estacional, geografía concreta y un límite científico fácil de explicar sin exagerar. La apertura posible parte de una detección fuera de la pauta estacional esperada; el giro es la coincidencia espacial con fracturas frescas; el límite es que no se observó una erupción y el origen magmático sigue siendo una interpretación. La cartografía solo puede señalar el centro de Alba Mons como referencia regional, no las fracturas individuales.

Antes de redactar el storyboard, resolver el DOI o dejar asentado que la URL editorial es la referencia primaria definitiva. El candidato 2 queda como alternativa separada para otro día; no mezclar ambos estudios como si demostraran lo mismo. El candidato 3 es la alternativa más fuerte de paleontología, pero exige precisión terminológica. Los candidatos 4 y 5 requieren una traducción narrativa más cuidadosa.

**Decisión de esta ejecución:** NO_DUPLICAR. La recomendación no se convierte en storyboard porque no hay slot libre y autorizado el 8-nov.

## 7. Seguimiento técnico: Meta y Google Trends

Se comparó el estado del documento docs/INVESTIGACION_API_META_Y_GOOGLE_TRENDS.md con la documentación oficial consultable:

- Google Trends API: https://developers.google.com/search/apis/trends. La página sigue ofreciendo acceso alfa limitado por solicitud, ventana móvil de cinco años, agregaciones diaria/semanal/mensual/anual y desglose geográfico. El blog oficial no muestra un anuncio nuevo de apertura general o cambio de especificación posterior al estado documentado.
- Meta Graph API changelog: https://developers.facebook.com/docs/graph-api/changelog — HTTP 429 en esta consulta.
- Instagram Platform changelog: https://developers.facebook.com/docs/instagram-platform/changelog — HTTP 429.
- Facebook Pages API y Page Insights: las referencias oficiales consultadas no fueron accesibles (429 o URL no accesible).

**Resultado:** no se identificó un cambio nuevo de Meta respaldado directamente por documentación oficial. No se actualiza ni reescribe docs/INVESTIGACION_API_META_Y_GOOGLE_TRENDS.md. La imposibilidad de recuperar las páginas oficiales de Meta queda registrada como límite de verificación, no como prueba de que no existan cambios.

## 8. Estado de narrative_qa preexistente — lectura directa de los JSON

Se releyeron los doce storyboards canónicos de proyectos/ del lote 5–7 nov. En todos, review_basis es exactamente lectura_en_frio_solo_narracion y reviewed_at es exactamente 2026-11-07T15:45:21-06:00. El orden de las siete claves de checks que sigue es el del JSON: pregunta_central_reconstruible, apertura_in_medias_res, progresion_por_escena, transiciones_causales, giro_cientifico_explicado, limite_evidencia_explicito, payoff_cierre_apertura.

| project_id | fecha_objetivo / slot_local | status / score | review_basis | reviewed_at | checks, en orden exacto | critical_flags |
|---|---|---|---|---|---|---|
| 2026-11-05_kids-dia-en-venus | 2026-11-05 / 07:00 | PASS / 88 | lectura_en_frio_solo_narracion | 2026-11-07T15:45:21-06:00 | [true,true,true,true,true,true,true] | [] |
| 2026-11-05_comida-palomitas | 2026-11-05 / 13:30 | FAIL / 82 | lectura_en_frio_solo_narracion | 2026-11-07T15:45:21-06:00 | [true,false,false,true,true,true,true] | ["APERTURA_DEFINICIONAL_NO_IN_MEDIAS_RES","ESCENA_6_REITERA_CAUSAS_DE_GRANOS_NO_REVENTADOS_SIN_INFORMACION_NUEVA"] |
| 2026-11-05_inter-arboles-se-comunican | 2026-11-05 / 17:00 | FAIL / 78 | lectura_en_frio_solo_narracion | 2026-11-07T15:45:21-06:00 | [true,false,true,true,true,true,true] | ["APERTURA_GENERICA_NO_IN_MEDIAS_RES"] |
| 2026-11-05_inter-rayo-globular | 2026-11-05 / 17:45 | FAIL / 81 | lectura_en_frio_solo_narracion | 2026-11-07T15:45:21-06:00 | [true,false,true,true,true,true,true] | ["APERTURA_HISTORICA_DESCRIPTIVA_NO_IN_MEDIAS_RES"] |
| 2026-11-06_kids-ballena-azul-corazon | 2026-11-06 / 07:00 | FAIL / 80 | lectura_en_frio_solo_narracion | 2026-11-07T15:45:21-06:00 | [true,true,true,true,true,true,false] | ["PAYOFF_SOBREAFIRMA_CASI_SE_DETIENE"] |
| 2026-11-06_comida-aguacate-negro | 2026-11-06 / 13:30 | FAIL / 79 | lectura_en_frio_solo_narracion | 2026-11-07T15:45:21-06:00 | [true,true,false,false,true,true,true] | ["REPETICION_ESCENAS_5_6_SIN_AVANCE_CAUSAL"] |
| 2026-11-06_inter-ranas-congeladas | 2026-11-06 / 17:00 | FAIL / 83 | lectura_en_frio_solo_narracion | 2026-11-07T15:45:21-06:00 | [true,true,false,false,true,true,true] | ["REPETICION_ESCENAS_5_6_LIMITES_DE_ESPECIE_Y_CONDICIONES"] |
| 2026-11-06_inter-arena-cantante | 2026-11-06 / 17:45 | PASS / 94 | lectura_en_frio_solo_narracion | 2026-11-07T15:45:21-06:00 | [true,true,true,true,true,true,true] | [] |
| 2026-11-07_kids-huesos-bebe | 2026-11-07 / 07:00 | FAIL / 82 | lectura_en_frio_solo_narracion | 2026-11-07T15:45:21-06:00 | [true,true,false,false,true,true,true] | ["ESCENA_6_REPITE_VARIACION_DE_CONTEO_Y_FUSION"] |
| 2026-11-07_comida-hielo-caliente | 2026-11-07 / 13:30 | FAIL / 81 | lectura_en_frio_solo_narracion | 2026-11-07T15:45:21-06:00 | [true,false,true,true,true,true,true] | ["APERTURA_DE_CREENCIAS_NO_IN_MEDIAS_RES"] |
| 2026-11-07_inter-pulpo-suenos | 2026-11-07 / 17:00 | FAIL / 80 | lectura_en_frio_solo_narracion | 2026-11-07T15:45:21-06:00 | [true,true,false,false,true,true,false] | ["REPETICION_ESCENAS_5_6_Y_PAYOFF_VAGO"] |
| 2026-11-07_inter-nubes-pesan | 2026-11-07 / 17:45 | FAIL / 78 | lectura_en_frio_solo_narracion | 2026-11-07T15:45:21-06:00 | [true,true,false,false,true,true,false] | ["ESCENA_7_REITERA_CIFRA_Y_LIMITE_SIN_PAYOFF_DE_SUSPENSION"] |

Balance literal de los doce JSON: 2 PASS y 10 FAIL. No se ejecutó una nueva evaluación narrativa ni se modificó ningún objeto narrative_qa.

Otros storyboards consultados:
- cola/entrada/2026-11-07_dato-clavo-te-cocina/storyboard.json: no contiene narrative_qa → PENDIENTE_AUDITOR. Su fecha_objetivo es 2026-11-07 y slot_local es 23:30.
- salidas/2026-11-04_inter-bioluminiscencia-mar/storyboard.json: no contiene narrative_qa → PENDIENTE_AUDITOR.
- salidas/2026-11-04_kids-hipo-por-que/storyboard.json: no contiene narrative_qa → PENDIENTE_AUDITOR.
- salidas/2026-11-04_comida-miel-no-caduca/storyboard.json: no contiene narrative_qa → PENDIENTE_AUDITOR.

## 9. Límites y acciones de esta ejecución

- Se creó únicamente docs/briefs/2026-11-08_RADAR_CAPCOT.md para registrar investigación y NO_DUPLICAR.
- No se creó storyboard porque no hay slot libre y autorizado. No se creó un project_id sin asignación.
- No se escribió en cola/entrada/ ni en cola/bloqueados/.
- No se creó archivo *_fuentes.md; las fuentes y estados de verificación están dentro de este brief.
- No se escribió narrative_qa, no se ejecutó QA narrativo, no se promovió ningún proyecto y no se declaró aceptación de Grok.
- No se generaron imágenes, frames, voz, audio, video ni renders.
- No se publicó ni programó contenido. No se consumieron créditos.
- No se modificaron data/*.json, main, workflows, motores ni motor U6.
