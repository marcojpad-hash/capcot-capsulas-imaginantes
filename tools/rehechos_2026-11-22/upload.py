import json, sys, time, os
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
TOK='/home/box/.capcot/token.json'
c=Credentials.from_authorized_user_file(TOK)
if not c.valid: c.refresh(Request())
y=build('youtube','v3',credentials=c)
R='/workspace/capcot_main/proyectos/'
PLAN=[('nube','2026-11-25T16:00:00Z'),('barreleye','2026-11-25T21:00:00Z'),('pan','2026-11-26T16:00:00Z'),('ratas','2026-11-26T21:00:00Z'),
      ('miel','2026-11-27T16:00:00Z'),('mar','2026-11-27T21:00:00Z'),('arena','2026-11-28T16:00:00Z'),('juno','2026-11-28T21:00:00Z'),('viento','2026-11-29T16:00:00Z')]
from specs import SPECS
log=json.load(open('uploads.json')) if os.path.exists('uploads.json') else {}
for key,at in PLAN:
    if key in log and log[key].get('id'): continue
    d=R+'2026-11-25_rehecho-'+SPECS[key]['slug']; m=json.load(open(d+'/metadata.json'))
    body={'snippet':{'title':m['youtube_title'],'description':m['descripcion'],'tags':m['tags'],'categoryId':'27','defaultLanguage':'es','defaultAudioLanguage':'es'},
          'status':{'privacyStatus':'private','publishAt':at,'selfDeclaredMadeForKids':False,'containsSyntheticMedia':True}}
    try:
        r=y.videos().insert(part='snippet,status',body=body,media_body=MediaFileUpload(d+'/capsula.mp4',mimetype='video/mp4',resumable=True,chunksize=-1)).execute()
        vid=r['id']; log[key]={'id':vid,'publishAt':at,'dir':d}
        print(key,vid,at,flush=True)
        json.dump(log,open('uploads.json','w'),indent=1)
    except Exception as e:
        print('FAIL',key,e,flush=True); log[key]={'error':str(e)[:500]}; json.dump(log,open('uploads.json','w'),indent=1); continue
