#!/usr/bin/env python3
"""Genera guion_mj.md: texto para que Mj lo lea con SU voz.
Marcas: "/" respiración corta (comas, dos puntos, punto y coma), "//" respiración larga (fin de frase y cambio de escena).
Incluye versión completa (~75-95 s), versión corta opcional 30-60 s (gancho + giro/cierre + reflexión) y fuentes al final.
Uso: python3 scripts/guion_mj.py salidas/<dir>/ [storyboard.json]"""
import json, os, re, sys
WPS = 2.6  # palabras/seg lectura natural de Mj (estimado; ajustar con su primera grabación)
def marcar(t):
    t = re.sub(r"([,;:])\s+", r"\1 / ", t.strip())
    return re.sub(r"([.?!…])\s+", r"\1 // ", t)
def palabras(t): return len(re.findall(r"\w+", t))
def generar(d, sbn="storyboard.json"):
    sb = json.load(open(os.path.join(d, sbn), encoding="utf-8")); sc = [s for s in sb["scenes"] if s["narration"].strip()]
    larga = [marcar(s["narration"]) + " //" for s in sc]
    corta, n = [], 0
    pref = ["hook_medias_res", "cierre_historia", "reflexion_o_pregunta"]
    for s in sc:
        if s["arc"] in pref or s is sc[1]:
            w = palabras(s["narration"])
            if n + w <= 60 * WPS or s["arc"] == "reflexion_o_pregunta": corta.append(marcar(s["narration"]) + " //"); n += w
    nl = sum(palabras(s["narration"]) for s in sc)
    L = [f"# {sb['title']} — guion para voz de Mj", "",
         "Marcas: `/` = respiración corta (~0.3 s) · `//` = respiración larga (~0.6 s). Sin pausas más largas: el ritmo es continuo.",
         "Tono: cercano, de narrador que cuenta una historia; sube la energía en el gancho, baja en la reflexión.", "",
         f"## Versión completa (~{nl} palabras ≈ {nl / WPS:.0f} s)", ""] + [f"{x}\n" for x in larga] + [
         f"## Versión corta opcional 30–60 s (~{n} palabras ≈ {n / WPS:.0f} s)", ""] + [f"{x}\n" for x in corta] + ["## Fuentes", ""] + [
         f"- {s['cita_corta']} {('https://doi.org/' + s['doi']) if s.get('doi') else s.get('url', '')}" for s in sb["sources"]]
    p = os.path.join(d, "guion_mj.md"); open(p, "w", encoding="utf-8").write("\n".join(L) + "\n"); return p
if __name__ == "__main__": print(generar(sys.argv[1], *(sys.argv[2:3])))
