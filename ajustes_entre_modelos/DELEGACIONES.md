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

### 7. Montar la semana 15–21 nov (lote oficial + reporte de créditos)
- DE: Pecas (orden de Marco, 2026-11-14 ~16:38 CST)
- PARA: Imaginantes (Grok Bot)
- QUÉ: montar el MP4 oficial de cada cápsula con voz es-MX-JorgeNeural (edge-tts, rate +7%, pitch −2 Hz), correr QA oficial y programar en YT + TT + FB, slot 13:30 CST.
  - PRIMERO, mínimo 2 (para medir cuántos créditos quedan): lun 16-nov `cola/entrada/2026-10-25_corales-contacto/` ("Un toque de vida") y mar 17-nov `cola/entrada/2026-10-26_baffin-bay-ice-shelf/` ("¿Qué sostuvo tres mantos?").
  - LUEGO, según alcancen los créditos: jue 19-nov `cola/entrada/2026-10-29_juno-choque-proa/` ("La frontera invisible"), vie 20-nov `cola/entrada/2026-11-01_mxenes-ia-descubrimiento/` ("¿IA descubre materiales?"), sáb 21-nov `cola/entrada/2026-11-02_oxoboranos-estables/` ("¿Molécula imposible?").
  - NO TOCAR: mié 18-nov, `cola/entrada/2026-10-28_mosquito-fruitless-audicion/` ("El mosquito que escucha") — ese lo monta Pecas como viral animado de la semana (ffmpeg + Kokoro/VoxCPM2 narradora_es). Regla anti-duplicado: paquete montado = paquete cerrado.
  - El dom 15-nov ya está cubierto: agua (YT O9QlSaft5DY, 13:30; TT/FB pendientes).
- CRÉDITOS (obligatorio): después de CADA montaje, reportar en el repo el saldo de Imaginantes antes y después. En el repo NO hay saldo de créditos (`data/balances_6h.json` es solo vistas/likes; último 2026-11-14 13:54 CDMX) y el costo por cápsula no está medido. Sin ese reporte no se puede saber cuántas cápsulas cubren los créditos que quedan.
- PARA CUÁNDO: el lote de 2 primero (16–17 nov); el resto 19–21 nov según créditos.
- ESTADO: PENDIENTE
- NOTA: los paquetes de la semana ya existen en `cola/entrada/` (storyboard + fuentes; sin capsula.mp4; sin frames salvo robot). Stock restante tras esta semana: 8 paquetes (autismo-microbioma, enzimas-oceano, bacterias-plasticos, sinergia-algas, adn-myc, webb-exoplaneta, robot-orbita, ldl). El robot (`2026-11-09_dato-robot-ensambla-orbita`) NO tiene frames — sigue bloqueado por Issues #161/#164, no se monta hasta tenerlos. Grok debe seguir generando el paquete diario C1 para la semana siguiente (el stock cubre ~8 días más). Reparto completo de la semana en `docs/COCINA_CAPCOT.md` § "Reparto semana 15–21 nov 2026".

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
