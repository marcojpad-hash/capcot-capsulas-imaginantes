#!/usr/bin/env python3
"""Ingesta de temas: (1) PRIORIDAD feeds RSS de noticias científicas recientes (≤7 días: ScienceDaily, Phys.org, NASA, ESA,
Nature, UNAM Global; EurekAlert/SINC si su RSS responde) y (2) RSS público de Google Trends (sin clave) como señal secundaria.
Uso: python3 scripts/tendencias.py [--geo MX] [--json salida.json] [--dias 7] [--sin-ciencia]
Cada noticia científica trae su URL; el guion DEBE citar el estudio original (DOI) que esa nota referencia.
Puntaje 0-10 = tráfico + palabras con ángulo científico/narrable − penalización (deporte, clima local, tragedia)."""
import argparse, json, re, sys, urllib.request, xml.etree.ElementTree as ET
NS = {"ht": "https://trends.google.com/trending/rss"}
CIENCIA = r"fen[oó]meno|ni[ñn]o|clima|volc|sismo|terremoto|eclipse|cometa|asteroide|nasa|espacio|luna|sol\b|planeta|virus|salud|ciencia|descubr|f[oó]sil|dinosaur|oc[eé]ano|hurac[aá]n|ia\b|inteligencia|robot|energ|petr[oó]leo|pemex|gen|c[eé]lula|cerebro|historia|incendio|arque"
EVITAR = r"\bvs\.?\b| - |futbol|f[uú]tbol|liga|championship|premier|serie a|fc\b|partido|resultado|clima [a-z]+$|muere|muerto|asesin|tiroteo|accidente|loter"

def leer(geo):
    req = urllib.request.Request(f"https://trends.google.com/trending/rss?geo={geo}", headers={"User-Agent": "capcot/1.0"})
    root = ET.fromstring(urllib.request.urlopen(req, timeout=20).read())
    out = []
    for it in root.iter("item"):
        tr = (it.findtext("ht:approx_traffic", "", NS) or "0").replace("+", "").replace(",", "")
        news = [{"titulo": n.findtext("ht:news_item_title", "", NS), "url": n.findtext("ht:news_item_url", "", NS),
                 "medio": n.findtext("ht:news_item_source", "", NS)} for n in it.findall("ht:news_item", NS)]
        out.append({"termino": it.findtext("title"), "trafico": int(tr or 0), "fecha": it.findtext("pubDate"), "geo": geo, "noticias": news})
    return out

import datetime, email.utils
FEEDS_CIENCIA = [  # (medio, url). Los que fallen se omiten sin romper la ingesta.
    ("ScienceDaily", "https://www.sciencedaily.com/rss/top/science.xml"),
    ("ScienceDaily Salud", "https://www.sciencedaily.com/rss/top/health.xml"),
    ("ScienceDaily Espacio", "https://www.sciencedaily.com/rss/space_time.xml"),
    ("Phys.org", "https://phys.org/rss-feed/"),
    ("NASA", "https://www.nasa.gov/news-release/feed/"),
    ("ESA", "https://www.esa.int/rssfeed/Our_Activities/Space_Science"),
    ("Nature", "https://www.nature.com/nature.rss"),
    ("EurekAlert", "https://www.eurekalert.org/rss/news.xml"),
    ("SINC", "https://www.agenciasinc.es/rss"),
    ("UNAM Global", "https://unamglobal.unam.mx/feed/"),
]
RUIDO = r"author correction|publisher correction|apod:|invites media|retraction|podcast|webinar"
def _fecha(txt):
    try: d = email.utils.parsedate_to_datetime(txt)
    except Exception:
        try: d = datetime.datetime.fromisoformat((txt or "").replace("Z", "+00:00"))
        except Exception: return None
    return d if d.tzinfo else d.replace(tzinfo=datetime.timezone.utc)

def leer_ciencia(dias=7):
    lim = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=dias); out = []
    for medio, url in FEEDS_CIENCIA:
        try:
            raw = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 capcot/1.0"}), timeout=15).read()
            root = ET.fromstring(raw)
        except Exception as ex:
            print(f"feed omitido {medio}: {str(ex)[:60]}", file=sys.stderr); continue
        A, R1, DC = "{http://www.w3.org/2005/Atom}", "{http://purl.org/rss/1.0/}", "{http://purl.org/dc/elements/1.1/}"
        items = list(root.iter("item")) or list(root.iter(A + "entry")) or list(root.iter(R1 + "item"))
        for it in items[:40]:
            tit = (it.findtext("title") or it.findtext(A + "title") or it.findtext(R1 + "title") or "").strip()
            link = it.findtext("link") or it.findtext(R1 + "link") or ((it.find(A + "link").get("href")) if it.find(A + "link") is not None else "")
            f = _fecha(it.findtext("pubDate") or it.findtext(A + "updated") or it.findtext(DC + "date") or "")
            if not tit or re.search(RUIDO, tit.lower()) or (f and f < lim): continue
            if any(o["termino"].lower() == tit.lower() for o in out): continue
            out.append({"termino": tit, "trafico": 0, "fecha": f.isoformat() if f else None, "geo": "ciencia", "tipo": "noticia_cientifica",
                        "medio": medio, "url": link, "noticias": [{"titulo": tit, "url": link, "medio": medio}]})
    return out

def puntuar(t):
    if t.get("tipo") == "noticia_cientifica":  # prioridad editorial: ciencia/investigación reciente (base 6)
        s = 6 + (1 if re.search(CIENCIA, t["termino"].lower()) else 0)
        f = _fecha(t.get("fecha") or ""); s += 2 if f and (datetime.datetime.now(datetime.timezone.utc) - f).days <= 2 else 1 if f else 0
        if re.search(r"muere|asesin|tiroteo", t["termino"].lower()): s -= 6
        return max(0, min(10, s))
    txt = (t["termino"] + " " + " ".join(n["titulo"] for n in t["noticias"])).lower()
    s = min(4, len(str(t["trafico"])) - 1)  # 100→2, 1000→3, 10000+→4
    s += 4 if re.search(CIENCIA, txt) else 0
    s += 2 if t["noticias"] else 0
    if re.search(EVITAR, t["termino"].lower()) or re.search(r"muere|asesin|tiroteo", txt): s -= 6
    return max(0, min(10, s))

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--geo", default="MX"); ap.add_argument("--json")
    ap.add_argument("--dias", type=int, default=7); ap.add_argument("--sin-ciencia", action="store_true")
    a = ap.parse_args(); ts = []
    if not a.sin_ciencia: ts += leer_ciencia(a.dias)
    try: ts += leer(a.geo)
    except Exception as ex: print("Google Trends no disponible:", ex, file=sys.stderr)
    for t in ts: t["puntaje"] = puntuar(t)
    ts.sort(key=lambda t: -t["puntaje"])
    for t in ts: print(f'{t["puntaje"]:>2}  {t["trafico"]:>6}+  {t["termino"]}', file=sys.stderr)
    if a.json: json.dump(ts, open(a.json, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    else: print(json.dumps(ts[:5], ensure_ascii=False, indent=1))
