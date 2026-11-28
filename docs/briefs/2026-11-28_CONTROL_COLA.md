# Control de cola CAPCOT — 2026-11-28

**Corte:** 2026-11-28.  
**Rama auditada:** `feature/capcot-video-discovery-continuity`.  
**Alcance:** borradores recientes y backlog interdiario 27–30 nov, inventario de colas, programación en `main`, 12 IDs canónicos del lote 5–7 nov, workflow Grok y últimas Actions.

## Resultado ejecutivo

- Se completó una pasada narrativa independiente en frío para `2026-11-28_llantas-hielo-albedo`: **PASS 90/100**, siete checks true y flags vacías. El registro quedó en `storyboard.json`; no se modificó narración ni claims.
- El storyboard vigente registra SRC-001 `VERIFICADO_CROSSREF` y SRC-002 `VERIFICADO_RESOLVEDOR` (ver commits de verificación del propio storyboard). El validador estructural real y su ejecución `--check-doi` no se ejecutaron en este corte.
- Ningún proyecto se promovió a `cola/entrada`. No hay entrada JSON plana, no hay recepción Grok confirmada y las compuertas estructural y DOI del borrador del día siguen sin verificación real.
- No se generaron medios, no se ejecutaron workflows, no se enviaron payloads, no se publicaron ni programaron videos y no se modificó `main` ni `data/*.json`.

## Proyectos recientes y backlog interdiario

| Proyecto | Fecha / slot | QA narrativo vigente | Estructura textual observada | Estado de handoff |
|---|---|---|---|---|
| `2026-11-27_dato-pav1-bacteriofago` | 27-nov / 07:00 | PASS 90 | 187 palabras, 8 escenas, 84 s | NOT_DISPATCHABLE: conflicto de slot con Microondas en main; DOI solo marcado VERIFICADO_URL |
| `2026-11-27_dato-registros-intermareales-1950s` | 27-nov / 23:30 | PASS 90 | 174 palabras, 8 escenas, 84 s | NOT_DISPATCHABLE: conflicto con Stubbs en main y procesamiento preexistente |
| `2026-11-28_llantas-hielo-albedo` | 28-nov / 23:30 | **PASS 90 vigente** | 229 palabras, 7 escenas, 78 s + 6 s de cortinilla = 84 s | NOT_DISPATCHABLE: conflicto con `2026-11-23_animal-tama` en main; producción previa y medios no verificables; sin entrada plana; estado Grok 404; validador real no ejecutado |
| `2026-11-30_liquen-gen-cereales` | 30-nov / 17:00 | PASS 93 existente | 200 palabras, 8 escenas, 84 s | NOT_DISPATCHABLE: DOI PENDING_CROSSREF; lunes fuera de días preferentes |
| `2026-11-30_rapaces-clima-reino-unido` | 30-nov / 07:00 | FAIL 82 existente | 184 palabras, 8 escenas, 84 s | NOT_DISPATCHABLE: `GIRO_CIENTIFICO_NOMBRADO_PERO_NO_EXPLICADO`; DOI PENDING_CROSSREF; lunes fuera de días preferentes |

No se repitió QA en los proyectos con revisión vigente y narración sin cambios. Los estilos de estos cinco proyectos son distintos entre sí.

### Conflictos y producción preexistente en main

- **27-nov 07:00 — Microondas:** el plan semanal de main contiene un video ID `nd0rs6iVy8E` y `publishAt=2026-11-27T13:00:00Z`. Ocupa el mismo fecha+slot que PAV1. Clasificación para PAV1: `CONFLICTO_DE_SLOT_ENTRE_RAMAS` y `NOT_DISPATCHABLE`. El plan referencia un MP4 fuera del árbol GitHub: `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`.
- **27-nov 23:30 — Animal Stubbs:** `proyectos/2026-11-23_animal-stubbs/metadata.json` reserva ese hueco y referencia MP4/portada; `render.log` registra 86.13 s. Los medios no aparecen en el árbol del repositorio. Para el proyecto intermareal: `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`, `CONFLICTO_DE_SLOT_ENTRE_RAMAS` y `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`.
- **27-nov 17:00 — Bacterias:** existe programación en main, pero no colisiona con los slots 07:00 ni 23:30 auditados.
- **28-nov 17:00 — Mareo:** el plan semanal contiene video ID `fcSNbU809ao` y `publishAt=2026-11-28T23:00:00Z`. Además, la relectura de `main/proyectos/2026-11-23_animal-tama/metadata.json` encontró `hueco=2026-11-28 23:30`; el slot de Llantas **no está libre en main** y queda `CONFLICTO_DE_SLOT_ENTRE_RAMAS`.
- No se encontró paquete de main para 30-nov. Los slots 07:00 y 17:00 de ese lunes están dentro de ventanas activas, pero el lunes no figura entre los días preferentes de esas ventanas.

## Revalidación de los 12 IDs canónicos del lote 5–7 nov

Los 12 storyboards se volvieron a leer y sus últimos commits siguen fechados el 18-nov; no hay cambios narrativos posteriores, por lo que no se repitió su QA.

- QA vigente: **2 PASS / 10 FAIL**. PASS: `2026-11-05_kids-dia-en-venus` (88) y `2026-11-06_inter-arena-cantante` (94).
- Los 12 contienen 85 escenas en total. Se confirmaron **510 campos narrativos obligatorios ausentes** (seis por escena: `dramatic_beat`, `scene_function`, `causal_bridge_from_previous`, `question_state`, `reason_to_continue`, `new_information`) y **75 escenas sin SFX**.
- `slot_cesta` coincide con el calendario para los 12. Hay dos discrepancias reales de `slot_local`: `2026-11-05_inter-rayo-globular` y `2026-11-06_inter-arena-cantante` usan 17:45 mientras `data/horario_semana_2026-11-01_07.json` registra 19:00. El caso `2026-11-07_inter-nubes-pesan` conserva 17:45 por la instrucción explícita del addendum; el JSON de horario también muestra 19:00, discrepancia que no se corrigió porque `data/*.json` es solo lectura.
- Los 12 siguen en proyectos; no se creó ni promovió cola. Sus estados individuales Grok devuelven 404.

## Inventario de cola, publicación e historial

- `main:data/publicaciones.json`: 62 registros; último fecha observado 24-nov; ninguno para 27–30 nov.
- `main:data/rotacion.json`: 39 registros; último fecha 21-nov; ninguno para 27–30 nov.
- `main:data/cola.json`: vacío.
- `main:data/vistas_historico.json`: 110 registros; sin coincidencias para 27–30 nov.
- `historial_youtube/` y `publicaciones/` como directorios devuelven 404; no existe un archivo independiente `historial_youtube` verificable en el árbol.
- `feature/cola/entrada/`: solo `.gitkeep` y el directorio anidado de 9-nov para el robot orbital; **cero JSON planos de primer nivel**. El workflow Grok solo escucha `cola/entrada/*.json` y su selector manual usa profundidad máxima 1.
- `feature/cola/bloqueados/`: 47 entradas; no contiene ninguno de los cinco project_id recientes como copia plana. Hay variantes heredadas con nombres distintos; no se renombraron ni movieron.
- `feature/cola/estado/`: directorio ausente. Se consultaron los 5 proyectos recientes y los 12 IDs canónicos: los 17 paths individuales devuelven HTTP 404. Estado exacto: `RECEPCION_GROK_NO_CONFIRMADA`.
- `feature/handoffs/grok_inbox/`: un único marcador pendiente de 9-nov para el robot orbital; no constituye acuse Grok ni prueba recepción de los proyectos actuales.
- `feature/salidas/`: sin salida para los cinco proyectos recientes. No se detectó montaje, video ID, publishAt o publicación de esos cinco en la rama feature.

## Workflow y Actions

