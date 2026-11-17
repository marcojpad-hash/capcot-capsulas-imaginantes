# RADAR CAPCOT — 17 de noviembre de 2026

**Consulta:** 17-nov-2026, 08:11 CDMX. **Ventana:** 10–17 nov-2026, inclusive.
**Repositorio:** `marcojpad-hash/capcot-capsulas-imaginantes` · `feature/capcot-video-discovery-continuity`.

## Resultado operativo y guardia anti-duplicación

- **Slot principal:** `17:00`, activo los martes dentro de la ventana 16:30–18:00. El 17-nov-2026 es martes. No había proyecto de esa fecha en `proyectos/`, `salidas/`, `cola/entrada/` ni `cola/bloqueados/`; el slot estaba libre. Se crea un único storyboard principal en `proyectos/`.
- **07:00:** el chequeo `ESTADO_SLOTS_2026-11-17.md` de 06:25 lo encontró vacío; después se programó el respaldo del ornitorrinco con publishAt 13:00Z (07:00 CDMX). No duplicar.
- **13:30:** ocupado por hielo/Baffin (`KnP1j4y72ug`), marcado como slot de prueba en `data/horarios.json`; no producir.
- **19:00:** el archivo de estado registra el video de riesgo LDL programado, pero `data/horarios.json` lo marca como retirado; se conserva como publicación preexistente y no se trata como slot nuevo autorizado.
- **23:30:** slot `dato_del_dia` fijo diario del contrato y libre por fecha/slot en los cuatro árboles. Hay un artículo del mismo día sobre detección de *Lobesia botrana*, pero el acceso directo al artículo devolvió `DisabledError` y DOI/Crossref no resolvieron; se registra `PENDING_SOURCE` y no se crea storyboard 23:30.
- No existe `data/horario_2026-11-17.json`; la activación se comprobó con `docs/CONTRATO_OPERATIVO_UNIFICADO.md` §3 y `data/horarios.json`. `data/temas_del_dia.json`, `data/rotacion.json` y `data/publicaciones.json` no contienen registros del 17-nov; las dos últimas llegan a 31-oct y temas del día a 28-oct. Se contrastó con los storyboards recientes y el código de `scripts/registro_editorial.py`.
- Antes de escribir no existían `docs/briefs/2026-11-17_RADAR_CAPCOT.md` ni `proyectos/2026-11-17_dato-suelo-dos-relojes/storyboard.json`. El entregable aplicable es un radar y un storyboard; no se crea archivo `*_fuentes.md` ni un segundo storyboard sin fuente apta.

## Candidatos científicos (3–5; se documentan cinco)

### 1. Rehidratación del suelo: dos relojes para CO₂ y crecimiento microbiano — RECOMENDADO 17:00

