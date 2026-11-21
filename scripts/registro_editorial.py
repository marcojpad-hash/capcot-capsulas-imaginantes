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


def _slot_containers(raw):
    containers = []
    pending = [raw]
    seen = set()
    while pending:
        parent = pending.pop(0)
        if not isinstance(parent, dict) or id(parent) in seen:
            continue
        seen.add(id(parent))
        containers.append(parent)
        for value in parent.values():
            if isinstance(value, dict):
                pending.append(value)
            elif isinstance(value, list):
                pending.extend(item for item in value if isinstance(item, dict))
    return containers


def _media_references(raw):
    refs = []
    containers = _slot_containers(raw)
    for container in containers:
        if not isinstance(container, dict):
            continue
        for key in (
            "asset_filename", "asset_path", "video", "video_file", "audio_asset",
            "mp4", "video_path", "audio_path", "frame_path",
        ):
            value = container.get(key)
            if isinstance(value, str) and value.strip() and "://" not in value:
                refs.append(value.strip())
        export = container.get("export")
        if isinstance(export, dict):
            value = export.get("filename")
            if isinstance(value, str) and value.strip() and "://" not in value:
                refs.append(value.strip())
        for key in ("approved_assets", "assets", "archivos"):
            values = container.get(key)
            if isinstance(values, list):
                for item in values:
                    if isinstance(item, str) and item.strip() and "://" not in item:
                        refs.append(item.strip())
                    elif isinstance(item, dict):
                        value = item.get("filename") or item.get("path") or item.get("asset_filename")
                        if isinstance(value, str) and value.strip() and "://" not in value:
                            refs.append(value.strip())
    return list(dict.fromkeys(refs))


def _media_reference_exists(reference, source_path, project_id):
    candidate = Path(reference)
    if candidate.is_absolute():
        return False
    locations = [ROOT / Path(source_path).parent / candidate]
    if project_id:
        locations.extend([
            ROOT / "proyectos" / project_id / candidate,
            ROOT / "cola" / "entrada" / project_id / candidate,
            ROOT / "cola" / "bloqueados" / project_id / candidate,
            ROOT / "salidas" / project_id / candidate,
        ])
    return any(path.exists() for path in locations)


def _local_timestamp(value, assume_utc=False):
    if not isinstance(value, str) or not value.strip():
        return None
    raw = value.strip()
    if not re.search(r"[T ]\d{1,2}:\d{2}", raw):
        return None
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


def _window_from_value(value, source):
    if isinstance(value, dict):
        start = value.get("inicio") or value.get("start")
        end = value.get("fin") or value.get("end")
        label = value.get("id") or value.get("nombre") or source
    else:
        match = re.search(r"(\\d{1,2}:\\d{2})\\s*[-–]\\s*(\\d{1,2}:\\d{2})", str(value or ""))
        if not match:
            return None
        start, end = match.groups()
        label = source
    start_clock, end_clock = _clock_in(str(start or "")), _clock_in(str(end or ""))
    if not start_clock or not end_clock:
        return None
    return {"id": str(label), "inicio": start_clock, "fin": end_clock, "fuente": source}


def _clock_minutes(value):
    clock = _clock_in(str(value or ""))
    if not clock:
        return None
    hour, minute = (int(part) for part in clock.split(":"))
    return hour * 60 + minute


