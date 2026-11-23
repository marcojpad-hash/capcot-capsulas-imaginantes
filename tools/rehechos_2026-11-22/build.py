import json, os, sys, subprocess, importlib
import specs; importlib.reload(specs)
from specs import SPECS
R='/workspace/capcot_main'
def credit(r):
    return f"{r['file'].replace('File:','').rsplit('.',1)[0]}. {r['artist']}, {r['lic']}. {r['page']}"
def build(key):
    s=SPECS[key]; pid=f'2026-11-25_rehecho-{s["slug"]}'; out=f'{R}/proyectos/{pid}'
    cred=json.load(open(out+'/frames/creditos.json'))
    scenes=[]
    for i,(nar,ost,q,sfx) in enumerate(s['scenes']):
        k=f'scene_{i+1:03d}'
        scenes.append({'id':k,'arc':'hook_medias_res' if i==0 else ('cierre' if i==len(s['scenes'])-1 else 'desarrollo'),'duration_seconds':10,
          'narration':nar,'on_screen_text':ost,'asset_filename':f'frames/{k}.jpg','sfx':sfx,'source_ids':[x['id'] for x in s['sources']],
          'image_credit':credit(cred[k]),'visual_description':cred[k]['file']})
    sb={'project_id':pid,'serie':'Rehechos con gancho nuevo','rehecho_de':s['orig'],'title':s['title'],'titulo':s['title'],'language':'es-MX','aspect_ratio':'9:16','target_duration_seconds':88,
        'estilo_id':'foto_commons','estilo_visual':'fotografías e ilustraciones de dominio público o licencia libre (Wikimedia Commons)',
        'proveedor_imagenes':'Wikimedia Commons (dominio público o CC, créditos en metadata)','parece_real':True,'keywords':[s['tema']],
        'voice':{'engine':'edge-tts','voice_id':'es-MX-JorgeNeural','rate':'+7%','pitch':'-2Hz','pad_seconds':0.35,'modo_pausas':'continuo'},
        'audio':{'music_asset':'sintetico:pulso','cama_musical':'pulso','music_bpm':92,'music_lufs':-27,'ambiente_lufs':-30},
        'canal':{'nombre':'Datos y ociosidades','handle':'@datosyociosidades'},'sources':s['sources'],'scenes':scenes,
        'cortinilla_fuentes':{'duration_seconds':6,'titulo':'Fuentes','aviso':'Imágenes de dominio público o con licencia libre (Wikimedia Commons). Voz sintética (IA). Audio sintetizado.','firma':'Datos y ociosidades · @datosyociosidades','bg_rgb':[18,16,14]},
        'export':{'filename':'capsula.mp4','resolution':'1080x1920','fps':30,'loudness_lufs':-14,'plano_seconds':4.0,'subtitle_max_words':3},
        'estructura':'arco_narrativo','hook_type':'mito_vs_dato'}
    json.dump(sb,open(out+'/storyboard.json','w'),ensure_ascii=False,indent=1)
    g=f"# {s['title']}\n\nRehecho de https://youtube.com/shorts/{s['orig']} (original intacto).\n\n"+"\n\n".join(f"**{x['on_screen_text']}**\n{x['narration']}" for x in scenes)
    g+="\n\n## Fuentes\n"+"\n".join(f"- {x['cita_corta']} {x['url']}" for x in s['sources'])+(f"\n\nNota: {s['nota']}" if s.get('nota') else '')
    g+="\n\n## Imágenes\n"+"\n".join(f"- {x['id']}: {x['image_credit']}" for x in scenes)+"\n"
    open(out+'/guion.md','w').write(g)
    words=sum(len(x['narration'].split()) for x in scenes)
    hook=scenes[0]['narration'].split('. ')[0].rstrip('.')+'.'
    imgs=[]; [imgs.append(x['image_credit']) for x in scenes if x['image_credit'] not in imgs]
    desc=(f"{hook}\n\n{s['title']}. Una cápsula de Datos y ociosidades: datos verificados contados como historia.\n\nFuentes:\n"
          +"\n".join(f"• {x['cita_corta']} {x['url']}" for x in s['sources'])
          +"\n\nImágenes (Wikimedia Commons, dominio público o licencia libre):\n"+"\n".join(f"• {c}" for c in imgs)
          +"\n\nVoz sintética generada con IA · audio sintetizado.\nSuscríbete: @datosyociosidades\nTikTok: https://www.tiktok.com/@datosyociosidades\n\n"+" ".join(s['ht']))
    tt_caption=f"{hook} {s['title']}. "+" ".join(s['ht'])
    meta={'titulo':s['title'],'youtube_title':s['title']+' #Shorts','descripcion':desc,'hashtags':s['ht'],'tags':[h[1:] for h in s['ht']]+['DatosYOciosidades','shorts'],
          'tiktok_caption':tt_caption,'facebook_caption':tt_caption,'contenido_sintetico':True,'rehecho_de':s['orig'],'palabras':words}
    json.dump(meta,open(out+'/metadata.json','w'),ensure_ascii=False,indent=1)
    return out, words
if __name__=='__main__':
    for k in sys.argv[1:]: print(k, build(k))
