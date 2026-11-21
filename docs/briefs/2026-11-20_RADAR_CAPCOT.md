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
- **Material preexistente:** `2026-11-20_dato-marea-cerebral-en-sueno`, 17:00. El storyboard usa 218 palabras, 8 escenas y 84 s; estructura `comparacion`, estilo `neon_noir`. La narración 60–83 coincide con los 41 participantes mayores que permanecen en el análisis nocturno después de las exclusiones por movimiento descritas en Methods; el abstract presenta el grupo general como 60–84. No existe discrepancia factual para la muestra analítica narrada.
- **QA narrativo:** `PASS 92/100` en auditoría independiente posterior al corte del radar; siete checks true y `critical_flags=[]`.

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
- **QA narrativo:** `PASS 91/100` en auditoría independiente posterior al corte del radar; siete checks true y `critical_flags=[]`.

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

## 6. Estado de QA narrativo al corte del radar (08:00 CDMX; histórico)

No se ejecutó QA nuevo en la corrida del investigador de las 08:00 ni se alteró entonces ningún `narrative_qa`. La tabla siguiente conserva fielmente el estado observado en ese corte: los dos storyboards del 20-nov estaban `PENDIENTE_AUDITOR`. La auditoría independiente posterior los evaluó PASS; los resultados vigentes se indican en los candidatos A/B y en `docs/briefs/2026-11-20_CONTROL_COLA.md`.

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

Los QA PASS anteriores no se repitieron ni se transfirieron a otras versiones. Al corte de las 08:00, los dos proyectos actuales permanecían en `proyectos/`; ninguno fue promovido a `cola/entrada/`. La auditoría posterior no promovió ninguno.

## 7. Rotación, continuidad y límites de ejecución

- `data/temas_del_dia.json` llega a 2026-10-28; `data/rotacion.json` a 2026-10-31; `data/estilos_usados.json` a 2026-10-28. Son históricos incompletos y permanecen intactos.
- Se leyó `scripts/registro_editorial.py` (recorre `storyboard.json` recursivamente en proyectos, cola y salidas; inventaría handoffs por separado) y `scripts/rotacion.py`. No se afirma haber ejecutado el script: la comprobación se hizo mediante lectura del código y de los árboles/archivos actuales de GitHub.
- Los estilos ya presentes hoy son `neon_noir` para 17:00 y `linograbado` para 23:30. No se selecciona ni repite estilo nuevo porque no se crea storyboard.
- No se modificaron storyboards existentes, `data/*.json`, main, workflows, motores canónicos ni Motor U6.
- No se crearon frames, imágenes, audio, voz, video ni renders; no se publicó ni programó contenido; no se consumieron créditos.
- Al corte de las 08:00 no se creó `narrative_qa`, no se hizo promoción, no se creó ni editó `cola/estado/`, y no se declaró recepción de Grok. La auditoría posterior registró QA independiente en los storyboards, pero no creó estados Grok.

**Entregables de esta ejecución:** únicamente este radar. No se creó storyboard principal ni storyboard 23:30 porque los slots están ocupados.

## Corrección de auditoría posterior — 2026-11-20, 12:26 CDMX

Esta nota no cambia el storyboard ni repite su QA narrativo; corrige la interpretación de fuente y amplía la guardia de producción:

- **Marea cerebral:** el abstract presenta el grupo mayor como 60–84 años, pero Methods §“Participant population and exclusion criteria”, después de excluir participantes por movimiento, deja 41 adultos mayores de 60–83 años en el análisis nocturno. La narración del storyboard (60–83) describe la muestra analítica final y es correcta; no hay discrepancia factual. El DOI aparece en la página/PDF editorial, pero Crossref/doi.org no completaron; `doi_verification_status` sigue `PENDIENTE_RESOLVEDOR`.
- **Sapropeles:** Nature Geoscience muestra en su ficha editorial título, DOI y publicación/versión de registro del 20-nov-2026; la apertura HTML directa redirige a autenticación y Crossref/doi.org no completaron. Se conserva `PENDIENTE_RESOLVEDOR`; no se declara DOI verificado por Crossref.
- **Guardia adicional en main:** `2026-11-20_react-proteinas-microbios` tiene `programacion.json` con 13:45 CDMX (`publish_at=2026-11-20T19:45:00Z`) y storyboard en `proyectos/` y `cola/entrada/`. Se clasifica `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`. El JSON declara `export.filename=capsula.mp4`, pero el MP4 no se encontró en `cola/entrada/<id>/`, `proyectos/<id>/` ni `salidas/<id>/`: `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`. No hay estado Grok individual ni publicación confirmada. No colisiona exactamente con los storyboards de feature de 17:00 y 23:30, pero se cuenta para la capacidad diaria.
- **Recepción de los dos borradores feature:** `cola/estado/<project_id>.json`, `handoffs/grok_inbox/<project_id>.json` y las rutas de cola/salidas comprobadas devuelven 404. Ambos siguen `RECEPCION_GROK_NO_CONFIRMADA` y `NOT_DISPATCHABLE`; no se promueven.
- **Horarios:** `feature/data/horarios.json` habilita 06:30–07:30 y 16:30–18:00 más 23:30 fijo; `main/data/horarios.json` habilita 06:30–07:30 y 13:00–14:30 más 23:30. `scripts/rotacion.py` conserva cinco ventanas de código (07:00, 13:30, 17:00, 19:00, 23:30). La divergencia permanece documentada; no se modificó ningún `data/*.json` ni el código de rotación.


