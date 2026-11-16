# CONTROL DE COLA Y ROTACIÓN — 2026-11-16

**Corte de auditoría:** 2026-11-16 15:45:46, America/Mexico_City  
**Repositorio:** `marcojpad-hash/capcot-capsulas-imaginantes`  
**Rama:** `feature/capcot-video-discovery-continuity`  
**Rol:** auditoría; no producción ni despacho.

## Resumen ejecutivo

- Briefs confirmados: `2026-11-16_RADAR_CAPCOT.md` y este control.
- Borradores del día en `proyectos/`: **1**.
- Entradas de cola con fecha objetivo 16-nov: **0** (ni JSON de primer nivel ni paquete anidado).
- Salidas del día: **0**.
- Borrador del día: QA narrativo **PASS 91**; estructura revisada estáticamente, pero no se ejecutó el validador real ni `--check-doi`. No está seleccionado ni recibido por Grok.
- Lote obligatorio 5–7-nov: **2 PASS / 10 FAIL** narrativos; **0/12** cumplen el contrato estructural completo.
- Siete proyectos del lote tienen evidencia de publicación/programación en plataformas: **PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR**.
- Recepción Grok del proyecto del día y de los 12 proyectos del lote: **RECEPCION_GROK_NO_CONFIRMADA**.
- No se generaron medios, no se publicaron cápsulas, no se disparó Actions ni se enviaron payloads.

## 1. Briefs y borradores del 16-nov

### Briefs

- `docs/briefs/2026-11-16_RADAR_CAPCOT.md`: existe. Propone un dato sobre microgeles de polen y nanotubos de carbono para la ventana de tarde; el candidato de 23:30 permanece `PENDING_SOURCE` y no tiene paquete.
- `docs/briefs/2026-11-16_CONTROL_COLA.md`: ya existía; se actualiza en este corte para reflejar el estado de los JSON releídos y las ejecuciones actuales.

### Inventario

| project_id | Creación en rama | Fecha objetivo | Slot local | slot_cesta | Ruta | Dispatch |
|---|---|---|---|---|---|---|
| `2026-11-16_dato-polen-desenreda-nanotubos` | 16-nov, commit de origen `37ea4181` | 2026-11-16 | 17:00 CDMX | `intermedio_1` | `proyectos/<id>/storyboard.json` | **NOT_DISPATCHABLE** |

El storyboard no declara `created_at`; la fecha de creación se toma del commit de origen. No hay un `data/horario_2026-11-16.json` ni una selección diaria oficial. Las 17:00 caen dentro de la ventana general de tarde (16:30–18:00), pero el lunes no es día preferente y `intermedio_1` no figura como cesta vigente en `data/horarios.json`. Por tanto sigue siendo **propuesta**, no slot seleccionado.

### Revisión narrativa en frío

Se leyó únicamente la narración concatenada, sin título, resumen, arco, notas ni `narrative_contract`.

- `narrative_qa.status=PASS`
- `score=91`
- `review_basis=lectura_en_frio_solo_narracion`
- Siete checks verdaderos; `critical_flags=[]`
- `reviewed_at=2026-11-16T15:45:46-06:00`

La pregunta central se reconstruye: cómo dispersar nanotubos de carbono en agua sin recurrir a sonicación de alta potencia. La narración abre con la tinta que se apelmaza, desarrolla el mecanismo de captura/fricción de los microgeles de polen, explica la estabilización con alginato, delimita la evidencia de laboratorio y paga la apertura aclarando que el polen no es el conductor. No se inventa un protagonista ni un episodio.

### Estructura — revisión estática

