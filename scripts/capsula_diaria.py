#!/usr/bin/env python3
"""Orquestador diario CAPCOT: tendencia -> guion -> frames -> validación -> montaje -> QA -> paquete. NO publica.
Uso: python3 scripts/capsula_diaria.py [--storyboard ruta.json] [--proveedor-img manual|xai|openai|placeholder] [--fecha AAAA-MM-DD]
- Sin --storyboard: elige el mejor tema del RSS MX y llama a generar_guion_llm.py (requiere CAPCOT_LLM_API_KEY).
- Con --storyboard: usa ese guion (lote o manual) y lo copia al paquete.
Paquete: salidas/<fecha>_<slug>/ {storyboard.json, guion.md, fuentes.md, frames/, capsula.mp4, capsula.srt, qa.json, publicacion.json(dry-run), LEEME.md}"""
import argparse, datetime, json, os, re, shutil, subprocess, sys, unicodedata
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); S = os.path.join(R, "scripts")
def sh(*a, ok=(0,)):
    print("$", " ".join(a)); p = subprocess.run(a); 
    if p.returncode not in ok: sys.exit(f"falló ({p.returncode}): {a[1]}")
    return p.returncode
def slug(t): return re.sub(r"[^a-z0-9]+", "-", unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower()).strip("-")[:40]
def guion_md(sb):
    L = [f"# {sb['title']}", f"Tema/tendencia: {sb.get('trend_source',{}).get('termino','')} · Estilo: {sb.get('estilo_visual','')}", ""]
    for s in sb["scenes"]: L += [f"**{s['id']} · {s['arc']} · {s['duration_seconds']} s**", f"- VOZ: {s['narration'] or '(silencio: la imagen narra)'}", f"- TEXTO: {s.get('on_screen_text','')}", f"- IMAGEN: {s.get('visual_description','')}", ""]
    return "\n".join(L)
def fuentes_md(sb): return "# Fuentes (verificadas)\n\n" + "\n".join(f"- [{s['id']}] {s['cita_corta']} {s['url']} (consulta {s.get('accessed','')}) — respalda: {'; '.join(s.get('supports',[]))}" for s in sb["sources"])
if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--storyboard"); ap.add_argument("--proveedor-img", default="manual"); ap.add_argument("--fecha", default=datetime.date.today().isoformat()); ap.add_argument("--estilo", default=None)
    a = ap.parse_args()
    if a.storyboard: sb = json.load(open(a.storyboard, encoding="utf-8")); src_dir = os.path.dirname(os.path.abspath(a.storyboard))
    else:
        tj = f"/tmp/tendencias_{a.fecha}.json"; sh("python3", f"{S}/tendencias.py", "--json", tj)
        t = json.load(open(tj))[0]; print("TEMA:", t["termino"], t["puntaje"])
        if t["puntaje"] < 6: print("AVISO: puntaje <6; usar backlog atemporal")
        tmp = f"/tmp/sb_{a.fecha}.json"
        rc = subprocess.run(["python3", f"{S}/generar_guion_llm.py", "--tema", t["termino"], "--noticias", json.dumps(t["noticias"], ensure_ascii=False), "--id", f"{a.fecha}_{slug(t['termino'])}", "-o", tmp]).returncode
        if rc == 3: sys.exit("Sin CAPCOT_LLM_API_KEY: escribe el guion a mano (o con el bot) y reejecuta con --storyboard")
        if rc: sys.exit("generar_guion_llm falló")
        sb = json.load(open(tmp)); src_dir = None
    out = os.path.join(R, "salidas", f"{a.fecha}_{slug(sb.get('project_id') if a.storyboard else sb['trend_source']['termino'])}")
    os.makedirs(os.path.join(out, "frames"), exist_ok=True)
    if src_dir and os.path.abspath(src_dir) != os.path.abspath(out):
        for s in sb["scenes"]:
            f = os.path.join(src_dir, s["asset_filename"])
            if os.path.exists(f): shutil.copy(f, os.path.join(out, s["asset_filename"]))
    sys.path.insert(0, S); import rotar_estilo
    sb = rotar_estilo.aplicar_estilo(sb, a.estilo)  # rota estilos (scripts/estilos.json); respeta estilo_id si ya viene
    sb.setdefault("canal", {"nombre": "Datos y ociosidades", "handle": "@datosyociosidades", "youtube_channel_id": "UCU2ZI-6pBJEr9aSFsF6bxLw"})
    sb.setdefault("cortinilla_fuentes", {}).setdefault("firma", "Datos y ociosidades · @datosyociosidades")
    sbp = os.path.join(out, "storyboard.json"); json.dump(sb, open(sbp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    sh("python3", f"{S}/generar_frames.py", sbp, "--proveedor", a.proveedor_img)
    sh("python3", f"{S}/validar_storyboard.py", sbp, "--check-doi")
    sh("python3", f"{S}/montar_capsula.py", sbp, "-o", os.path.join(out, "capsula.mp4"))
    qa = sh("python3", f"{S}/qa_capsula.py", os.path.join(out, "capsula.mp4"), sbp, ok=(0, 1))
    open(os.path.join(out, "guion.md"), "w").write(guion_md(sb)); open(os.path.join(out, "fuentes.md"), "w").write(fuentes_md(sb))
    sh("python3", f"{S}/metadata.py", out)  # metadata.json: descripción + hashtags + canal
    sh("python3", f"{S}/publicar.py", out)  # dry-run
    rotar_estilo.marcar(sb["estilo_id"], sb.get("project_id", out))
    sh("python3", f"{S}/metricas.py", "registrar", out)
    open(os.path.join(out, "LEEME.md"), "w").write(f"Paquete {os.path.basename(out)} · QA {'OK' if qa == 0 else 'CON FALLAS (ver qa.json)'} · NO publicado (publicar.py --ejecutar requiere aprobación y cuentas de Mj).\n")
    print("PAQUETE:", out, "QA_OK" if qa == 0 else "QA_FALLAS")
