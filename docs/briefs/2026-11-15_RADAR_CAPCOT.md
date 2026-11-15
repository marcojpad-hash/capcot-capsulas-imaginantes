# RADAR CAPCOT — 2026-11-15

Rama: `feature/capcot-video-discovery-continuity`  
Serie: **Datos y ociosidades**  
Fecha de consulta y paquete: **domingo 15 de noviembre de 2026, CDMX**.

## Resultado operativo y guardia anti-duplicación

Se leyeron los documentos obligatorios, el catálogo de estilos, la plantilla, las fuentes de rotación y el inventario combinado de `proyectos/`, `salidas/`, `cola/entrada/` y `cola/bloqueados/`. La lectura de `scripts/registro_editorial.py` confirma que el registro combinado recoge proyectos, cola y salidas y deduplica por `project_id`; para esta guardia también se contrastaron explícitamente `fecha_objetivo`, `slot_local` y `slot_cesta` de los 153 archivos `storyboard.json` encontrados. No apareció ningún storyboard con `fecha_objetivo=2026-11-15`, ni ocupación de 17:00 o 23:30 para esa fecha. Tampoco hay registros del 15-nov en `data/rotacion.json` ni `data/publicaciones.json`. No existe `data/horario_2026-11-15.json`; se aplicó el horario general y el contrato operativo.

El estado operativo de slots del día ya registra:
- **07:00:** colibrí `es6hWxPdt2A`, privado y con publicación programada para 13:00Z; no se declara publicado.
- **13:30:** agua-imanes `O9QlSaft5DY`, registrado como slot de prueba.
- **19:00:** autismo-microbioma `aTau_z2yWq8`, registrado en el estado del día aunque la ventana 19:00 aparece retirada en la configuración actual.
- **17:00:** libre; cae dentro de la ventana activa 16:30–18:00. El domingo no es día preferente, pero no está excluido.
- **23:30:** libre; slot fijo `slot_cesta=dato_del_dia`, autorizado por el contrato.

Hay tres elementos previos en el estado operativo; los dos nuevos borradores dejan el día en el límite de cinco elementos. No se tocó ninguno de los slots preexistentes.

### Archivos creados

1. `proyectos/2026-11-15_dato-quasar-pareja-cosmic-dawn/storyboard.json` — slot 17:00, commit `20aa7ae3d07bfb71165adef7d12f0ab345f4439c`, lectura de vuelta SHA `1fa6f92d83f537f29eb2fa21e90388ade9a67b11`.
2. `proyectos/2026-11-15_dato-dia-diapausa-lestes-sponsa/storyboard.json` — slot 23:30 `dato_del_dia`, commit `b8fe24acb0a3cb4bf9aeb7d569c1b115642757bf`, lectura de vuelta SHA `3cb6846a5755e48321892db046b6055720a54df8`.

El brief es el único otro entregable de la fecha. No se creó `*_fuentes.md`.

## Candidatos científicos — ventana 8–15 nov

La fecha indicada es la publicación editorial del artículo, no necesariamente la primera fecha de un preprint. Para todos los DOI se intentó resolver mediante `doi.org` y/o Crossref; los endpoints devolvieron “URL is not accessible via this tool”. **Ningún DOI se declara validado por Crossref o resolvedor.** Las páginas editoriales y el manuscrito primario accesibles se conservan como enlaces verificables.

### 1. Pareja candidata de cuásares en el amanecer cósmico — principal, 17:00
- **Autoría/año:** Onorato et al. (2026).
- **Estudio:** *Nāpōwawā‘enakaulua: A Close Quasar Pair at Cosmic Dawn in the Aether Survey*, *The Astrophysical Journal Letters* 1011, L59; publicación editorial 10-nov-2026. El manuscrito de autor está en arXiv:2609.31835 (preprint anterior, 25-sep-2026).
- **DOI:** `10.3847/2041-8213/aeb11f` — **PENDIENTE_RESOLVEDOR**.
- **Fuente primaria:** https://arxiv.org/abs/2609.31835  
  **Comunicado institucional:** https://noirlab.edu/public/news/noirlab2627/ (release noirlab2627; espejo editorial consultado: https://www.sci.news/astronomy/record-breaking-quasar-pair-early-universe-15191.html).
