# Radar CAPCOT — 5 de noviembre de 2026

**Repositorio:** `marcojpad-hash/capcot-capsulas-imaginantes`  
**Rama:** `feature/capcot-video-discovery-continuity`  
**Corte de investigación y Trends:** 1-nov-2026  
**Entrega:** preproducción textual; sin medios, render, QA audiovisual ni publicación.

## Candidatos científicos recientes (corte 1-nov-2026)

Los cuatro estudios siguientes se publicaron entre el 27 y el 29 de octubre; entran en la ventana de siete días de esta revisión. La parrilla del día mantiene la mezcla de líneas y no desplaza los cuatro paquetes asignados.

| Candidato | Fuente primaria | Hallazgo / límite | Línea |
|---|---|---|---|
| Pardelas y desfase de brújula solar | [Science, DOI 10.1126/science.adz2542](https://doi.org/10.1126/science.adz2542) | Datos GPS de largo plazo; analogía con jet lag solo como explicación del desfase del reloj interno, no como diagnóstico humano. | Naturaleza / comportamiento |
| Cometas y origen de la vida | [Scientific Reports, DOI 10.1038/s41598-026-74214-y](https://doi.org/10.1038/s41598-026-74214-y) | Modelos sugieren que impactos cometarios son una vía poco probable para entregar compuestos prebióticos en concentraciones útiles; no descarta otras rutas. | Química / astronomía |
| Meteorito marciano Teghaza 001 | [Science, DOI 10.1126/science.adz5646](https://doi.org/10.1126/science.adz5646) | Roca de al menos 4.1 mil millones de años; una muestra no representa todo Marte ni demuestra vida. | Geología planetaria |
| Aburrimiento en museos | [Scientific Reports, DOI 10.1038/s41598-026-74062-w](https://doi.org/10.1038/s41598-026-74062-w) | Tres estudios y 1,269 participantes; resultados acotados a dos museos de Viena. | Educación / psicología |

## Google Trends México — observado el 1-nov-2026

Fuente: [Google Trends México, últimas 24 horas](https://trends.google.com.mx/trending?geo=MX&hl=es).

La lista visible está dominada por fútbol, entretenimiento y Día de Muertos. Entre las señales no deportivas aparece **superluna** (≈2 mil búsquedas, según la página). No hay una tendencia científica inequívoca que justifique forzar un vínculo con los temas de la parrilla. La señal se registra como contexto, no como causa de selección editorial.

## Paquetes de la fecha

Los cuatro storyboards del día se encuentran en `cola/entrada/` como JSON de primer nivel. Cada uno contiene fuentes, mapa contextual, capa de dato, biblia visual, voz y SFX. No contiene medios ni autoriza publicación.

## Límites de esta revisión

- Trends se consultó para México, ventana de últimas 24 horas, el 1-nov; no se extrapola a los días futuros.
- Los candidatos recientes son alternativas editoriales; no sustituyen los temas ya asignados.
- El slot de 23:30 es noticia del mismo día o de las 48 horas previas y se investiga el propio día; no se inventa anticipadamente.
- No se afirma recepción, selección, QA ni publicación por Grok.


### Asignación de slots

07:00 Venus; 13:30 palomitas; 17:00 árboles; 19:00 rayo globular.

**Estado:** cuatro paquetes textuales en cola; recepción y decisión de Grok pendientes. El slot de 23:30 queda reservado para noticia científica del mismo día (≤48 h), con fuente primaria y verificación en la fecha de emisión.


## Corrección operativa de estado — 2-nov-2026

La frase anterior «cuatro paquetes textuales en cola» no acredita una entrega a Imaginantes. Verificación del árbol de la rama: Venus, palomitas y árboles están en cola/bloqueados/<project_id>/; rayo globular tiene un JSON directo en cola/bloqueados. Ninguno está en `cola/entrada/`.

- No hay entrega acreditada a Grok/Imaginantes ni acuse individual.
- Los storyboards recuperados tienen 7 escenas y no contienen `narrative_qa`; por tanto, no cumplen el contrato vigente de handoff.
- La receta semanal pide `cola/entrada/<project_id>/` con tres archivos, pero el workflow de despacho escucha únicamente `cola/entrada/*.json` (JSON de primer nivel). La incompatibilidad debe resolverse antes de entregar.
- Estado real: preproducción textual; sin frames, audio, render ni publicación.


### Aclaración de jerarquía documental — 2-nov-2026

Corrección a la nota anterior: la receta semanal del 31-oct es un documento de coordinación legado y contradice el contrato operativo unificado vigente desde 1-nov. La ruta activa es `proyectos/<project_id>/storyboard.json` → QA narrativo independiente PASS → `cola/entrada/<project_id>.json` (JSON de primer nivel). El workflow actual coincide con este contrato; no se debe modificar para aceptar carpetas. Los archivos observados en `cola/bloqueados/` son copias heredadas y no son borradores canónicos listos para promoción. Ver `docs/briefs/2026-11-02_CONTROL_COLA.md`.


## Control de ejecución — 5-nov-2026, 07:59 CDMX

**Resultado: NO_DUPLICAR.** No se creó un segundo storyboard ni se reescribió ninguno de los proyectos canónicos. El radar de esta fecha ya existía antes de esta ejecución; por tanto, tampoco se creó otro brief.

### Inventario verificado del día

| Proyecto canónico | Fecha objetivo | Slot local | Tratamiento |
|---|---|---:|---|
| `2026-11-05_kids-dia-en-venus` | 2026-11-05 | 07:00 | Preexistente; conservar |
| `2026-11-05_comida-palomitas` | 2026-11-05 | 13:30 | Preexistente; conservar |
| `2026-11-05_inter-arboles-se-comunican` | 2026-11-05 | 17:00 | Tema correcto: red micorrícica común / wood-wide web, con Karst et al. 2023. QA narrativo independiente FAIL 78 por apertura genérica, no por desajuste temático; permanece fuera de cola hasta corregir narrativa y superar validación estructural. La variante de respiración nocturna es otro artefacto bloqueado y no es el storyboard canónico. |
| `2026-11-05_inter-rayo-globular` | 2026-11-05 | 17:45 | Preexistente; conservar |

La fuente de horario `data/horario_semana_2026-11-01_07.json` confirma que el segundo slot intermedio se reubicó de 19:00 a **17:45** el 2-nov. Por tanto, la asignación de 19:00 de la sección anterior de este radar queda corregida por esta nota; 19:00 no es un slot libre del lote. El slot 23:30 está excluido de esta ejecución. No queda un slot libre y autorizado para desarrollar un quinto borrador.

Inventario de rutas: los cuatro proyectos están en `proyectos/`; no hay proyecto del 5-nov en `salidas/` ni en `cola/entrada/`. Las variantes observadas en `cola/bloqueados/` no se consideran proyectos alternativos ni se promueven. No se modificó ningún storyboard ni archivo `data/*.json`.

### Alcance de investigación de esta ejecución

El radar preexistente conserva corte de investigación y Google Trends del **1-nov-2026**; no se presenta como una revisión fresca del 5-nov. La guardia anti-duplicación detuvo la creación de paquete porque el radar ya existe y los cuatro slots ordinarios están asignados. No se consultaron ni se parsearon RSS científicos o Google Trends RSS en esta ejecución; no se afirma una lectura XML ni una actualización de candidatos.

### Seguimiento técnico incremental

Consulta de documentación oficial realizada el 5-nov-2026:
- Google Trends API: la documentación oficial sigue presentando acceso alfa limitado, ventana móvil de cinco años, agregaciones diaria/semanal/mensual/anual y desgloses geográficos. Los valores son interés de búsqueda escalado, no volúmenes absolutos. No se identificó un cambio respecto del informe técnico.
- Meta: el changelog de Graph API v26 y las referencias de Instagram Insights y Facebook Page Insights no pudieron recuperarse desde el lector disponible; el changelog de Instagram Platform respondió HTTP 429. No se usa documentación secundaria como sustituto de confirmación oficial ni se atribuye un cambio nuevo a Meta.

**Decisión técnica:** no actualizar `docs/INVESTIGACION_API_META_Y_GOOGLE_TRENDS.md`; no hay un cambio nuevo relevante sustentado por documentación oficial accesible en esta ejecución.
