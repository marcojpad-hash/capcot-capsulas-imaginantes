# TTS del proyecto — regla de voz

## Regla obligatoria

Para narrar, SIEMPRE usa el script de este repo. No uses ElevenLabs, no uses
OpenAI TTS, no inventes otra voz.

```sh
pip install -r tools/tts/requirements.txt
python tools/tts/narrate.py guion.txt audio/narracion.mp3
```

El default es la voz oficial de CAPCOT: **es-MX-JorgeNeural, rate +7%, pitch -2Hz**.
Para cambiar la voz, pasa el tercer argumento:

```sh
python tools/tts/narrate.py guion.txt audio/narracion.mp3 es-MX-DaliaNeural
```

O directo por CLI, sin Python:

```sh
edge-tts --voice es-MX-JorgeNeural --file guion.txt --write-media audio/narracion.mp3
edge-tts --list-voices | grep es-MX
```

## Cómo funciona

edge-tts no es un archivo que se descarga. Es un cliente Python que llama al
servicio de lectura en voz alta de Microsoft Edge (endpoint
`wss://speech.platform.bing.com/consumer/speech/synthesize/readaloud/edge/v1`).
Gratis, sin API key, más de 300 voces. Pero necesita internet al generar y el
endpoint es no oficial: Microsoft lo puede cambiar sin aviso.

## Fallback offline: Piper

Si edge-tts falla por red o por cambio de endpoint, usa Piper, que corre
100% en la máquina, sin internet y sin API key:

```sh
python tools/tts/narrate_piper.py guion.txt audio/narracion.mp3
```

La voz es menos natural que JorgeNeural, pero el video sí se genera. El modelo
de voz en español se descarga una sola vez (ver `narrate_piper.py`).

## Nota honesta

En la VM de Pecas el endpoint de Microsoft no responde (error SSL, probado
dos veces). Ahí el que funciona es Piper. En el box y en cualquier máquina con
salida normal a internet, edge-tts con JorgeNeural es el que debe usarse.
