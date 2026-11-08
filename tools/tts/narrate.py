#!/usr/bin/env python3
"""CAPCOT TTS: Edge TTS online, Piper local fallback.

The repository stores this client, not installed packages or voice-model binaries.
Piper fallback is activated only when --piper-model is supplied (or PIPER_MODEL is set).
"""
from __future__ import annotations

import argparse
import asyncio
import os
import shutil
import subprocess
import sys
from pathlib import Path


DEFAULT_VOICE = "es-MX-JorgeNeural"


async def edge_synthesize(text: str, output: Path, voice: str) -> None:
    try:
        import edge_tts
    except ImportError as exc:
        raise RuntimeError(
            "Falta edge-tts. Instala: python -m pip install -r tools/tts/requirements-edge.txt"
        ) from exc
    await edge_tts.Communicate(text, voice).save(str(output))


def piper_synthesize(text: str, output: Path, model: Path) -> Path:
    executable = shutil.which("piper")
    if not executable:
        raise RuntimeError(
            "Piper no está instalado. Instala tools/tts/requirements-piper.txt."
        )
    if not model.is_file():
        raise RuntimeError(f"No existe el modelo Piper configurado: {model}")
    actual_output = output if output.suffix.lower() == ".wav" else output.with_suffix(".wav")
    subprocess.run(
        [executable, "--model", str(model), "--output_file", str(actual_output)],
        input=text,
        text=True,
        check=True,
        capture_output=True,
    )
    return actual_output


def synthesize(text: str, output: Path, voice: str, engine: str, piper_model: str | None) -> tuple[Path, str]:
    output.parent.mkdir(parents=True, exist_ok=True)
    if not text.strip():
        raise ValueError("El texto de entrada está vacío.")

    if engine in ("auto", "edge"):
        try:
            asyncio.run(edge_synthesize(text, output, voice))
            if not output.is_file() or output.stat().st_size == 0:
                raise RuntimeError("Edge TTS no produjo un archivo de audio válido.")
            return output, "edge-tts"
        except Exception as exc:
            output.unlink(missing_ok=True)
            if engine == "edge" or not piper_model:
                raise RuntimeError(
                    f"Edge TTS falló ({type(exc).__name__}: {exc}). "
                    "Para permitir respaldo local, configura --piper-model o PIPER_MODEL."
                ) from exc
            print(
                f"AVISO: Edge TTS falló; se activa Piper local de forma explícita. Motivo: {exc}",
                file=sys.stderr,
            )

    if engine == "piper" and not piper_model:
        raise RuntimeError("Para --engine piper debes indicar --piper-model o PIPER_MODEL.")

    model = Path(piper_model).expanduser() if piper_model else None
    if model is None:
        raise RuntimeError("No hay modelo Piper configurado.")
    actual_output = piper_synthesize(text, output, model)
    if not actual_output.is_file() or actual_output.stat().st_size == 0:
        raise RuntimeError("Piper no produjo un archivo WAV válido.")
    return actual_output, "piper-local"


def main() -> int:
    parser = argparse.ArgumentParser(description="Genera narración con Edge TTS y respaldo Piper.")
    parser.add_argument("text_file", help="Archivo UTF-8 con el guion.")
    parser.add_argument("output_file", help="Salida .mp3 (Edge) o .wav (Piper).")
    parser.add_argument("--voice", default=DEFAULT_VOICE, help=f"Voz Edge TTS (default: {DEFAULT_VOICE}).")
    parser.add_argument("--engine", choices=("auto", "edge", "piper"), default="auto")
    parser.add_argument("--piper-model", default=os.environ.get("PIPER_MODEL"))
    args = parser.parse_args()

    try:
        text = Path(args.text_file).read_text(encoding="utf-8")
        output, provider = synthesize(
            text, Path(args.output_file), args.voice, args.engine, args.piper_model
        )
        print(f"OK provider={provider} output={output}")
        return 0
    except Exception as exc:
        print(f"ERROR TTS: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
