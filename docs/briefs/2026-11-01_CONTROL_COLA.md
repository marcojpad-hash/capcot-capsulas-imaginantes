# CONTROL DE COLA CAPCOT — 2026-11-01

**Corte:** 2026-11-01, 14:20 CDMX  
**Repositorio:** `marcojpad-hash/capcot-capsulas-imaginantes`  
**Rama:** `feature/capcot-video-discovery-continuity`  
**Tipo de revisión:** auditoría estática de GitHub; no se ejecutó el runtime local.

## Dictamen

**HANDOFF NO CONFIABLE.** Hay cinco piezas audiovisuales asignadas a slots del 1-nov y una sexta entrada de dato del día pendiente. Ninguna tiene acuse machine-readable en `cola/estado/`. Los paquetes de cola están en carpetas anidadas que el workflow de dispatch no detecta. Las últimas diez ejecuciones de Actions aparecen fallidas; las ocho ejecuciones cuyo job se inspeccionó fallaron en el mismo paso de configuración y omitieron el envío.

Los artefactos de salida de pulpo y cebolla contienen QA de 19/21, con fallo de mapa y dato/gráfico, pero también contienen registros de carga/programación. Baffin tiene 20/21 y duración renderizada de 91.93 s, fuera del límite de 90 s. Xolo y tiburón no tienen `qa.json`. No se puede atribuir recepción ni QA aprobado a Grok sin el estado correspondiente.

## 1. Briefs y paquetes del 1-nov

No existe `docs/briefs/2026-11-01_RADAR_CAPCOT.md` (404). En `docs/briefs/` están 30-oct, 31-oct y los radares 5–7 nov. Sí existe un brief de trabajo para el slot de 23:30 en `ajustes_entre_modelos/PARA_CHATGPT_dato_del_dia.md`; no es un storyboard ni un paquete de cola. El documento propone el cambio de horario y el estudio Sandhu et al. (2014), y pide comprobar con fuente oficial la excepción mexicana de municipios fronterizos antes de afirmarla.

### Entradas asignadas a slots del 1-nov

| Slot CDMX | project_id | Ubicación/evidencia | Estado de auditoría |
|---|---|---|---|
| 03:00 | `2026-11-01_dato-xolo-mictlan` | Solo en `salidas/`; no hay entrada en cola ni carpeta de proyecto | NOT_DISPATCHABLE; sin QA ni estado Grok |
| 07:00 | `2026-11-01_pulpo-tres-corazones` | `cola/entrada/<id>/storyboard.json`, `proyectos/`, `salidas/` | NOT_DISPATCHABLE; QA 19/21 |
| 13:30 | `2026-11-01_llorar-cebolla-quimica` | `cola/entrada/<id>/storyboard.json`, `proyectos/`, `salidas/` | NOT_DISPATCHABLE; QA 19/21 |
| 17:00 | `2026-10-26_baffin-bay-ice-shelf` | Entrada anidada y salida; ID conserva fecha original aunque el slot es 1-nov | NOT_DISPATCHABLE; QA 20/21 |
| 19:00 | `2026-11-03_kids-tiburon-groenlandia` | Entrada anidada, proyecto/salida; ID conserva fecha original aunque el slot es 1-nov | NOT_DISPATCHABLE; no existe `qa.json` |
| 23:30 | `2026-11-01_dato-TBD-news` | Slot pendiente; brief de trabajo en `ajustes_entre_modelos/PARA_CHATGPT_dato_del_dia.md` | SIN PAQUETE; aún dentro del plazo de hoy |

### Validación por paquete

**Xolo — 03:00**
- 7 escenas, 214 palabras, 77 s de escenas + 12 s de cortinilla = 89 s; estilo `teatro_sombras`, presente en el catálogo.
- Sin capas de mapa ni dato/gráfico. Tiene rutas `asset_filename` en las escenas, pero no hay evidencia de esos frames en el paquete. `approved_assets=[]`, `render_status=NOT_GENERATED`.
- No existe `qa.json` ni `cola/estado/2026-11-01_dato-xolo-mictlan.json`.
- `publicacion.json` registra YouTube `uploaded/private` con `publishAt=2026-11-01T09:00:00Z`, y TikTok/Facebook como programados. Es registro de carga/programación, no comprobación en vivo de visibilidad pública.
- Lectura en frío independiente: 85/100, narrativa PASS; el arco mito → arqueología → genética se puede reconstruir y el cierre vuelve a la ofrenda. El storyboard no guarda `narrative_qa`; el paquete falla el contrato estructural por ausencia de mapa/dato y QA.