- `.github/workflows/capcot-grok-dispatch.yml` filtra JSON planos de primer nivel. No se disparó workflow ni se envió payload.
- En las últimas 100 Actions consultadas no aparece una ejecución reciente del dispatcher. La última evidencia anterior registraba `GROK_WEBHOOK_URL` ausente en la ejecución observada del 1-nov; el estado actual del secreto no se puede confirmar desde este run. No se leyó ningún valor de secreto.
- `Trabajador de cola`, run 46119729030 (28-nov 07:07Z), terminó SUCCESS; el log dice literalmente `[trabajador] sin trabajo en cola.`
- `CAPCOT — validar preproducción Kuroshio`, run 46078959750, terminó SUCCESS, pero valida exclusivamente el proyecto Kuroshio. Su comando no incluye `--check-doi` y no valida Llantas.
- CodeQL run 46115595793 terminó SUCCESS; CodeQL no sustituye validador estructural, DOI/Crossref ni QA narrativo.

## Radar, fuentes y errores de herramientas

- Se conservan cinco candidatos en el radar 28-nov; Llantas fue el único desarrollado para el slot 23:30. Google Trends HTML oficial (México, últimas 24 h) mostró 254 tendencias y «agujero de la capa de ozono» con 2K+ búsquedas; no se seleccionó porque la tendencia no aporta por sí sola una fuente científica primaria publicada dentro de la ventana de 48 h.
- El lector web no pudo renderizar RSS XML: ScienceDaily science/health/space devolvió HTTP 400 `Unsupported content-type: application/xml`; Phys.org HTTP 400 `text/xml`; NASA, Nature y UNAM Global HTTP 400 `application/rss+xml`; ESA HTTP 404; Google Trends RSS, EurekAlert y SINC devolvieron «URL ... is not accessible via this tool». Estos errores describen al lector web y no prueban por sí solos que urllib falle.
- No se ejecutó localmente `scripts/tendencias.py`: el intento de descargar el script desde raw GitHub terminó con `Could not resolve host: raw.githubusercontent.com`. Se utilizó el respaldo HTML oficial de Google Trends.
- El artículo primario de Nature Climate Change aparece indexado con DOI `10.1038/s41558-026-02800-z` y fecha 27-nov-2026. La apertura directa de Crossref API y doi.org devolvió «URL ... is not accessible via this tool»; por eso `SRC-001` queda `PENDING_CROSSREF`. El registro Zenodo 23299235 sí está accesible; el DOI `10.5281/zenodo.23299235` quedó agregado a `SRC-002` con estado `VERIFICADO_URL`.

## Estado final del borrador 28-nov

- Narrativa: PASS 90/100, siete checks true, flags vacías.
- Inspección estática recontada desde el JSON: 229 palabras, 7 escenas, 78 s de escenas + 6 s de cortinilla = 84 s, voz es-MX-JorgeNeural +7% pitch -2Hz, prompt_base del catálogo, mapa global con bounds y fuente, capa de dato, fuentes por escena, ambiente/SFX por escena, approved_assets=[], render NOT_GENERATED y ausencia de rutas/asset_filename/asset_type.
- **Validador estructural real: PENDIENTE.** No se pudo ejecutar localmente por el error DNS; la inspección estática no se declara como PASS del validador.
- **DOI/Crossref: PENDIENTE** para SRC-001.
- **Handoff: NOT_DISPATCHABLE** y `RECEPCION_GROK_NO_CONFIRMADA`.
- No se promovió a cola, no se creó/alteró estado Grok, no se generaron medios y no se publicó.

## Commits verificados en esta actualización

- QA narrativo independiente: `aff34611b30506f0d933348127aa4447f44f5858`.
- Corrección de metadatos DOI/estado de fuentes: `c21c7ce5e8c69d7546179a57b532df8b61383f33`.
- Actualización del radar: `650bf264052e2ad8111bed72689805b4ad41dfd2`.

## Revisión adicional de IDs históricos y copias bloqueadas — 28-nov

Se buscó cada uno de los 12 project_id canónicos en `data/publicaciones.json`, `data/vistas_historico.json` y `cola/bloqueados/`:

- Solo dos IDs tienen registro en `data/publicaciones.json`:
  - `2026-11-07_comida-hielo-caliente`: video ID `HSgrnejAcaI`, `publishAt` 11-nov 13:30 CDMX. La nota del registro dice que el Short ya no aparecía en el canal el 12-nov; TikTok y Facebook sí quedaron publicados. No hay programación futura registrada.
  - `2026-11-07_inter-nubes-pesan`: video ID `4Qpl17Ts_vI`, publicación 12-nov 07:00 CDMX; TikTok y Facebook también publicados. No hay programación futura registrada.
- Ambos se clasifican `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`. No se canceló ni alteró ninguna publicación.
- Ninguno de los 12 project_id aparece en `data/vistas_historico.json`; no existe el directorio independiente `historial_youtube/`. La comprobación histórica disponible procede de `data/publicaciones.json`.
- `cola/bloqueados/` conserva copias para `2026-11-05_inter-rayo-globular`, `2026-11-06_comida-aguacate-negro`, `2026-11-06_inter-ranas-congeladas`, `2026-11-06_inter-arena-cantante`, `2026-11-07_kids-huesos-bebe` y `2026-11-07_inter-nubes-pesan`, además de una variante `2026-11-05_comida-palomitas-explotan` (no es el project_id canónico). Las copias permanecen intactas; no se movieron ni renombraron.
- No hay entradas planas de esos IDs en `cola/entrada/`. Los dos IDs con publicación histórica no deben volver a procesarse; las demás copias heredadas permanecen bloqueadas.



## Reconciliación posterior — 2026-11-28 04:11 CDMX

- **DOI del proyecto de llantas:** SRC-001 queda `VERIFICADO_CROSSREF` (Crossref REST devolvió el DOI, título y fecha de publicación 27-nov-2026); SRC-002 queda `VERIFICADO_RESOLVEDOR` (el DOI resuelve al registro Zenodo 23299235). Se actualizaron los dos estados de fuente en `storyboard.json`; no se tocaron claims ni narración.
- **Estructura:** espejo estático de las reglas del validador: cero errores, 225 palabras, 7 escenas, 78 s + cortinilla de 6 s = 84 s, voz y prompt_base coincidentes, mapa con bounds globales válidos, dato/gráfico con fuente, 7 checks narrativos true, approved_assets vacío y render NOT_GENERATED. El script Python real no se ejecutó; el intento local de acceso a raw.githubusercontent.com falló con `Temporary failure in name resolution`. El espejo no autoriza handoff.
- **Main / slot:** la parrilla semanal de main conserva Mareo en 2026-11-28 17:00 CDMX (video ID `fcSNbU809ao`, `publishAt=2026-11-28T23:00:00Z`). No ocupa el slot fijo de dato 23:30. No aparece una publicación de main para 23:30; el slot sigue libre para este borrador.
- **Worker:** Actions run `46119729030`, job `140901360903`, terminó SUCCESS, pero el log dice literalmente `[trabajador] sin trabajo en cola.`. No acredita recepción Grok ni producción.
- **Handoff:** `cola/entrada` no contiene una entrada plana del proyecto y `cola/estado/2026-11-28_llantas-hielo-albedo.json` no existe (404): `RECEPCION_GROK_NO_CONFIRMADA`. El workflow de dispatch escucha únicamente `cola/entrada/*.json`; el buzón de repo escribe un marker `pending`, que no equivale a acuse de Grok. No se disparó workflow ni webhook.
- **Estado:** `NOT_DISPATCHABLE` por falta de validador estructural ejecutado y recepción Grok confirmada. No se promovió, no se generaron medios y no se publicó.


## Revalidación de backlog, slots y publicaciones — 2026-11-28 04:11 CDMX

