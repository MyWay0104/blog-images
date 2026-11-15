#!/bin/bash
# 사용법: bash check.sh <요일한글> <html파일>  — 이미지 번호/파일 존재/** 잔존/금지어 점검
# 금지어 목록은 공개 저장소에 올리지 않는다. 환경변수 FORBID(정규식, '|'로 구분)로 넘기거나 같은 폴더의 forbid.txt(한 줄 정규식)에 둔다.
K=$1; f=$2; d=$(dirname "$f")
FORBID="${FORBID:-$(cat "$(dirname "$0")/forbid.txt" 2>/dev/null)}"
echo "--- 이미지 번호 순서"
grep -o "\[이미지 [0-9]*: ${K}_[0-9]*_[^ ]*" "$f" | awk '{n=$2; sub(":","",n); split($3,a,"_"); printf "%s %s %s\n", n, a[2], (n+0==a[2]+0?"ok":"MISMATCH")}'
echo "--- 파일 존재"
for p in $(grep -o "${K}_[0-9]*_[^ |]*\.png" "$f" | sort -u); do [ -f "$d/$p" ] && echo "ok $p" || echo "MISSING $p"; done
echo "--- ** 잔존: $(grep -o '\*\*' "$f" | wc -l)"
echo "--- 금지어"
if [ -n "$FORBID" ]; then grep -n -i -E "$FORBID" "$f" | cut -c1-160; else echo "(FORBID 미설정 — 금지어 검사 건너뜀)"; fi
echo "(끝)"
