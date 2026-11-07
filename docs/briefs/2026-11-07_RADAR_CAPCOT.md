# Radar CAPCOT — 7 de noviembre de 2026

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

07:00 huesos del bebé; 13:30 efecto Mpemba; 17:00 sueño de pulpos; 19:00 masa de las nubes.

**Estado:** cuatro paquetes textuales en cola; recepción y decisión de Grok pendientes. El slot de 23:30 queda reservado para noticia científica del mismo día (≤48 h), con fuente primaria y verificación en la fecha de emisión.


## Corrección operativa de estado — 2-nov-2026

La frase anterior «cuatro paquetes textuales en cola» no acredita una entrega a Imaginantes. Verificación del árbol de la rama: Huesos, Mpemba y sueño de pulpos están en cola/bloqueados/<project_id>/; nubes tiene dos representaciones con el mismo project_id en cola/bloqueados. Ninguno está en `cola/entrada/`.

- No hay entrega acreditada a Grok/Imaginantes ni acuse individual.
- Los storyboards recuperados tienen 7 escenas y no contienen `narrative_qa`; por tanto, no cumplen el contrato vigente de handoff.
- La receta semanal pide `cola/entrada/<project_id>/` con tres archivos, pero el workflow de despacho escucha únicamente `cola/entrada/*.json` (JSON de primer nivel). La incompatibilidad debe resolverse antes de entregar.
- Estado real: preproducción textual; sin frames, audio, render ni publicación.


### Aclaración de jerarquía documental — 2-nov-2026

Corrección a la nota anterior: la receta semanal del 31-oct es un documento de coordinación legado y contradice el contrato operativo unificado vigente desde 1-nov. La ruta activa es `proyectos/<project_id>/storyboard.json` → QA narrativo independiente PASS → `cola/entrada/<project_id>.json` (JSON de primer nivel). El workflow actual coincide con este contrato; no se debe modificar para aceptar carpetas. Los archivos observados en `cola/bloqueados/` son copias heredadas y no son borradores canónicos listos para promoción. Ver `docs/briefs/2026-11-02_CONTROL_COLA.md`.


---

## Registro de ejecución — 2026-11-07 08:03 CDMX

### Resultado de guardia anti-duplicación: NO_DUPLICAR

Se releyeron los cuatro storyboards canónicos de la fecha en `proyectos/` y se contrastaron sus metadatos internos con `data/horario_semana_2026-11-01_07.json`:

| project_id | fecha_objetivo | slot_local | Estado de ubicación |
|---|---|---:|---|
| `2026-11-07_kids-huesos-bebe` | 2026-11-07 | 07:00 | `proyectos/<id>/storyboard.json` |
| `2026-11-07_comida-hielo-caliente` | 2026-11-07 | 13:30 | `proyectos/<id>/storyboard.json` |
| `2026-11-07_inter-pulpo-suenos` | 2026-11-07 | 17:00 | `proyectos/<id>/storyboard.json` |
| `2026-11-07_inter-nubes-pesan` | 2026-11-07 | 17:45 | `proyectos/<id>/storyboard.json` |

Los cuatro pares fecha/slot coinciden con la parrilla semanal. La decisión del 2-nov retiró la programación de 19:00 desde el 5-nov y reubicó intermedio_2 a 17:45; 23:30 queda excluido por la instrucción operativa vigente. No queda un slot autorizado libre para otro storyboard de esta fecha.

Inventario de ubicaciones: `cola/entrada/` contiene únicamente `.gitkeep`; no hay entradas de esta fecha. `salidas/` no contiene proyectos del 5–7 nov. `cola/bloqueados/` conserva variantes heredadas, entre ellas `2026-11-07_inter-mpemba-mito`, `2026-11-07_inter-suenos-pulpo`, `2026-11-07_inter-nubes-pesan`, `2026-11-07_extra-nubes-pesan` y `2026-11-07_kids-huesos-bebe`; no se trataron como proyectos canónicos ni como slots libres. No se movió ni modificó ninguno.

El radar de esta fecha ya existía, por lo que no se creó otro. Su corte científico y de Trends sigue siendo **2026-11-01**; los candidatos enumerados arriba no se presentan como una búsqueda nueva del 7-nov ni se certifican como dentro de la ventana móvil de siete días al día de hoy. No se hizo una nueva ingesta RSS ni una nueva selección científica porque todos los entregables aplicables ya existen y no hay slot autorizado libre. Este apéndice registra NO_DUPLICAR y corrige el estado operativo; no actualiza el radar científico.

### Estado de narrative_qa releído desde los 12 JSON canónicos

Se consultó directamente cada `proyectos/<project_id>/storyboard.json`. Los doce contienen `narrative_qa`; por tanto, ninguno queda como `PENDIENTE_AUDITOR`. En todos, `review_basis` es `lectura_en_frio_solo_narracion` y `reviewed_at` es `2026-11-06T15:10:29-06:00`. Los checks se consignan en el orden exacto de las claves del JSON:

