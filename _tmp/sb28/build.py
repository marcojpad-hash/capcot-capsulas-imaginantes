import json, os, sys
R="/workspace/capcot"; E=json.load(open(R+"/scripts/estilos.json"))
def build(spec):
    est=E[spec["estilo_id"]]; pid=spec["project_id"]; d=f"{R}/proyectos/{pid}"; os.makedirs(d+"/frames",exist_ok=True)
    scenes=[]
    for i,s in enumerate(spec["scenes"],1):
        w=len(s["n"].split()); sc={"id":f"scene_{i:03d}","arc":s["arc"],"duration_seconds":round(max(6.0,w/2.55+0.6),1),
          "narration":s["n"],"on_screen_text":s.get("t",""),"visual_description":f"Ilustración generada con IA, estilo {est['nombre']} (interpretación artística): {s['img']}",
          "image_prompt":est["prompt_base"]+" + "+s["img"]+", no text","source_ids":s.get("src",[]),"asset_filename":f"frames/scene_{i:03d}.jpg",
          "ambiente":"","sfx":[],"image_origen":{"tipo":"ia_generada","herramienta":"GenerateImage"}}
        if "capa" in s: sc["capa"]=s["capa"]
        scenes.append(sc)
    tot=sum(x["duration_seconds"] for x in scenes)+6
    sb={"project_id":pid,"serie":"Datos y ociosidades","title":spec["title"],"titulo":spec["titulo"],"titulo_yt":spec["title"]+" #Shorts",
      "language":"es-MX","aspect_ratio":"9:16","target_duration_seconds":int(min(90,max(75,round(tot)))),
      "estructura":spec["estructura"],"estilo_id":spec["estilo_id"],"estilo_visual":est["nombre"],"trend_source":spec["trend_source"],
      "voice":{"engine":"edge-tts","voice_id":"es-MX-JorgeNeural","rate":"+7%","pitch":"-2Hz","pad_seconds":0.3,"modo_pausas":"continuo"},
      "sources":spec["sources"],"scenes":scenes,
      "cortinilla_fuentes":{"duration_seconds":6,"titulo":"Fuentes","aviso":f"Ilustraciones generadas con IA (estilo {est['nombre']}); interpretación artística. Voz sintética con IA (edge-tts). Música sintetizada.","bg_rgb":[28,30,52],"firma":"Datos y ociosidades · @datosyociosidades"},
      "audio":{"music_asset":"sintetico:","music_lufs":-27,"ambiente_lufs":-28,"music_license":"Sintetizado por scripts/cama_sonora.py (obra propia)","sfx_license":"Wikimedia Commons CC0/PD, ver assets/sfx/LICENCIAS.json"},
      "export":{"filename":"capsula.mp4","resolution":"1080x1920","fps":30,"subtitle_max_words":3,"plano_seconds":2.5,"loudness_lufs":-14},
      "canal":{"nombre":"Datos y ociosidades","handle":"@datosyociosidades","youtube_channel_id":"UCU2ZI-6pBJEr9aSFsF6bxLw"},
      "origen":"propia","parece_real":False,"proveedor_imagenes":"GenerateImage (IA) con prompt_base del estilo","slot_cdmx":spec["slot"],"estado":"storyboard 2026-10-28"}
    json.dump(sb,open(d+"/storyboard.json","w"),ensure_ascii=False,indent=1)
    print(d, "dur",round(tot,1),"palabras",sum(len(s["n"].split()) for s in spec["scenes"]))
    for x in scenes: print(x["id"], "|", x["image_prompt"].split(" + ",1)[1])
