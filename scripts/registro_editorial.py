#!/usr/bin/env python3
"""Vista reconciliada de rotación CAPCOT sin modificar data/*.json.

Une los registros canónicos con storyboards de cola, proyectos, bloqueados y salidas.
Los archivos de cola/proyecto cuentan como evidencia de tema/estilo/estructura
aunque todavía no equivalgan a una publicación.
"""
from pathlib import Path
import json
import re
import datetime
from zoneinfo import ZoneInfo

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
        "origen": raw.get("origen") or ("externa" if source in {"cola", "bloqueado"} else "propia"),
        "estado": raw.get("estado") or raw.get("status"),
        "_source": source,
    }

def _storyboard_paths():
    patterns = (
        ROOT / "proyectos",
        ROOT / "cola" / "entrada",
        ROOT / "cola" / "bloqueados",
        ROOT / "cola",
        ROOT / "salidas",
    )
    found = set()
    for base in patterns:
        if not base.exists():
            continue
        # Recorre cualquier profundidad: hay paquetes heredados anidados
        # más de un nivel bajo cola/entrada, cola/bloqueados y salidas.
        for p in base.rglob("storyboard.json"):
            if "pendiente" in p.parts:
                continue
            found.add(p)
        if base.name in {"entrada", "bloqueados"}:
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
    if "bloqueados" in path.parts:
        source, default_origin = "bloqueado", "externa"
    elif "entrada" in path.parts:
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

def handoffs_grok_inbox():
    """Inventario separado de markers; un marker pending nunca confirma recepción Grok."""
    base = ROOT / "handoffs" / "grok_inbox"
    if not base.exists():
        return []
    rows = []
    for path in sorted(base.rglob("*.json")):
        marker = _read(path, None)
        if not isinstance(marker, dict):
            continue
        pid = marker.get("project_id") or path.stem
        rows.append({
            "project_id": str(pid),
            "event": marker.get("event"),
            "status": marker.get("status") or "unknown",
            "created_at": marker.get("created_at"),
            "branch": marker.get("branch"),
            "commit_sha": marker.get("commit_sha"),
            "package_path": marker.get("package_path"),
            "marker_path": str(path.relative_to(ROOT)),
            "receipt_confirmed": False,
            "receipt_rule": "Solo cola/estado/<project_id>.json confirma recepción Grok.",
        })
    return rows


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
                # El origen describe de dónde entró el paquete; una copia posterior
                # en proyectos/ o salidas/ no convierte una entrada externa en propia.
                if key == "origen" and target.get("origen") == "externa" and value == "propia":
                    continue
                target[key] = value
    result = list(merged.values()) + anonymous
    return sorted(result, key=lambda x: (x.get("fecha") or "", x.get("project_id") or ""))

def registros_dia(fecha):
    return [r for r in registros() if r.get("fecha") == fecha]

def temas_dia(fecha):
    """Temas canónicos + temas de cola/proyectos/bloqueados; nunca escribe data/temas_del_dia.json."""
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



LOCAL_TZ = ZoneInfo("America/Mexico_City")
_SLOT_RE = re.compile(r"(?<!\d)([01]?\d|2[0-3]):([0-5]\d)(?!\d)")
_DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}")
_SLOT_FILES = {
    "storyboard.json", "programacion.json", "metadata.json", "resumen.json",
    "publication.json", "publicacion.json", "youtube.json", "tiktok.json",
    "facebook.json", "estado.json",
}


def _project_id_from_path(path):
    for part in reversed(Path(path).parts):
        if re.match(r"^\d{4}-\d{2}-\d{2}_.+", part):
            return part
    return None


def _pick_field(containers, keys):
    for container in containers:
        if not isinstance(container, dict):
            continue
        for key in keys:
            value = container.get(key)
            if value not in EMPTY:
                return value, key
    return None, None


