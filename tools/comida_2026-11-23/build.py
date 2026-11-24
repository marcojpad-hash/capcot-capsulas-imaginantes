import json, os, sys, subprocess, urllib.request, time, copy, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from commons import by_title, UA
from specs import SPECS
from PIL import Image, ImageFilter, ImageEnhance
R='/workspace/capcot_main'; W,H=1080,1920
ARCH={'LCCN':'Library of Congress','BEIC':'Biblioteca Europea di Informazione e Cultura (BEIC)','BL Add MS':'British Library','Mendel':'Stadtbibliothek Nürnberg (Hausbücher der Nürnberger Zwölfbrüderstiftungen)',
      'Monte Cassino':'Archivio dell’Abbazia di Montecassino','Musée Carnavalet':'Musée Carnavalet (Paris Musées)','NJ9828':'Paris Musées','IA dr':'David Rumsey Map Collection vía Internet Archive (Braun y Hogenberg, Civitates Orbis Terrarum)','Dorothea Lange':'National Archives / War Relocation Authority (Dorothea Lange)'}
def prep(src,dst):
    im=Image.open(src).convert('RGB')
    bg=im.copy(); r=max(W/bg.width,H/bg.height); bg=bg.resize((int(bg.width*r)+1,int(bg.height*r)+1))
    bg=bg.crop(((bg.width-W)//2,(bg.height-H)//2,(bg.width-W)//2+W,(bg.height-H)//2+H)).filter(ImageFilter.GaussianBlur(40))
    bg=ImageEnhance.Brightness(bg).enhance(0.55)
    r=min(W/im.width,1500/im.height); fg=im.resize((int(im.width*r),int(im.height*r)),Image.LANCZOS)
    y=int(H*0.56-fg.height/2); bg.paste(fg,((W-fg.width)//2,max(y,0))); bg.save(dst,quality=92)
def frames(s,out):
    os.makedirs(out+'/frames',exist_ok=True); os.makedirs(out+'/raw',exist_ok=True)
    mp=out+'/creditos_imagenes.json'; meta=json.load(open(mp)) if os.path.exists(mp) else {}
    for i,sc in enumerate(s['scenes']):
        k=f'scene_{i+1:03d}'
        if k in meta and meta[k]['file']==sc['img'] and os.path.exists(f'{out}/frames/{k}.jpg'): continue
        r=by_title(sc['img']); raw=f'{out}/raw/{k}.jpg'
        for t in range(4):
            try: open(raw,'wb').write(urllib.request.urlopen(urllib.request.Request(r['thumb'],headers=UA),timeout=60).read()); break
            except Exception as e: print('retry',e); time.sleep(4)
        prep(raw,f'{out}/frames/{k}.jpg')
        r['archivo']='Wikimedia Commons'+''.join(f' · original: {v}' for kk,v in ARCH.items() if kk in r['file'] or kk in r['artist'])
        if 'en gaulle' in r['file']: r['artist']='Élisabeth Vigée Le Brun (1783; foto de Kaho Mitsuki)'
        meta[k]=r; print(k,r['file'],r['lic'])
    json.dump(meta,open(mp,'w'),ensure_ascii=False,indent=1); return meta
def credit(r): return f"{r['file'].replace('File:','').rsplit('.',1)[0]}. {r['artist'].replace('Unknown authorUnknown author','autor desconocido').replace('AnonymousUnknown author','anónimo')}, {r['lic']}. {r['archivo']}. {r['page']}"
def capa_lang(c,lang):
    if not c: return None
    c=copy.deepcopy(c)
    if lang=='en':
        for f in ('titulo','valor','etiqueta'):
            if f+'_en' in c: c[f]=c.pop(f+'_en')
        for p in c.get('puntos',[]):
            if 'nombre_en' in p: p['nombre']=p.pop('nombre_en')
    else:
        for f in list(c):
            if f.endswith('_en'): c.pop(f)
        for p in c.get('puntos',[]): p.pop('nombre_en',None)
    if c['tipo']=='mapa': c['plano']=1
    return c
def storyboard(s,out,cred,lang):
    pid=f'2026-11-23_comida-{s["slug"]}'; en=lang=='en'
    scenes=[]
    for i,sc in enumerate(s['scenes']):
        k=f'scene_{i+1:03d}'; d={'id':k,'arc':'hook_medias_res' if i==0 else ('reflexion_o_pregunta' if i==len(s['scenes'])-1 else 'desarrollo'),
          'duration_seconds':10,'narration':sc[lang],'on_screen_text':sc['ost_'+lang],'asset_filename':f'frames/{k}.jpg','sfx':sc['sfx'],
          'source_ids':[x['id'] for x in s['sources']],'image_credit':credit(cred[k]),'visual_description':cred[k]['file']}
        c=capa_lang(sc.get('capa'),lang)
        if c: d['capa']=c
        scenes.append(d)
    title=s['title_'+lang]
    return {'project_id':pid+('_en' if en else ''),'serie':'Comida: mito vs dato','numero_lista':s['n'],'title':title,'titulo':title,'language':'en-US' if en else 'es-MX',
        'aspect_ratio':'9:16','target_duration_seconds':88,'estilo_id':'foto_commons','estilo_visual':'obras y fotografías de dominio público o licencia libre (Wikimedia Commons)',
        'proveedor_imagenes':'Wikimedia Commons (dominio público o CC; archivo original citado en creditos_imagenes.json)','parece_real':True,'keywords':[s['slug']],
        'voice':({'engine':'edge-tts','voice_id':'en-US-AndrewNeural','rate':s.get('en_rate','+5%'),'pitch':'-2Hz','pausa_extra':s.get('en_extra',0),'pad_seconds':s.get('en_pad',0.6)} if en else {'engine':'edge-tts','voice_id':'es-MX-JorgeNeural','rate':'+7%','pitch':'-2Hz'})|({} if en else {'pad_seconds':s.get('pad',0.6)})|{'modo_pausas':'continuo'},
        'audio':{'music_asset':'sintetico:'+s['cama'],'cama_musical':s['cama'],'music_bpm':s['bpm'],'music_lufs':-27,'ambiente_lufs':-30},
        'canal':{'nombre':'Datos y ociosidades','handle':'@datosyociosidadesEN' if en else '@datosyociosidades'},'sources':s['sources'],'scenes':scenes,
        'cortinilla_fuentes':{'duration_seconds':(s.get('en_cort',5) if en else s.get('cortinilla_s',5)),'titulo':'Sources' if en else 'Fuentes',
            'aviso':('Images: public domain or free license (Wikimedia Commons). Synthetic AI voice (IA). Synthesized audio.' if en else 'Imágenes de dominio público o con licencia libre (Wikimedia Commons). Voz sintética (IA). Audio sintetizado.'),
            'firma':'Datos y ociosidades · '+('@datosyociosidadesEN' if en else '@datosyociosidades'),'bg_rgb':[18,16,14]},
        'export':{'filename':'capsula_en.mp4' if en else 'capsula.mp4','resolution':'1080x1920','fps':30,'loudness_lufs':-14,'plano_seconds':4.0,'subtitle_max_words':3},
        'estructura':'mito_vs_dato','hook_type':'mito_vs_dato'}
def render(out,lang):
    sbf=out+('/storyboard_en.json' if lang=='en' else '/storyboard.json'); mp4=out+('/capsula_en.mp4' if lang=='en' else '/capsula.mp4')
    lic=out+'/licencias.json'; keep=open(lic).read() if (lang=='en' and os.path.exists(lic)) else None
    px=str(json.load(open(sbf))['voice'].get('pausa_extra',0))
    r=subprocess.run(['python3',os.path.dirname(os.path.abspath(__file__))+'/montar_reintentos.py',sbf,'-o',mp4],capture_output=True,text=True,env=os.environ|{'PAUSA_EXTRA':px})
    open(out+f'/render_{lang}.log','w').write(r.stdout+r.stderr[-3000:])
    if lang=='en':
        shutil.move(lic,out+'/licencias_en.json')
        if keep: open(lic,'w').write(keep)
    q=subprocess.run(['python3',R+'/scripts/qa_capsula.py',mp4,sbf],capture_output=True,text=True,cwd=R)
    shutil.move(out+'/qa.json',out+f'/qa_{lang}.json') if os.path.exists(out+'/qa.json') else None
    if lang=='es': subprocess.run(['ffmpeg','-y','-v','error','-i',mp4,'-frames:v','1','-q:v','2',out+'/portada.jpg'])
    else: subprocess.run(['ffmpeg','-y','-v','error','-i',mp4,'-frames:v','1','-q:v','2',out+'/portada_en.jpg'])
    return r.returncode, r.stdout.strip().splitlines()[-1:] , q.stdout
def yt_tt_hashtags(raw):
    temas=[h for h in (raw or []) if h.lower() not in ('#shorts','#short','#sabiasque')]
    yt=temas[:5]+(['#sabiasque'] if '#sabiasque' not in [x.lower() for x in temas] else [])+['#Shorts']
    tt=temas[:5]
    if len(tt)<4:
        for f in ('#comida','#historia','#sabiasque','#curiosidades'):
            if f.lower() not in {x.lower() for x in tt} and len(tt)<4: tt.append(f)
    return yt, tt[:5]
def metadata(s,out,cred):
    imgs=[]; [imgs.append(credit(cred[k])) for k in sorted(cred) if credit(cred[k]) not in imgs]
    srcs="\n".join(f"• {x['cita_corta']} {x['url']}" for x in s['sources'])
    hook_es=s['scenes'][0]['es'].split('. ')[0].rstrip('.')+'.'; hook_en=s['scenes'][0]['en'].split('. ')[0].rstrip('.')+'.'
    yt_es, tt_es = yt_tt_hashtags(s['ht_es']); yt_en, tt_en = yt_tt_hashtags(s['ht_en'])
    d_es=(f"{hook_es}\n\n{s['title_es']}\n\nFuentes:\n{srcs}\n\nImágenes (Wikimedia Commons; dominio público o licencia libre; archivo original indicado):\n"
          +"\n".join(f"• {c}" for c in imgs)+"\n\nVoz sintética generada con IA · música y ambiente sintetizados.\nSuscríbete: @datosyociosidades\nTikTok: https://www.tiktok.com/@datosyociosidades\n\n"+" ".join(yt_es))
    d_en=(f"{hook_en}\n\n{s['title_en']}\n\nSources:\n{srcs}\n\nImages (Wikimedia Commons; public domain or free license; original archive noted):\n"
          +"\n".join(f"• {c}" for c in imgs)+"\n\nSynthetic AI-generated voice · synthesized music and ambience.\nSubscribe: @datosyociosidadesEN\nSpanish channel: @datosyociosidades\nTikTok: https://www.tiktok.com/@datosyociosidades\n\n"+" ".join(yt_en))
    m={'numero_lista':s['n'],'titulo_es':s['title_es'],'youtube_title_es':(s['title_es']+' #Shorts')[:100] if len(s['title_es'])+8<=100 else s['title_es'],'descripcion_es':d_es,
       'caption_tiktok_es':f"{s['title_es']} "+" ".join(tt_es),'hashtags_es':yt_es,
       'titulo_en':s['title_en'],'youtube_title_en':(s['title_en']+' #Shorts')[:100] if len(s['title_en'])+8<=100 else s['title_en'],'descripcion_en':d_en,
       'caption_tiktok_en':f"{s['title_en']} "+" ".join(tt_en),'hashtags_en':yt_en,
       'tags_es':[h[1:] for h in yt_es],'tags_en':[h[1:] for h in yt_en],
       'contenido_sintetico':True,'aviso_ia':'Voz sintética (IA). Marcar «contenido alterado o sintético» al subir.',
       'palabras_es':sum(len(x['es'].split()) for x in s['scenes']),'palabras_en':sum(len(x['en'].split()) for x in s['scenes']),
       'nota_guion':'Narración ES = guion verificado de Mj, tal cual (pendientes/abiertos/2026-11-22_guiones-semana-30nov-6dic.md). EN = traducción fiel.'}
    json.dump(m,open(out+'/metadata.json','w'),ensure_ascii=False,indent=1)
def guion(s,out,cred):
    for lang in ('es','en'):
        g=f"# Nº {s['n']} · {s['title_'+lang]}\n\n"+"\n\n".join(f"**{sc['ost_'+lang] or s['title_'+lang]}**\n{sc[lang]}" for sc in s['scenes'])
        g+="\n\n## Fuentes\n"+"\n".join(f"- {x['cita_corta']} {x['url']}" for x in s['sources'])+"\n\n## Imágenes\n"+"\n".join(f"- {k}: {credit(cred[k])}" for k in sorted(cred))+"\n"
        open(out+('/guion_en.md' if lang=='en' else '/guion.md'),'w').write(g)
def run(key,langs=('es','en')):
    s=SPECS[key]; out=f'{R}/proyectos/2026-11-23_comida-{s["slug"]}'; os.makedirs(out,exist_ok=True)
    cred=frames(s,out); guion(s,out,cred); metadata(s,out,cred)
    res={}
    for lang in langs:
        json.dump(storyboard(s,out,cred,lang),open(out+('/storyboard_en.json' if lang=='en' else '/storyboard.json'),'w'),ensure_ascii=False,indent=1)
        res[lang]=render(out,lang); print(key,lang,res[lang][0],res[lang][1]); print(res[lang][2])
    return res
if __name__=='__main__':
    langs=('es','en') if '--en' in sys.argv else ('es',)
    for k in [a for a in sys.argv[1:] if not a.startswith('--')]: run(k,langs)
