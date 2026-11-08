from thumb import make
ac='#845ef7'
# 핵심 질문: 서브에이전트와 Agent Teams는 뭐가 다른가 / 분위기: 비교·선택 / 팔레트: 짙은 남보라 배경 + 보라 / 중심 오브젝트: 왼쪽은 위 상자 하나로 화살표가 모이는 모양(보고), 오른쪽은 상자 셋이 서로 연결된 모양(협업)
svg=f'''<defs><filter id="g" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="22"/></filter>
<marker id="m" markerUnits="userSpaceOnUse" markerWidth="26" markerHeight="26" refX="20" refY="13" orient="auto"><path d="M0,0 L26,13 L0,26 z" fill="{ac}"/></marker></defs>
<!-- left: report structure -->
<rect x="120" y="60" width="300" height="90" rx="22" fill="{ac}" opacity=".28" filter="url(#g)"/>
<rect x="120" y="60" width="300" height="90" rx="22" fill="#241a45" stroke="{ac}" stroke-width="6"/>
<text x="270" y="118" text-anchor="middle" font-size="34" font-weight="900" fill="#fff">메인</text>
<g fill="#1a1233" stroke="#6f5bd0" stroke-width="5">
<rect x="70" y="330" width="120" height="90" rx="18"/><rect x="210" y="330" width="120" height="90" rx="18"/><rect x="350" y="330" width="120" height="90" rx="18"/>
</g>
<g stroke="{ac}" stroke-width="8" fill="none" marker-end="url(#m)">
<path d="M130 325 L200 165"/><path d="M270 325 L270 165"/><path d="M410 325 L340 165"/>
</g>
<text x="270" y="500" text-anchor="middle" font-size="28" fill="#d0bfff">결과만 보고</text>
<!-- divider -->
<line x1="540" y1="60" x2="540" y2="520" stroke="#3b2d6b" stroke-width="4" stroke-dasharray="14 12"/>
<!-- right: team structure -->
<rect x="640" y="60" width="340" height="70" rx="18" fill="#1a1233" stroke="{ac}" stroke-width="5" stroke-dasharray="16 10"/>
<text x="810" y="107" text-anchor="middle" font-size="26" font-weight="700" fill="#d0bfff">공유 작업 목록</text>
<g fill="#241a45" stroke="{ac}" stroke-width="6">
<rect x="600" y="300" width="110" height="100" rx="20"/><rect x="755" y="300" width="110" height="100" rx="20"/><rect x="910" y="300" width="100" height="100" rx="20"/>
</g>
<rect x="600" y="300" width="410" height="100" rx="20" fill="{ac}" opacity=".18" filter="url(#g)"/>
<g stroke="#d0bfff" stroke-width="6" fill="none">
<path d="M655 295 L655 140"/><path d="M810 295 L810 140"/><path d="M960 295 L960 140"/>
</g>
<g stroke="{ac}" stroke-width="7" fill="none" marker-end="url(#m)">
<path d="M714 335 L748 335"/><path d="M751 365 L717 365"/><path d="M869 335 L903 335"/><path d="M906 365 L872 365"/>
</g>
<text x="810" y="500" text-anchor="middle" font-size="28" fill="#d0bfff">서로 메시지</text>'''
make('th_mon2','/home/claude/out2/mon/월_01_썸네일.png','#0f0a1f','#2a1f5a',ac,'서브에이전트 vs','Agent Teams','결과만 받는 구조와 같이 일하는 구조, 공식 문서로 비교',svg,fs=100)