- **12 IDs canónicos del lote 5–7 nov:** se releen los 12 storyboards actuales. Persisten exactamente 2 PASS (Venus 88 y arena 94) y 10 FAIL; no se repitió QA PASS ni se reescribió narración. Los 12 `cola/estado/<id>.json` devuelven HTTP 404: `RECEPCION_GROK_NO_CONFIRMADA` para cada uno.
- **Publicación histórica de esos 12:** `data/publicaciones.json` contiene dos registros: `2026-11-07_comida-hielo-caliente` (YT `HSgrnejAcaI`, 11-nov; el registro dice que ya no aparece en el canal, aunque TikTok/FB siguen publicados) y `2026-11-07_inter-nubes-pesan` (YT `4Qpl17Ts_vI`, 12-nov; publicado en las tres plataformas). Ninguno de los 12 aparece en `data/vistas_historico.json` (110 registros); no existe directorio independiente `historial_youtube/`. Las copias heredadas en `cola/bloqueados/` permanecen intactas.
- **27-nov:** PAV1 conserva PASS90, pero main tiene Microondas con `nd0rs6iVy8E` a las 07:00; Intermareales conserva PASS90, pero main tiene Stubbs a las 23:30 y hay procesamiento/medios preexistentes. Ambos siguen `NOT_DISPATCHABLE` por conflicto entre ramas; no se duplican ni cancelan.
- **28-nov:** llantas mantiene PASS90, DOI SRC-001 Crossref y SRC-002 resolvedor verificados; estructura estática sin errores, pero validador Python real pendiente. Main tiene Mareo `fcSNbU809ao` a las 17:00 y no ocupa 23:30. El proyecto de llantas sigue en `proyectos/`, sin estado Grok ni entrada plana.
- **29-nov:** main reserva 07:00 (`Jw_PpIT7JsI`), 13:30 (`2ugUwsX4k6g`), 17:00 (`jNMThVLPXvc`) y 19:00 (`gr3DmwXZLsY`) en `data/miniaturas_auditoria_2026-11-21.json`. Además `proyectos/2026-11-23_animal-billy/metadata.json` reserva 23:30 aunque `publishAt_utc=null`. No hay slot libre para un storyboard nuevo ese día; se marca `CONFLICTO_DE_SLOT_ENTRE_RAMAS` para cualquier propuesta de 29-nov en esos horarios.
- **30-nov:** lichen 17:00 conserva QA PASS93; su DOI `10.1038/s41586-026-11151-w` ya está `VERIFICADO_CROSSREF` (Crossref: publicado 25-nov). Rapaces 07:00 conserva FAIL82 por `GIRO_CIENTIFICO_NOMBRADO_PERO_NO_EXPLICADO`; su DOI `10.3389/fevo.2026.1922294` ya está `VERIFICADO_CROSSREF` (Crossref: publicado 26-nov). No se reescribió narración. Ambos slots son lunes, fuera de los días preferentes; no se promueven.
- Main reserva 30-nov 23:30 para Cher Ami (`publishAt_utc=2026-12-01T05:30:00Z`). No hay storyboard nuevo para ese slot; se conserva la reserva de main.
- No hay archivos `ESTADO_EJECUCION.md` en las carpetas de los cinco proyectos recientes; tampoco hay entradas planas actuales en `cola/entrada/`, ni salidas/publicaciones del proyecto de llantas. `publicaciones/` y `historial_youtube/` no existen como directorios independientes.
- Los 12 IDs y los cuatro proyectos recientes con storyboard mantienen `RECEPCION_GROK_NO_CONFIRMADA` por ausencia de sus estados individuales. No se creó ni editó ningún `cola/estado/`.


## Verificación DOI adicional de backlog — 2026-11-28 04:11 CDMX

- PAV1 `10.3389/fpls.2026.2008228`: Crossref REST devolvió `status=ok`, tipo `journal-article`, título coincidente, publisher Frontiers Media SA y registro creado/publicado el 26-nov-2026. Se actualizó únicamente `sources[0].verification_status=VERIFICADO_CROSSREF`; QA PASS90 y narración permanecen sin cambios. El conflicto de slot con main y el procesamiento previo siguen impidiendo promoción.
- Intermareales mantiene SRC-001 `VERIFICADO_CROSSREF` y SRC-002/SRC-004 `VERIFICADO_RESOLVEDOR`; no se modificaron.


## Corrección de fuente de programación y estado vigente — 2026-11-28 04:11 CDMX

Esta sección **supersede las líneas anteriores de este control** cuando difieran; conserva el historial de observaciones previas.

### Estado vigente de los cinco proyectos

- **PAV1 (27-nov 07:00):** DOI `10.3389/fpls.2026.2008228` verificado por Crossref; QA PASS90 sin cambios. Main mantiene dos registros para el mismo `publishAt=2026-11-27T13:00:00Z`: Microondas `nd0rs6iVy8E` en el plan semanal y `jiX6RdwJ1gg` en `data/miniaturas_auditoria_2026-11-21.json`. La duplicidad interna de main no libera el slot; PAV1 sigue `CONFLICTO_DE_SLOT_ENTRE_RAMAS` y `NOT_DISPATCHABLE`.
- **Intermareales (27-nov 23:30):** main reserva ese hueco con `2026-11-23_animal-stubbs`. Su metadata indica `hueco=2026-11-27 23:30`, hay `render.log` y `render_en.log`, pero los MP4 referenciados no aparecen en la carpeta del proyecto ni en `salidas/`: `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR` + `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`. Para Intermareales: `CONFLICTO_DE_SLOT_ENTRE_RAMAS` y `NOT_DISPATCHABLE`.
- **Llantas (28-nov 23:30):** PASS90; SRC-001 `VERIFICADO_CROSSREF`, SRC-002 `VERIFICADO_RESOLVEDOR`; 225 palabras, 7 escenas y 84 s totales en inspección estática. El validador Python real sigue sin ejecutarse; no promover.
- **Líquenes (30-nov 17:00):** PASS93 conservado; DOI `10.1038/s41586-026-11151-w` `VERIFICADO_CROSSREF` (publicación 25-nov). Lunes fuera de días preferentes; no promover.
- **Rapaces (30-nov 07:00):** FAIL82 conservado; DOI `10.3389/fevo.2026.1922294` `VERIFICADO_CROSSREF` (publicación 26-nov). No reescribir narración; lunes fuera de días preferentes; no promover.

### Main: horarios, reservas y producción preexistente

- **27-nov 17:00 — Bacterias:** la carpeta `main/cola/entrada/2026-11-27_bacterias-vuelta-oxigeno/` contiene literalmente `PLACEHOLDER` en `storyboard.json` y `fuentes.md`; no es JSON válido ni paquete dispatchable. No se cuenta como producción ni como reserva confirmada de slot.
- **28-nov:** Mareo `fcSNbU809ao` ocupa 17:00; el slot 23:30 de Llantas no tiene conflicto en main. La auditoría de miniaturas también registra Big Ben a 19:00; no colisiona con 23:30.
- **29-nov:** main tiene `Jw_PpIT7JsI` a 07:00, `m1FeS0mhfZ4` a 10:00 (archivo `data/rehechos_2026-11-22.json`), `2ugUwsX4k6g` a 13:30, `jNMThVLPXvc` a 17:00 y `gr3DmwXZLsY` a 19:00. Además, `2026-11-23_animal-billy` reserva 23:30 con render logs y MP4 referenciado fuera del árbol GitHub. No hay slot libre para un storyboard nuevo ese día.
- **30-nov 23:30:** Cher Ami está programado con `publishAt_utc=2026-12-01T05:30:00Z`; hay render logs y referencia a MP4, pero el archivo no aparece en el directorio del proyecto: `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR` + `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`. Los slots 07:00/17:00 de ese lunes no tienen reserva main observada, pero lunes no es día preferente.
- Los proyectos main Stubbs, Billy y Cher Ami tienen `render.log`/ `render_en.log` y referencias `mp4_es`/ `mp4_en`; no hay MP4 en sus carpetas GitHub. No inferir que el medio existe por el path de workspace.
- La auditoría de miniaturas de main contiene 36 registros con MP4 no presente en esa caja ni miniatura vertical: 32 `programado`, 3 `público` y 1 `privado sin publishAt`. No regenerar ni cancelar; clasificar los medios como `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`.

