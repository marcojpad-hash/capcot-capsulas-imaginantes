#!/usr/bin/env python3
"""metadata.json + guion.md por cápsula (Grupo B animales, 23-nov-2026)."""
import json, os, sys, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from specs_animales import SPECS
R = '/workspace/capcot_main'
def yt_tt_hashtags(raw):
    temas=[h for h in (raw or []) if h.lower() not in ('#shorts','#short','#sabiasque')]
    yt=temas[:5]+(['#sabiasque'] if '#sabiasque' not in [x.lower() for x in temas] else [])+['#Shorts']
    tt=temas[:5]
    if len(tt)<4:
        for f in ('#animales','#historia','#sabiasque','#curiosidades'):
            if f.lower() not in {x.lower() for x in tt} and len(tt)<4: tt.append(f)
    return yt, tt[:5]
def dur(p):
    return round(float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p]).decode()), 2) if os.path.exists(p) else None
def creds(cr, en, s=None):
    out = []
    for k, c in cr.items():
        if not c.get('page'):
            out.append((s or {}).get('ia_nota_en' if en else 'ia_nota_es') or ('Scene 1: AI-generated illustration (no free photo of Billy exists); Datos y ociosidades.' if en else 'Escena 1: ilustración generada con IA (no hay foto libre de Billy); Datos y ociosidades.'))
            continue
        line = f"{c['file'].replace('File:', '').rsplit('.', 1)[0]} — {c['artist'].replace('Unknown authorUnknown author', 'Unknown author')}, {c['lic']} — {c['biblioteca'].replace(' vía ', ' via ') if en else c['biblioteca']}: {c['page']}"
        if line not in out: out.append(line)
    return out
def run(k):
    s = SPECS[k]; d = f"{R}/proyectos/{s.get('dir', '2026-11-23_animal-' + k)}"; cr = json.load(open(f'{d}/creditos_imagenes.json'))
    m = {'project_id': os.path.basename(d), 'hueco': s['hueco'], 'publishAt_utc': s.get('publishAt_utc'), 'hueco_plataformas': 'YouTube ES (Mj sube), TikTok @datosyociosidades', 'contenido_sintetico': True}
    for lang in ('es', 'en'):
        en = lang == 'en'; hook = s['scenes'][0][1 if en else 0]
        hook1 = hook.split('. ')[0].rstrip('.') + '.'
        yt_hs, tt_hs = yt_tt_hashtags(s['ht_' + lang])
        src = '\n'.join(f"• {x['cita_corta']} {x['url']}" for x in s['sources'] + s.get('fuentes_extra', []))
        desc = (f"{hook}\n\n{s['title_'+lang]}." + (" A Datos y ociosidades capsule: verified facts told as a story." if en else " Una cápsula de Datos y ociosidades: datos verificados contados como historia.")
                + ("\n\nSources:\n" if en else "\n\nFuentes:\n") + src
                + ("\n\nImages (public domain or free licence):\n" if en else "\n\nImágenes (dominio público o licencia libre):\n") + '\n'.join('• ' + c for c in creds(cr, en, s))
                + ("\n\nSynthetic AI voice · synthesized audio." if en else "\n\nVoz sintética generada con IA · audio sintetizado.")
                + ("\nSpanish channel: @datosyociosidades" if en else "\nSuscríbete: @datosyociosidades")
                + ('\n' + s['extra_desc_' + lang] if s.get('extra_desc_' + lang) else '') + "\nTikTok: https://www.tiktok.com/@datosyociosidades\n\n" + ' '.join(yt_hs))
        cap = (s.get('caption_' + lang) or f"{hook1} {s['title_'+lang]}.") + ' ' + ' '.join(tt_hs)
        m.update({f'titulo_{lang}': s['title_' + lang], f'youtube_title_{lang}': (s['title_' + lang] + ' #Shorts') if len(s['title_' + lang])+8<=100 else s['title_' + lang], f'portada_texto_{lang}': s['cover_' + lang],
                  f'descripcion_{lang}': desc, f'caption_tiktok_{lang}': cap, f'hashtags_{lang}': yt_hs,
                  f'mp4_{lang}': f"{d}/{'capsula_en.mp4' if en else 'capsula.mp4'}", f'duracion_{lang}_s': dur(f"{d}/{'capsula_en.mp4' if en else 'capsula.mp4'}"),
                  f'palabras_{lang}': sum(len(x[1 if en else 0].split()) for x in s['scenes'])})
        assert len(desc.encode()) < 5000 and '<' not in desc and '>' not in desc
    json.dump(m, open(f'{d}/metadata.json', 'w'), ensure_ascii=False, indent=1)
    g = f"# {s['title_es']} / {s['title_en']}\n\nHueco: {s['hueco']} · Portada: «{s['cover_es']}» / «{s['cover_en']}»\n\n"
    for i, sc in enumerate(s['scenes']):
        g += f"## Escena {i+1}\n**ES:** {sc[0]}\n\n**EN:** {sc[1]}\n\n_Imagen:_ {sc[2]}\n\n"
    g += "## Fuentes\n" + '\n'.join(f"- {x['cita_corta']} {x['url']}" for x in s['sources']) + "\n\n## Imágenes\n" + '\n'.join('- ' + c for c in creds(cr, False, s)) + "\n"
    open(f'{d}/guion.md', 'w').write(g); print(k, m['duracion_es_s'], m['duracion_en_s'])
if __name__ == '__main__':
    for k in (sys.argv[1:] or SPECS): run(k)
