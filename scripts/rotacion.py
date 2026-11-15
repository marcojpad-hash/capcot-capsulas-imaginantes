#!/usr/bin/env python3
"""Rotación anti 'contenido en serie' (YouTube: support.google.com/youtube/answer/1311392 y /2801973).
- estructura narrativa: nunca la misma dos veces seguidas
- cama musical: nunca la misma dos veces seguidas (y evita las 2 últimas)
- duración objetivo: variable por tema, 60-95 s, nunca <60
- límite DURO: 2 cápsulas por día (producidas + publicadas, por fecha); la 2.ª difiere en tema, estructura, estilo y música
- hora de publicación variable por ventanas (America/Mexico_City)
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
CAMAS = ["pulso", "marimba", "pizzicato", "arpegio", "tambor", "circuito_neural"]
def log(): return json.load(open(LOG)) if os.path.exists(LOG) else []
def _h(s): return int(hashlib.md5(s.encode()).hexdigest(), 16)
def elegir_estructura(tema="", evitar=()):
    u = [x["estructura"] for x in log()]; ops = [e for e in ESTRUCTURAS if (not u or e != u[-1]) and e not in evitar]
    ops.sort(key=lambda e: (u[-4:].count(e), _h(tema + e) % 97)); return ops[0]
def elegir_cama(tema="", evitar=()):
    u = [x.get("cama") for x in log()]; ops = [c for c in CAMAS if c not in u[-2:] and c not in evitar] or [c for c in CAMAS if (not u or c != u[-1]) and c not in evitar] or [c for c in CAMAS if c not in u[-2:]]
    return sorted(ops, key=lambda c: _h(tema + c) % 97)[0]
def duracion_objetivo(tema="", n_fuentes=2):
    """60-95 s según tema: más fuentes/complejidad -> más largo; varía respecto de la anterior."""
    base = 62 + min(n_fuentes, 4) * 6 + _h(tema) % 10; prev = [x.get("duracion") for x in log()][-1:] or [None]
    if prev[0] and abs(base - prev[0]) < 5: base += 7 if base < 85 else -7
    return max(62, min(95, base))
MAX_POR_DIA = 3  # total: 2 propias + 1 externa (ChatGPT vía cola/)
MAX_ORIGEN = {"propia": 2, "externa": 1}
TEMAS = os.path.join(R, "data", "temas_del_dia.json")
def temas_del_dia(fecha=None):
    f = fecha or datetime.date.today().isoformat(); d = json.load(open(TEMAS)) if os.path.exists(TEMAS) else {}
    return d.get(f, [])
def registrar_tema(fecha, tema, origen, project_id):
    """data/temas_del_dia.json: TODA fuente (propia o externa) lo consulta y escribe para no repetir tema el mismo día."""
    d = json.load(open(TEMAS)) if os.path.exists(TEMAS) else {}
    l = d.setdefault(fecha, [])
    if not any(x["project_id"] == project_id for x in l): l.append({"tema": (tema or "").lower(), "origen": origen, "project_id": project_id})
    json.dump(d, open(TEMAS, "w"), ensure_ascii=False, indent=1)
def tema_ocupado(fecha, tema, project_id=None):
    t = (tema or "").lower().strip()
    return any(x["tema"] == t and x["project_id"] != project_id for x in temas_del_dia(fecha)) or any((x.get("tema") or "").lower() == t and x["project_id"] != project_id for x in hecha_hoy(fecha))
PUB = os.path.join(R, "data", "publicaciones.json")
VENTANAS = [(9, 11), (13, 15), (18, 21)]  # horas locales America/Mexico_City
def publicaciones(): return json.load(open(PUB)) if os.path.exists(PUB) else []
def hecha_hoy(fecha=None):
    """Cápsulas del día (unión por project_id de data/rotacion.json y data/publicaciones.json)."""
    f = fecha or datetime.date.today().isoformat(); d = {}
    for x in log() + publicaciones():
        if x.get("fecha") == f: d.setdefault(x["project_id"], {}).update({k: v for k, v in x.items() if v is not None})
    return list(d.values())
def exigir_cupo(fecha=None, origen="propia"):
    h = hecha_hoy(fecha)
    if os.environ.get("CAPCOT_FORZAR_CUPO") == "1": print("AVISO: cupo diario forzado por orden explícita de Mj"); return h
    n = sum(1 for x in h if x.get("origen", "propia") == origen)
    if len(h) >= MAX_POR_DIA: sys.exit(f"LÍMITE DURO: ya hay {len(h)} cápsulas el {fecha or 'hoy'} ({', '.join(x['project_id'] for x in h)}). Máximo {MAX_POR_DIA} por día.")
    if n >= MAX_ORIGEN[origen]: sys.exit(f"LÍMITE DURO: ya hay {n} cápsulas '{origen}' el {fecha or 'hoy'}. Máximo {MAX_ORIGEN[origen]} {origen}(s) por día (2 propias + 1 externa).")
    return h
def diferencias_con_hoy(sb, fecha):
    """Errores si la cápsula repite tema/estructura/estilo/música de otra del mismo día."""
    e = []; tema = (sb.get("trend_source", {}).get("termino") or sb.get("title", "")).lower()
    for x in hecha_hoy(fecha):
        if x.get("project_id") == sb.get("project_id"): e.append("mismo project_id que otra del día"); continue
        if x.get("tema") and x["tema"].lower() == tema: e.append(f"tema repetido ({tema})")
        if x.get("estructura") == sb.get("estructura"): e.append(f"estructura repetida ({x['estructura']})")
        if x.get("estilo") and x["estilo"] == sb.get("estilo_id"): e.append(f"estilo repetido ({x['estilo']})")
        if x.get("cama") and x["cama"] == sb.get("audio", {}).get("cama_musical"): e.append(f"música repetida ({x['cama']})")
    if any(x["tema"] == tema and x["project_id"] != sb.get("project_id") for x in temas_del_dia(fecha)) and not any("tema repetido" in y for y in e): e.append(f"tema repetido en temas_del_dia ({tema})")
    return e
def evitar_hoy(fecha):
    h = hecha_hoy(fecha); ev = {k: {x.get(k) for x in h} - {None} for k in ("tema", "estructura", "estilo", "cama")}
    ev["tema"] |= {x["tema"] for x in temas_del_dia(fecha)}; return ev
def hora_publicacion(fecha, ahora=None, semilla=None):
    """Hora aleatoria dentro de una ventana no usada hoy y >=20 min en el futuro. Devuelve (local_iso, utc_iso 'Z')."""
    import random, zoneinfo
    tz = zoneinfo.ZoneInfo("America/Mexico_City"); ahora = ahora or datetime.datetime.now(tz)
    usadas = {p.get("ventana") for p in publicaciones() if p.get("fecha") == fecha}
    rnd = random.Random(semilla); d = datetime.date.fromisoformat(fecha)
    for i, (h0, h1) in enumerate(VENTANAS):
        if i in usadas: continue
        ini = datetime.datetime(d.year, d.month, d.day, h0, tzinfo=tz); fin = datetime.datetime(d.year, d.month, d.day, h1, tzinfo=tz)
        ini = max(ini, ahora + datetime.timedelta(minutes=20))
        if ini >= fin: continue
        t = ini + datetime.timedelta(seconds=rnd.randint(0, int((fin - ini).total_seconds())))
        t = t.replace(second=0, microsecond=0)
        return t.isoformat(), t.astimezone(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), i
    return None, None, None  # sin ventana disponible hoy
def registrar_publicacion(rec):
    os.makedirs(os.path.dirname(PUB), exist_ok=True); l = publicaciones(); l.append(rec)
    json.dump(l, open(PUB, "w"), ensure_ascii=False, indent=1)
def marcar(fecha, project_id, estructura, cama, duracion, tema=None, estilo=None, origen="propia"):
    os.makedirs(os.path.dirname(LOG), exist_ok=True); l = log()
    l.append({"fecha": fecha, "project_id": project_id, "estructura": estructura, "cama": cama, "duracion": duracion, "tema": tema, "estilo": estilo, "origen": origen})
    json.dump(l, open(LOG, "w"), ensure_ascii=False, indent=1)
if __name__ == "__main__":
    print(json.dumps({"log": log()[-5:], "siguiente": {"estructura": elegir_estructura(), "cama": elegir_cama(), "duracion": duracion_objetivo()}}, ensure_ascii=False, indent=1))
