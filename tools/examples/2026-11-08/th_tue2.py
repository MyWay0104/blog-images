from thumb import make
ac='#ff922b'
# 핵심 질문: 컨텍스트가 차면 /clear와 /compact 중 뭘 치나 / 분위기: 비교·선택 / 팔레트: 짙은 갈색 배경 + 주황 / 중심 오브젝트: 꽉 찬 창 하나가 두 갈래로 — 왼쪽은 빈 창(비움), 오른쪽은 작게 접힌 창(압축)
svg=f'''<defs><filter id="g" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="22"/></filter>
<marker id="m" markerUnits="userSpaceOnUse" markerWidth="26" markerHeight="26" refX="20" refY="13" orient="auto"><path d="M0,0 L26,13 L0,26 z" fill="{ac}"/></marker></defs>
<!-- full window -->
<rect x="430" y="10" width="220" height="150" rx="22" fill="#2b1a08" stroke="{ac}" stroke-width="6"/>
<g fill="{ac}"><rect x="450" y="26" width="180" height="20" rx="5" opacity=".55"/><rect x="450" y="52" width="180" height="20" rx="5" opacity=".7"/><rect x="450" y="78" width="180" height="20" rx="5" opacity=".85"/><rect x="450" y="104" width="180" height="20" rx="5"/><rect x="450" y="130" width="180" height="20" rx="5"/></g>
<text x="540" y="200" text-anchor="middle" font-size="24" fill="#ffd8a8">꽉 찬 컨텍스트</text>
<!-- arrows -->
<path d="M470 170 L300 275" stroke="{ac}" stroke-width="10" fill="none" marker-end="url(#m)"/>
<path d="M610 170 L780 275" stroke="{ac}" stroke-width="10" fill="none" marker-end="url(#m)"/>
<!-- left: empty window -->
<rect x="130" y="290" width="240" height="170" rx="22" fill="{ac}" opacity=".22" filter="url(#g)"/>
<rect x="130" y="290" width="240" height="170" rx="22" fill="#2b1a08" stroke="{ac}" stroke-width="6"/>
<rect x="150" y="422" width="200" height="22" rx="6" fill="{ac}" opacity=".55"/>
<text x="250" y="375" text-anchor="middle" font-size="44" font-weight="900" fill="#fff">/clear</text>
<text x="250" y="505" text-anchor="middle" font-size="25" fill="#ffd8a8">비운다 · 비용 없음</text>
<!-- right: compacted window -->
<rect x="710" y="290" width="240" height="170" rx="22" fill="{ac}" opacity=".22" filter="url(#g)"/>
<rect x="710" y="290" width="240" height="170" rx="22" fill="#2b1a08" stroke="{ac}" stroke-width="6"/>
<rect x="730" y="422" width="200" height="22" rx="6" fill="{ac}" opacity=".55"/>
<rect x="730" y="388" width="200" height="28" rx="6" fill="#ffa94d"/>
<text x="830" y="408" text-anchor="middle" font-size="18" font-weight="700" fill="#1c1006">요약</text>
<text x="830" y="365" text-anchor="middle" font-size="44" font-weight="900" fill="#fff">/compact</text>
<text x="830" y="505" text-anchor="middle" font-size="25" fill="#ffd8a8">요약으로 줄인다</text>'''
make('th_tue2','/home/claude/out/tue/화_01_썸네일.png','#1c1006','#5a3410',ac,'컨텍스트가 찼다','비울까, 압축할까?','Claude Code /clear vs /compact, 공식 문서로 비교',svg,fs=96)
