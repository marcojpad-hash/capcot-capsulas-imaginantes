# Radar CAPCOT — 6 de noviembre de 2026

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

07:00 corazón de ballena azul; 13:30 aguacate; 17:00 ranas congeladas; 19:00 dunas cantantes.

**Estado:** cuatro paquetes textuales en cola; recepción y decisión de Grok pendientes. El slot de 23:30 queda reservado para noticia científica del mismo día (≤48 h), con fuente primaria y verificación en la fecha de emisión.


## Corrección operativa de estado — 2-nov-2026

La frase anterior «cuatro paquetes textuales en cola» no acredita una entrega a Imaginantes. Verificación del árbol de la rama: Corazón de ballena, aguacate y ranas están en cola/bloqueados/<project_id>/; dunas cantantes tiene un JSON directo en cola/bloqueados. Ninguno está en `cola/entrada/`.

- No hay entrega acreditada a Grok/Imaginantes ni acuse individual.
- Los storyboards recuperados tienen 7 escenas y no contienen `narrative_qa`; por tanto, no cumplen el contrato vigente de handoff.
- La receta semanal pide `cola/entrada/<project_id>/` con tres archivos, pero el workflow de despacho escucha únicamente `cola/entrada/*.json` (JSON de primer nivel). La incompatibilidad debe resolverse antes de entregar.
- Estado real: preproducción textual; sin frames, audio, render ni publicación.


### Aclaración de jerarquía documental — 2-nov-2026

Corrección a la nota anterior: la receta semanal del 31-oct es un documento de coordinación legado y contradice el contrato operativo unificado vigente desde 1-nov. La ruta activa es `proyectos/<project_id>/storyboard.json` → QA narrativo independiente PASS → `cola/entrada/<project_id>.json` (JSON de primer nivel). El workflow actual coincide con este contrato; no se debe modificar para aceptar carpetas. Los archivos observados en `cola/bloqueados/` son copias heredadas y no son borradores canónicos listos para promoción. Ver `docs/briefs/2026-11-02_CONTROL_COLA.md`.


---

## Control de ejecución — 6-nov-2026, 07:55 CDMX

**Resultado: NO_DUPLICAR.** El radar de la fecha ya existe y los cuatro slots ordinarios autorizados están ocupados por los storyboards canónicos de `proyectos/`. No se crea otro storyboard ni se modifica ninguno de esos proyectos. Esta anotación corrige la asignación horaria anterior de 19:00 y distingue los borradores de cualquier entrega a cola.

### Inventario canónico comprobado en GitHub

| project_id | fecha_objetivo | slot_local | ruta | estado editorial leído |
|---|---|---:|---|---|
| `2026-11-06_kids-ballena-azul-corazon` | 2026-11-06 | 07:00 | `proyectos/2026-11-06_kids-ballena-azul-corazon/storyboard.json` | `BORRADOR_ESPERA_AUDITOR_PASS` |
| `2026-11-06_comida-aguacate-negro` | 2026-11-06 | 13:30 | `proyectos/2026-11-06_comida-aguacate-negro/storyboard.json` | `BORRADOR_ESPERA_AUDITOR_PASS` |
| `2026-11-06_inter-ranas-congeladas` | 2026-11-06 | 17:00 | `proyectos/2026-11-06_inter-ranas-congeladas/storyboard.json` | `BORRADOR_ESPERA_AUDITOR_PASS` |
| `2026-11-06_inter-arena-cantante` | 2026-11-06 | 17:45 | `proyectos/2026-11-06_inter-arena-cantante/storyboard.json` | `BORRADOR_ESPERA_AUDITOR_PASS` |

Los cuatro JSON se releen desde la rama y sus campos `project_id`, `fecha_objetivo`, `slot_local`, `estilo_id` y estado editorial coinciden con la tabla. No se infiere QA PASS por la presencia del contrato narrativo. Permanecen en `proyectos/`, sujetos al auditor independiente.

### Corrección de horario y rutas