- **Novedad observada:** candidato a pareja a z≈6.078; separación angular 0.98±0.01″ y separación transversal proyectada 5.56±0.06 pkpc; estimaciones espectrales de 1.530×10⁹ y 3.99×10⁸ masas solares. La compañera apareció al inspeccionar el sondeo Aether de 200 cuásares.
- **Tendencia:** sin señal científica/natural visible en el top 25 de Google Trends México.
- **Relevancia científica:** alta; ofrece una prueba poco común sobre el crecimiento de agujeros negros masivos en el universo temprano.
- **Oportunidad editorial:** alta; dos fuentes casi superpuestas y una incertidumbre científica real.
- **Riesgos:** los autores favorecen dos fuentes físicas por diferencias en las alas azules de [O III], pero no descartan definitivamente una lente gravitacional. La separación es proyectada, no tridimensional; las masas son estimaciones espectrales, no pesajes directos.
- **Recomendación:** desarrollar como pregunta “¿dos cuásares o una imagen duplicada?”. Borrador en el proyecto 17:00.

### 2. Controles biofísicos de la fotosíntesis diurna global
- **Autoría/año:** Xi Liu, Jingyu Lin, Yanan Zhou, Zikang Diao y Xing Li (2026).
- **Estudio:** *Divergent biophysical controls on the complementary dimensions of global diurnal photosynthesis*, *Communications Earth & Environment*.
- **Fecha editorial:** 14-nov-2026.
- **DOI:** `10.1038/s43247-026-04214-3` — **PENDIENTE_RESOLVEDOR**.
- **Fuente primaria:** https://www.nature.com/articles/s43247-026-04214-3
- **Novedad observada:** análisis global horario de producción primaria bruta; el déficit de presión de vapor ayuda a explicar la asimetría y la depresión de mediodía, mientras temperatura y verdor controlan otras dimensiones de magnitud. Los modelos no reproducen bien algunas de esas formas diurnas.
- **Tendencia:** sin señal en top 25 de Trends.
- **Relevancia científica:** alta; mejora la representación de los ciclos diarios de carbono.
- **Oportunidad editorial:** alta; “por qué la fotosíntesis no alcanza su máximo al mediodía”.
- **Riesgos:** son productos globales y controles biofísicos agregados; no afirmar que todas las plantas se detienen al mediodía ni que se midió cada hoja directamente.

### 3. Olas de calor marinas ocultas bajo la superficie
- **Autoría/año:** Shujing Zhang et al. (2026).
- **Estudio:** *Vertical structure and evolution of large-scale subsurface marine heatwaves*, *npj Climate and Atmospheric Science*.
- **Fecha editorial:** 14-nov-2026.
- **DOI:** `10.1038/s41612-026-01592-5` — **PENDIENTE_RESOLVEDOR**.
- **Fuente primaria:** https://www.nature.com/articles/s41612-026-01592-5
- **Novedad observada:** identifica más de 500 eventos subsuperficiales en los primeros 1,000 m del océano (60°N–60°S, 1993–2020), con siete estructuras verticales recurrentes y vínculos con ENSO en parte de los eventos.
- **Tendencia:** sin señal en top 25 de Trends.
- **Relevancia científica:** alta; añade profundidad y estructura vertical a la evaluación de extremos oceánicos.
- **Oportunidad editorial:** alta; “el océano también tiene olas de calor invisibles desde la superficie”.
- **Riesgos:** no presentar los eventos del reanálisis como 500 mediciones directas en cada punto del océano; el periodo analizado termina en 2020.

