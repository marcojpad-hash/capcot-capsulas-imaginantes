#!/usr/bin/env python3
"""Orquestador diario CAPCOT: tendencia -> guion -> frames -> validación -> montaje -> QA -> paquete. NO publica.
Uso: python3 scripts/capsula_diaria.py [--storyboard ruta.json] [--proveedor-img manual|xai|openai|placeholder] [--fecha AAAA-MM-DD]
- Sin --storyboard: elige el mejor tema del RSS MX y llama a generar_guion_llm.py (proveedor gratuito: CAPCOT_LLM_PROVIDER=gemini|groq; sin clave -> modo manual).
- Con --storyboard: usa ese guion (lote o manual) y lo copia al paquete.
Paquete: salidas/<fecha>_<slug>/ {storyboard.json, guion.md, fuentes.md, frames/, capsula.mp4, capsula.srt, qa.json, metadata.json, resumen.json, LEEME.md}. Publica solo con --publicar (si QA pasa); --dry-run prueba sin subir ni registrar."""
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
    ap.add_argument("--publicar", action="store_true", help="si QA pasa, sube a YouTube (public, o programado con --programar)")
    ap.add_argument("--programar", action="store_true", help="con --publicar: status.publishAt a hora aleatoria de una ventana libre (9-11, 13-15, 18-21 h CDMX)")
    ap.add_argument("--origen", choices=["propia", "externa"], default="propia", help="externa = guion de otro modelo vía cola/ (procesar_cola.py)")
    ap.add_argument("--dry-run", action="store_true", help="cadena completa sin publicar ni registrar en data/ (prueba)")
    a = ap.parse_args()
    sys.path.insert(0, S); import rotacion
    rotacion.exigir_cupo(a.fecha, a.origen)  # LÍMITE DURO: 3/día = 2 propias + 1 externa (producidas+publicadas; YouTube 2801973: nada de producción masiva)
    ev = rotacion.evitar_hoy(a.fecha)  # la 2.ª del día difiere en tema, estructura, estilo y música
    if a.storyboard: sb = json.load(open(a.storyboard, encoding="utf-8")); src_dir = os.path.dirname(os.path.abspath(a.storyboard))
    else:
        tj = f"/tmp/tendencias_{a.fecha}.json"; sh("python3", f"{S}/tendencias.py", "--json", tj)
        ts = json.load(open(tj)); DEP = re.compile(r"(futbol|fútbol|liga|vs\.?|partido|dortmund|real madrid|barcelona|américa|chivas|cruz azul|pumas|tigres|nfl|nba|mlb|f1|gol|champions)", re.I)
        ts = [x for x in ts if not DEP.search(x["termino"])] or ts  # deportes/marcadores no son cápsula de datos
        t = next((x for x in ts if x["termino"].lower() not in {y.lower() for y in ev["tema"]}), ts[0]); print("TEMA:", t["termino"], t["puntaje"])
        if t["puntaje"] < 6: print("AVISO: puntaje <6; usar backlog atemporal")
        tmp = f"/tmp/sb_{a.fecha}.json"
        est, dobj = rotacion.elegir_estructura(t["termino"], ev["estructura"]), rotacion.duracion_objetivo(t["termino"], len(t.get("noticias", [])))
        rc = subprocess.run(["python3", f"{S}/generar_guion_llm.py", "--estructura", est, "--duracion", str(dobj), "--tema", t["termino"], "--noticias", json.dumps(t["noticias"], ensure_ascii=False), "--id", f"{a.fecha}_{slug(t['termino'])}", "-o", tmp]).returncode
        if rc == 3:
            os.makedirs(os.path.join(R, "salidas", "pendiente"), exist_ok=True)
            shutil.move(os.environ.get("CAPCOT_PROMPT_OUT", "prompt_guion.txt"), os.path.join(R, "salidas", "pendiente", f"prompt_guion_{a.fecha}.txt")) if os.path.exists(os.environ.get("CAPCOT_PROMPT_OUT", "prompt_guion.txt")) else None
            json.dump({"fecha": a.fecha, "estado": "MANUAL", "tema": t["termino"], "estructura": est, "duracion_objetivo": dobj, "prompt": f"salidas/pendiente/prompt_guion_{a.fecha}.txt", "accion": f"AGENTE: escribe salidas/pendiente/storyboard_{a.fecha}.json con ese prompt (estructura={est}, ~{dobj} s, capas mapa+dato/grafico, fuentes verificadas), genera frames/ y reejecuta con --storyboard"}, open(os.path.join(R, "salidas", f"resumen_{a.fecha}.json"), "w"), ensure_ascii=False, indent=1)
            sys.exit("Modo manual: escribe el guion y reejecuta con --storyboard")
        if rc: sys.exit("generar_guion_llm falló")
        sb = json.load(open(tmp)); src_dir = None
    out = os.path.join(R, "salidas", f"{a.fecha}_{slug(sb.get('project_id') if a.storyboard else sb['trend_source']['termino'])}")
    os.makedirs(os.path.join(out, "frames"), exist_ok=True)
    if src_dir and os.path.abspath(src_dir) != os.path.abspath(out):
        for s in sb["scenes"]:
            f = os.path.join(src_dir, s["asset_filename"])
            if os.path.exists(f): shutil.copy(f, os.path.join(out, s["asset_filename"]))
    sys.path.insert(0, S); import rotar_estilo, tendencias_estilos
    if not tendencias_estilos.vigente():
        try: tendencias_estilos.actualizar()  # DIARIO: pesos de viralidad
        except Exception as ex: print('tendencias no actualizadas:', ex)
    if not a.estilo and not sb.get("estilo_id") and ev["estilo"]:
        a.estilo = next(e for _, e, _ in rotar_estilo.ranking(sb.get("trend_source", {}).get("termino", sb.get("title", ""))) if e not in ev["estilo"])
    sb = rotar_estilo.aplicar_estilo(sb, a.estilo)
    tema = sb.get("trend_source", {}).get("termino", sb.get("title", ""))
    u = [x["estructura"] for x in rotacion.log()]
    if not sb.get("estructura") or (u and sb["estructura"] == u[-1]):
        if sb.get("estructura"): sys.exit(f"estructura '{sb['estructura']}' repetida respecto de la cápsula anterior: reescribe el guion con {rotacion.elegir_estructura(tema)}")
        sb["estructura"] = rotacion.elegir_estructura(tema, ev["estructura"])
    sb.setdefault("target_duration_seconds", rotacion.duracion_objetivo(tema, len(sb.get("sources", []))))
    aud = sb.setdefault("audio", {})
    if not aud.get("music_asset") or aud["music_asset"].startswith("sintetico"):
        aud["music_asset"] = "sintetico:" + rotacion.elegir_cama(tema, ev["cama"]); aud["cama_musical"] = aud["music_asset"].split(":")[1]  # elige estilo por temática + tendencia, sin repetir el anterior; respeta estilo_id/--estilo
    sb.setdefault("canal", {"nombre": "Datos y ociosidades", "handle": "@datosyociosidades", "youtube_channel_id": "UCU2ZI-6pBJEr9aSFsF6bxLw"})
    sb.setdefault("cortinilla_fuentes", {}).setdefault("firma", "Datos y ociosidades · @datosyociosidades")
    sb["origen"] = a.origen
    dif = rotacion.diferencias_con_hoy(sb, a.fecha)
    if os.environ.get("CAPCOT_FORZAR_CUPO") == "1": dif = [d for d in dif if d.startswith(("tema", "estilo"))]  # cupo forzado: solo tema/estilo deben diferir
    if dif: sys.exit("La cápsula repite respecto de la otra de hoy: " + "; ".join(dif))
    sbp = os.path.join(out, "storyboard.json"); json.dump(sb, open(sbp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    sh("python3", f"{S}/generar_frames.py", sbp, "--proveedor", a.proveedor_img)
    sh("python3", f"{S}/validar_storyboard.py", sbp, "--check-doi")
    sh("python3", f"{S}/montar_capsula.py", sbp, "-o", os.path.join(out, "capsula.mp4"))
    qa = sh("python3", f"{S}/qa_capsula.py", os.path.join(out, "capsula.mp4"), sbp, ok=(0, 1))
    open(os.path.join(out, "guion.md"), "w").write(guion_md(sb)); open(os.path.join(out, "fuentes.md"), "w").write(fuentes_md(sb))
    sh("python3", f"{S}/metadata.py", out)  # metadata.json: descripción + hashtags + canal
    # guion_mj.py DESCONECTADO 2026-10-24 (Mj: era de otro proyecto). Ver docs/obsoleto/guion_mj.py
    tema = sb.get("trend_source", {}).get("termino", sb.get("title", ""))
    if not a.dry_run:
        rotar_estilo.marcar(sb["estilo_id"], sb.get("project_id", out))
        rotacion.marcar(a.fecha, sb.get("project_id", out), sb["estructura"], sb["audio"].get("cama_musical", "externa"), sb.get("target_duration_seconds"), tema, sb["estilo_id"], a.origen)
        rotacion.registrar_tema(a.fecha, tema, a.origen, sb.get("project_id", os.path.basename(out)))
        sh("python3", f"{S}/metricas.py", "registrar", out)
    pub = {"publicado": False}
    if a.publicar and qa != 0:
        pub = {"publicado": False, "motivo": "QA falló: NO se publica", "fallas": [r for r in json.load(open(os.path.join(out, "qa.json"))) if not r["ok"]]}
        print("NO SE PUBLICA: QA falló", pub["fallas"])
    elif a.publicar:
        cmd = ["python3", f"{S}/publicar.py", out + "/", "--plataforma", "yt", "--privacidad", "public"]
        loc = utc = ven = None
        if a.programar:
            loc, utc, ven = rotacion.hora_publicacion(a.fecha)
            if utc: cmd += ["--publish-at", utc]
            else: print("sin ventana libre hoy: se publica inmediato")
        if not a.dry_run: cmd.append("--ejecutar")
        r = subprocess.run(cmd, capture_output=True, text=True); print(r.stdout[-1500:], r.stderr[-1500:])
        yid = next((l.split()[1] for l in r.stdout.splitlines() if l.startswith("YT_ID ")), None)
        pub = {"publicado": bool(yid), "dry_run": a.dry_run, "yt_id": yid, "publishAt_utc": utc, "hora_local": loc, "ventana": ven, "rc": r.returncode,
               **({"error": (r.stderr or r.stdout)[-800:]} if r.returncode else {})}
        if yid:
            rotacion.registrar_publicacion({"fecha": a.fecha, "project_id": sb.get("project_id", os.path.basename(out)), "yt_id": yid, "url": f"https://youtube.com/shorts/{yid}",
                "privacidad": "private→public (publishAt)" if utc else "public", "publishAt_utc": utc, "hora_local": loc, "ventana": ven,
                "titulo": sb["title"], "tema": tema, "origen": a.origen, "tiktok": "pendiente_tiktok", "estructura": sb["estructura"], "estilo": sb["estilo_id"], "cama": sb["audio"].get("cama_musical")})
    md = json.load(open(os.path.join(out, "metadata.json"), encoding="utf-8"))
    tk = {"estado": "pendiente_tiktok" if qa == 0 else "bloqueado_qa", "mp4": os.path.join(out, "capsula.mp4"), "caption": md["tiktok_caption"],
          "hashtags": md.get("tiktok_hashtags", []), "descripcion_completa": md.get("tiktok_descripcion_completa"), "cuenta": "@datosyociosidades",
          "hora_sugerida_local": pub.get("hora_local"), "yt_id": pub.get("yt_id"),
          "instruccion": "Agente principal: subir por navegador (agente de escritorio) con este caption; al terminar poner estado='publicado_tiktok' y url."}
    json.dump(tk, open(os.path.join(out, "tiktok.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    pub["tiktok"] = tk["estado"]
    open(os.path.join(out, "LEEME.md"), "w").write(f"Paquete {os.path.basename(out)} · QA {'OK' if qa == 0 else 'CON FALLAS (ver qa.json)'} · {'PUBLICADO ' + str(pub.get('yt_id')) if pub.get('publicado') else 'NO publicado'}.\n")
    qj = json.load(open(os.path.join(out, "qa.json"))) if os.path.exists(os.path.join(out, "qa.json")) else {}
    res = {"fecha": a.fecha, "paquete": out, "titulo": sb["title"], "estilo": sb.get("estilo_id"), "qa_ok": qa == 0, "qa": qj,
           "archivos": sorted(os.listdir(out)), **pub,
           "comando_subida_manual": f"python3 scripts/publicar.py {os.path.relpath(out, R)}/ --plataforma yt --privacidad public --ejecutar",
           "estructura": sb["estructura"], "cama_musical": sb["audio"].get("cama_musical"),
           "tiktok_json": os.path.join(out, "tiktok.json")}
    json.dump(res, open(os.path.join(out, "resumen.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("PAQUETE:", out, "QA_OK" if qa == 0 else "QA_FALLAS")
