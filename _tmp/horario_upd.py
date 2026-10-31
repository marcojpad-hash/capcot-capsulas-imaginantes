import json,sys
pid,yt,pa=sys.argv[1:4];f='data/horario_semana_2026-11-01_07.json';d=json.load(open(f))
def walk(x):
    if isinstance(x,dict):
        if x.get('project_id')==pid:
            x.update(estado='programado_yt',yt_id=yt,publishAt=pa); x['plataformas']={'yt':'programado','tt':'pending_tiktok','fb':'pending_fb'}; print('upd',x.get('fecha'),x.get('hora'))
        for v in x.values(): walk(v)
    elif isinstance(x,list): [walk(v) for v in x]
walk(d);json.dump(d,open(f,'w'),ensure_ascii=False,indent=2);open(f,'a').write('\n')
