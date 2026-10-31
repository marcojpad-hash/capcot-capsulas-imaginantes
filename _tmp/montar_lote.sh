cd /workspace/capcot
m(){ python3 scripts/montar_capsula.py $1 -o $2 > _tmp/m4_$(basename $(dirname $2)).log 2>&1; echo "$2 EXIT $? $(tail -1 _tmp/m4_$(basename $(dirname $2)).log)"; }
for p in 2026-10-31_murcielagos-viroma-global 2026-11-01_pulpo-tres-corazones 2026-11-01_llorar-cebolla-quimica 2026-11-02_camaron-mantis 2026-10-30_arqueas-origen-eucariotas 2026-10-26_baffin-bay-ice-shelf 2026-11-02_comida-pan-duro 2026-10-31_sequias-energia-renovable; do m proyectos/$p/storyboard.json salidas/$p/capsula_v4.mp4; done
m salidas/2026-11-03_2026-11-03-kids-tiburon-groenlandia/storyboard.json salidas/2026-11-03_2026-11-03-kids-tiburon-groenlandia/capsula.mp4