def _local_timestamp(value, assume_utc=False):
    if not isinstance(value, str) or not value.strip():
        return None
    raw = value.strip()
    try:
        parsed = datetime.datetime.fromisoformat(raw.replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(
            tzinfo=datetime.timezone.utc if assume_utc else LOCAL_TZ
        )
    return parsed.astimezone(LOCAL_TZ)


def _date_in(value):
    if not isinstance(value, str):
        return None
    match = _DATE_RE.search(value)
    return match.group(0) if match else None


def _clock_in(value):
    if not isinstance(value, str):
        return None
    match = _SLOT_RE.search(value)
    if not match:
        return None
    return f"{int(match.group(1)):02d}:{match.group(2)}"


def _slot_evidence(raw, source_path, default_project_id=None):
    """Normaliza una evidencia de fecha/slot sin convertirla en publicación confirmada."""
    if not isinstance(raw, dict):
        return None

    publicacion = raw.get("publicacion") or raw.get("publication") or {}
    programacion = raw.get("programacion") or raw.get("schedule") or {}
    containers = [raw, publicacion, programacion]
    pid = (
        raw.get("project_id") or raw.get("id") or raw.get("proyecto")
        or default_project_id or _project_id_from_path(source_path)
    )
    if not pid:
        return None

    date_value, date_key = _pick_field(
        containers,
        ("fecha_objetivo", "fecha", "target_date", "publication_date",
         "published_date", "date"),
    )
    clock_value, clock_key = _pick_field(
        containers,
        ("slot_local", "hora_cdmx", "hora_local", "slot", "time_local",
         "scheduled_time", "hora"),
    )
    timestamp_value, timestamp_key = _pick_field(
        containers,
        ("publish_at", "publishAt", "publishAt_utc", "publish_at_utc",
         "scheduled_at", "scheduledAt", "published_at", "publishedAt"),
    )

    local_dt = _local_timestamp(
        timestamp_value,
        assume_utc=bool(timestamp_key and timestamp_key.lower().endswith("_utc")),
    )
    fecha = _date_in(date_value) or _date_in(clock_value)
    slot_local = _clock_in(clock_value)
    if local_dt:
        fecha = fecha or local_dt.date().isoformat()
        slot_local = slot_local or local_dt.strftime("%H:%M")
    fecha = fecha or _date_in(str(pid))
    if not fecha or not slot_local:
        return None

    video_id, _ = _pick_field(
        containers, ("yt_id", "video_id", "youtube_id", "id_video")
    )
    state_value, _ = _pick_field(containers, ("estado", "status", "publication_status"))
    state_text = str(state_value or "").strip().lower()
    path_text = "/" + str(source_path).replace("\\", "/").strip("/") + "/"

    if video_id or "publicado" in state_text or "published" in state_text:
        evidence_state = "PUBLICADO_O_ID_REGISTRADO"
    elif timestamp_value or "programad" in state_text or "scheduled" in state_text:
        evidence_state = "PROGRAMADO_DECLARADO"
    elif "/estado/" in path_text:
        evidence_state = "ESTADO_GROK"
    elif "/bloqueados/" in path_text:
        evidence_state = "BLOQUEADO"
    elif "/entrada/" in path_text:
        evidence_state = "EN_COLA"
    elif "/salidas/" in path_text:
        evidence_state = "SALIDA_EN_REPOSITORIO"
    elif "/proyectos/" in path_text:
        evidence_state = "PROPUESTA_EN_PROYECTOS"
    elif str(source_path).endswith("data/rotacion.json"):
        evidence_state = "ROTACION_REGISTRADA"
    elif str(source_path).endswith("data/cola.json"):
        evidence_state = "REGISTRO_DE_COLA"
    else:
        evidence_state = "EVIDENCIA_DE_SLOT"

    trend = raw.get("trend_source") or {}
    return {
        "fecha": fecha,
        "slot_local": slot_local,
        "project_id": str(pid),
        "tema": raw.get("tema") or raw.get("topic") or raw.get("title")
                or raw.get("titulo") or (trend.get("termino") if isinstance(trend, dict) else None),
        "estado_evidencia": evidence_state,
        "estado_fuente": state_value,
        "video_id": str(video_id) if video_id else None,
        "publish_at": timestamp_value,
        "source_path": str(source_path),
        "date_field": date_key,
        "slot_field": clock_key,
        "timestamp_field": timestamp_key,
    }


def ocupacion_slots(fecha=None):
    """Inventario de ocupación por fecha/slot y discrepancias entre evidencias.

    Lee los JSON canónicos y sidecars del árbol actual. No escribe archivos y no
    trata un marker de handoff como recepción Grok ni una propuesta como publicación.
    """
    evidence = []
    data = ROOT / "data"
    for filename in ("publicaciones.json", "rotacion.json", "cola.json"):
        path = data / filename
        raw = _read(path, [])
        if isinstance(raw, list):
            for item in raw:
                rec = _slot_evidence(item, path.relative_to(ROOT))
                if rec:
                    evidence.append(rec)

    for base in (ROOT / "proyectos", ROOT / "cola", ROOT / "salidas"):
        if not base.exists():
            continue
        for path in sorted(base.rglob("*.json")):
            if path.name not in _SLOT_FILES:
                continue
            raw = _read(path, None)
            rec = _slot_evidence(
                raw,
                path.relative_to(ROOT),
                default_project_id=_project_id_from_path(path),
            )
            if rec:
                evidence.append(rec)

    evidence = [
        row for row in evidence
        if not fecha or row["fecha"] == fecha
    ]
    evidence.sort(
        key=lambda row: (
            row["fecha"], row["slot_local"], row["project_id"], row["source_path"]
        )
    )

    by_slot = {}
    by_project = {}
    for row in evidence:
        slot_key = (row["fecha"], row["slot_local"])
        by_slot.setdefault(slot_key, {}).setdefault(row["project_id"], []).append(row)
        by_project.setdefault(row["project_id"], set()).add(slot_key)

    conflicts = []
    for (day, slot), projects in sorted(by_slot.items()):
        if len(projects) > 1:
            conflicts.append({
                "fecha": day,
                "slot_local": slot,
                "project_ids": sorted(projects),
                "evidence_count": sum(len(rows) for rows in projects.values()),
                "evidence": [
                    row for project_rows in projects.values() for row in project_rows
                ],
            })

    discrepancies = []
    for pid, slots in sorted(by_project.items()):
        if len(slots) > 1:
            discrepancies.append({
                "project_id": pid,
                "slots": [
                    {"fecha": day, "slot_local": slot}
                    for day, slot in sorted(slots)
                ],
                "evidence": [row for row in evidence if row["project_id"] == pid],
            })

    return {
        "ocupaciones": evidence,
        "conflictos": conflicts,
        "discrepancias_por_project_id": discrepancies,
    }

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Vista reconciliada de rotación CAPCOT (solo lectura).")
    parser.add_argument("--fecha", help="Limitar la vista a YYYY-MM-DD.")
    args = parser.parse_args()
    handoffs = handoffs_grok_inbox()
    if args.fecha:
        handoffs = [row for row in handoffs if _date(row.get("project_id")) == args.fecha]
    payload = {
        "registros": registros_dia(args.fecha) if args.fecha else registros(),
        "handoffs_grok_inbox": handoffs,
        "ocupacion_slots": ocupacion_slots(args.fecha),
    }
    if args.fecha:
        payload["temas_del_dia"] = temas_dia(args.fecha)
    print(json.dumps(payload, ensure_ascii=False, indent=2))
