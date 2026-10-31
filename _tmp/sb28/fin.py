import json,sys,os
d,hora=sys.argv[1],sys.argv[2]; D=f"/workspace/capcot/salidas/{d}"
p=json.load(open(D+"/publicacion.json"))["resultado"]["youtube"]; st=p["status"]; yid=p["id"]
print(yid, st["privacyStatus"], st.get("publishAt"))
sb=json.load(open(D+"/storyboard.json")); md=json.load(open(D+"/metadata.json"))
tt=json.load(open(D+"/tiktok.json")) if os.path.exists(D+"/tiktok.json") else {}
tags=tt.get("hashtags",md.get("tiktok_hashtags",[]))[:5]
tt.update({"estado":"pendiente_tiktok","mp4":D+"/capsula.mp4","yt_id":yid,"hora_sugerida_local":f"2026-10-28 {hora} CDMX","hashtags":tags,
 "caption_corto":sb["title"]+"\n\nFuentes en YouTube @datosyociosidades\n"+" ".join(tags[:3]),
 "etiqueta_ia":"Activar etiqueta 'Contenido generado por IA' (imágenes y voz sintéticas)","etiqueta_ia_activada":False,
 "instruccion":"Mj/agente con browser sube en TikTok Studio con caption_corto, etiqueta IA y programa a la hora del slot; luego estado='programado_tiktok'/'publicado_tiktok' + url.","url":None})
json.dump(tt,open(D+"/tiktok.json","w"),ensure_ascii=False,indent=1)
fb={"estado":"pendiente_fb","mp4":D+"/capsula.mp4","caption":md.get("description",p["snippet"]["description"]),"programar_cdmx":f"2026-10-28 {hora}","yt_id":yid,
 "nota":"Programar en Meta Business Suite (zona Suite = America/Indiana/Indianapolis, CDMX+2). Sin computerUse en este agente: pendiente.","fb_id":None}
json.dump(fb,open(D+"/facebook.json","w"),ensure_ascii=False,indent=1)
