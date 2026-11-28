# Control de cola CAPCOT — 2026-11-28

**Corte:** 2026-11-28.  
**Rama auditada:** `feature/capcot-video-discovery-continuity`.  
**Alcance:** borradores recientes y backlog interdiario 27–30 nov, inventario de colas, programación en `main`, 12 IDs canónicos del lote 5–7 nov, workflow Grok y últimas Actions.

## Resultado ejecutivo

- Se completó una pasada narrativa independiente en frío para `2026-11-28_llantas-hielo-albedo`: **PASS 90/100**, siete checks true y flags vacías. El registro quedó en `storyboard.json`; no se modificó narración ni claims.
- Se corrigieron solo metadatos de fuente: el DOI del dataset Zenodo quedó consignado y la fuente primaria quedó explícitamente `PENDING_CROSSREF`.
- Ningún proyecto se promovió a `cola/entrada`. No hay entrada JSON plana, no hay recepción Grok confirmada y las compuertas estructural y DOI del borrador del día siguen sin verificación real.
- No se generaron medios, no se ejecutaron workflows, no se enviaron payloads, no se publicaron ni programaron videos y no se modificó `main` ni `data/*.json`.

## Proyectos recientes y backlog interdiario

| Proyecto | Fecha / slot | QA narrativo vigente | Estructura textual observada | Estado de handoff |
|---|---|---|---|---|
| `2026-11-27_dato-pav1-bacteriofago` | 27-nov / 07:00 | PASS 90 | 187 palabras, 8 escenas, 84 s | NOT_DISPATCHABLE: conflicto de slot con Microondas en main; DOI solo marcado VERIFICADO_URL |
| `2026-11-27_dato-registros-intermareales-1950s` | 27-nov / 23:30 | PASS 90 | 174 palabras, 8 escenas, 84 s | NOT_DISPATCHABLE: conflicto con Stubbs en main y procesamiento preexistente |
| `2026-11-28_llantas-hielo-albedo` | 28-nov / 23:30 | **PASS 90 nuevo** | 225 palabras, 7 escenas, 78 s + 6 s de cortinilla = 84 s | NOT_DISPATCHABLE: DOI Crossref y validador estructural real pendientes; recepción 404 |
| `2026-11-30_liquen-gen-cereales` | 30-nov / 17:00 | PASS 93 existente | 200 palabras, 8 escenas, 84 s | NOT_DISPATCHABLE: DOI PENDING_CROSSREF; lunes fuera de días preferentes |
| `2026-11-30_rapaces-clima-reino-unido` | 30-nov / 07:00 | FAIL 82 existente | 184 palabras, 8 escenas, 84 s | NOT_DISPATCHABLE: `GIRO_CIENTIFICO_NOMBRADO_PERO_NO_EXPLICADO`; DOI PENDING_CROSSREF; lunes fuera de días preferentes |

No se repitió QA en los proyectos con revisión vigente y narración sin cambios. Los estilos de estos cinco proyectos son distintos entre sí.

### Conflictos y producción preexistente en main

- **27-nov 07:00 — Microondas:** el plan semanal de main contiene un video ID `nd0rs6iVy8E` y `publishAt=2026-11-27T13:00:00Z`. Ocupa el mismo fecha+slot que PAV1. Clasificación para PAV1: `CONFLICTO_DE_SLOT_ENTRE_RAMAS` y `NOT_DISPATCHABLE`. El plan referencia un MP4 fuera del árbol GitHub: `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`.
- **27-nov 23:30 — Animal Stubbs:** `proyectos/2026-11-23_animal-stubbs/metadata.json` reserva ese hueco y referencia MP4/portada; `render.log` registra 86.13 s. Los medios no aparecen en el árbol del repositorio. Para el proyecto intermareal: `PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR`, `CONFLICTO_DE_SLOT_ENTRE_RAMAS` y `MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO`.
- **27-nov 17:00 — Bacterias:** existe programación en main, pero no colisiona con los slots 07:00 ni 23:30 auditados.
- **28-nov 17:00 — Mareo:** el plan semanal contiene video ID `fcSNbU809ao` y `publishAt=2026-11-28T23:00:00Z`. No colisiona con el slot fijo 23:30 de Llantas. El slot 28-nov 23:30 permanece libre en main.
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
- Inspección estática: 225 palabras, 7 escenas, 84 s totales, voz es-MX-JorgeNeural +7% pitch -2Hz, prompt_base del catálogo, bounds globales, capa de dato, fuentes por escena, ambiente/SFX por escena, approved_assets=[], render NOT_GENERATED y ausencia de rutas/asset_filename/asset_type.
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
