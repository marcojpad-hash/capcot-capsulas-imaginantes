#!/usr/bin/env python3
"""Genera frames PLACEHOLDER 1080x1920 (Pillow) para la demo. No son arte final."""
import json, os, random
from PIL import Image, ImageDraw, ImageFont
here = os.path.dirname(os.path.abspath(__file__))
sb = json.load(open(os.path.join(here, "storyboard.json"), encoding="utf-8"))
os.makedirs(os.path.join(here, "frames"), exist_ok=True)
F = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
for i, sc in enumerate(sb["scenes"]):
    random.seed(i)
    top, bot = (40 + i * 12, 30 + i * 6, 25), (150 - i * 8, 90, 50 + i * 10)
    img = Image.new("RGB", (1080, 1920)); d = ImageDraw.Draw(img)
    for y in range(1920):
        t = y / 1919; d.line([(0, y), (1080, y)], fill=tuple(int(a + (b - a) * t) for a, b in zip(top, bot)))
    for _ in range(40):  # "árboles" esquemáticos
        x = random.randint(0, 1080); y = random.randint(1000, 1800); a = random.uniform(-0.8, 0.8)
        d.line([(x, y), (x + 220 * a, y - 220)], fill=(30, 20, 15), width=10)
    d.ellipse([390, 380, 690, 680], outline=(200, 40, 30), width=8)
    f1, f2 = ImageFont.truetype(F, 60), ImageFont.truetype(F, 38)
    d.text((80, 160), "PLACEHOLDER", font=f1, fill=(255, 220, 120))
    d.text((80, 240), f"{sc['id']} · {sc['arc']}", font=f2, fill=(255, 255, 255))
    words, line, y = sc["visual_description"].split(), "", 760
    for w in words:
        if d.textlength(line + " " + w, font=f2) > 900: d.text((80, y), line, font=f2, fill=(255, 255, 255)); y += 50; line = w
        else: line = (line + " " + w).strip()
    d.text((80, y), line, font=f2, fill=(255, 255, 255))
    img.save(os.path.join(here, sc["asset_filename"]))
print("frames listos")
