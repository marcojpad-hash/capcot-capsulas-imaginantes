# Auditoría de main — proyectos 24–29 nov (corte 2026-11-24 14:00 CDMX)

## Alcance y autoridad
- Fuente de auditoría: `main` HEAD `6bce6166d424a8a793a81e1f44cbc71031c88462` (solo lectura).
- Rama de trabajo/documentación: `feature/capcot-video-discovery-continuity`, HEAD observado al cerrar el análisis: `05be0c168e312d605e032909b0b7803b7f325136`.
- No se modificó `main`, `data/*.json`, proyectos, cola, estados Grok, publicaciones ni medios.
- La comparación de main desde `4860fa4addbfa903b26d274e95f5c34a33c1041a` muestra solo actualización de `data/endscreens_rotacion.json`; no cambió proyectos, programación ni cola.
- El árbol de main contiene 207 archivos multimedia históricos, pero ninguno de los nueve proyectos `2026-11-25_rehecho-*` ni los proyectos `yo-soy-sam` y `magnetismo-p-wave-eusi` tiene sus MP4/frames/portada dentro del repositorio.

## Lectura en frío independiente de los nueve rehechos
Método: lectura separada de la narración concatenada únicamente. Durante esa pasada no se consultaron título, resumen, arco, notas ni `narrative_contract`. Base exacta: `review_basis="lectura_en_frio_solo_narracion"`.

| project_id | score | status | pregunta central | apertura in medias res | progresión por escena | transiciones causales | giro científico explicado | límite de evidencia explícito | payoff cierre-apertura | critical_flags |
|---|---:|---|---|---|---|---|---|---|---|---|
| `2026-11-25_rehecho-barreleye-no-son-sus-ojos` | 89 | PASS | true | true | true | true | true | true | true | [] |
| `2026-11-25_rehecho-dunas-que-cantan-no-es-viento` | 92 | PASS | true | true | true | true | true | true | true | [] |
| `2026-11-25_rehecho-dunkelflaute-sin-sol-ni-viento` | 82 | FAIL | true | false | true | true | true | true | true | [`APERTURA_DEFINICIONAL`] |
| `2026-11-25_rehecho-escudo-jupiter-no-es-pared` | 82 | FAIL | true | true | true | true | false | true | true | [`GIRO_CIENTIFICO_NO_EXPLICADO`] |
| `2026-11-25_rehecho-miel-su-unico-enemigo` | 88 | PASS | true | true | true | true | true | true | true | [] |
| `2026-11-25_rehecho-nube-500-toneladas` | 91 | PASS | true | true | true | true | true | true | true | [] |
| `2026-11-25_rehecho-ola-azul-alarma-antirrobo` | 82 | FAIL | true | true | true | true | true | true | false | [`PAYOFF_NO_CIERRA_GANCHO`] |
| `2026-11-25_rehecho-pan-refri-endurece` | 90 | PASS | true | true | true | true | true | true | true | [] |
| `2026-11-25_rehecho-ratas-topo-ayudar-no-es-cuidar` | 91 | PASS | true | true | true | true | true | true | true | [] |

**Resultado narrativo externo:** 6 PASS y 3 FAIL. Los PASS cumplen score ≥85, siete checks true y flags vacías; los FAIL no cumplen. Esta revisión es una lectura en frío separada, pero no está incrustada como `narrative_qa` en los storyboards de main. Por la regla de autoridad de rama, no se modificaron esos archivos; el gate oficial de cada storyboard sigue sin registro embebido y ninguno se promueve.

## Compuertas estructurales de los nueve rehechos

Hallazgos comunes verificados en los nueve storyboards:

- 7 escenas y 215–229 palabras: dentro del rango de escenas/palabras.
- `titulo` de 7–10 palabras: supera el máximo de 6 palabras del gancho.
- `target_duration_seconds=88`; la suma de escenas es 70 s y la cortinilla 6 s (76 s declarados por escenas). `data/rehechos_2026-11-22.json` registra duraciones de render entre 86.47 y 88.80 s, pero los MP4 no están en el árbol GitHub; esa medición no se pudo verificar de forma independiente. Hay 10–13 s que no están explicados por el desglose de escenas.
- Voz declarada: `es-MX-JorgeNeural`, pitch +7%, velocidad -2 Hz.
- `estilo_id=foto_commons` no existe en el catálogo de 50 estilos de `scripts/estilos.json`; falta `visual_identity.prompt_base`.
- Faltan `visual_identity`, `typography_identity`, `trend_source`, `narrative_contract`, `narrative_qa`, `approved_assets` y `publicacion`.
- `export.filename=capsula.mp4` está declarado, pero no existe el MP4 en el árbol; falta `export.render_status=NOT_GENERATED`. Los nombres de medios en `data/rehechos` apuntan al workspace, no a archivos verificables del repositorio.
- En escenas faltan `dramatic_beat`, `scene_function`, `causal_bridge_from_previous`, `question_state`, `reason_to_continue`, `new_information`, `image_prompt` y `ambiente`. Hay SFX, pero no ambiente por escena.
- No hay mapa con coordenadas ni capa de dato/gráfico.
- No hay `fuentes.md` por proyecto ni `verification_status` en las fuentes. La compuerta Crossref/resolvedor no está acreditada y no se demuestra fuente primaria apta en todos los casos: **PENDING_SOURCE**.
- Ningún storyboard contiene `fecha_objetivo` ni `slot_local`; los horarios se encuentran en el registro separado `data/rehechos_2026-11-22.json`.
- Para los nueve `cola/estado/<project_id>.json` se consultó la ruta individual; todos devolvieron 404: **RECEPCION_GROK_NO_CONFIRMADA**.
- No hay copias de estos IDs en `cola/entrada/`, `cola/bloqueados/` ni `salidas/`. El registro separado sí tiene `programado_CDMX`, IDs de YouTube y estados de programación en TikTok/Facebook: **PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR**. No cancelar ni duplicar.
- Medios: **MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO**.