### Inventario heredado y selector

- `main/cola/entrada` tiene paquetes anidados; el subdirectorio `2026-11-27_bacterias-vuelta-oxigeno` es el placeholder anterior. `feature/cola/entrada` solo conserva el paquete anidado del 09-nov; no hay JSON plano actual en primer nivel.
- El paquete 09-nov `2026-11-09_dato-robot-ensambla-orbita` tiene producción real en `main/cola/entrada/<id>/` (MP4, portada y nueve frames); su YouTube ID `ZG4iQgmWrLI` tiene programación histórica para 21-nov 19:00, ya pasada. `metadata.json` conserva `privacyStatus=private` mientras `programacion.json` dice `programado`; el estado público no está verificado. En feature, la carpeta `frames/` solo tiene `.gitkeep`; el estado individual Grok sigue 404. Clasificación: `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`, `NOT_DISPATCHABLE_POR_SELECTOR`, y no inferir recepción.
- `feature/cola/bloqueados` tiene 47 entradas y 9 pares de copias JSON/directorio con nombres heredados; varias variantes no coinciden con los 12 IDs canónicos. No se movió ni borró nada.
- `main/data/publicaciones.json` conserva 62 registros (última fecha observada 24-nov); dos de los 12 IDs canónicos tienen publicación histórica. `data/vistas_historico.json` tiene 110 registros y ninguno de los 12 IDs. No existen directorios separados `publicaciones/` ni `historial_youtube/`.
- El worker de cola `46119729030` terminó SUCCESS, pero su log dice `[trabajador] sin trabajo en cola.`; no prueba recepción ni dispatch. El workflow Grok selecciona JSON planos de primer nivel; no se disparó workflow ni webhook.


## Corrección adicional: colisiones internas de main — 2026-11-28 04:11 CDMX

La comparación entre el plan semanal y `data/miniaturas_auditoria_2026-11-21.json` muestra tres discrepancias internas en main; no se debe tratar un único registro como calendario definitivo:

- **27-nov 07:00:** plan semanal registra Microondas `nd0rs6iVy8E`; la auditoría de miniaturas registra `jiX6RdwJ1gg` (“¿Los caballeros necesitaban una grúa?”) con `hora_cdmx=2026-11-27 07:00 CST`.
- **27-nov 17:00:** el plan semanal refiere Bacterias, pero `main/cola/entrada/2026-11-27_bacterias-vuelta-oxigeno/` contiene solo placeholders; la auditoría de miniaturas registra `_slEv21gbpM` (“¿Todos los artistas odiaban la Torre Eiffel?”) a 17:00.
- **28-nov 17:00:** plan semanal registra Mareo `fcSNbU809ao`; la auditoría de miniaturas registra `gN6svdqe62Q` (“El Cinco de Mayo NO es la Independencia”) a 17:00.

Los registros no se editaron. Las tres horas se consideran ocupadas/conflictivas para CAPCOT; la discrepancia interna de main debe resolverse por el operador del calendario, no por este investigador. La reserva de Llantas para 28-nov 23:30 sigue libre de conflicto en main.


## Conteo exacto de cola por rama — 2026-11-28 04:11 CDMX

- `main/cola/entrada/`: 36 entradas: un `.gitkeep` y 35 directorios anidados; **cero JSON planos** en el primer nivel.
- `feature/capcot-video-discovery-continuity/cola/entrada/`: 2 entradas: un `.gitkeep` y el directorio anidado del 09-nov; **cero JSON planos**.
- `main/cola/estado/2026-11-09_dato-robot-ensambla-orbita.json` y `main/cola/estado/2026-11-27_bacterias-vuelta-oxigeno.json` devuelven HTTP 404. No crear ni corregir estados.
- El selector del workflow escucha `cola/entrada/*.json` de primer nivel. Por tanto, los 35 paquetes anidados de main y el paquete anidado de feature no disparan el dispatch actual; el SUCCESS del worker con `sin trabajo en cola` es coherente con ese selector.


## CI y límites de automatización — 2026-11-28 04:11 CDMX

- PR #3 permanece OPEN/DRAFT, base main, head `512004c2e2a04094533d927baa17c6adaf29aad3`, `mergeable=false`. Los dos CodeQL runs del head anterior terminaron SUCCESS; el CodeQL del head actual `46135841079` seguía IN_PROGRESS al último chequeo.
- Esos checks son CodeQL, no el validador estructural de storyboards. `validar-kuroshio.yml` solo cubre el expediente Kuroshio del 18-nov y ejecuta `validar_storyboard.py` sin `--check-doi`; no valida el storyboard de llantas ni acredita DOI.
- `capcot-descubrimiento.yml` tiene `schedule: 30 14 * * 1`, `permissions.contents: write` y un paso que hace commit/push a `GITHUB_REF_NAME`. En una ejecución `schedule`, la rama de referencia predeterminada es main; por tanto, el workflow puede escribir el catálogo en main aunque la política operativa declare main de solo consulta. No se disparó ni modificó ese workflow.
- `capcot-grok-dispatch.yml` sigue limitado a JSON planos de primer nivel en push; no se ejecutó manualmente y no se envió webhook.


## Reconciliación de cola y programación — 2026-11-28 04:40 CDMX

### Slots de main revalidados con evidencia histórica
El snapshot `data/miniaturas_auditoria_2026-11-21.json` no es una consulta en vivo de YouTube; se registra como último estado histórico disponible. En ese snapshot, el 28-nov contiene además de los elementos ya recogidos en este control:
- 07:00 CDMX — `LSbmUp1J5VY`, `publishAt=2026-11-28T13:00:00Z`.
- 13:30 CDMX — `CcZ_jacsDXM`, `publishAt=2026-11-28T19:30:00Z` (fuera de la ventana activa actual, pero programado en el snapshot).
- 17:00 CDMX — `fcSNbU809ao` y `gN6svdqe62Q` aparecen en el mismo horario; se conserva el conflicto interno de main, sin cancelar ni duplicar.
- 19:00 CDMX — `U2p-lzkavbE`, `publishAt=2026-11-29T01:00:00Z`; pertenece a una ventana retirada y queda como riesgo de ID antiguo todavía programado en el último snapshot.
No se modificó ni canceló ningún video. La ausencia de una entrada en el snapshot no prueba que YouTube no tenga una programación posterior.

### Slot nuevo y borrador de 1-dic
- `data/horarios.json` en main mantiene la ventana 06:30–07:30 y martes como día preferente. El 1-dic-2026 es martes.
- La búsqueda de main, `proyectos/`, `cola/entrada/`, `cola/bloqueados/`, `salidas/`, `data/publicaciones.json`, `data/rotacion.json` y el snapshot de miniaturas no encontró una ocupación de GitHub para 1-dic 07:00. La única programación con fecha UTC 1-dic hallada es Cher Ami de 30-nov 23:30 (`publishAt=2026-12-01T05:30:00Z`), que no coincide con 07:00 CDMX.
- Se creó `proyectos/2026-12-01_elefantes-huerfanos-integracion-social/storyboard.json` como BORRADOR_EN_PROYECTOS_NO_APTO_PARA_PROMOCION: 8 escenas, 189 palabras, 78 s de escenas + 6 s de cortinilla = 84 s, gancho de 6 palabras, mapa con bounds publicados y capa de dato. DOI SRC-001/SRC-002 contrastados con Crossref REST. No se creó `narrative_qa`, `ESTADO_EJECUCION`, cola, estado Grok, medios ni programación. El snapshot de YouTube es histórico; no se afirma que el slot esté confirmado libre en vivo.
- Rotación: main conserva 39 registros y no contiene elefantes/Sera/Kenia; el catálogo de estilos usados contiene 32 registros y no incluye `amigurumi`. La rama feature mantiene snapshots más antiguos (27 rotación/21 estilos); no se modificó ningún `data/*.json`.