def politica_horaria(fecha=None):
    """Lee la política horaria sin modificarla y expone su fecha de corte."""
    path = ROOT / "data" / "horarios.json"
    raw = _read(path, None)
    if not isinstance(raw, dict):
        return {
            "estado": "POLITICA_NO_DISPONIBLE",
            "source_path": "data/horarios.json",
            "actualizado": None,
            "fecha_politica": None,
            "ventanas_activas": [],
            "ventanas_en_prueba": [],
            "slot_fijo": None,
            "estado_frescura": "NO_VERIFICABLE",
        }

    target = _date(fecha)
    policies = []
    for key, value in raw.items():
        match = re.fullmatch(r"politica_desde_(\\d{4}-\\d{2}-\\d{2})", str(key))
        if match and isinstance(value, dict):
            policies.append((match.group(1), key, value))
    applicable = [item for item in policies if not target or item[0] <= target]
    selected = max(applicable or policies, key=lambda item: item[0]) if policies else None
    policy_date, policy_key, policy = selected if selected else (None, None, {})
    active_values = policy.get("ventanas")
    if not isinstance(active_values, list) or not active_values:
        active_values = raw.get("ventanas", [])
    active_windows = [
        window for index, value in enumerate(active_values)
        if (window := _window_from_value(value, f"ventana_{index + 1}")) is not None
    ]
    test_values = policy.get("ventanas_en_prueba", raw.get("ventanas_en_prueba", []))
    test_windows = [
        window for index, value in enumerate(test_values if isinstance(test_values, list) else [])
        if (window := _window_from_value(value, f"prueba_{index + 1}")) is not None
    ]

    fixed_value = (
        policy.get("slot_fijo_dato") or policy.get("slot_fijo")
        or raw.get("slot_fijo_dato")
    )
    if isinstance(fixed_value, dict):
        fixed_value = (
            fixed_value.get("hora") or fixed_value.get("slot_local")
            or fixed_value.get("slot")
        )
    fixed_slot = _clock_in(str(fixed_value or ""))

    updated = _date(raw.get("actualizado"))
    if not selected and active_windows:
        policy_date = updated
    if target and policy_date:
        freshness = (
            "CORTE_ANTERIOR_A_FECHA_OBJETIVO" if target > policy_date
            else "OBJETIVO_ANTERIOR_A_POLITICA" if target < policy_date
            else "AL_CORTE"
        )
    else:
        freshness = "SIN_FECHA_OBJETIVO" if not target else "SIN_CORTE"
    status = "CARGADA" if active_windows or test_windows or fixed_slot else "SIN_VENTANAS"
    return {
        "estado": status,
        "source_path": "data/horarios.json",
        "actualizado": updated,
        "fecha_politica": policy_date,
        "policy_key": policy_key,
        "zona_horaria": raw.get("zona_horaria"),
        "ventanas_activas": active_windows,
        "ventanas_en_prueba": test_windows,
        "slot_fijo": fixed_slot,
        "estado_frescura": freshness,
    }


def _clasificar_ventana(slot_local, policy):
    clock = _clock_in(str(slot_local or ""))
    if not clock or policy.get("estado") != "CARGADA":
        return "POLITICA_NO_DISPONIBLE"
    if clock == policy.get("slot_fijo"):
        return "SLOT_FIJO"
    minute = _clock_minutes(clock)
    for window in policy.get("ventanas_en_prueba", []):
        start, end = _clock_minutes(window["inicio"]), _clock_minutes(window["fin"])
        if start is not None and end is not None and start <= minute < end:
            return "VENTANA_EN_PRUEBA"
    for window in policy.get("ventanas_activas", []):
        start, end = _clock_minutes(window["inicio"]), _clock_minutes(window["fin"])
        if start is not None and end is not None and start <= minute < end:
            return "VENTANA_REGULAR"
    return "FUERA_DE_VENTANA"


