#!/usr/bin/env python3
"""Monta la cápsula con la narración YA existente (no regenera TTS)."""
import json, os, sys, re, subprocess, tempfile
sys.path.insert(0, '../../scripts'); import montar_capsula as mc, cama_sonora as cs
B = os.path.abspath('.'); SAL = os.path.abspath('../../salidas/2026-10-25-reina-olor')
sb = json.load(open('storyboard.json')); VOZ = f'{SAL}/narracion.mp3'; FPS = 30
NAR = mc.dur(VOZ); CORT = sb['cortinilla_fuentes']['duracion']; TOTAL = NAR + CORT
tmp = tempfile.mkdtemp(prefix='reina_'); run = mc.run
# --- subtítulos: palabras con tiempo proporcional dentro de cada cue del VTT
def t2s(x): h, m, s = x.replace(',', '.').split(':'); return int(h)*3600+int(m)*60+float(s)
words = []
for b in open(f'{SAL}/narracion.vtt').read().strip().split('\n\n'):
    l = b.strip().split('\n')
    if len(l) < 3 or '-->' not in l[1]: continue
    a, z = [t2s(x.strip()) for x in l[1].split('-->')]; a = max(a, words[-1][1] if words else 0)
    ws = ' '.join(l[2:]).split(); tot = sum(len(w)+1 for w in ws); t = a
    for w in ws: d = (z-a)*(len(w)+1)/tot; words.append((t, t+d*0.95, w)); t += d
mc.ass_from_srt(mc.srt_from_words(words, 3), f'{tmp}/subs.ass')
# --- video: planos ~2.5 s por escena, cortes exactos por frame acumulado
parts = []; k = 0; prev = 0
for i, s in enumerate(sb['scenes']):
    end = NAR if i == len(sb['scenes'])-1 else s['end']
    ov = None
    if s['on_screen_text']: ov = f'{tmp}/t{i}.png'; mc.texto_png(s['on_screen_text'], ov, gancho=(i == 0))
    n = mc.n_planos(end - s['start']); seg = (end - s['start'])/n
    for j in range(n):
        f_end = round((s['start'] + seg*(j+1))*FPS) if not (i == len(sb['scenes'])-1 and j == n-1) else round(NAR*FPS)
        fr = f_end - prev; prev = f_end; out = f'{tmp}/p{k:03}.mp4'
        mc._plano(s['asset_filename'], fr/FPS, out, mc.MOVS[k % len(mc.MOVS)], ov if j == 0 else None, 3.0 if j == 0 and i > 0 else None)
        parts.append(out); k += 1
# cortinilla: frame 10 oscurecido de fondo + texto
mc.cortinilla(sb, f'{tmp}/cort.png')
from PIL import Image, ImageEnhance
bg = ImageEnhance.Brightness(Image.open('frames/scene_010.jpg')).enhance(0.18)
txt = Image.open(f'{tmp}/cort.png').convert('RGB'); mask = txt.convert('L').point(lambda v: 255 if v > 40 else 0)
bg.paste(txt, (0, 0), mask); bg.save(f'{tmp}/cort2.png')
run(['ffmpeg','-y','-loop','1','-i',f'{tmp}/cort2.png','-vf','fade=t=in:d=0.5,format=yuv420p','-frames:v',str(round(CORT*FPS)),'-c:v','libx264','-preset','veryfast','-crf','20','-r','30',f'{tmp}/cort.mp4'])
parts.append(f'{tmp}/cort.mp4')
open(f'{tmp}/l.txt','w').writelines(f"file '{p}'\n" for p in parts)
run(['ffmpeg','-y','-f','concat','-safe','0','-i',f'{tmp}/l.txt','-c','copy',f'{tmp}/video.mp4'])
# --- cama: ambiente por escena (sfx reales del manifest) + música sintética; baja a ~5 % en cortinilla
durs = [((s['sfx']), (NAR if i == len(sb['scenes'])-1 else s['end']) - s['start']) for i, s in enumerate(sb['scenes'])]
durs[0] = (durs[0][0], durs[0][1] + sb['scenes'][0]['start']); durs.append(('viento', CORT))
cs.guardar(cs.pista_sfx(durs, TOTAL, '../../assets/sfx'), f'{tmp}/amb.wav')
cs.guardar(cs.musica(TOTAL, 92, 'pulso'), f'{tmp}/mus.wav')
run(['ffmpeg','-y','-i',f'{tmp}/amb.wav','-af','loudnorm=I=-30:TP=-3','-ar','48000',f'{tmp}/amb_n.wav'])
run(['ffmpeg','-y','-i',f'{tmp}/mus.wav','-af','loudnorm=I=-27:TP=-3','-ar','48000',f'{tmp}/mus_n.wav'])
env = f"volume='if(lt(t,{NAR:.2f}),1,max(0.05,1-(t-{NAR:.2f})/1.5))':eval=frame"
fc = (f"[1:a]loudnorm=I=-16:TP=-1.5,aresample=48000,apad[v];[v]asplit[v1][v2];"
      f"[2:a][3:a]amix=inputs=2:normalize=0[c];[c][v2]sidechaincompress=threshold=0.05:ratio=6:attack=20:release=300[cd];"
      f"[cd]{env},afade=t=out:st={TOTAL-1.5:.2f}:d=1.5[cf];[v1][cf]amix=inputs=2:normalize=0,atrim=0:{TOTAL:.2f}[a]")
sub = f'{tmp}/subs.ass'
run(['ffmpeg','-y','-i',f'{tmp}/video.mp4','-i',VOZ,'-i',f'{tmp}/amb_n.wav','-i',f'{tmp}/mus_n.wav','-filter_complex',
     fc + f";[0:v]ass={sub}[vo]",'-map','[vo]','-map','[a]','-c:v','libx264','-preset','medium','-crf','20','-pix_fmt','yuv420p',
     '-r','30','-c:a','aac','-b:a','192k','-ar','48000','-t',f'{TOTAL:.2f}','-movflags','+faststart',f'{SAL}/capsula.mp4'])
print('OK', f'{SAL}/capsula.mp4', TOTAL)