### Reconciliación de llantas/albedo
- El storyboard ya contiene `narrative_qa` PASS/90 y las dos fuentes muestran verificación DOI (SRC-001 Crossref; SRC-002 resolver). Se realizó una lectura en frío separada de la narración concatenada y se confirmó que el QA existente sigue sustentado; no se alteró la narración ni se repitió el objeto PASS.
- El validador estructural Python real no se ejecutó; el proyecto continúa sin promoción. Se corrigieron únicamente las notas de validación/riesgo que decían erróneamente que faltaba narrative_qa y que el DOI seguía pendiente.

### Workflows y Actions
- `.github/workflows/capcot-grok-dispatch.yml` existe en feature, no en main; no se disparó ni se envió payload. La cola continúa vacía y el estado Grok individual no se crea desde este rol.
- `.github/workflows/capcot-descubrimiento.yml` existe en feature y PR #3 sigue OPEN/DRAFT. Su run más reciente `46135943670` terminó SUCCESS solo en dos jobs CodeQL (Python y Actions); no ejecutó el validador de storyboard ni `--check-doi`.
- El workflow de descubrimiento contiene permisos `contents: write` y una ruta de push basada en `GITHUB_REF_NAME`. Si se integra, el evento schedule corre sobre la rama por defecto; eso podría escribir en main, que permanece SOLO_CONSULTA. No se fusionó ni se disparó el workflow. PR #3 conserva además modificaciones a `data/*.json`, contrarias a la regla de solo lectura; no debe integrarse hasta separar/restaurar esos cambios.
- El estado actual de secretos no es observable. El último reporte histórico registró `GROK_WEBHOOK_URL` ausente y no confirmó `GROK_WEBHOOK_TOKEN`; no se atribuye ese estado al presente.

### Clasificación
- Nuevo borrador 1-dic: NOT_DISPATCHABLE; permanece solo en `proyectos/`, sin QA independiente, validador estructural, JSON plano, receipt Grok ni promoción.
- Llantas/albedo: NOT_DISPATCHABLE; solo en `proyectos/`, sin entrada plana ni receipt Grok. `RECEPCION_GROK_NO_CONFIRMADA` permanece.


## Lectura de vuelta posterior a los commits — 2026-11-28 04:56 CDMX

- Storyboard `proyectos/2026-12-01_elefantes-huerfanos-integracion-social/storyboard.json` releído desde GitHub: 8 escenas, 189 palabras, 78 s + 6 s = 84 s, gancho de 6 palabras, voz es-MX-JorgeNeural +7%/-2Hz, mapa con bounds SRC-002, capa de dato SRC-001, `approved_assets=[]`, `render_status=NOT_GENERATED`, `publicacion=PENDIENTE_DECISION_GROK`, sin `narrative_qa` ni rutas de assets.
- Consulta individual de `cola/estado/2026-12-01_elefantes-huerfanos-integracion-social.json` devolvió literalmente `HTTP 404: Not Found`; estado registrado: `RECEPCION_GROK_NO_CONFIRMADA`. `cola/entrada` plano/anidado y `cola/bloqueados` también devolvieron 404; el árbol de la rama no contiene salida. Clasificación: NOT_DISPATCHABLE. No se creó ni editó ningún estado Grok.
- GitHub Actions automáticas de CodeQL asociadas a los cuatro commits del cambio terminaron SUCCESS: `46137479201`, `46137482402`, `46137484046`, `46137486217`. Cada ejecución solo muestra jobs `Analyze (python)` y `Analyze (actions)`; no ejecutó `scripts/validar_storyboard.py`, `--check-doi` ni QA narrativo.
- HEAD de feature después de la lectura de vuelta: `f84854b95b0fab6d7cf6f5b7646194bf801641cf`. El proyecto permanece exclusivamente en `proyectos/`; no hay promoción, webhook, render ni publicación.


## Auditoría posterior — 2026-11-28 06:03 CDMX

### 1-dic — QA y lectura estructural manual

- Se registró en el storyboard `narrative_qa=FAIL/0`, `review_basis=lectura_en_frio_solo_narracion`, los siete checks false y `critical_flags=["REVISION_INDEPENDIENTE_AUSENTE"]`. No se acreditó una revisión en conversación separada; el cero es fail-closed y no una valoración de calidad del guion. No se emitió PASS.
- Lectura de vuelta: 8 escenas, 189 palabras, 78 s + 6 s = 84 s, título de 6 palabras, voz `es-MX-JorgeNeural` +7%/-2Hz, resolución 1080x1920, arco completo, seis campos narrativos por escena presentes, cierre exacto, estilo coincidente con catálogo, mapa en escena 2 (bounds regionales publicados SRC-002) y capa de dato cualitativa en escena 5 (SRC-001). `approved_assets=[]`, `render_status=NOT_GENERATED`, publicación pendiente.
- El mapa usa [1.04, 37.75, 1.66, 37.92] como límites publicados del santuario; no son coordenadas GPS del estudio de 2026. El gráfico declara concentraciones comparables para fGCM y fT3, sin valores numéricos añadidos.
- `cola/estado/2026-12-01_elefantes-huerfanos-integracion-social.json` sigue 404 → `RECEPCION_GROK_NO_CONFIRMADA`; no hay entrada plana, salida ni promoción. `NOT_DISPATCHABLE`.
- El validador Python real no se ejecutó. `web.open` de GitHub Raw devolvió `DisabledError`; la descarga local devolvió `URLError: <urlopen error [Errno -3] Temporary failure in name resolution>`. La inspección manual del código y campos no se presenta como ejecución de `--structural-only` ni `--check-doi`.

### Backlog y lote canónico

- 27-nov PAV1 e intermareal: ambos siguen en `proyectos/`; sus estados Grok individuales devolvieron 404. Intermareal conserva conflicto de slot 23:30 con producción preexistente de main; no redispatchar.
- 28-nov llantas/albedo: PASS/90 y DOI verificados en el registro previo; no se repitió QA porque la narración no cambió. Sigue sin entrada plana ni acuse Grok.
- 30-nov liquen: PASS/93 existente, DOI/Crossref pendiente; no promover. 30-nov rapaces: FAIL/82 existente; no reescribir narración ni repetir QA.
- Lote canónico 5–7 nov: se releyeron los 12 storyboards y sus 12 estados. Los blobs narrativos/QA siguen fechados el 18-nov: 2 PASS (88, 94) y 10 FAIL; no se repitió QA. Los doce estados devolvieron 404 → `RECEPCION_GROK_NO_CONFIRMADA`.
- Dos IDs del lote tienen procesamiento histórico en `main:data/publicaciones.json`: nubes (`4Qpl17Ts_vI`, 12-nov 13:00Z) y hielo caliente (`HSgrnejAcaI`, 11-nov 19:30Z; la nota posterior indica que ya no aparece en el canal, mientras TikTok/Facebook constan publicados). Ambos: `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`.
- `historial_youtube/` y `publicaciones/` no existen en el árbol (404). `data/publicaciones.json` tiene 62 registros y llega hasta 24-nov; no hay conexión de YouTube Studio verificada. El snapshot histórico del 21-nov conserva IDs de slots del 28-nov, pero su vigencia externa no está confirmada.

