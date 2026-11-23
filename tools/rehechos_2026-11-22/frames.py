import json, os, sys, urllib.request, time
from PIL import Image, ImageFilter, ImageEnhance
from commons import search, UA
from specs import SPECS
W,H=1080,1920
def prep(src, dst):
    im=Image.open(src).convert('RGB')
    bg=im.copy(); r=max(W/bg.width,H/bg.height); bg=bg.resize((int(bg.width*r)+1,int(bg.height*r)+1))
    bg=bg.crop(((bg.width-W)//2,(bg.height-H)//2,(bg.width-W)//2+W,(bg.height-H)//2+H)).filter(ImageFilter.GaussianBlur(40))
    bg=ImageEnhance.Brightness(bg).enhance(0.55)
    # primer plano: ocupar ancho completo; si es vertical, alto hasta 1500
    r=min(W/im.width, 1500/im.height); fg=im.resize((int(im.width*r),int(im.height*r)), Image.LANCZOS)
    y=int(H*0.56-fg.height/2); bg.paste(fg,((W-fg.width)//2,max(y,0))); bg.save(dst,quality=92)
def run(key, picks=None):
    s=SPECS[key]; out=f'/workspace/capcot_main/proyectos/2026-11-25_rehecho-{s["slug"]}'; os.makedirs(out+'/frames',exist_ok=True); os.makedirs(out+'/raw',exist_ok=True)
    meta={}; mp=out+'/frames/creditos.json'
    if os.path.exists(mp): meta=json.load(open(mp))
    used=set(m['file'] for m in meta.values())
    for i,sc in enumerate(s['scenes']):
        k=f'scene_{i+1:03d}'
        if k in meta and not (picks and k in picks): continue
        q=sc[2]; idx=0
        if picks and k in picks: q,idx=picks[k]
        res=[r for r in search(q) if r['file'] not in used or (picks and k in picks)]
        if not res: print('NO RESULT',key,k,q); continue
        r=res[min(idx,len(res)-1)]
        raw=f'{out}/raw/{k}.jpg'
        for t in range(3):
            try:
                data=urllib.request.urlopen(urllib.request.Request(r['thumb'],headers=UA),timeout=60).read(); open(raw,'wb').write(data); break
            except Exception as e: print('retry',e); time.sleep(3)
        prep(raw, f'{out}/frames/{k}.jpg'); used.add(r['file']); meta[k]=r; print(key,k,r['file'],r['lic'])
    json.dump(meta,open(mp,'w'),ensure_ascii=False,indent=1)
    return out
if __name__=='__main__':
    for k in sys.argv[1:]: run(k)
