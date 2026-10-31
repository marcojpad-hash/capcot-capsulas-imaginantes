#!/usr/bin/env python3
"""Valida el contrato textual CAPCOT y, en producción, los assets ya generados.

Uso:
  python3 scripts/validar_storyboard.py cola/entrada/AAAA-MM-DD_slug.json
  python3 scripts/validar_storyboard.py salidas/AAAA-MM-DD_slug/storyboard.json --check-doi
La etapa de preproducción no requiere ni acepta rutas de assets inexistentes.
"""
import json
import os
import re
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARC = ["hook_medias_res", "desarrollo", "cierre_historia", "reflexion_o_pregunta"]
VOICE = {"engine": "edge-tts", "voice_id": "es-MX-JorgeNeural", "language": "es-MX", "rate": "+7%", "pitch": "-2Hz"}

def check_doi(doi):
    try:
        req = urllib.request.Request(
            "https://api.crossref.org/works/" + doi,
            headers={"User-Agent": "capcot-validador/2.0"}
        )
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status == 200
    except Exception:
        return False

def words(text):
    return re.findall(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ0-9]+(?:['’.-][A-Za-zÁÉÍÓÚÜÑáéíóúüñ0-9]+)*", text or "")

def validar(path, doi=False):
    errs, warns = [], []
    with open(path, encoding="utf-8") as f:
        sb = json.load(f)
    base = os.path.dirname(os.path.abspath(path))
    mode = sb.get("production_mode", "storyboard_only")
    required = [
        "project_id", "serie", "title", "titulo", "language", "aspect_ratio",
        "target_duration_seconds", "estructura", "trend_source", "estilo_id",
        "visual_identity", "typography_identity", "voice", "sources", "scenes",
        "cortinilla_fuentes", "audio", "export", "publicacion"
    ]
    for key in required:
        if key not in sb:
            errs.append(f"falta campo raíz: {key}")
    if errs:
        return errs, warns

    if sb["serie"] != "Datos y ociosidades":
        errs.append("serie debe ser exactamente 'Datos y ociosidades'")
    if sb["language"] != "es-MX":
        errs.append("language debe ser es-MX")
    if sb["aspect_ratio"] != "9:16":
        errs.append("aspect_ratio debe ser 9:16")
    if sb["export"].get("resolution") != "1080x1920":
        errs.append("export.resolution debe ser 1080x1920")
    if not 75 <= float(sb["target_duration_seconds"]) <= 90:
        errs.append("target_duration_seconds debe estar entre 75 y 90 segundos")
    if not 1 <= len(words(sb.get("titulo", ""))) <= 6:
        errs.append("titulo/gancho debe tener entre 1 y 6 palabras")
    scenes = sb.get("scenes") or []
    if not 7 <= len(scenes) <= 9:
        errs.append(f"se requieren 7–9 escenas; hay {len(scenes)}")

    voice = sb.get("voice") or {}
    for k, expected in VOICE.items():
        if voice.get(k) != expected:
            errs.append(f"voice.{k} debe ser {expected}")
    if not isinstance(sb.get("visual_identity"), dict):
        errs.append("visual_identity debe ser un objeto")
        visual = {}
    else:
        visual = sb["visual_identity"]
    if visual.get("style_id") != sb.get("estilo_id"):
        errs.append("visual_identity.style_id debe coincidir con estilo_id")

    catalog_path = os.path.join(ROOT, "scripts", "estilos.json")
    try:
        with open(catalog_path, encoding="utf-8") as f:
            catalog = json.load(f)
    except Exception as ex:
        catalog = {}
        errs.append(f"no se pudo leer scripts/estilos.json: {ex}")
    style = catalog.get(sb.get("estilo_id"), {})
    prompt_base = style.get("prompt_base")
    if not prompt_base:
        errs.append(f"estilo_id no existe en scripts/estilos.json: {sb.get('estilo_id')}")
    elif visual.get("prompt_base") != prompt_base:
        errs.append("visual_identity.prompt_base no coincide literalmente con scripts/estilos.json")

    sources = sb.get("sources") or []
    source_ids = set()
    if not 1 <= len(sources) <= 5:
        errs.append("se requieren entre 1 y 5 fuentes")
    for src in sources:
        sid = src.get("id")
        if not sid or not src.get("cita_corta") or not src.get("url"):
            errs.append(f"fuente {sid or '?'} sin id/cita_corta/url")
        if sid:
            source_ids.add(sid)
        status = str(src.get("verification_status") or "").lower()
        if status and ("pendiente" in status or "pending" in status):
            warns.append(f"{sid}: verificación pendiente; no presentarla como DOI validado")
        if doi and src.get("doi") and not check_doi(src["doi"]):
            errs.append(f"DOI no confirmado por Crossref en esta ejecución: {src['doi']}")

    arcs = [sc.get("arc") for sc in scenes]
    for arc in ARC:
        if arc not in arcs:
            errs.append(f"arco incompleto: falta {arc}")
    if arcs:
        if arcs[0] != "hook_medias_res":
            errs.append("la primera escena debe ser hook_medias_res")
        if arcs[-1] != "reflexion_o_pregunta":
            errs.append("la última escena debe ser reflexion_o_pregunta")
        if arcs.index("cierre_historia") > arcs.index("reflexion_o_pregunta"):
            errs.append("cierre_historia debe preceder a reflexion_o_pregunta")

    total_scene_seconds, word_count = 0.0, 0
    map_found, data_found = False, False
    for sc in scenes:
        sid = sc.get("id", "?")
        for key in ("id", "arc", "duration_seconds", "narration", "visual_description", "image_prompt", "source_ids", "ambiente", "sfx"):
            if key not in sc:
                errs.append(f"{sid}: falta {key}")
        total_scene_seconds += float(sc.get("duration_seconds", 0) or 0)
        word_count += len(words(sc.get("narration", "")))
        if not sc.get("source_ids"):
            errs.append(f"{sid}: falta source_ids")
        for source_id in sc.get("source_ids", []):
            if source_id not in source_ids:
                errs.append(f"{sid}: source_id desconocido {source_id}")
        if re.search(r"\d", sc.get("narration", "")) and not sc.get("source_ids"):
            errs.append(f"{sid}: cifra sin source_ids")
        if prompt_base and not str(sc.get("image_prompt") or "").startswith(prompt_base):
            errs.append(f"{sid}: image_prompt no comienza con el prompt_base literal")
        if sc.get("style_id") and sc.get("style_id") != sb.get("estilo_id"):
            errs.append(f"{sid}: style_id distinto al de la cápsula")
        layer = sc.get("capa") or sc.get("layer") or {}
        kind = str(layer.get("tipo") or layer.get("type") or "").lower()
        if kind == "mapa":
            pts = layer.get("puntos") or layer.get("points") or []
            if not pts or not (layer.get("fuente") or layer.get("source")):
                errs.append(f"{sid}: mapa sin puntos o fuente")
            for pt in pts:
                lat = pt.get("lat", pt.get("latitude"))
                lon = pt.get("lon", pt.get("longitude"))
                if lat is None or lon is None or not (-90 <= float(lat) <= 90) or not (-180 <= float(lon) <= 180):
                    errs.append(f"{sid}: coordenadas de mapa ausentes o fuera de rango")
            if pts:
                map_found = True
        if kind in {"dato", "grafico", "gráfico"}:
            if not (layer.get("fuente") or layer.get("source")):
                errs.append(f"{sid}: capa de dato/gráfico sin fuente")
            data_found = True
        if mode == "storyboard_only":
            if sc.get("asset_filename") or sc.get("asset_type"):
                errs.append(f"{sid}: storyboard textual no debe declarar assets inexistentes")
        else:
            af = sc.get("asset_filename")
            if not af:
                errs.append(f"{sid}: producción sin asset_filename")
            elif not os.path.exists(os.path.join(base, af)):
                errs.append(f"{sid}: asset declarado no existe ({af})")

    if not map_found:
        errs.append("falta una capa mapa con coordenadas reales y fuente")
    if not data_found:
        errs.append("falta una capa dato/gráfico con fuente")
    if not 170 <= word_count <= 235:
        errs.append(f"narración debe tener 170–235 palabras; hay {word_count}")
    slate = sb.get("cortinilla_fuentes") or {}
    slate_seconds = float(slate.get("duration_seconds", 0) or 0)
    if slate_seconds != 6:
        errs.append("cortinilla_fuentes.duration_seconds debe ser 6")
    for sid in slate.get("source_ids", []):
        if sid not in source_ids:
            errs.append(f"cortinilla: source_id desconocido {sid}")
    total = total_scene_seconds + slate_seconds
    if not 75 <= total <= 90:
        errs.append(f"duración escenas+cortinilla debe ser 75–90 s; suma {total:.1f}")
    if abs(float(sb["target_duration_seconds"]) - total) > 2:
        warns.append(f"target_duration_seconds ({sb['target_duration_seconds']}) difiere de escenas+cortinilla ({total:.1f})")

    last_text = scenes[-1].get("narration", "") if scenes else ""
    if "Esto fue Datos y ociosidades." not in last_text:
        errs.append("el cierre hablado debe contener exactamente 'Esto fue Datos y ociosidades.'")

    if mode == "storyboard_only":
        if sb.get("export", {}).get("filename"):
            errs.append("export.filename no debe declarar un video inexistente")
        if sb.get("approved_assets"):
            errs.append("approved_assets debe estar vacío en preproducción textual")
        pub = sb.get("publicacion") or {}
        if str(pub.get("status") or "").upper() not in {"PENDIENTE_DECISION_GROK", "NO_AUTORIZADA", "PENDIENTE"}:
            errs.append("publicacion.status debe quedar pendiente de decisión de Grok")
        for platform in ("youtube", "tiktok", "facebook", "instagram"):
            if isinstance(pub.get(platform), dict) and pub[platform].get("privacy") == "public":
                errs.append(f"publicacion.{platform} no puede declarar privacy=public en preproducción")
    return errs, warns

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    errors, warnings = validar(sys.argv[1], "--check-doi" in sys.argv)
    for item in warnings:
        print("AVISO:", item)
    for item in errors:
        print("ERROR:", item)
    print("OK" if not errors else f"FALLÓ ({len(errors)} errores)")
    sys.exit(1 if errors else 0)
