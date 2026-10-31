#!/usr/bin/env python3
"""Audit whether all storyboard-declared image assets exist beside the storyboard."""
import argparse
import json
from pathlib import Path

def audit(storyboard: Path, output: Path | None = None):
    sb = json.loads(storyboard.read_text(encoding="utf-8"))
    root = storyboard.parent
    declared = []
    for scene in sb.get("scenes", []):
        if scene.get("asset_filename"):
            declared.append({"filename": scene["asset_filename"], "scene_id": scene.get("id"), "kind": "frame"})
        layer = scene.get("capa")
        if isinstance(layer, dict) and layer.get("asset_filename"):
            declared.append({"filename": layer["asset_filename"], "scene_id": scene.get("id"), "kind": "layer"})
    # De-duplicate while retaining order.
    unique = {}
    for item in declared:
        unique.setdefault(item["filename"], item)
    present, missing = [], []
    for item in unique.values():
        target = root / item["filename"]
        record = {**item, "resolved_path": str(target)}
        (present if target.is_file() else missing).append(record)
    report = {
        "project_id": sb.get("project_id"),
        "storyboard": str(storyboard),
        "declared_assets": len(unique),
        "present_count": len(present),
        "missing_count": len(missing),
        "visual_review_status": "READY_FOR_REVIEW" if not missing else "BLOCKED_MISSING_MEDIA",
        "present": present,
        "missing": missing,
        "note": "La existencia del archivo no certifica continuidad estética; todos los frames y el audio aún requieren revisión audiovisual.",
    }
    if output:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return report

def main():
    p = argparse.ArgumentParser()
    p.add_argument("storyboard")
    p.add_argument("--output")
    args = p.parse_args()
    audit(Path(args.storyboard), Path(args.output) if args.output else None)

if __name__ == "__main__":
    main()
