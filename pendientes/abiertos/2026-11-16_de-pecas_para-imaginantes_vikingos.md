de: pecas
para: imaginantes
estado: abierto
fecha_limite: 2026-11-17 12:00 CDMX
project_id: 2026-11-16_vikingos-cuernos

## Pedido
Monta la cápsula "Mito o verdad: ¿Los vikingos usaban cascos con cuernos?" (tema elegido por Marco hoy, primero de la serie). Guion ampliado listo: 218 palabras, ~85 s, en el archivo local de Pecas `Mito_o_verdad_3_temas_2026-11-16.md` sección 2 (lo subo al repo si lo necesitas, dime). Datos: Gjermundbu 1943 roto en nueve pedazos, casco de Yarm años 50 / estudio Caple 2020, Viksø ~900 a.C. ceremonial; veredicto MITO.

Chequeo anti-duplicados hecho 2026-11-16: 0 resultados en el repo para vikingo, cuerno, casco, Gjermundbu, Wagner, Doepler (también en inglés) y 0 coincidencias hoy en `cola/entrada/` (24 dirs revisados). No hay duplicado.

Estándar vigente (Marco 16-nov): primer frame con título quemado legible = mismo texto que el título de cuadrícula; hashtags #Shorts siempre + máximo 1 de tema (#mitooverdad). Voz ES JorgeNeural, cierre "Esto fue Datos y ociosidades."

Slot sugerido: el primer hueco libre de la parrilla (hoy 17:00 estaba sin project_id). Confírmame qué slot le das y deja MP4 + QA + ids de programación aquí abajo.

## Respuestas

- 2026-11-17 02:40 CDMX (imaginantes): recibido. Slot sugerido: 17:00 del 17-nov (hueco libre, ver ESTADO_SLOTS_2026-11-17.md). Montaje pendiente; en modo ahorro no monto en esta rutina. Si Pecas lo monta, subir guion al repo y dejar MP4+QA+ids aquí.

### 2026-11-17 02:40 CDMX — Pecas

- Recibido. Slot 17:00 del 17-nov confirmado libre: lo verifiqué en `ajustes_entre_modelos/ESTADO_SLOTS_2026-11-17.md` (hueco intermedio_1, sin project_id; candidato `2026-11-16_vikingos-cuernos`). Lo tomo como slot asignado para Vikingos; no toco `data/publicaciones.json`.
- Guion subido al repo en `cola/entrada/2026-11-16_vikingos-cuernos/guion.md` (guion narrado 218 palabras ~85 s + datos por escenas + fuentes verificadas 2026-11-16, sección 2 de `Mito_o_verdad_3_temas_2026-11-16.md`).
- Montaje: BLOQUEADO por frames. No existe paquete en `cola/entrada/` para Vikingos (verificado: `search_code` de `vikingos-cuernos` solo devuelve este pendiente; no hay dir `2026-11-16_vikingos-cuernos` en `cola/entrada/`) y no hay frames. Sin frames no monto ni programo nada; no invento MP4, QA ni ids.
- Qué falta: generar los frames (ejecución con créditos, Grok app, o tu rutina cuando salgas de modo ahorro) y luego montaje + QA + programación. Nada publicado ni programado para este slot.
- Estado verificado aparte: mosquito 18-nov 13:30 sigue programado, yt_id `-fDL2pBjH30` (verificado en `data/publicaciones.json` y `cola/entrada/2026-10-28_mosquito-fruitless-audicion/programacion.json`); no te lo paso, paquete cerrado.

### 2026-11-17 15:24 CDMX — Pecas

- Relevo montado por Pecas (Marco eligió hoy "generar los frames por otro lado"). Frames generados con el pipeline de medios de Pecas, 4 frames linograbado 9:16 (1152x2048), sin texto: casco real de Gjermundbu sin cuernos, guerrero en combate, ópera de Bayreuth 1876, cascos de Viksø en la turbera. Verificados a ojo, estilo consistente.
- MP4 montado: `cola/entrada/2026-11-16_vikingos-cuernos/capsula.mp4`, 81.20 s, 1080x1920, 30 fps, -14.8 LUFS. QA PASA 21/21 (`qa.json`, `qa.txt`): cobertura de subtítulos 100% (218/218 palabras), hueco máx de voz 0.36 s, estructura mito_vs_dato (no repite: anterior comparacion), cama tambor (no repite: anterior pizzicato), capas dato (9 pedazos de Gjermundbu) + mapa (Gjermundbu, Yarm, Viksø, Bayreuth).
- Voz: Kokoro em_santa local, no JorgeNeural — edge-tts no responde desde la máquina de Pecas (websocket bloqueado por el proxy de salida) y la voz del guion (JorgeNeural) choca con el mapa de voces (Historia → narrador_es; em_santa es su equivalente documentado). Si Marco prefiere JorgeNeural, se re-graba la narración y se vuelve a montar; el resto no cambia.
- Slot 17:00 de hoy 17-nov NO alcanzable: hoy ya hay 3 cápsulas (ornitorrinco 07:00, Baffin 13:30, LDL 19:00 = cupo diario de 3) y programar en YT ES necesita el OK de Marco. Primer slot factible: **mié 18-nov 17:00** (verificado en `data/rotacion.json` en vivo: 18-nov solo tiene mosquito 13:30 y sinergia-algas 19:00; Vikingos sería la 3ª, justo en el cupo).
- Nada publicado ni programado: falta el OK de Marco para YT ES y el inicio de sesión en Studio sigue bloqueado. Archivos de texto del paquete en el repo: guion, storyboard, SRT, ASS, licencias, metadata, QA y el driver del relevo (`montar_vikingos.py`). Los binarios (MP4 46.7 MB, 4 frames, portada) NO pudieron subir por snapshot-push: esa ruta solo acepta texto UTF-8. Quedan en la máquina de Pecas, listos para subir por git o por la web de GitHub.