1. `pregunta_central_reconstruible`
2. `apertura_in_medias_res`
3. `progresion_por_escena`
4. `transiciones_causales`
5. `giro_cientifico_explicado`
6. `limite_evidencia_explicito`
7. `payoff_cierre_apertura`

`true/false` conserva los booleanos del JSON; las banderas se reproducen literalmente.

#### 5 de noviembre

**2026-11-05_kids-dia-en-venus**
- status: `PASS`; score: `88`.
- review_basis: `lectura_en_frio_solo_narracion`.
- reviewed_at: `2026-11-06T15:10:29-06:00`.
- checks: `pregunta_central_reconstruible=true`, `apertura_in_medias_res=true`, `progresion_por_escena=true`, `transiciones_causales=true`, `giro_cientifico_explicado=true`, `limite_evidencia_explicito=true`, `payoff_cierre_apertura=true`.
- critical_flags: `[]`.

**2026-11-05_comida-palomitas**
- status: `FAIL`; score: `82`.
- review_basis: `lectura_en_frio_solo_narracion`.
- reviewed_at: `2026-11-06T15:10:29-06:00`.
- checks: `pregunta_central_reconstruible=true`, `apertura_in_medias_res=false`, `progresion_por_escena=false`, `transiciones_causales=true`, `giro_cientifico_explicado=true`, `limite_evidencia_explicito=true`, `payoff_cierre_apertura=true`.
- critical_flags: `["APERTURA_DEFINICIONAL_NO_IN_MEDIAS_RES","ESCENA_6_REITERA_CAUSAS_DE_GRANOS_NO_REVENTADOS_SIN_INFORMACION_NUEVA"]`.

**2026-11-05_inter-arboles-se-comunican**
- status: `FAIL`; score: `78`.
- review_basis: `lectura_en_frio_solo_narracion`.
- reviewed_at: `2026-11-06T15:10:29-06:00`.
- checks: `pregunta_central_reconstruible=true`, `apertura_in_medias_res=false`, `progresion_por_escena=true`, `transiciones_causales=true`, `giro_cientifico_explicado=true`, `limite_evidencia_explicito=true`, `payoff_cierre_apertura=true`.
- critical_flags: `["APERTURA_GENERICA_NO_IN_MEDIAS_RES"]`.

**2026-11-05_inter-rayo-globular**
- status: `FAIL`; score: `81`.
- review_basis: `lectura_en_frio_solo_narracion`.
- reviewed_at: `2026-11-06T15:10:29-06:00`.
- checks: `pregunta_central_reconstruible=true`, `apertura_in_medias_res=false`, `progresion_por_escena=true`, `transiciones_causales=true`, `giro_cientifico_explicado=true`, `limite_evidencia_explicito=true`, `payoff_cierre_apertura=true`.
- critical_flags: `["APERTURA_HISTORICA_DESCRIPTIVA_NO_IN_MEDIAS_RES"]`.

#### 6 de noviembre

**2026-11-06_kids-ballena-azul-corazon**
- status: `FAIL`; score: `80`.
- review_basis: `lectura_en_frio_solo_narracion`.
- reviewed_at: `2026-11-06T15:10:29-06:00`.
- checks: `pregunta_central_reconstruible=true`, `apertura_in_medias_res=true`, `progresion_por_escena=true`, `transiciones_causales=true`, `giro_cientifico_explicado=true`, `limite_evidencia_explicito=true`, `payoff_cierre_apertura=false`.
- critical_flags: `["PAYOFF_SOBREAFIRMA_CASI_SE_DETIENE"]`.

**2026-11-06_comida-aguacate-negro**
- status: `FAIL`; score: `79`.
- review_basis: `lectura_en_frio_solo_narracion`.
- reviewed_at: `2026-11-06T15:10:29-06:00`.
- checks: `pregunta_central_reconstruible=true`, `apertura_in_medias_res=true`, `progresion_por_escena=false`, `transiciones_causales=false`, `giro_cientifico_explicado=true`, `limite_evidencia_explicito=true`, `payoff_cierre_apertura=true`.
- critical_flags: `["REPETICION_ESCENAS_5_6_SIN_AVANCE_CAUSAL"]`.

**2026-11-06_inter-ranas-congeladas**
- status: `FAIL`; score: `83`.
- review_basis: `lectura_en_frio_solo_narracion`.
- reviewed_at: `2026-11-06T15:10:29-06:00`.
- checks: `pregunta_central_reconstruible=true`, `apertura_in_medias_res=true`, `progresion_por_escena=false`, `transiciones_causales=false`, `giro_cientifico_explicado=true`, `limite_evidencia_explicito=true`, `payoff_cierre_apertura=true`.
- critical_flags: `["REPETICION_ESCENAS_5_6_LIMITES_DE_ESPECIE_Y_CONDICIONES"]`.

