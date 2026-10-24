#!/usr/bin/env python3
"""Descarga los SFX de scripts/sfx_manifest.json a assets/sfx/ y RE-VERIFICA la licencia en la API de Commons
(aborta si no es CC0/dominio público). Escribe la URL real en assets/sfx/LICENCIAS.json."""
import json, os, sys, urllib.parse, urllib.request
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); M = json.load(open(os.path.join(R, "scripts", "sfx_manifest.json")))
D = os.path.join(R, "assets", "sfx"); os.makedirs(D, exist_ok=True); UA = {"User-Agent": "capcot/1.0 (datosyociosidades)"}
out = {}
for k, v in M.items():
    if k.startswith("_"): continue
    q = urllib.parse.urlencode({"action": "query", "format": "json", "titles": v["commons"], "prop": "imageinfo",
                                "iiprop": "url|extmetadata", "iiextmetadatafilter": "LicenseShortName|Artist"})
    p = next(iter(json.load(urllib.request.urlopen(urllib.request.Request("https://commons.wikimedia.org/w/api.php?" + q, headers=UA)))["query"]["pages"].values()))
    ii = p["imageinfo"][0]; lic = ii["extmetadata"]["LicenseShortName"]["value"]
    if not ("CC0" in lic or "public domain" in lic.lower()): sys.exit(f"{k}: licencia no permitida {lic}")
    dst = os.path.join(D, v["archivo"])
    if not os.path.exists(dst): open(dst, "wb").write(urllib.request.urlopen(urllib.request.Request(ii["url"], headers=UA)).read())
    out[k] = {**v, "url": ii["url"], "pagina": ii["descriptionurl"], "licencia_verificada": lic}
json.dump(out, open(os.path.join(D, "LICENCIAS.json"), "w"), ensure_ascii=False, indent=1); print("OK", len(out))
