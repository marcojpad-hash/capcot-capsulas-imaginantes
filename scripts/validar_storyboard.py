#!/usr/bin/env python3
"""Valida un storyboard vertical CAPCOT (solo stdlib).
Uso: python3 validar_storyboard.py proyectos/x/storyboard.json [--check-doi]
Sale con código 0 si pasa, 1 si hay errores."""
import json, os, re, sys, urllib.request

ARC = ["hook_medias_res", "desarrollo", "cierre_historia", "reflexion_o_pregunta"]

def check_doi(doi):
    try:
        req = urllib.request.Request("https://api.crossref.org/works/" + doi,
                                     headers={"User-Agent": "capcot-validador/1.0"})
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status == 200
    except Exception:
        return False

def validar(path, doi=False):
    errs, warns = [], []
    sb = json.load(open(path, encoding="utf-8"))
    base = os.path.dirname(os.path.abspath(path))
    for k in ["project_id", "title", "language", "aspect_ratio", "target_duration_seconds",
              "trend_source", "voice", "sources", "scenes", "cortinilla_fuentes", "export"]:
        if k not in sb: errs.append(f"falta campo raíz: {k}")
    if errs: return errs, warns
    if sb["aspect_ratio"] != "9:16": errs.append("aspect_ratio debe ser 9:16")
    if sb["export"].get("resolution") != "1080x1920": errs.append("export.resolution debe ser 1080x1920")
    t = sb["target_duration_seconds"]
    if not (60 <= t <= 90): errs.append(f"target_duration_seconds={t} fuera de 60-90")
    src_ids = set()
    for s in sb["sources"]:
        for k in ["id", "cita_corta", "url"]:
            if not s.get(k): errs.append(f"fuente {s.get('id')} sin {k}")
        src_ids.add(s.get("id"))
        if doi and s.get("doi"):
            if not check_doi(s["doi"]): errs.append(f"DOI no resuelve en Crossref: {s['doi']}")
    if not 1 <= len(sb["sources"]) <= 4: warns.append("se recomiendan 1-4 fuentes en la cortinilla")
    arcs = [sc.get("arc") for sc in sb["scenes"]]
    for a in ARC:
        if a not in arcs: errs.append(f"arco incompleto: ninguna escena con arc={a}")
    if arcs and arcs[0] != "hook_medias_res": errs.append("la primera escena debe ser hook_medias_res")
    total, words = 0.0, 0
    for sc in sb["scenes"]:
        sid = sc.get("id", "?")
        for k in ["id", "arc", "duration_seconds", "narration", "visual_description", "image_prompt", "asset_filename"]:
            if k not in sc: errs.append(f"{sid}: falta {k}")
        total += float(sc.get("duration_seconds", 0))
        words += len(sc.get("narration", "").split())
        for r in sc.get("source_ids", []):
            if r not in src_ids: errs.append(f"{sid}: source_id desconocido {r}")
        if re.search(r"\d", sc.get("narration", "")) and not sc.get("source_ids"):
            warns.append(f"{sid}: narración con cifra pero sin source_ids")
        ost = sc.get("on_screen_text", "")
        if len(ost.split()) > 6: warns.append(f"{sid}: on_screen_text >6 palabras")
        af = os.path.join(base, sc.get("asset_filename", ""))
        if not os.path.exists(af): warns.append(f"{sid}: asset aún no existe ({sc.get('asset_filename')})")
    first = sb["scenes"][0].get("narration", "").split(".")[0] if sb["scenes"] else ""
    if len(first.split()) > 12: warns.append("primera frase del gancho >12 palabras")
    total += float(sb["cortinilla_fuentes"].get("duration_seconds", 0))
    if not (60 <= total <= 90): errs.append(f"duración planificada {total:.1f}s fuera de 60-90")
    if words > 210: warns.append(f"{words} palabras: riesgo de exceder 90 s")
    return errs, warns

if __name__ == "__main__":
    if len(sys.argv) < 2: sys.exit(__doc__)
    e, w = validar(sys.argv[1], "--check-doi" in sys.argv)
    for x in w: print("AVISO:", x)
    for x in e: print("ERROR:", x)
    print("OK" if not e else f"FALLÓ ({len(e)} errores)")
    sys.exit(1 if e else 0)
