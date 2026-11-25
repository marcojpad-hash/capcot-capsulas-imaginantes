# CAPCOT — control de cola, backlog y producción preexistente
**Corte:** 2026-11-24 22:00 CDMX  
**Rama auditada:** `feature/capcot-video-discovery-continuity` — HEAD `962178fbf7400638b61ddd1dbde4c3cff23419ff`  
**Comparación de solo lectura:** `main` — HEAD `aa023def4955509502e567549064505854f54e7e`

## Inventario de la rama de trabajo
- La rama de trabajo conserva 90 storyboards; no contiene proyecto nuevo de fecha 24 o 25 de noviembre ni nuevas entradas para esos días.
- El control anterior sigue registrando 32 storyboards con QA narrativo y 40 sin QA; el lote de 12 IDs del 5–7 de noviembre permanece en 2 PASS y 10 FAIL. No se repitieron PASS válidos.
- No se creó ni promovió ningún archivo a `cola/entrada`; no se modificó `cola/estado`.

## Proyectos de main: solo lectura

### 24-nov — magnetismo p-wave en EuSi
- Existe en `proyectos/2026-11-24_magnetismo-p-wave-eusi/` y como copia en `cola/entrada/2026-11-24_magnetismo-p-wave-eusi/`.
- `programacion.json` declara `publishAt=2026-11-24T23:15:00Z` (17:15 CDMX), ya pasado en este corte. Es procesamiento/programación preexistente: **PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR**.
- El storyboard tiene 121 palabras y 6 escenas; no contiene `narrative_qa`. El `export.filename` referencia `capsula.mp4`, pero el archivo no aparece en el árbol. No hay `cola/estado/<id>.json`: **RECEPCION_GROK_NO_CONFIRMADA** y **MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO**.
- Clasificación: **NOT_DISPATCHABLE**. No se duplicó, canceló ni redispatchó.
- `yo-soy-sam` ya tiene publicación registrada a las 07:00 con IDs de plataforma; no se reprograma ni redispatcha.

### 25-nov — nueve reworks preexistentes
Los siguientes nueve proyectos están en `main`, no en la rama de trabajo:
- `2026-11-25_rehecho-barreleye-no-son-sus-ojos` — 221 palabras, 7 escenas, render.log 87.53 s.
- `2026-11-25_rehecho-dunas-que-cantan-no-es-viento` — 220 palabras, 7 escenas, 86.70 s.
- `2026-11-25_rehecho-dunkelflaute-sin-sol-ni-viento` — 217 palabras, 7 escenas, 88.77 s.
- `2026-11-25_rehecho-escudo-jupiter-no-es-pared` — 225 palabras, 7 escenas, 87.40 s.
- `2026-11-25_rehecho-miel-su-unico-enemigo` — 229 palabras, 7 escenas, 86.47 s.
- `2026-11-25_rehecho-nube-500-toneladas` — 215 palabras, 7 escenas, 86.80 s.
- `2026-11-25_rehecho-ola-azul-alarma-antirrobo` — 220 palabras, 7 escenas, 87.17 s.
- `2026-11-25_rehecho-pan-refri-endurece` — 219 palabras, 7 escenas, 88.47 s.
- `2026-11-25_rehecho-ratas-topo-ayudar-no-es-cuidar` — 218 palabras, 7 escenas, 88.80 s.

Los logs dicen `OK .../capsula.mp4`, pero ninguno de los nueve MP4 aparece en el árbol de Git. Por tanto, las duraciones son **declaraciones de render.log**, no mediciones re-verificadas sobre el archivo: **MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO**. Hay un aviso en Barreleye: la cortinilla invade la zona segura inferior.

Los nueve storyboards carecen de `fecha_objetivo`, `slot_local`, `narrative_qa`, `narrative_contract`, `approved_assets`, `publicacion`, `visual_identity`, `typography_identity` y `trend_source`; usan `export.filename` y no declaran `export.render_status`. Todos usan `estilo_id=foto_commons`, que no existe en el catálogo de 50 estilos de main. Las escenas no incluyen mapa/capa de datos ni el contrato dramático completo. No hay entrada de cola, salida ni estado Grok individual para esos IDs.

