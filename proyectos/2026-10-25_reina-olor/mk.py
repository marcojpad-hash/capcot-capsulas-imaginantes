import json
PB="linocut print, two-tone indigo and ochre ink on cream paper, bold carved lines, visible gouge marks, high contrast, vertical 9:16 composition, no text"
V=open('../../salidas/2026-10-25-reina-olor/narracion.vtt').read().split('\n\n')
cues=[]
for b in V:
    l=b.strip().split('\n')
    if len(l)>=3 and '-->' in l[1]: cues.append(' '.join(l[2:]))
G=[(0,0.0,7.447),(1,7.447,15.236),(3,15.236,24.026),(6,24.026,34.552),(8,34.552,43.039),(10,43.039,49.460),(11,49.460,56.631),(12,56.631,65.421),(13,65.421,70.750),(14,70.750,80.304)]
groups=[[0],[1,2],[3,4,5],[6,7],[8,9],[10],[11],[12],[13],[14,15]]
S=[("La reina que manda con su olor","A naked mole-rat queen, wrinkled hairless body, long front teeth, inside an underground burrow chamber, wavy scent lines radiating from her","Reina rata topo con ondas de olor","viento"),
("","Cross-section of an underground naked mole-rat colony: a network of tunnels and chambers like an anthill, many small hairless mole-rats","Corte de túneles tipo hormiguero","viento"),
("Una sola reina","A large naked mole-rat queen resting on a nest of roots, surrounded by smaller worker mole-rats bowing at a distance","Reina grande rodeada de obreras","viento"),
("Nature, 2026","A scientist's hands holding a glass vial with a single drop near a sleeping naked mole-rat in a tunnel, wavy chemical scent curls","Frasco y pista química","madera"),
("Miristato de isopropilo","Abstract molecule chain of carbon atoms drawn as carved beads, floating like a scent cloud above a naked mole-rat queen","Molécula como nube de olor","viento"),
("","Close-up of a naked mole-rat snout sniffing, with stylized olfactory neurons branching like roots toward the brain; another mole-rat turning away","Hocico, neuronas olfativas, rechazo","viento"),
("Prolactina y progesterona","Stylized hormone symbols as swirling carved patterns flowing through a silhouette of a female naked mole-rat, a closed flower symbol on her belly","Hormonas y freno reproductivo","viento"),
("Colonia sin reina","An empty queen throne-like nest chamber in a tunnel, a dropper adding scent every day, worker naked mole-rats waiting calmly","Nido vacío con olor diario","madera"),
("","Two naked mole-rats fighting with bared front teeth in a narrow tunnel, dust and motion lines","Peleas por el trono","madera"),
("","A naked mole-rat beside a honeybee and an ant, linked by curling scent lines, unified in a decorative carved border","Rata topo, abeja y hormiga unidas","viento")]
sc=[]
for i,((t,a,b),gi,(ost,vp,vd,amb)) in enumerate(zip([(None,g[1],g[2]) for g in G],groups,S),1):
    sc.append({"id":f"scene_{i:03}","start":a,"end":b,"duration":round(b-a,3),"narration":" ".join(cues[k] for k in gi),
      "on_screen_text":ost,"visual_description":vd,"image_prompt":PB+", "+vp,"asset_filename":f"frames/scene_{i:03}.jpg","ambiente":amb,"sfx":amb})
sb={"project_id":"2026-10-25_reina-olor","serie":"Datos y ociosidades","canal":{"nombre":"Datos y ociosidades","handle":"@datosyociosidades"},
"title":"La reina que manda con su olor","titulo":"Reina del olor","language":"es-MX","aspect_ratio":"9:16","estilo_id":"linograbado","estilo_visual":"Linograbado bitono",
"audio_existente":"salidas/2026-10-25-reina-olor/narracion.mp3","narration_duration":80.304,
"voice":{"engine":"edge-tts","voice_id":"es-MX-JorgeNeural","nota":"preexistente, no regenerar"},
"audio":{"music_asset":"sintetico:menor_calma","cama_musical":"pulso"},
"sources":[{"id":"SRC-001","cita_corta":"Khallaf et al. (2026). A queen odour mediates reproductive suppression in a eusocial mammal. Nature.","doi":"10.1038/s41586-026-10772-5","url":"https://doi.org/10.1038/s41586-026-10772-5","accessed":"2026-10-25","ref_display":"Nature · doi:10.1038/s41586-026-10772-5"}],
"cortinilla_fuentes":{"titulo":"Fuente","duracion":6,"aviso":"Imágenes generadas con IA. Voz sintética.","firma":"Datos y ociosidades · @datosyociosidades"},
"scenes":sc}
json.dump(sb,open('storyboard.json','w'),ensure_ascii=False,indent=1)
for s in sc: print(s['id'],s['duration'],'|',s['narration'][:60])
