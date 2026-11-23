#!/usr/bin/env python3
"""Grupo B animales (23-nov-2026). Uso: python3 build.py frames|sb|render|post <key> [es|en]"""
import json, os, sys, subprocess, shutil, urllib.request
from PIL import Image, ImageFilter, ImageEnhance
HERE = os.path.dirname(os.path.abspath(__file__)); R = '/workspace/capcot_main'
sys.path.insert(0, HERE); sys.path.insert(0, R + '/tools/rehechos_2026-11-22')
from specs_animales import SPECS
from commons import by_title, UA
W, H = 1080, 1920
def pdir(k): return f"{R}/proyectos/{SPECS[k].get('dir', '2026-11-23_animal-' + k)}"
def prep(src, dst):
    im = Image.open(src).convert('RGB')
    bg = im.copy(); r = max(W/bg.width, H/bg.height); bg = bg.resize((int(bg.width*r)+1, int(bg.height*r)+1))
    bg = bg.crop(((bg.width-W)//2, (bg.height-H)//2, (bg.width-W)//2+W, (bg.height-H)//2+H)).filter(ImageFilter.GaussianBlur(40))
    bg = ImageEnhance.Brightness(bg).enhance(0.55)
    r = min(W/im.width, 1500/im.height); fg = im.resize((int(im.width*r), int(im.height*r)), Image.LANCZOS)
    y = int(H*0.56-fg.height/2); bg.paste(fg, ((W-fg.width)//2, max(y, 0))); bg.save(dst, quality=92)
def frames(k):
    s = SPECS[k]; out = pdir(k); os.makedirs(out+'/frames', exist_ok=True); os.makedirs(out+'/raw', exist_ok=True)
    cred = {}
    for i, sc in enumerate(s['scenes']):
        key = f'scene_{i+1:03d}'; img = sc[2]; raw = f'{out}/raw/{key}.jpg'
        if img.startswith('IA:'):
            shutil.copy(f'{HERE}/{img[3:]}', raw)
            cred[key] = {'file': ('Ilustración propia generada con IA (lazo y baumanómetro; sin personaje ni arte de DC)' if k == 'wonder-woman' else 'Ilustración generada con IA (no es una foto de Billy)'), 'artist': 'Datos y ociosidades (IA)', 'lic': 'ilustración propia generada con IA',
                         'page': '', 'biblioteca': 'ninguna: ilustración del canal'}
        else:
            m = by_title(img)
            if not os.path.exists(raw):
                open(raw, 'wb').write(urllib.request.urlopen(urllib.request.Request(m['thumb'], headers=UA), timeout=60).read())
            desc = m['artist']; lib = 'Wikimedia Commons'
            if 'LCCN' in img or 'ppmsca' in img: lib = 'Library of Congress vía Wikimedia Commons'
            elif 'Sig Corps' in img or ('NARA' in img and 'SC-' in img): lib = 'U.S. National Archives (NARA) / Signal Corps vía Wikimedia Commons'
            elif 'NARA' in img or 'National Archives' in m['artist']: lib = 'U.S. National Archives (NARA) vía Wikimedia Commons'
            elif 'Medal of Honor' in img: lib = 'U.S. Army vía Wikimedia Commons'
            elif 'Google Art Project' in img: lib = 'Google Arts & Culture vía Wikimedia Commons'
            elif 'IWM' in img: lib = 'Imperial War Museums vía Wikimedia Commons'
            elif 'Wellcome' in img: lib = 'Wellcome Collection vía Wikimedia Commons'
            elif 'geograph' in img: lib = 'Geograph Britain and Ireland vía Wikimedia Commons'
            m['biblioteca'] = lib; cred[key] = m
        prep(raw, f'{out}/frames/{key}.jpg')
    json.dump(cred, open(f'{out}/creditos_imagenes.json', 'w'), ensure_ascii=False, indent=1)
def credit(c):
    if not c.get('page'): return c['file'] + '.'
    return f"{c['file'].replace('File:', '').rsplit('.', 1)[0]}. {c['artist']}, {c['lic']}. {c['biblioteca']}: {c['page']}"
def sb(k, lang):
    s = SPECS[k]; out = pdir(k); cred = json.load(open(f'{out}/creditos_imagenes.json')); en = lang == 'en'
    scenes = []
    for i, sc in enumerate(s['scenes']):
        key = f'scene_{i+1:03d}'; capa = None
        if sc[3]:
            capa = {kk: v for kk, v in sc[3].items() if not kk.endswith('_en')}
            if en:
                for kk in ('titulo', 'valor', 'etiqueta'):
                    if kk + '_en' in sc[3]: capa[kk] = sc[3][kk + '_en']
                capa['fuente'] = capa.get('fuente', '').replace('Gobierno de Japón', 'Government of Japan').replace('estimación Univ. Kansai', 'Kansai Univ. estimate')
        n = len(s['scenes'])
        x = {'id': key, 'arc': 'hook_medias_res' if i == 0 else ('reflexion_o_pregunta' if i == n-1 else 'desarrollo'), 'duration_seconds': 10,
             'narration': sc[1] if en else sc[0], 'on_screen_text': '', 'asset_filename': f'frames/{key}.jpg', 'sfx': [s['sfx']],
             'source_ids': [z['id'] for z in s['sources']], 'image_credit': credit(cred[key])}
        if capa: x['capa'] = capa
        scenes.append(x)
    aviso_es = 'Imágenes de dominio público o licencia libre (Wikimedia Commons y archivos citados en la descripción).' + (' Escena 1: ilustración generada con IA.' if k in ('billy', 'wonder-woman') else '') + ' Voz sintética (IA).'
    aviso_en = 'Public-domain or freely licensed images (Wikimedia Commons and archives credited in the description).' + (' Scene 1: AI-generated illustration.' if k in ('billy', 'wonder-woman') else '') + ' Synthetic voice (AI / IA).'
    d = {'project_id': os.path.basename(pdir(k)) + ('_en' if en else ''), 'serie': 'Cómics y ciencia' if k == 'wonder-woman' else 'Dato del día' if k == 'thanksgiving' else 'Animales con oficio humano (dato del día)', 'title': s['title_en' if en else 'title_es'],
         'titulo': s['cover_en' if en else 'cover_es'], 'language': 'en-US' if en else 'es-MX', 'aspect_ratio': '9:16', 'target_duration_seconds': 88,
         'estilo_id': 'foto_commons', 'estilo_visual': 'fotografías de dominio público o licencia libre', 'proveedor_imagenes': 'Wikimedia Commons (PD/CC, créditos en creditos_imagenes.json)' + ('; escena 1 ilustración IA' if k in ('billy', 'wonder-woman') else ''),
         'parece_real': True, 'keywords': [s['tema']],
         'titulo_estilo': {'size': 96, 'caja_rgb': [205, 25, 25], 'texto_rgb': [255, 222, 0], 'subrayado_rgb': [255, 222, 0]},
         'voice': {'engine': 'edge-tts', 'voice_id': 'en-US-AndrewMultilingualNeural' if en else 'es-MX-JorgeNeural', 'rate': '+7%', 'pitch': '-2Hz', 'pad_seconds': 0.3, 'modo_pausas': 'continuo'},
         'audio': {'music_asset': 'sintetico:' + s['cama'], 'cama_musical': s['cama'], 'music_bpm': 96, 'music_lufs': -27, 'ambiente_lufs': -31},
         'canal': {'nombre': 'Datos y ociosidades', 'handle': '@datosyociosidades'}, 'sources': s['sources'], 'scenes': scenes,
         'cortinilla_fuentes': {'duration_seconds': 6, 'titulo': 'Sources' if en else 'Fuentes', 'aviso': aviso_en if en else aviso_es,
                                'firma': 'Datos y ociosidades · @datosyociosidades', 'bg_rgb': [18, 16, 14]},
         'export': {'filename': 'capsula_en.mp4' if en else 'capsula.mp4', 'resolution': '1080x1920', 'fps': 30, 'loudness_lufs': -14, 'plano_seconds': 4.0, 'subtitle_max_words': 3},
         'estructura': 'historia', 'hook_type': 'animal_con_oficio_humano'}
    if en: d['cortinilla_fuentes']['aviso'] = d['cortinilla_fuentes']['aviso'].replace('(IA)', '(AI)')
    if en: d['voice']['rate'] = '+5%'
    fn = f'{out}/storyboard_en.json' if en else f'{out}/storyboard.json'
    json.dump(d, open(fn, 'w'), ensure_ascii=False, indent=1); return fn
def render(k, lang):
    out = pdir(k); en = lang == 'en'; fn = sb(k, lang); mp4 = f'{out}/capsula_en.mp4' if en else f'{out}/capsula.mp4'
    for _ in range(3):
        r = subprocess.run(['python3', R + '/scripts/montar_capsula.py', fn, '-o', mp4], capture_output=True, text=True)
        if r.returncode == 0: break
    open(f'{out}/render{"_en" if en else ""}.log', 'w').write(r.stdout + r.stderr); print(r.stdout[-400:], r.stderr[-800:])
    q = subprocess.run(['python3', R + '/scripts/qa_capsula.py', mp4, fn], capture_output=True, text=True, cwd=R)
    if not os.path.exists(f'{out}/qa.json'): print('QA NO CORRIÓ', q.stderr[-500:]); return
    shutil.move(f'{out}/qa.json', f'{out}/qa{"_en" if en else "_es"}.json'); print(q.stdout)
    if not en: subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', mp4, '-frames:v', '1', '-q:v', '2', f'{out}/portada.jpg'], check=True)
    else: subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', mp4, '-frames:v', '1', '-q:v', '2', f'{out}/portada_en.jpg'], check=True)
if __name__ == '__main__':
    cmd, k = sys.argv[1], sys.argv[2]; lang = sys.argv[3] if len(sys.argv) > 3 else 'es'
    {'frames': lambda: frames(k), 'sb': lambda: print(sb(k, lang)), 'render': lambda: render(k, lang)}[cmd]()