### Actions y PR

- Worker `46119729030`: SUCCESS, salida literal `[trabajador] sin trabajo en cola.`; no fue dispatch Grok.
- CodeQL PR #3 `46137567879`: SUCCESS en `Analyze (python)` y `Analyze (actions)`; no ejecutó el validador ni Crossref.
- PR #3 sigue abierto, en borrador y con `mergeable_state=dirty`; no se integró. No se disparó `capcot-grok-dispatch.yml`.
- PR #15 de coordenadas booleanas sigue abierto. La rama activa ya contiene validación de booleanos y bounds; no se fusionó ni cerró el PR.
- Para el 28-nov no se creó otro storyboard: los registros históricos ocupan 07:00, 13:30, 17:00 y 19:00; 23:30 ya está asignado a llantas/albedo en esta rama.
- No se modificaron `data/*.json`, `main`, estados Grok, colas, salidas, secretos ni permisos. No se generaron medios, no se enviaron webhooks y no se consumieron créditos.


### Issues abiertas revisadas en este run

- **#11 — auditoría narrativa independiente de cuásares:** sigue OPEN. El storyboard fue corregido por ChatGPT y su QA previo fue FAIL/82; la auditoría solicitada debe realizarla otro modelo. No se emitió una segunda revisión de ChatGPT ni se marcó PASS.
- **#16 — handoff Imaginantes:** sigue OPEN. Solicita enlaces externos, reenvío de 17 MP4 y 10 resubidas a TikTok. No se generaron ni enviaron medios, no se publicaron/resubieron piezas y no se enviaron mensajes externos.
- Commits de este run, ambos leídos de vuelta: storyboard `b018aa1f0c7d72078ad36fb783b792d237a7747c`; control de cola `de910f0ad073c1b594a992b89fef15b5fca00032`.


### Reintento de fuentes — 2026-11-28 06:03 CDMX

- RSS ScienceDaily ciencia y Google Trends RSS México devolvieron `URLError(gaierror(-3, 'Temporary failure in name resolution'))`. No se interpreta como caída global de los servicios.
- Respaldo Exa en fuentes oficiales: Crossref REST y resolvedor DOI verificaron cuatro artículos de Nature/Nature Physics/Nature Cell Biology/Nature Astronomy/Nature Plants. Se añadieron al radar tres alternativas no seleccionadas (agregados bacterianos, VEXAS y materia oscura); el candidato de materia oscura supera 48 h y el de PM2.5/greening se marcó `NO_DUPLICAR` por solapamiento con la rotación.
- No se creó storyboard adicional: el slot 28-nov 23:30 ya está asignado a llantas/albedo y no se abrió otro slot. Radar actualizado y leído de vuelta en commit `06fc5b0ebcec0a4a035fd5fa2a2038e321af5605`.


### Precisión de producción preexistente — main / Bacterias 27-nov 17:00

- `main/proyectos/2026-11-27_bacterias-vuelta-oxigeno/programacion.json` confirma `publish_at=2026-11-27T23:00:00Z` (17:00 CDMX) y `estado=programado_sin_montar`. Por existir programación, clasificar `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`, aunque no se verificó un video_id ni un montaje terminado.
- El storyboard de main referencia `asset_filename` y `export.filename`; la carpeta `salidas/2026-11-27_bacterias-vuelta-oxigeno/` no existe y los medios no aparecen en el árbol: `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`.
- La copia anidada de `cola/entrada/` contiene `PLACEHOLDER` en `storyboard.json` y `fuentes.md`; no es un paquete JSON dispatchable. `cola/estado` devuelve 404.
- El snapshot de miniaturas registra además `_slEv21gbpM` a 17:00; se conserva como posible colisión interna del plan de main, sin cancelar ni redispatchar. No hay un proyecto de feature a las 17:00, por lo que no se declara `CONFLICTO_DE_SLOT_ENTRE_RAMAS` para Bacterias.


- Corrección final de encabezado del radar: se sustituyó el estado inicial obsoleto (“borrador sin DOI/QA”) por el estado verificado de llantas/albedo: 7 escenas, 229 palabras, 84 s, PASS/90 y DOI/resolvedor verificados; siguen pendientes el validador estructural real y el estado Grok. Lectura de vuelta en commit `33b44c7b5c084036a4cfc6bcea0fe7335afb032c`.


## Corrección de auditoría — 2026-11-28 08:03 CDMX (supersede las conclusiones previas sobre el slot 23:30)

- **Conflicto de slot confirmado en main:** `proyectos/2026-11-23_animal-tama/metadata.json` (blob `091b10c0e51cf19dcc0f69073cfdcdd2a495e4d3`) reserva explícitamente `2026-11-28 23:30 (America/Mexico_City)`; `guion.md` (blob `455e98fbe46a9ba03d468374a9e08ffe770d5da1`) repite el mismo hueco. Esto corrige y deja sin efecto las notas anteriores que decían que main estaba libre a las 23:30.
- **Producción preexistente en main:** `render.log` (blob `604813b1c4b623d47d2bc1bf8cb134d9779aa0ba`) registra `OK ... capsula.mp4 duración 85.11s`; `qa_es.json` (blob `ba1eab3d853e14d1aea0969693539f81c40e8051`) registra los checks audiovisuales en true. La metadata declara `mp4_es=/workspace/capcot_main/proyectos/2026-11-23_animal-tama/capsula.mp4` y duración 85.11 s, pero el árbol GitHub actual contiene logs/QA y **no** el MP4: `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`.
- **Clasificación para Llantas/albedo:** `CONFLICTO_DE_SLOT_ENTRE_RAMAS` + `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR` + `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO` + `NOT_DISPATCHABLE`. `publishAt_utc=null` en Tama: no se afirma que esté programado o publicado; el conflicto se funda en la reserva explícita del hueco y el render preexistente.
- **Lectura de vuelta del storyboard feature:** blob `aa85beae3b0c3517ceb742bafe9c6187728c98c1`; 229 palabras, 7 escenas, 78 s + 6 s = 84 s, título de 5 palabras, overlay inicial de 5 palabras, prompt_base literal del catálogo, mapa global y capa de dato con fuente, siete checks narrativos true, PASS/90, SRC-001 `VERIFICADO_CROSSREF`, SRC-002 `VERIFICADO_RESOLVEDOR`, `approved_assets=[]`, `render_status=NOT_GENERATED`, estado `BORRADOR_EN_PROYECTOS_NO_APTO_PARA_PROMOCION`. Es una inspección estática; no sustituye el validador Python.
- **Handoff:** `cola/entrada/2026-11-28_llantas-hielo-albedo.json` y `cola/estado/2026-11-28_llantas-hielo-albedo.json` devolvieron 404. No se creó entrada ni estado. El workflow acepta únicamente JSON plano en `cola/entrada/*.json`; no se disparó.
- **Feeds de este corte:** ScienceDaily y Phys.org rechazaron la lectura RSS por tipo XML (`400 Unsupported content-type`); NASA devolvió `400 Unsupported content-type: application/rss+xml`; Google Trends RSS México no fue accesible por este lector. Se usó búsqueda de respaldo; no se eligió candidato adicional ni se abrió otro storyboard.
- No se modificaron main, `data/*.json`, cola, estados Grok, workflow, secretos, permisos ni medios. No se publicó, programó ni redispatchó nada.


## Relectura de backlog y estados Grok — 2026-11-28 08:03 CDMX

### Lote canónico 5–7 nov (12 IDs)

Se releyeron los 12 storyboards actuales. No se recalculó narrative_qa ni se repitieron PASS; se conservaron los dictámenes ya registrados.

