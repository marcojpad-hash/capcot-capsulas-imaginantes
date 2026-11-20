# RADAR CAPCOT — 2026-11-20

**Serie:** Datos y ociosidades  
**Corte:** 2026-11-20, 08:00 America/Mexico_City  
**Rama de trabajo:** `feature/capcot-video-discovery-continuity`  
**HEAD feature al corte:** `f92871ea7ba8e46bf96fb70595eaed590804b3e8`  
**HEAD main consultado en solo lectura:** `05e842dc55577461e63d8f5de13fba96c46ff5f1`  
**Resultado operativo:** `SOLO_RADAR` · `NO_DUPLICAR` en todos los slots aplicables. No se creó storyboard nuevo porque no existe un slot autorizado libre.

## 1. Decisión de staging y guardia cruzada

Se enumeraron los árboles actuales de `proyectos/`, `salidas/`, `cola/entrada/`, `cola/bloqueados/`, `handoffs/grok_inbox/` y `cola/estado/` en feature, y se contrastaron los registros de publicación, programación y paquetes de main.

| Slot CDMX | Evidencia actual | Estado de ocupación |
|---|---|---|
| 07:00 | En **main**, `data/publicaciones.json` contiene `2026-11-17_resubida_flamenco`, YouTube ID `msWV2AXr6Uk`, `publishAt=2026-11-20T13:00:00Z`, hora local 07:00 | `CONFLICTO_DE_SLOT_ENTRE_RAMAS` / `NO_DUPLICAR` |
| 13:30 | En **main**, `2026-11-01_mxenes-ia-descubrimiento`, YouTube ID `WTlFSZV9HYg`, `publishAt=2026-11-20T19:30:00Z`; su `programacion.json` registra YouTube, TikTok y Facebook programados a las 13:30 CDMX | `CONFLICTO_DE_SLOT_ENTRE_RAMAS` / `NO_DUPLICAR` |
| 17:00 | En **feature**, `2026-11-20_dato-marea-cerebral-en-sueno`, `fecha_objetivo=2026-11-20`, `slot_local=17:00`, `slot_cesta=intermedio_1` | `NO_DUPLICAR` |
| 23:30 | En **feature**, `2026-11-20_dato-dia-atlantico-humedad-sapropeles`, `fecha_objetivo=2026-11-20`, `slot_local=23:30`, `slot_cesta=dato_del_dia` | `NO_DUPLICAR` |
| 19:00 | Retirado por la política de horarios vigente; no se reutiliza como hueco | No autorizado |

**Conclusión de ocupación:** los dos slots de feature que corresponden a la producción principal y al dato del día ya tienen storyboard. Los slots 07:00 y 13:30 tienen evidencia de publicación/programación en main para la misma fecha. No se crea una segunda versión para ninguno. El slot 23:30 sí tiene una fuente publicada el mismo día —el estudio de sapropeles—, pero ya está ocupado; por tanto corresponde `NO_DUPLICAR`, no `PENDING_SOURCE`.

### Diferencias de horario entre ramas

- `feature/data/horarios.json` fue actualizado el 2026-11-09: política activa con ventanas 06:30–07:30 y 16:30–18:00, más el slot fijo 23:30; 13:30 permanece en prueba y 19:00 está retirado.
- `main/data/horarios.json` fue actualizado el 2026-11-16: ventanas 06:30–07:30 y 13:00–14:30, más 23:30 fijo; 16:30–18:00 queda en prueba.
- No existe `data/horario_2026-11-20.json` en feature.
- `scripts/rotacion.py` conserva cinco ventanas de código (07:00, 13:30, 17:00, 19:00 y 23:30), mientras las políticas fechadas de `data/horarios.json` ya no coinciden exactamente con esas cinco ventanas. Se registra la discrepancia; no se modifica el código ni ningún JSON de datos.
- `feature/data/publicaciones.json` conserva 22 registros y llega a 2026-10-31; main contiene 48 registros y sí incluye las dos reservas del 20-nov. La rama principal se consultó solo como guardia de colisión; no se modificó.

