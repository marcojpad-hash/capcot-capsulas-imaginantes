#!/usr/bin/env python3
"""Publicación YouTube Shorts / TikTok (borrador). POR DEFECTO --dry-run: solo arma y muestra la petición.
Publicar de verdad exige --ejecutar Y credenciales de Mj:
  YouTube: ~/.capcot/client_secret.json + ~/.capcot/token.json (refresh token; scopes youtube.upload+readonly)
           (override: CAPCOT_YT_CLIENT_SECRETS / CAPCOT_YT_TOKEN). NUNCA commitear ni imprimir esos archivos.
  Verificación solo lectura: python3 scripts/publicar.py --verificar-yt
  TikTok : CAPCOT_TIKTOK_ACCESS_TOKEN (scope video.upload -> buzón de borradores; Mj publica desde la app)
Uso: python3 scripts/publicar.py salidas/<dir>/  [--plataforma yt] [--ejecutar]
TikTok DESACTIVADO por defecto (no hay cuenta nueva; la descripción de YT enlaza al TikTok de Mj).
Solo se usa tt/ambas si además se pasa --habilitar-tiktok."""
import argparse, json, os, sys

CANAL_ID = "UCU2ZI-6pBJEr9aSFsF6bxLw"  # Datos y ociosidades (@datosyociosidades)

def metadatos(d, sbn="storyboard.json"):
    """Usa metadata.json de la cápsula (lo genera scripts/metadata.py si falta)."""
    mp = os.path.join(d, "metadata.json")
    if not os.path.exists(mp):
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import metadata; metadata.generar(d, sbn)
    m = json.load(open(mp, encoding="utf-8"))
    return m, {"title": m["titulo"], "description": m["descripcion"], "tags": m["tags"]}

YT_TOKEN = os.environ.get("CAPCOT_YT_TOKEN", os.path.expanduser("~/.capcot/token.json"))
YT_SCOPES = ["https://www.googleapis.com/auth/youtube.upload", "https://www.googleapis.com/auth/youtube.readonly"]

def yt_cliente():
    from google.oauth2.credentials import Credentials; from google.auth.transport.requests import Request
    from googleapiclient.discovery import build
    if not os.path.exists(YT_TOKEN): sys.exit(f"FALTA token OAuth en {YT_TOKEN}")
    cr = Credentials.from_authorized_user_file(YT_TOKEN, YT_SCOPES)
    if not cr.valid and cr.refresh_token:
        cr.refresh(Request())
        fd = os.open(YT_TOKEN, os.O_WRONLY | os.O_TRUNC | os.O_CREAT, 0o600); os.write(fd, cr.to_json().encode()); os.close(fd)
    return build("youtube", "v3", credentials=cr, cache_discovery=False)

def verificar_yt():
    r = yt_cliente().channels().list(part="id,snippet", mine=True).execute()
    ids = [(c["id"], c["snippet"]["title"]) for c in r.get("items", [])]
    print("canales del token:", ids, "| OK" if any(i == CANAL_ID for i, _ in ids) else f"| NO coincide con {CANAL_ID}")

def youtube(mp4, md, ejecutar):
    priv = META.get("privacyStatus", "private")
    body = {"snippet": {**md, "categoryId": "27", "defaultLanguage": "es"},
            "status": {"privacyStatus": priv, "selfDeclaredMadeForKids": False, "containsSyntheticMedia": True}}
    print(f"[YT] canal destino {CANAL_ID} (verificar que el token sea de ese canal)")
    print("[YT] videos.insert part=snippet,status", json.dumps(body, ensure_ascii=False)[:600])
    if not ejecutar: return {"dry_run": True}
    from googleapiclient.http import MediaFileUpload
    yt = yt_cliente()
    mine = [c["id"] for c in yt.channels().list(part="id", mine=True).execute().get("items", [])]
    if CANAL_ID not in mine: sys.exit(f"token no es del canal {CANAL_ID}: {mine}")
    return yt.videos().insert(part="snippet,status", body=body, media_body=MediaFileUpload(mp4, resumable=True)).execute()

def tiktok(mp4, md, ejecutar):
    md = {**md, "caption": META.get("tiktok_caption", "")}
    size = os.path.getsize(mp4)
    body = {"source_info": {"source": "FILE_UPLOAD", "video_size": size, "chunk_size": size, "total_chunk_count": 1}}
    body["post_info"] = {"title": md.get("caption", "")}
    print("[TT] POST /v2/post/publish/inbox/video/init/ (borrador)", json.dumps(body))
    if not ejecutar: return {"dry_run": True}
    tok = os.environ.get("CAPCOT_TIKTOK_ACCESS_TOKEN")
    if not tok: sys.exit("FALTA CAPCOT_TIKTOK_ACCESS_TOKEN")
    import urllib.request
    r = json.load(urllib.request.urlopen(urllib.request.Request("https://open.tiktokapis.com/v2/post/publish/inbox/video/init/",
        json.dumps(body).encode(), {"Authorization": "Bearer " + tok, "Content-Type": "application/json; charset=UTF-8"})))
    url = r["data"]["upload_url"]
    urllib.request.urlopen(urllib.request.Request(url, open(mp4, "rb").read(), {"Content-Type": "video/mp4",
        "Content-Range": f"bytes 0-{size-1}/{size}"}, method="PUT"))
    return r

if __name__ == "__main__":
    if "--verificar-yt" in sys.argv: verificar_yt(); sys.exit()
    ap = argparse.ArgumentParser(); ap.add_argument("dir"); ap.add_argument("--plataforma", default="yt"); ap.add_argument("--habilitar-tiktok", action="store_true"); ap.add_argument("--video", default="capsula.mp4"); ap.add_argument("--storyboard", default="storyboard.json")
    ap.add_argument("--ejecutar", action="store_true", help="publica de verdad (requiere aprobación de Mj)")
    a = ap.parse_args(); META, md = metadatos(a.dir, a.storyboard); mp4 = os.path.join(a.dir, a.video); res = {}
    if a.plataforma in ("yt", "ambas"): res["youtube"] = youtube(mp4, md, a.ejecutar)
    if a.plataforma in ("tt", "ambas") and not a.habilitar_tiktok: res["tiktok"] = "desactivado (usa --habilitar-tiktok)"
    elif a.plataforma in ("tt", "ambas"): res["tiktok"] = tiktok(mp4, md, a.ejecutar)
    json.dump({"metadatos": md, "resultado": res}, open(os.path.join(a.dir, "publicacion.json"), "w"), ensure_ascii=False, indent=1)
    print("dry-run: nada publicado" if not a.ejecutar else "publicado")
