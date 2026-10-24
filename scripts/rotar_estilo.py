#!/usr/bin/env python3
"""Selector de estilo visual POR TEMÁTICA (no rotación mecánica).
puntaje(e) = 3*empate_tema(e) + 0.5*atractivo(e) + 2*peso_tendencia(e) - penalización_reciente
  - empate_tema: palabras de 'temas' del estilo presentes en tema+guion de la cápsula (reglas por etiquetas).
  - atractivo: 1-5 en estilos.json (prioriza estéticas visualmente atractivas).
  - peso_tendencia: data/tendencias_estilos.json (scripts/tendencias_estilos.py, semanal).
  - NUNCA repite el estilo de la cápsula anterior; -2 si se usó en las últimas 5.
Opcional --llm: si CAPCOT_LLM_API_KEY existe, el LLM elige entre el top-5 (desempate).
Uso: python3 scripts/rotar_estilo.py "texto del tema" [--top N] | --marcar <estilo> <proyecto>"""
import json, os, re, sys, unicodedata
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAT, LOG = os.path.join(R, "scripts", "estilos.json"), os.path.join(R, "data", "estilos_usados.json")
TEN = os.path.join(R, "data", "tendencias_estilos.json")
def catalogo(): return json.load(open(CAT, encoding="utf-8"))
def usados(): return json.load(open(LOG)) if os.path.exists(LOG) else []
def _n(s): return unicodedata.normalize("NFKD", s.lower()).encode("ascii", "ignore").decode()
STOP = {"del","los","las","una","por","que","con","para","como","mas","sus","the","and"}
def _raiz(w): return w[:5]
def ranking(tema=""):
    cat, u = catalogo(), [x["estilo"] for x in usados()]
    ten = json.load(open(TEN)).get("pesos", {}) if os.path.exists(TEN) else {}
    toks = {_raiz(w) for w in re.findall(r"[a-z]{3,}", _n(tema)) if w not in STOP}
    res = []
    for e, c in cat.items():
        if u and e == u[-1]: continue  # no consecutivos
        etq = {_raiz(w) for w in re.findall(r"[a-z]{3,}", _n(c.get("temas", ""))) if w not in STOP}
        m = len(toks & etq)
        s = 3 * m + 0.5 * c.get("atractivo", 3) + 2 * ten.get(e, 0) - (2 if e in u[-5:] else 0)
        res.append((round(s, 2), e, m))
    return sorted(res, reverse=True)
def elegir(tema=""): return ranking(tema)[0][1]
def marcar(e, pid):
    os.makedirs(os.path.dirname(LOG), exist_ok=True); l = usados(); l.append({"estilo": e, "proyecto": pid})
    json.dump(l, open(LOG, "w"), ensure_ascii=False, indent=1)
def tema_de(sb): return " ".join([sb.get("topic", ""), sb.get("title", "")] + [s.get("voiceover", "") for s in sb.get("scenes", [])])
def aplicar_estilo(sb, e=None):
    e = e or sb.get("estilo_id") or elegir(tema_de(sb)); c = catalogo()[e]
    sb["estilo_id"], sb["estilo_visual"] = e, c["nombre"]
    for s in sb["scenes"]:
        p = s.get("image_prompt", "")
        if c["prompt_base"] not in p: s["image_prompt"] = f"{p.rstrip('. ')}. Style: {c['prompt_base']}"
    a = sb.setdefault("audio", {})
    if not a.get("ambiente") and c.get("ambiente_sugerido"): a["ambiente"] = c["ambiente_sugerido"]
    if not a.get("music_asset") and c.get("musica_sugerida", "").startswith("sintetico"): a["music_asset"] = c["musica_sugerida"]
    return sb
if __name__ == "__main__":
    if len(sys.argv) == 4 and sys.argv[1] == "--marcar": marcar(sys.argv[2], sys.argv[3])
    else:
        for r in ranking(" ".join(a for a in sys.argv[1:] if not a.startswith("--")))[:5]: print(*r)
