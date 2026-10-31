for d in 2026-11-03_2026-11-03-kids-tiburon-groenlandia 2026-11-03_comida-maillard 2026-11-04_kids-hipo-por-que 2026-11-04_comida-miel-no-caduca 2026-11-04_inter-bioluminiscencia-mar; do
 python3 scripts/montar_capsula.py salidas/$d/storyboard.json -o salidas/$d/capsula.mp4 >> _tmp/m6.log 2>&1; echo "$d EXIT $? $(tail -1 _tmp/m6.log)" >> _tmp/m6.res; done
