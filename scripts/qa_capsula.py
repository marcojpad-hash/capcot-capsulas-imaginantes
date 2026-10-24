#!/usr/bin/env python3
"""Compuertas automáticas (PLAN_MAESTRO §5) sobre un MP4 renderizado + su storyboard.
Uso: python3 scripts/qa_capsula.py salida.mp4 storyboard.json  -> escribe qa.json junto al mp4; código 0 si pasa."""
import json, os, re, subprocess, sys
mp4, sbp = sys.argv[1], sys.argv[2]; sb = json.load(open(sbp, encoding="utf-8")); R = []
def ok(n, c, d=""): R.append({"check": n, "ok": bool(c), "detalle": d})
pr = json.loads(subprocess.check_output(["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", mp4]))
v = next(s for s in pr["streams"] if s["codec_type"] == "video"); a = [s for s in pr["streams"] if s["codec_type"] == "audio"]
d = float(pr["format"]["duration"])
ok("duracion_>=60_<=120", 60 <= d <= 120, f"{d:.2f}s (objetivo {sb.get('target_duration_seconds', '?')})"); ok("resolucion_1080x1920", (v["width"], v["height"]) == (1080, 1920))
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
# Cobertura de subtítulos (feedback Mj 11:06): 100 % del guion, sin solapes, y ASS dentro de cuadro
def _norm_w(t): return [w for w in _re.sub(r"[^\wáéíóúüñ]+", " ", t.lower()).split() if w]
_guion = _norm_w(" ".join(s["narration"] for s in sb["scenes"]))
_subs = _norm_w(" ".join(" ".join(b.split("\n")[2:]) for b in open(_srt, encoding="utf-8").read().strip().split("\n\n"))) if _os.path.exists(_srt) else []
import difflib as _dl
_m = sum(b.size for b in _dl.SequenceMatcher(None, _guion, _subs, autojunk=False).get_matching_blocks())
_cov = _m / max(len(_guion), 1); ok("subs_cobertura_>=99%", _cov >= 0.99, f"{_cov*100:.1f}% ({_m}/{len(_guion)} palabras)")
_ov = [i for i in range(len(_bl)-1) if _t(_bl[i+1][0]) < _t(_bl[i][1])]
ok("subs_sin_solapes", not _ov, f"{len(_ov)} solapes")
_ass = _os.path.splitext(sys.argv[1])[0] + ".ass"
if _os.path.exists(_ass):
    _a = open(_ass, encoding="utf-8").read(); _py = int(_re.search(r"PlayResY:\s*(\d+)", _a).group(1))
    _mv = int(_a.split("Style: Sub,")[1].split("\n")[0].split(",")[-2])
    ok("subs_en_cuadro_zona_segura", _py == 1920 and 1920*0.20 <= _mv <= 1920*0.55, f"PlayResY {_py}, MarginV {_mv}")
else: ok("subs_ass_existe", False, "sin .ass (SRT con PlayResY 288 saca el texto de cuadro)")
pal = sum(len(s["narration"].split()) for s in sb["scenes"]); ok("voz_<=240_palabras", pal <= 240, f"{pal} palabras")
# Reglas anti 'contenido no auténtico / en serie' (YouTube 1311392, 2801973)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import rotacion
prev = [x for x in rotacion.log() if x.get("project_id") != sb.get("project_id")]
est = sb.get("estructura"); ok("estructura_valida", est in rotacion.ESTRUCTURAS, str(est))
ok("estructura_no_repite_anterior", not prev or est != prev[-1].get("estructura"), f"anterior: {prev[-1].get('estructura') if prev else '-'}")
cama = sb.get("audio", {}).get("cama_musical"); ok("cama_musical_no_repite_anterior", not prev or not cama or cama != prev[-1].get("cama"), f"{cama} (anterior: {prev[-1].get('cama') if prev else '-'})")
capas = [sc["capa"]["tipo"] for sc in sb["scenes"] if sc.get("capa")]
ok("capa_mapa", "mapa" in capas, ",".join(capas) or "sin capas"); ok("capa_grafico_o_dato", bool({"grafico", "dato"} & set(capas)), ",".join(capas) or "sin capas")
ok("licencias_json", os.path.exists(os.path.join(os.path.dirname(os.path.abspath(mp4)), "licencias.json")))
json.dump(R, open(os.path.join(os.path.dirname(os.path.abspath(mp4)), "qa.json"), "w"), ensure_ascii=False, indent=1)
for r in R: print(("PASA " if r["ok"] else "FALLA"), r["check"], r["detalle"])
sys.exit(0 if all(r["ok"] for r in R) else 1)
