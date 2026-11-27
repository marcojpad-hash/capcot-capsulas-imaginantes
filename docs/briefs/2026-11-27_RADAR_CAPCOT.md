# RADAR CAPCOT — 2026-11-27

**Corte:** 27 de noviembre de 2026, 00:02 CDMX.  
**Última actualización:** 27 de noviembre de 2026, 09:59 CDMX. Shortlist vigente de cinco candidatos del corte: EpTFIIAγ, malaria m⁶A/YTH.2, actividad fuera del blanco de CAY10641/CAY10650, ensamblaje de CAST tipo I-F y circuito intestino-cerebro de Drosophila. El borrador de EpTFIIAγ permanece en `proyectos/` para 30-11 17:00; no está seleccionado, preparado ni promovido. DOI/Crossref y validador estructural real pendientes.

## Método y fuentes

Se consultaron los feeds definidos en `scripts/tendencias.py` y Google Trends RSS México. Los feeds no entregaron cuerpos XML utilizables en esta ejecución:

| Feed | Resultado observado |
|---|---|
| ScienceDaily Science, Health y Space | HTTP 400 — Unsupported content-type |
| Phys.org | HTTP 400 — Unsupported content-type |
| NASA | HTTP 400 — Unsupported content-type |
| Nature RSS | HTTP 400 — Unsupported content-type |
| UNAM Global | HTTP 400 — Unsupported content-type |
| ESA Space Science | HTTP 404 |
| EurekAlert | URL not accessible |
| Agencia SINC | URL not accessible |
| Google Trends RSS México | URL not accessible |

**Respaldo oficial de tendencias:** la página HTML de Google Trends México mostró 252 tendencias en la ventana consultada. Las primeras 25 estaban dominadas por deportes, actualidad, clima y personalidades; no apareció una señal científica/natural clara para seleccionar un tema.

**DOI y resolvedor:** se consultaron páginas editoriales y se intentó acceso directo a Crossref y `doi.org`. El acceso al resolvedor no quedó disponible en esta ejecución. Los DOI que aparecen en páginas editoriales se conservan como referencias, pero **ninguno se marca VERIFICADO_CROSSREF**. `--check-doi` no se ejecutó.

## Candidatos

### 1. Drenaje histórico de turberas y forzamiento climático