| project_id | Blob SHA | QA vigente | Palabras / escenas / s |
|---|---|---:|---:|
| 2026-11-05_comida-palomitas | `8c913dc8ad16b005735da9ebe882206d285c96bf` | FAIL 82 | 173 / 7 / 84 |
| 2026-11-05_inter-arboles-se-comunican | `05618f1d5d2cd8f713ee43ac802bcfb04bb9bb1d` | FAIL 78 | 170 / 8 / 84 |
| 2026-11-05_inter-rayo-globular | `5cd02d9a5d21ecdbd416a2858e433395cb9acc63` | FAIL 81 | 197 / 7 / 84 |
| 2026-11-05_kids-dia-en-venus | `3660c16f866d6ec74471e6ad88e640ea7df7df1d` | PASS 88 | 170 / 7 / 84 |
| 2026-11-06_comida-aguacate-negro | `d63b2afcbf22a579b7d5d8ced11265aca8b3dc2a` | FAIL 79 | 170 / 7 / 84 |
| 2026-11-06_inter-arena-cantante | `386ad015311e277782a09f82a72b7e1118b72e69` | PASS 94 | 206 / 7 / 84 |
| 2026-11-06_inter-ranas-congeladas | `84585c042be07fa1ea52f1c9de310e83a1105f16` | FAIL 83 | 177 / 7 / 84 |
| 2026-11-06_kids-ballena-azul-corazon | `37eda55883011c0f7a2ec022c43e880d33b58313` | FAIL 80 | 174 / 7 / 84 |
| 2026-11-07_comida-hielo-caliente | `fe8baf47a0e97f4c3607a187f6bac5524546e875` | FAIL 81 | 172 / 7 / 84 |
| 2026-11-07_inter-nubes-pesan | `190090e434d16acb4126e83d86fea17ad6e8f4e6` | FAIL 78 | 221 / 7 / 84 |
| 2026-11-07_inter-pulpo-suenos | `89080ebda22783403d5d8033d52c93dd00bc5fde` | FAIL 72 | 170 / 7 / 84 |
| 2026-11-07_kids-huesos-bebe | `981f384d44db08469ef8290b988b96fd26bc4cd0` | FAIL 82 | 172 / 7 / 84 |

Resultado: 2 PASS y 10 FAIL. Los 12 `cola/estado/<project_id>.json` devolvieron 404 → `RECEPCION_GROK_NO_CONFIRMADA`. Ninguno tiene entrada plana en `cola/entrada/`. Las copias bloqueadas siguen intactas; no se movió ni borró ninguna. `data/publicaciones.json` en main conserva dos registros históricos: hielo caliente (`HSgrnejAcaI`) y nubes (`4Qpl17Ts_vI`); ambos siguen protegidos contra redispatch.

### Proyectos recientes y próximos

| project_id | QA / estado | Hallazgo de handoff |
|---|---|---|
| 2026-11-27_dato-pav1-bacteriofago | PASS 90; 187 palabras; 8 escenas; 84 s | Grok 404; main tiene Microondas con videoId + publishAt a 07:00 y snapshot de colisión con otro ID → `CONFLICTO_DE_SLOT_ENTRE_RAMAS` + `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR` + `COLISION_HORARIA_NO_RESUELTA` |
| 2026-11-27_dato-registros-intermareales-1950s | PASS 90; 173 palabras; 8 escenas; 84 s | Grok 404; main reserva 23:30 para Stubbs y tiene render preexistente; MP4 no está en árbol → `CONFLICTO_DE_SLOT_ENTRE_RAMAS` + `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR` + `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO` |
| 2026-11-30_liquen-gen-cereales | PASS 93; 199 palabras; 8 escenas; 84 s | Grok 404; lunes fuera de días preferentes; no promover |
| 2026-11-30_rapaces-clima-reino-unido | FAIL 82; 182 palabras; 8 escenas; 84 s | Giro científico no explicado; Grok 404; no reescribir durante auditoría |
| 2026-12-01_elefantes-huerfanos-integracion-social | FAIL 0 por `REVISION_INDEPENDIENTE_AUSENTE`; 189 palabras; 8 escenas; 84 s | Grok 404; main no contiene reserva 1-dic 07:00 en el árbol consultado; no promover por ausencia de revisión independiente |

No se repitieron auditorías narrativas. Los 5 estados Grok anteriores devolvieron 404. No se creó cola ni se cambió el estado de ningún proyecto.


## Revisión de programación e IDs de YouTube — 2026-11-28 08:03 CDMX

- No existe archivo `historial_youtube` en el árbol actual de CAPCOT. La fuente disponible más reciente para IDs programados es `docs/briefs/produccion_2026-11-23_28/plan_semana.json` (blob `ed4467d1dc91a176de8da0c681ed3cf3467ae0bd`, generado 21-nov) y el snapshot `data/miniaturas_auditoria_2026-11-21.json` (blob `afc0a587025534eb5a338169383171bb0f38254c`).
- El plan registra seis IDs con `publishAt` y `publishAt_leido`: `tmOji99zGPE` (23-nov 07:00), `_YzBY4OfUeo` (24-nov 17:00), `W9g2tPZTpD4` (25-nov 07:00), `-1DRh_qj7Bg` (26-nov 17:00), `nd0rs6iVy8E` (27-nov 07:00) y `fcSNbU809ao` (28-nov 17:00). El snapshot del 21-nov los registra privados/programados. `data/publicaciones.json` solo contiene un registro de esos seis: `_YzBY4OfUeo`; los otros cinco no tienen confirmación en ese ledger.
- El snapshot de miniaturas registra seis colisiones de `publishAt`. La del 28-nov 17:00 CDMX enfrenta `gN6svdqe62Q` y `fcSNbU809ao`, ambos anotados como `programado`; la del 27-nov 07:00 enfrenta `jiX6RdwJ1gg` y `nd0rs6iVy8E`. Son hallazgos de un snapshot del 21-nov, no lectura actual de YouTube Studio: registrar `RIESGO_IDS_ANTIGUOS_AUN_PROGRAMADOS` y `COLISION_HORARIA_NO_RESUELTA`, sin afirmar que hoy siguen activos.
- El paquete de Microondas en main conserva `videoId=nd0rs6iVy8E` y `publishAt=2026-11-27T13:00:00Z`; por eso PAV1 no se redispatcha. Stubbs conserva `render.log` y `qa_es.json` con 86.13 s, pero su MP4 referido no aparece en el árbol; no se redispatcha.
- El ID `fcSNbU809ao` tiene reserva del 28-nov 17:00 en el plan, pero el snapshot registra otra cápsula a la misma hora. No se cambió horario, privacidad, miniatura, video ni publicación. Requiere comprobación del propietario en YouTube Studio para resolver la colisión y reconciliar los cinco IDs sin registro de publicación.


## Issue #11 — cuásares: revisión de independencia — 2026-11-28 08:03 CDMX

- Issue #11 sigue abierto aunque conserva la etiqueta `hecho`; su cuerpo exige auditor Groq/Gemini distinto de ChatGPT y lectura independiente.
- PR #12 está cerrado sin merge. PR #13 sigue abierto sin merge; ambos contienen `AUDITORIA.md` en sus ramas de trabajador, no en el árbol actual de feature.
- El informe de PR #13 fue generado por Groq `gpt-oss-120b`, pero revisa título, estructura, líneas y metadatos del storyboard. No acredita lectura ciega de la narración concatenada con título, resumen, arco, notas y `narrative_contract` ocultos.
- El storyboard actual (blob `91a366af5993f934722227026566ae2034880263`) conserva `narrative_qa=FAIL`, score 0, `review_basis=lectura_en_frio_solo_narracion`, flags `REVISION_INDEPENDIENTE_AUSENTE` y `REVISION_EN_FRIO_NO_ACREDITADA`. No se repitió PASS ni se alteró el guion.
- No se cerró el Issue, no se fusionó PR #13 ni se cambió la etiqueta. La única acción que puede levantar la compuerta es una revisión verdaderamente ciega por un modelo/revisor distinto, usando solo la narración concatenada.


