# usage: pipe.sh ID "tags" privacidad [publishAt]
P=$1; mkdir -p salidas/$P; cp proyectos/$P/storyboard.json salidas/$P/
python3 scripts/generar_frames.py proyectos/$P/storyboard.json --proveedor manual 2>&1|tail -1
python3 scripts/montar_capsula.py proyectos/$P/storyboard.json -o salidas/$P/capsula.mp4 > _tmp/mont_$P.log 2>&1; tail -1 _tmp/mont_$P.log
[ -f salidas/$P/capsula.mp4 ] || { echo FAIL_MONTAJE $P; exit 1; }
python3 scripts/qa_capsula.py salidas/$P/capsula.mp4 salidas/$P/storyboard.json 2>&1 | grep FALLA
python3 _tmp/fixmeta.py salidas/$P "$2" | head -1
if [ -n "$4" ]; then python3 scripts/publicar.py salidas/$P --plataforma yt --ejecutar --privacidad $3 --publish-at $4 2>&1|tail -1
else python3 scripts/publicar.py salidas/$P --plataforma yt --ejecutar --privacidad $3 2>&1|tail -1; fi