**Clasificación de los nueve:** **PROCESAMIENTO_PREEXISTENTE_NO_REDISPATCHAR**, **RECEPCION_GROK_NO_CONFIRMADA**, **MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO**, **NOT_DISPATCHABLE**. No se copiaron a feature ni se modificó main.

## QA narrativo en frío — solo narración concatenada
Se hizo una revisión independiente de esta ejecución, sin título, resumen, arco, notas ni narrative_contract. La revisión no se escribió en los storyboards porque son de main, solo lectura. Por ello, los artefactos siguen sin `narrative_qa` persistido y no son promovibles.

- Barreleye: 90, 7/7 checks; PASS en esta revisión.
- Dunas cantoras: 90, 7/7; PASS.
- Dunkelflaute: 86, 6/7; FAIL — `apertura_in_medias_res=false` por apertura definicional.
- Escudo de Júpiter: 90, 7/7; PASS.
- Miel: 90, 7/7; PASS.
- Nube de 500 toneladas: 90, 7/7; PASS narrativo; la analogía de densidad del aire requiere revisión factual separada.
- Ola azul: 90, 7/7; PASS.
- Pan refrigerado: 90, 7/7; PASS.
- Ratas topo: 90, 7/7; PASS.

En los PASS, los siete checks fueron true: pregunta central reconstruible, apertura in medias res, progresión por escena, transiciones causales, giro científico explicado, límite de evidencia explícito y payoff cierre-apertura. El único FAIL no se reescribió.

## Programación, cola, acciones y seguridad
- `data/publicaciones.json` contiene tres registros del 24-nov; `tt_fb_alineacion_2026-11-24.json` y `miniaturas_auditoria_2026-11-21.json` enumeran más publicaciones/slots previstos. `data/rotacion.json` y `data/temas_del_dia.json` no tienen registro del 24/25. Se mantiene **REGISTROS_PUBLICACION_NO_CONCILIADOS** y la colisión de las 17:00; no se libera un slot por inferencia.
- El trabajador de cola de main terminó SUCCESS con el log `[trabajador] sin trabajo en cola.`; el callback de delegaciones terminó SUCCESS. No se disparó ningún workflow manualmente.
- Kuroshio: run [45502897065](https://github.com/marcojpad-hash/capcot-capsulas-imaginantes/actions/runs/45502897065) SUCCESS, pero ejecutó solo `python scripts/validar_storyboard.py ...`, sin `--check-doi`; no verifica DOI.
- Semgrep: run [45531032208](https://github.com/marcojpad-hash/capcot-capsulas-imaginantes/actions/runs/45531032208) FAIL, 37 hallazgos bloqueantes. Gitleaks había pasado en el corte anterior.
- El último dispatch visible, run [41306776689](https://github.com/marcojpad-hash/capcot-capsulas-imaginantes/actions/runs/41306776689), falló el 1-nov con `Falta configurar GROK_WEBHOOK_URL`; el entorno también mostró `WEBHOOK_TOKEN` vacío. No existe run más reciente de ese workflow en la rama de trabajo; el estado actual de secretos no se puede inferir.
- PR #15 continúa abierto y obsoleto frente al validador actual; no se portó código redundante.

## Resultado del corte
- **EJECUTADO:** auditoría de main/feature, revisión en frío independiente, reintento de fuentes, actualización del radar y este registro.
- **VERIFICADO:** lectura de vuelta de ramas, storyboards, logs, datos, workflow y Actions.
- **PENDIENTE:** registro de narrative_qa en la rama autorizada, DOI/Crossref, conciliación de programación y medios, recepción Grok individual.
- No se generaron medios, no se promovió cola, no se publicó ni se consumieron créditos.