### 4. Cas9 dividido para detectar ácidos nucleicos sin dependencia de PAM
- **Autoría/año:** Wenhao Yin et al. (2026).
- **Estudio:** *A split RNA-guided Cas9 system for PAM-independent and cis-cleavage-free nucleic acid detection*, *Nature Communications*.
- **Fecha editorial:** 14-nov-2026.
- **DOI:** `10.1038/s41467-026-79722-z` — **PENDIENTE_RESOLVEDOR**.
- **Fuente primaria:** https://www.nature.com/articles/s41467-026-79722-z
- **Novedad observada:** sistema SCas9 con guía dividida; detección de ssDNA/RNA a escala picomolar en unos 30 minutos y de dsDNA/RNA largo a escala attomolar con amplificación; ensayos con HPV16 y miR-21.
- **Tendencia:** sin señal en top 25 de Trends.
- **Relevancia científica:** alta para diagnóstico molecular y herramientas de detección.
- **Oportunidad editorial:** media-alta; explica cómo dividir una guía cambia el comportamiento de Cas9.
- **Riesgos:** método experimental/analítico; no presentarlo como prueba clínica aprobada ni como diagnóstico disponible.

### 5. Diapausa embrionaria del caballito del diablo *Lestes sponsa* — dato del día, 23:30
- **Autoría/año:** Ulf Norling y Szymon Sniegula (2026).
- **Estudio:** *Maintenance and termination of embryonic diapause in the damselfly Lestes sponsa: the role of temperature and photoperiod*, *Scientific Reports*.
- **Fecha editorial:** 15-nov-2026; cumple la regla de fuente del mismo día y ventana de 48 horas.
- **DOI:** `10.1038/s41598-026-80392-6` — **PENDIENTE_RESOLVEDOR**.
- **Fuente primaria:** https://www.nature.com/articles/s41598-026-80392-6
- **Novedad observada:** tras 19–21 semanas a 5 °C, la transferencia a 21 °C produjo eclosión casi completa en 2–4 días bajo fotoperiodos distintos. También se observó eclosión a 5 °C y supervivencia larvaria durante dos semanas cerca de 0 °C.
- **Tendencia:** sin señal en top 25 de Trends.
- **Relevancia científica:** alta para fisiología estacional y plasticidad del desarrollo.
- **Oportunidad editorial:** muy alta; una pausa embrionaria que acumula frío y sincroniza la salida.
- **Riesgos:** ensayo de laboratorio, huevos agrupados y muestra materna pequeña; la posible eclosión invernal bajo inviernos más cálidos es una hipótesis de los autores, no un cambio de campo demostrado.
- **Recomendación:** usar como storyboard independiente 23:30 `dato_del_dia`. La URL editorial está accesible; el DOI sigue pendiente.

## RSS científicos y Google Trends

Se consultaron los diez RSS configurados en `scripts/tendencias.py`. La herramienta no pudo leer sus tipos MIME; **no se afirma que se haya parseado XML**:
- ScienceDaily ciencia, salud y espacio: HTTP 400, `Unsupported content type: application/xml`.
- Phys.org: HTTP 400, `Unsupported content type: text/xml`.
- NASA: HTTP 400, `Unsupported content type: application/rss+xml`.
- ESA: HTTP 404, `Not Found`.
- Nature: HTTP 400, `Unsupported content type: application/rss+xml`.
- EurekAlert y Agencia SINC: `URL is not accessible via this tool`.
- UNAM Global: HTTP 400, `Unsupported content type: application/rss+xml`.
- Google Trends RSS México: `URL is not accessible via this tool`.

**Respaldo oficial:** Google Trends Trending Now México: 207 tendencias en la vista consultada; las primeras 25 estuvieron dominadas por deportes y entretenimiento. No apareció una señal inequívoca de ciencia o naturaleza que explicara los cinco candidatos. No se atribuye popularidad a ninguno de los artículos.

## Rotación, estilo y narrativa

