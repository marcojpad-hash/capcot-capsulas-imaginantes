#!/bin/bash
set -e; cd /workspace/capcot; P=$1; H=$2; Z=$3; shift 3
A=/cursor/stores/store-cb166cf7-ee6b-484e-a44b-f434c72c9730/grok-bot/agents/74b43c8f-7eeb-486b-ba03-1764f8ea7ed4/assets
i=1; for h in "$@"; do cp $A/$h*.jpg proyectos/$P/frames/scene_00$i.jpg; i=$((i+1)); done
python3 scripts/validar_storyboard.py proyectos/$P/storyboard.json --check-doi
CAPCOT_FORZAR_CUPO=1 python3 scripts/capsula_diaria.py --storyboard proyectos/$P/storyboard.json --proveedor-img manual --fecha 2026-10-28 > _tmp/sb28/$P.log 2>&1 || { tail -20 _tmp/sb28/$P.log; exit 1; }
tail -1 _tmp/sb28/$P.log
BAD=salidas/2026-10-28_${P/2026-10-28_/2026-10-28-}; rm -rf salidas/$P; mv $BAD salidas/$P; grep -rl "${BAD#salidas/}" salidas/$P | xargs -r sed -i "s#${BAD#salidas/}#$P#g"
grep -q '"ok": false' salidas/$P/qa.json && { echo QA_FAIL; exit 1; }
ffprobe -v error -show_entries format=duration -of csv=p=0 salidas/$P/capsula.mp4
python3 scripts/publicar.py salidas/$P/ --plataforma yt --privacidad private --publish-at $Z --ejecutar 2>&1 | tail -1
python3 _tmp/sb28/fin.py $P $H