### Control previo que quedó obsoleto

`docs/briefs/2026-11-20_CONTROL_COLA.md` tiene corte 00:35 CDMX y afirma que aún no había proyectos del 20-nov. La lectura actual de GitHub a HEAD feature confirma dos storyboards creados después de ese corte. Para la decisión de hoy prevalece el inventario actual, no la afirmación histórica del control de las 00:35.

### Recepción de Grok

- `cola/estado/2026-11-20_dato-marea-cerebral-en-sueno.json`: 404.
- `cola/estado/2026-11-20_dato-dia-atlantico-humedad-sapropeles.json`: 404.
- `handoffs/grok_inbox/` solo contiene el marker histórico del 09-nov y su README; no hay marker de los dos proyectos actuales.
- Estado para ambos: `RECEPCION_GROK_NO_CONFIRMADA`. No se crea ni modifica ningún archivo de estado o marker.

## 2. Candidatos científicos (publicados del 13 al 20 de noviembre)

La ventana de búsqueda fue 2026-11-13 a 2026-11-20, inclusive. Los dos primeros candidatos ya están representados por los storyboards existentes de hoy; se documentan como material preexistente, no como publicaciones ni como trabajo creado en esta ejecución.

### Candidato A — Ondas de líquido cefalorraquídeo durante el sueño y envejecimiento

