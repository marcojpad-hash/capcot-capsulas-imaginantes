while pgrep -f montar_lote.sh >/dev/null; do sleep 10; done
for d in 2026-11-03_comida-maillard 2026-11-04_kids-hipo-por-que 2026-11-04_comida-miel-no-caduca 2026-11-04_inter-bioluminiscencia-mar; do
 python3 scripts/montar_capsula.py salidas/$d/storyboard.json -o salidas/$d/capsula.mp4 >> _tmp/m5.log 2>&1; echo "$d EXIT $? $(ls salidas/$d/capsula.mp4 2>&1)" >> _tmp/m5.log; done
