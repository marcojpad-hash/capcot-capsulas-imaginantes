#!/usr/bin/env python3
"""Cola de publicación para guiones EXTERNOS (p. ej. ChatGPT con docs/RECETA_CAPSULA.md). Ver docs/FLUJO_EXTERNO.md.
Entrada: cola/entrada/<id>.json  o  cola/entrada/<id>/storyboard.json (+ frames/ opcional).
Uso: python3 scripts/procesar_cola.py [--publicar --programar] [--dry-run] [--fecha AAAA-MM-DD] [--proveedor-img manual]
Flujo: validar (esquema + DOI + tema libre en data/temas_del_dia.json + cupo externo 1/día) -> mover a cola/<fecha>_<id>/
-> capsula_diaria.py --storyboard ... --origen externa (render, QA, metadata, tiktok.json, publicación si QA pasa)."""
import argparse, datetime, glob, json, os, shutil, subprocess, sys
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); S = os.path.join(R, "scripts"); sys.path.insert(0, S)
import rotacion
COLA = os.path.join(R, "data", "cola.json")
def cola(): return json.load(open(COLA)) if os.path.exists(COLA) else []
def guardar(l): json.dump(l, open(COLA, "w"), ensure_ascii=False, indent=1)
def upd(l, pid, **k):
    for x in l:
        if x["id"] == pid: x.update(k); x["actualizado"] = datetime.datetime.now().isoformat(timespec="seconds")
    guardar(l)
if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--fecha", default=datetime.date.today().isoformat())
    ap.add_argument("--publicar", action="store_true"); ap.add_argument("--programar", action="store_true"); ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--proveedor-img", default="manual"); a = ap.parse_args()
    ent = sorted(glob.glob(os.path.join(R, "cola", "entrada", "*.json")) + glob.glob(os.path.join(R, "cola", "entrada", "*", "storyboard.json")))
    if not ent: sys.exit("cola/entrada/ vacía")
    def fecha_archivo(path):
        nombre = os.path.basename(path)
        if nombre == "storyboard.json":
            nombre = os.path.basename(os.path.dirname(path))
        return nombre[:10]
    candidatas = [p for p in ent if fecha_archivo(p) == a.fecha]
    if not candidatas:
        antiguas = ", ".join(os.path.relpath(p, R) for p in ent[:8])
        sys.exit(f"Sin entrada para {a.fecha}; no se procesan colas antiguas automáticamente. Entradas existentes: {antiguas}")
    l = cola(); f = candidatas[0]  # solo una externa del día; nunca consumir la cola histórica más antigua
    sb = json.load(open(f, encoding="utf-8")); pid = sb.get("project_id") or os.path.splitext(os.path.basename(f))[0]
    tema = sb.get("trend_source", {}).get("termino") or sb.get("title", "")
    if not any(x["id"] == pid for x in l): l.append({"id": pid, "fecha": a.fecha, "origen": "externa", "tema": tema, "estado": "recibido", "entrada": os.path.relpath(f, R)}); guardar(l)
    if rotacion.tema_ocupado(a.fecha, tema, pid): upd(l, pid, estado="rechazado", motivo=f"tema '{tema}' ya usado hoy (data/temas_del_dia.json)"); sys.exit(f"RECHAZADO: tema repetido hoy: {tema}")
    dst = os.path.join(R, "cola", f"{a.fecha}_{pid}"); os.makedirs(dst, exist_ok=True)
    src = os.path.dirname(f) if os.path.basename(f) == "storyboard.json" else None
    if src: shutil.copytree(src, dst, dirs_exist_ok=True)
    else: shutil.copy(f, os.path.join(dst, "storyboard.json"))
    sbp = os.path.join(dst, "storyboard.json")
    v = subprocess.run(["python3", f"{S}/validar_storyboard.py", sbp, "--check-doi"])
    if v.returncode: upd(l, pid, estado="invalido", motivo="validar_storyboard falló (ver salida)"); sys.exit("storyboard externo inválido; queda en cola/ para corregir")
    upd(l, pid, estado="validado", carpeta=os.path.relpath(dst, R))
    if not a.dry_run:  # sale de entrada/ solo en corrida real
        shutil.rmtree(src) if src else os.remove(f)
    cmd = ["python3", f"{S}/capsula_diaria.py", "--storyboard", sbp, "--origen", "externa", "--fecha", a.fecha, "--proveedor-img", a.proveedor_img]
    cmd += [x for x, on in (("--publicar", a.publicar), ("--programar", a.programar), ("--dry-run", a.dry_run)) if on]
    rc = subprocess.run(cmd).returncode
    res = sorted(glob.glob(os.path.join(R, "salidas", f"{a.fecha}_*", "resumen.json")), key=os.path.getmtime)
    r = json.load(open(res[-1])) if res and rc == 0 else {}
    upd(l, pid, estado=("publicado_yt+pendiente_tiktok" if r.get("publicado") else "renderizado+pendiente_tiktok" if r.get("qa_ok") else "fallo"),
        rc=rc, paquete=os.path.relpath(r["paquete"], R) if r.get("paquete") else None, yt_id=r.get("yt_id"), qa_ok=r.get("qa_ok"))
    print("COLA:", pid, "rc", rc)