- `data/horario_semana_2026-11-01_07.json` asigna para el 6-nov 07:00, 13:30, 17:00 y 17:45. El segundo intermedio se movió de 19:00 a 17:45 desde el 5-nov; 19:00 no es un slot libre.
- El quinto horario, 23:30, está excluido expresamente de esta ejecución.
- El árbol de GitHub contiene `cola/entrada/.gitkeep`, sin paquetes de esta fecha; no hay storyboard del 6-nov en `salidas/`.
- Hay copias heredadas en `cola/bloqueados/` para aguacate, ranas y arena, además de una variante histórica `2026-11-06_inter-corazon-ballena-azul`. No son proyectos canónicos alternativos ni se promueven. Las copias bloqueadas inspeccionadas no contienen `narrative_contract` ni `narrative_qa`.
- `data/temas_del_dia.json` no llega al 6-nov; `data/rotacion.json` y `data/publicaciones.json` tampoco registran ese día. Esto no invalida los cuatro proyectos: `scripts/registro_editorial.py` define los storyboards de `proyectos/` como evidencia de rotación y propuesta, no como publicación. No se modificó ningún `data/*.json`.

### Vigencia de la investigación existente

El radar preexistente conserva corte de investigación y Trends del **1-nov-2026**. Los cuatro candidatos de su tabla (publicados el 27–29-oct) ya no están dentro de la ventana móvil de siete días al 6-nov. No se actualizan ni se presentan como candidatos recientes de esta ejecución: la guardia anti-duplicación encontró el radar existente y ningún slot ordinario libre. No se hizo una nueva verificación Crossref de esos DOI ni una nueva selección de 3–5 estudios.

### Fuentes RSS y Google Trends — observación de esta ejecución

No se afirma haber descargado ni parseado XML. El lector web disponible devolvió estos errores exactos al intentar abrir los feeds definidos en `scripts/tendencias.py`:

- ScienceDaily ciencia, salud y espacio: `400 Unsupported content-type: application/xml`.
- Phys.org: `400 Unsupported content-type: text/xml`.
- NASA: `400 Unsupported content-type: application/rss+xml`.
- Nature: `400 Unsupported content-type: application/rss+xml`.
- UNAM Global: `400 Unsupported content-type: application/rss+xml`.
- ESA Space Science: `404 Not Found`.
- EurekAlert y SINC: `URL ... is not accessible via this tool`.
- Google Trends RSS México (`https://trends.google.com/trending/rss?geo=MX`): `URL ... is not accessible via this tool`.

Como respaldo, se abrió la página oficial [Trending Now de Google Trends México](https://trends.google.com.mx/trending?geo=MX&hl=es), configurada en últimas 24 horas. Entre las señales visibles: «cfe» (20 mil+ búsquedas, activa hace 10 h) y «sismo temblor hoy» (2 mil+, activa hace 14 h); la lista también está dominada por entretenimiento y deportes. Son consultas de búsqueda, no evidencia científica ni prueba de oportunidad editorial. No se fuerza una cápsula a partir de ellas.

### Seguimiento técnico incremental

- Google Trends API: la documentación oficial consultada sigue describiendo una alfa de acceso limitado, ventana móvil de cinco años, agregaciones diaria/semanal/mensual/anual, desgloses regionales y datos de interés escalados —no volúmenes absolutos—: [documentación oficial](https://developers.google.com/search/apis/trends). No se verificó un cambio nuevo respecto del informe del repositorio.
- Meta: el changelog de Graph API no fue accesible; Instagram Platform changelog devolvió `429 Too Many Requests`; la referencia de Instagram Insights no fue accesible; Pages API devolvió `429 Too Many Requests`; la referencia de Page Insights no fue accesible. Sin acceso a las referencias oficiales no se atribuye un cambio nuevo ni se actualiza `docs/INVESTIGACION_API_META_Y_GOOGLE_TRENDS.md`.

**Cierre:** NO_DUPLICAR. El único cambio de esta ejecución es esta anotación de control en el radar existente. No se creó ni reescribió ningún storyboard, no se escribió en `cola/entrada/`, no se añadió `narrative_qa`, no se promovió material y no se alteraron datos operativos.
