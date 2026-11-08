#!/usr/bin/env python3
"""Narra un guion con edge-tts (Microsoft Edge Read-Aloud, gratis, sin API key).

Uso:
    python tools/tts/narrate.py guion.txt audio/narracion.mp3 [voz] [rate] [pitch]

Defaults CAPCOT: voz es-MX-JorgeNeural, rate +7%, pitch -2Hz.
Requiere internet: edge-tts llama a wss://speech.platform.bing.com/... (endpoint no oficial).
Si falla por red o por cambio de endpoint, usa el fallback offline:
    python tools/tts/narrate_piper.py guion.txt audio/narracion.mp3
(ver README.md en esta misma carpeta).
"""
import asyncio
import sys

import edge_tts

DEFAULT_VOICE = "es-MX-JorgeNeural"
DEFAULT_RATE = "+7%"
DEFAULT_PITCH = "-2Hz"


async def main(text_file, out_file, voice=DEFAULT_VOICE, rate=DEFAULT_RATE, pitch=DEFAULT_PITCH):
    with open(text_file, encoding="utf-8") as f:
        text = f.read().strip()
    if not text:
        raise SystemExit("guion vacio: nada que narrar")
    communicate = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
    await communicate.save(out_file)
    print(f"OK: {out_file} ({voice}, rate {rate}, pitch {pitch})")


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) < 2:
        print(__doc__)
        raise SystemExit(1)
    asyncio.run(main(*args[:5]))