- Último storyboard del repositorio (14-nov): `paper_rasgado_capas`, estructura `comparacion`, cama `circuito_neural`.
- Storyboard previo (13-nov): `dibujo_cientifico_scratchboard`, cama `pizzicato`.
- Nuevos borradores: 17:00 `van_gogh` + `pregunta` + `arpegio`; 23:30 `rubber_hose_1930s` + `historia` + `pulso`. No repiten entre sí ni los dos últimos storyboards del repositorio.
- **Límite de rotación:** el estilo del colibrí del slot 07:00 no está guardado en el estado operativo ni hay storyboard/asset del video en este repositorio. La unicidad visual respecto de esa cápsula inmediatamente anterior no es certificable; no se inventa su estilo. Se deja esta limitación explícita en ambos borradores.
- Ambos borradores abren con acción ya en curso, incluyen contrato narrativo de seis campos, ocho escenas, fuentes por afirmación, mapa con coordenadas reales (el punto de Lund es solo referencia regional), capa de dato, voz `edge-tts es-MX-JorgeNeural +7% pitch -2Hz`, ambiente y SFX por escena y cortinilla de seis segundos.

## QA preexistente — lectura de 153 storyboard.json

Se relevaron 153 archivos `storyboard.json` en `proyectos/`, `salidas/`, `cola/entrada/` y `cola/bloqueados/`, contrastando también `fecha_objetivo`, `slot_local` y `slot_cesta`. Se encontraron 35 copias con `narrative_qa`, correspondientes a 27 `project_id` distintos (8 copias duplicadas en cola/bloqueados/entrada); 11 PASS y 16 FAIL. Las otras 118 copias no contienen la clave y quedan **PENDIENTE_AUDITOR**. No se creó ni modificó QA, no se interpretó `salidas/qa.json` como narrative_qa y no se promovió ningún proyecto.

En todos los registros siguientes, `review_basis` aparece exactamente como `lectura_en_frio_solo_narracion`. Cuando `reviewed_at` dice `AUSENTE_EN_JSON`, el campo no existe en el objeto leído. Los siete checks se reproducen con sus claves y valores:

