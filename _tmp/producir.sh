#!/bin/bash
# uso: producir.sh SRC PID CAMA HASHTAGS hash1 ... hash8
set -e; SRC=$1; P=$2; CAMA=$3; TAGS=$4; shift 4
A=/cursor/stores/store-cb166cf7-ee6b-484e-a44b-f434c72c9730/grok-bot/agents/74b43c8f-7eeb-486b-ba03-1764f8ea7ed4/assets
F=proyectos/$P/frames; mkdir -p $F; i=1
for h in "$@"; do ffmpeg -loglevel error -y -i $A/$h*.jpg -vf "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920" -q:v 2 $F/scene_00$i.jpg; i=$((i+1)); done
python3 _tmp/normalizar_cola.py $SRC $P $CAMA silencio "$TAGS"
python3 - <<P
import json;f='proyectos/$P/storyboard.json';d=json.load(open(f));d['voice']['rate']='-2%';d['voice']['pad_seconds']=0.7;json.dump(d,open(f,'w'),ensure_ascii=False,indent=1)
P
python3 scripts/montar_capsula.py proyectos/$P/storyboard.json -o salidas/$P/capsula.mp4 > _tmp/montar_$P.log 2>&1; tail -1 _tmp/montar_$P.log
cp proyectos/$P/storyboard.json salidas/$P/
python3 scripts/qa_capsula.py salidas/$P/capsula.mp4 salidas/$P/storyboard.json > salidas/$P/qa.txt 2>&1 || true; grep -E "FALLA|duracion" salidas/$P/qa.txt
