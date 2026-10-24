#!/usr/bin/env python3
"""Divide un lote {"projects":[...]} en un storyboard vertical por cápsula, adaptado al
esquema de validar_storyboard.py (arc, voice, trend_source, cortinilla_fuentes, image_prompt, cita_corta).
Uso: python3 scripts/dividir_lote.py proyectos/guiones_lote_01/storyboard.json [--out proyectos]"""
import argparse, json, os, re

VOICE = {"engine": "edge-tts", "voice_id": "es-MX-JorgeNeural", "rate": "-8%", "pitch": "-2Hz", "pad_seconds": 0.8}

def cita_corta(title):
    t = re.sub(r"\s+", " ", title).strip()
    return t if len(t) <= 110 else t[:107].rsplit(" ", 1)[0] + "…"

def adaptar(p, lote):
    sc = [dict(s) for s in p["scenes"]]
    cort = 6
    if sc and sc[-1]["on_screen_text"].lower().startswith("fuentes") and not sc[-1]["narration"].strip():
        cort = sc.pop()["duration_seconds"]
    n = len(sc)
    for i, s in enumerate(sc):
        s["arc"] = ("hook_medias_res" if i == 0 else "reflexion_o_pregunta" if i == n - 1
                    else "cierre_historia" if i == n - 2 else "desarrollo")
        s["image_prompt"] = s.pop("generation_prompt", s.get("image_prompt", ""))
        s["asset_filename"] = "frames/" + os.path.basename(s["asset_filename"])
    srcs = []
    for s in p["sources"]:
        m = re.search(r"doi\.org/(.+)$", s["url"])
        d = {"id": s["id"], "cita_corta": cita_corta(s["title"]), "url": s["url"],
             "accessed": s.get("accessed"), "supports": s.get("supports", [])}
        if m: d["doi"] = m.group(1)
        srcs.append(d)
    return {"project_id": p["project_id"], "serie": "Imaginantes de la ciencia", "title": p["title"],
            "language": p.get("language", "es-MX"), "aspect_ratio": "9:16",
            "target_duration_seconds": p["target_duration_seconds"], "audience": p.get("audience", ""),
            "estilo_visual": p.get("style", ""), "music_mood": p.get("music_mood", ""),
            "trend_source": {"tipo": "lote", "rss_geo": "MX", "url": lote.get("trends_feed"), "lote": lote.get("lote"),
                             "fecha_consulta": lote.get("created")},
            "voice": VOICE, "sources": srcs, "scenes": sc,
            "cortinilla_fuentes": {"duration_seconds": cort, "titulo": "Fuentes",
                                   "aviso": "Imágenes generadas con IA. Voz sintética.", "bg_rgb": [18, 16, 14]},
            "audio": {"music_asset": "", "music_license": "", "music_volume": 0.25},
            "export": {"filename": p["project_id"] + ".mp4", "resolution": "1080x1920", "fps": 30, "subtitle_max_words": 3},
            "estado": "GUION_OK"}

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("lote"); ap.add_argument("--out", default="proyectos")
    a = ap.parse_args(); lote = json.load(open(a.lote, encoding="utf-8"))
    for p in lote["projects"]:
        d = os.path.join(a.out, p["project_id"]); os.makedirs(os.path.join(d, "frames"), exist_ok=True)
        json.dump(adaptar(p, lote), open(os.path.join(d, "storyboard.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(os.path.join(d, "storyboard.json"))
