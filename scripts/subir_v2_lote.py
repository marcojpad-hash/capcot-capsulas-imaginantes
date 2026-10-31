import json,os,sys,datetime
sys.path.insert(0,'scripts'); import publicar as P
H='data/horario_semana_2026-11-01_07.json'
h=json.load(open(H)); yt=P.yt_cliente(); out=[]
now=datetime.datetime.now().astimezone().isoformat(timespec='seconds')
for s in h['slots']:
    pid=s.get('project_id'); 
    if pid=='2026-11-01_pulpo-tres-corazones':
        if s['yt_id']!='pxX0eGK3r98':
            s.setdefault('yt_id_historial',[]).append(s['yt_id']); s['yt_id']='pxX0eGK3r98'
        continue
    if not s.get('yt_id') or s.get('yt_v2'): continue
    d='salidas/'+pid; old=s['yt_id']; pa=s['publishAt']
    meta,md=P.metadatos(d)
    r=P.youtube(os.path.join(d,'capsula_v2.mp4'),md,True,None,pa)
    new=r['id']; th='ok'
    try: P.thumbnail_gancho(new,d,yt=yt)
    except Exception as e: th='error: %s'%e
    pj=os.path.join(d,'publicacion.json'); pub=json.load(open(pj)) if os.path.exists(pj) else {}
    pub['metadatos']=md; R=pub.setdefault('resultado',{}); R['youtube']=r
    R.setdefault('historial_youtube',[]).append({'id':old,'estado':'SIGUE PROGRAMADO %s — borrar a mano en Studio (token sin scope youtube)'%pa,'reemplazado_por':new,'fecha':now})
    R['youtube_thumbnail']={'fuente':'scene_001 (gancho)','estado':th}
    pub['remontaje_cierre']={'fecha':now,'video':'capsula_v2.mp4','tiktok_facebook':'siguen con video viejo (pre-cierre)'}
    json.dump(pub,open(pj,'w'),ensure_ascii=False,indent=1)
    s.setdefault('yt_id_historial',[]).append(old); s['yt_id']=new; s['yt_v2']=True
    json.dump(h,open(H,'w'),ensure_ascii=False,indent=2)
    print('OK',pid,old,'->',new,r['status'].get('publishAt'),th,flush=True)
json.dump(h,open(H,'w'),ensure_ascii=False,indent=2)
