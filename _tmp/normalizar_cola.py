#!/usr/bin/env python3
"""Normaliza storyboard de cola (V2 / paquete) al formato baffin para montar_capsula. No cambia texto."""
import json,sys,copy
src,pid,cama,amb,tags=sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5].split(',')
T=json.load(open('proyectos/2026-10-26_baffin-bay-ice-shelf/storyboard.json'))
d=json.load(open(src))
o={}
for k in ['project_id','serie','language','aspect_ratio','target_duration_seconds','estructura','trend_source','resumen','keywords','estilo_id','estilo_visual','sources']:
    if k in d: o[k]=d[k]
o['project_id']=pid
tt=d.get('titulo_yt') or (d['title']+' #Shorts')
o['title']=tt; o['titulo']=d['titulo']; o['audience']=T['audience']
o['voice']=T['voice']
sc=[]
for i,s in enumerate(d['scenes'],1):
    s=copy.deepcopy(s); s['asset_filename']=f'frames/scene_{i:03d}.jpg'; s['asset_type']='image'
    s.setdefault('motion','kenburns_auto'); s['animated_hook']=False
    s['ambiente']=amb; s['sfx']=[x for x in (s.get('sfx') or []) if x in ('olas','gaviotas','lluvia','tormenta','truenos','viento','viento_costa','campanas','reloj','pluma','madera')] or ['viento']
    s['image_origen']=T['scenes'][0]['image_origen']; sc.append(s)
o['scenes']=sc
cf=copy.deepcopy(T['cortinilla_fuentes']); cf.pop('fuentes_en_pantalla',None)
cf['fuentes_en_pantalla']=[(x.get('ref_display') or x.get('cita_corta'))+(f", doi:{x['doi']}" if x.get('doi') and 'doi' not in (x.get('ref_display') or '') else '') for x in d['sources']][:4]
o['cortinilla_fuentes']=cf
a=copy.deepcopy(T['audio']); a['music_asset']='sintetico:'+cama; a['cama_musical']=cama; o['audio']=a
o['export']=T['export']; o['proveedor_imagenes']='Generador de imágenes IA de Grok Bot; ocho imágenes ilustrativas generadas para este paquete y ajustadas a 1080x1920.'
o['parece_real']=False; o['canal']=T['canal']
fu='\n'.join(f"• {x['cita_corta']} {x['url']}" for x in d['sources'])
o['publicacion']={'youtube':{'privacy':'private','publishAt':'','titulo':tt,'tags':['#Shorts']+[t.lstrip('#') for t in tags],'synthetic_content':True}}
o['estado_produccion']='MONTADO_PENDIENTE_PROGRAMAR'
json.dump(o,open(f'proyectos/{pid}/storyboard.json','w'),ensure_ascii=False,indent=1)
hook=sc[0]['narration']
desc=f"{hook}\n\n{tt}. Una cápsula de Datos y ociosidades: datos verificados contados como historia.\n\nFuentes:\n{fu}\n\nImágenes generadas con IA · voz sintética · audio sintetizado.\nSuscríbete: @datosyociosidades\nTikTok: https://www.tiktok.com/@datosyociosidades\n\n{' '.join(tags)} #Shorts"
m=json.load(open('salidas/2026-10-26_baffin-bay-ice-shelf/metadata.json'))
m.update(titulo=tt,descripcion=desc,hashtags=tags+['#Shorts'],tags=[t.lstrip('#') for t in tags]+['Shorts'],
 tiktok_caption=f"{hook}\n\n{d.get('resumen','')}\n\nFuentes en YouTube @datosyociosidades\n\n{' '.join(tags)}",tiktok_hashtags=tags,
 tiktok_descripcion_completa=desc.replace('Suscríbete: @datosyociosidades\nTikTok: https://www.tiktok.com/@datosyociosidades','Fuentes en YouTube @datosyociosidades'))
import os; os.makedirs(f'salidas/{pid}',exist_ok=True)
json.dump(m,open(f'salidas/{pid}/metadata.json','w'),ensure_ascii=False,indent=1)
print('ok',len(sc),tt,len(desc))
