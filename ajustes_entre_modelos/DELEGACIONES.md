# Delegaciones entre modelos

Tablero vivo del callback. Quien delega escribe aquí. Quien recibe lee aquí.
Reglas en `PROTOCOLO_CALLBACK.md`.

Este tablero es de CAPCOT. El motor U6 es un proyecto aparte y no lleva
delegaciones aquí. Si el callback se implementa en el motor después, será
su propio tablero.

## Pendientes

### 1. Montar la cápsula Mpemba
- DE: ChatGPT / Grok
- PARA: Imaginantes
- QUÉ: montar el MP4 oficial con voz es-MX-JorgeNeural, correr QA oficial y programar. Paquete en `cola/entrada/2026-11-07_comida-hielo-caliente/`
- PARA CUÁNDO: slot 2026-11-07 13:30 (ya pasó; reprogramar)
- ESTADO: PENDIENTE
- NOTA: Imaginantes pausado por ahorro de créditos

### 2. Montar la cápsula Barreleye
- DE: ChatGPT / Grok
- PARA: Imaginantes
- QUÉ: montar el MP4 oficial con los 2 arreglos de texto (scene_002: "frente a la costa de California"; scene_004: quitar "verdes" o citar Robison y Reisenbichler 2008), correr QA oficial y programar. Paquete en `cola/entrada/2026-11-07_barreleye-4k/`
- PARA CUÁNDO: primera cápsula de la semana 8-14 nov (propuesto, sin confirmar)
- ESTADO: PENDIENTE
- NOTA: Imaginantes pausado por ahorro de créditos

### 3. Subir los workflows de seguridad de CAPCOT
- DE: Pecas
- PARA: Pecas (por navegador; ruta probada con guardian.yml 2026-11-09)
- QUÉ: subir `gitleaks.yml` y `semgrep.yml` (CAPCOT). Archivos listos en `~/workspace/security-upload/`
- PARA CUÁNDO: cuanto antes
- ESTADO: PENDIENTE
- NOTA: reasignado 2026-11-10 (G3): Marco no es el autorizador ni sube nada; la vía del bus a Copilot/Codex no cerraba porque no puede leer el workspace de Pecas, así que va por el navegador de Pecas

### 4. Activar la seguridad nativa en GitHub
- DE: Pecas
- PARA: Pecas (por navegador, en Settings > Code security)
- QUÉ: secret scanning y CodeQL en CAPCOT, alertas de Dependabot en CAPCOT
- PARA CUÁNDO: cuanto antes
- ESTADO: PENDIENTE
- NOTA: reasignado 2026-11-10 (G3): Marco no es el autorizador; los toggles de Settings los activa el navegador de Pecas, no Marco

### 5. Crear cuenta gratuita de Clayzo
- DE: Pecas
- PARA: Marco (decide si se crea; si dice que sí, Pecas la crea por navegador)
- QUÉ: crear la cuenta gratuita para probar el render del documento Mpemba (1080x1920, capas de texto/dato/mapa)
- PARA CUÁNDO: sin fecha
- ESTADO: PENDIENTE
- NOTA: reasignado 2026-11-10 (G3): crear cuentas es decisión de Marco, no trabajo de autorización; la ejecución es de Pecas. Duda: Mpemba v2 ya se montó con los clips originales, ¿sigue haciendo falta esta prueba?

## En progreso

(nada)

## Hechas