## Revalidación y siguiente slot — 20-nov-2026, 14:00 CDMX

- **Slot seleccionado:** 21-nov, 17:00 CDMX, cesta `intermedio_1`. La ventana de trabajo de la rama es 16:30–18:00 y el sábado es día preferente. La revisión de proyectos, cola, salidas y programación no encontró ocupación exacta a las 17:00. En `main/data/publicaciones.json` aparecen 13:30 y 19:00; no son el mismo slot. No se usa 23:30 ni se adelanta un dato del día.
- **Cupo:** el registro de `main/data/publicaciones.json` muestra dos piezas propias para el 21-nov. Este borrador se marca explícitamente `origen=externa`; el total observado queda por debajo del máximo diario de cinco y no aumenta el cupo propio.
- **Tema elegido:** descubrimiento de PSR J1622−7204 mediante una búsqueda basada en retículas. No aparece otro proyecto de púlsares en el inventario actual. Publicación del artículo: 19-nov-2026; línea provisional: `Actualidad`.
- **Fuente primaria:** Pook-Kolb et al., *Physical Review Letters* 137, 211201 (2026), DOI `10.1103/vlt2-xzgk`. La página editorial APS muestra el DOI y su enlace DOI redirige a la página editorial. La API REST de Crossref no estuvo accesible; queda pendiente el chequeo oficial `--check-doi`, no se declara ejecutado.
- **Coordenadas del mapa:** Table I, p. 3: RA nominal 16h22m12.72s (245.553°), DEC −72°03′57.6″ (−72.066°). La capa usa proyección celeste ICRS; RA se envuelve a −114.447° solo para el rango de la proyección, no como longitud terrestre.
- **Rotación:** estilo `pixel_art` no usado en los proyectos recientes; estructura `historia` (no repite la última `pregunta`); cama `sintetico:arpegio` (no coincide con las dos últimas camas registradas). No se modificó ningún `data/*.json`.
- **Borrador creado:** `proyectos/2026-11-21_pulsar-gamma-reticulo/storyboard.json`, commit `404b9c0ad24d41604b20f9ab62176dfc93d1c1ec`. Lectura de vuelta: 8 escenas, 209 palabras, 78 s de escenas + 6 s de cortinilla = 84 s; gancho de 4 palabras; voz es-MX-JorgeNeural +7% / −2Hz; fuente en todas las escenas; mapa y dato; ambiente y SFX por escena.
- **Estado deliberado:** solo preproducción textual. No contiene `narrative_qa`; queda para auditoría independiente. `approved_assets=[]`, `export.render_status=NOT_GENERATED`, publicación `PENDIENTE_DECISION_GROK`. No se creó entrada de cola, estado Grok ni medio.

## Addendum de ejecución — 20 de noviembre de 2026, 16:00 CDMX

