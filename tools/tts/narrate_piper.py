#!/usr/bin/env python3
"""Fallback offline: narra un guion con Piper TTS (100% local, sin internet, sin API key).

Uso:
    python tools/tts/narrate_piper.py guion.txt audio/narracion.mp3 [modelo.onnx]

El modelo de voz en espanol (es_MX-ald-medium, ~63 MB) se descarga una sola vez
y se guarda en tools/tts/voices/ (o se pasa su ruta como tercer argumento):
    https://huggingface.co/rhasspy/piper-voices/resolve/main/es/es_MX/ald/medium/es_MX-ald-medium.onnx
    https://huggingface.co/rhasspy/piper-voices/resolve/main/es/es_MX/ald/medium/es_MX-ald-medium.onnx.json

Requiere: pip install piper-tts (y ffmpeg si la salida es .mp3).
La voz es menos natural que es-MX-JorgeNeural, pero el video si se genera.
Probado 2026-11-07 en la VM de Pecas: 6,2 s de narracion en espanol, offline.
"""
import subprocess
import sys
from pathlib import Path

DEFAULT_MODEL = Path(__file__).parent / "voices" / "es_MX-ald-medium.onnx"


def main(text_file, out_file, model=str(DEFAULT_MODEL)):
    text = Path(text_file).read_text(encoding="utf-8").strip()
    if not text:
        raise SystemExit("guion vacio: nada que narrar")
    if not Path(model).exists():
        raise SystemExit(f"modelo Piper no encontrado: {model} (ver README.md)")
    out = Path(out_file)
    wav = out.with_suffix(".wav") if out.suffix.lower() == ".mp3" else out
    subprocess.run(
        [sys.executable, "-m", "piper", "--model", model,
         "--output_file", str(wav)],
        input=text, text=True, check=True, capture_output=True,
    )
    if wav != out:
        subprocess.run(
            ["ffmpeg", "-y", "-v", "error", "-i", str(wav), str(out)],
            check=True,
        )
        wav.unlink()
    print(f"OK: {out_file} (Piper offline, modelo {Path(model).name})")


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) < 2:
        print(__doc__)
        raise SystemExit(1)
    main(*args[:3])
