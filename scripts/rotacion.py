#!/usr/bin/env python3
"""Rotación anti 'contenido en serie' (YouTube: support.google.com/youtube/answer/1311392 y /2801973).
- estructura narrativa: nunca la misma dos veces seguidas
- cama musical: nunca la misma dos veces seguidas (y evita las 2 últimas)
- duración objetivo: variable por tema, 60-95 s, nunca <60
- límite DURO: 1 cápsula por día
Registro: data/rotacion.json (lista de {fecha, project_id, estructura, cama, duracion})."""
import datetime, hashlib, json, os, sys
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); LOG = os.path.join(R, "data", "rotacion.json")
ESTRUCTURAS = {
    "mito_vs_dato": "Abre con una creencia común (el mito) y la desmonta con el dato verificado; cierra con por qué importa.",
    "pregunta": "Abre con una pregunta concreta que el público se haría; responde paso a paso y cierra con la respuesta en una frase.",
    "historia": "Cuenta un caso o personaje histórico real con fecha y lugar; el dato científico aparece como giro de la historia.",
    "comparacion": "Compara dos cosas (antes/después, aquí/allá, A vs B) con cifras; cierra con la diferencia clave.",
    "sabias_que": "Encadena 3 datos sorprendentes y verificados sobre el tema, de menor a mayor impacto.",
}
CAMAS = ["pulso", "marimba", "pizzicato", "arpegio", "tambor"]
def log(): return json.load(open(LOG)) if os.path.exists(LOG) else []
def _h(s): return int(hashlib.md5(s.encode()).hexdigest(), 16)
def elegir_estructura(tema=""):
    u = [x["estructura"] for x in log()]; ops = [e for e in ESTRUCTURAS if not u or e != u[-1]]
    ops.sort(key=lambda e: (u[-4:].count(e), _h(tema + e) % 97)); return ops[0]
def elegir_cama(tema=""):
    u = [x.get("cama") for x in log()]; ops = [c for c in CAMAS if c not in u[-2:]] or [c for c in CAMAS if not u or c != u[-1]]
    return sorted(ops, key=lambda c: _h(tema + c) % 97)[0]
def duracion_objetivo(tema="", n_fuentes=2):
    """60-95 s según tema: más fuentes/complejidad -> más largo; varía respecto de la anterior."""
    base = 62 + min(n_fuentes, 4) * 6 + _h(tema) % 10; prev = [x.get("duracion") for x in log()][-1:] or [None]
    if prev[0] and abs(base - prev[0]) < 5: base += 7 if base < 85 else -7
    return max(62, min(95, base))
def hecha_hoy(fecha=None):
    f = fecha or datetime.date.today().isoformat(); return [x for x in log() if x.get("fecha") == f]
def exigir_cupo(fecha=None):
    h = hecha_hoy(fecha)
    if h: sys.exit(f"LÍMITE DURO: ya hay una cápsula el {fecha or 'hoy'} ({h[0].get('project_id')}). Máximo 1 por día; no se genera otra.")
def marcar(fecha, project_id, estructura, cama, duracion):
    os.makedirs(os.path.dirname(LOG), exist_ok=True); l = log()
    l.append({"fecha": fecha, "project_id": project_id, "estructura": estructura, "cama": cama, "duracion": duracion})
    json.dump(l, open(LOG, "w"), ensure_ascii=False, indent=1)
if __name__ == "__main__":
    print(json.dumps({"log": log()[-5:], "siguiente": {"estructura": elegir_estructura(), "cama": elegir_cama(), "duracion": duracion_objetivo()}}, ensure_ascii=False, indent=1))
