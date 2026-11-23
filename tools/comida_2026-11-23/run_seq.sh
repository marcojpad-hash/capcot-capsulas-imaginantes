cd /workspace/capcot_main/tools/comida_2026-11-23


for k in antonieta fortuna croissant agua; do
python3 - $k > /tmp/en_$k.log 2>&1 <<'PY'
import sys, json, time; sys.path.insert(0,'.'); import build
k=sys.argv[1]; s=build.SPECS[k]; out=f"{build.R}/proyectos/2026-11-23_comida-{s['slug']}"; cred=json.load(open(out+'/creditos_imagenes.json'))
json.dump(build.storyboard(s,out,cred,'en'),open(out+'/storyboard_en.json','w'),ensure_ascii=False,indent=1)
for t in range(3):
    r=build.render(out,'en'); print(k,'en',r[0],r[1]); print(r[2])
    if r[1] and 'OK' in r[1][0]: break
    time.sleep(10)
PY
done
echo ALLDONE
