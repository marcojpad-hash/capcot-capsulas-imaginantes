#!/usr/bin/env python3
"""Métricas -> SQLite (data/metricas.db) y puntaje del PLAN_MAESTRO §7.
  registrar: python3 scripts/metricas.py registrar <dir_salida>   (guarda tema, estilo, gancho, duración)
  recolectar: python3 scripts/metricas.py recolectar [--dry-run]  (YouTube Analytics con CAPCOT_YT_TOKEN; TikTok video.list con CAPCOT_TIKTOK_ACCESS_TOKEN)
  reporte:   python3 scripts/metricas.py reporte
Sin credenciales, 'recolectar' solo informa qué falta."""
import json, os, sqlite3, sys, datetime
DB = os.path.join(os.path.dirname(__file__), "..", "data", "metricas.db")
def con():
    os.makedirs(os.path.dirname(DB), exist_ok=True); c = sqlite3.connect(DB)
    c.execute("create table if not exists capsulas(id text primary key, fecha text, tema text, estilo text, gancho text, duracion real, yt_id text, tt_id text)")
    c.execute("create table if not exists metricas(id text, plataforma text, ts text, vistas int, retencion real, likes int, comentarios int, compartidos int, guardados int, subs int)")
    return c
def puntaje(r):
    v = max(r["vistas"] or 1, 1)
    return 0.4 * (r["retencion"] or 0) / 100 + 0.3 * ((r["compartidos"] or 0) + (r["guardados"] or 0)) / v + 0.2 * (r["comentarios"] or 0) / v + 0.1 * (r["subs"] or 0) / v
if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "reporte"; c = con()
    if cmd == "registrar":
        d = sys.argv[2]; sb = json.load(open(os.path.join(d, "storyboard.json"), encoding="utf-8"))
        qa = {}
        c.execute("insert or replace into capsulas values(?,?,?,?,?,?,?,?)", (sb["project_id"], datetime.date.today().isoformat(),
                  sb.get("trend_source", {}).get("termino", sb["title"]), sb.get("estilo_visual", ""), sb["scenes"][0].get("on_screen_text", ""),
                  sum(s["duration_seconds"] for s in sb["scenes"]), None, None)); c.commit(); print("registrada", sb["project_id"])
    elif cmd == "recolectar":
        falt = [k for k in ("CAPCOT_YT_TOKEN", "CAPCOT_TIKTOK_ACCESS_TOKEN") if not os.environ.get(k)]
        if falt: print("Sin credenciales, no se recolecta:", ", ".join(falt)); sys.exit(0)
        print("TODO con credenciales: youtubeAnalytics.reports.query(ids=channel==MINE, metrics=views,averageViewPercentage,likes,comments,shares,subscribersGained, filters=video==<yt_id>) y TikTok POST /v2/video/query/")
    else:
        c.row_factory = sqlite3.Row
        for r in c.execute("select * from metricas"): print(r["id"], r["plataforma"], round(puntaje(r), 4))
        print("capsulas registradas:", c.execute("select count(*) from capsulas").fetchone()[0])
