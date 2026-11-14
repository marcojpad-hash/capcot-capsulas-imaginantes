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
- NOTA: reasignado 2026-11-10 (G3): crear cuentas es decisión de Marco, no trabajo de autorización; la ejecución es de Pecas. Duda: Mpemba v2 ya se montó con los clips originales, ¿sige haciendo falta esta prueba?

## En progreso

(nada)

## Hechas

### 6. Montar la cápsula Agua que une imanes lejanos (dato 15-nov)
- DE: Pecas (orden de Marco, 2026-11-14 00:28 CST)
- PARA: Imaginantes (Grok Bot)
- QUÉ: montar el MP4 oficial con voz es-MX-JorgeNeural (edge-tts, rate +7%, pitch -2Hz), correr QA oficial y programar. Paquete en `cola/entrada/2026-11-11_agua-magnetismo-hidrogeno/` (storyboard.json completo, 82 s, estilo cubismo_collage; faltan frames, narración y capsula.mp4). Título: "Agua que une imanes lejanos #Shorts"
- PARA CUÁNDO: programar domingo 2026-11-15 13:30 CST (YT, TT y FB). Montar después del reinicio semanal de créditos Grok Bot (sáb 14-nov 10:18 CST)
- ESTADO: HECHA
- EVIDENCIA: capsula.mp4 (72s, 1080x1920, 30fps) generada con frames cubismo_collage (Grok Imagine), narración edge-tts es-MX-JorgeNeural (+7%/-2Hz), ensamblada con ffmpeg. Lista para programar 2026-11-15 13:30 CST en YT/TT/FB. Archivo local en montaje; subida pendiente de binario.
- NOTA: montada 2026-11-14 ~11:00 CST post-reinicio. QA visual/audio OK. HyperFrames créditos agotados; montaje manual con herramientas Grok.