def _slot_evidence(raw, source_path, default_project_id=None):
    """Normaliza una evidencia de fecha/slot sin convertirla en publicación confirmada."""
    if not isinstance(raw, dict):
        return None

    containers = _slot_containers(raw)
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
    timestamp_local = local_dt.isoformat(timespec="minutes") if local_dt else None
    timestamp_mismatch = bool(
        local_dt and (
            (fecha and fecha != local_dt.date().isoformat())
            or (slot_local and slot_local != local_dt.strftime("%H:%M"))
        )
    )
    if local_dt:
        fecha = fecha or local_dt.date().isoformat()
        slot_local = slot_local or local_dt.strftime("%H:%M")
    fecha = fecha or _date_in(str(pid))
    if not fecha or not slot_local:
        return None

    video_id, _ = _pick_field(
        containers, ("yt_id", "video_id", "youtube_id", "id_video")
    )
    platform_containers = [
        container for container in containers
        if isinstance(container, dict) and any(
            key in container for key in (
                "privacyStatus", "publishAt", "publishedAt", "channelId",
                "kind", "post_id", "video_id",
            )
        )
    ]
    if not video_id:
        video_id, _ = _pick_field(platform_containers, ("id",))
    state_value, _ = _pick_field(
        containers, ("estado", "status", "publication_status", "privacyStatus", "privacy")
    )
    state_text = str(state_value or "").strip().lower()
    path_text = "/" + str(source_path).replace("\\", "/").strip("/") + "/"
    published_at, _ = _pick_field(
        containers,
        ("published_at", "publishedAt", "yt_published_at",
         "tiktok_published_at", "facebook_published_at"),
    )
    media_refs = _media_references(raw)
    missing_media = [
        ref for ref in media_refs
        if not _media_reference_exists(ref, source_path, str(pid))
    ]

    if published_at or "publicado" in state_text or "published" in state_text:
        evidence_state = "PUBLICACION_REGISTRADA"
    elif video_id and timestamp_value:
        evidence_state = "PROGRAMADO_CON_VIDEO_ID"
    elif str(source_path).endswith("data/publicaciones.json") and video_id:
        evidence_state = "PUBLICACION_REGISTRADA"
    elif timestamp_value or "programad" in state_text or "scheduled" in state_text:
        evidence_state = "PROGRAMADO_DECLARADO"
    elif video_id:
        evidence_state = "VIDEO_ID_REGISTRADO"
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
        "timestamp_local": timestamp_local,
        "timestamp_mismatch": timestamp_mismatch,
        "media_references": media_refs,
        "missing_media_references": missing_media,
        "media_status": (
            "MEDIOS_NO_VERIFICADOS_EN_REPOSITORIO" if missing_media
            else "VERIFICADOS_EN_REPOSITORIO" if media_refs
            else "SIN_REFERENCIAS"
        ),
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

    # Los snapshots diarios son evidencia de slots programados/publicados;
    # se leen, pero nunca se modifican. Los slots sin ID son ventanas vacías.
    for path in sorted(data.glob("horario_*.json")):
        raw = _read(path, None)
        if not isinstance(raw, dict):
            continue
        for group in ("slots", "atrasados_revisados"):
            items = raw.get(group, [])
            if not isinstance(items, list):
                continue
            for index, item in enumerate(items):
                if not isinstance(item, dict):
                    continue
                project_id = item.get("project_id") or item.get("id") or item.get("proyecto")
                if not project_id:
                    continue
                merged = dict(raw)
                merged.update(item)
                merged["project_id"] = project_id
                if group == "atrasados_revisados" and item.get("hora_original"):
                    merged["fecha"] = _date(item.get("hora_original")) or item.get("fecha") or raw.get("fecha")
                    merged["hora_local"] = item.get("hora_original")
                else:
                    merged["fecha"] = item.get("fecha") or raw.get("fecha") or _date_in(path.stem)
                source = f"{path.relative_to(ROOT)}#{group}[{index}]"
                rec = _slot_evidence(merged, source)
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
    policy = politica_horaria(fecha)
    for row in evidence:
        row["coincidencia_horaria"] = _clasificar_ventana(row["slot_local"], policy)
        row["estado_frescura_horaria"] = policy["estado_frescura"]
        row["fecha_politica_horaria"] = policy["fecha_politica"]
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
    timestamp_mismatches = [
        row for row in evidence if row.get("timestamp_mismatch")
    ]

    return {
        "ocupaciones": evidence,
        "conflictos": conflicts,
        "discrepancias_por_project_id": discrepancies,
        "inconsistencias_timestamp": timestamp_mismatches,
        "politica_horaria": policy,
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
