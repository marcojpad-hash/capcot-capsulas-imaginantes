#!/usr/bin/env python3
"""Adaptador de imágenes: genera frames 1080x1920 para cada escena de un storyboard.
Proveedores (--proveedor):
  xai          API de imágenes de xAI (CAPCOT_IMAGE_API_KEY; modelo CAPCOT_IMAGE_MODEL, def. grok-2-image)
  openai       API compatible OpenAI images (CAPCOT_IMAGE_API_KEY, CAPCOT_IMAGE_BASE_URL)
  manual       no genera: lista prompts y espera los archivos (p.ej. hechos con la herramienta GenerateImage del bot)
  placeholder  frames de prueba con Pillow (NUNCA en producción)
Siempre normaliza a 1080x1920 (recorte centrado). Uso:
  python3 scripts/generar_frames.py proyectos/x/storyboard.json --proveedor manual"""
import argparse, base64, json, os, sys, urllib.request
from PIL import Image, ImageDraw, ImageFont

def normalizar(path):
    im = Image.open(path).convert("RGB"); W, H = 1080, 1920
    r = max(W / im.width, H / im.height); im = im.resize((round(im.width * r), round(im.height * r)), Image.LANCZOS)
    l, t = (im.width - W) // 2, (im.height - H) // 2; im.crop((l, t, l + W, t + H)).save(path)

def api(prompt, out, base, model):
    key = os.environ.get("CAPCOT_IMAGE_API_KEY")
    if not key: sys.exit("FALTA CAPCOT_IMAGE_API_KEY")
    body = json.dumps({"model": model, "prompt": prompt + ". Vertical 9:16, no text.", "n": 1, "response_format": "b64_json"}).encode()
    req = urllib.request.Request(base + "/images/generations", body, {"Authorization": "Bearer " + key, "Content-Type": "application/json"})
    open(out, "wb").write(base64.b64decode(json.load(urllib.request.urlopen(req, timeout=180))["data"][0]["b64_json"]))

def placeholder(sc, out, i):
    im = Image.new("RGB", (1080, 1920), (30 + i * 15, 40, 70 - i * 4)); d = ImageDraw.Draw(im)
    f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 44)
    d.text((80, 200), "PLACEHOLDER " + sc["id"], font=f, fill=(255, 220, 120))
    y = 320
    for k in range(0, len(sc.get("visual_description", "")), 34):
        d.text((80, y), sc["visual_description"][k:k + 34], font=f, fill=(255, 255, 255)); y += 60
    im.save(out)

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("storyboard"); ap.add_argument("--proveedor", default="manual")
    a = ap.parse_args(); sb = json.load(open(a.storyboard, encoding="utf-8")); base = os.path.dirname(os.path.abspath(a.storyboard))
    falt = 0
    for i, sc in enumerate(sb["scenes"]):
        out = os.path.join(base, sc["asset_filename"]); os.makedirs(os.path.dirname(out), exist_ok=True)
        if os.path.exists(out) and a.proveedor != "placeholder": normalizar(out); continue
        p = sc.get("image_prompt") or sc.get("generation_prompt", "")
        if a.proveedor == "placeholder": placeholder(sc, out, i)
        elif a.proveedor == "xai": api(p, out, "https://api.x.ai/v1", os.environ.get("CAPCOT_IMAGE_MODEL", "grok-2-image")); normalizar(out)
        elif a.proveedor == "openai": api(p, out, os.environ.get("CAPCOT_IMAGE_BASE_URL", "https://api.openai.com/v1"), os.environ.get("CAPCOT_IMAGE_MODEL", "gpt-image-1")); normalizar(out)
        else: print(f"PENDIENTE {sc['asset_filename']}: {p}"); falt += 1
    print("frames OK" if not falt else f"{falt} frames pendientes"); sys.exit(1 if falt else 0)