- **Fuente primaria:** Nature, 25-11-2026. DOI: [10.1038/s41586-026-11339-0](https://doi.org/10.1038/s41586-026-11339-0). [Artículo editorial](https://www.nature.com/articles/s41586-026-11339-0).
- **Observación:** reconstrucción global de drenaje de turberas para 1800–2020. El estudio estima un forzamiento radiativo de 73 mW m⁻² (intervalo informado: 48–99 mW m⁻²), asociado a una superficie drenada de aproximadamente 0.4–0.5% de la superficie terrestre.
- **Cálculo CAPCOT:** ninguno. Las cifras anteriores son resultados reportados por el artículo, no cálculos independientes.
- **Inferencia:** una fracción pequeña de superficie puede tener un efecto climático desproporcionado por las emisiones asociadas al drenaje. No equivale a una predicción meteorológica local ni a una medición directa de cada turbera.
- **Recomendación:** prioridad alta. Tiene un arco visual claro —poca superficie, efecto grande— y permite cartografía global si se valida el dataset suplementario.
- **Estado de fuente:** `PENDING_CROSSREF`.

### 2. Producción de cemento mediante una ruta de plasma de carbono y microondas

- **Fuente primaria:** Nature, 25-11-2026. DOI: [10.1038/s41586-026-11313-w](https://doi.org/10.1038/s41586-026-11313-w). [Artículo editorial](https://www.nature.com/articles/s41586-026-11313-w).
- **Observación:** el trabajo presenta una ruta de calentamiento por plasma de carbono asistido por microondas, con temperaturas reportadas de hasta 2,400 °C, para transformar pasta de cemento hidratada de desecho en clínker que cumple especificaciones de cemento Portland ordinario. El artículo describe un reactor de lotes de hasta 100 kg.
- **Cálculo CAPCOT:** ninguno.
- **Inferencia:** la ruta puede acortar el tiempo de proceso y valorizar pasta hidratada residual; el resultado experimental no demuestra por sí solo adopción comercial ni balance neto de emisiones a escala industrial.
- **Recomendación:** prioridad alta, condicionada a explicar la diferencia entre reactor experimental y planta comercial. El sitio experimental exacto debe verificarse antes de fijar un mapa.
- **Estado de fuente:** `PENDING_CROSSREF`.

### 3. Complejidad vertical de copas forestales y enfriamiento local

- **Fuente primaria:** Nature Communications, 25-11-2026. DOI: [10.1038/s41467-026-79796-9](https://doi.org/10.1038/s41467-026-79796-9). [Artículo editorial](https://www.nature.com/articles/s41467-026-79796-9).
- **Observación:** el estudio relaciona la complejidad vertical de la estructura de las copas con el enfriamiento local. Reporta enfriamiento local en la gran mayoría de los bosques y estima una reducción potencial cercana a 0.25 °C en temperatura superficial terrestre de bosques gestionados si su complejidad se aproxima a la de bosques intactos de referencia.
- **Cálculo CAPCOT:** ninguno.
- **Inferencia:** conservar/restaurar estructura vertical puede ser una palanca de adaptación local. La cifra corresponde a temperatura superficial terrestre modelada, no a una reducción equivalente de temperatura media del aire.
- **Recomendación:** prioridad alta. El mapa debe distinguir bosques gestionados, referencias intactas y escala local.
- **Estado de fuente:** `PENDING_CROSSREF`.

### 4. Reutilización de materia orgánica de algas para gestionar floraciones

- **Fuente primaria:** Nature Communications, 25-11-2026. DOI: [10.1038/s41467-026-79713-0](https://doi.org/10.1038/s41467-026-79713-0). [Artículo editorial](https://www.nature.com/articles/s41467-026-79713-0).
- **Observación:** el trabajo estudia el uso de materia orgánica algal recuperada como coagulante. Reporta eficiencias de eliminación de células algales de 82–95%, reducción de turbidez de 86–95% y recuperación de 45–79% de materia orgánica algal en un proceso de aproximadamente dos minutos. El análisis reporta reducciones de huella de carbono frente al tratamiento convencional.
- **Cálculo CAPCOT:** ninguno; no se recalcularon los porcentajes.
- **Inferencia:** parte del material retirado puede reutilizarse como insumo del propio tratamiento. No debe presentarse como solución ya desplegada a escala de lago o cuenca.
- **Recomendación:** prioridad media-alta por su giro circular. Antes de storyboard deben confirmarse escala experimental, origen de muestras y lugar de ensayo para no inventar un mapa.
- **Estado de fuente:** `PENDING_CROSSREF`.

### 5. Beneficios climáticos de productos de madera según uso y escenario

- **Fuente primaria disponible:** preprint de Research Square, DOI [10.21203/rs.3.rs-8591788/v1](https://doi.org/10.21203/rs.3.rs-8591788/v1). **Registro de artículo final:** Environmental Science & Technology, DOI [10.1021/acs.est.6c10525](https://doi.org/10.1021/acs.est.6c10525).
- **Observación:** el análisis compara 81 variantes de productos de madera, seis categorías de uso y tres escenarios de descarbonización para 2020–2070. Los factores de desplazamiento varían ampliamente entre usos; el beneficio no es uniforme y el desplazamiento asociado a energía disminuye hacia 2070.
- **Cálculo CAPCOT:** ninguno. No se extrapolan los factores a una cifra universal de “madera carbono-negativa”.
- **Inferencia:** el beneficio depende del producto sustituido, su vida útil y la descarbonización del sistema energético/material.
- **Recomendación:** prioridad media. Requiere lectura de la versión final del artículo y verificación de los límites del análisis antes de convertirlo en guion.
- **Estado de fuente:** `PENDING_PRIMARY_ACCESS` para la versión final editorial y `PENDING_CROSSREF`.

## Vigilancia, no selección

Frontiers in Materials aceptó el 26-11-2026 un artículo sobre compensación de velocidad de impresión en pinzas bilaminares impresas en 4D, DOI [10.3389/fmats.2026.2016303](https://doi.org/10.3389/fmats.2026.2016303). La página editorial indica que la versión final formateada aparecerá después. Se conserva como vigilancia, no como candidato listo para storyboard.

## Decisión editorial del corte

1. No se creó storyboard nuevo para el 28-11-2026 23:30: el slot no muestra ocupación en los registros consultados, pero no hay DOI/Crossref verificado para ninguno de los candidatos.
2. El storyboard de rapaces del 30-11-2026 07:00 sigue en `proyectos/`; no está preparado ni promovido.
3. No se generaron medios, frames, voz, audio, video, renders ni placeholders.
4. Ningún candidato se marca como recibido por Grok, seleccionado, producido, aprobado o publicado.


## Revalidación de fuentes y tendencias — 27-11-2026 02:04 CDMX

**Alcance de esta reconsulta:** se intentó abrir directamente cada URL RSS definida en `scripts/tendencias.py`; no se ejecutó el script Python en un runtime del repositorio. Los resultados exactos fueron:

| Fuente | Error de acceso |
|---|---|
| ScienceDaily Science | `400 Unsupported content-type: application/xml` |
| ScienceDaily Health | `400 Unsupported content-type: application/xml` |
| ScienceDaily Space | `400 Unsupported content-type: application/xml` |
| Phys.org | `400 Unsupported content-type: text/xml` |
| NASA | `400 Unsupported content-type: application/rss+xml` |
| ESA Space Science | `404 Not Found` |
| Nature RSS | `400 Unsupported content-type: application/rss+xml` |
| EurekAlert | `URL ... is not accessible via this tool` |
| Agencia SINC | `URL ... is not accessible via this tool` |
| UNAM Global | `400 Unsupported content-type: application/rss+xml` |
| Google Trends RSS México | `URL ... is not accessible via this tool` |

El respaldo HTML oficial de [Google Trends México](https://trends.google.com/trending?geo=MX) mostró **253 tendencias**. Las primeras 25 siguieron dominadas por deportes, clima, actualidad, figuras públicas y entretenimiento; no se identificó una señal científica/natural admisible.

### Vigilancia adicional — PAV1 y el patógeno de la agalla de la corona

- **Fuente primaria:** Sabri et al., *Frontiers in Plant Science*, Original Research, publicado el 26-11-2026. DOI declarado por la página editorial: [10.3389/fpls.2026.2008228](https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2026.2008228/full).
- **Observación:** el artículo describe PAV1 como el primer bacteriófago identificado que infecta *Allorhizobium vitis*. Reporta inhibición del crecimiento bacteriano superior al 98% en 48 h in vitro. En plantas de tomate, a los 25 días, la incidencia fue 83.3% en controles sin tratar y 46.7%/50.0% tras aplicaciones preventivas por inyección del tallo/aspersión foliar.
- **Observación de procedencia:** el fago se aisló de una muestra de aguas residuales tomada en noviembre de 2025 en la entrada de la planta municipal de tratamiento de Bari, Italia (41.1081° N, 16.2606° E). Esa coordenada corresponde al punto de aislamiento, no al lugar de los ensayos en tomate.
- **Límite:** el ensayo de biocontrol descrito es en tomate; no demuestra eficacia de campo en viñedos ni control de agalla en plantas de vid. No convertir los porcentajes en una promesa de tratamiento comercial.
- **Cálculo CAPCOT:** ninguno.
- **Inferencia:** candidato con giro visual fuerte —un virus bacteriano aislado de aguas residuales que reduce una enfermedad vegetal en condiciones experimentales—, pero requiere explicar la diferencia entre actividad in vitro y ensayo preventivo en tomate.
- **Recomendación:** conservar como vigilancia, no añadirlo a los cinco candidatos principales ni crear storyboard todavía. No se identificó una ubicación publicada para los ensayos en tomate; el único pin verificable es el sitio de aislamiento en Bari.
- **Estado DOI:** `PENDING_CROSSREF`. La apertura directa de Crossref y `doi.org` devolvió `Internal Error ()` y “URL ... is not accessible via this tool”; la página editorial primaria sí está accesible. No marcar el DOI como verificado.

Los cinco candidatos principales del corte permanecen sin cambios y con Crossref pendiente. No se creó storyboard para el 28-11-2026 23:30 ni para otro slot.


## Corte adicional — 27-11-2026 03:55 CDMX

**RSS y respaldo:** se reintentó abrir directamente las URL RSS de `scripts/tendencias.py`; se mantuvieron los errores de tipo de contenido XML/RSS, ESA 404 y las URL no accesibles de EurekAlert/SINC/Google Trends RSS. No se ejecutó el script Python porque el entorno no pudo recuperar GitHub por DNS; por tanto, estos son resultados de apertura directa, no una ejecución de `tendencias.py`. La vista HTML oficial de [Google Trends México](https://trends.google.com/trending?geo=MX) mostró **257 tendencias**; las primeras 25 no aportaron señal científica/natural admisible.

### Cinco candidatos activos del corte

1. **PAV1: bacteriófago contra `Allorhizobium vitis` — seleccionado para borrador 27-11 07:00.**
   - Fuente primaria: Sabri et al., *Frontiers in Plant Science*, Original Research, publicado 26-11-2026. DOI 10.3389/fpls.2026.2008228. [Artículo primario](https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2026.2008228/full).
   - Observación: primer bacteriófago descrito para `A. vitis`; inhibición de crecimiento superior al 98% en 48 h in vitro contra la cepa probada; a 25 días, incidencia en tomate de 83.3% en controles, 46.7% con inyección preventiva y 50.0% con aspersión preventiva.
   - Mapa: el artículo publica 41.1081° N, 16.2606° E para la entrada de la planta municipal de tratamiento de aguas residuales de Bari, donde se aisló PAV1 en noviembre de 2025. Esa coordenada **no** es el lugar del ensayo en tomate.
   - Límite: ensayo preventivo en tomate; no demuestra eficacia en viñedos, curación de plantas ya enfermas ni control de campo. El artículo no publica coordenadas del ensayo en tomate.
   - Verificación: página primaria accesible y DOI visible en el encabezado; el acceso directo a `doi.org` no estuvo disponible desde esta herramienta. Estado de DOI: `VERIFICADO_URL`; Crossref/`--check-doi` pendiente.
   - Decisión: se creó únicamente `proyectos/2026-11-27_dato-pav1-bacteriofago/storyboard.json` para el slot libre 07:00. No se creó narrative_qa, ESTADO_EJECUCION ni entrada de cola.

2. **Riesgo genético en fauna mesopelágica del Golfo de México.**
   - Fuente primaria: *Nature Communications*, DOI 10.1038/s41467-026-79098-0. [Artículo editorial](https://www.nature.com/articles/s41467-026-79098-0). Cobertura de ScienceDaily, 26-11-2026: [nota](https://www.sciencedaily.com/releases/2026/11/261125045249.htm).
   - Observación: 486 ejemplares, cinco especies, datos de 2011–2023; pérdida neta cercana al 8% en tres métricas para `Diaphus dumerilii`; los modelos proyectan menor hábitat adecuado para cuatro de cinco especies, con cambios dependientes de especie y escenario.
   - Límite: no atribuir el cambio a Deepwater Horizon; los autores no pueden establecer causalidad por falta de muestras genéticas anteriores al derrame. El mapa de crucero DP02 2015 es solo una ventana contextual, no todas las estaciones de la serie.
   - Verificación: el enlace DOI redirigió al dominio editorial; PDF primario accesible. Crossref REST no se obtuvo directamente.

3. **Reclasificación de `Westlothiana`, fósil de aproximadamente 345 millones de años.**
   - Fuente primaria: *Nature*, DOI 10.1038/s41586-026-11090-6. Cobertura de ScienceDaily, 26-11-2026: [nota](https://www.sciencedaily.com/releases/2026/11/261125045239.htm).
   - Observación: la nueva evidencia anatómica lo ubica como tetrápodo troncal, no como el reptil más antiguo.
   - Límite: no convertir la reclasificación en una afirmación de que ya era un amniota o un reptil temprano.
   - Verificación: enlace DOI redirigió a Nature; Crossref REST pendiente.

4. **L-BAIBA y adaptación muscular asociada al ejercicio.**
   - Fuente primaria: *Nature Communications*, DOI 10.1038/s41467-026-76307-8. Cobertura de ScienceDaily, 26-11-2026: [nota](https://www.sciencedaily.com/releases/2026/11/261125045244.htm).
   - Observación: el estudio investiga una molécula asociada al ejercicio y respuestas metabólicas/musculares en modelos experimentales.
   - Límite: no recomendar suplementos ni extrapolar eficacia a humanos sin evidencia clínica.
   - Verificación: enlace DOI redirigió a Nature; Crossref REST pendiente.

5. **Dimorfismo sexual en `Uintatherium`.**
   - Fuente primaria: *PLOS ONE*, DOI 10.1371/journal.pone.0345236. [Artículo primario](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0345236). Cobertura de ScienceDaily, 26-11-2026: [nota](https://www.sciencedaily.com/releases/2026/11/261125045251.htm).
   - Observación: el análisis morfométrico no respalda una separación extrema y simple entre cráneos masculinos y femeninos.
   - Límite: no asignar sexo a cada cráneo individual ni presentar la discusión como resuelta por completo.
   - Verificación: enlace DOI redirigió a PLOS; Crossref REST pendiente.

### Reclasificación del corte inicial 00:02

Los cinco candidatos iniciales (turberas, cemento por plasma, complejidad de copas, coagulante de algas y madera) se conservan como históricos, pero siguen `PENDING_SOURCE` hasta comprobar que cada DOI/URL conduce al artículo que afirma la ficha. No se usaron para el storyboard matutino. PAV1 deja de ser solo vigilancia y pasa a candidato principal por artículo original del 26-11, DOI visible, resultados explícitos y coordenada de aislamiento publicada.

### Decisión de slot

- **27-11 07:00:** libre en la ventana activa 06:30–07:30; se creó borrador PAV1 en `proyectos/`.
- **27-11 23:30:** no disponible; main reserva el mismo fecha+slot para Stubbs, con render reportado de 86.13 s. No crear una segunda entrada para ese slot.
- El borrador PAV1 queda `BORRADOR_EN_PROYECTOS_NO_APTO_PARA_PROMOCION`: 187 palabras, 8 escenas, 78 s de escenas + 6 s de cortinilla = 84 s, gancho de 5 palabras, voz es-MX-JorgeNeural +7%/-2Hz, mapa con la coordenada publicada de aislamiento, dato/gráfico, ambiente y SFX por escena, `approved_assets=[]`, `export.render_status=NOT_GENERATED`, publicación pendiente. No se ejecutó el validador Python real ni `--check-doi`; no hay narrative_qa por rol de investigador.

## Revalidación RSS/Trends y DOI — 27-11-2026 04:23 CDMX

- `scripts/tendencias.py` fue leído, pero no se pudo ejecutar en el runtime local: la prueba de red a Google Trends RSS y Crossref REST devolvió `URLError: <urlopen error [Errno -3] Temporary failure in name resolution>`; la prueba multi-feed posterior agotó el límite de 30 s. No se atribuyen esos errores a los servidores de origen.
- Consulta web directa de feeds: ScienceDaily devolvió `HTTP 400 Unsupported content-type application/xml`; NASA, Nature y UNAM Global devolvieron `HTTP 400 Unsupported content-type application/rss+xml`; ESA devolvió `404 Not Found`; Phys.org, EurekAlert y SINC no fueron accesibles desde esta herramienta. Google Trends RSS tampoco fue accesible.
- **Respaldo oficial:** la página HTML de Google Trends México sí respondió y mostró 260 tendencias; las primeras 25 se concentraron en deportes, clima, aguinaldo y actualidad general, sin candidato científico/natural admisible. No se añade tema por tendencia.
- **PAV1:** el artículo primario de Frontiers está accesible, publicado el 26-11-2026, con DOI visible `10.3389/fpls.2026.2008228`. La consulta directa a Crossref REST falló por resolución DNS y la herramienta no confirmó la redirección `doi.org`; se mantiene `VERIFICADO_URL`, Crossref/`--check-doi` pendiente. El storyboard conserva el slot libre 07:00, pero su QA narrativo quedó `FAIL/0` por `REVISION_INDEPENDIENTE_AUSENTE`; no es apto para promoción.
- Los cinco candidatos activos del radar se conservan sin añadir uno nuevo: PAV1, riesgo genético mesopelágico, `Westlothiana`, L-BAIBA y `Uintatherium`. Los otros cuatro continúan con la verificación DOI/Crossref pendiente; no se inventan resoluciones.


## Revalidación de fuentes y tendencias — 27-11-2026, 05:58 CDMX

- Se ejecutó una copia local del código vigente de `scripts/tendencias.py` con `--geo MX --dias 7`. Los diez RSS científicos configurados fallaron por DNS: `URLError(gaierror(-3, 'Temporary failure in name resolution'))`. Google Trends RSS devolvió el mismo error; salida del script: lista vacía. No se interpretó como ausencia de noticias.
- Respaldo oficial: Google Trends HTML México, últimas 24 horas, mostró 249 tendencias. Las primeras 25 estuvieron dominadas por deportes, clima, asuntos de consumo y actualidad; no apareció un candidato científico/natural apto.
- PAV1: la página completa de Frontiers confirma publicación el 26-11-2026, DOI `10.3389/fpls.2026.2008228` y el punto de aislamiento `41.1081 N, 16.2606 E` en Métodos. El DOI resolver mostró redirección hacia la URL editorial de Frontiers; el runtime no pudo recuperar esa URL redirigida y Crossref REST siguió inaccesible por DNS. Se conserva `VERIFICADO_URL`; no se marca Crossref como verificado.
- No se añade candidato ni storyboard nuevo: las demás candidaturas siguen con compuertas de fuente/DOI pendientes y el slot siguiente de 23:30 está ocupado en main.

## Reconsulta del 27-11-2026, 07:59 CDMX — corte adicional

### Ingesta y respaldo de tendencias

Se probaron directamente los diez RSS definidos en `scripts/tendencias.py` (ScienceDaily ciencia/salud/espacio, Phys.org, NASA, ESA, Nature, EurekAlert, SINC y UNAM Global) y Google Trends RSS México. Los once endpoints devolvieron el mismo error exacto:

`URLError(gaierror(-3, 'Temporary failure in name resolution'))`

Respaldo oficial consultado: [Google Trends México, últimas 24 horas](https://trends.google.com/trending?geo=MX&hl=es). La página mostró 249 tendencias; el primer bloque de 25 estuvo dominado por fútbol, clima, aguinaldo y búsquedas de actualidad. No apareció un candidato científico útil. Los candidatos siguientes proceden de artículos primarios recientes, no de una tendencia social.

### Tres candidatos primarios nuevos

#### 1. EpTFIIAγ: un factor de un hongo formador de líquenes mejora el rendimiento bajo sequía

- **Artículo:** Du et al., “An extremophile transgene improves drought resistance and yield in cereals”, *Nature*, publicado en línea el 25-11-2026.
- **DOI:** 10.1038/s41586-026-11151-w.
- **Fuente primaria:** https://www.nature.com/articles/s41586-026-11151-w.pdf
- **Observación:** EpTFIIAγ procede del micobionte del liquen *Endocarpon pusillum*. En cinco fondos de trigo, el artículo reporta aumentos de 19.4–32.8% en rendimiento por parcela bajo condiciones de agua limitada; también informa aumentos de rendimiento por planta en arroz y maíz. En Yangling, las parcelas limitadas recibieron aproximadamente 30% del volumen de agua de las parcelas con riego completo. Los Métodos publican coordenadas de Yangling, Heyang, Cangzhou y Linfen.
- **Cálculo:** las coordenadas DMS del artículo se convirtieron a decimal sin interpolar parcelas: Yangling 34.266667, 108.066667; Heyang 35.716667, 110.033333; Cangzhou 38.550000, 116.633333; Linfen 36.933333, 112.566667.
- **Inferencia:** el factor podría ser un recurso para programas de mejoramiento, pero el estudio no demuestra una variedad comercial disponible ni una solución universal.
- **Recomendación:** candidato principal para el slot libre 2026-11-30, 17:00. Se creó el borrador `proyectos/2026-11-30_liquen-gen-cereales/storyboard.json`; sigue como PROPUESTA_PENDIENTE_DECISION_GROK.
- **Verificación:** URL primaria accesible y artículo completo inspeccionado. Crossref REST y doi.org no pudieron resolverse por DNS; estado DOI = PENDING_CROSSREF. No promover.

#### 2. La marca m⁶A y la proteína YTH.2 preparan al parásito de malaria para el cambio de huésped

- **Artículo:** Mussgnug et al., “Temperature-sensitive N6-methyladenosine interactions prime the malaria parasite for transmission”, *Nature Microbiology*, publicado en línea el 25-11-2026.
- **DOI:** 10.1038/s41564-026-02516-y.
- **Fuente primaria:** https://www.nature.com/articles/s41564-026-02516-y.pdf
- **Observación:** en gametocitos masculinos de *Plasmodium falciparum*, YTH.2 reconoce transcritos marcados con m⁶A y reprime su traducción después de la ingestión por el mosquito. La interacción represora es sensible a la temperatura y requiere el descenso térmico asociado a la transmisión. El artículo distingue ese descenso del aumento de pH y del ácido xanturénico, que también participan en la activación.
- **Inferencia:** el parásito prepara parte de su respuesta antes de entrar al mosquito; el hallazgo es un mecanismo celular, no un tratamiento ni una intervención de campo.
- **Recomendación:** conservar como candidato para un slot posterior libre; no duplicar el slot de 30-11 ya asignado al borrador de EpTFIIAγ.
- **Verificación:** PDF primario accesible e inspeccionado. DOI = PENDING_CROSSREF por el mismo fallo DNS.

#### 3. Dos compuestos etiquetados como inhibidores de cPLA₂ también inhiben LTA₄H

- **Artículo:** König et al., “Unmasking a molecular impostor: cPLA₂ inhibitors emerge as potent LTA₄H suppressors”, *Frontiers in Pharmacology*, investigación original publicada el 26-11-2026.
- **DOI:** 10.3389/fphar.2026.1944522.
- **Fuente primaria:** https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2026.1944522/full
- **Observación:** CAY10641 y CAY10650, descritos previamente como inhibidores de cPLA₂, suprimieron LTB₄ mediante inhibición de LTA₄H; los IC₅₀ reportados en PMNL estimulados fueron 37 ± 4 nM y 36 ± 4 nM, respectivamente.
- **Inferencia:** algunos resultados farmacológicos previos podrían requerir reinterpretación por actividad fuera del blanco. La evidencia del artículo es experimental/in vitro; no demuestra eficacia clínica.
- **Recomendación:** candidato de menor prioridad editorial por su complejidad bioquímica, pero útil para una cápsula sobre especificidad farmacológica.
- **Verificación:** página primaria accesible e inspeccionada. DOI = PENDING_CROSSREF por el mismo fallo DNS.

### Compuertas del corte

- El acceso DNS fallido impidió ejecutar una verificación Crossref/resolvedor satisfactoria para los tres DOI. No se sustituyó esa compuerta por la mera presencia del DOI en el artículo.
- El único storyboard nuevo es un borrador en `proyectos/`; no contiene `narrative_qa`, no está marcado PREPARADO y no tiene medios.
- `approved_assets=[]`, `export.render_status=NOT_GENERATED` y `publicacion.status=PENDIENTE_DECISION_GROK`.
- La promoción permanece bloqueada hasta DOI/Crossref, validador estructural real y revisión narrativa independiente PASS.


## Revalidación de fuentes y tendencias — 27-11-2026, 09:59 CDMX

### Ingesta RSS y respaldo de tendencias

Se intentó abrir cada URL declarada en `scripts/tendencias.py`. El visor web no pudo consumir los XML/RSS; los errores exactos fueron:

| Feed | Resultado de apertura directa |
|---|---|
| ScienceDaily Science, Health y Space | `400 Unsupported content-type: application/xml` |
| Phys.org | `400 Unsupported content-type: text/xml` |
| NASA | `400 Unsupported content-type: application/rss+xml` |
| ESA Space Science | `404 Not Found` |
| Nature RSS | `400 Unsupported content-type: application/rss+xml` |
| EurekAlert | `URL ... is not accessible via this tool` |
| Agencia SINC | `URL ... is not accessible via this tool` |
| UNAM Global | `400 Unsupported content-type: application/rss+xml` |
| Google Trends RSS México | `URL ... is not accessible via this tool` |

No se atribuyen los errores de tipo de contenido a una caída de los feeds. Tampoco se afirma una nueva ejecución local de `tendencias.py`: el intento de recuperar los scripts desde GitHub en el contenedor falló con `curl: (6) Could not resolve host: raw.githubusercontent.com`.

**Respaldo oficial:** [Google Trends México, últimas 24 horas](https://trends.google.com/trending?geo=MX) mostró 250 tendencias. En las primeras 25, la señal científica/natural más clara fue “agujero de la capa de ozono” (2K+ búsquedas, activa unas 6 horas antes del corte). Se conserva solo como señal de tendencia: `PENDING_SOURCE`; no se encontró en este corte un artículo primario específico que permita convertirla en candidato.

### Shortlist vigente del corte — cinco candidatos

Los cinco elementos siguientes forman la shortlist de este corte. Los candidatos de cortes anteriores (PAV1, riesgo mesopelágico, `Westlothiana`, L-BAIBA, `Uintatherium`, turberas, cemento, copas forestales, coagulante algal y madera) permanecen como registros históricos/vigilancia; no se promueven ni se vuelven a contar en esta shortlist.

#### 1. EpTFIIAγ de un hongo formador de líquenes — candidato principal ya en borrador

- **Fuente primaria:** Du et al., *Nature*, publicado el 25-11-2026. [Artículo y PDF primarios](https://www.nature.com/articles/s41586-026-11151-w.pdf). DOI: `10.1038/s41586-026-11151-w`.
- **Observación:** la expresión heteróloga de EpTFIIAγ mejoró el rendimiento por parcela de cinco cultivares de trigo bajo déficit hídrico en 19.4–32.8%; el artículo también informa aumentos de rendimiento por planta en arroz y maíz.
- **Cálculo:** ninguno adicional; las cifras son las reportadas por el artículo. Las coordenadas de cuatro sitios de trigo se convirtieron de grados/minutos a decimales y se documentaron en el storyboard.
- **Inferencia:** el factor puede ayudar a coordinar respuestas al estrés y programas de desarrollo; no demuestra una variedad comercial disponible ni una solución universal.
- **Recomendación:** mantener como candidato principal para el slot de 30-11 17:00, sujeto a compuertas. El storyboard sigue siendo borrador.
- **DOI:** `PENDING_CROSSREF`; la página/PDF primaria muestra el DOI, pero Crossref y `doi.org` no fueron accesibles en esta sesión.

#### 2. m⁶A/YTH.2 y la transmisión de malaria

- **Fuente primaria:** Mussgnug et al., *Nature Microbiology*, 25-11-2026. [Artículo primario](https://www.nature.com/articles/s41564-026-02516-y.pdf). DOI: `10.1038/s41564-026-02516-y`.
- **Observación:** en gametocitos masculinos de *Plasmodium falciparum*, YTH.2 reconoce transcritos marcados con m⁶A y reprime su traducción; el descenso térmico asociado a la ingestión por el mosquito modifica esa interacción.
- **Cálculo:** ninguno.
- **Inferencia:** parte de la preparación para la transmisión depende de una respuesta molecular sensible a temperatura; no es evidencia de tratamiento ni de control del mosquito en campo.
- **Recomendación:** candidato de prioridad media-alta para un slot posterior, sin duplicar el de EpTFIIAγ.
- **DOI:** `PENDING_CROSSREF`.

#### 3. Actividad fuera del blanco de inhibidores de cPLA₂

- **Fuente primaria:** König et al., *Frontiers in Pharmacology*, Original Research, 26-11-2026. [Artículo primario](https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2026.1944522/full). DOI: `10.3389/fphar.2026.1944522`.
- **Observación:** CAY10641 y CAY10650, descritos como inhibidores de cPLA₂, también suprimieron LTB₄ mediante inhibición de LTA₄H; los IC₅₀ reportados en PMNL estimulados fueron 37 ± 4 nM y 36 ± 4 nM.
- **Cálculo:** ninguno.
- **Inferencia:** resultados farmacológicos previos pueden requerir reinterpretación por actividad fuera del blanco; la evidencia es experimental/in vitro y no demuestra eficacia clínica.
- **Recomendación:** prioridad media por complejidad bioquímica; útil para explicar por qué “inhibidor selectivo” requiere comprobar el blanco real.
- **DOI:** `PENDING_CROSSREF`.

#### 4. Ensamblaje de transposasas CRISPR tipo I-F (CAST)

- **Fuente primaria:** Finocchio et al., *Nature*, publicado el 25-11-2026. [Artículo primario](https://www.nature.com/articles/s41586-026-11196-x.pdf). DOI: `10.1038/s41586-026-11196-x`.
- **Observación:** mediante cryo-EM y ensayos de transposición, el trabajo describe estados funcionales de PseCAST: formación de un R-loop, heptamerización de TnsC, reclutamiento de TnsAB y remodelación alostérica que activa la integración de ADN donador.
- **Cálculo:** ninguno.
- **Inferencia:** el mecanismo ofrece una base estructural para ingeniería de sistemas de integración guiados por ARN; no demuestra una terapia ni una edición clínica segura.
- **Recomendación:** prioridad media-alta, condicionada a explicar que el resultado es mecanístico y estructural. No crear storyboard: no hay coordenadas geográficas de ensayo publicadas que respalden un mapa geográfico exigido por el contrato.
- **DOI:** `PENDING_CROSSREF`; el PDF primario muestra el DOI, pero el resolvedor no se pudo consultar.

#### 5. Circuito intestino-cerebro que regula la ingestión de azúcar en *Drosophila*

- **Fuente primaria:** Cui et al., *Nature*, publicado el 25-11-2026. [Artículo primario](https://www.nature.com/articles/s41586-026-11315-8). DOI: `10.1038/s41586-026-11315-8`.
- **Observación:** neuronas sensoriales entéricas que detectan azúcar envían señal excitatoria a neuronas cerebrales IN1; estas inhiben neuronas motoras entéricas que controlan el conducto del crop, relajan su musculatura y facilitan el paso de alimento al crop.
- **Cálculo:** ninguno; no se añaden porcentajes ni tamaños de efecto ausentes del resumen consultado.
- **Inferencia:** en moscas, la detección de nutrientes en el intestino puede modular directamente la salida motora que sostiene la ingestión; no extrapolar el circuito a humanos.
- **Recomendación:** prioridad alta por su secuencia visual sensor → cerebro → músculo; no crear storyboard hasta disponer de un mapa/capa compatible con el contrato y de un slot verificado.
- **DOI:** `PENDING_CROSSREF`.

### Compuertas y decisiones del corte

- Crossref REST y `doi.org` devolvieron “URL ... is not accessible via this tool”; no se marca ningún DOI nuevo como verificado por resolver.
- No se creó storyboard para 27-11 17:00: aunque el horario maestro contempla la ventana 16:30–18:00 y los registros de main consultados no muestran ese slot, no existe en el árbol una fuente de historial/programación externa que permita descartar de forma suficiente un ID antiguo ya programado. Se deja sin desarrollar para no arriesgar duplicación.
- El borrador de EpTFIIAγ del 30-11 17:00 sigue en `proyectos/`, sin `narrative_qa`, sin entrada plana en `cola/entrada/` y sin estado Grok confirmado. No es dispatchable.
- No se generaron medios ni se consumieron créditos.
