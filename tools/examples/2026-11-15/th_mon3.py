from thumb import make
ac='#fa5252'
# 핵심 질문: 하이드레이션 경고는 왜 생겼고 왜 덮지 않고 경로를 없앴나 / 분위기: 디버깅·추적 / 팔레트: 짙은 자주빛 검정 + 크림슨 / 중심 오브젝트: 서버 HTML 조각과 브라우저 HTML 조각이 맞물리지 못하는 틈 (tabIndex 0 vs -1)
mono="font-family=\"'DejaVu Sans Mono','Noto Sans Mono CJK KR',monospace\""
svg=f'''<defs><filter id="g" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="26"/></filter>
<linearGradient id="p" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3a1016"/><stop offset="1" stop-color="#1f0a0d"/></linearGradient></defs>
<!-- 서버 조각 -->
<path d="M70 70 H470 L440 170 L480 260 L430 360 L470 460 H70 Z" fill="url(#p)" stroke="#7a2a33" stroke-width="6"/>
<text x="110" y="140" font-size="34" font-weight="700" fill="#ff8787">서버</text>
<text x="110" y="230" font-size="38" fill="#ffe3e3" {mono}>&lt;a</text>
<text x="110" y="300" font-size="38" fill="#ffe3e3" {mono}>tabIndex=</text>
<text x="110" y="370" font-size="54" font-weight="700" fill="{ac}" {mono}>"0"</text>
<!-- 브라우저 조각 (어긋남) -->
<path d="M610 70 H1010 V460 H610 L650 360 L600 260 L640 170 Z" fill="url(#p)" stroke="#7a2a33" stroke-width="6"/>
<text x="700" y="140" font-size="34" font-weight="700" fill="#ff8787">브라우저</text>
<text x="700" y="230" font-size="38" fill="#ffe3e3" {mono}>&lt;a</text>
<text x="700" y="300" font-size="38" fill="#ffe3e3" {mono}>tabIndex=</text>
<text x="700" y="370" font-size="54" font-weight="700" fill="{ac}" {mono}>"-1"</text>
<!-- 틈의 발광 -->
<path d="M470 70 L440 170 L480 260 L430 360 L470 460 L540 460 L600 360 L560 260 L600 170 L570 70 Z" fill="{ac}" opacity=".35" filter="url(#g)"/>
<text x="540" y="285" text-anchor="middle" font-size="86" font-weight="900" fill="{ac}">≠</text>
<text x="540" y="560" text-anchor="middle" font-size="28" fill="#ff8787">같은 코드, 다른 결과 — 속성을 맞추지 않고 합치는 경로를 없앴다</text>'''
make('th_mon3','/home/claude/out/mon/월_01_썸네일.png','#1a0608','#4a1420',ac,'Next.js 하이드레이션','경고를 덮지 않았다','tabIndex가 서버와 브라우저에서 달랐던 이유와 수정',svg,fs=92)
