#!/usr/bin/env python3
"""Genera metadata.json (título, descripción, hashtags, canal) para una cápsula. publicar.py lo usa.
Uso: python3 scripts/metadata.py salidas/<dir>/ [storyboard.json]"""
import json, os, sys, re, unicodedata
CANAL = {"nombre": "Datos y ociosidades", "handle": "@datosyociosidades", "youtube_channel_id": "UCU2ZI-6pBJEr9aSFsF6bxLw"}
TIKTOK = os.environ.get("CAPCOT_TIKTOK_HANDLE") or "@datosyociosidades"  # TikTok existente (confirmado); único placeholder
BASE_TAGS = ["#DatosYOciosidades", "#Shorts", "#ciencia", "#divulgación", "#SabíasQue"]
def tiktok_linea():
    """Línea con el TikTok EXISTENTE de Mj Fija: @datosyociosidades; CAPCOT_TIKTOK_HANDLE solo sobreescribe."""
    h = TIKTOK.lstrip("@")
    return f"TikTok: https://www.tiktok.com/@{h}"
def tag(t): return "#" + re.sub(r"[^A-Za-z0-9ÁÉÍÓÚáéíóúÑñ]", "", "".join(w.capitalize() for w in t.split()))
# Regla de etiqueta "contenido alterado o sintético" (YouTube support.google.com/youtube/answer/14328491):
# SÍ cuando algo PARECE REAL (personas reales, lugares/eventos reales recreados de forma realista, escenas
# realistas que no ocurrieron) o cuando la música generada por IA es el elemento central. NO para ilustración
# no realista (garabato, crayón, tatuaje, acuarela...), voz TTS genérica, guion/miniatura asistidos ni infografías.
ESTILOS_REALISTAS = {"fotorrealista", "foto", "documental_realista", "miniatura_realista"}
def etiqueta_sintetica(sb):
    motivos = []
    if sb.get("parece_real"): motivos.append("imágenes/escenas que parecen reales (parece_real=true)")
    if sb.get("estilo_id") in ESTILOS_REALISTAS: motivos.append(f"estilo realista: {sb.get('estilo_id')}")
    if any(s.get("persona_real_recreada") for s in sb.get("scenes", [])): motivos.append("persona real recreada")
    a = sb.get("audio", {})
    if a.get("music_ia") and a.get("music_protagonista"): motivos.append("música generada por IA como elemento central")
    return bool(motivos), motivos
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
          "contenido_sintetico": etiqueta_sintetica(sb)[0], "contenido_sintetico_motivos": etiqueta_sintetica(sb)[1] or ["no realista: ilustración estilizada + voz TTS; no requiere etiqueta (YouTube 14328491)"],
          "privacyStatus": "private", "tiktok_caption": f"{gancho} {' '.join(hashtags)}"[:2200]}
    json.dump(md, open(os.path.join(d, "metadata.json"), "w"), ensure_ascii=False, indent=1); return md
if __name__ == "__main__": print(json.dumps(generar(sys.argv[1], *(sys.argv[2:3])), ensure_ascii=False, indent=1))
