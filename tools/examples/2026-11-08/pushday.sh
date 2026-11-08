#!/bin/bash
# 사용법: bash pushday.sh <요일한글> <요일영문> <게시일> <원고빌드스크립트>  예: bash pushday.sh 월 mon 2026-10-26 build_mon.py
set -e
K=$1; E=$2; D=$3; B=$4
R=/home/claude/blog-images; F=${D}_${E}
mkdir -p $R/$F
for p in /home/claude/out/$E/${K}_*.png; do n=$(basename $p | cut -d_ -f2); cp $p $R/$F/${E}_$n.png; done
cd $R && git add $F && git commit -qm "$F: 본문 이미지 $(ls $F | wc -l)장" && git push -q origin main && echo pushed $F
cd /home/claude/work/wk && IMG_URL_BASE=https://myway0104.github.io/blog-images/$F OUT=$(ls /home/claude/out/$E/*.html | grep -v 이미지주소포함 | sed 's/\.html$/_이미지주소포함.html/') python3 $B
ls $R/$F
