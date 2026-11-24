#!/usr/bin/env python3
"""Auditor de programación a partir de snapshots de CAPCOT main.

Lee únicamente miniaturas_auditoria_*.json y rehechos_*.json de un directorio
exportado desde main. No cambia data, programaciones, colas ni publicaciones.
La hora canónica se deriva de publishAt UTC y se contrasta con la hora CDMX
declarada cuando existe. Cada colisión conserva los IDs y archivos de origen.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

LOCAL_TZ = ZoneInfo("America/Mexico_City")
_PROJECT_RE = re.compile(r"(?:^|/)proyectos/([^/]+)(?:/|$)")
_LOCAL_RE = re.compile(r"(?<!\d)(\d{4}-\d{2}-\d{2})[ T]+(\d{1,2}):(\d{2})(?!\d)")


def _parse_utc(value):
    if not isinstance(value, str) or not value.strip():
        return None
    try:
        parsed = datetime.fromisoformat(value.strip().replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def _parse_local_hint(value):
    if not isinstance(value, str):
        return None
    match = _LOCAL_RE.search(value)
    if not match:
        return None
    try:
        naive = datetime.fromisoformat(f"{match.group(1)}T{int(match.group(2)):02d}:{match.group(3)}")
    except ValueError:
        return None
    return naive.replace(tzinfo=LOCAL_TZ)


def _project_id_from_media(value):
    if not isinstance(value, str) or not value.strip():
        return None
    normalized = value.replace("\\", "/")
    match = _PROJECT_RE.search(normalized)
    if match:
        return match.group(1)
    for part in reversed(normalized.split("/")):
        if re.match(r"^\d{4}-\d{2}-\d{2}_.+", part):
            return part
    return None


def _record(*, project_id, video_id, title, publish_at, local_hint,
            state, source_file, source_kind, media_paths=()):
    utc_dt = _parse_utc(publish_at)
    hinted_dt = _parse_local_hint(local_hint)
    if utc_dt is None and hinted_dt is None:
        return None
    derived_local = utc_dt.astimezone(LOCAL_TZ) if utc_dt else None
    local_dt = hinted_dt or derived_local
    mismatch = bool(
        hinted_dt and derived_local
        and hinted_dt.replace(tzinfo=None) != derived_local.replace(tzinfo=None)
    )
    return {
        "fecha": local_dt.date().isoformat(),
        "slot_local": local_dt.strftime("%H:%M"),
        "project_id": str(project_id),
        "video_id": str(video_id) if video_id else None,
        "titulo": str(title) if title else None,
        "publishAt_utc": publish_at,
        "hora_cdmx_declarada": local_hint,
        "estado": state,
        "source_kind": source_kind,
        "source_file": str(source_file),
        "media_paths": [str(x) for x in media_paths if isinstance(x, str) and x.strip()],
        "timestamp_mismatch": mismatch,
    }


def _read_json(path, errors):
    try:
        with path.open(encoding="utf-8") as handle:
            return json.load(handle)
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        errors.append(f"{path}: {type(exc).__name__}: {exc}")
        return None


def _capsule_project_id(capsule):
    for key in ("mp4", "portada"):
        project_id = _project_id_from_media(capsule.get(key))
        if project_id:
            return project_id
    clave = capsule.get("clave")
    if clave:
        return f"rehecho:{clave}"
    youtube = capsule.get("youtube") or {}
    if youtube.get("id"):
        return f"rehecho:{youtube['id']}"
    return None


def load_snapshots(main_data_dir, fecha=None):
    """Devuelve ocupaciones, colisiones y errores exactos sin modificar fuentes."""
    root = Path(main_data_dir)
    errors = []
    records = []
    if not root.is_dir():
        errors.append(f"{root}: FileNotFoundError: no existe directorio de snapshots")
        return {
            "source_dir": str(root), "source_files": [], "ocupaciones": [],
            "conflictos": [], "resumen_por_fecha": [],
            "inconsistencias_timestamp": [], "errores": errors,
            "resumen": {"ocupaciones": 0, "conflictos": 0, "errores": 1},
        }

    snapshot_paths = sorted(root.glob("miniaturas_auditoria_*.json")) + sorted(root.glob("rehechos_*.json"))
    if not snapshot_paths:
        errors.append(f"{root}: NoSnapshotFiles: no se encontraron miniaturas_auditoria_*.json ni rehechos_*.json")
    source_files_read = [path.name for path in snapshot_paths]

    for path in sorted(root.glob("miniaturas_auditoria_*.json")):
        raw = _read_json(path, errors)
        if not isinstance(raw, dict):
            continue
        if "siguen_mal_sin_mp4_no_se_invento" not in raw:
            errors.append(f"{path}: falta clave siguen_mal_sin_mp4_no_se_invento")
            continue
        items = raw.get("siguen_mal_sin_mp4_no_se_invento") or []
        if not isinstance(items, list):
            errors.append(f"{path}: siguen_mal_sin_mp4_no_se_invento no es una lista")
            continue
        for index, item in enumerate(items):
            if not isinstance(item, dict):
                continue
            video_id = item.get("yt_id")
            if not video_id:
                errors.append(f"{path}#siguen_mal_sin_mp4_no_se_invento[{index}]: falta yt_id")
                continue
            row = _record(
                project_id=f"yt:{video_id}",
                video_id=video_id,
                title=item.get("titulo"),
                publish_at=item.get("publishAt"),
                local_hint=item.get("hora_cdmx"),
                state=item.get("estado"),
                source_file=f"{path.name}#siguen_mal_sin_mp4_no_se_invento[{index}]",
                source_kind="miniaturas_auditoria",
                media_paths=(item.get("fileName"),),
            )
            if row:
                records.append(row)
            else:
                errors.append(
                    f"{path}#siguen_mal_sin_mp4_no_se_invento[{index}]: "
                    "publishAt y hora_cdmx ausentes o no interpretables"
                )

        # Colisiones explícitas del snapshot: estos IDs pueden no aparecer en
        # siguen_mal_sin_mp4_no_se_invento porque esa lista solo contiene videos con
        # miniatura/archivo problemático. Omitir este bloque deja fuera publicaciones
        # programadas y hace que la auditoría declare slots libres incorrectamente.
        collisions = raw.get("colisiones_horario_mismo_publishAt") or []
        if not isinstance(collisions, list):
            errors.append(f"{path}: colisiones_horario_mismo_publishAt no es una lista")
        else:
            for collision_index, collision in enumerate(collisions):
                if not isinstance(collision, dict):
                    errors.append(
                        f"{path}#colisiones_horario_mismo_publishAt[{collision_index}]: debe ser objeto"
                    )
                    continue
                videos = collision.get("videos")
                if not isinstance(videos, list) or len(videos) < 2:
                    errors.append(
                        f"{path}#colisiones_horario_mismo_publishAt[{collision_index}]: "
                        "se requieren al menos dos videos"
                    )
                    continue
                for video_index, video in enumerate(videos):
                    if not isinstance(video, dict) or not video.get("yt_id"):
                        errors.append(
                            f"{path}#colisiones_horario_mismo_publishAt[{collision_index}]"
                            f".videos[{video_index}]: falta yt_id"
                        )
                        continue
                    video_id = video["yt_id"]
                    row = _record(
                        project_id=f"yt:{video_id}",
                        video_id=video_id,
                        title=video.get("titulo"),
                        publish_at=collision.get("publishAt"),
                        local_hint=collision.get("hora_cdmx"),
                        state=collision.get("estado"),
                        source_file=(
                            f"{path.name}#colisiones_horario_mismo_publishAt[{collision_index}]"
                            f".videos[{video_index}]"
                        ),
                        source_kind="miniaturas_colision",
                    )
                    if row:
                        records.append(row)
                    else:
                        errors.append(
                            f"{path}#colisiones_horario_mismo_publishAt[{collision_index}]"
                            f".videos[{video_index}]: publishAt y hora_cdmx ausentes o no interpretables"
                        )

    for path in sorted(root.glob("rehechos_*.json")):
        raw = _read_json(path, errors)
        if not isinstance(raw, dict):
            continue
        if "capsulas" not in raw:
            errors.append(f"{path}: falta clave capsulas")
            continue
        capsules = raw.get("capsulas") or []
        if not isinstance(capsules, list):
            errors.append(f"{path}: capsulas no es una lista")
            continue
        for index, capsule in enumerate(capsules):
            if not isinstance(capsule, dict):
                continue
            youtube = capsule.get("youtube") or {}
            if not isinstance(youtube, dict):
                youtube = {}
            video_id = youtube.get("id")
            project_id = _capsule_project_id(capsule)
            if not project_id or not video_id:
                errors.append(
                    f"{path}#capsulas[{index}]: falta project_id derivable o youtube.id"
                )
                continue
            row = _record(
                project_id=project_id,
                video_id=video_id,
                title=capsule.get("titulo") or youtube.get("titulo"),
                publish_at=youtube.get("publishAt_utc"),
                local_hint=capsule.get("programado_CDMX") or youtube.get("hora_cdmx"),
                state=youtube.get("estado"),
                source_file=f"{path.name}#capsulas[{index}]",
                source_kind="rehechos",
                media_paths=(capsule.get("mp4"), capsule.get("portada")),
            )
            if row:
                records.append(row)
            else:
                errors.append(
                    f"{path}#capsulas[{index}]: publishAt_utc y hora local ausentes o no interpretables"
                )

    if fecha:
        records = [row for row in records if row["fecha"] == fecha]

    # Deduplica la misma evidencia repetida en snapshots distintos, conservando fuentes.
    merged = {}
    for row in records:
        key = (row["project_id"], row["video_id"], row["fecha"], row["slot_local"])
        if key not in merged:
            merged[key] = dict(row)
            merged[key]["source_files"] = [row["source_file"]]
        else:
            if row["source_file"] not in merged[key]["source_files"]:
                merged[key]["source_files"].append(row["source_file"])
            merged[key]["timestamp_mismatch"] = (
                merged[key]["timestamp_mismatch"] or row["timestamp_mismatch"]
            )
    occupancies = sorted(
        merged.values(),
        key=lambda row: (row["fecha"], row["slot_local"], row["project_id"], row["video_id"] or ""),
    )

    by_slot = defaultdict(list)
    for row in occupancies:
        by_slot[(row["fecha"], row["slot_local"])].append(row)
    conflicts = []
    for (day, slot), rows in sorted(by_slot.items()):
        identities = {row["video_id"] or row["project_id"] for row in rows}
        if len(identities) > 1:
            conflicts.append({
                "fecha": day,
                "slot_local": slot,
                "video_ids": sorted({row["video_id"] for row in rows if row["video_id"]}),
                "project_ids": sorted({row["project_id"] for row in rows}),
                "evidencia": rows,
            })

    by_date = defaultdict(list)
    for row in occupancies:
        by_date[row["fecha"]].append(row)
    conflicts_by_date = defaultdict(list)
    for conflict in conflicts:
        conflicts_by_date[conflict["fecha"]].append(conflict["slot_local"])
    daily_summary = []
    for day, rows in sorted(by_date.items()):
        daily_summary.append({
            "fecha": day,
            "slots_distintos": sorted({row["slot_local"] for row in rows}),
            "cantidad_slots": len({row["slot_local"] for row in rows}),
            "cantidad_videos": len({row["video_id"] or row["project_id"] for row in rows}),
            "slots_con_colision": sorted(set(conflicts_by_date.get(day, []))),
        })

    return {
        "source_dir": str(root),
        "source_files": source_files_read,
        "ocupaciones": occupancies,
        "conflictos": conflicts,
        "resumen_por_fecha": daily_summary,
        "inconsistencias_timestamp": [row for row in occupancies if row["timestamp_mismatch"]],
        "errores": errors,
        "resumen": {
            "ocupaciones": len(occupancies),
            "conflictos": len(conflicts),
            "errores": len(errors),
        },
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description="Audita slots de snapshots CAPCOT main (solo lectura).")
    parser.add_argument("--main-data-dir", required=True, help="Directorio local con snapshots JSON descargados de main/data/.")
    parser.add_argument("--fecha", help="Limita a YYYY-MM-DD.")
    parser.add_argument("--json", dest="json_path", help="Escribe el resultado JSON en esta ruta; las fuentes no se modifican.")
    args = parser.parse_args(argv)
    result = load_snapshots(args.main_data_dir, args.fecha)
    payload = json.dumps(result, ensure_ascii=False, indent=2)
    if args.json_path:
        Path(args.json_path).write_text(payload + "\n", encoding="utf-8")
    else:
        print(payload)
    return 0 if not result["errores"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
