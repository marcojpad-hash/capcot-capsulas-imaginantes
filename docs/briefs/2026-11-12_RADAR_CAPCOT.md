# RADAR CAPCOT — 2026-11-12

**Corte:** jueves 12 de noviembre de 2026, 08:00 America/Mexico_City  
**Repositorio:** `marcojpad-hash/capcot-capsulas-imaginantes`  
**Rama:** `feature/capcot-video-discovery-continuity`  
**Rol de esta entrega:** investigación, documentación y borrador textual. No es selección editorial final de Grok.

## 1. Guardia de duplicación y ventana

- Enumeración de `proyectos/`, `salidas/`, `cola/entrada/` y `cola/bloqueados/`: **sin project_id del 2026-11-12**.
- `data/temas_del_dia.json`, `data/rotacion.json` y `data/publicaciones.json` no contienen asignación para el 12-nov.
- No existe `data/horario_2026-11-12.json`.
- Según `data/horarios.json`, las ventanas activas son 06:30–07:30 y 16:30–18:00 CDMX. La ventana 13:30 está en prueba, no se toma como activa; 23:30 queda excluida por la instrucción vigente. La ventana de tarde tiene días preferentes mar/mié/sáb; jueves no es preferente, pero la ventana sigue activa.
- A las 08:00 la ventana matutina ya pasó. Se usa **17:00 únicamente como referencia de staging** dentro de 16:30–18:00; no es una hora de publicación ni programa nada.
- No se reescribió ningún proyecto ajeno ni se creó copia en cola.

## 2. RSS y tendencias

### RSS científicos

Se consultaron las URL declaradas en `scripts/tendencias.py`. El lector web no entregó XML utilizable; **no se afirma que se haya parseado XML**.

| Feed | Resultado exacto de lectura |
|---|---|
| ScienceDaily — Science | HTTP 400: tipo de contenido XML no compatible con el lector web (`application/xml`) |
| ScienceDaily — Health | HTTP 400: tipo de contenido XML no compatible (`application/xml`) |
| ScienceDaily — Space/Time | HTTP 400: tipo de contenido XML no compatible (`application/xml`) |
| Phys.org | HTTP 400: tipo de contenido XML no compatible (`text/xml`) |
| NASA News Release | HTTP 400: tipo de contenido RSS/XML no compatible (`application/rss+xml`) |
| ESA Space Science | HTTP 404: Not Found |
| Nature RSS | HTTP 400: tipo de contenido RSS/XML no compatible (`application/rss+xml`) |
| EurekAlert | URL no accesible mediante el lector web; no se obtuvo XML |
| Agencia SINC | URL no accesible mediante el lector web; no se obtuvo XML |
| UNAM Global | HTTP 400: tipo de contenido RSS/XML no compatible (`application/rss+xml`) |
| Google Trends RSS México | URL no accesible mediante el lector web; no se obtuvo XML |

El script no se ejecutó contra esos feeds desde un entorno de red alternativo. No se inventan titulares ni se afirma que se leyeron los XML.

### Google Trends México — respaldo oficial

