#!/usr/bin/env python3
"""Actualiza la descripción del canal («Información / Acerca de») desde docs/ACERCA_DE_CANAL.md.
YouTube Data API channels.update part=brandingSettings (cuota 50). Por defecto DRY-RUN.
SCOPE requerido (developers.google.com/youtube/v3/docs/channels/update): uno de
  https://www.googleapis.com/auth/youtube | https://www.googleapis.com/auth/youtube.force-ssl | .../youtubepartner
El token actual (~/.capcot/token.json) solo tiene youtube.upload + youtube.readonly -> channels.update daría 403 insufficientPermissions.
Re-autorización (la hace Mj; este script NO la intenta): InstalledAppFlow con client_secret.json y scopes
  [youtube.upload, youtube.readonly, youtube.force-ssl], cuenta dueña de @datosyociosidades, guardar en ~/.capcot/token.json.
Uso: python3 scripts/actualizar_acerca_de.py [--ejecutar]
Nota: channels.update SOBRESCRIBE todo brandingSettings -> se lee el actual (readonly basta) y solo se cambia description."""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import publicar
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ESCRITURA = {"https://www.googleapis.com/auth/youtube", "https://www.googleapis.com/auth/youtube.force-ssl", "https://www.googleapis.com/auth/youtubepartner"}
MAX = 1000  # límite de brandingSettings.channel.description
def texto():
    md = open(os.path.join(R, "docs", "ACERCA_DE_CANAL.md"), encoding="utf-8").read()
    m = re.search(r"<!-- CANAL -->(.*?)<!-- /CANAL -->", md, re.S)
    t = m.group(1) if m else md.split("\n---\n", 1)[-1]
    t = re.sub(r"\*\*(.+?)\*\*", r"\1", t); t = re.sub(r"^- ", "• ", t, flags=re.M); t = re.sub(r"\n{3,}", "\n\n", t).strip()
    return t.replace("<", "‹").replace(">", "›")
def scopes_token():
    try: return set(json.load(open(publicar.YT_TOKEN)).get("scopes", []))  # solo se leen los nombres de scope, nunca secretos
    except Exception: return set()
if __name__ == "__main__":
    ej = "--ejecutar" in sys.argv; t = texto()
    print(f"descripción ({len(t)}/{MAX} chars):\n{t}\n")
    if len(t) > MAX: sys.exit(f"ERROR: {len(t)} > {MAX} caracteres; acorta el bloque <!-- CANAL --> de docs/ACERCA_DE_CANAL.md")
    sc = scopes_token(); falta = not (sc & ESCRITURA)
    print("scopes del token:", sorted(s.rsplit("/", 1)[-1] for s in sc), "| FALTA scope de escritura youtube / youtube.force-ssl" if falta else "| OK")
    yt = publicar.yt_cliente()
    ch = yt.channels().list(part="brandingSettings", id=publicar.CANAL_ID).execute()["items"][0]
    bs = ch["brandingSettings"]; antes = bs.get("channel", {}).get("description", "")
    bs.setdefault("channel", {})["description"] = t
    print("descripción actual:", repr(antes[:200])); print("channels.update body:", json.dumps({"id": publicar.CANAL_ID, "brandingSettings": bs}, ensure_ascii=False)[:800])
    if not ej: print("DRY-RUN: nada cambiado"); sys.exit(0)
    if falta: sys.exit("NO SE EJECUTA: el token no tiene youtube ni youtube.force-ssl (re-autoriza primero; ver docstring)")
    from google.oauth2.credentials import Credentials; from googleapiclient.discovery import build
    yt = build("youtube", "v3", credentials=Credentials.from_authorized_user_file(publicar.YT_TOKEN, sorted(sc)), cache_discovery=False)
    r = yt.channels().update(part="brandingSettings", body={"id": publicar.CANAL_ID, "brandingSettings": bs}).execute()
    print("OK descripción del canal actualizada:", r["id"])
