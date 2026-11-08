# TTS reutilizable CAPCOT

## Estado y alcance

Cliente compartido en `tools/tts/narrate.py`. Cualquier agente que tenga acceso al repositorio y un entorno Python puede leer la skill e invocarlo. No es un servicio remoto permanente: se ejecuta en el entorno del agente que produce la narración.

- Primario: Edge TTS online, sin API key, requiere conexión.
- Voz por defecto: `es-MX-JorgeNeural` (voz CAPCOT vigente).
- Respaldo: Piper local, solo si se instaló y se configuró un modelo ONNX.
- Salida Edge: MP3.
- Salida Piper: WAV.
- Las dependencias se instalan en cada entorno ejecutor; un `requirements.txt` versiona dependencias, no contiene paquetes instalados.
- Los modelos Piper no se guardan en Git: se descargan una vez en el entorno que los utilizará y se configuran mediante `PIPER_MODEL`.

## Preparar el entorno

```bash
python -m pip install -r tools/tts/requirements-edge.txt
```

Para habilitar el respaldo local:

```bash
python -m pip install -r tools/tts/requirements-piper.txt
python -m piper.download_voices
```

Elige una voz española del catálogo oficial y descarga su modelo. Configura la ruta del archivo `.onnx` en `PIPER_MODEL`. Conserva el archivo de configuración `.onnx.json` junto al modelo.

## Uso

```bash
python tools/tts/narrate.py guion.txt audio/narracion.mp3
```

Con fallback:

```bash
python tools/tts/narrate.py guion.txt audio/narracion.mp3 --engine auto --piper-model /ruta/modelo.onnx
```

Forzar un motor:

```bash
python tools/tts/narrate.py guion.txt audio/narracion.mp3 --engine edge
python tools/tts/narrate.py guion.txt audio/narracion.wav --engine piper --piper-model /ruta/modelo.onnx
```

El cliente informa el proveedor realmente utilizado. Si Edge falla y no existe modelo Piper configurado, devuelve error; no inventa un archivo ni cambia de voz en silencio.

## Integración del renderizador actual

`scripts/montar_capsula.py` mantiene su integración propia con Edge TTS porque recoge marcas temporales por palabra para construir subtítulos sincronizados. Este cliente compartido aún no reemplaza ese módulo ni conecta Piper al renderizador. No declarar que el renderizador completo tiene fallback Piper hasta integrar y probar esa ruta específica.

## Licencias y límites

- Edge TTS utiliza un endpoint online no oficial de Microsoft; puede cambiar o dejar de funcionar sin aviso. No es un motor offline ni una API con SLA.
- Piper actual se distribuye como GPL-3.0-or-later. Revisar obligaciones de licencia antes de redistribuir software que lo incorpore.
- Cada modelo de voz tiene sus propios términos. Verificarlos antes de publicar.
- No guardar claves, modelos grandes ni archivos de audio de prueba en el repositorio.
- El uso de esta herramienta corresponde al agente autorizado para producción audiovisual. No modifica el reparto de responsabilidades del contrato CAPCOT.

Referencias oficiales:
- https://github.com/rany2/edge-tts
- https://github.com/OHF-Voice/piper1-gpl
- https://github.com/OHF-Voice/piper1-gpl/blob/main/docs/CLI.md
