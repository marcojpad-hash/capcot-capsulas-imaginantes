# Delegaciones entre modelos

Tablero vivo del callback. Quien delega escribe aquí. Quien recibe lee aquí.
Reglas en `PROTOCOLO_CALLBACK.md`.

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

### 3. Subir los workflows de seguridad
- DE: Pecas
- PARA: Marco (por navegador, la app de Muse no tiene permiso Workflows)
- QUÉ: subir `gitleaks.yml` (ambos repos), `semgrep.yml` (CAPCOT) y `semgrep-motor.yml` (motor). Archivos listos en `~/workspace/security-upload/`
- PARA CUÁNDO: cuanto antes
- ESTADO: PENDIENTE

### 4. Activar la seguridad nativa en GitHub
- DE: Pecas
- PARA: Marco (manual en Settings)
- QUÉ: secret scanning y CodeQL en CAPCOT, alertas de Dependabot en ambos repos
- PARA CUÁNDO: cuanto antes
- ESTADO: PENDIENTE

### 5. Crear cuenta gratuita de Clayzo
- DE: Pecas
- PARA: Marco
- QUÉ: crear la cuenta gratuita para probar el render del documento Mpemba (1080x1920, capas de texto/dato/mapa)
- PARA CUÁNDO: sin fecha
- ESTADO: PENDIENTE

### 6. Verificar tokens.jsonl del motor
- DE: Pecas
- PARA: Marco
- QUÉ: verificar `stinkbox/tokens.jsonl` del motor (17 MB). Si tiene tokens vivos, rotarlos y sacarlo del historial
- PARA CUÁNDO: sin fecha
- ESTADO: PENDIENTE

### 7. Motor U6: lote diario automático
- DE: Pecas
- PARA: Copilot / motor
- QUÉ: ponerle cron a `fabrica-lote-diario.yml` (hoy solo tiene workflow_dispatch), manifiesto de dependencias y rutas parametrizadas, cohorte de 20 casos ciegos
- PARA CUÁNDO: sin fecha
- ESTADO: PENDIENTE

## En progreso

(nada)

## Hechas

(nada registrado aún en este tablero)
