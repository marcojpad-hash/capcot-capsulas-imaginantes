#!/usr/bin/env python3
"""Paso de tendencias (semanal, lunes; lo llama capsula_diaria.py si data/tendencias_estilos.json tiene >7 días).
Fuente: Google News RSS (consultas sobre estéticas de animación en TikTok/Shorts). TikTok Creative Center requiere
login/JS -> no accesible sin navegador; revisión manual opcional. Cuenta menciones de palabras clave por estilo y
normaliza a peso 0-1, mezclado 50/50 con los pesos previos (curados con búsqueda web, ver 'fuente')."""
import json, os, re, time, urllib.parse, urllib.request
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); TEN = os.path.join(R, "data", "tendencias_estilos.json")
Q = ["TikTok animation trend", "viral animation style shorts", "claymation trend", "stop motion trend TikTok", "AI video aesthetic trend"]
KW = {"claymation": "claymation|clay|plasticine", "papel_stop_motion": "paper cut|papercraft|stop.motion", "principito_2015": "little prince|papercraft",
      "disney_clasico": "disney|hand.drawn|2d animation", "acuarela_linea": "ghibli|watercolor", "pixel_art": "pixel art", "ukiyo_e": "ukiyo|woodblock",
      "pop_art_comic": "comic|pop art", "amigurumi": "crochet|amigurumi|felt", "risografia": "risograph", "van_gogh": "van gogh"}
def actualizar():
    txt = ""
    for q in Q:
        u = "https://news.google.com/rss/search?q=" + urllib.parse.quote(q + " when:30d") + "&hl=en-US&gl=US&ceid=US:en"
        try: txt += urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=15).read().decode("utf-8", "ignore").lower()
        except Exception as ex: print("fallo", q, ex)
    cnt = {e: len(re.findall(p, txt)) for e, p in KW.items()}; mx = max(cnt.values()) or 1
    d = json.load(open(TEN)) if os.path.exists(TEN) else {"pesos": {}}
    for e, n in cnt.items(): d["pesos"][e] = round(0.5 * d["pesos"].get(e, 0) + 0.5 * n / mx, 2)
    d["actualizado"] = time.strftime("%Y-%m-%d"); d["conteo_ultimo"] = cnt
    json.dump(d, open(TEN, "w"), ensure_ascii=False, indent=1); return d
def vigente(): return os.path.exists(TEN) and time.time() - os.path.getmtime(TEN) < 1 * 86400  # revisión DIARIA de estilos virales
if __name__ == "__main__": print(json.dumps(actualizar()["pesos"], indent=1))