- **Novedad observada:** el estudio compara adultos jóvenes de 18–39 años con adultos mayores de 60–84 durante el sueño nocturno. Reporta ondas de flujo de LCR reducidas en el grupo mayor y relaciona la diferencia con potencia EEG de ondas lentas, oscilaciones hemodinámicas y atrofia de materia gris.
- **Fuente primaria:** Bailes, S. M.; Williams, S. D.; Ashenagar, B.; Pham, T. L. D.; Valdiviezo, Z.; Licata, J.; Bosli, M. Y.; Dormes, B. J.; Yun, H. J.; Zimmerman, D.; Hernandez Moyers, A.; Salat, D. H.; Lewis, L. D. (2026). “The aging human brain exhibits reduced hemodynamic and cerebrospinal fluid flow waves during sleep”. *Nature Aging*. Publicado 2026-11-13.
- **DOI:** 10.1038/s43587-026-01270-4. **Estado:** `PENDIENTE_RESOLVEDOR`; PubMed confirma DOI, fecha, autoría y resumen, pero Crossref y el resolvedor DOI no fueron accesibles en esta ejecución. La apertura directa de Nature devolvió HTTP 500 y redirección a `idp.nature.com`.
- **Enlaces:** [PubMed, PMID 43026299](https://pubmed.ncbi.nlm.nih.gov/43026299/) · [Nature Aging](https://www.nature.com/articles/s43587-026-01270-4).
- **Línea:** dato científico / cuerpo y cerebro.
- **Tendencia:** sin señal científica clara en las primeras 25 tendencias de Google Trends México.
- **Relevancia científica:** alta; mide fisiología humana durante sueño con EEG y fMRI.
- **Oportunidad editorial:** alta, por el mecanismo acoplado de ondas neuronales, cambios vasculares y flujo de LCR.
- **Público/ocasión:** público general interesado en sueño, cerebro y salud.
- **Riesgos:** no afirmar que el estudio midió limpieza de desechos, eliminación de proteínas, prevención de Alzheimer ni riesgo individual. El resultado es una diferencia promedio de señal/flujo entre grupos.
- **Material preexistente:** `2026-11-20_dato-marea-cerebral-en-sueno`, 17:00. El storyboard actual usa 218 palabras, 8 escenas y 84 s; estructura `comparacion`, estilo `neon_noir`. Su narración escribe 60–83 años, mientras el registro primario de PubMed indica 60–84. **Discrepancia factual para el auditor/autor; no se corrigió ni reescribió el storyboard.**
- **QA narrativo:** `PENDIENTE_AUDITOR`; no existe `narrative_qa`.

### Candidato B — Humedad atlántica, salinidad mediterránea y sapropeles

- **Novedad observada:** reconstrucción de 350 mil años que compara precipitación invernal del margen ibérico atlántico, inferida mediante Ln(Zr+Ti)/K en sedimentos de Site U1385, con salinidad superficial del Mediterráneo occidental. Los episodios de baja salinidad y sapropeles coinciden con mayor precipitación invernal en el margen ibérico.
- **Fuente primaria:** Sierro, F. J.; Jimenez-Espejo, F. J.; Tarruella, J. P.; et al. (2026). “Mediterranean low-salinity and anoxic sapropel events triggered by Atlantic atmospheric moisture”. *Nature Geoscience*. Publicado 2026-11-20.
- **DOI:** 10.1038/s41561-026-02141-8. **Estado:** `PENDIENTE_RESOLVEDOR`; DOI y fecha aparecen en el registro editorial de Nature, pero Crossref y el resolvedor DOI no fueron accesibles. La apertura directa de Nature devolvió HTTP 500 y redirección a `idp.nature.com`.
- **Enlace:** [Artículo en Nature Geoscience](https://www.nature.com/articles/s41561-026-02141-8).
- **Línea:** actualidad / clima y geociencias.
- **Tendencia:** no apareció como señal científica en Google Trends México.
- **Relevancia científica:** alta; conecta un proxy sedimentario de lluvia atlántica con salinidad y ventilación profunda mediterráneas.
- **Oportunidad editorial:** alta por la conexión geográfica no intuitiva entre el Atlántico y la sal del Mediterráneo.
- **Público/ocasión:** público general interesado en océanos, clima y pasado terrestre.
- **Riesgos:** la precipitación se reconstruye mediante proxies; el clima antiguo no fue observado directamente. La asociación con fases negativas de la oscilación del Atlántico Norte se presenta como potencial, no como causa demostrada de cada evento.
- **Material preexistente:** `2026-11-20_dato-dia-atlantico-humedad-sapropeles`, 23:30 / `dato_del_dia`. El storyboard actual usa 215 palabras, 8 escenas y 84 s; estructura `pregunta`, estilo `linograbado`. No se crea otra versión.
- **QA narrativo:** `PENDIENTE_AUDITOR`; no existe `narrative_qa`.

### Candidato C — Una intrusión volcánica liberó metano sin erupción

- **Novedad observada:** satélites midieron un episodio de metano y CO₂ en Fentale, Etiopía, después de una intrusión magmática de 2025. El artículo estima al menos 38.2 ± 3.9 kt de CH₄ en tres meses y 2.9 ± 1.0 Mt de CO₂ en 14 días; la tasa máxima de metano estimada fue 157 ± 41 t/h. El volcán no estaba en erupción.
- **Fuente primaria:** Dualeh, E. W.; Biggs, J.; Sharma, S.; et al. (2026). “Methane outburst driven by magma–sediment interactions at Fentale Volcano detected by satellite”. *Nature Geoscience*. Publicado y versión de registro: 2026-11-19.
- **DOI:** 10.1038/s41561-026-02137-4. **Estado:** `PENDIENTE_RESOLVEDOR`; el registro editorial indexado ofrece autoría, resumen, métodos, fecha y DOI, pero Crossref y el resolvedor DOI no fueron accesibles. La apertura directa de Nature devolvió HTTP 500 y redirección a `idp.nature.com`.
- **Enlace:** [Artículo en Nature Geoscience](https://www.nature.com/articles/s41561-026-02137-4).
- **Línea:** actualidad / clima y geociencias.
- **Tendencia:** no apareció como tendencia científica en las primeras 25 consultas de México.
- **Relevancia científica:** alta; identifica una fuente episódica de metano y CO₂ que puede faltar en inventarios de emisiones naturales.
- **Oportunidad editorial:** muy alta; el giro “volcán sin erupción, pero con una gran descarga de gas” permite una historia visual clara.
- **Público/ocasión:** público general interesado en volcanes, satélites y cambio climático.
- **Riesgos:** el episodio ocurrió en 2025 y el artículo se publicó en 2026; no presentarlo como una descarga de hoy. Los autores proponen que la intrusión fracturó un sello y liberó metano termogénico de sedimentos ricos en hidrocarburos; no afirmar que el magma produjo directamente todo el metano. El artículo señala que no hay mediciones isotópicas directas en Fentale y que el episodio es pequeño frente a las emisiones anuales de la industria de petróleo y gas.
- **Oportunidad para siguiente slot:** primera recomendación cuando haya hueco, después de resolver el DOI. No se crea storyboard hoy porque los slots están ocupados.

### Candidato D — Un púlsar gamma descubierto con una búsqueda basada en retículos

- **Novedad observada:** el equipo reporta el primer púlsar gamma descubierto con una extensión de un algoritmo basado en vectores cortos en retículos de alta dimensión. Identificó PSR J1622−7204, aislado y girando a 261 Hz, en 15 años de datos Fermi-LAT usando alrededor de 10 horas de CPU. El método semicoherente anterior había fallado tras aproximadamente 600 años de CPU.
- **Fuente primaria:** Pook-Kolb, D.; Gazith, D.; Clark, C. J.; Agrell, E.; Zackay, B.; Allen, B. (2026). “Gamma-Ray Pulsar Discovery Using a Lattice-Based Method”. *Physical Review Letters* 137, 211201. Publicado 2026-11-19.
- **DOI:** 10.1103/vlt2-xzgk. **Estado:** `VERIFICADO_RESOLVEDOR`; el enlace DOI resolvió a la página editorial de APS, que confirma título, autoría, fecha, DOI y resumen.
- **Enlaces:** [Artículo en Physical Review Letters](https://journals.aps.org/prl/abstract/10.1103/vlt2-xzgk) · [DOI](https://doi.org/10.1103/vlt2-xzgk).
- **Línea:** actualidad / espacio y tecnología.
- **Tendencia:** sin señal científica visible en el primer bloque de Google Trends México.
- **Relevancia científica:** alta; es una aplicación observacional de un algoritmo de búsqueda en datos extremadamente dispersos.
- **Oportunidad editorial:** alta; la comparación de coste computacional ofrece un giro cuantificable y fácil de visualizar.
- **Público/ocasión:** público general interesado en astronomía, espacio y computación.
- **Riesgos:** “10 horas” y “600 años” son presupuestos de CPU reportados, no tiempos de calendario comparables de dos ejecuciones en idénticas condiciones. No decir que el método garantiza descubrir todos los púlsares ni que el algoritmo es una IA; el artículo describe una búsqueda basada en retículos.
- **Alternativa verificada:** si Fentale continúa sin resolución DOI, este es el candidato con verificación de enlace más sólida para el siguiente slot libre.

## 3. Separación de señales y recomendación

- **OBSERVADO — tendencia:** la página oficial Google Trends México muestra 179 tendencias en las últimas 24 horas. Entre las primeras 25 aparecen principalmente búsquedas generales, deportes, entretenimiento y actualidad local (por ejemplo, “cajero”, “accidente”, “Luis de Llano Macedo”, “Bruno Mars” y “Texans - Colts”). “Fiona hipopótamo” aparece con 2 mil+ búsquedas, pero no se encontró una noticia científica primaria asociada en esta revisión.
- **OBSERVADO — relevancia científica:** Fentale y sapropeles aportan hallazgos de geociencias; el púlsar aporta un método computacional con resultado observacional; el estudio de LCR aporta fisiología humana. La tendencia de búsqueda no equivale a calidad científica.
- **CÁLCULO:** los cuatro candidatos caen dentro de la ventana editorial de siete días (13–20 nov). La ocupación observada cubre los slots 07:00, 13:30, 17:00 y 23:30; 19:00 está retirado. No queda slot libre para crear un storyboard en esta ejecución.
- **INFERENCIA EDITORIAL:** Fentale ofrece el mejor giro visual inmediato; el púlsar ofrece la verificación DOI más firme y un contraste computacional claro. Ninguno debe desplazarse a un slot ocupado.
- **RECOMENDACIÓN:** conservar Fentale como primera opción para el siguiente slot realmente libre, condicionada a resolver DOI/Crossref; usar el púlsar como alternativa si el resolver de Fentale sigue pendiente. No seleccionar estilo, estructura ni redactar storyboard hasta confirmar el hueco y volver a consultar la rotación vigente.

## 4. RSS y respaldo Google Trends

Se consultaron las diez URL declaradas en `scripts/tendencias.py` y el RSS de Google Trends México mediante el lector web disponible. **No se parseó XML** y no se ejecutó `scripts/tendencias.py`; los errores siguientes son los devueltos por el lector web, no una afirmación de que el servidor de origen esté caído:

| Feed | Resultado exacto |
|---|---|
| ScienceDaily Science | `(400) Unsupported content-type: application/xml` |
| ScienceDaily Health | `(400) Unsupported content-type: application/xml` |
| ScienceDaily Space | `(400) Unsupported content-type: application/xml` |
| Phys.org | `(400) Unsupported content-type: text/xml` |
| NASA News Release | `(400) Unsupported content-type: application/rss+xml` |
| ESA Space Science | `(404) Not Found` |
| Nature RSS | `(400) Unsupported content-type: application/rss+xml` |
| EurekAlert | `URL https://www.eurekalert.org/rss/news.xml is not accessible via this tool.` |
| SINC | `URL https://www.agenciasinc.es/rss is not accessible via this tool.` |
| UNAM Global | `(400) Unsupported content-type: application/rss+xml` |
| Google Trends RSS MX | `URL https://trends.google.com/trending/rss?geo=MX is not accessible via this tool.` |

**Respaldo oficial consultado:** [Google Trends — Tendencias actuales, México](https://trends.google.com/trending?geo=MX&hl=es), filtro “Últimas 24 horas”. La página muestra 179 tendencias; la primera página contiene 25. No se infiere volumen absoluto ni demanda de audiencia CAPCOT a partir de estos buckets.

## 5. Seguimiento técnico Meta / Google Trends

Se compararon las referencias oficiales actuales con `docs/INVESTIGACION_API_META_Y_GOOGLE_TRENDS.md` (último corte documental: 2026-11-19).

- **Graph API:** el changelog oficial sigue declarando v27.0 como versión más reciente, introducida el 2026-11-04. Coincide con el registro del 19-nov; no se encontró una nueva versión o cambio de endpoint relevante para CAPCOT.
- **Instagram Insights:** la guía mantiene Unified Login, Instagram Login y Facebook Login con tokens, hosts y permisos distintos; conserva los límites de acceso y retención ya registrados. No apareció una nueva métrica de Insights en esta revisión.
- **Facebook Page Insights:** la referencia sigue mostrando v27.0, mínimo de 100 likes, actualización aproximada cada 24 h, retención de dos años, consultas de hasta 90 días, umbral demográfico de 100 personas y exclusión de interacciones de Reels. Sin cambio nuevo relevante.
- **Google Trends API alfa:** continúa con acceso limitado mediante solicitud, ventana móvil de cinco años, agregaciones diaria/semanal/mensual/anual, regiones/subregiones y escala consistente. Sin cambio nuevo relevante.

**Decisión técnica:** no actualizar `docs/INVESTIGACION_API_META_Y_GOOGLE_TRENDS.md`. No se hicieron llamadas autenticadas, no se modificaron conectores, permisos, OAuth, versiones configuradas ni credenciales.

## 6. Estado de QA narrativo preexistente

No se ejecutó QA nuevo ni se alteró ningún `narrative_qa`. Los campos se transcriben de los JSON actuales. Los dos storyboards del 20-nov no tienen la propiedad `narrative_qa`, por lo que su estado es `PENDIENTE_AUDITOR`.

**Nombres de los siete checks, en este orden:** `pregunta_central_reconstruible`, `apertura_in_medias_res`, `progresion_por_escena`, `transiciones_causales`, `giro_cientifico_explicado`, `limite_evidencia_explicito`, `payoff_cierre_apertura`.

| project_id | status / score | review_basis | reviewed_at | Checks (orden anterior) | critical_flags |
|---|---|---|---|---|---|
| `2026-11-20_dato-marea-cerebral-en-sueno` | PENDIENTE_AUDITOR | no existe `narrative_qa` | no existe | no existen | no existen |
| `2026-11-20_dato-dia-atlantico-humedad-sapropeles` | PENDIENTE_AUDITOR | no existe `narrative_qa` | no existe | no existen | no existen |
| `2026-11-19_dato-dia-luz-dos-manos-oro-poroso` | PASS / 91 | `lectura_en_frio_solo_narracion` | 2026-11-19T15:04:50-06:00 | true, true, true, true, true, true, true | [] |
| `2026-11-19_dato-estrella-dentro-de-estrella` | PASS / 90 | `lectura_en_frio_solo_narracion` | 2026-11-19T15:04:50-06:00 | true, true, true, true, true, true, true | [] |
| `2026-11-18_dato-catorce-campos-hidrotermales` | FAIL / 68 | `lectura_en_frio_solo_narracion` | 2026-11-19T15:04:50-06:00 | false, true, false, false, false, true, false | [`PREGUNTA_CENTRAL_NO_RECONSTRUIBLE`, `SECUENCIA_DE_HALLAZGOS_SIN_PROGRESION_CAUSAL`, `GIRO_CIENTIFICO_NOMBRADO_PERO_NO_EXPLICADO`, `CIERRE_RESUMEN_SIN_PAYOFF`] |
| `2026-11-18_dato-kuroshio-puente-atmosferico` | PASS / 90 | `lectura_en_frio_solo_narracion` | campo ausente en JSON | true, true, true, true, true, true, true | [] |
| `2026-11-17_dato-suelo-dos-relojes` | PASS / 89 | `lectura_en_frio_solo_narracion` | 2026-11-17T15:35:22-06:00 | true, true, true, true, true, true, true | [] |
| `2026-11-16_dato-polen-desenreda-nanotubos` | PASS / 91 | `lectura_en_frio_solo_narracion` | 2026-11-16T15:45:46-06:00 | true, true, true, true, true, true, true | [] |
| `2026-11-15_dato-dia-diapausa-lestes-sponsa` | PASS / 90 | `lectura_en_frio_solo_narracion` | 2026-11-15T15:51:23-06:00 | true, true, true, true, true, true, true | [] |
| `2026-11-15_dato-quasar-pareja-cosmic-dawn` | FAIL / 82 | `lectura_en_frio_solo_narracion` | 2026-11-15T15:51:23-06:00 | true, true, false, false, true, true, true | [`ESCENA_002_REITERA_GEMINI_NORTH_Y_NO_AVANZA_LA_PREGUNTA`, `TRANSICION_002_003_NO_CAUSAL`] |
| `2026-11-11_dato-ratas-topo-damaraland` (bloqueados) | PASS / 91 | `lectura_en_frio_solo_narracion` | 2026-11-20T01:57:46-06:00 | true, true, true, true, true, true, true | [] |
| `2026-11-07_dato-clavo-te-cocina` (bloqueados) | FAIL / 82 | `lectura_en_frio_solo_narracion` | 2026-11-20T01:57:46-06:00 | true, true, true, true, true, false, true | [`CIFRAS_SIN_UNIDAD_Y_CONDICIONES_DE_ENSAYO_INSUFICIENTES`] |

Los QA PASS anteriores no se repitieron ni se transfirieron a otras versiones. Los dos proyectos actuales permanecen en `proyectos/`; ninguno fue promovido a `cola/entrada/`.

## 7. Rotación, continuidad y límites de ejecución

- `data/temas_del_dia.json` llega a 2026-10-28; `data/rotacion.json` a 2026-10-31; `data/estilos_usados.json` a 2026-10-28. Son históricos incompletos y permanecen intactos.
- Se leyó `scripts/registro_editorial.py` (recorre `storyboard.json` recursivamente en proyectos, cola y salidas; inventaría handoffs por separado) y `scripts/rotacion.py`. No se afirma haber ejecutado el script: la comprobación se hizo mediante lectura del código y de los árboles/archivos actuales de GitHub.
- Los estilos ya presentes hoy son `neon_noir` para 17:00 y `linograbado` para 23:30. No se selecciona ni repite estilo nuevo porque no se crea storyboard.
- No se modificaron storyboards existentes, `data/*.json`, main, workflows, motores canónicos ni Motor U6.
- No se crearon frames, imágenes, audio, voz, video ni renders; no se publicó ni programó contenido; no se consumieron créditos.
- No se creó `narrative_qa`, no se hizo promoción, no se creó ni editó `cola/estado/`, y no se declaró recepción de Grok.

**Entregables de esta ejecución:** únicamente este radar. No se creó storyboard principal ni storyboard 23:30 porque los slots están ocupados.

## Corrección de auditoría posterior — 2026-11-20, 12:26 CDMX

Esta nota no cambia el storyboard ni repite su QA narrativo; corrige la interpretación de fuente y amplía la guardia de producción:

- **Marea cerebral:** el abstract presenta el grupo mayor como 60–84 años, pero Methods §“Participant population and exclusion criteria”, después de excluir participantes por movimiento, deja 41 adultos mayores de 60–83 años en el análisis nocturno. La narración del storyboard (60–83) describe la muestra analítica final y es correcta; no hay discrepancia factual. El DOI aparece en la página/PDF editorial, pero Crossref/doi.org no completaron; `doi_verification_status` sigue `PENDIENTE_RESOLVEDOR`.
- **Sapropeles:** Nature Geoscience muestra en su ficha editorial título, DOI y publicación/versión de registro del 20-nov-2026; la apertura HTML directa redirige a autenticación y Crossref/doi.org no completaron. Se conserva `PENDIENTE_RESOLVEDOR`; no se declara DOI verificado por Crossref.
- **Guardia adicional en main:** `2026-11-20_react-proteinas-microbios` tiene `programacion.json` con 13:45 CDMX (`publish_at=2026-11-20T19:45:00Z`) y storyboard en `proyectos/` y `cola/entrada/`. Se clasifica `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`. El JSON declara `export.filename=capsula.mp4`, pero el MP4 no se encontró en `cola/entrada/<id>/`, `proyectos/<id>/` ni `salidas/<id>/`: `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`. No hay estado Grok individual ni publicación confirmada. No colisiona exactamente con los storyboards de feature de 17:00 y 23:30, pero se cuenta para la capacidad diaria.
- **Recepción de los dos borradores feature:** `cola/estado/<project_id>.json`, `handoffs/grok_inbox/<project_id>.json` y las rutas de cola/salidas comprobadas devuelven 404. Ambos siguen `RECEPCION_GROK_NO_CONFIRMADA` y `NOT_DISPATCHABLE`; no se promueven.
- **Horarios:** `feature/data/horarios.json` habilita 06:30–07:30 y 16:30–18:00 más 23:30 fijo; `main/data/horarios.json` habilita 06:30–07:30 y 13:00–14:30 más 23:30. `scripts/rotacion.py` conserva cinco ventanas de código (07:00, 13:30, 17:00, 19:00, 23:30). La divergencia permanece documentada; no se modificó ningún `data/*.json` ni el código de rotación.