## Relectura de cola, ramas y rotación — 2026-11-28 10:00 CDMX

### Precisión sobre las copias bloqueadas

La relectura de los 12 JSON planos de la raíz de `cola/bloqueados/` confirma que sus `project_id` no coinciden todos con los 12 IDs canónicos de la tabla del lote 5–7 nov. Coincidencia exacta: rayo globular, aguacate negro, arena cantante, ranas congeladas, nubes pesan y huesos de bebé (6/12). Los otros seis son IDs históricos distintos: palomitas-explotan, árboles-mito-respiran, venus-dia-largo, corazón-ballena-azul, mpemba-mito y sueños-pulpo. No se puede afirmar que esos seis sean copias de los seis storyboards canónicos con nombres distintos sin reconciliar contenido/hashes. Se conservan todos; no se movió, borró ni renombró nada.

### Cola y acuse

- En feature, `cola/entrada/` contiene `.gitkeep` y una única carpeta anidada, `2026-11-09_dato-robot-ensambla-orbita/`; no hay JSON plano de primer nivel.
- El workflow `.github/workflows/capcot-grok-dispatch.yml` (blob `47bbd228cfce5a1d402dc952e283e8d0f8e37030`) solo selecciona `cola/entrada/*.json` a profundidad 1. La carpeta anidada es `NOT_DISPATCHABLE_POR_SELECTOR`.
- El marcador `handoffs/grok_inbox/2026-11-09_dato-robot-ensambla-orbita.json` (blob `6d8923d662ca2ba3642a1ef03a2f1ea01e4b9b1e`) conserva `status=pending`; `handoffs/grok_done/` solo contiene `.gitkeep`. Es un marcador de handoff, no un acuse de Grok.
- `cola/estado/` no existe en feature; los cinco estados consultados individualmente (llantas/albedo, liquen, rapaces, PAV1 e intermareales) devolvieron 404 → `RECEPCION_GROK_NO_CONFIRMADA`.
- El workflow valida sintaxis JSON con `python -m json.tool`, crea un marcador pending y solo llama al webhook si existen ambas variables secretas. No ejecuta el validador estructural, DOI/Crossref, QA narrativo ni comprobación de conflictos. No se disparó; no se enviaron payloads. La visibilidad de secretos no está disponible en esta lectura, por lo que no se declara que falten.

### Diferencia de inventario entre feature y main

Los archivos `data/*.json` se mantuvieron en solo lectura. El snapshot de feature está atrasado respecto de main:
- `publicaciones.json`: feature 22 registros, último 31-oct (blob `a17dbe541d35b7e3d8a835756a06f0588039049a`); main 62 registros, último 24-nov (blob `a822459849571a443196e6a5b5d4ee73d109b1cd`).
- `rotacion.json`: feature 27 registros, último 31-oct (blob `01677e27569826e49736501a0c22c166f8015a45`); main 39 registros, último 21-nov (blob `1cb16c1cfad8b968e24221793047df27d83eb5e0`).
- `estilos_usados.json`: feature 21 registros, último 28-oct; main 32 registros, último 9-nov (blob main `d5532a357e6b2c3b13e3a0b57701ce74513d900b`).
- `horarios.json` difiere por blob entre ramas (feature `550599906c26e747de71b6b962080b6bd469f23f`; main `2261993d542de445df23e0abbe63bca9b54c2ff1`); ambos declaran corte 9-nov. La programación semanal de main, de 21-nov, se consultó en solo lectura para detectar colisiones. No se sincronizó ni modificó ningún `data/*.json`.

### Producción preexistente confirmada

- Para 27-nov 17:00, `main/proyectos/2026-11-27_bacterias-vuelta-oxigeno/programacion.json` (blob `e2947181dccbb247d68630d1bdce3a04d51485df`; `estado=programado_sin_montar`, `publish_at=2026-11-27T23:00:00Z`). El paquete anidado de main contiene `PLACEHOLDER` tanto en `storyboard.json` como en `fuentes.md`; `salidas/2026-11-27_bacterias-vuelta-oxigeno/` y `cola/estado/` devuelven 404. El snapshot de miniaturas del 21-nov también registra `_slEv21gbpM` a las 17:00. Se conserva `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`; no se atribuye conflicto entre ramas porque no hay storyboard feature para ese slot.
- Para 28-nov 17:00, el plan semanal de main registra `fcSNbU809ao` (Mareo) y el snapshot del 21-nov registra además `gN6svdqe62Q` en el mismo `publishAt`. Es una colisión histórica no resuelta; no se afirma que ambos sigan activos hoy sin YouTube Studio.
- Para 28-nov 23:30, Tama reserva el mismo hueco en main y tiene `render.log` con 85.11 s; `publishAt_utc=null` y el MP4 no está en el árbol. Se mantiene para Llantas/albedo `CONFLICTO_DE_SLOT_ENTRE_RAMAS`, `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`, `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO` y `NOT_DISPATCHABLE`.
- Llantas/albedo: lectura estática actual conserva 229 palabras, 7 escenas, 84 s, QA registrado PASS/90, siete checks true, fuentes con estados Crossref/resolvedor, `approved_assets=[]` y `render_status=NOT_GENERATED`. Esta relectura no volvió a ejecutar el validador Python ni re-certificó la independencia del reviewer; no se promovió.
- Liquen (30-nov 17:00) conserva PASS/93; Rapaces (30-nov 07:00), FAIL/82 por giro científico no explicado. Ambos caen en lunes, fuera de los días preferentes de la ventana actual; no se promovieron ni reescribieron.

No se modificaron main, `data/*.json`, estados Grok, bloqueados, workflow, medios, secretos ni permisos. No hubo redispatch, publicación ni programación.


## Revisión estática de PR #15 — 2026-11-28 10:00 CDMX

- PR #15 sigue OPEN, 12 commits, 2 archivos, HEAD `947df50e1ee895e7744e54cc43f3865c78eedf13`; no se ejecutaron sus pruebas y no se fusionó.
- El diff rechaza booleanos en coordenadas terrestres/celestes y bounds, y fija la consulta a `https://api.crossref.org` mediante HTTPS con verificación TLS.
- Hallazgo de revisión: `check_doi()` devuelve PASS únicamente por `HTTP 200`; no parsea el JSON de Crossref ni compara `message.DOI` con el DOI solicitado. La prueba añadida simula solo `status=200`. Para que `--check-doi` pruebe el registro correcto, falta validar el cuerpo JSON y la coincidencia del DOI devuelto, además de probar respuesta 200 sin registro o con DOI distinto. Este hallazgo es estático; no se atribuye una prueba ejecutada.
- PR #3 sigue DRAFT contra main, 728 archivos cambiados y su propio cuerpo reconoce cambios a `data/*.json` incompatibles con el contrato. No se fusionó.


## Trazabilidad de esta ejecución — 2026-11-28

Commits creados en la rama de trabajo y leídos de vuelta:
- `0fa99d80daa5aae84308bbe9a0dea8aa4ebed038` — precisión de cola, bloqueados y diferencia entre ramas.
- `dcf42c6f3643f3d713d6b4b95849147c2f5d8b51` — errores exactos de RSS y respaldo HTML de Trends.
- `0a510bfc66c8173321b6ad27c6897481a7f4f97d` — corrección de la referencia al blob de programación de Bacterias.
- `ca66e3238246a075c55764e1adb9206720838fcc` — revisión estática del control Crossref en PR #15.

HEAD previo a este registro: `ca66e3238246a075c55764e1adb9206720838fcc`; commit de este registro: `84f97ab13561cf8f77aa55da0a54ed379d142aa1`. No se modificó `main`, `data/*.json`, cola operativa, estados Grok ni medios.
