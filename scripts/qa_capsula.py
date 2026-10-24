#!/usr/bin/env python3
"""Compuertas automáticas (PLAN_MAESTRO §5) sobre un MP4 renderizado + su storyboard.
Uso: python3 scripts/qa_capsula.py salida.mp4 storyboard.json  -> escribe qa.json junto al mp4; código 0 si pasa."""
import json, os, re, subprocess, sys
mp4, sbp = sys.argv[1], sys.argv[2]; sb = json.load(open(sbp, encoding="utf-8")); R = []
def ok(n, c, d=""): R.append({"check": n, "ok": bool(c), "detalle": d})
pr = json.loads(subprocess.check_output(["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", mp4]))
v = next(s for s in pr["streams"] if s["codec_type"] == "video"); a = [s for s in pr["streams"] if s["codec_type"] == "audio"]
d = float(pr["format"]["duration"])
ok("duracion_60_95", 60 <= d <= 95, f"{d:.2f}s"); ok("resolucion_1080x1920", (v["width"], v["height"]) == (1080, 1920))
ok("h264_aac", v["codec_name"] == "h264" and a and a[0]["codec_name"] == "aac"); ok("fps_30", v["r_frame_rate"] == "30/1", v["r_frame_rate"])
e = subprocess.run(["ffmpeg", "-i", mp4, "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True).stderr
I = float(re.findall(r"I:\s+(-?[\d.]+) LUFS", e)[-1]); ok("loudness_-14", abs(I + 14) <= 1, f"{I} LUFS")
srt = os.path.splitext(mp4)[0] + ".srt"
if os.path.exists(srt):
    bl = [b.split("\n") for b in open(srt, encoding="utf-8").read().strip().split("\n\n")]
    ok("subs_max_3_palabras", all(len(" ".join(b[2:]).split()) <= 3 for b in bl), f"{len(bl)} bloques")
else: ok("subs_existen", False)
ok("fuentes_1_4", 1 <= len(sb["sources"]) <= 4); ok("aviso_ia", "IA" in sb["cortinilla_fuentes"].get("aviso", ""))
arcs = [s["arc"] for s in sb["scenes"]]; ok("arco", arcs[0] == "hook_medias_res" and arcs[-1] == "reflexion_o_pregunta")
# Regla de pausas (feedback Mj 2026-10-24): narración casi continua, sin huecos >0.9 s entre subtítulos
import re as _re, os as _os
_srt = _os.path.splitext(sys.argv[1])[0] + ".srt"
def _t(x): h, m, r = x.split(":"); s_, ms = r.split(","); return int(h)*3600 + int(m)*60 + int(s_) + int(ms)/1000
_bl = _re.findall(r"(\d\d:\d\d:\d\d,\d+) --> (\d\d:\d\d:\d\d,\d+)", open(_srt).read()) if _os.path.exists(_srt) else []
_gaps = [_t(_bl[i+1][0]) - _t(_bl[i][1]) for i in range(len(_bl)-1)]
_mx = max(_gaps) if _gaps else 0
ok("sin_huecos_voz_<=0.9s", _mx <= 0.9, f"hueco máx {_mx:.2f}s")
pal = sum(len(s["narration"].split()) for s in sb["scenes"]); ok("voz_<=240_palabras", pal <= 240, f"{pal} palabras")
json.dump(R, open(os.path.join(os.path.dirname(os.path.abspath(mp4)), "qa.json"), "w"), ensure_ascii=False, indent=1)
for r in R: print(("PASA " if r["ok"] else "FALLA"), r["check"], r["detalle"])
sys.exit(0 if all(r["ok"] for r in R) else 1)
