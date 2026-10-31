import json,sys,os
sys.path.insert(0,'scripts'); import metadata
d,tags=sys.argv[1],sys.argv[2].split()
metadata.generar(d,"storyboard.json")
p=os.path.join(d,"metadata.json"); m=json.load(open(p))
base="#datos #ciencia #sabiasque #Shorts #DatosYOciosidades".split()
old=" ".join(m["hashtags"]); h=list(dict.fromkeys(tags+base))
m["hashtags"]=h; m["tags"]=[x.lstrip("#") for x in h]
m["descripcion"]=m["descripcion"].replace(old," ".join(h))
t=m["titulo"]
while t.count("#Shorts")>1: t=t.replace(" #Shorts","",1)
m["titulo"]=t
json.dump(m,open(p,"w"),ensure_ascii=False,indent=2)
print(m["titulo"]); print(m["descripcion"][-300:])
