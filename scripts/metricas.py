#!/usr/bin/env python3
"""Métricas -> SQLite (data/metricas.db) y puntaje del PLAN_MAESTRO §7.
  registrar: python3 scripts/metricas.py registrar <dir_salida>   (guarda tema, estilo, gancho, duración)
  recolectar: python3 scripts/metricas.py recolectar [--dry-run]  (YouTube Analytics con CAPCOT_YT_TOKEN; TikTok video.list con CAPCOT_TIKTOK_ACCESS_TOKEN)
  reporte:   python3 scripts/metricas.py reporte
  metas:     python3 scripts/metricas.py metas [subs_actuales vistas_shorts_90d horas_largos_12m]  (metas semanales hacia el YPP, fecha límite 2026-12-05)
Sin credenciales, 'recolectar' solo informa qué falta."""
import json, os, sqlite3, sys, datetime
DB = os.path.join(os.path.dirname(__file__), "..", "data", "metricas.db")
def con():
    os.makedirs(os.path.dirname(DB), exist_ok=True); c = sqlite3.connect(DB)
    c.execute("create table if not exists capsulas(id text primary key, fecha text, tema text, estilo text, gancho text, duracion real, yt_id text, tt_id text)")
    c.execute("create table if not exists metricas(id text, plataforma text, ts text, vistas int, retencion real, likes int, comentarios int, compartidos int, guardados int, subs int)")
    return c
# YouTube Partner Program (verificado por web 2026-10-24, support.google.com/youtube/answer/72851):
YPP = {"ruta_shorts": "1,000 suscriptores + 10,000,000 vistas válidas de Shorts públicos en los últimos 90 días",
       "ruta_largos": "1,000 suscriptores + 4,000 horas de visualización válidas de videos largos públicos en 12 meses (las horas de Shorts NO cuentan)",
       "otros": "políticas de monetización, país elegible, sin strikes, verificación en 2 pasos, funciones avanzadas, AdSense vinculado; revisión ~1 mes"}
# Metas semanales (agresivas, 1-2 cápsulas/día + 1-2 largos recopilatorios) hasta el 5 dic 2026:
# (fin de semana, subs acumulados, vistas Shorts esa semana, vistas Shorts acumuladas, horas de largos acumuladas)
METAS = [("2026-10-31", 60, 15000, 15000, 0), ("2026-11-07", 150, 40000, 55000, 5), ("2026-11-14", 280, 90000, 145000, 30),
         ("2026-11-21", 450, 180000, 325000, 80), ("2026-11-28", 700, 320000, 645000, 160), ("2026-12-05", 1000, 500000, 1145000, 300)]
# Realidad: 1,000 subs al 5 dic es la meta alcanzable; 10M vistas/90 d o 4,000 h requieren un viral o más meses.
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
    elif cmd == "metas":
        act = [float(x) for x in sys.argv[2:5]] + [0, 0, 0][len(sys.argv[2:5]):]
        print("Requisitos YPP verificados 2026-10-24 en support.google.com/youtube/answer/72851:")
        for k, v in YPP.items(): print(f"  {k}: {v}")
        print("\nSemana (cierra)   subs acum  vistas Shorts semana  vistas Shorts acum  horas largos acum")
        for f, su, vs, va, h in METAS:
            print(f"  {f}     {su:>6}      {vs:>10,}       {va:>12,}       {h:>6}")
        hoy = datetime.date.today().isoformat(); m = next((x for x in METAS if x[0] >= hoy), METAS[-1])
        print(f"\nMeta vigente ({m[0]}): {m[1]} subs, {m[3]:,} vistas Shorts acum., {m[4]} h largos. Actual: {act[0]:.0f} subs, {act[1]:,.0f} vistas, {act[2]:.0f} h")
        print("  ->", "EN META" if act[0] >= m[1] and act[1] >= m[3] else "POR DEBAJO: subir frecuencia (2/día), reforzar ganchos y temas con tendencia")
    else:
        c.row_factory = sqlite3.Row
        for r in c.execute("select * from metricas"): print(r["id"], r["plataforma"], round(puntaje(r), 4))
        print("capsulas registradas:", c.execute("select count(*) from capsulas").fetchone()[0])