### Programación preexistente registrada en data/rehechos

| Proyecto | programado_CDMX | duración registrada (no verificada en MP4 del repo) |
|---|---|---:|
| nube 500 toneladas | 2026-11-25 10:00 | 87.13 s |
| barreleye | 2026-11-25 15:00 | 86.93 s |
| pan en refrigerador | 2026-11-26 10:00 | 87.27 s |
| ratas topo | 2026-11-26 15:00 | 86.47 s |
| miel | 2026-11-27 10:00 | 88.80 s |
| ola azul | 2026-11-27 15:00 | 87.07 s |
| escudo de Júpiter | 2026-11-28 10:00 | 86.47 s |
| dunas cantoras | 2026-11-28 15:00 | 86.47 s |
| Dunkelflaute | 2026-11-29 10:00 | 88.80 s |

**NO_DUPLICAR:** barreleye, choque de proa de Juno/escudo de Júpiter y ratas topo de Damaraland ya aparecen en la rotación reciente. Los otros seis no aparecen como coincidencia exacta en los 39 registros de rotación revisados; esto no demuestra unicidad frente a todo el histórico.

## Otros dos proyectos del 24 de noviembre

### `2026-11-24_yo-soy-sam`
- No tiene `storyboard.json` ni `fuentes.md`; sí tiene `programacion.json`, `facebook.json` y `tiktok.json`.
- Los registros muestran YouTube publicado a las 07:00 CDMX, TikTok a las 07:38 y Facebook a las 07:41.
- Comparte 07:00 con `2026-11-24_purpura-no-piedras`: conflicto exacto de slot.
- El contenido es una pieza narrativa/ficcional, fuera de la línea de ciencia/naturaleza/cocina/cuerpo/espacio de Datos y ociosidades.
- No hay MP4 ni storyboard en el árbol GitHub: **PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR** y **MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO**. No redistribuir ni duplicar.

### `2026-11-24_magnetismo-p-wave-eusi`
- Hay proyecto en `proyectos/` y copia heredada en `cola/entrada/2026-11-24_magnetismo-p-wave-eusi/`; la copia está anidada, mientras el selector del workflow acepta JSON plano en la raíz de `cola/entrada/`: **NOT_DISPATCHABLE**.
- `programacion.json` registra `publish_at=2026-11-24T23:15:00Z` (17:15 CDMX) y estado `programado_para_publicar`, pero indica explícitamente que falta montar el MP4 con el pipeline oficial.
- El storyboard tiene 6 escenas y 138 palabras; no tiene `narrative_qa`, `narrative_contract`, mapa ni capa de dato/gráfico. Declara `export.filename` y referencias de frames que no aparecen en el árbol.
- `cola/estado/2026-11-24_magnetismo-p-wave-eusi.json` devolvió 404: **RECEPCION_GROK_NO_CONFIRMADA**.
- No hay MP4/frames/portada verificables: **MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO**.
- Por programación preexistente: **PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR**. No mover, cancelar ni volver a enviar desde esta auditoría.

## Inventario y ocupación observada

- `data/publicaciones.json`: 62 registros (el conteo de 52 del corte anterior queda corregido).
- `data/rotacion.json`: 39 registros.
- `data/cola.json`: 0 registros; esto no elimina la copia anidada de Magnetismo encontrada en el árbol.
- `data/miniaturas_auditoria_2026-11-21.json`: 36 elementos en `siguen_mal_sin_mp4_no_se_invento`; colisiones registradas el 25 (07:00), 26 (17:00), 27 (07:00) y 28 (17:00). Además, `publicaciones.json` muestra colisión 24 (07:00: Yo soy Sam/Púrpura) y el snapshot muestra 24 (17:00: Pollo/Vomitorium).
- 24 nov: cinco horas ocupadas (07:00, 13:30, 17:00, 17:15 y 19:00), con colisiones en 07:00 y 17:00. El slot fijo 23:30 no tiene proyecto identificado en los registros consultados.
- 25–28 nov: seis horas ocupadas por día (07:00, 10:00, 13:30, 15:00, 17:00 y 19:00), por encima del máximo de cinco; el slot fijo 23:30 está reservado, pero no se encontró un proyecto individual para contarlo como ocupado. El conteo previo 7/5 incluía esa reserva.
- 29 nov: cinco horas ocupadas (07:00, 10:00, 13:30, 17:00 y 19:00).
- La política activa fija ventanas 06:30–07:30 y 16:30–18:00, con 13:00–14:30 como prueba; 10:00, 15:00 y 19:00 quedan fuera. Son programaciones preexistentes: no cancelar ni reprogramar desde esta auditoría.
- `historial_youtube.json` no existe (404); se usaron `publicaciones.json` y los snapshots disponibles, sin inferir historial adicional.

## Acciones y límites
- No se promovió ningún proyecto a cola.
- No se modificó `main`, `data/*.json`, `cola/estado`, publicaciones ni permisos.
- No se disparó `capcot-grok-dispatch.yml`, no se envió payload, no se consultaron valores de secretos y no se generó ningún medio.
- La lectura narrativa externa no sustituye el campo `narrative_qa` en main; la promoción sigue cerrada por estructura, fuente, recepción Grok, medios y programación preexistente.
