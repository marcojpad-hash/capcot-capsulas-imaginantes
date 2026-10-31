import json,os,subprocess
H='data/horario_2026-10-31.json'; h=json.load(open(H))
pub=json.load(open('data/publicaciones.json')); rot=json.load(open('data/rotacion.json'))
pids={p.get('yt_id') for p in pub}; rids={r.get('project_id')+r.get('fecha','') for r in rot}
ven={'07:00':'manana','13:30':'comida','17:00':'tarde','19:00':'noche','23:30':'noche_tarde'}
for s in h['slots']:
  d=f"salidas/{s['id']}"; pj=os.path.join(d,'publicacion.json')
  if not os.path.exists(pj): continue
  r=json.load(open(pj)); y=r['resultado']['youtube']; yid=y['id']; st=y.get('status',{})
  pa=st.get('publishAt'); m=json.load(open(os.path.join(d,'metadata.json'))); sb=json.load(open(os.path.join(d,'storyboard.json')))
  dur=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',d+'/capsula.mp4']).decode())
  s.update(yt_id=yid,url=f"https://youtube.com/shorts/{yid}",publishAt=pa,estado='programado_yt' if pa else 'publicado_yt',
           mp4=d+'/capsula.mp4',duracion_s=round(dur,1),tiktok='pendiente_browser',facebook='pendiente_browser',hashtags_yt=m['hashtags'])
  if s['id'].startswith('2026-10-31_pardelas'): s['nota']="override rotacion historia; único dato-día 31"
  if yid not in pids:
    pub.append({"fecha":"2026-10-31","project_id":s['id'],"yt_id":yid,"url":s['url'],"privacidad":"private→public (publishAt)" if pa else "public",
      "publishAt_utc":pa,"hora_local":f"2026-10-31 {s['hora']} CDMX","ventana":s.get('cesta'),"titulo":m['titulo'],"origen":"propia","tiktok":"pendiente_browser","facebook":"pendiente_browser"})
  if s['id']+'2026-10-31' not in rids:
    au=sb.get('audio',{}) or {}
    rot.append({"fecha":"2026-10-31","project_id":s['id'],"estructura":sb.get('estructura') or s.get('estructura'),"cama":au.get('cama_musical') or str(au.get('music_asset','')).split(':')[-1],
      "duracion":round(dur),"tema":sb.get('tema') or sb.get('title'),"estilo":s.get('estilo') or sb.get('style_id'),"origen":"propia"})
for f,o in [(H,h),('data/publicaciones.json',pub),('data/rotacion.json',rot)]: json.dump(o,open(f,'w'),ensure_ascii=False,indent=2)
for s in h['slots']: print(s['hora'],s['id'],s.get('estado'),s.get('yt_id'),s.get('publishAt'),s.get('duracion_s'))