- El slot fijo del dato del día **21-nov, 23:30 CDMX** estaba libre: el inventario de esta rama solo mostraba el proyecto de púlsar a las 17:00; en `main`, las publicaciones del 21-nov visibles son 13:30 y 19:00, sin programación a 23:30 (`publishAt=2026-11-22T05:30:00Z` no aparece).
- Se creó y releyó `proyectos/2026-11-21_fentale-metano-sin-erupcion/storyboard.json` para 23:30. Commit: `096612f3809fb16b47b66489fae497f669c9c688`. Usa el estilo de catálogo `pulp_comic_1940s`, no repetido en los storyboards revisados del 5 al 21 de noviembre.
- Preflight estático: 8 escenas, 170 palabras, 78 s de escenas + 6 s de cortinilla = 84 s; gancho de 3 palabras; voz es-MX-JorgeNeural +7% / -2Hz; mapa con coordenadas GVP 8.985°N, 39.906°E y capa de datos. No se ejecutó el validador oficial.
- La página editorial primaria de Nature Geoscience está indexada y muestra el artículo y el DOI `10.1038/s41561-026-02137-4`; el acceso HTML directo y las consultas Crossref/doi.org no completaron. `doi_verification_status=PENDIENTE_RESOLVEDOR`. El borrador no es promocionable hasta completar esa verificación y el validador oficial.
- El storyboard permanece solo en `proyectos/`: después de crearlo, la auditoría independiente registró `narrative_qa=PASS 90/100` con siete checks true y flags vacías. No se creó estado Grok, entrada de cola ni medios; `approved_assets=[]`, `render_status=NOT_GENERATED`, publicación pendiente.
- El proyecto de púlsar de 21-nov a las 17:00 sigue ocupando ese slot y tiene QA narrativo `FAIL 83`; no se reescribió su narración durante esta ejecución.


## Addendum de actualización — 20-nov-2026, 18:05 CDMX

### Respaldo oficial de Google Trends México

