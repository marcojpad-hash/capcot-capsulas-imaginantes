#!/usr/bin/env python3
"""Ingesta de tendencias: RSS público de Google Trends (sin clave) + puntuación heurística.
Uso: python3 scripts/tendencias.py [--geo MX] [--json salida.json]
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

def puntuar(t):
    txt = (t["termino"] + " " + " ".join(n["titulo"] for n in t["noticias"])).lower()
    s = min(4, len(str(t["trafico"])) - 1)  # 100→2, 1000→3, 10000+→4
    s += 4 if re.search(CIENCIA, txt) else 0
    s += 2 if t["noticias"] else 0
    if re.search(EVITAR, t["termino"].lower()) or re.search(r"muere|asesin|tiroteo", txt): s -= 6
    return max(0, min(10, s))

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--geo", default="MX"); ap.add_argument("--json")
    a = ap.parse_args(); ts = leer(a.geo)
    for t in ts: t["puntaje"] = puntuar(t)
    ts.sort(key=lambda t: -t["puntaje"])
    for t in ts: print(f'{t["puntaje"]:>2}  {t["trafico"]:>6}+  {t["termino"]}', file=sys.stderr)
    if a.json: json.dump(ts, open(a.json, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    else: print(json.dumps(ts[:5], ensure_ascii=False, indent=1))
