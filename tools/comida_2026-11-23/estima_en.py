import sys, asyncio, tempfile, os
sys.path.insert(0,'/workspace/capcot_main/scripts'); import montar_capsula as mc
from specs import SPECS
async def one(txt,rate):
    for t in range(6):
        try:
            f=tempfile.mktemp(suffix='.mp3'); await mc.tts(txt,'en-US-AndrewNeural',f,rate,'-2Hz'); return mc.dur(f)
        except Exception: await asyncio.sleep(3)
    raise SystemExit("tts fail")
def est(k,rate,extra,pad,cort):
    mc.PAUSAS={kk:v+extra for kk,v in {".": 0.32, "?": 0.35, "!": 0.35, "…": 0.35, ":": 0.25, ";": 0.25}.items()}
    ds=[asyncio.run(one(sc['en'],rate)) for sc in SPECS[k]['scenes']]
    return round(sum(d+0.25+pad for d in ds)+cort,1)
k,rate,extra,pad,cort=sys.argv[1],sys.argv[2],float(sys.argv[3]),float(sys.argv[4]),float(sys.argv[5])
print(k,rate,extra,pad,cort,est(k,rate,extra,pad,cort))