**Pulpo — 07:00**
- 8 escenas, 228 palabras; 78 s de escenas + 12 s de cortinilla = 90 s, aunque `target_duration_seconds=84`. `ESTADO_EJECUCION.md` dice 78 + 6 = 84 s: contradicción entre JSON y estado.
- Sin mapa ni dato/gráfico. Las ocho escenas llevan `sfx=[]`; ambiente `oceano`. Ocho `asset_filename` apuntan a `frames/scene_00N.jpg`, pero no son assets aprobados ni generados.
- QA de salida: **19/21**. Fallan literalmente `capa_mapa: sin capas` y `capa_grafico_o_dato: sin capas`. La misma QA registra 61.80 s de render y 125 palabras de voz, frente a 228 palabras del storyboard. El chequeo de duración usado por esa QA permite 60–120 s, no el contrato editorial de 75–90 s.
- `publicacion.json` registra YouTube `uploaded/private` con publicación programada para 13:00Z; TikTok/Facebook aparecen programados. `ESTADO_EJECUCION.md` aún dice pendiente de revisión Grok y que no hubo publicación/programación. No se puede resolver esa contradicción sin estado de Grok y comprobación de plataforma.
- Lectura en frío: **72/100, FAIL**. La pregunta se entiende y el mecanismo avanza, pero la apertura hipotética («Si pudieras…») no es in medias res. Flags: la comparación de branquias con pulmones que «sacan aire del agua» es imprecisa; «si uno falla, los otros no lo reemplazan» no está respaldado por las fuentes enumeradas. No existe `narrative_qa` en el JSON.

**Cebolla — 13:30**
- 8 escenas, 231 palabras; 78 s de escenas + 12 s de cortinilla = 90 s, aunque el objetivo es 84 s. El estado de ejecución declara cortinilla de 6 s y total 84 s.
- Sin mapa ni dato/gráfico. Las ocho escenas tienen `sfx=[]` y ambiente `silencio`. Ocho `asset_filename` son rutas de frames no aprobados/generados.
- QA de salida: **19/21**; fallan mapa y dato/gráfico. Registra 66.70 s de render y 127 palabras de voz frente a 231 palabras en el storyboard. El umbral mecánico de esa QA (60–120 s) no corresponde al contrato 75–90 s.
- `publicacion.json` registra YouTube `uploaded/private` con `publishAt=2026-11-01T19:30:00Z`; TikTok/Facebook figuran programados. El estado de entrada dice pendiente de revisión Grok y no realizada la programación. No hay estado Grok que resuelva la discrepancia.
- Lectura en frío: **84/100, FAIL** por flag crítico: el cierre afirma que la cebolla «inventó» la alarma química para que nadie se la coma. La fuente primaria demuestra la síntesis enzimática del factor lacrimógeno, no esa intención evolutiva. El resto de la progresión causal y el retorno a las lágrimas se entiende. No existe `narrative_qa` en el JSON.

**Baffin — slot 17:00**
- ID de proyecto 26-oct, slot asignado 1-nov. 9 escenas, 215 palabras, 81 + 6 = 87 s; estilo `art_deco_poster`. Mapa y datos presentes; las escenas tienen rutas de assets que no deben confundirse con medios aprobados.
- QA de salida: **20/21**. Falla `subs_max_3_palabras` con 83 bloques. Duración renderizada: **91.93 s**, excede 90 s. `publicacion.json` registra YouTube `uploaded/private` para 23:00Z y TikTok/Facebook programados.
- Lectura en frío: **78/100, FAIL**. La cadena evidencia → reconstrucción → función de soporte → colapso es legible, pero la apertura «Imagina una tapa…» es descriptiva, no una anomalía/acción ya en curso. Flag factual: «Tapaba la bahía de Baffin completa» excede lo que el paper reporta explícitamente (plataforma de 150,000 km²; espesor estimado 1,400–2,100 m). El artículo primario habla de una plataforma que abarcaba la cuenca; no autoriza a convertirlo sin matiz en cobertura literal de toda la bahía.

**Tiburón de Groenlandia — slot 19:00**
- ID de proyecto 3-nov, reasignado al 1-nov 19:00. 8 escenas, **244 palabras** (9 sobre el máximo), 78 + 6 = 84 s; mapa y dato presentes; estilo `crayones_infantiles`. Hay ocho rutas `asset_filename`.
- No existe `qa.json`. `ESTADO_EJECUCION.md` aún lo describe como paquete del 3-nov 07:00, 211 palabras, preparado y sin medios; `publicacion.json` registra YouTube `uploaded/private` con `publishAt=2026-11-02T01:00:00Z`, mientras TikTok/Facebook aparecen `pendiente_ui`. El horario semanal, en cambio, los marca programados en las tres plataformas.
- Lectura en frío: **89/100, narrativa PASS**. La pregunta sobre cómo estimar la edad se sostiene; el método del cristalino, radiocarbono, estimaciones y margen de error forman una progresión; el final paga la apertura. El paquete global sigue FAIL: 244 palabras, no hay `narrative_qa` ni QA de producción, y el estado conserva el slot anterior.