- **Fuente primaria:** Caro, T. A., Ibarra Arriaga, J., Solini, G., Shivji, Z., Grossman, E., Jhatro, A., Stewart, B., Fu, X., Sessions, A. L. & Karthikeyan, S. (2026). *SIP-enabled multi-omics reveals soil microbiome responses to drought and rehydration*. Nature Communications, Article in Press. Publicado en línea: 12-nov-2026. DOI impreso: `10.1038/s41467-026-79474-w`.
- **URL editorial/PDF:** [Artículo](https://www.nature.com/articles/s41467-026-79474-w) · [PDF primario](https://www.nature.com/articles/s41467-026-79474-w_reference.pdf) · [DOI](https://doi.org/10.1038/s41467-026-79474-w).
- **Novedad observada:** el flujo de CO₂ comienza dentro de la primera hora tras rehidratación; el máximo medido de crecimiento llega a 6 h en controles y a 72 h en la pastura de Jalama sometida a sequía de alta intensidad. El control de arena de sílice estéril detecta liberación abiótica de CO₂ por desorción/alteración de poros en ~9 min.
- **Tendencia:** no aparece señal científica en las primeras 25 tendencias visibles de Google Trends México.
- **Relevancia científica:** alta; separa procesos catabólicos y anabólicos en el ciclo del carbono del suelo y cuantifica la respuesta a sequía/rehidratación.
- **Oportunidad editorial:** alta; paradoja clara: el suelo emite CO₂ antes de que la biomasa microbiana alcance su máximo. Permite explicar dos relojes y una posible fuente abiótica del pulso inicial.
- **Público/ocasión:** público general de ciencia/naturaleza; slot de tarde 17:00.
- **Riesgos:** son dos casos de campo paralelos en biomas/usos/tratamientos distintos y una parcela por condición y sitio; no generalizar. El control de ~9 min es arena estéril, no suelo vivo. Los metabolitos como explicación son hipótesis. El máximo de 72 h es el máximo medido en el ensayo de rehidratación, no una regla universal.
- **Verificación:** PDF editorial primario abierto; se contrastaron resumen, figura 1, figura 2, resultados y discusión. El DOI está impreso en el PDF, pero Crossref y el resolvedor `doi.org` no fueron accesibles; `DOI=PENDIENTE_RESOLVEDOR`, no se declara validado. La URL editorial/PDF sí fue consultada.

### 2. Caracoles terrestres del bosque en turberas abiertas: el filtro local pesa más que la cercanía al bosque

- **Fuente primaria:** Svobodová, K., Coufal, R., Horsáková, V. & Horsák, M. (2026). *Habitat filtering and species-specific spillover of forest gastropods across forest-open fen boundaries*. Scientific Reports, Article in Press. Publicado: 12-nov-2026. DOI: `10.1038/s41598-026-80137-5`.
- **URL editorial/PDF:** [Artículo](https://www.nature.com/articles/s41598-026-80137-5) · [PDF primario](https://www.nature.com/articles/s41598-026-80137-5_reference.pdf) · [DOI](https://doi.org/10.1038/s41598-026-80137-5).
- **Novedad observada:** análisis de transectos en 17 turberas de manantial de los Cárpatos occidentales y escala continental de 500 turberas europeas. Mayor pH del agua se asocia con mayor abundancia de especies forestales; más humedad tiene efecto negativo; la proximidad del bosque solo fue significativa para 4 de 12 especies.
- **Tendencia:** sin señal visible en Trends México.
- **Relevancia científica:** media-alta; muestra que la filtración ambiental puede limitar la presencia de fauna más allá de la distancia al hábitat fuente.
- **Oportunidad editorial:** media; contraste visual bosque–turbera y caracoles pequeños.
- **Público/ocasión:** naturaleza/ecología; alternativa para un slot posterior.
- **Riesgos:** “spillover” describe patrones de ocurrencia, no dispersión observada directamente; asociaciones con pH/humedad no prueban causalidad. DOI pendiente de resolución independiente.
- **Verificación:** PDF primario editorial abierto y resumen contrastado; DOI visible en PDF, pero Crossref/resolvedor inaccesibles: `DOI=PENDIENTE_RESOLVEDOR`.

### 3. La dormancia puede estabilizar ciertas redes alimentarias — modelo matemático

- **Fuente primaria:** Miller, Z. R., Vasseur, D. A. & Hull, P. M. (2026). *Dormancy stabilizes structured food webs*. Proceedings of the National Academy of Sciences (PNAS), 123(46), e2633661123. Epub: 11-nov-2026; fecha del fascículo: 17-nov-2026. DOI: `10.1073/pnas.2633661123`.
- **URL editorial/registro:** [PNAS](https://www.pnas.org/doi/10.1073/pnas.2633661123) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/43013542/) · [DOI](https://doi.org/10.1073/pnas.2633661123).
- **Novedad observada:** un modelo matemático mínimo muestra que la dormancia puede estabilizar dinámicas oscilatorias en redes alimentarias estructuradas con inestabilidad oscilatoria; el efecto es raro en redes no estructuradas o con interacciones simétricas competitivas/mutualistas.
- **Tendencia:** sin señal visible en Trends México.
- **Relevancia científica:** alta para ecología teórica y estabilidad de redes.
- **Oportunidad editorial:** media; analogía visual de “banco de semillas” que guarda organismos temporalmente fuera de las interacciones.
- **Público/ocasión:** público general interesado en ecología; alternativa de tarde.
- **Riesgos:** resultado teórico, no demostración experimental en una comunidad real; el efecto depende de la estructura de la red. DOI pendiente de resolución independiente.
- **Verificación:** registro PubMed y página PNAS consultados; DOI aparece en el registro/editorial, pero Crossref/resolvedor no accesibles: `DOI=PENDIENTE_RESOLVEDOR`.

### 4. Seis fuentes podrían reducir la toxicidad farmacéutica prevista en ríos — modelo global

- **Fuente primaria:** Chen, J., He, X., Zhao, L., Wen, J., Blaney, L., Yu, G. & Cai, Z. (2026). *Curbing six key sources could halve pharmaceutical mixture exceedance in global rivers*. Nature Geoscience. Publicado: 12-nov-2026. DOI: `10.1038/s41561-026-02096-w`.
- **URL editorial:** [Nature Geoscience](https://www.nature.com/articles/s41561-026-02096-w) · [DOI](https://doi.org/10.1038/s41561-026-02096-w).
- **Novedad observada:** mapa global de 2 km para mezclas de 53 fármacos en ríos, entrenado con 1,017 ensayos de toxicidad y 24 predictores geoespaciales. El modelo predice excedencia del umbral en 13% de celdas fluviales; escenarios contrafactuales de seis fuentes estiman reducción de 54–92% del área de excedencia.
- **Tendencia:** sin señal visible en Trends México.
- **Relevancia científica:** alta para ecotoxicología y gestión de contaminantes.
- **Oportunidad editorial:** alta por el mapa global y la pregunta “¿qué fuentes conviene controlar primero?”.
- **Público/ocasión:** ciencia/medio ambiente; alternativa para una cápsula de mapa.
- **Riesgos:** son predicciones y escenarios contrafactuales, no mejoras observadas tras intervenciones reales; 13% se refiere a celdas fluviales, no a “13% de todos los ríos”. La página completa de Nature redirigió/bloqueó el acceso directo; se consultó el resultado oficial con abstract, pero DOI/Crossref siguen pendientes.
- **Verificación:** abstract y metadatos visibles en el índice oficial de Nature; texto completo directo no accesible: `PENDING_FULLTEXT`, `DOI=PENDIENTE_RESOLVEDOR`.

### 5. Detección visual de la polilla de la vid *Lobesia botrana* con RPA–CRISPR/Cas12a–LFD — candidato 23:30

- **Fuente primaria:** Wang, Z., Zhao, J., Meng, C., Li, Y., Chen, X. & Xu, F. (2026). *Rapid and visual detection of the invasive pest Lobesia botrana using an RPA-CRISPR/Cas12a-LFD system*. Scientific Reports. Publicado: 17-nov-2026. DOI: `10.1038/s41598-026-79505-y`.
- **URL editorial:** [Scientific Reports](https://www.nature.com/articles/s41598-026-79505-y) · [DOI](https://doi.org/10.1038/s41598-026-79505-y).
- **Novedad observada en el resumen oficial:** ensayo RPA–CRISPR/Cas12a con lectura de tira de flujo lateral; límite de detección declarado de 1×10⁻³ ng/µL, reacción a 37–38 °C y ~45 min de muestra a resultado con extracción rápida en sitio; se reportan muestras de campo de distintas fases de desarrollo.
- **Tendencia:** sin señal visible en las primeras 25 tendencias de México.
- **Relevancia científica:** alta para detección de una plaga invasora de la viticultura.
- **Oportunidad editorial:** alta por la lectura visual de tira y el flujo de detección.
- **Público/ocasión:** naturaleza/agricultura; slot `23:30`, `dato_del_dia`.
- **Riesgos:** el resumen no muestra el tamaño de muestra; “todas las muestras probadas positivas” no equivale a sensibilidad poblacional universal. No se pudo abrir la página editorial directa (`DisabledError`) y DOI/Crossref no resolvieron.
- **Verificación/slot:** la ficha del editor indica publicación el 17-nov-2026, dentro de la ventana temporal del slot, pero la verificación primaria completa no se pudo cerrar: **`PENDING_SOURCE`**. El slot 23:30 está libre, pero no se crea storyboard sin fuente apta.

## Google Trends México y límites de señal

- **RSS Google Trends México:** `https://trends.google.com/trending/rss?geo=MX` no accesible desde esta sesión; no se descargó ni parseó XML.
- **Respaldo oficial:** [Trending Now México](https://trends.google.com/trending?geo=MX&hl=es-419). La página mostró 201 tendencias y 25 visibles en la consulta. Entre las visibles predominaban deportes, entretenimiento y conversación pública; no apareció una señal inequívoca de ciencia o naturaleza. “clima mexicali” y temas meteorológicos no se interpretan como noticia científica.
- **Límite:** la ausencia de una señal en las primeras 25 tendencias no demuestra ausencia de interés; solo describe la superficie consultada.

## RSS científicos: intentos y errores exactos

No se afirmó haber parseado XML. Los endpoints declarados en `scripts/tendencias.py` se intentaron por URL; el lector web rechazó varios tipos MIME XML/RSS:

| Feed | Resultado observado |
|---|---|
| ScienceDaily Top Science | HTTP 400: `Unsupported content-type: application/xml` |
| ScienceDaily Health | HTTP 400: `Unsupported content-type: application/xml` |
| ScienceDaily Space | HTTP 400: `Unsupported content-type: application/xml` |
| Phys.org | HTTP 400: `Unsupported content-type: text/xml` |
| NASA News Releases | HTTP 400: `Unsupported content-type: application/rss+xml` |
| ESA Space Science | HTTP 404: `Not Found` |
| Nature RSS | HTTP 400: `Unsupported content-type: application/rss+xml` |
| EurekAlert | `URL not accessible` |
| Agencia SINC | `URL not accessible` |
| UNAM Global | HTTP 400: `Unsupported content-type: application/rss+xml` |
| Google Trends RSS México | `URL not accessible` |

## Rotación, estilo y decisión editorial

- `data/horarios.json` marca la ventana de tarde 16:30–18:00 activa los martes; se toma 17:00 como slot libre. El slot 23:30 es fijo diario según contrato.
- `ESTADO_SLOTS_2026-11-17.md` confirma 07:00 ocupado después del respaldo ornitorrinco, 13:30 ocupado por hielo/Baffin y 19:00 con un video de riesgo LDL programado. El último se conserva como registro existente aunque la política actual marca 19:00 retirado.
- La cápsula anterior (16-nov) usó `collage_cientifico_vintage`, estructura `paradoja_mecanica` y cama `menor_calma`. Las del 15-nov usaron Van Gogh/rubber hose y estructuras `pregunta`/`historia`; la del 14-nov usó `papel_rasgado_capas` y `comparacion`. El nuevo borrador usa `papel_stop_motion`, prompt_base literal del catálogo, estructura `sabias_que` y cama `circuito_neural`; no repite estilo de la cápsula anterior ni estructura/estilo ya usado el mismo día.
- El tema se distingue del proyecto del 03-nov sobre microbios transportados en polvo africano: aquí se estudia el pulso de CO₂ y el crecimiento de microbioma de suelo tras sequía/rehidratación, no dispersión atmosférica.
- `scripts/registro_editorial.py` se leyó como fuente de lógica combinada, pero no se ejecutó en un runtime del repositorio; la rotación se reconstruyó leyendo sus reglas y los JSON/storyboards disponibles. No se modificó `data/*.json`.

## Observado, cálculo, inferencia y recomendación

- **Observado:** el artículo principal informa inicio de flujo de CO₂ dentro de 1 h, máximo medido de crecimiento a 6 h en controles y a 72 h en la pastura de Jalama con sequía de alta intensidad; el control abiótico de sílice libera CO₂ en ~9 min.
- **Cálculo:** storyboard de 214 palabras, 8 escenas, 78 s de escenas + 6 s de cortinilla = 84 s.
- **Inferencia editorial:** el conflicto narrativo más sólido es que el primer pulso de CO₂ no equivale necesariamente a recuperación de biomasa; la explicación incluye gas relictual y una hipótesis de metabolitos.
- **Recomendación:** usar el microbioma del suelo en 17:00; mantener 23:30 en `PENDING_SOURCE` hasta que el artículo de *Lobesia botrana* pueda abrirse y su DOI/URL verificarse independientemente.

## Seguimiento técnico Meta y Google Trends

- Se revisaron las páginas oficiales de Graph API changelog/versioning, Graph API Insights, Instagram Insights, Page Insights y Google Trends API alpha.
- Graph API overview y Page Insights siguen mostrando v27.0, mientras la tabla oficial de versiones consultada continúa listando v26.0; la discrepancia ya estaba en el informe técnico previo y no apareció un cambio nuevo sustentado. Las páginas Meta de changelog/Instagram Insights/Page Insights devolvieron 429 o bloqueo de acceso.
- Google Trends API continúa en alfa limitada; no se encontró un cambio nuevo en la documentación oficial de Trends. La actualización de Search Analytics API del 16-nov es otro producto de Google y no se atribuye a Trends.
- **Decisión:** no modificar `docs/INVESTIGACION_API_META_Y_GOOGLE_TRENDS.md` porque no apareció un cambio nuevo relevante y verificable.

## Validación previa y staging

- Se eligió un candidato principal y se creó solo `proyectos/2026-11-17_dato-suelo-dos-relojes/storyboard.json`.
- 9:16; 84 s totales con cortinilla de 6 s; 214 palabras; 8 escenas; gancho de 5 palabras; arco completo; fuentes por escena; voz `edge-tts es-MX-JorgeNeural` +7%, -2Hz; mapa con coordenadas de Fig. 1; capas dato y gráfico.
- `approved_assets=[]`; `export.render_status=NOT_GENERATED`; no existe `export.filename`, rutas de medios ni claves de assets; `publicacion.status=PENDIENTE_DECISION_GROK`.
- El storyboard no incluye `narrative_qa`; queda en `proyectos/` como `PENDIENTE_AUDITOR`. No se escribió en `cola/entrada/`, no se marcó preparado y no se generaron medios.
- El slot 23:30 queda `PENDING_SOURCE`; no se creó segundo storyboard.
- Se crearon exactamente dos entregables para el 17-nov: este radar y el storyboard principal. No se creó archivo de fuentes separado.

## QA preexistente — lectura de storyboards canónicos

Se revisaron los 159 archivos `storyboard.json` del árbol en `proyectos/`, `salidas/`, `cola/entrada/` y `cola/bloqueados/`. Se releyó el archivo canónico priorizando `proyectos/` y, cuando no existía, la copia disponible en las colas o salidas. Se encontraron **30 registros con `narrative_qa` en PASS/FAIL (13 PASS, 17 FAIL)**, **1 registro con `narrative_qa.status=PENDIENTE`** y **61 entradas sin la clave: PENDIENTE_AUDITOR**, enumeradas abajo. La lista previa incluía `2026-11-04_machu-picchu-fallas-pisa`, pero no existe un storyboard canónico de ese proyecto en el árbol actual; se registra aparte como `MISSING_CANONICAL_FILE` y no se recrea. El nuevo storyboard del 17-nov se añade a `PENDIENTE_AUDITOR`. `scripts/registro_editorial.py` se leyó y se usó como referencia para la consolidación por `project_id`; el script no se ejecutó porque esta conexión no ofrece runtime del repositorio, por lo que los 61 rótulos de la lista son identificadores/rutas leídos y no se afirma un conteo adicional de IDs únicos. No se ejecutó QA nuevo, no se escribió `narrative_qa`, no se interpretó `salidas/qa.json` como autorización y no se promovió ningún proyecto.

En los 30 registros PASS/FAIL, `review_basis` aparece exactamente como `lectura_en_frio_solo_narracion`. Los siete checks y `critical_flags` se reproducen tal como aparecen. `AUSENTE_EN_JSON` significa que el campo `reviewed_at` no existe en el objeto leído.

| project_id | status | score | review_basis | reviewed_at | checks | critical_flags |
|---|---:|---:|---|---|---|---|
| `2026-10-31_murcielagos-viroma-global` | FAIL | 72 | `lectura_en_frio_solo_narracion` | AUSENTE_EN_JSON | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":false,"progresion_por_escena":true,"transiciones_causales":false,"giro_cientifico_explicado":false,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `["APERTURA_ESTATICA_Y_ESCENARIO_NO_DOCUMENTADO","TRANSICIONES_GENERICAS","CIFRA_300000_SIN_UNIDAD_DE_ANALISIS","GIRO_COMPARATIVO_NO_EXPLICADO"]` |
| `2026-10-31_sequias-energia-renovable` | FAIL | 56 | `lectura_en_frio_solo_narracion` | AUSENTE_EN_JSON | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":false,"progresion_por_escena":false,"transiciones_causales":false,"giro_cientifico_explicado":false,"limite_evidencia_explicito":true,"payoff_cierre_apertura":false}` | `["GANCHO_DEFINICIONAL","CIFRAS_SIN_DIRECCION_INTERPRETABLE","GIRO_SOLO_NOMBRADO","PAYOFF_NO_DERIVADO_DE_LA_EVIDENCIA"]` |
| `2026-11-01_dato-cambio-horario-corazon` | FAIL | 84 | `lectura_en_frio_solo_narracion` | 2026-11-01T18:08:00-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `["CIERRE_PRESELLO_INFERIOR_A_110_CARACTERES"]` |
| `2026-11-01_llorar-cebolla-quimica` | FAIL | 79 | `lectura_en_frio_solo_narracion` | 2026-11-01T15:09:29-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":false,"payoff_cierre_apertura":false}` | `["CIERRE_ATRIBUYE_INTENCION_EVOLUTIVA_NO_DEMOSTRADA","LIMITE_DE_EVIDENCIA_NO_EXPLICITO"]` |
| `2026-11-01_pulpo-tres-corazones` | FAIL | 72 | `lectura_en_frio_solo_narracion` | 2026-11-01T15:09:29-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":false,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":false,"payoff_cierre_apertura":true}` | `["APERTURA_HIPOTETICA_NO_IN_MEDIAS_RES","ANALOGIA_BRANQUIAS_SACAR_AIRE_DEL_AGUA_IMPRECISA","AFIRMACION_CORAZONES_NO_SUSTITUIBLES_SIN_RESPALDO"]` |
| `2026-11-01_red-electrica-pulso-minuto` | PASS | 89 | `lectura_en_frio_solo_narracion` | 2026-11-01T15:09:29-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `[]` |
| `2026-11-02_camaron-mantis` | PASS | 90 | `lectura_en_frio_solo_narracion` | AUSENTE_EN_JSON | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `[]` |
| `2026-11-02_comida-pan-duro` | FAIL | 84 | `lectura_en_frio_solo_narracion` | AUSENTE_EN_JSON | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `["CIERRE_SOBREAFIRMA_Y_CONTRADICE_LIMITE_DE_SECADO"]` |
| `2026-11-04_cielo-azul-atardecer-rojo` | PASS | 94 | `lectura_en_frio_solo_narracion` | 2026-11-04T15:58:40-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `[]` |
| `2026-11-05_comida-palomitas` | FAIL | 82 | `lectura_en_frio_solo_narracion` | 2026-11-16T15:45:46-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":false,"progresion_por_escena":false,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `["APERTURA_DEFINICIONAL_NO_IN_MEDIAS_RES","ESCENA_6_REITERA_CAUSAS_DE_GRANOS_NO_REVENTADOS_SIN_INFORMACION_NUEVA"]` |
| `2026-11-05_inter-arboles-se-comunican` | FAIL | 78 | `lectura_en_frio_solo_narracion` | 2026-11-16T15:45:46-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":false,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `["APERTURA_GENERICA_NO_IN_MEDIAS_RES"]` |
| `2026-11-05_inter-rayo-globular` | FAIL | 81 | `lectura_en_frio_solo_narracion` | 2026-11-16T15:45:46-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":false,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `["APERTURA_HISTORICA_DESCRIPTIVA_NO_IN_MEDIAS_RES"]` |
| `2026-11-05_kids-dia-en-venus` | PASS | 88 | `lectura_en_frio_solo_narracion` | 2026-11-16T15:45:46-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `[]` |
| `2026-11-06_comida-aguacate-negro` | FAIL | 79 | `lectura_en_frio_solo_narracion` | 2026-11-16T15:45:46-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":false,"transiciones_causales":false,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `["REPETICION_ESCENAS_5_6_SIN_AVANCE_CAUSAL"]` |
| `2026-11-06_inter-arena-cantante` | PASS | 94 | `lectura_en_frio_solo_narracion` | 2026-11-16T15:45:46-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `[]` |
| `2026-11-06_inter-ranas-congeladas` | FAIL | 83 | `lectura_en_frio_solo_narracion` | 2026-11-16T15:45:46-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":false,"transiciones_causales":false,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `["REPETICION_ESCENAS_5_6_LIMITES_DE_ESPECIE_Y_CONDICIONES"]` |
| `2026-11-06_kids-ballena-azul-corazon` | FAIL | 80 | `lectura_en_frio_solo_narracion` | 2026-11-16T15:45:46-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":false}` | `["PAYOFF_SOBREAFIRMA_CASI_SE_DETIENE"]` |
| `2026-11-07_comida-hielo-caliente` | FAIL | 81 | `lectura_en_frio_solo_narracion` | 2026-11-16T15:45:46-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":false,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `["APERTURA_DE_CREENCIAS_NO_IN_MEDIAS_RES"]` |
| `2026-11-07_inter-nubes-pesan` | FAIL | 78 | `lectura_en_frio_solo_narracion` | 2026-11-16T15:45:46-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":false,"transiciones_causales":false,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":false}` | `["ESCENA_7_REITERA_CIFRA_Y_LIMITE_SIN_PAYOFF_DE_SUSPENSION"]` |
| `2026-11-07_inter-pulpo-suenos` | FAIL | 72 | `lectura_en_frio_solo_narracion` | 2026-11-16T15:45:46-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":false,"transiciones_causales":false,"giro_cientifico_explicado":false,"limite_evidencia_explicito":false,"payoff_cierre_apertura":false}` | `["FUENTE_PRIMARIA_CORRESPONDE_A_OCTOPUS_LAQUEUS_NO_INSULARIS","REPETICION_ESCENAS_5_6_Y_PAYOFF_VAGO"]` |
| `2026-11-07_kids-huesos-bebe` | FAIL | 82 | `lectura_en_frio_solo_narracion` | 2026-11-16T15:45:46-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":false,"transiciones_causales":false,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `["ESCENA_6_REPITE_VARIACION_DE_CONTEO_Y_FUSION"]` |
| `2026-11-09_dato-robot-ensambla-orbita` | PASS | 90 | `lectura_en_frio_solo_narracion` | 2026-11-09T18:45:00-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `[]` |
| `2026-11-10_comida-aprendizaje-sabor-nutriente` | PASS | 92 | `lectura_en_frio_solo_narracion` | 2026-11-10T15:47:50-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `[]` |
| `2026-11-10_dato-adn-sincroniza-flujo` | PASS | 91 | `lectura_en_frio_solo_narracion` | 2026-11-10T16:16:00-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `[]` |
| `2026-11-12_dato-pedorreta-chimpances` | PASS | 91 | `lectura_en_frio_solo_narracion` | 2026-11-12T15:38:50-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `[]` |
| `2026-11-13_dato-caracol-16-embriones` | PASS | 91 | `lectura_en_frio_solo_narracion` | 2026-11-13T15:42:39-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `[]` |
| `2026-11-14_dato-microplasticos-pantanal` | PASS | 88 | `lectura_en_frio_solo_narracion` | 2026-11-14T15:04:13-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `[]` |
| `2026-11-15_dato-dia-diapausa-lestes-sponsa` | PASS | 90 | `lectura_en_frio_solo_narracion` | 2026-11-15T15:51:23-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `[]` |
| `2026-11-15_dato-quasar-pareja-cosmic-dawn` | FAIL | 82 | `lectura_en_frio_solo_narracion` | 2026-11-15T15:51:23-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":false,"transiciones_causales":false,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `["ESCENA_002_REITERA_GEMINI_NORTH_Y_NO_AVANZA_LA_PREGUNTA","TRANSICION_002_003_NO_CAUSAL"]` |

| `2026-11-16_dato-polen-desenreda-nanotubos` | PASS | 91 | `lectura_en_frio_solo_narracion` | 2026-11-16T15:45:46-06:00 | `{"pregunta_central_reconstruible":true,"apertura_in_medias_res":true,"progresion_por_escena":true,"transiciones_causales":true,"giro_cientifico_explicado":true,"limite_evidencia_explicito":true,"payoff_cierre_apertura":true}` | `[]` |

### Registro con narrative_qa.status=PENDIENTE

`2026-11-04_dato-polvo-atrapa-oro`: `status=PENDIENTE`; `score=AUSENTE_EN_JSON`; `review_basis=lectura_en_frio_solo_narracion`; `reviewed_at=AUSENTE_EN_JSON`; `checks=AUSENTE_EN_JSON`; `critical_flags=AUSENTE_EN_JSON`. El JSON conserva `reviewer_role=pendiente_auditor_capcot_independiente` y la nota: “Sin auditor independiente disponible antes del slot; autoauditoría Grok Bot: balazo in medias res, ¿y a mí qué? en esc. 2, límite en esc. 7, giro+pregunta+sello en esc. 8.” No se interpreta como PASS ni como QA independiente.

### Proyectos sin narrative_qa — PENDIENTE_AUDITOR

`2026-10-24_abejas-bullying`, `2026-10-24_aves-temen-mas-a-mujeres`, `2026-10-24_fenomeno-el-nino`, `2026-10-24_ideonella-pet`, `2026-10-24_osedax-comehuesos`, `2026-10-24_serpientes-que-ruedan`, `2026-10-25_ave-jurasica-sin-vuelo`, `2026-10-25_corales-contacto`, `2026-10-25_reina-olor`, `2026-10-25_sueno-electricidad-qom`, `2026-10-26_baffin-bay-ice-shelf`, `2026-10-26_catrina-posada-monerismo`, `2026-10-26_hongo-gente-diminuta`, `2026-10-26_papel-picado-dia-muertos`, `2026-10-26_papel-picado-dia-muertos_parte2`, `2026-10-26_pimiento-verde-rojo`, `ddm-parte3-pomuch`, `2026-10-28_ddm-parte4-templo-mayor`, `2026-10-28_familia-voyager-disco-oro`, `2026-10-28_kids-titanoboa`, `2026-10-28_monarca-almas`, `2026-10-28_mosquito-fruitless-audicion`, `2026-10-28_noct-lince-milanos`, `2026-10-28_pan-de-muerto-huesos`, `2026-10-29_juno-choque-proa`, `2026-10-29_muralismo-cu`, `2026-10-30_arqueas-origen-eucariotas`, `2026-10-30_kromdraai-primera-fecha`, `2026-10-31_pardelas-jetlag-solar`, `2026-10-31_smartpe-edicion-plantas`, `2026-11-01_dato-xolo-mictlan`, `2026-11-03_comida-maillard`, `2026-11-03_dato-polvo-africano-microbios`, `2026-11-03_enzimas-incrustadas-oceano`, `2026-11-03_kids-leche-enchilado`, `2026-11-03_kids-tiburon-groenlandia`, `2026-11-04_comida-miel-no-caduca`, `2026-11-04_inter-bioluminiscencia-mar`, `2026-11-04_kids-hipo-por-que`, `2026-11-05_comida-palomitas-explotan`, `2026-11-05_inter-arboles-mito-respiran`, `2026-11-05_inter-venus-dia-largo`, `2026-11-06_inter-corazon-ballena-azul`, `2026-11-07_dato-clavo-te-cocina`, `2026-11-07_inter-mpemba-mito`, `2026-11-07_inter-suenos-pulpo`, `2026-11-11_dato-ratas-topo-damaraland`, `2026-11-xx_kids-flamencos-rosas`, `cempasuchil-ciencia`, `corneja-decision-rapida`, `demo-001`, `familia-ajolote`, `guiones_lote_01`, `kids-serpiente-voladora`, `lote01-01-el-nino`, `lote01-02-petroleo`, `lote01-03-balon-curva`, `lote01-04-tardigrado`, `lote01-05-chicxulub`, `noct-anfibio-marino`, `2026-11-17_dato-suelo-dos-relojes`

El storyboard `2026-11-16_dato-polen-desenreda-nanotubos` ya contiene `narrative_qa=PASS` (91; revisión independiente del 2026-11-16). El nuevo borrador `2026-11-17_dato-suelo-dos-relojes` no contiene `narrative_qa` y queda **PENDIENTE_AUDITOR**. La revisión en frío corresponde al auditor independiente.



### Archivo canónico faltante

- `MISSING_CANONICAL_FILE`: `2026-11-04_machu-picchu-fallas-pisa` figuraba en el radar anterior, pero no existe `storyboard.json` en el árbol actual. Se mantiene la exclusión histórica; no se reconstruye ni sustituye.