| project_id | status | score | review_basis | reviewed_at | checks | critical_flags |
|---|---:|---:|---|---|---|---|
| `2026-10-31_murcielagos-viroma-global` | FAIL | 72 | `lectura_en_frio_solo_narracion` | AUSENTE_EN_JSON | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":false,"progresion_por_escena":true,"transiciones_causales":false,"giro_cientifico_explicado":false,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `["APERTURA_NO_IN_MEDIAS_RES","TRANSICION_ENTRE_ESCENAS_2_3_SIN_PUENTE_CAUSAL","GIRO_CIENTIFICO_NO_SE_DESPRENDE_DE_LA_EVIDENCIA","PAGO_FINAL_NO_CIERRA_LA_PREGUNTA_CENTRAL"]` |
| `2026-10-31_sequias-energia-renovable` | FAIL | 56 | `lectura_en_frio_solo_narracion` | AUSENTE_EN_JSON | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":false,"progresion_por_escena":false,"transiciones_causales":false,"giro_cientifico_explicado":false,"limite_evidencia_explicito":true,"payoff_cierre_apertura":false}` | `["GANCHO_DEFINICIONAL_SIN_ACCION","TRANSICIONES_CAUSALES_AUSENTES","GIRO_CIENTIFICO_NO_EXPLICADO","PAYOFF_NO_PAGA_LA_APERTURA"]` |
| `2026-11-01_dato-cambio-horario-corazon` | FAIL | 84 | `lectura_en_frio_solo_narracion` | 2026-11-01T18:08:00-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `["CIERRE_SUPERA_110_CARACTERES_Y_ROMPE_SELLO"]` |
| `2026-11-01_llorar-cebolla-quimica` | FAIL | 79 | `lectura_en_frio_solo_narracion` | 2026-11-01T15:09:29-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":false,"payoff_cierre_apertura":false}` | `["LIMITES_DE_EVIDENCIA_AUSENTES","CIERRE_INTRODUCE_UNA_CONCLUSION_NO_SUSTENTADA"]` |
| `2026-11-01_pulpo-tres-corazones` | FAIL | 72 | `lectura_en_frio_solo_narracion` | 2026-11-01T15:09:29-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":false,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":false,"payoff_cierre_apertura":true}` | `["APERTURA_NO_IN_MEDIAS_RES","REPETICION_DE_DATOS_ENTRE_ESCENAS_3_Y_4","GIRO_NO_EXPLICADO"]` |
| `2026-11-01_red-electrica-pulso-minuto` | PASS | 89 | `lectura_en_frio_solo_narracion` | 2026-11-01T15:09:29-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `[]` |
| `2026-11-02_camaron-mantis` | PASS | 90 | `lectura_en_frio_solo_narracion` | AUSENTE_EN_JSON | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `[]` |
| `2026-11-02_comida-pan-duro` | FAIL | 84 | `lectura_en_frio_solo_narracion` | AUSENTE_EN_JSON | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `["CIERRE_SOBREAFIRMA_Y_CONTRADICE_LIMITE_DE_SECADO"]` |
| `2026-11-04_cielo-azul-atardecer-rojo` | PASS | 94 | `lectura_en_frio_solo_narracion` | 2026-11-04T15:58:40-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `[]` |
| `2026-11-05_comida-palomitas` | FAIL | 82 | `lectura_en_frio_solo_narracion` | 2026-11-14T15:04:13-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":false,"progresion_por_escena":false,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `["APERTURA_NO_IN_MEDIAS_RES","TRANSICION_2_3_GENERICA_SIN_PUENTE_CAUSAL"]` |
| `2026-11-05_inter-arboles-se-comunican` | FAIL | 78 | `lectura_en_frio_solo_narracion` | 2026-11-14T15:04:13-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":false,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `["APERTURA_GENERICA_NO_IN_MEDIAS_RES"]` |
| `2026-11-05_inter-rayo-globular` | FAIL | 81 | `lectura_en_frio_solo_narracion` | 2026-11-14T15:04:13-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":false,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `["APERTURA_HISTORICA_DESCRIPTIVA_NO_IN_MEDIAS_RES"]` |
| `2026-11-05_kids-dia-en-venus` | PASS | 88 | `lectura_en_frio_solo_narracion` | 2026-11-14T15:04:13-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `[]` |
| `2026-11-06_comida-aguacate-negro` | FAIL | 79 | `lectura_en_frio_solo_narracion` | 2026-11-14T15:04:13-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":false,"transiciones_causales":false,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `["REPETICION_ESCENAS_5_6_SIN_AVANCE_CAUSAL"]` |
| `2026-11-06_inter-arena-cantante` | PASS | 94 | `lectura_en_frio_solo_narracion` | 2026-11-14T15:04:13-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `[]` |
| `2026-11-06_inter-ranas-congeladas` | FAIL | 83 | `lectura_en_frio_solo_narracion` | 2026-11-14T15:04:13-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":false,"transiciones_causales":false,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `["REPETICION_ESCENAS_5_6_LIMITES_DE_ESPECIE_Y_CONDICIONES"]` |
| `2026-11-06_kids-ballena-azul-corazon` | FAIL | 80 | `lectura_en_frio_solo_narracion` | 2026-11-14T15:04:13-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":false}` | `["PAYOFF_SOBREAFIRMA_CASI_SE_DETIENE"]` |
| `2026-11-07_comida-hielo-caliente` | FAIL | 81 | `lectura_en_frio_solo_narracion` | 2026-11-14T15:04:13-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":false,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `["APERTURA_DE_CREENCIAS_NO_IN_MEDIAS_RES"]` |
| `2026-11-07_inter-nubes-pesan` | FAIL | 78 | `lectura_en_frio_solo_narracion` | 2026-11-14T15:04:13-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":false,"transiciones_causales":false,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":false}` | `["ESCENA_7_REITERA_CIFRA_Y_LIMITE_SIN_PAYOFF_DE_SUSPENSION"]` |
| `2026-11-07_inter-pulpo-suenos` | FAIL | 80 | `lectura_en_frio_solo_narracion` | 2026-11-14T15:04:13-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":false,"transiciones_causales":false,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":false}` | `["REPETICION_ESCENAS_5_6_Y_PAYOFF_VAGO"]` |
| `2026-11-07_kids-huesos-bebe` | FAIL | 82 | `lectura_en_frio_solo_narracion` | 2026-11-14T15:04:13-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":false,"transiciones_causales":false,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `["ESCENA_6_REPITE_VARIACION_DE_CONTEO_Y_FUSION"]` |
| `2026-11-09_dato-robot-ensambla-orbita` | PASS | 90 | `lectura_en_frio_solo_narracion` | 2026-11-09T18:45:00-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `[]` |
| `2026-11-10_comida-aprendizaje-sabor-nutriente` | PASS | 92 | `lectura_en_frio_solo_narracion` | 2026-11-10T15:47:50-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `[]` |
| `2026-11-10_dato-adn-sincroniza-flujo` | PASS | 91 | `lectura_en_frio_solo_narracion` | 2026-11-10T16:16:00-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `[]` |
| `2026-11-12_dato-pedorreta-chimpances` | PASS | 91 | `lectura_en_frio_solo_narracion` | 2026-11-12T15:38:50-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `[]` |
| `2026-11-13_dato-caracol-16-embriones` | PASS | 91 | `lectura_en_frio_solo_narracion` | 2026-11-13T15:42:39-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `[]` |
| `2026-11-14_dato-microplasticos-pantanal` | PASS | 88 | `lectura_en_frio_solo_narracion` | 2026-11-14T15:04:13-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `[]` |