### 7. Montar la semana 15–21 nov (lote oficial + reporte de créditos)
- DE: Pecas (orden de Marco, 2026-11-14 ~16:38 CST)
- PARA: Imaginantes (Grok Bot)
- QUÉ: montar el MP4 oficial de cada cápsula con voz es-MX-JorgeNeural (edge-tts, rate +7%, pitch −2 Hz), correr QA oficial y programar en YT + TT + FB, slot 13:30 CST.
- ESTADO: HECHA (mp4 en origin/main y YT programado en las 5 que tocan a Imaginantes; TT/FB pendientes de Studio). NO se tocó el mosquito del 18-nov.
- CRÉDITOS (Grok Bot, cuota semanal incluida): antes del lote 13.5% usada; después de corales 15.2%; después de las 5, 20.4% usada. No hay on-demand. El reset es el sábado 21-nov a las 10:18 (hora de Mexico City).
- EVIDENCIA:

  1) Corales — `cola/entrada/2026-10-25_corales-contacto/capsula.mp4`
     - commit mp4: `9e1fd2dfdc0b7e89570e1db52ff98e1ebc9a8bb7` (blob `73509135dfdede0fb18a0e710596776fb061fc00`, confirmado con `git ls-tree origin/main`)
     - ffprobe: 90.00 s, 1080x1920, 30 fps, h264+aac
     - voz: es-MX-JorgeNeural, edge-tts rate +7%, pitch -2Hz
     - QA oficial: 21/21
     - YT: `45WOvkNQTHo` (https://youtube.com/shorts/45WOvkNQTHo), private, publishAt `2026-11-16T19:30:00Z`, miniatura vertical sardefault = portada (título «Un toque de vida», sin subtítulo). Sin colisión. Token `~/.capcot/token.json`.
     - local: `/workspace/entregas/2026-11-16_corales/`

  2) Baffin — `cola/entrada/2026-10-26_baffin-bay-ice-shelf/capsula.mp4`
     - commit mp4: `1c9fccb99454372e7b4d7d28b76bdd5172d9aec9` (blob `5db072f37fc9ca206b7e197aa558991b6360c0b9`)
     - ffprobe: 90.17 s, 1080x1920, 30 fps, h264+aac (0.17 s sobre 90; cierre 10.1 s)
     - voz: es-MX-JorgeNeural, edge-tts rate +7%, pitch -2Hz
     - QA oficial: 21/21
     - YT: `KnP1j4y72ug` (https://youtube.com/shorts/KnP1j4y72ug), private, publishAt `2026-11-17T19:30:00Z`, sardefault = portada (título «¿Qué sostuvo tres mantos?»). Sin colisión.
     - local: `/workspace/entregas/2026-11-17_baffin/`

  3) Juno — `cola/entrada/2026-10-29_juno-choque-proa/capsula.mp4`
     - commit mp4: `bb8294c7b0bf0f282930aac863a1cf276f649101` (blob `69e74a55b6d523724ad354364e82462e232d0606`, confirmado con `git ls-tree origin/main`)
     - ffprobe: 86.97 s, 1080x1920, 30 fps, h264+aac
     - 8 frames (no se inventaron); cierre/cortinilla 16 s (voz termina ~70.8 s)
     - voz: es-MX-JorgeNeural, edge-tts rate +7%, pitch -2Hz
     - QA oficial: 21/21
     - YT: `vj5RZDt-dfc` (https://youtube.com/shorts/vj5RZDt-dfc), private, publishAt `2026-11-19T19:30:00Z`, sardefault = portada (título «La frontera invisible»). Sin colisión.
     - local: `/workspace/entregas/2026-11-19_juno/`

  4) MXenes — `cola/entrada/2026-11-01_mxenes-ia-descubrimiento/capsula.mp4`
     - commit mp4: `ecd7df67344b0c4fb194c11e0eb233f2b7972900` (blob `6fccddaffea4c99e92ca881dd0d41d56086268c3`, confirmado con `git ls-tree origin/main`)
     - ffprobe: 89.00 s, 1080x1920, 30 fps, h264+aac
     - 8 frames (no se inventaron); cierre ~11.8 s (voz termina ~77.2 s)
     - voz: es-MX-JorgeNeural, edge-tts rate +7%, pitch -2Hz
     - QA oficial: 21/21
     - YT: `WTlFSZV9HYg` (https://youtube.com/shorts/WTlFSZV9HYg), private, publishAt `2026-11-20T19:30:00Z`, sardefault = portada (título «¿IA descubre materiales?»). Sin colisión.
     - local: `/workspace/entregas/2026-11-20_mxenes/`

  5) Oxoboranos — `cola/entrada/2026-11-02_oxoboranos-estables/capsula.mp4`
     - commit mp4: `49aee3fd13668b0b79a302aef33f1da3a1e5ea96` (blob `7e1ab4b8f064bc64b0a7ef46b109ebc106d8780e`, confirmado con `git ls-tree origin/main`)
     - ffprobe: 90.90 s, 1080x1920, 30 fps, h264+aac (0.90 s sobre 90 para no recortar el cierre de 10 s; voz termina ~80.87 s)
     - 8 frames (no se inventaron)
     - voz: es-MX-JorgeNeural, edge-tts rate +7%, pitch -2Hz
     - QA oficial: 21/21
     - YT: `K4qNkx2f4RI` (https://youtube.com/shorts/K4qNkx2f4RI), private, publishAt `2026-11-21T19:30:00Z`, sardefault = portada (título «¿Molécula imposible?»). Sin colisión.
     - local: `/workspace/entregas/2026-11-21_oxoboranos/`

- NOTA: TT y FB quedan pendientes en las 5, con portada = primer frame. No se tocó `2026-10-28_mosquito-fruitless-audicion/` ni el dato del día. Casilla YT de contenido sintético en «No» (ilustración no realista + aviso de IA en la descripción), igual que agua.

### 6. Montar la cápsula Agua que une imanes lejanos (dato 15-nov)
- DE: Pecas (orden de Marco, 2026-11-14 00:28 CST)
- PARA: Imaginantes (Grok Bot)
- QUÉ: montar el MP4 oficial con voz es-MX-JorgeNeural (edge-tts, rate +7%, pitch -2Hz), correr QA oficial y programar. Paquete en `cola/entrada/2026-11-11_agua-magnetismo-hidrogeno/`
- PARA CUÁNDO: programar domingo 2026-11-15 13:30 CST (YT, TT y FB)
- ESTADO: HECHA (mp4 en origin/main; YT programado; TT/FB pendientes de Studio)
- EVIDENCIA:
  - path en repo: `cola/entrada/2026-11-11_agua-magnetismo-hidrogeno/capsula.mp4` (confirmado con `git ls-tree origin/main`; blob `3bd75a813b00c0ed6822fec6837e1b3424463003`)
  - commit del mp4: `357a341541ec81dfadeae87e3ab8d05259991613`
  - ffprobe: 85.13 s, 1080x1920, 30 fps, h264+aac (YouTube reporta PT1M26S)
  - voz: es-MX-JorgeNeural, edge-tts rate +7%, pitch -2Hz (no otra voz)
  - QA oficial: 21/21
  - YT: `O9QlSaft5DY` (https://youtube.com/shorts/O9QlSaft5DY), private, publishAt `2026-11-15T19:30:00Z`, thumbnails.set con `portada.jpg` (primer frame, título en caja crema). Token `~/.capcot/token.json`. Sin colisión en ese slot el 15-nov.
- NOTA: los commits previos (11:06 / Altair 55.9 s) no cuentan: no había capsula.mp4 en el remoto y/o no usaban JorgeNeural. El guion original de 6 escenas era demasiado corto para ~82 s en modo continuo; se amplió a 9 escenas y 203 palabras conservando SRC-001/SRC-002. No había un capsula.mp4 de Altair en el paquete que renombrar. TT y FB quedan pendientes, con archivos en `/workspace/entregas/2026-11-15_agua-imanes/`.
