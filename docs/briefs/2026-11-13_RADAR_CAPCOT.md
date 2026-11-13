# RADAR CAPCOT — 2026-11-13

**Corte:** 13-nov-2026, America/Mexico_City.  
**Rama:** feature/capcot-video-discovery-continuity.  
**Rol:** investigación y preproducción textual; no selección editorial final, producción audiovisual ni publicación.

## 1. Guardias, rotación y disponibilidad

Se leyeron los documentos operativos obligatorios en el orden establecido, los datos editoriales, el catálogo de estilos, la plantilla vertical, el registro editorial y los briefs/storyboards recientes. La lectura de scripts/registro_editorial.py se usó para reconciliar registros por project_id; la revisión de storyboards se hizo directamente contra GitHub, sin modificar data/*.json.

- Antes de esta ejecución no había project_id ni storyboard con fecha_objetivo 2026-11-13 en proyectos/, salidas/, cola/entrada/ ni cola/bloqueados/. Se comprobó el contenido de fecha_objetivo y slot_local, no solo el prefijo del directorio.
- data/temas_del_dia.json, data/rotacion.json y data/publicaciones.json no contienen registro del 13-nov.
- El horario vigente conserva las ventanas 06:30–07:30 y 16:30–18:00. Viernes no figura entre los días preferentes de la tarde, pero la ventana no lo prohíbe. Se usa 17:00 como slot_local de staging, dentro de la ventana activa; no es hora de publicación ni programación.
- 19:00 está retirado; 13:30 es una franja de prueba no activa en el horario vigente; 23:30 permanece excluido.
- El estilo más reciente fue collage_cientifico_vintage (12-nov); el 11-nov fue linograbado. El borrador de hoy usa dibujo_cientifico_scratchboard, no repetido en los storyboards recientes. La estructura historia no repite la estructura del 12-nov (pregunta). La cama pizzicato no repite las dos últimas camas conocidas (arpegio y pulso).

**Inventario anti-duplicación:** 151 archivos storyboard.json leídos en las cuatro rutas y reconciliados por project_id. El corte anterior tenía 83 project_id únicos; se añadieron desde entonces el proyecto de ratas topo del 11-nov y el proyecto de chimpancés del 12-nov. Resultado preexistente: 85 project_id únicos, 25 con narrative_qa y 60 PENDIENTE_AUDITOR; 13 directorios de proyectos no tienen storyboard. No se encontró duplicado temático de caracoles fósiles con embriones, microplásticos en tapires/osos hormigueros, meiofauna de nódulos ni recetas moleculares de momificación de cocodrilos.

## 2. RSS científicos y Google Trends México

### RSS

Se consultaron los URL definidos en scripts/tendencias.py. Ningún RSS se declaró leído ni se afirmó haber parseado XML. Fallos observados:

| Feed | Resultado |
|---|---|
| ScienceDaily Science | HTTP 400 — Unsupported content-type: application/rss+xml |
| ScienceDaily Salud | HTTP 400 — Unsupported content-type: application/rss+xml |
| ScienceDaily Espacio | HTTP 400 — Unsupported content-type: application/rss+xml |
| Phys.org | HTTP 400 — Unsupported content-type: text/xml |
| NASA News Release | HTTP 400 — Unsupported content-type: application/rss+xml |
| ESA Space Science | HTTP 404 — Not Found |
| Nature RSS | HTTP 400 — Unsupported content-type: application/rss+xml |
| EurekAlert | URL no accesible mediante la herramienta de lectura |
| SINC | URL no accesible mediante la herramienta de lectura |
| UNAM Global | HTTP 400 — Unsupported content-type: application/rss+xml |
| Google Trends RSS México | URL no accesible mediante la herramienta de lectura |

No se inventaron títulos ni fechas a partir de esos feeds. Se pasó al respaldo oficial de Trending Now.

### Trending Now oficial

URL consultada: https://trends.google.com/trending?geo=MX&hl=es

- La página oficial abrió y mostró 235 tendencias; se revisó el conjunto visible de las primeras 25.
- La mayoría de las tendencias visibles correspondía a deportes, entretenimiento, tecnología, política y búsquedas generales.
- 1998 KY26 fue la señal de ciencia/espacio más clara: 2 mil+ búsquedas, aumento de 700% y actividad aproximada de 10 horas al momento de consulta.
- La tendencia no valida ninguna hipótesis científica. La cobertura viral mezcla el estudio térmico del asteroide con la especulación no confirmada de que podría ser una sonda soviética perdida. Esa especulación no se recomienda para CAPCOT.
- No se detectó una tendencia científica/natural mexicana amplia que deba desplazar la relevancia del estudio primario seleccionado.

## 3. Candidatos publicados del 6 al 13 de noviembre

La fecha de publicación se tomó de la página editorial o del registro primario visible. Los cuatro DOI aparecen en los metadatos editoriales, pero Crossref y el resolvedor DOI no completaron una validación independiente en esta ejecución. Se marcan PENDIENTE_RESOLVEDOR; no se presentan como DOI validados. Las páginas de Nature devolvieron redirección a idp.nature.com y error HTTP 500 al abrirse directamente; el índice editorial sí mostró título, fecha, resumen y datos del artículo.

### Candidato A — caracoles fósiles con embriones internos

- **Fecha / autoría / revista:** 10-nov-2026; Taro Yoshimura et al.; Communications Biology 9, artículo 1450.
- **Estudio original:** “Exceptional preservation reveals the deep-time reproductive ecology and trophic breadth of Early Cretaceous viviparid gastropods”.
- **DOI editorial mostrado, pendiente de resolver:** 10.1038/s42003-026-11188-7.
- **URL editorial:** https://www.nature.com/articles/s42003-026-11188-7
- **Novedad observada:** conjunto de caracoles de agua dulce de la Formación Kitadani, Japón, de unos 120 Ma. El artículo informa 313 especímenes examinados; 240 con embriones; tras excluir 45 con un solo embrión, 195 individuos con varios embriones; media de 6.78 en ese subconjunto; máximo de 16 en una concha de 19.4 mm. El gradiente de tamaño axial dentro de la concha materna apoya ovoviviparidad obligada. Residuos gastrointestinales indican raspado de microalgas, alimentación por suspensión y detritivoría.
- **Tendencia:** sin señal específica visible en Trends México.
- **Relevancia científica:** evidencia fósil directa de estrategias reproductivas y alimentarias en gasterópodos del Cretácico temprano.
- **Oportunidad editorial:** muy alta; una tomografía revela embriones dentro de una concha y permite un arco de anomalía → patrón → interpretación → límite de preservación.
- **Público/ocasión:** público general; ventana de tarde.
- **Riesgos:** 16 es el máximo de un individuo, no el promedio; 6.78 corresponde a 195 individuos con más de un embrión; la ceniza alcalina como amortiguador de acidez es una hipótesis tafonómica de los autores, no una causa observada directamente.
- **Verificación:** resumen y metadatos editoriales visibles; DOI PENDIENTE_RESOLVEDOR.

### Candidato B — microplásticos en tapires y osos hormigueros

- **Fecha / autoría / revista:** 11-nov-2026; Ferraz et al.; Nature.
- **Estudio original:** “Human land use drives microplastic abundance in terrestrial wildlife”.
- **DOI editorial mostrado, pendiente de resolver:** 10.1038/s41586-026-11285-x.
- **URL editorial:** https://www.nature.com/articles/s41586-026-11285-x
- **Novedad observada:** el estudio combinó mediciones in vivo de microplásticos en sangre con seguimiento de alta resolución de tapires de tierras bajas y osos hormigueros gigantes en Brasil. En 47 animales se identificaron 17,165 partículas con HQI>75; 2,815 (16.4%) se identificaron como microplásticos. El artículo dice que aparecieron en todos menos cuatro animales; 43/47 es el cálculo derivado de esa frase, no una cifra independiente. Cuarenta animales tenían datos GPS suficientes para el análisis de uso del hábitat. Las cargas se asociaron con mayor exposición a huella humana y proximidad a desarrollo e infraestructura de residuos; también se detectaron partículas en animales de hábitats aparentemente prístinos.
- **Tendencia:** sin señal específica visible en Trends México.
- **Relevancia científica:** alta; conecta movimiento individual, uso del paisaje y exposición sistémica a microplásticos.
- **Oportunidad editorial:** alta; fauna carismática y una paradoja visual —exposición incluso en hábitats remotos—.
- **Público/ocasión:** público general interesado en fauna y ambiente.
- **Riesgos:** asociación observacional, no causalidad; no se identifica una fuente única ni la ruta de cada partícula; no afirmar que una instalación concreta causó la exposición.
- **Verificación:** resumen y resultados del artículo editorial visibles; DOI PENDIENTE_RESOLVEDOR.

### Candidato C — microfauna en grietas de nódulos polimetálicos

- **Fecha / autoría / revista:** 11-nov-2026; Diaz-Recio Lorenzo et al.; Scientific Reports.
- **Estudio original:** “Polymetallic nodules provide a distinct habitat for abyssal meiofauna”.
- **DOI editorial mostrado, pendiente de resolver:** 10.1038/s41598-026-76737-w.
- **URL editorial:** https://www.nature.com/articles/s41598-026-76737-w
- **Novedad observada:** estudio de nódulos de la zona Clarion-Clipperton del Pacífico central. Las grietas albergan comunidades de meiofauna dominadas por nematodos y copépodos, distintas de las de sedimentos cercanos. Las abundancias de nematodos y copépodos en grietas equivalieron aproximadamente al 10% y 25% de las registradas en sedimentos cercanos, respectivamente. El análisis incluyó 244 nódulos para relaciones de volumen y abundancia; el propio artículo advierte que siguen siendo una muestra pequeña frente a la extensión total de la CCZ.
- **Tendencia:** sin señal específica visible en Trends México.
- **Relevancia científica:** alta; describe un microhábitat bentónico poco caracterizado y un posible impacto de la extracción de nódulos.
- **Oportunidad editorial:** media-alta; revelar un ecosistema diminuto escondido en grietas de rocas del fondo abisal.
- **Público/ocasión:** público interesado en océano, biodiversidad y geología.
- **Riesgos:** no afirmar que el estudio inventarió toda la biodiversidad de la CCZ; no convertir el riesgo potencial de minería en un daño ya ocurrido; las abundancias son comparaciones entre tipos de muestra y áreas concretas.
- **Verificación:** resumen y resultados del artículo editorial visibles; DOI PENDIENTE_RESOLVEDOR.

### Candidato D — química de momificación de cocodrilos

- **Fecha / autoría / revista:** 11-nov-2026; Tabea J. Koch, Emma Phillips, Marie Vandenbeusch et al.; Scientific Reports.
- **Estudio original:** “Biomolecular evidence reveals site-specific embalming recipes for ancient Egyptian crocodiles”.
- **DOI editorial mostrado, pendiente de resolver:** 10.1038/s41598-026-80426-z.
- **URL editorial:** https://www.nature.com/articles/s41598-026-80426-z
- **Novedad observada:** análisis por cromatografía de gases-espectrometría de masas de siete momias de cocodrilo de periodos tardío a grecorromano. Se identificaron distintas combinaciones de cera de abeja, resina/alquitrán de pino y alquitrán de cedro. Al integrar datos anteriores, los autores observan una receta consistente en Kom Ombo durante varios siglos.
- **Tendencia:** sin señal específica visible en Trends México.
- **Relevancia científica:** alta para arqueometría y química orgánica.
- **Oportunidad editorial:** media; la receta molecular de una momia animal permite mostrar cómo se identifican materiales invisibles a simple vista.
- **Público/ocasión:** público adulto interesado en química y arqueología.
- **Riesgos:** muestra de siete momias; no generalizar a todo Egipto ni a todas las prácticas; evitar afirmaciones religiosas o sociales que el análisis químico no demuestra.
- **Verificación:** resumen, metadatos, autoría, fecha y DOI visibles en la página editorial; DOI PENDIENTE_RESOLVEDOR.

### Candidato E — asteroide 1998 KY26 y estabilidad de hielo

- **Fecha / autoría / repositorio:** 06-nov-2026; Korbin Hansen y Masatoshi Hirabayashi; arXiv.
- **Preprint original:** “Thermally unfavorable conditions of volatile existence in near-Earth asteroid 1998 KY26, the Hayabusa extended mission's target”.
- **Identificador:** arXiv:2611.10275; no se muestra DOI.
- **URL primaria:** https://arxiv.org/abs/2611.10275
- **Novedad observada:** modelado térmico en 13 caracterizaciones del asteroide; los autores concluyen que las temperaturas medias calculadas superan los umbrales de sublimación de volátiles y que el flujo de agua no permitiría mantener hielo enterrado. Es un preprint, no un artículo revisado por pares.
- **Tendencia:** 1998 KY26 fue la señal de ciencia/espacio más visible en Trending Now México: 2 mil+ búsquedas y +700%.
- **Relevancia científica:** moderada; contribuye a evaluar una explicación de la aceleración no gravitacional del objeto.
- **Oportunidad editorial:** alta por tendencia, pero subordinada a la cautela científica.
- **Público/ocasión:** público de espacio y astronomía.
- **Riesgos:** preprint sin revisión por pares; no presentar como hecho la especulación viral de que el asteroide sería una sonda soviética perdida; no afirmar que el misterio está resuelto.
- **Verificación:** registro primario de arXiv visible; enlace verificado, sin DOI y sin revisión por pares.

## 4. Recomendación editorial y staging

**Candidato principal recomendado:** A — caracoles fósiles con embriones internos.

La recomendación se basa en relevancia científica y oportunidad narrativa, no en tendencia. La primera escena puede abrir con la tomografía revelando los embriones; el gradiente axial explica el giro reproductivo; los residuos digestivos añaden ecología; la ceniza alcalina cierra con un mecanismo de preservación expresamente inferido.

### Separación epistemológica del candidato principal

- **Observado en el estudio:** 313 especímenes examinados; 240 con embriones; 195 individuos con más de un embrión tras excluir 45 con uno; media 6.78 en ese subconjunto; máximo 16 embriones en una concha de 19.4 mm; gradiente de tamaños; residuos gastrointestinales.
- **Cálculo:** 313 − 240 no se usa para inferir una tasa biológica; 16 es el máximo de un individuo. La media 6.78 no se atribuye a los 313 especímenes, sino al subconjunto de 195 con más de un embrión.
- **Inferencia de los autores:** el gradiente apoya ovoviviparidad obligada; la ceniza alcalina de paleoincendios habría amortiguado la acidez y reducido la disolución de carbonato. Esta segunda explicación es tafonómica y debe narrarse como propuesta, no como observación.
- **Recomendación:** mantener el foco en el máximo de 16 y el gradiente; no convertir el máximo en promedio ni la hipótesis de ceniza en causa demostrada.

### Borrador creado

- Archivo: proyectos/2026-11-13_dato-caracol-16-embriones/storyboard.json
- Commit real: e10ecc27c1694c79e3135e4ba12ef083be101279
- Lectura posterior desde GitHub: JSON parseado; 210 palabras de narración; 8 escenas; 78 segundos de escenas + 6 de cortinilla = 84 segundos; 9:16.
- Arco: hook_medias_res → desarrollo → cierre_historia → reflexion_o_pregunta.
- Gancho: “La concha guardó 16 embriones” (5 palabras).
- Voz: edge-tts, es-MX-JorgeNeural, +7%, pitch -2Hz.
- Estilo: dibujo_cientifico_scratchboard; prompt_base copiado literalmente del catálogo.
- Mapa: Formación Kitadani, 36.1 N, 136.6 E, pin regional aproximado; no representa coordenadas de especímenes.
- Capa de dato/gráfico: conteo de 313/240/195 y comparación explícita entre máximo individual 16 y media 6.78 del subconjunto.
- Ambientes y SFX: declarados por escena.
- Fuentes: SRC-001 estudio original; SRC-002 página municipal del yacimiento; SRC-003 referencia cartográfica secundaria para el punto aproximado.
- DOI del estudio: PENDIENTE_RESOLVEDOR; la URL editorial queda como enlace verificable, pero el DOI no se declara validado.
- No contiene narrative_qa. Estado: PENDIENTE_AUDITOR.
- La carpeta contiene únicamente storyboard.json; no se creó *_fuentes.md.

### Compuerta de cumplimiento — lectura de vuelta del JSON

| Condición | Resultado |
|---|---|
| approved_assets es exactamente [] | PASS |
| export.render_status es exactamente NOT_GENERATED | PASS |
| No existe export.filename ni rutas de frames/audio/voz/video/render | PASS |
| publicacion.status = PENDIENTE_DECISION_GROK | PASS |
| No se fija privacidad ni horario de publicación | PASS |
| source_ids resuelven dentro de sources | PASS |
| Voz exacta | PASS |
| Estilo y prompt_base literal | PASS |
| Mapa con coordenada regional real y precisión declarada | PASS |
| Capa de dato/gráfico | PASS |
| 170–235 palabras | PASS |
| 75–90 segundos incluyendo cortinilla | PASS |
| 7–9 escenas | PASS |
| narrative_qa ausente | PASS |

El borrador queda en proyectos/; no se promovió a cola/entrada y no se declara QA oficial ni aceptación de Grok.

## 5. Seguimiento técnico — Meta y Google Trends

- **Meta Graph API:** no se encontró una entrada oficial nueva posterior a la versión v27.0 ya registrada. La lectura directa del changelog volvió a fallar por acceso/429.
- **Instagram Insights:** la página oficial de changelog de Instagram Platform no se pudo leer directamente por restricción de acceso; no se halló una actualización nueva sustentada.
- **Facebook Pages Insights:** la referencia oficial abrió. Confirma la familia de métricas page_media_view, page_total_media_view_unique, post_media_view y post_total_media_view_unique. page_media_view y post_media_view cuentan reproducciones/visualizaciones de contenido y no deben tratarse automáticamente como vistas exclusivamente de video; las métricas únicas cuentan espectadores únicos. La referencia también indica que las interacciones de Reels no se incluyen en Page Insights. La información confirma el estado documentado, pero no constituye un cambio de producto nuevo respecto del corte técnico previo.
- **Google Trends API:** la documentación oficial mantiene el acceso alfa limitado; no se encontró anuncio nuevo de disponibilidad general.
- **Decisión documental:** no se reescribe docs/INVESTIGACION_API_META_Y_GOOGLE_TRENDS.md porque no se encontró un cambio nuevo de producto o changelog suficientemente sustentado. Los fallos de acceso y el estado de verificación quedan registrados en este radar.

## 6. Estado de QA narrativo preexistente — lectura exclusiva

Se releyeron los storyboards canónicos y las copias únicas en proyectos/, salidas/, cola/entrada/ y cola/bloqueados/, deduplicando por project_id conforme a la lógica de scripts/registro_editorial.py. No se ejecutó QA, no se escribió narrative_qa y no se promovió material.

**Corte anterior (11-nov):** 83 project_id únicos, 24 con narrative_qa (8 PASS, 16 FAIL), 59 PENDIENTE_AUDITOR y 13 directorios de proyectos sin storyboard.  
**Cambios posteriores comprobados:**
- 2026-11-11_dato-ratas-topo-damaraland: no contiene narrative_qa; PENDIENTE_AUDITOR.
- 2026-11-12_dato-pedorreta-chimpances: PASS/91; review_basis=lectura_en_frio_solo_narracion; reviewed_at=2026-11-12T15:38:50-06:00; siete checks true; critical_flags=[].
- Borrador de hoy 2026-11-13_dato-caracol-16-embriones: no contiene narrative_qa; PENDIENTE_AUDITOR.

**Inventario al cierre:** 86 project_id únicos incluyendo el borrador de hoy; 25 con narrative_qa (9 PASS, 16 FAIL); 61 PENDIENTE_AUDITOR; 13 directorios de proyectos sin storyboard. Las 25 entradas con QA se detallan a continuación; el orden de los siete checks es el del esquema oficial.

### 6.1 Metadatos y critical_flags

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
| 2026-11-12_dato-pedorreta-chimpances | PASS | 91 | lectura_en_frio_solo_narracion | 2026-11-12T15:38:50-06:00 | [] |

### 6.2 Los siete checks — valores exactos

Orden: pregunta_central_reconstruible; apertura_in_medias_res; progresion_por_escena; transiciones_causales; giro_cientifico_explicado; limite_evidencia_explicito; payoff_cierre_apertura.

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
| 2026-11-12_dato-pedorreta-chimpances | true | true | true | true | true | true | true |

### 6.3 PENDIENTE_AUDITOR — 60 storyboards preexistentes sin narrative_qa

Proyectos:
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

Salidas únicas:
- 2026-10-24_aves-temen-mas-a-mujeres
- 2026-10-24_fenomeno-el-nino
- 2026-11-01_dato-xolo-mictlan
- 2026-11-03_kids-tiburon-groenlandia
- 2026-11-03_comida-maillard
- 2026-11-04_comida-miel-no-caduca
- 2026-11-04_inter-bioluminiscencia-mar
- 2026-11-04_kids-hipo-por-que

Cola de entrada:
- 2026-11-07_dato-clavo-te-cocina
- 2026-11-11_dato-ratas-topo-damaraland

Bloqueados únicos:
- 2026-11-03_enzimas-incrustadas-oceano
- 2026-11-04_machu-picchu-fallas-pisa
- 2026-11-05_comida-palomitas-explotan
- 2026-11-05_inter-arboles-mito-respiran
- 2026-11-05_inter-venus-dia-largo
- 2026-11-06_inter-corazon-ballena-azul
- 2026-11-07_inter-mpemba-mito

El borrador creado hoy, 2026-11-13_dato-caracol-16-embriones, tampoco contiene narrative_qa y queda PENDIENTE_AUDITOR. No se usa salidas/qa.json como narrative_qa.

### 6.4 Directorios sin storyboard — 13

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

## 7. Cierre y límites

- Entregables de esta fecha: este radar y proyectos/2026-11-13_dato-caracol-16-embriones/storyboard.json. No se creó archivo separado de fuentes.
- El storyboard permanece en proyectos/ y PENDIENTE_AUDITOR; el Auditor independiente decide PASS/FAIL y cualquier promoción posterior.
- No se creó ni modificó narrative_qa, cola/entrada/, cola/bloqueados/, salidas/ ni archivos de otros proyectos.
- No se modificaron main, data/*.json, workflows, motores canónicos ni Motor U6.
- No se generaron imágenes, frames, audio, video ni renders; no se publicó ni programó contenido; no se consumieron créditos.