Se abrió **Trending Now** oficial para México: [trends.google.com/trending?geo=MX&hl=es](https://trends.google.com/trending?geo=MX&hl=es). En la captura se mostraban 145 tendencias; las señales visibles de mayor afinidad con ciencia/naturaleza fueron clima, tiempo y frente frío. La lista estuvo dominada por actualidad general, deporte y entretenimiento; no apareció una tendencia inequívoca sobre comunicación de chimpancés, contaminación acústica o gastruloides. La tendencia no se usa como prueba científica ni como sustituto de publicación primaria.

## 3. Candidatos publicados dentro de los últimos siete días

### Candidato principal propuesto — Convenciones vocales en chimpancés

- **Estudio:** Antoine Valet, Richard Moore, Tatiana Bortolato, Tal Kleinhause Gedalyahou, Aude de Witasse-Thézy, Cédric Girard-Buttoz, Roman M. Wittig y Catherine Crockford (2026). “A signal convention in natural chimpanzee communication”. *Proceedings of the National Academy of Sciences*, 123(47), e2606837123. Publicación: 9-nov-2026.
- **DOI listado por la editorial:** `10.1073/pnas.2606837123`. **Estado: PENDIENTE_RESOLVEDOR.** La página editorial PNAS es accesible y muestra el artículo y el DOI; el clic al resolvedor `doi.org` devolvió HTTP 500 y no se obtuvo registro Crossref utilizable. No se declara el DOI validado por resolvedor.
- **Enlace editorial verificable:** [PNAS — artículo original](https://www.pnas.org/doi/10.1073/pnas.2606837123).
- **Contraste oficial:** [University of Warwick — comunicado de investigación](https://warwick.ac.uk/news/pressreleases/chimpanzees-blowing-raspberries/), 10-nov-2026.
- **Observado:** 91 chimpancés, de 0 a 55 años, en ocho grupos; cuatro comunidades silvestres de Taï y cuatro grupos de Tacugama. El uso de llamadas sin voz parecidas a una pedorreta fue más estable y concentrado en un contexto cuando había modelos adultos; en grupos sin esos modelos fue más variable. En un grupo del santuario, la incorporación de un adulto estuvo seguida por un uso más consistente y parecido al del recién llegado.
- **Línea temática:** Naturaleza/bichos; actualidad científica; comunicación animal y aprendizaje social.
- **Tendencia:** baja/no señal específica en Google Trends México.
- **Relevancia científica:** alta; el estudio aborda convenciones de uso de señales y aprendizaje social en comunicación natural.
- **Oportunidad editorial:** alta; gancho visual y comprensible, con giro claro: no se aprende necesariamente un sonido nuevo, sino cuándo usar una llamada que ya existe.
- **Público/ocasión:** público general interesado en animales y conducta; formato móvil de 75–90 s.
- **Riesgos:** diseño cuasiexperimental; los grupos tienen historias y entornos distintos; el cambio tras introducir un adulto se observó en un solo grupo. No llamarlo lenguaje humano, palabra ni prueba de sintaxis. No afirmar que aprendieron a producir un sonido nuevo.
- **Verificación:** artículo primario PNAS consultado; DOI pendiente de resolución independiente. Comunicado de Warwick consultado para sitios, grupos y caso del adulto recién incorporado.

### Candidato 2 — Contaminación acústica como amenaza global

- **Estudio:** Hansjoerg P. Kunc y Rouven Schmidt (2026). “Echoes of the Anthropocene: Noise pollution as a global threat”. *Science*, 394, 660–664. Publicación: 5-nov-2026.
- **DOI:** `10.1126/science.adu9593`. **Estado: PENDIENTE_RESOLVEDOR.** El registro institucional de Queen’s University Belfast muestra metadatos, DOI y resumen; el acceso a Science devolvió 403 y la resolución independiente no quedó confirmada.
- **Fuente primaria institucional:** [Queen’s University Belfast — registro y manuscrito aceptado](https://pure.qub.ac.uk/en/publications/echoes-of-the-anthropocene-noise-pollution-as-a-global-threat/). [Enlace editorial Science](https://www.science.org/doi/10.1126/science.adu9593).
- **Observado:** meta-análisis de 214 estudios experimentales y 177 especies terrestres y acuáticas; los rangos de las especies cubrían seis continentes. En el 80% de las especies estudiadas, el ruido alteró al menos un rasgo fisiológico, del desarrollo o del comportamiento; las respuestas variaron y hubo especies favorecidas y perjudicadas.
- **Línea temática:** Naturaleza/bichos; ecología del sonido.
- **Tendencia:** afinidad indirecta con términos de clima/ambiente; no se observó tendencia específica de ruido.
- **Relevancia científica:** alta.
- **Oportunidad editorial:** alta; estadística potente y visual global.
- **Público/ocasión:** público general interesado en biodiversidad y ambiente.
- **Riesgos:** el 80% corresponde solo a las especies incluidas en el meta-análisis, no a todas las especies del planeta; no todas responden igual. No usar porcentajes secundarios de mortalidad no contrastados en el resumen primario.
- **Verificación:** resumen y metadatos del registro institucional consultados; DOI pendiente de resolvedor.

### Candidato 3 — Rutas alternativas de elongación en gastruloides

- **Estudio:** Serrano Nájera et al. (2026). “Gastruloids reveal alternative morphogenetic routes for body-axis elongation with distinct cytoskeletal dependencies”. *PNAS*, 123(45), e2606813123. Publicación electrónica: 6-nov-2026.
- **DOI:** `10.1073/pnas.2606813123`. **Estado: PENDIENTE_RESOLVEDOR.** La página editorial/registro bibliográfico muestra el artículo y DOI; el resolvedor directo devolvió HTTP 500.
- **Fuente editorial:** [PNAS — artículo original](https://www.pnas.org/doi/10.1073/pnas.2606813123).
- **Observado:** en modelos celulares in vitro, los gastruloides flotantes formaron un eje posterior único; sobre laminina se aplanaron y generaron varias corrientes celulares con polaridad anteroposterior. La ruta adherida necesitó forminas y tracción mediada por adhesiones focales.
- **Línea temática:** ciencia; biología del desarrollo.
- **Tendencia:** sin señal específica en Trends México.
- **Relevancia científica:** alta.
- **Oportunidad editorial:** media-alta; comparación visual fuerte, pero requiere explicar qué es un gastruloide.
- **Público/ocasión:** público general curioso por biología; necesita analogía visual clara.
- **Riesgos:** modelo in vitro, no embrión completo ni desarrollo humano; no describir las corrientes como varios embriones completos.
- **Verificación:** página editorial consultada; DOI pendiente de resolvedor.

### Candidato 4 — Diversidad de patrones de resiliencia poblacional

- **Estudio:** Merrien et al. (2026). “The diversity of resilience patterns of natural populations decreases closer to human activities”. *Ecology*, 107(11), e70557. Publicación: 5-nov-2026.
- **DOI:** `10.1002/ecy.70557`. **Estado: PENDIENTE_RESOLVEDOR.** La página editorial Wiley apareció en resultados, pero la lectura directa devolvió `DisabledError`; no se completó resolución independiente.
- **Fuente editorial:** [Ecology — Wiley](https://esajournals.onlinelibrary.wiley.com/doi/10.1002/ecy.70557). Registro bibliográfico: [PubMed](https://pubmed.ncbi.nlm.nih.gov/42970683/).
- **Observado:** análisis de 956 poblaciones, 300 especies de plantas y 47 de animales; la diversidad de patrones de resiliencia fue menor cerca de actividades humanas. El resultado no equivale a que todas las poblaciones cercanas sean menos resilientes.
- **Línea temática:** naturaleza; ecología de poblaciones.
- **Tendencia:** baja/no señal específica.
- **Relevancia científica:** alta.
- **Oportunidad editorial:** media; requiere explicar “diversidad de resiliencia” sin simplificarlo a una escala única de mejor/peor.
- **Público/ocasión:** público general interesado en ecología, con mayor necesidad de contexto.
- **Riesgos:** asociación espacial no demuestra causalidad; muchas especies están representadas por una sola población; evitar convertir el resultado en una regla universal.
- **Verificación:** metadatos y resumen del resultado editorial consultados; página completa no accesible y DOI pendiente.

### Candidato 5 — Maullidos de gatos ante la presencia humana

- **Estudio:** Fukimoto et al. (2026), *Animal Behaviour*, artículo 123756. Título de trabajo indexado: “The social use of meow in the interaction between cats and humans”.
- **DOI listado en la referencia editorial:** `10.1016/j.anbehav.2026.123756`. **Estado: PENDIENTE_RESOLVEDOR y PENDIENTE_FUENTE_PRIMARIA.** ScienceDirect devolvió HTTP 403; los detalles disponibles proceden de cobertura secundaria.
- **Enlace editorial:** [ScienceDirect — artículo](https://www.sciencedirect.com/science/article/abs/pii/S0003347226002940). Cobertura secundaria: [ScienceAlert](https://www.sciencealert.com/cats-meow-more-when-humans-are-present-study-finds).
- **Observado en la cobertura secundaria:** 38 gatos seleccionados porque sus tutores reportaban maullidos relacionados con comida; se reportaron 86 maullidos con una persona presente y 20 cuando estaba ausente.
- **Línea temática:** animales; comunicación humano-animal.
- **Tendencia:** sin señal específica comprobada en Trends México.
- **Relevancia científica:** media; diseño pequeño y muestra seleccionada.
- **Oportunidad editorial:** alta, pero no se elige como principal por falta de acceso al estudio original.
- **Público/ocasión:** público general y amantes de gatos.
- **Riesgos:** no inferir intención consciente de pedir ayuda ni generalizar a todos los gatos; no confundir conteos totales con tasa individual.
- **Verificación:** cobertura secundaria disponible; fuente primaria y DOI pendientes.

## 4. Recomendación editorial provisional

**Candidato principal propuesto para revisión independiente:** “A signal convention in natural chimpanzee communication”.

La fuerza del hallazgo está en separar la producción del sonido de la regla social para usarlo. El gancho es una llamada parecida a una pedorreta durante el acicalamiento; el giro es que el contexto de uso aparece más estable donde hay modelos adultos. El caso del adulto incorporado aporta una pista adicional, pero no elimina los límites del diseño cuasiexperimental.

Grok conserva la decisión editorial final, el QA oficial, la generación audiovisual y la publicación. El borrador se deja solo en `proyectos/`.

## 5. Separación de evidencia

- **Observado:** 91 chimpancés, ocho grupos, dos sitios; patrón de uso de llamadas distinto según presencia de modelos adultos; un caso de incorporación de adulto seguido de mayor consistencia.
- **Cálculo:** cuatro comunidades silvestres + cuatro grupos de santuario = ocho grupos; el borrador usa 198 palabras narradas, ocho escenas y 78 s de escenas + 6 s de cortinilla = 84 s.
- **Inferencia:** el patrón es compatible con aprendizaje social de la ocasión de uso de una señal existente. El diseño no permite afirmar que el adulto causó por sí solo todos los cambios ni que los chimpancés aprendieron lenguaje humano.
- **Recomendación:** conservar “aprenden cuándo usar una llamada que ya producen”; evitar “hablan”, “aprenden palabras” o “inventan un sonido”.

## 6. Estado de QA narrativo preexistente

El último inventario exhaustivo disponible es el radar del 11-nov-2026: **83 storyboards canónicos únicos; 24 con `narrative_qa` (8 PASS y 16 FAIL); 59 PENDIENTE_AUDITOR; 13 directorios de proyecto sin storyboard**. Véase [radar del 11-nov](./2026-11-11_RADAR_CAPCOT.md) para el detalle de ese corte.

Desde ese corte se añadió a `cola/entrada/` el storyboard `2026-11-11_dato-ratas-topo-damaraland`; su JSON no contiene `narrative_qa`, por lo que está **PENDIENTE_AUDITOR**. El storyboard del 10-nov `2026-11-10_comida-aprendizaje-sabor-nutriente` contiene QA **PASS/92**, con siete checks verdaderos y `critical_flags=[]`. No se escribió ni modificó QA en esta ejecución. El nuevo borrador del 12-nov tampoco contiene `narrative_qa`; queda reservado al auditor independiente.

## 7. Seguimiento técnico Meta / Google Trends

Se revisaron los cambios oficiales disponibles de Meta Graph API, Instagram Insights, Facebook Pages Insights y Google Trends API alfa frente a `docs/INVESTIGACION_API_META_Y_GOOGLE_TRENDS.md`.

- Las páginas oficiales de Meta no pudieron leerse de forma estable en esta sesión (respuestas 429/403); no se confirma un cambio nuevo posterior al ya registrado en el informe.
- La documentación oficial de Google Trends API sigue describiendo acceso alfa limitado; no se encontró anuncio oficial nuevo de disponibilidad general.
- **Resultado:** no hay cambio nuevo sustentado que justifique reescribir `docs/INVESTIGACION_API_META_Y_GOOGLE_TRENDS.md`.

## 8. Cumplimiento

- Entregables de esta fecha: este brief y `proyectos/2026-11-12_dato-pedorreta-chimpances/storyboard.json`; no se crea `*_fuentes.md`.
- El storyboard permanece en `proyectos/`; no se escribe en `cola/entrada/` ni `cola/bloqueados/`.
- No se genera ni simula ningún frame, imagen, audio, video o render.
- No se modifica `data/*.json`, `main`, workflows, motores canónicos ni Motor U6.
- No se publica ni programa nada; no se consumen créditos.


## Reejecución idempotente — 2026-11-12

**Resultado: NO_DUPLICAR.** En esta reejecución ya existen el radar de esta fecha y el storyboard canónico `proyectos/2026-11-12_dato-pedorreta-chimpances/storyboard.json`. La carpeta del proyecto contiene únicamente `storyboard.json`; no hay otro proyecto de la fecha en `salidas/`, `cola/entrada/` ni `cola/bloqueados/`. El proyecto declara `fecha_objetivo=2026-11-12` y `slot_local=17:00`, que permanece como referencia de staging y no como programación.

Se volvió a leer el JSON directamente desde GitHub y se comprobó: 8 escenas; 198 palabras de narración; 78 segundos de escenas + 6 de cortinilla = 84 segundos; estilo `collage_cientifico_vintage` con `prompt_base` idéntico al catálogo y distinto del estilo `linograbado` del paquete de 11-nov; fuentes y `source_ids` presentes; capas de mapa y dato/gráfico; voz `edge-tts / es-MX-JorgeNeural / +7% / -2Hz`; `approved_assets=[]`; `export.render_status=NOT_GENERATED`; ausencia de `export.filename` y rutas de medios; `publicacion.status=PENDIENTE_DECISION_GROK`.

El storyboard no contiene `narrative_qa`: estado **PENDIENTE_AUDITOR**. No se realizó QA narrativo ni se modificó el storyboard. No se creó otra propuesta, copia de cola, archivo de fuentes ni medio.

Seguimiento técnico de esta reejecución: las páginas oficiales de Graph API e Instagram Platform devolvieron HTTP 429; la referencia oficial de Page Insights no fue accesible; la página oficial de Google Trends confirma que la API sigue en alfa de acceso limitado. No se encontró un cambio nuevo sustentado respecto del corte técnico ya documentado; el informe técnico no se reescribe.

No se modificaron `data/*.json`, `main`, workflows, motores canónicos ni Motor U6. No se publicó, programó ni consumió créditos.