## 2. Recepción y dispatch

- `cola/estado/` devuelve 404: no existe directorio de estados. Para cada storyboard del 1-nov: **RECEPCION_GROK_NO_CONFIRMADA**. No se creó ni modificó ningún estado.
- El workflow `.github/workflows/capcot-grok-dispatch.yml` escucha `cola/entrada/*.json`; en push usa grep `^cola/entrada/[^/]+\.json$`. En `workflow_dispatch`, `all` ejecuta `find cola/entrada -maxdepth 1 -type f -name '*.json'`, y un ID concreto intenta `cola/entrada/<id>.json`. Por tanto ignora las carpetas anidadas con `storyboard.json`. Los paquetes reutilizados/anidados de Baffin y tiburón tampoco son dispatchables por ese workflow; Xolo ni siquiera está en la cola.
- Las diez ejecuciones más recientes listadas (runs 138–147) terminaron en failure. En las ocho inspeccionadas, el único paso fallido fue `Verificar configuración del receptor`; `Entregar paquetes y exigir acuse individual` quedó skipped. Los logs muestran literalmente: `Falta configurar GROK_WEBHOOK_URL.` En el entorno del job aparecen vacíos `WEBHOOK_URL` y `WEBHOOK_TOKEN`; la comprobación del URL falla antes de llegar a la comprobación del token. No hubo POST ni acuse.
- No se atribuye recepción, selección, QA aprobado ni publicación pública a Grok por la mera existencia de `salidas/` o de un ID de video.

## 3. Procesador, rotación y contradicciones

- `scripts/procesar_cola.py` recoge `cola/entrada/*.json` y `cola/entrada/*/storyboard.json`; toma los primeros diez caracteres del nombre del archivo/carpeta y filtra por `--fecha`, cuyo default es la fecha CDMX. No procesa automáticamente otras fechas. Para 1-nov detecta las carpetas anidadas de pulpo y cebolla; no selecciona Baffin (prefijo 26-oct) ni tiburón (prefijo 3-nov), aunque estén asignados al 1-nov en el horario. El filtro por fecha de paquete funciona, pero no equivale a fecha objetivo del slot.
- `scripts/rotacion.py` fija `MAX_POR_DIA=5`. `data/horario_semana_2026-11-01_07.json` declara `slots_por_dia=5` y `total=35`, pero contiene **36 registros** y seis slots para el 1-nov: 03:00, 07:00, 13:30, 17:00, 19:00 y 23:30. El slot 03:00 es el extra respecto a las cinco ventanas declaradas; no aparece una excepción de cupo en el registro consultado.
- `data/temas_del_dia.json` solo llega a 28-oct; `data/rotacion.json` tiene 27 registros, con fechas 24–28 y 31-oct, ninguno del 1-nov; `data/publicaciones.json` tiene 22 registros y llega a 31-oct. Los tres registros operativos están desactualizados para el día auditado.
- `scripts/registro_editorial.py` fusiona rotación, publicaciones, `data/cola.json` y storyboards de cola/proyectos/salidas, pero no lee `data/horario_semana_2026-11-01_07.json`. Deriva la fecha del `project_id`: Baffin queda como 26-oct y tiburón como 3-nov aunque ambos ocupen slots del 1-nov. Esto subcuenta la rotación del día y puede permitir colisiones/cupo incorrecto.
- En el horario, `project_id_plan` no coincide con `project_id` para pulpo (`2026-11-01_kids-pulpo-tres-corazones`) ni cebolla (`2026-11-01_comida-cebolla-llorar`).
- Contradicción adicional: `PARA_CHATGPT_faltantes_ahora.md` y `PARA_CHATGPT_tema_feynman_brasil.md` indican luz verde para Feynman en Brasil en el hueco kids del 3-nov 07:00; el horario semanal conserva `2026-11-03_kids-TBD` y notas de reemplazo pendientes. Requiere reconciliar el horario antes de tratar Feynman como asignado.
- Rotación visual observada: los cinco paquetes existentes usan estilos distintos y presentes en el catálogo: `teatro_sombras`, `carton_recortado`, `papel_recortado_popup`, `art_deco_poster`, `crayones_infantiles`. No se detectó repetición de estilo entre esos cinco.

