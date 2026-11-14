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
