# Respaldo local Piper

Edge TTS es el motor primario y requiere internet. Piper es el respaldo local: una vez instalado el runtime y descargados el modelo ONNX y su configuración, la síntesis no necesita red.

## Preparación del entorno

```bash
python -m pip install -r tools/tts/requirements-piper.txt
python -m piper.download_voices <VOICE_ID>
```

Elige un modelo español disponible en el catálogo oficial de voces de Piper y conserva juntos el archivo `.onnx` y su `.onnx.json`. No se versionan modelos binarios en este repositorio: pesan mucho y cada voz tiene sus propios términos de licencia.

Configura `PIPER_MODEL=/ruta/al/modelo.onnx` en el entorno que ejecuta la síntesis.

## Uso

```bash
python tools/tts/narrate.py guion.txt audio/narracion.mp3 --engine auto --piper-model /ruta/modelo.onnx
```

- Primero intenta Edge TTS con `es-MX-JorgeNeural`.
- Si Edge falla y hay un modelo Piper configurado, activa el respaldo y lo informa por stderr.
- El respaldo produce WAV. Si la ruta solicitada termina en `.mp3`, el script genera el WAV con la misma base y extensión `.wav`.
- Para exigir Edge y bloquear cualquier sustitución: `--engine edge`.
- Para ejecutar Piper directamente: `--engine piper --piper-model /ruta/modelo.onnx`.

Catálogo y documentación: https://github.com/OHF-Voice/piper1-gpl · https://github.com/OHF-Voice/piper1-gpl/blob/main/docs/CLI.md · https://huggingface.co/rhasspy/piper-voices

**Licencias:** revisar la licencia del modelo de voz concreto antes de usarlo en una publicación comercial. La licencia del runtime no sustituye la licencia del modelo.
