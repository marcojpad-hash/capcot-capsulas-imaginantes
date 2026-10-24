#!/usr/bin/env python3
"""Compila varias cápsulas (9:16) en un video LARGO horizontal 1920x1080 (las horas de videos largos son las que cuentan para
la ruta de 4,000 h del YPP; las de Shorts no). Cada cápsula va centrada sobre un fondo desenfocado de sí misma, con
tarjeta de capítulo (2.5 s). Genera capitulos.txt (marcas de tiempo para la descripción de YouTube). NO sube nada.
Uso: python3 scripts/compilar_largo.py -o salidas/largo01/largo.mp4 --titulo "El clima en historias" salidas/A/capsula.mp4 salidas/B/capsula.mp4 ..."""
import argparse, json, os, subprocess, tempfile
def dur(f): return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]).decode())
def titulo_de(mp4):
    d = os.path.dirname(mp4)
    for n in ("storyboard_v3.json", "storyboard.json"):
        p = os.path.join(d, n)
        if os.path.exists(p): return json.load(open(p, encoding="utf-8"))["title"]
    return os.path.basename(d)
def esc(t): return t.replace("\\", "\\\\").replace(":", "\\:").replace("'", "\u2019")
if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("videos", nargs="+"); ap.add_argument("-o", "--out", required=True); ap.add_argument("--titulo", default="Datos y ociosidades")
    a = ap.parse_args(); os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True); tmp = tempfile.mkdtemp(); partes, caps, t = [], [], 0.0
    font = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    for i, v in enumerate(a.videos, 1):
        tt = titulo_de(v); card = os.path.join(tmp, f"c{i}.mp4"); seg = os.path.join(tmp, f"s{i}.mp4")
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i", "color=c=0x1d1b2e:s=1920x1080:r=30:d=2.5", "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo", "-t", "2.5",
            "-vf", f"drawtext=fontfile={font}:text='{i}. {esc(tt)}':fontcolor=white:fontsize=64:x=(w-tw)/2:y=(h-th)/2", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", "-shortest", card], check=True)
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", v, "-filter_complex",
            "[0:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,boxblur=30:5,eq=brightness=-0.15[bg];[0:v]scale=-2:1080[fg];[bg][fg]overlay=(W-w)/2:0,fps=30,format=yuv420p",
            "-c:v", "libx264", "-crf", "20", "-c:a", "aac", "-ar", "48000", "-ac", "2", seg], check=True)
        m, s = divmod(int(t), 60); caps.append(f"{m:02d}:{s:02d} {tt}"); t += 2.5 + dur(seg); partes += [card, seg]
    lst = os.path.join(tmp, "l.txt"); open(lst, "w").write("".join(f"file '{p}'\n" for p in partes))
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c:v", "libx264", "-crf", "20", "-c:a", "aac", "-af", "loudnorm=I=-14:TP=-1.5", a.out], check=True)
    cp = os.path.join(os.path.dirname(os.path.abspath(a.out)), "capitulos.txt"); open(cp, "w").write(a.titulo + "\n\n" + "\n".join(caps) + "\n")
    print("OK", a.out, f"{t:.1f}s"); print(open(cp).read())
