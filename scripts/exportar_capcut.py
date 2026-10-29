#!/usr/bin/env python3
"""Exporta CAPCUT_IMPORT.json a subtítulos SRT y plan CSV para CapCut Web/Desktop.

Los tiempos de los subtítulos son estimaciones distribuidas por palabras dentro
de cada escena. Para sincronía palabra a palabra, reemplazar con tiempos del TTS.
No crea un proyecto nativo ni usa APIs privadas de CapCut.
"""
from __future__ import annotations
import argparse
import csv
import json
import re
from pathlib import Path


def stamp(seconds: float) -> str:
    ms = max(0, round(seconds * 1000))
    hours, ms = divmod(ms, 3_600_000)
    minutes, ms = divmod(ms, 60_000)
    secs, ms = divmod(ms, 1000)
    return f"{hours:02}:{minutes:02}:{secs:02},{ms:03}"


def word_count(text: str) -> int:
    return max(1, len(re.findall(r"\S+", text.strip())))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=Path(
        "cola/entrada/2026-10-28_mosquito-fruitless-audicion/CAPCUT_IMPORT.json"))
    parser.add_argument("--out-dir", type=Path, default=None)
    args = parser.parse_args()
    source = args.input
    data = json.loads(source.read_text(encoding="utf-8"))
    if data.get("format") != "CAPCOT_EDIT_SPEC_NOT_NATIVE_CAPCUT":
        raise SystemExit("Formato no reconocido; no se generó ningún archivo.")
    scenes = data.get("scenes")
    if not isinstance(scenes, list) or not scenes:
        raise SystemExit("El manifiesto no contiene escenas.")

    out_dir = args.out_dir or source.parent
    out_dir.mkdir(parents=True, exist_ok=True)
    srt_path = out_dir / "CAPCUT_SUBTITULOS.srt"
    csv_path = out_dir / "CAPCUT_PLAN_MONTAJE.csv"
    cursor = 0.0
    subtitles: list[str] = []
    rows: list[dict[str, str]] = []
    subtitle_id = 1

    for scene in scenes:
        duration = float(scene["duration_seconds"])
        blocks = scene.get("caption_blocks") or [scene.get("narration", "")]
        weights = [word_count(str(block)) for block in blocks]
        total_weight = sum(weights)
        local = 0.0
        start = cursor
        for block, weight in zip(blocks, weights):
            span = duration * weight / total_weight
            begin = cursor + local
            end = cursor + local + span
            if str(block).strip():
                subtitles.extend([
                    str(subtitle_id),
                    f"{stamp(begin)} --> {stamp(end)}",
                    str(block).strip(),
                    "",
                ])
                subtitle_id += 1
            local += span
        rows.append({
            "order": str(scene.get("order", "")),
            "start_seconds": f"{start:.3f}",
            "duration_seconds": f"{duration:.3f}",
            "end_seconds": f"{cursor + duration:.3f}",
            "asset": str(scene.get("asset", "")),
            "on_screen_text": str(scene.get("on_screen_text", "")),
            "motion": str(scene.get("motion", "")),
            "narration": str(scene.get("narration", "")),
            "layer_json": json.dumps(scene.get("layer"), ensure_ascii=False),
        })
        cursor += duration

    slate = data.get("source_slate", {})
    slate_duration = float(slate.get("duration_seconds", 0))
    rows.append({
        "order": "FUENTES",
        "start_seconds": f"{cursor:.3f}",
        "duration_seconds": f"{slate_duration:.3f}",
        "end_seconds": f"{cursor + slate_duration:.3f}",
        "asset": "",
        "on_screen_text": str(slate.get("titulo", "Fuentes")),
        "motion": "still",
        "narration": "",
        "layer_json": json.dumps(slate, ensure_ascii=False),
    })

    srt_path.write_text("\n".join(subtitles).rstrip() + "\n", encoding="utf-8")
    with csv_path.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    print(f"SRT: {srt_path} ({subtitle_id - 1} bloques; tiempos estimados)")
    print(f"Plan: {csv_path} ({len(rows)} filas; duración total {cursor + slate_duration:.1f} s)")
    print("Nota: no se creó un proyecto nativo de CapCut ni se afirmó sincronía exacta.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
