import sys, asyncio, tempfile, os, subprocess
sys.path.insert(0,'/workspace/capcot_main/scripts'); import montar_capsula as mc
from specs import SPECS
from concurrent.futures import ThreadPoolExecutor
def one(args):
    txt,voice,rate=args; f=tempfile.mktemp(suffix='.mp3'); asyncio.run(mc.tts(txt,voice,f,rate,'-2Hz')); return mc.dur(f)
def est(key,lang):
    s=SPECS[key]; v,r=('en-US-AndrewNeural','+5%') if lang=='en' else ('es-MX-JorgeNeural','+7%')
    with ThreadPoolExecutor(6) as ex: ds=list(ex.map(one,[(sc[lang],v,r) for sc in s['scenes']]))
    tot=sum(d+0.25+0.35 for d in ds)+6
    print(key,lang,sum(len(sc[lang].split()) for sc in s['scenes']),'palabras',round(tot,1),'s')
for a in sys.argv[2:]: est(a,sys.argv[1])
