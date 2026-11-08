from thumb import make
ac='#ff6b6b'
# 핵심 질문: 남의 에이전트를 붙일 때 MCP인가 A2A인가 / 분위기: 비교·선택 / 팔레트: 짙은 적갈색 배경 + 코랄 / 중심 오브젝트: 가운데 에이전트 원 하나, 아래로 꽂힌 도구(세로, MCP), 옆으로 이어진 다른 에이전트 원(가로, A2A)
svg=f'''<defs><filter id="g" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="24"/></filter>
<marker id="m" markerUnits="userSpaceOnUse" markerWidth="26" markerHeight="26" refX="20" refY="13" orient="auto"><path d="M0,0 L26,13 L0,26 z" fill="{ac}"/></marker></defs>
<!-- my agent -->
<circle cx="330" cy="180" r="120" fill="{ac}" opacity=".28" filter="url(#g)"/>
<circle cx="330" cy="180" r="120" fill="#3d1212" stroke="{ac}" stroke-width="7"/>
<text x="330" y="170" text-anchor="middle" font-size="34" font-weight="900" fill="#fff">내</text>
<text x="330" y="216" text-anchor="middle" font-size="34" font-weight="900" fill="#fff">에이전트</text>
<!-- vertical: MCP tools -->
<path d="M330 305 L330 380" stroke="{ac}" stroke-width="10" marker-end="url(#m)"/>
<g fill="#2f0d0d" stroke="#ff8787" stroke-width="5">
<rect x="180" y="392" width="90" height="70" rx="14"/><rect x="285" y="392" width="90" height="70" rx="14"/><rect x="390" y="392" width="90" height="70" rx="14"/>
</g>
<text x="330" y="505" text-anchor="middle" font-size="28" font-weight="900" fill="{ac}">MCP</text>
<text x="330" y="538" text-anchor="middle" font-size="22" fill="#ffc9c9">도구를 꽂는다 (세로)</text>
<!-- horizontal: A2A other agent -->
<path d="M455 180 L640 180" stroke="{ac}" stroke-width="10" marker-end="url(#m)"/>
<path d="M640 220 L455 220" stroke="{ac}" stroke-width="10" marker-end="url(#m)"/>
<circle cx="790" cy="200" r="120" fill="#2f0d0d" stroke="#ff8787" stroke-width="7" stroke-dasharray="18 12"/>
<text x="790" y="190" text-anchor="middle" font-size="34" font-weight="900" fill="#ffc9c9">남의</text>
<text x="790" y="236" text-anchor="middle" font-size="34" font-weight="900" fill="#ffc9c9">에이전트</text>
<text x="548" y="280" text-anchor="middle" font-size="28" font-weight="900" fill="{ac}">A2A</text>
<text x="790" y="380" text-anchor="middle" font-size="22" fill="#ffc9c9">속은 안 보인다 (가로)</text>'''
make('th_wed2','/home/claude/out/wed/수_01_썸네일.png','#1f0808','#5a1a1a',ac,'MCP vs A2A','뭐가 다를까?','도구를 붙이는 것과 에이전트를 붙이는 것, 공식 문서로 비교',svg,fs=104)
