#!/usr/bin/env python3
"""Rotación de estilos visuales: elige el estilo menos usado recientemente (data/estilos_usados.json).
Uso: python3 scripts/rotar_estilo.py [--marcar <estilo_id> <project_id>]  -> imprime estilo_id elegido.
Aplica: storyboard['estilo_id'], ['estilo_visual'] y antepone prompt_base a cada image_prompt (aplicar_estilo)."""
import json, os, sys
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAT, LOG = os.path.join(R, "scripts", "estilos.json"), os.path.join(R, "data", "estilos_usados.json")
def catalogo(): return json.load(open(CAT, encoding="utf-8"))
def usados(): return json.load(open(LOG)) if os.path.exists(LOG) else []
def elegir():
    u = [x["estilo"] for x in usados()]
    return min(catalogo(), key=lambda e: (len(u) - 1 - u[::-1].index(e)) if e in u else -1)
def marcar(e, pid):
    os.makedirs(os.path.dirname(LOG), exist_ok=True); l = usados(); l.append({"estilo": e, "proyecto": pid})
    json.dump(l, open(LOG, "w"), ensure_ascii=False, indent=1)
def aplicar_estilo(sb, e=None):
    e = e or sb.get("estilo_id") or elegir(); c = catalogo()[e]
    sb["estilo_id"], sb["estilo_visual"] = e, c["nombre"]
    for s in sb["scenes"]:
        p = s.get("image_prompt", "")
        if c["prompt_base"] not in p: s["image_prompt"] = f"{p.rstrip('. ')}. Style: {c['prompt_base']}"
    a = sb.setdefault("audio", {})
    if not a.get("ambiente") and c["ambiente_sugerido"]: a["ambiente"] = c["ambiente_sugerido"]
    if not a.get("music_asset") and c["musica_sugerida"].startswith("sintetico"): a["music_asset"] = c["musica_sugerida"]
    return sb
if __name__ == "__main__":
    if len(sys.argv) == 4 and sys.argv[1] == "--marcar": marcar(sys.argv[2], sys.argv[3])
    else: print(elegir())