- 8 escenas; 196 palabras de narración.
- 78 s de escenas + cortinilla de 6 s = **84 s**; objetivo declarado 84 s.
- Gancho: 4 palabras.
- Arco: gancho → desarrollo → cierre → reflexión; cierre verbal del canal presente.
- `narrative_contract`: seis campos completos.
- Voz: `es-MX-JorgeNeural`, coherente con ciencia/materiales y con `docs/VOCES_POR_TEMA.md`.
- `estilo_id=collage_cientifico_vintage`: existe en `scripts/estilos.json`; el `prompt_base` coincide exactamente y los ocho prompts visuales empiezan con él. El catálogo lo vincula con botánica.
- `source_ids`: todos resuelven a fuentes declaradas.
- Mapa y capa de dato/gráfico presentes. El pin de Wuhan representa afiliación institucional de autores, **no** el lugar del experimento.
- Ambiente y SFX presentes en las ocho escenas.
- `approved_assets=[]`; `export.render_status=NOT_GENERATED`; no hay `asset_filename`, `asset_type`, `export.filename` ni rutas de medios.
- DOI citado: [10.1038/s41467-026-79607-1](https://doi.org/10.1038/s41467-026-79607-1). La página/PDF oficial de Nature muestra el DOI y publicación en línea del 14-nov-2026. La fuente es un artículo en prensa. El campo de estado sigue `PENDIENTE_RESOLVEDOR`: no se ejecutó Crossref/DOI resolver ni `--check-doi`.

**Estado editorial:** `BORRADOR_EN_PROYECTOS_PENDIENTE_VALIDACION_ESTRUCTURAL`; `publicacion.status=PENDIENTE_DECISION_GROK`. No está seleccionado, no está en producción, no tiene QA audiovisual ni publicación.

**Handoff:** no existe `cola/entrada/<id>.json`, `cola/estado/<id>.json` devuelve 404 y no hay marcador de inbox para este proyecto. **RECEPCION_GROK_NO_CONFIRMADA**. La ubicación bajo `proyectos/` no coincide con los paths del workflow; **NOT_DISPATCHABLE**. No se promovió para evitar un dispatch y porque la selección editorial sigue pendiente.

## 2. Cola, Grok y dispatchabilidad

### Inventario del día

- `cola/entrada/*.json` de primer nivel con fecha 16-nov: **0**.
- `cola/entrada/<project_id>/storyboard.json` con fecha objetivo 16-nov: **0**.
- `proyectos/<project_id>/storyboard.json` del día: **1**, el de polen.
- `salidas/<project_id>/` del día: no existe.
- `cola/estado/2026-11-16_dato-polen-desenreda-nanotubos.json`: 404 → **RECEPCION_GROK_NO_CONFIRMADA**.
- No se creó ni modificó ningún estado Grok.

### Workflow y procesador

El workflow actual `.github/workflows/capcot-grok-dispatch.yml`:

- El trigger `push` escucha `cola/entrada/*.json`, solo archivos JSON en el primer nivel.
- El selector de `workflow_dispatch` usa `find -maxdepth 1` y acepta `cola/entrada/<project_id>.json`.
- No encuentra `proyectos/<id>/storyboard.json` ni `cola/entrada/<id>/storyboard.json` anidado.
- Escribe un marcador `handoffs/grok_inbox`; el estado `cola/estado/<id>.json` sigue siendo responsabilidad exclusiva de Grok.
- El webhook es opcional en la versión actual: si no están disponibles ambos secretos, queda el flujo de inbox del repositorio. Esto no equivale a recepción confirmada.

`scripts/procesar_cola.py` usa la fecha actual por defecto, pero permite sobrescribirla con `--fecha`; por tanto puede seleccionar históricos si alguien invoca explícitamente otra fecha. Busca también paquetes anidados y usa el prefijo del nombre/ruta, no una comparación obligatoria con `fecha_objetivo` dentro del JSON. No es correcto describirlo como un selector que **solo** puede procesar la fecha actual.

### Actions

No se encontraron ejecuciones nuevas de `capcot-grok-dispatch` después de la **run #147**, del 1-nov-2026. La última ejecución disponible pertenece a una versión anterior del workflow y falló en “Verificar configuración del receptor” con el error literal:

`Falta configurar GROK_WEBHOOK_URL.`

En ese job también aparece `GROK_WEBHOOK_TOKEN` vacío en el entorno; no se muestran valores. La versión actual ya no exige el webhook para escribir el marcador de inbox, pero no hay una ejecución posterior que pruebe ese camino. Las ejecuciones recientes de otros workflows/CodeQL no son evidencia de despacho Grok.

## 3. Lote obligatorio 5–7-nov

Los doce `project_id`, `fecha_objetivo`, `slot_local` y `slot_cesta` coinciden con `data/horario_semana_2026-11-01_07.json`. Se preserva la identidad canónica de `2026-11-07_inter-nubes-pesan`; la variante extra sigue siendo material distinto, no un segundo proyecto. El storyboard canónico de árboles sigue tratando redes micorrícicas comunes y Karst et al. (2023); no se marca desajuste temático.

### QA narrativo releído desde los JSON

Todos usan `review_basis=lectura_en_frio_solo_narracion`. Los 12 `reviewed_at` quedaron actualizados a `2026-11-16T15:45:46-06:00`; scores y checks no se cambiaron.

| project_id | score | status |
|---|---:|---|
| `2026-11-05_kids-dia-en-venus` | 88 | PASS |
| `2026-11-05_comida-palomitas` | 82 | FAIL |
| `2026-11-05_inter-arboles-se-comunican` | 78 | FAIL |
| `2026-11-05_inter-rayo-globular` | 81 | FAIL |
| `2026-11-06_kids-ballena-azul-corazon` | 80 | FAIL |
| `2026-11-06_comida-aguacate-negro` | 79 | FAIL |
| `2026-11-06_inter-ranas-congeladas` | 83 | FAIL |
| `2026-11-06_inter-arena-cantante` | 94 | PASS |
| `2026-11-07_kids-huesos-bebe` | 82 | FAIL |
| `2026-11-07_comida-hielo-caliente` | 81 | FAIL |
| `2026-11-07_inter-pulpo-suenos` | 72 | FAIL |
| `2026-11-07_inter-nubes-pesan` | 78 | FAIL |

Resultado: **2 PASS / 10 FAIL**. Los PASS tienen siete checks verdaderos y flags vacíos; los FAIL conservan los checks y flags exactos guardados en cada JSON.

### Estructura y fuentes

- 85 escenas en total; todos los ganchos tienen 3–5 palabras.
- Duración real con cortinilla: **84–88 s**.
- Todos cierran con el sello verbal del canal; los arcos declarados tienen gancho, cierre y reflexión.
- `narrative_contract` completo en los 12; `source_ids` resuelven; `prompt_base` coincide con el catálogo de estilos.
- 510 campos narrativos obligatorios ausentes (seis por escena: función dramática, puente causal, estado de pregunta, razón para continuar, información nueva y beat dramático).
- 75 arrays SFX están vacíos; la receta pide silencio explícito, no un array vacío. Ambiente sí está presente en las 85 escenas.
- Árboles: 169 palabras (por debajo del mínimo 170) y no contiene capa de mapa ni de dato/gráfico.
- Los otros once cumplen el rango de escenas y palabras; todos los paquetes tienen `approved_assets=[]`, `export.render_status=NOT_GENERATED` y no contienen rutas `asset_filename`/medios.
- Cuatro fuentes no incluyen campo DOI (`Venus`, `Aguacate`, `Huesos`, `Nubes`); allí se puede comprobar la URL declarada, no un DOI inexistente.
- El artículo de Pophale et al. citado en Pulpo estudia *Octopus laqueus*, no *Octopus insularis*. La fuente editorial lo especifica: [Nature, DOI 10.1038/s41586-023-06203-4](https://www.nature.com/articles/s41586-023-06203-4). Es una discrepancia de especie que impide aprobar ese paquete.

### Voz y estilo

`docs/VOCES_POR_TEMA.md` asigna `narradora_es` a biología y cocina, y `JorgeNeural` a ciencia/física/química/astronomía. Siete paquetes usan JorgeNeural aunque el tema requiere narradora_es: **Palomitas, Árboles, Ballena, Aguacate, Ranas, Huesos y Pulpo**. El validador actual usa una voz global JorgeNeural y no detecta esta regla por tema.

Los doce estilos existen en el catálogo y sus prompts base coinciden. Hay desajustes de afinidad temática que deben quedar visibles, no corregirse aquí: Venus/constructivista ruso (catálogo orientado a historia/industria), Palomitas/papel recortado popup (lenguaje/ideas abstractas), Rayo/pixel art (tecnología/videojuegos), Hielo/sátira de periódico (política/economía/noticias) y Pulpo/amigurumi (ritos/emociones/infancia/antropología). La afinidad no invalida por sí sola un QA narrativo, pero no está justificada en el catálogo.

### Handoff y producción preexistente

Los 12 estados `cola/estado/<project_id>.json` devuelven 404: **RECEPCION_GROK_NO_CONFIRMADA**. No hay copias de estos doce en `cola/entrada/`; permanecen en `proyectos/`. No se encontraron directorios `salidas/<project_id>/` para el lote, pero sí hay sidecars de plataforma en siete carpetas de proyecto. Todos esos siete se clasifican **PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR**:

| Proyecto | Evidencia de plataforma | Horario/privacidad/discrepancia |
|---|---|---|
| Venus | TikTok `7705488176793652481`; Facebook `2544385142727016`; sin YT ID en su sidecar | Sidecar marca TikTok 7-nov 17:00 y Facebook 17:58; no coincide con slot canónico 5-nov 07:00. |
| Palomitas | YouTube `zTP5akrGA9M`; TikTok `7705593452003691794`; Facebook `1167496802382795` | Publicados; reprogramado a 8-nov 07:00. |
| Ballena | YouTube `wbFrlM2e_YE`; TikTok `7705594333574991122`; Facebook programado | YT/TT públicos; Facebook sigue como programado en el sidecar; 11-nov 07:00. |
| Aguacate | YouTube `nSS_q2tj2P0`; TikTok `7705594217136966920`; Facebook programado | YT/TT públicos; Facebook sigue como programado; 10-nov 07:00. |
| Ranas | YouTube `UBFuKBU3cx0`; TikTok `7705596671807245586`; Facebook programado | YT/TT públicos; Facebook sigue como programado; 9-nov 07:00. |
| Arena | YouTube `m4RqQRaz55k` público; TikTok `7705502155427368212`; Facebook `2224920108452190`; otro YT `ztIkYcXB91U` sigue descrito como programado | Sidecar marca TikTok 7-nov 13:30 y Facebook 17:58; no coincide con slot canónico 6-nov 17:45. `ztIkYcXB91U` es riesgo de duplicado mientras siga programado. |
| Hielo caliente | YouTube `HSgrnejAcaI` privado/programado; TikTok `7706905447424347393` programado Everyone; Facebook `1460158683840154` programado Público/“En proceso” | 11-nov 13:30; no cancelar ni borrar. |

Los sidecars de estos siete proyectos referencian MP4 en rutas externas `/workspace` que no aparecen en el árbol GitHub: **MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO**. No se afirma que esos archivos existan en GitHub. No se borró ni canceló ninguna publicación. No se encontró un archivo independiente `historial_youtube`; el riesgo concreto de ID antiguo todavía programado aparece en el sidecar de Arena.

## 4. Datos, rotación y documentos contradictorios

### Frescura de `data/*.json`

- `data/endscreens_rotacion.json`: actualizado 16-nov 14:32; es el registro más reciente.
- `data/horarios.json`: política actualizada 9-nov; no contiene asignación diaria para 16-nov.
- `data/horario_semana_2026-11-01_07.json`: fuente canónica de los doce slots históricos.
- `data/horario_2026-11-08.json` a `data/horario_2026-11-11.json`: contienen reprogramaciones y estados posteriores de plataforma.
- `data/reprogramacion_tt_fb_v4_2026-11-01_03.json`: solo cubre 1–3 nov.
- `data/publicaciones.json`: llega hasta 1-nov.
- `data/rotacion.json` y `data/cola.json`: último corte 31-oct.
- `data/estilos_usados.json`, `data/temas_del_dia.json`, `data/vistas_historico.json` y `data/balances_6h.json`: corte 28-oct.
- `data/tendencias_estilos.json`: corte 31-oct.
- `data/cierre_diario/`: solo hay cierres de octubre; no existe cierre 16-nov.

El estilo actual `collage_cientifico_vintage` es válido para botánica y no se repite en los proyectos del 13–15 nov; el ledger de estilos está atrasado y registra un uso anterior el 28-oct. No se puede usar ese ledger como rotación completa de noviembre.

### Registro y selección

- `registro_editorial.py` lee proyectos, cola y salidas, pero no incorpora de forma completa `cola/bloqueados`, `handoffs/grok_inbox` ni sidecars sociales. Deriva fechas del ID del proyecto, no de `fecha_objetivo`; puede subcontar procesamiento y discrepancias de plataforma.
- `procesar_cola.py` filtra por prefijo de ruta; `--fecha` permite históricos manuales.
- El workflow escucha solo JSON de primer nivel; el procesador también admite paquetes anidados. Esta diferencia hace que un paquete pueda ser seleccionable por script y, a la vez, no despachable por Actions.

### Contradicciones vigentes

1. `README.md` describe como entregable de ChatGPT `cola/entrada/YYYY-MM-DD_slug.json`; `docs/FLUJO_EXTERNO.md` establece staging en `proyectos/` y promoción solo tras QA independiente.
2. `templates/storyboard.template.json` conserva un contrato antiguo 16:9/120 s y campos de assets; `templates/storyboard_vertical.template.json` es el contrato activo 9:16/75–90 s.
3. `docs/RECETA_CAPSULA.md` pide silencio explícito; la plantilla vertical usa arrays `sfx: []` como ejemplo y el validador no rechaza arrays vacíos.
4. `docs/VOCES_POR_TEMA.md` asigna voz por tema; `validar_storyboard.py` comprueba una voz global y no detecta los siete desajustes anteriores.
5. El validador no fuerza `export.render_status=NOT_GENERATED`, la presencia exacta de `approved_assets=[]`, fecha/slot internos ni el mapa de voz por tema. Esos puntos se revisaron manualmente.
6. La última ejecución antigua exigía webhook; el workflow actual permite inbox sin webhook. No hay run posterior que demuestre el comportamiento actual.

## 5. API, runtime y límites

- No se detectó un cambio oficial nuevo de API que justificara una revisión adicional; no se abrió una auditoría de APIs.
- No había runtime local del repositorio. **No se ejecutaron** `validar_storyboard.py`, `procesar_cola.py`, `registro_editorial.py` ni `--check-doi`. La validación estructural descrita aquí es estática.
- Se contrastó el DOI del proyecto del día en la página/PDF oficial de Nature; no se ejecutó el resolvedor Crossref.
- No se disparó workflow, no se enviaron payloads, no se generaron imágenes/frames/voz/audio/video/renders, no se publicó ni se consumieron créditos.

## 6. Cambios efectuados en este corte

- Se actualizó `narrative_qa.reviewed_at` en el storyboard del 16-nov y en los doce storyboards del lote a `2026-11-16T15:45:46-06:00`.
- Se releeron los trece JSON después de escribir. Los scores/statuses del cuadro coinciden con los valores persistidos.
- No se modificaron `data/*.json`, `cola/estado/`, workflows, secretos, permisos, `main` ni decisiones editoriales.
- No se promovió ningún proyecto a `cola/entrada/`.
- Las exclusiones absolutas del lote (slots 23:30 de dato del día, kids 3-nov 07:00 y Machu Picchu 4-nov 19:00) quedan fuera de la revisión y en sus rutas originales; no hay cambios netos en ellas.

## Conclusión operativa

El proyecto del 16-nov tiene una historia aprobada en frío y pasa la inspección estructural estática, pero sigue siendo propuesta: falta validación ejecutable/DOI resolver, selección editorial y recepción de Grok. Los doce proyectos del lote conservan 2 PASS narrativos y 10 FAIL; ninguno cumple el contrato estructural completo. Siete ya tienen procesamiento de plataforma y no deben redispatcharse. El lote permanece abierto.
