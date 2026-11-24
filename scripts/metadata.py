#!/usr/bin/env python3
"""Genera metadata.json (título, descripción, hashtags, canal) para una cápsula. publicar.py lo usa.
Uso: python3 scripts/metadata.py salidas/<dir>/ [storyboard.json]

Regla de títulos y hashtags (Mj, 24-nov-2026):
  Título YouTube: gancho de Short y, si se puede, de búsqueda (pregunta, mito «NO»
  o nombre/entidad conocida; escena clara tipo «El/La X que Y»). Sin jerga ni
  apellido suelto. Añadir « #Shorts» al final solo si cabe en 100 caracteres;
  nunca recortar a «#Short». Sin hashtags temáticos en el título.
  YouTube: 3 a 5 hashtags del tema en la descripción + #sabiasque + #Shorts.
  #ia / #inteligenciaartificial solo si el dato va de IA. Sin pack fijo
  (#datos #difusión #difusióncientífica #DatosYOciosidades) y sin camelcase de frase.
  TikTok: 4 a 5 hashtags, sin #Shorts y sin mencionar YouTube.
"""
import json, os, sys, re, unicodedata
CANAL = {"nombre": "Datos y ociosidades", "handle": "@datosyociosidades", "youtube_channel_id": "UCU2ZI-6pBJEr9aSFsF6bxLw"}
TIKTOK = os.environ.get("CAPCOT_TIKTOK_HANDLE") or "@datosyociosidades"  # TikTok existente (confirmado); único placeholder
# YouTube (Mj 24-nov-2026): temas + #sabiasque + #Shorts. El pack anterior
# (#datos #ciencia #difusión #difusióncientífica #ia #DatosYOciosidades) ya no se inserta solo.
YT_FIJOS = ["#sabiasque", "#Shorts"]
YT_BASE_TAGS = []  # compat: ya no hay pack obligatorio
YT_TAGS = list(YT_FIJOS)
TT_CORE = ["#aprendeentiktok", "#sabiasque", "#ciencia", "#divulgacioncientifica"]  # 4 fijos; slot 5 = tema
BASE_TAGS = YT_BASE_TAGS
PROHIBIDOS_PACK = {"#datos", "#difusión", "#difusion", "#difusióncientífica", "#difusioncientifica", "#datosyociosidades", "#ia"}
AI_RE = re.compile(r"\b(ia|inteligenciaartificial|inteligencia artificial|chatgpt|openai|llm)\b", re.I)
def tiktok_linea():
    """Línea con el TikTok EXISTENTE de Mj Fija: @datosyociosidades; CAPCOT_TIKTOK_HANDLE solo sobreescribe."""
    h = TIKTOK.lstrip("@")
    return f"TikTok: https://www.tiktok.com/@{h}"
def tag(t):
    """Hashtag corto, sin camelcase de frase. Conservado por compatibilidad."""
    return slug_hashtag(t) or "#tema"
def slug_hashtag(t):
    """Hashtag corto (≤24 letras). No convierte una frase en CamelCase kilométrico."""
    raw = (t or "").strip()
    if raw.startswith("#"):
        raw = raw[1:]
    # Si ya es una sola palabra o un nombre corto, respeta mayúsculas de nombres propios cortos.
    s = re.sub(r"[^A-Za-z0-9ÁÉÍÓÚÜÑáéíóúüñ]", "", raw)
    if not s or len(s) > 24:
        # intenta la primera palabra útil
        parts = re.findall(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ0-9]+", raw)
        s = parts[0] if parts else ""
        if not s or len(s) > 24:
            return None
    return "#" + s
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
def titulo_youtube(title):
    """Añade #Shorts si cabe en 100 caracteres; nunca recorta a #Short."""
    t = limpiar_texto_yt(title or "").strip()
    t = re.sub(r"\s+#Shorts?\s*$", "", t, flags=re.I).rstrip()
    if len(t) + len(" #Shorts") <= 100:
        t = t + " #Shorts"
    elif len(t) > 100:
        t = t[:100].rstrip()
        if t.lower().endswith("#short"):
            t = t[:-6].rstrip()
    return t
def tema_es_ia(*textos):
    return bool(AI_RE.search(" ".join(t or "" for t in textos)))
def hashtags_youtube(sb):
    """3 a 5 hashtags de tema + #sabiasque + #Shorts. #ia solo si el dato va de IA."""
    tema = (sb.get("trend_source") or {}).get("termino", "") or ""
    kws = list(sb.get("keywords") or [])
    topics, seen = [], set()
    for x in ([tema] if tema else []) + kws:
        h = slug_hashtag(x)
        if not h:
            continue
        key = h.lower()
        if key in seen or key in PROHIBIDOS_PACK or key in {"#shorts", "#short", "#sabiasque"}:
            continue
        topics.append(h); seen.add(key)
    blob = " ".join([sb.get("title") or "", tema, " ".join(kws)])
    if tema_es_ia(blob):
        if not any(h.lower() in {"#ia", "#inteligenciaartificial"} for h in topics):
            topics.insert(0, "#inteligenciaartificial")
            seen.add("#inteligenciaartificial")
    else:
        topics = [h for h in topics if h.lower() not in {"#ia", "#inteligenciaartificial"}]
    topics = topics[:5]
    for filler in ("#ciencia", "#historia", "#datoscuriosos"):
        if len(topics) >= 3:
            break
        if filler not in seen:
            topics.append(filler); seen.add(filler)
    return list(dict.fromkeys(topics[:5] + list(YT_FIJOS)))
