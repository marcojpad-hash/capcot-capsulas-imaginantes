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