Los borradores nuevos `2026-11-15_dato-quasar-pareja-cosmic-dawn` y `2026-11-15_dato-dia-diapausa-lestes-sponsa` no contienen `narrative_qa`: ambos quedan **PENDIENTE_AUDITOR**. La evaluación en frío corresponde exclusivamente al auditor independiente.

## Seguimiento técnico Meta / Google

Se revisaron las páginas oficiales de Graph API, Instagram Insights, Facebook Pages Insights y Google Trends API alfa. El informe `docs/INVESTIGACION_API_META_Y_GOOGLE_TRENDS.md` ya contiene la discrepancia de versión observada (referencias v27.0 frente a tabla de versiones v26.0), las rutas de Insights y el estado alfa de Trends; no apareció un cambio oficial nuevo y sustentado que justifique reescribirlo. **No se modificó el informe técnico.**

## Compuerta de entrega y límites

- Se crearon exactamente tres archivos para la fecha: un `RADAR_CAPCOT` y dos storyboards (17:00 principal y 23:30 `dato_del_dia`).
- Ambos JSON fueron releídos desde GitHub y parseados.
- Cada uno tiene 183 o 178 palabras respectivamente, ocho escenas, 78 segundos de narración más seis de cortinilla (84 s), gancho de seis palabras o menos, seis campos de `narrative_contract`, arcos completos, `source_ids` existentes, voz y estilo de catálogo, mapa y dato/gráfico.
- En ambos: `approved_assets=[]`; `export.render_status=NOT_GENERATED`; no existe `export.filename`, `asset_filename`, `asset_type` ni ruta de medios; `publicacion.status=PENDIENTE_DECISION_GROK`; no existe `narrative_qa`.
- Los DOI de los dos storyboards permanecen `PENDIENTE_RESOLVEDOR`; las URL primarias están incluidas dentro de los JSON.
- Los borradores permanecen únicamente en `proyectos/`; no se copiaron a `cola/entrada/`, no se marcaron preparados y no se aceptaron por Grok.
- No se generaron frames, imágenes, audio, voz, video ni renders. No se publicó ni programó. No se modificaron `data/*.json`, `main`, workflows, motores canónicos ni Motor U6. No se consumieron créditos.

## Reejecución de control — 15-nov-2026, 09:33 CDMX