def hashtags_tiktok(sb, extra_yt=None):
    """4 a 5 hashtags, sin #Shorts."""
    tema = (sb.get("trend_source") or {}).get("termino", "") or ""
    extra = extra_yt or []
    tema_tt = slug_hashtag(tema) if tema else (extra[0] if extra else "#curiosidades")
    if not tema_tt or tema_tt.lower() in {t.lower() for t in TT_CORE} | {"#shorts", "#short"}:
        tema_tt = next((t for t in extra if t.lower() not in {c.lower() for c in TT_CORE} | {"#shorts", "#short", "#sabiasque"}), "#curiosidades")
    return [h for h in list(dict.fromkeys(TT_CORE + [tema_tt]))[:5] if h.lower() not in {"#shorts", "#short"}]
def sanitizar_yt(md):
    """Título ≤100 chars (sin recortar a #Short), descripción ≤5000 bytes UTF-8, tags sin <> y total ≤500 chars (YouTube Data API)."""
    md["titulo"] = titulo_youtube(md.get("titulo") or "")
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
    if re.search(r"#Short([^s]|$)", md.get("titulo") or ""): e.append("titulo recortado a #Short")
    if any(c in md["descripcion"] for c in "<>"): e.append("descripcion con < >")
    if len(md["descripcion"].encode("utf-8")) > 5000: e.append("descripcion >5000 bytes")
    if _tags_len(md.get("tags", [])) > 500: e.append("tags >500 chars")
    if any(c in t for t in md.get("tags", []) for c in "<>"): e.append("tags con < >")
    if len(md.get("tiktok_caption", "")) > 2200: e.append("tiktok_caption >2200")
    hs = md.get("hashtags") or []
    if "#sabiasque" not in [h.lower() if h.startswith("#") else h for h in
                            [x if x.startswith("#") else x for x in hs]] and "#sabiasque" not in [h.lower() for h in hs]:
        e.append("falta #sabiasque")
    if not any(h.lower() == "#shorts" for h in hs):
        e.append("falta #Shorts")
    temas = [h for h in hs if h.lower() not in {"#shorts", "#short", "#sabiasque"}]
    if not (3 <= len(temas) <= 5):
        e.append(f"hashtags de tema {len(temas)} (deben ser 3 a 5 + #sabiasque + #Shorts)")
    if any(len(h.lstrip("#")) > 24 for h in hs):
        e.append("hashtag camelcase/frase demasiado largo")
    blob = (md.get("titulo") or "") + " " + " ".join(hs)
    if any(h.lower() in {"#ia", "#inteligenciaartificial"} for h in hs) and not tema_es_ia(md.get("titulo") or "", " ".join(hs)):
        # Permitir #inteligenciaartificial solo si el título o el tema hablan de IA.
        if not tema_es_ia(md.get("titulo") or ""):
            e.append("#ia en un video que no va de IA")
    tt = md.get("tiktok_hashtags") or []
    if not (4 <= len(tt) <= 5): e.append(f"tiktok_hashtags {len(tt)} (deben ser 4 a 5)")
    if any("shorts" in t.lower() for t in tt): e.append("tiktok_hashtags incluye #Shorts")
    cap = md.get("tiktok_caption") or ""
    if "youtube" in cap.lower(): e.append("tiktok_caption menciona YouTube")
    if re.search(r"#shorts\b", cap, re.I): e.append("tiktok_caption incluye #Shorts")
    return e
def generar(d, sbn="storyboard.json"):
    md = construir(json.load(open(os.path.join(d, sbn), encoding="utf-8")))
    json.dump(md, open(os.path.join(d, "metadata.json"), "w"), ensure_ascii=False, indent=1); return md
def construir(sb):
    hashtags = hashtags_youtube(sb)
    temas = [h for h in hashtags if h.lower() not in {"#shorts", "#short", "#sabiasque"}]
    tt_list = hashtags_tiktok(sb, temas)
    gancho = next((s["narration"] for s in sb["scenes"] if s["narration"].strip()), "")
    gancho = re.split(r"(?<=[.?!])\s", gancho)[0]
    resumen = sb.get("resumen") or f"{sb['title']}. Datos verificados contados como historia."
    fuentes = "\n".join(f"• {s['cita_corta']} {('https://doi.org/' + s['doi']) if s.get('doi') else s['url']}" for s in sb["sources"])
    cuerpo = (f"{gancho}\n\n{sb['title']}. Una cápsula de {CANAL['nombre']}: datos verificados contados como historia.\n\n"
              f"Fuentes:\n{fuentes}\n\nImágenes generadas con IA · voz sintética · audio sintetizado.\n")
    desc = cuerpo + f"Suscríbete: {CANAL['handle']}\n{tiktok_linea()}\n\n{' '.join(hashtags)}"
    tt_tags = " ".join(tt_list)
    tt_cap = f"{gancho}\n\n{resumen}\n\n"
    tt_cap = (tt_cap[:2200 - len(tt_tags) - 1] + tt_tags) if tt_tags else tt_cap[:2200]
    md = {"canal": CANAL, "titulo": titulo_youtube(sb["title"]), "descripcion": desc[:4900], "hashtags": hashtags,
          "tags": [h.lstrip("#") for h in hashtags], "idioma": "es-MX", "categoria_yt": "27", "contiene_ia": True,
          "contenido_sintetico": etiqueta_sintetica(sb)[0], "contenido_sintetico_motivos": etiqueta_sintetica(sb)[1] or ["no realista: ilustración estilizada + voz TTS; no requiere etiqueta (YouTube 14328491)"],
          "privacyStatus": "private", "tiktok_caption": tt_cap, "tiktok_hashtags": tt_list,
          "tiktok_descripcion_completa": (cuerpo + tt_tags)[:2200]}
    return sanitizar_yt(md)
if __name__ == "__main__": print(json.dumps(generar(sys.argv[1], *(sys.argv[2:3])), ensure_ascii=False, indent=1))
