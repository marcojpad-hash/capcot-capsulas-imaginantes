"""Resube capsula_<ver>.mp4 al mismo slot; portada = primer frame del mp4. Uso: subir_vN.py ver pid [pid...]"""
import json,os,sys,datetime,subprocess
sys.path.insert(0,'scripts'); import publicar as P
from googleapiclient.http import MediaFileUpload
ver=sys.argv[1]; pids=sys.argv[2:]
H='data/horario_semana_2026-11-01_07.json'; h=json.load(open(H)); yt=P.yt_cliente()
now=datetime.datetime.now().astimezone().isoformat(timespec='seconds')
for s in h['slots']:
    pid=s.get('project_id')
    if pid not in pids or s.get('yt_'+ver): continue
    d='salidas/'+pid; mp4=os.path.join(d,'capsula.mp4' if ver=='v1' else 'capsula_%s.mp4'%ver); old=s.get('yt_id'); pa=s['publishAt']
    if not os.path.exists(mp4): print('SIN MP4',pid); continue
    meta,md=P.metadatos(d)
    try: r=P.youtube(mp4,md,True,None,pa)
    except Exception as e: print('ERROR_UPLOAD',pid,e,flush=True); break
    new=r['id']; th='ok'; jpg=os.path.join(d,'thumbnail_frame0.jpg')
    try:
        subprocess.run(['ffmpeg','-y','-loglevel','error','-i',mp4,'-frames:v','1','-q:v','3',jpg],check=True)
        yt.thumbnails().set(videoId=new,media_body=MediaFileUpload(jpg,mimetype='image/jpeg')).execute()
    except Exception as e: th='error: %s'%e
    pj=os.path.join(d,'publicacion.json'); pub=json.load(open(pj)) if os.path.exists(pj) else {}
    R=pub.setdefault('resultado',{}); R['youtube']=r
    if old: R.setdefault('historial_youtube',[]).append({'id':old,'estado':'SIGUE PROGRAMADO %s — borrar a mano en Studio'%pa,'reemplazado_por':new,'fecha':now})
    R['youtube_thumbnail']={'fuente':'primer frame mp4','estado':th}
    json.dump(pub,open(pj,'w'),ensure_ascii=False,indent=1)
    if old: s.setdefault('yt_id_historial',[]).append(old)
    s['yt_id']=new; s['yt_'+ver]=True; s['mp4']=mp4
    json.dump(h,open(H,'w'),ensure_ascii=False,indent=2)
    print('OK',pid,old,'->',new,pa,th,flush=True)
