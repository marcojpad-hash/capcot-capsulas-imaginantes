#!/usr/bin/env python3
"""Genera metadata.json (título, descripción, hashtags, canal) para una cápsula. publicar.py lo usa.
Uso: python3 scripts/metadata.py salidas/<dir>/ [storyboard.json]"""
import json, os, sys, re, unicodedata
CANAL = {"nombre": "Datos y ociosidades", "handle": "@datosyociosidades", "youtube_channel_id": "UCU2ZI-6pBJEr9aSFsF6bxLw"}
BASE_TAGS = ["#DatosYOciosidades", "#Shorts", "#ciencia", "#divulgación", "#SabíasQue"]
def tiktok_linea():
    """Línea con el TikTok EXISTENTE de Mj (no se crea cuenta nueva). Handle configurable: CAPCOT_TIKTOK_HANDLE."""
    h = (os.environ.get("CAPCOT_TIKTOK_HANDLE") or "@PENDIENTE_HANDLE_MJ").lstrip("@")
    return f"TikTok: https://www.tiktok.com/@{h}"
def tag(t): return "#" + re.sub(r"[^A-Za-z0-9ÁÉÍÓÚáéíóúÑñ]", "", "".join(w.capitalize() for w in t.split()))
def generar(d, sbn="storyboard.json"):
    sb = json.load(open(os.path.join(d, sbn), encoding="utf-8"))
    tema = sb.get("trend_source", {}).get("termino", "")
    extra = [tag(x) for x in ([tema] if tema else []) + sb.get("keywords", [])][:4]
    hashtags = list(dict.fromkeys(BASE_TAGS + extra))[:8]
    gancho = next((s["narration"] for s in sb["scenes"] if s["narration"].strip()), "")
    gancho = re.split(r"(?<=[.?!])\s", gancho)[0]
    fuentes = "\n".join(f"• {s['cita_corta']} {('https://doi.org/' + s['doi']) if s.get('doi') else s['url']}" for s in sb["sources"])
    desc = (f"{gancho}\n\n{sb['title']}. Una cápsula de {CANAL['nombre']}: datos verificados contados como historia.\n\n"
            f"Fuentes:\n{fuentes}\n\nImágenes generadas con IA · voz sintética · audio sintetizado.\n"
            f"Suscríbete: {CANAL['handle']}\n{tiktok_linea()}\n\n{' '.join(hashtags)}")
    md = {"canal": CANAL, "titulo": (sb["title"] + " #Shorts")[:100], "descripcion": desc[:4900], "hashtags": hashtags,
          "tags": [h.lstrip("#") for h in hashtags], "idioma": "es-MX", "categoria_yt": "27", "contiene_ia": True,
          "privacyStatus": "private", "tiktok_caption": f"{gancho} {' '.join(hashtags)}"[:2200]}
    json.dump(md, open(os.path.join(d, "metadata.json"), "w"), ensure_ascii=False, indent=1); return md
if __name__ == "__main__": print(json.dumps(generar(sys.argv[1], *(sys.argv[2:3])), ensure_ascii=False, indent=1))
