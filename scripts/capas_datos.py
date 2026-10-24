#!/usr/bin/env python3
"""Capas informativas animadas (no solo Ken Burns): mapa, gráfico y dato grande. Render con matplotlib -> mp4.
Campo por escena en el storyboard: scenes[].capa = {"tipo": "mapa"|"grafico"|"dato", "plano": índice (def. último), ...}
  mapa:    {"region": [lon0, lon1, lat0, lat1], "puntos": [{"nombre","lon","lat"}], "flechas": [[lon,lat,lon,lat,"etiqueta"]], "titulo"}
  grafico: {"x": [...], "y": [...], "titulo", "unidad", "fuente"}  (línea que se dibuja progresivamente)
  dato:    {"valor": "+0.5 °C", "etiqueta": "umbral de El Niño (NOAA)", "fuente"}
Mapa base: Natural Earth 110m (dominio público), descargado a assets/geo/ (gitignored) por scripts/descargar_geo.sh."""
import json, os, subprocess, tempfile
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W, H, FPS, DPI = 1080, 1920, 30, 120
PAPEL, TINTA, ACENTO, AGUA = "#efe6d2", "#1f2a44", "#d9a441", "#c9d6df"
FONT = "DejaVu Sans"

def _fig():
    f = plt.figure(figsize=(W / DPI, H / DPI), dpi=DPI); f.patch.set_facecolor(PAPEL); return f

def _texto(f, titulo, fuente=""):
    if titulo: f.text(0.08, 0.86, titulo, fontsize=30, weight="bold", color=TINTA, family=FONT, wrap=True)
    if fuente: f.text(0.08, 0.24, "Fuente: " + fuente, fontsize=15, color="#555", family=FONT)

def _mapa(f, c, p):
    ax = f.add_axes([0.04, 0.36, 0.92, 0.46]); ax.set_facecolor(AGUA)
    gj = json.load(open(os.path.join(R, "assets", "geo", "ne_110m_land.geojson")))
    for ft in gj["features"]:
        g = ft["geometry"]; polys = g["coordinates"] if g["type"] == "MultiPolygon" else [g["coordinates"]]
        for poly in polys:
            for ring in poly[:1]:
                xs, ys = zip(*ring); ax.fill(xs, ys, color="#e0cfa4", ec=TINTA, lw=1)
                ax.fill([x + 360 for x in xs], ys, color="#e0cfa4", ec=TINTA, lw=1)  # para Pacífico centrado
    lo0, lo1, la0, la1 = c.get("region", [90, 300, -35, 35]); ax.set_xlim(lo0, lo1); ax.set_ylim(la0, la1)
    ax.set_xticks([]); ax.set_yticks([]); [s.set_color(TINTA) for s in ax.spines.values()]
    for pt in c.get("puntos", []):
        if p > 0.15:
            ax.plot(pt["lon"], pt["lat"], "o", ms=14, color=ACENTO, mec=TINTA, mew=2)
            ax.text(pt["lon"], pt["lat"] + 3, pt["nombre"], fontsize=20, weight="bold", color=TINTA, ha="center", family=FONT)
    for fl in c.get("flechas", []):
        x0, y0, x1, y1 = fl[:4]; q = min(1, max(0, (p - 0.3) / 0.5))
        if q > 0:
            ax.add_patch(FancyArrowPatch((x0, y0), (x0 + (x1 - x0) * q, y0 + (y1 - y0) * q), arrowstyle="-|>", mutation_scale=40, lw=5, color="#b5462f"))
            if len(fl) > 4 and q >= 1: ax.text((x0 + x1) / 2, (y0 + y1) / 2 - 5, fl[4], fontsize=20, color="#b5462f", ha="center", weight="bold", family=FONT)

def _grafico(f, c, p):
    ax = f.add_axes([0.12, 0.36, 0.8, 0.42]); ax.set_facecolor(PAPEL)
    x, y = c["x"], c["y"]; k = max(2, int(len(x) * min(1, p / 0.8)))
    ax.plot(x[:k], y[:k], color=TINTA, lw=5); ax.fill_between(x[:k], y[:k], min(y), color=ACENTO, alpha=.35)
    ax.set_xlim(min(x), max(x)); ax.set_ylim(min(y) - 0.1 * abs(max(y) - min(y)), max(y) * 1.1)
    ax.tick_params(labelsize=18, colors=TINTA); [s.set_color(TINTA) for s in ax.spines.values()]
    ax.spines[["top", "right"]].set_visible(False)
    if c.get("unidad"): ax.set_ylabel(c["unidad"], fontsize=20, color=TINTA)

def _dato(f, c, p):
    s = min(1, p / 0.35); f.text(0.5, 0.55, c["valor"], fontsize=40 + 60 * s, weight="bold", color=TINTA, ha="center", family=FONT, alpha=s)
    if p > 0.3: f.text(0.5, 0.45, c.get("etiqueta", ""), fontsize=28, color=TINTA, ha="center", family=FONT, wrap=True)

def render_capa(c, seconds, out_mp4):
    tmpd = tempfile.mkdtemp(prefix="capa_"); n = int(round(seconds * FPS)); step = 2  # 15 fps de dibujo, duplicados a 30
    for i in range(0, n, step):
        p = i / max(n - 1, 1); f = _fig()
        {"mapa": _mapa, "grafico": _grafico, "dato": _dato}[c["tipo"]](f, c, p)
        _texto(f, c.get("titulo", ""), c.get("fuente", "")); f.savefig(os.path.join(tmpd, f"{i // step:04d}.png"), dpi=DPI, facecolor=PAPEL); plt.close(f)
    subprocess.run(["ffmpeg", "-y", "-framerate", str(FPS / step), "-i", os.path.join(tmpd, "%04d.png"), "-vf", f"scale={W}:{H},fps={FPS},format=yuv420p",
                    "-frames:v", str(n), "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-r", str(FPS), out_mp4], check=True, capture_output=True)