## 4. QA de narrativa y estructura

Ninguno de los cinco storyboards contiene `narrative_contract` ni `narrative_qa`; por tanto, ninguno pasa la compuerta machine-readable. La lectura en frío de este auditor produjo: Xolo 85 PASS; pulpo 72 FAIL; cebolla 84 FAIL; Baffin 78 FAIL; tiburón 89 PASS. Los PASS narrativos de Xolo y tiburón no significan que el paquete completo pase: siguen fallando requisitos estructurales/administrativos descritos arriba.

El validador `scripts/validar_storyboard.py` es estructural: comprueba etiquetas de arco, conteo, duración, fuentes, mapa/dato, estilo y assets, pero no transiciones ni progresión. Los paquetes de pulpo, cebolla y Xolo no tienen mapa/dato. Los cinco storyboards inspeccionados incluyen `asset_filename` aunque están en modo textual con `approved_assets=[]` y `render_status=NOT_GENERATED`; esos nombres son placeholders, no medios. No se ejecutó el validador porque no hay checkout/runtime local disponible en esta auditoría; se hizo comprobación estática de los JSON, scripts y QA guardadas.

## 5. Fuentes y DOI

Los DOI principales se contrastaron con registros de editor/indexadores:
- Cebolla: Imai et al. (2002), Nature, 10.1038/419685a — confirmado. La fuente demuestra síntesis específica por LFS; no demuestra por sí sola la intención evolutiva atribuida en el cierre.
- Pulpo: Wells (1980), J. Exp. Biol., 10.1242/jeb.85.1.111 — confirmado.
- Xolo: Drögemüller et al. (2008), Science, 10.1126/science.1162525 — confirmado.
- Baffin: artículo primario Nature Geoscience, 10.1038/s41561-026-02126-7 — confirmado; publicado 21-oct-2026. La segunda fuente, 10.1038/s41561-026-02127-6, es un Research Briefing de Nature publicado 26-oct, no el artículo primario.
- Tiburón: Nielsen et al. (2016), Science, 10.1126/science.aaf1703 — confirmado.

No se revisaron changelogs de APIs en esta pasada: no apareció un cambio oficial nuevo como parte de los bloqueos auditados.

## 6. Cambios ejecutados en esta auditoría

- Se creó este informe de control en la rama de trabajo.
- No se modificaron `data/*.json`, storyboards, estados de Grok, workflows, secretos, permisos, `main` ni Motor U6.
- No se generaron cápsulas ni medios, no se publicó, no se programó y no se consumieron créditos.
- La recepción por Grok sigue **NO CONFIRMADA** mientras falten los estados individuales y el dispatch no complete un POST con acuse verificable.


## 7. Acción posterior a la auditoría — cuarentena de la cola

**Corte:** 2026-11-01, 14:29 CDMX. Esta sección registra una operación posterior al corte estático de la auditoría; no altera sus hallazgos originales.

La inspección de los 38 storyboard JSON que permanecían en `cola/entrada/` encontró que ninguno contenía `narrative_contract` ni `narrative_qa`. Por tanto, ninguno acreditaba PASS machine-readable. Se retiraron de la cola y se conservaron en `cola/bloqueados/`:

- Commit [057474c](https://github.com/marcojpad-hash/capcot-capsulas-imaginantes/commit/057474c747202e164c28d3cf2f54c3196d55ca9f): cuatro paquetes asignados a slots del 1-nov, 15 archivos movidos.
- Commit [3795f4](https://github.com/marcojpad-hash/capcot-capsulas-imaginantes/commit/3795f40cd035a8293efed759a2af1b5d58ef1ef0): 29 project_id adicionales, 101 archivos movidos.
- Commit [6b9cf52](https://github.com/marcojpad-hash/capcot-capsulas-imaginantes/commit/6b9cf5285b19ba064d09fc843d741d69852f4d28): README de cuarentena y condiciones de reingreso.

**Verificación:** 116 archivos en total, 33 project_id; cada destino conserva exactamente el SHA de blob original y cada ruta fuente fue retirada. La consulta posterior al árbol encontró cero storyboard JSON en `cola/entrada/`. No se borró contenido, no se reescribió narración/fuentes, no se modificó `cola/estado/` y no se disparó el workflow (`[skip ci]` en el commit masivo).

Los PASS narrativos que el auditor reportó para Xolo y tiburón no se promovieron: sus JSON no contienen los siete checks ni el registro `narrative_qa`, y sus paquetes siguen teniendo fallos estructurales/administrativos. Xolo permanece en `salidas/`, no en cola. El reingreso requiere completar `narrative_contract`, revisión independiente registrada y validador estructural correcto.