**2026-11-06_inter-arena-cantante**
- status: `PASS`; score: `94`.
- review_basis: `lectura_en_frio_solo_narracion`.
- reviewed_at: `2026-11-06T15:10:29-06:00`.
- checks: `pregunta_central_reconstruible=true`, `apertura_in_medias_res=true`, `progresion_por_escena=true`, `transiciones_causales=true`, `giro_cientifico_explicado=true`, `limite_evidencia_explicito=true`, `payoff_cierre_apertura=true`.
- critical_flags: `[]`.

#### 7 de noviembre

**2026-11-07_kids-huesos-bebe**
- status: `FAIL`; score: `82`.
- review_basis: `lectura_en_frio_solo_narracion`.
- reviewed_at: `2026-11-06T15:10:29-06:00`.
- checks: `pregunta_central_reconstruible=true`, `apertura_in_medias_res=true`, `progresion_por_escena=false`, `transiciones_causales=false`, `giro_cientifico_explicado=true`, `limite_evidencia_explicito=true`, `payoff_cierre_apertura=true`.
- critical_flags: `["ESCENA_6_REPITE_VARIACION_DE_CONTEO_Y_FUSION"]`.

**2026-11-07_comida-hielo-caliente**
- status: `FAIL`; score: `81`.
- review_basis: `lectura_en_frio_solo_narracion`.
- reviewed_at: `2026-11-06T15:10:29-06:00`.
- checks: `pregunta_central_reconstruible=true`, `apertura_in_medias_res=false`, `progresion_por_escena=true`, `transiciones_causales=true`, `giro_cientifico_explicado=true`, `limite_evidencia_explicito=true`, `payoff_cierre_apertura=true`.
- critical_flags: `["APERTURA_DE_CREENCIAS_NO_IN_MEDIAS_RES"]`.

**2026-11-07_inter-pulpo-suenos**
- status: `FAIL`; score: `80`.
- review_basis: `lectura_en_frio_solo_narracion`.
- reviewed_at: `2026-11-06T15:10:29-06:00`.
- checks: `pregunta_central_reconstruible=true`, `apertura_in_medias_res=true`, `progresion_por_escena=false`, `transiciones_causales=false`, `giro_cientifico_explicado=true`, `limite_evidencia_explicito=true`, `payoff_cierre_apertura=false`.
- critical_flags: `["REPETICION_ESCENAS_5_6_Y_PAYOFF_VAGO"]`.

**2026-11-07_inter-nubes-pesan**
- status: `FAIL`; score: `78`.
- review_basis: `lectura_en_frio_solo_narracion`.
- reviewed_at: `2026-11-06T15:10:29-06:00`.
- checks: `pregunta_central_reconstruible=true`, `apertura_in_medias_res=true`, `progresion_por_escena=false`, `transiciones_causales=false`, `giro_cientifico_explicado=true`, `limite_evidencia_explicito=true`, `payoff_cierre_apertura=false`.
- critical_flags: `["ESCENA_7_REITERA_CIFRA_Y_LIMITE_SIN_PAYOFF_DE_SUSPENSION"]`.

**Balance leído:** 2 PASS (Venus y arena cantante) y 10 FAIL. Este registro reproduce el QA preexistente; no se ejecutó una nueva lectura narrativa, no se modificó `narrative_qa`, no se promovió ningún storyboard y no se tocó `cola/entrada/`.

### Seguimiento técnico — 2026-11-07

- **Google Trends API alfa:** la documentación oficial sigue ofreciendo acceso alfa por solicitud limitada, con ventana móvil de cinco años, agregación diaria/semanal/mensual/anual y desgloses regionales/subregionales. La página no anuncia apertura general ni cambio de especificación: https://developers.google.com/search/apis/trends
- **Meta Graph API / Instagram Platform / Facebook Pages Insights:** los endpoints oficiales consultados no pudieron recuperarse en esta ejecución (la página de Instagram Platform devolvió HTTP 429; las referencias Graph API v26.0 y Page Insights no fueron accesibles). Los resultados secundarios describen cambios v26.0 y una fecha de aplicación general del 27-oct-2026, pero no se elevan a especificación CAPCOT sin revalidación directa en el changelog oficial.
- **Decisión:** no se actualizó `docs/INVESTIGACION_API_META_Y_GOOGLE_TRENDS.md`; no hay cambio nuevo de Meta verificable directamente en la documentación oficial consultada. No se hicieron llamadas a activos privados ni se solicitaron credenciales.
- No se ejecutaron cambios técnicos, no se modificó `data/*.json`, no se generaron medios ni se publicó/programó contenido.