**Resultado: NO_DUPLICAR.** El RADAR de esta fecha ya existe y conserva sus cinco candidatos; los dos storyboards aplicables también existen. No se creó un segundo brief ni un tercer storyboard.

La relectura de ajustes_entre_modelos/ESTADO_SLOTS_2026-11-15.md (corte 06:24 CDMX) y de los storyboards confirma cinco slots con registro:
- **07:00:** colibrí es6hWxPdt2A, privado y programado para 13:00Z; no se declara publicación efectiva.
- **13:30:** agua-imanes O9QlSaft5DY, slot de prueba ocupado.
- **17:00:** 2026-11-15_dato-quasar-pareja-cosmic-dawn, existente en proyectos/.
- **19:00:** autismo-microbioma aTau_z2yWq8, registrado en el estado del día aunque la ventana aparece retirada en la configuración actual.
- **23:30:** 2026-11-15_dato-dia-diapausa-lestes-sponsa, existente en proyectos/, slot_cesta=dato_del_dia.

El archivo específico data/horario_2026-11-15.json no existe; se mantiene la referencia al contrato y horario general. Los cinco slots ya tienen registro y el cupo diario global de cinco está alcanzado. Resultado por slot: 17:00 y 23:30 **NO_DUPLICAR**; 07:00, 13:30 y 19:00 ya están ocupados/registrados. No hay slot autorizado libre para otro storyboard.

### Relectura de los dos storyboards existentes

- **2026-11-15_dato-quasar-pareja-cosmic-dawn:** fecha_objetivo=2026-11-15, slot_local=17:00, 178 palabras, 8 escenas, 78 s de escenas + 6 s de cortinilla = 84 s.
- **2026-11-15_dato-dia-diapausa-lestes-sponsa:** fecha_objetivo=2026-11-15, slot_local=23:30, slot_cesta=dato_del_dia, 183 palabras, 8 escenas, 78 s de escenas + 6 s de cortinilla = 84 s.

Ambos conservan arcos completos, narrative_contract, source_ids válidos, estilo y prompt_base literal, voz edge-tts es-MX-JorgeNeural (+7%, -2Hz), mapa y capa de dato. En ambos se revalidó approved_assets=[], export.render_status=NOT_GENERATED, ausencia de export.filename, asset_filename, asset_type y rutas de medios, y publicacion.status=PENDIENTE_DECISION_GROK. Ninguno contiene narrative_qa: ambos siguen **PENDIENTE_AUDITOR**. No se modificaron sus archivos ni se promovieron a cola.

### RSS y Google Trends — nueva comprobación

Los diez RSS científicos y Google Trends RSS México se volvieron a consultar con las URL exactas de scripts/tendencias.py. Se reprodujeron los mismos fallos: ScienceDaily (3 feeds) HTTP 400 Unsupported content-type: application/xml; Phys.org HTTP 400 text/xml; NASA HTTP 400 application/rss+xml; ESA HTTP 404 Not Found; Nature HTTP 400 application/rss+xml; EurekAlert y SINC URL is not accessible via this tool; UNAM Global HTTP 400 application/rss+xml; Google Trends RSS México URL is not accessible via this tool. No se afirmó parseo XML.

Como respaldo se consultó Trending Now oficial de México (últimas 24 h): **214 tendencias** en la vista. Las primeras 25 estuvieron dominadas por fútbol/deportes y entretenimiento; no apareció una señal inequívoca de ciencia o naturaleza. El snapshot no se interpreta como interés científico ni como validación de los candidatos.

### Seguimiento técnico

Se añadió la sección 9.8 a docs/INVESTIGACION_API_META_Y_GOOGLE_TRENDS.md para documentar la discrepancia oficial entre el overview y Page Insights (v27.0) y la tabla de versiones (v26.0). No se cambió ninguna integración. Instagram Insights y el changelog general devolvieron HTTP 429; Page Insights sí fue consultable y mantiene los límites ya registrados, incluida la exclusión de interacciones de Reels. Google Trends API continúa en alfa limitada sin cambio nuevo de contrato.
