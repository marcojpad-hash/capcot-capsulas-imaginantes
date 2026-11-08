---
name: capcot-ai-video-tts
description: Usa el cliente TTS versionado de CAPCOT para sintetizar narración Edge TTS y activar Piper local cuando esté configurado.
---

# CAPCOT — voz y narración

Antes de producir, lee `AGENTS.md`, `docs/CONTRATO_OPERATIVO_UNIFICADO.md`, `docs/CONTINUIDAD_AUDIOVISUAL.md` y el contrato de producción vigente.

## Regla de ejecución

- Para producción audiovisual autorizada por el contrato, usa el cliente versionado `tools/tts/narrate.py`; no reimplementes llamadas TTS en cada proyecto.
- Motor primario: Edge TTS, voz oficial CAPCOT `es-MX-JorgeNeural`.
- Piper es un respaldo local opcional. Solo se activa si el entorno tiene instalado `piper-tts` y un modelo ONNX configurado. El cambio de motor debe quedar visible en el log y el registro de producción.
- No sustituyas la voz oficial silenciosamente. Si no hay modelo Piper configurado, el proceso falla con un error explícito.
- No guardes modelos ONNX, claves, cookies ni credenciales dentro del repositorio.
- No afirmes que el audio existe hasta comprobar que el archivo de salida existe y tiene tamaño mayor que cero.

## Instalación automática en un entorno limpio

```bash
python -m pip install -r tools/tts/requirements-edge.txt
```

Para habilitar el respaldo local:

```bash
python -m pip install -r tools/tts/requirements-piper.txt
python -m piper.download_voices <VOICE_ID>
```

Configura `PIPER_MODEL` con la ruta del archivo ONNX en el entorno ejecutor. Consulta `tools/tts/fallback.md` para detalles y licencias.

## Uso

```bash
python tools/tts/narrate.py guion.txt audio/narracion.mp3
```

Con respaldo explícito:

```bash
python tools/tts/narrate.py guion.txt audio/narracion.mp3 --engine auto --piper-model "$PIPER_MODEL"
```

El resultado informa `provider=edge-tts` o `provider=piper-local`. Piper entrega WAV; no renombres el WAV como MP3.

## Límite de responsabilidades

Esta skill es para el agente autorizado a producir audio (Imaginantes/Grok Bot, según el contrato CAPCOT). No amplía por sí sola las facultades de ChatGPT: la investigación y preproducción textual siguen separadas de la generación de voz, audio, render y publicación.
