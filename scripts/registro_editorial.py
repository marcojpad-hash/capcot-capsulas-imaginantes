#!/usr/bin/env python3
"""Vista reconciliada de rotación CAPCOT sin modificar data/*.json.

Une los registros canónicos con storyboards de cola, proyectos y salidas.
Los archivos de cola/proyecto cuentan como evidencia de tema/estilo/estructura
aunque todavía no equivalgan a una publicación.
"""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
EMPTY = (None, "", [], {})

def _read(path, default):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError, TypeError):
        return default

def _date(value):
    m = re.match(r"^(\d{4}-\d{2}-\d{2})", str(value or ""))
    return m.group(1) if m else None

def _normal_record(raw, source):
    if not isinstance(raw, dict):
        return None
    pid = raw.get("project_id") or raw.get("id") or raw.get("proyecto")
    theme = raw.get("tema") or raw.get("topic") or raw.get("title")
    if not pid and not theme:
        return None
    return {
        "fecha": _date(raw.get("fecha") or pid),
        "project_id": str(pid) if pid else None,
        "tema": theme,
        "estructura": raw.get("estructura"),
        "estilo": raw.get("estilo") or raw.get("estilo_id"),
        "cama": raw.get("cama") or raw.get("cama_musical"),
        "duracion": raw.get("duracion") or raw.get("target_duration_seconds"),
        "origen": raw.get("origen") or ("externa" if source == "cola" else "propia"),
        "estado": raw.get("estado") or raw.get("status"),
        "_source": source,
    }

def _storyboard_paths():
    patterns = (
        ROOT / "proyectos",
        ROOT / "cola" / "entrada",
        ROOT / "cola",
        ROOT / "salidas",
    )
    found = set()
    for base in patterns:
        if not base.exists():
            continue
        for p in base.glob("*/storyboard.json"):
            if "pendiente" in p.parts:
                continue
            found.add(p)
        if base.name == "entrada":
            for p in base.glob("*.json"):
                found.add(p)
    return sorted(found, key=lambda p: str(p))

def _storyboard_record(path):
    sb = _read(path, None)
    if not isinstance(sb, dict):
        return None
    pid = sb.get("project_id") or path.parent.name or path.stem
    trend = sb.get("trend_source") or {}
    audio = sb.get("audio") or {}
    music = audio.get("cama_musical") or audio.get("music_asset")
    if isinstance(music, str) and music.startswith("sintetico:"):
        music = music.split(":", 1)[1]
    duration = sum(float(s.get("duration_seconds", 0) or 0) for s in sb.get("scenes", []) if isinstance(s, dict))
    duration += float((sb.get("cortinilla_fuentes") or {}).get("duration_seconds", 0) or 0)
    if "entrada" in path.parts:
        source, default_origin = "cola", "externa"
    elif "proyectos" in path.parts:
        source, default_origin = "proyecto", "propia"
    else:
        source, default_origin = "salida", sb.get("origen") or "propia"
    return {
        "fecha": _date(pid) or _date(path.parent.name) or _date(path.name),
        "project_id": str(pid),
        "tema": trend.get("termino") or sb.get("title") or sb.get("titulo"),
        "estructura": sb.get("estructura"),
        "estilo": sb.get("estilo_id"),
        "cama": music,
        "duracion": duration or sb.get("target_duration_seconds"),
        "origen": sb.get("origen") or default_origin,
        "estado": sb.get("estado") or sb.get("editorial_status") or "storyboard_en_repo",
        "_source": source,
        "_path": str(path.relative_to(ROOT)),
    }

def registros():
    """Registros unidos por project_id; la evidencia de storyboard completa campos faltantes."""
    data = ROOT / "data"
    rows = []
    for filename, source in (
        ("rotacion.json", "rotacion"),
        ("publicaciones.json", "publicacion"),
        ("cola.json", "cola"),
    ):
        raw = _read(data / filename, [])
        if isinstance(raw, list):
            for item in raw:
                rec = _normal_record(item, source)
                if rec:
                    if source == "cola" and str(rec.get("estado") or "").lower() in {"rechazado", "invalido", "invalid", "rejected"}:
                        continue
                    rows.append(rec)
    for path in _storyboard_paths():
        rec = _storyboard_record(path)
        if rec:
            rows.append(rec)

    merged = {}
    anonymous = []
    for rec in rows:
        pid = rec.get("project_id")
        if not pid:
            anonymous.append(rec)
            continue
        target = merged.setdefault(pid, {})
        for key, value in rec.items():
            if value not in EMPTY:
                target[key] = value
    result = list(merged.values()) + anonymous
    return sorted(result, key=lambda x: (x.get("fecha") or "", x.get("project_id") or ""))

def registros_dia(fecha):
    return [r for r in registros() if r.get("fecha") == fecha]

def temas_dia(fecha):
    """Temas canónicos + temas de cola/proyectos; nunca escribe data/temas_del_dia.json."""
    raw = _read(ROOT / "data" / "temas_del_dia.json", {})
    base = raw.get(fecha, []) if isinstance(raw, dict) else []
    out = []
    seen = set()
    for item in base:
        if not isinstance(item, dict):
            continue
        pid = item.get("project_id")
        key = (str(pid), str(item.get("tema") or "").strip().lower())
        if key not in seen:
            out.append(dict(item))
            seen.add(key)
    for rec in registros_dia(fecha):
        pid, theme = rec.get("project_id"), rec.get("tema")
        if not theme:
            continue
        key = (str(pid), str(theme).strip().lower())
        if key not in seen:
            out.append({"tema": str(theme).lower(), "origen": rec.get("origen"), "project_id": pid, "registro": rec.get("_source")})
            seen.add(key)
    return out

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Vista reconciliada de rotación CAPCOT (solo lectura).")
    parser.add_argument("--fecha", help="Limitar la vista a YYYY-MM-DD.")
    args = parser.parse_args()
    payload = {"registros": registros_dia(args.fecha) if args.fecha else registros()}
    if args.fecha:
        payload["temas_del_dia"] = temas_dia(args.fecha)
    print(json.dumps(payload, ensure_ascii=False, indent=2))