La página HTML oficial de Trending Now volvió a cargar: **185 tendencias activas** en la ventana mostrada. `volcán` aparece con **2 mil+ búsquedas** y actividad de unas 7 horas. Es una señal temática general; no demuestra interés específico por Fentale ni valida por sí sola el candidato. [Google Trends México](https://trends.google.com/trending?geo=MX&hl=es).

Los errores de RSS documentados arriba siguen siendo la referencia de ejecución previa. En este run no se ejecutó `scripts/tendencias.py`; el lector web tampoco interpreta directamente los cuerpos XML de los feeds. No se atribuye ese límite del lector a una caída nueva de cada proveedor.

### Verificación de los candidatos que ya tienen storyboard

- **Fentale:** la página editorial de Nature identifica el artículo primario y su fecha de publicación como 19-nov-2026. DOI `10.1038/s41561-026-02137-4`. La página no muestra hora de publicación; para el slot `2026-11-21 23:30` no se puede certificar la ventana editorial de 48 h. Crossref `--check-doi` sigue pendiente. No promover todavía.
- **Púlsar gamma:** la página editorial de Physical Review Letters identifica el artículo y DOI `10.1103/vlt2-xzgk`, publicado el 19-nov-2026. El storyboard conserva QA narrativo FAIL 83; no promover.
- **Sapropeles** y **flujo de LCR durante el sueño** siguen como candidatos documentados A–D. No se creó un quinto storyboard ni se duplicó tema/slot en esta actualización.

No se modificaron `data/*.json`, la rotación ni los storyboards en este addendum.


---

## Actualización de investigación — run 11, 20-nov-2026 20:08 CDMX

### Feeds RSS y respaldo de tendencias

Se intentaron las fuentes declaradas en `scripts/tendencias.py`. El lector no pudo entregar los XML; los errores observados fueron:

- ScienceDaily `science.xml`, `health.xml` y `space_time.xml`: `(400) Unsupported content-type: application/xml`.
- Phys.org `rss-feed/`: `(400) Unsupported content-type: text/xml`.
- NASA `news-release/feed/`: `(400) Unsupported content-type: application/rss+xml`.
- Nature `nature.rss` y UNAM Global `feed/`: `(400) Unsupported content-type: application/rss+xml`.
- ESA Space Science RSS: `(404) Not Found`.
- EurekAlert y Agencias SINC: `URL ... is not accessible via this tool`.
- Google Trends RSS México: `URL ... is not accessible via this tool`.

Estos son errores del acceso/lector disponible; no demuestran por sí solos que todos los servidores RSS estén caídos. Se usó como respaldo la página oficial [Google Trends México](https://trends.google.com/trending?geo=MX&hl=es): 178 tendencias visibles; “volcán” aparecía con más de 5 mil búsquedas y actividad iniciada unas 9 horas antes. Es una señal general, no evidencia de demanda específica para una cápsula sobre Homo erectus.

### Candidatos recientes, 18–20 de noviembre

1. **Rainforest adaptation in late Homo erectus from southern China** — *Nature*, 18-nov-2026. Artículo primario: [Nature](https://www.nature.com/articles/s41586-026-11155-6), DOI `10.1038/s41586-026-11155-6`; [registro PubMed](https://pubmed.ncbi.nlm.nih.gov/43052437/). El editor y PubMed muestran el mismo DOI y fecha. Las consultas directas a doi.org y Crossref REST no fueron accesibles en esta sesión, por lo que el DOI queda pendiente de resolución independiente; la URL editorial primaria sí fue verificada. Hallazgo: nueve dientes de homininos en dos cuevas de Guangxi, ocho identificados como H. erectus; 43 edades radiométricas mediante cinco técnicas; intervalos modelados 324–184 ka; fauna e isótopos compatibles con selva tropical de dosel cerrado. Candidato de naturaleza/paleontología sin ángulo social. Se creó borrador para el slot libre 21-nov 07:00: `proyectos/2026-11-21_homo-erectus-selva-tropical/storyboard.json`. Sigue sin narrative_qa y no es promocionable.

2. **Welopōʻai, a peculiar triple system 8 pc from the Sun** — *Astronomy & Astrophysics*, 19-nov-2026, DOI `10.1051/0004-6361/202661214`. La investigación describe una enana roja y dos enanas blancas a unos 27.6 años luz. La página primaria A&A y el resolvedor DOI no se pudieron recuperar en esta sesión; hay comunicado institucional de la Université de Montréal y resumen de Phys.org proporcionado por la universidad. Estado: `PENDING_SOURCE`; no se creó storyboard.

3. **Fundamental-mode lasing at 30 keV in an X-ray free-electron laser** — *Optica* 13(11), pp. 2271–2274, número fechado 20-nov-2026, DOI declarado `10.1364/optica.610411`. La página oficial del número confirma título, autores y fecha; la página HTML del artículo devolvió “Your token has expired or is invalid”. No se obtuvo resolución DOI/Crossref ni lectura primaria completa para los claims cuantitativos. Estado: `PENDING_SOURCE`; no se creó storyboard.

4. **Fentale / metano sin erupción** — *Nature Geoscience*, 19-nov-2026, ya tiene borrador para 21-nov 23:30. `NO_DUPLICAR`; conserva QA independiente PASS 90. DOI/resolvedor sigue pendiente. Su campo de estructura `paradoja_mecanica` no pertenece a las cinco estructuras que admite `scripts/rotacion.py`; no se cambió porque requeriría una decisión editorial.

5. **Púlsar gamma / retícula** — *Physical Review Letters*, 19-nov-2026, ya tiene borrador para 21-nov 17:00. `NO_DUPLICAR`; conserva FAIL 83 por giro científico insuficientemente explicado. No se reescribió la narración.

Se descartaron como “recientes” Longipteryx y el estudio de mortalidad de murciélagos en turbinas: los artículos originales que respaldan esas notas están fechados el 27-oct-2026, fuera de la ventana de siete días.

### Slot del 21 de noviembre

El slot 07:00 cae dentro de la ventana matutina 06:30–07:30 y el sábado es día preferente. La revisión cruzada encontró ocupados 13:30 (oxoboranos, main), 17:00 (púlsar, proyecto feature), 19:00 (robot orbital, main) y 23:30 (Fentale, proyecto feature). 07:00 estaba libre. Con el nuevo borrador se alcanza el máximo de cinco piezas/reservas del día: dos propias y tres externas. No se deben añadir más proyectos para esa fecha.

La rotación del nuevo borrador usa `papel_rasgado_capas`, estructura `sabias_que` y cama `circuito_neural`, sin repetir las combinaciones de los otros cuatro elementos del día.

### Corrección de verificación — 20-nov-2026 20:22 CDMX

El DOI `10.1038/s41586-026-11155-6` **sí resolvió**: al seguir el enlace DOI desde el registro PubMed, el resolvedor redirigió al artículo Nature correcto. El contenido final de Nature no pudo abrirse por redirección a autorización, pero el registro PubMed muestra DOI, fecha 18-nov-2026 y abstract; el resultado indexado del artículo Nature expone los detalles de métodos y resultados. Crossref REST siguió sin estar accesible. Se actualizó el storyboard: `doi_verification_status=VERIFICADO_RESOLVEDOR`. Esto cierra la compuerta DOI, pero no la revisión narrativa independiente ni el validador estructural oficial; la pieza sigue en proyectos y no se promueve.

### Corrección de rotación visual — 20-nov-2026 20:24 CDMX

Se detectó que `papel_rasgado_capas` había sido usado el 14 y el 18 de noviembre, por lo que no era una elección suficientemente rotada para el 21. Se sustituyó en el storyboard por `dibujo_cientifico_scratchboard`, estilo del catálogo apropiado para paleontología; su último uso visible fue el 13-nov, fuera de la ventana 14–20 nov. Se actualizaron `estilo_id`, `visual_identity` y los ocho `image_prompt` con el `prompt_base` literal del catálogo. Narración, claims, fuentes, estructura `sabias_que` y cama `circuito_neural` no cambiaron.


### Actualización de investigación y siguiente slot — run 12, 2026-11-20 22:06 CDMX

#### Ingesta de tendencias

Se intentó leer cada feed definido en `scripts/tendencias.py`. La lectura XML no produjo cuerpos utilizables en este entorno. Errores visibles exactos: ScienceDaily Top Science devolvió `(400) Unsupported content-type: application/xml`; Google Trends RSS México devolvió `URL https://trends.google.com/trending/rss?geo=MX is not accessible via this tool`. Para los demás feeds el lector no expuso un cuerpo ni un error individual legible; no se inventa un código HTTP.

Respaldo oficial: la página HTML de Google Trends México mostró 173 tendencias activas; `volcán` aparecía con más de 5 mil búsquedas en 11 horas y `ola de frío` con más de 10 mil en 8 horas. Ninguna de esas tendencias constituye evidencia científica ni cambia la selección editorial.

#### Cinco candidatos revisados

1. **Voyager 1 a un día-luz** — NASA/JPL, 19-nov-2026. Hito del 18-nov: aproximadamente 25.9 mil millones de km; señal de ida ≈24 h y comunicación de ida y vuelta ≈48 h. La portadora seguía llegando; los datos científicos y de ingeniería no se recibían desde el 14-nov. Fuente primaria: https://www.jpl.nasa.gov/news/nasas-voyager-1-makes-history-reaching-one-light-day-from-earth/. **Seleccionado** para 22-nov 07:00.
2. **CGMap: priorización de genes** — *Nature Machine Intelligence*, 16-nov-2026, DOI 10.1038/s42256-026-01327-4. El artículo reporta 12,022 genes analizados y 70 candidatos; FN1 y TTN se examinaron en líneas celulares. No equivale a 70 tratamientos ni a validación clínica. Reserva, no duplicar con la pieza seleccionada.
3. **Metano de Fentale sin erupción** — *Nature Geoscience*, 19-nov-2026. Ya reservado para 21-nov 23:30; conserva PASS narrativo 90, pero su estructura `paradoja_mecanica` no pertenece al catálogo de rotación y el DOI sigue pendiente. No duplicar.
4. **Homo erectus en selva tropical** — *Nature*, 18-nov-2026. Ya reservado para 21-nov 07:00; QA narrativo FAIL 83. No reescribir durante auditoría.
5. **Púlsar gamma y retícula** — *Physical Review Letters*, 19-nov-2026. Ya reservado para 21-nov 17:00; QA narrativo FAIL 83. No reescribir durante auditoría.

Descartes de búsqueda: el artículo “Bridging Roche Lobe Overflow…” está fechado el 3-jun-2026, no es reciente; el candidato de nanopartículas/Claudin-4 no se pudo verificar en la página primaria de ACS, por lo que permanece `PENDING_SOURCE`.

#### Slot siguiente y borrador creado

El 21-nov ya tiene cinco reservas: 07:00 Homo, 13:30 oxoboranos en main, 17:00 púlsar, 19:00 robot orbital preexistente en main y 23:30 Fentale. No añadir más para esa fecha.

El 22-nov 07:00 está libre en `main/data/publicaciones.json` y en `feature/proyectos/`; la ventana matutina sigue activa. Es domingo, día no preferente, pero no está excluido por la política. Se dejó libre 23:30: el artículo de Voyager no sería noticia del mismo día ni cumpliría la ventana de 48 horas para `dato del día`.

Creado y releído `proyectos/2026-11-22_voyager-1-un-dia-luz/storyboard.json`, commit `1450f262225e16d08ee4a98148441d0a0a4ca0a4`. Tiene 8 escenas, 180 palabras, 78 s de escenas + 6 s de cortinilla = 84 s; estilo `risografia`, estructura `mito_vs_dato` y cama `pizzicato`. El mapa sitúa los tres complejos DSN con coordenadas publicadas de Goldstone (35.4266667, -116.89), Madrid (40.42917, -4.24972) y Canberra (-35.40139, 148.98167); la red y su separación se apoyan en NASA/JPL y las páginas cartográficas se usan solo como localizadores. Observación, cálculo, inferencia y recomendación quedaron separados en `analisis`.

La pieza permanece en `proyectos/`: sin `narrative_qa` (corresponde a auditoría posterior), sin `ESTADO_EJECUCION`, sin medios, sin assets, sin cola y sin programación. No se ejecutó el validador estructural oficial ni se promovió.


### Actualización de investigación y siguiente slot — run 13, 2026-11-20 22:44 CDMX

#### Ingesta de feeds

- Se reintentaron los feeds definidos en `scripts/tendencias.py`. En este entorno no se obtuvo XML utilizable para ScienceDaily, Phys.org, NASA, ESA, Nature, EurekAlert, SINC ni UNAM Global; no se inventan códigos HTTP cuando el lector no los expone.
- Errores exactos ya registrados para esta ruta de ingesta: ScienceDaily Top Science devolvió `(400) Unsupported content-type: application/xml`; Google Trends RSS México devolvió `URL https://trends.google.com/trending/rss?geo=MX is not accessible via this tool`.
- Respaldo oficial: la página HTML de Google Trends México abrió; las tendencias visibles no aportaron una señal científica nueva que justificara sustituir la selección por popularidad.

#### Candidatos recientes revisados

1. **ADN de yubarta desde el soplo** — *Molecular Ecology Resources*, 17-nov-2026, DOI [10.1111/1755-0998.70219](https://doi.org/10.1111/1755-0998.70219). Fuente primaria: 58 muestras de soplo de 26 yubartas; 84% de lecturas endógenas en promedio; cobertura media 2.3× nuclear y 94× mitocondrial; contraste con muestras repetidas y biopsias pareadas de dos individuos. DOI resuelto a la página editorial Wiley. **Seleccionado** para 22-nov 17:00.
2. **Comunicación gravitatoria a través de una pared** — *Science Advances*, publicación 20-nov-2026, DOI 10.1126/sciadv.aee0802. PubMed confirma el artículo y su resumen: mensaje de unos 0.7 m a través de pared de ladrillo, a 1 bit/min. La resolución directa del DOI no quedó disponible en esta sesión; estado `PENDING_DOI_RESOLUTION`, no se creó storyboard.
3. **Toxina que remodela la piel del pez pulmonado africano** — *Cell*, 17-nov-2026, DOI 10.1016/j.cell.2026.10.038. PubMed confirma el artículo y el mecanismo de Protop-CrTX-A; la resolución directa del DOI no quedó disponible en esta sesión. Estado `PENDING_DOI_RESOLUTION`, no se creó storyboard.
4. **Lluvias y floración en Atacama asociadas a El Niño** — NASA Earth Observatory, 19-nov-2026. Fuente oficial, pero el tema El Niño ya tiene antecedente editorial en el canal; `NO_DUPLICAR` hasta una decisión editorial que justifique un ángulo distinto.
5. **Nube de sodio de Europa** — nota del 20-nov; el estudio primario localizado está fechado el 10-oct-2026, fuera de la ventana de siete días para una novedad primaria. No seleccionado.

#### Selección y rotación

- Se creó `proyectos/2026-11-22_yubarta-genoma-soplo/storyboard.json` para el 22-nov 17:00 CDMX, dentro de la ventana activa 16:30–18:00. La consulta de `main/data/publicaciones.json` no encontró publicación ni programación para 22-nov 17:00; en feature solo estaba el borrador Voyager a las 07:00. El slot vespertino no presenta conflicto exacto.
- Rotación: `tatuaje_acuarela` (catálogo, sublínea naturaleza/océano/biología), estructura `pregunta`, cama `arpegio`. El estilo no aparece entre los últimos 15 registros de rotación de main; la cama no está entre las dos últimas.
- El mapa usa únicamente la caja regional publicada por Hakai para el territorio Gitga'at, no puntos de muestreo ni trayectorias inventadas. Fuentes: DOI primario del artículo y DOI del catálogo Hakai `10.21966/2aap-hn61`.
- Borrador: 8 escenas, 180 palabras, 78 s de escenas + 6 s de cortinilla = 84 s. Voz `es-MX-JorgeNeural` +7%, pitch -2Hz. Sin `narrative_qa`, sin `ESTADO_EJECUCION.md`, sin medios, sin assets, sin cola y sin programación.

