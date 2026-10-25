#!/usr/bin/env python3
"""Genera metadata.json (título, descripción, hashtags, canal) para una cápsula. publicar.py lo usa.
Uso: python3 scripts/metadata.py salidas/<dir>/ [storyboard.json]"""
import json, os, sys, re, unicodedata
CANAL = {"nombre": "Datos y ociosidades", "handle": "@datosyociosidades", "youtube_channel_id": "UCU2ZI-6pBJEr9aSFsF6bxLw"}
TIKTOK = os.environ.get("CAPCOT_TIKTOK_HANDLE") or "@datosyociosidades"  # TikTok existente (confirmado); único placeholder
# YouTube: base + marca. TikTok: máx 5 (Mj 24-oct-2026); prioridad alcance nicho ES.
YT_BASE_TAGS = ["#datos", "#ciencia", "#difusión", "#difusióncientífica", "#ia"]
YT_TAGS = ["#DatosYOciosidades", "#Shorts"]  # solo YouTube
# Orden por alcance (estudios ES + Toklytics 2026): discovery → curiosidad → nicho → tema
TT_CORE = ["#aprendeentiktok", "#sabiasque", "#ciencia", "#divulgacioncientifica"]  # 4 fijos; slot 5 = tema
BASE_TAGS = YT_BASE_TAGS  # compat validar_yt / hashtags YT
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
def _url_seguro(m): return m.group(0).replace("<", "%3C").replace(">", "%3E")
def limpiar_texto_yt(t):
    """YouTube rechaza '<' y '>' en título/descripción (invalidDescription/invalidTitle): en URLs -> %3C/%3E; fuera -> ‹ ›."""
    t = re.sub(r"https?://\S+", _url_seguro, t or ""); return t.replace("<", "‹").replace(">", "›")
def _tags_len(tags): return sum(len(x) + (2 if " " in x else 0) for x in tags) + max(len(tags) - 1, 0)
def sanitizar_yt(md):
    """Título ≤100 chars, descripción ≤5000 bytes UTF-8, tags sin <> y total ≤500 chars (YouTube Data API)."""
    md["titulo"] = limpiar_texto_yt(md["titulo"]).strip()
    if len(md["titulo"]) > 100: md["titulo"] = md["titulo"][:100].rstrip()
    d = limpiar_texto_yt(md["descripcion"])
    while len(d.encode("utf-8")) > 5000: d = d[:-50]
    md["descripcion"] = d
    tags = []
    for x in md.get("tags", []):
        x = re.sub(r"[<>,]", "", x).strip()
        if x and _tags_len(tags + [x]) <= 500: tags.append(x)
    md["tags"] = tags; return md
def validar_yt(md):
    """Lista de problemas (vacía = aceptable para videos.insert)."""
    e = []
    if any(c in md["titulo"] for c in "<>"): e.append("titulo con < >")
    if len(md["titulo"]) > 100: e.append(f"titulo {len(md['titulo'])}>100")
    if any(c in md["descripcion"] for c in "<>"): e.append("descripcion con < >")
    if len(md["descripcion"].encode("utf-8")) > 5000: e.append("descripcion >5000 bytes")
    if _tags_len(md.get("tags", [])) > 500: e.append("tags >500 chars")
    if any(c in t for t in md.get("tags", []) for c in "<>"): e.append("tags con < >")
    if len(md.get("tiktok_caption", "")) > 2200: e.append("tiktok_caption >2200")
    if any(b not in md.get("hashtags", []) for b in YT_BASE_TAGS + YT_TAGS): e.append("faltan hashtags base")
    tt = md.get("tiktok_hashtags") or []
    if len(tt) > 5: e.append(f"tiktok_hashtags {len(tt)}>5")
    if not all(c in tt for c in TT_CORE[:3]): e.append("faltan hashtags TikTok de alcance")
    return e
def generar(d, sbn="storyboard.json"):
    md = construir(json.load(open(os.path.join(d, sbn), encoding="utf-8")))
    json.dump(md, open(os.path.join(d, "metadata.json"), "w"), ensure_ascii=False, indent=1); return md
def construir(sb):
    tema = sb.get("trend_source", {}).get("termino", "")
    extra = [tag(x) for x in ([tema] if tema else []) + sb.get("keywords", [])][:4]  # hashtags del tema (YT)
    comunes = list(dict.fromkeys(YT_BASE_TAGS + extra))
    hashtags = list(dict.fromkeys(YT_TAGS + comunes))
    # TikTok: exactamente hasta 5 — 4 de alto alcance + 1 del tema (Mj: solo 5 caben)
    tema_tt = tag(tema) if tema else (extra[0] if extra else "#curiosidades")
    if tema_tt.lower() in {t.lower() for t in TT_CORE}:
        tema_tt = next((t for t in extra if t.lower() not in {c.lower() for c in TT_CORE}), "#curiosidades")
    tt_list = list(dict.fromkeys(TT_CORE + [tema_tt]))[:5]
    gancho = next((s["narration"] for s in sb["scenes"] if s["narration"].strip()), "")
    gancho = re.split(r"(?<=[.?!])\s", gancho)[0]
    resumen = sb.get("resumen") or f"{sb['title']}. Datos verificados contados como historia."
    fuentes = "\n".join(f"• {s['cita_corta']} {('https://doi.org/' + s['doi']) if s.get('doi') else s['url']}" for s in sb["sources"])
    cuerpo = (f"{gancho}\n\n{sb['title']}. Una cápsula de {CANAL['nombre']}: datos verificados contados como historia.\n\n"
              f"Fuentes:\n{fuentes}\n\nImágenes generadas con IA · voz sintética · audio sintetizado.\n")
    desc = cuerpo + f"Suscríbete: {CANAL['handle']}\n{tiktok_linea()}\n\n{' '.join(hashtags)}"
    tt_tags = " ".join(tt_list)
    tt_cap = f"{gancho}\n\n{resumen}\n\nFuentes en YouTube {CANAL['handle']}\n\n"
    tt_cap = tt_cap[:2200 - len(tt_tags) - 1] + tt_tags
    md = {"canal": CANAL, "titulo": (sb["title"] + " #Shorts")[:100], "descripcion": desc[:4900], "hashtags": hashtags,
          "tags": [h.lstrip("#") for h in hashtags], "idioma": "es-MX", "categoria_yt": "27", "contiene_ia": True,
          "contenido_sintetico": etiqueta_sintetica(sb)[0], "contenido_sintetico_motivos": etiqueta_sintetica(sb)[1] or ["no realista: ilustración estilizada + voz TTS; no requiere etiqueta (YouTube 14328491)"],
          "privacyStatus": "private", "tiktok_caption": tt_cap, "tiktok_hashtags": tt_list,
          "tiktok_descripcion_completa": (cuerpo + f"Fuentes en YouTube {CANAL['handle']}\n\n{tt_tags}")[:2200]}
    return sanitizar_yt(md)
if __name__ == "__main__": print(json.dumps(generar(sys.argv[1], *(sys.argv[2:3])), ensure_ascii=False, indent=1))
