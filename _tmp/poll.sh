for i in $(seq 50); do
 out=""; for d in proyectos/2026-10-{27_corneja-decision-rapida,25_corales-contacto,28_mosquito-fruitless-audicion,29_juno-choque-proa,31_pardelas-jetlag-solar}; do out="$out $(basename $d):$(ls $d/frames 2>/dev/null|wc -l)"; done
 echo "$(date +%T)$out"; sleep 30; done
