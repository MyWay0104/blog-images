from thumb import make
ac='#51cf66'
# 핵심 질문: Swagger UI와 OpenAPI는 뭐가 다른가 / 분위기: 비교·선택 / 팔레트: 짙은 초록 배경 + 연두 / 중심 오브젝트: 왼쪽 문서 한 장(명세)에서 화살표가 나가 오른쪽 화면(브라우저 창의 GET/POST 막대)으로 그려지는 모양
svg=f'''<defs><filter id="g" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="22"/></filter>
<marker id="m" markerUnits="userSpaceOnUse" markerWidth="26" markerHeight="26" refX="20" refY="13" orient="auto"><path d="M0,0 L26,13 L0,26 z" fill="{ac}"/></marker></defs>
<!-- document -->
<rect x="90" y="60" width="300" height="400" rx="18" fill="{ac}" opacity=".22" filter="url(#g)"/>
<path d="M90 60 H330 L390 120 V460 H90 Z" fill="#0d2a16" stroke="{ac}" stroke-width="7" stroke-linejoin="round"/>
<path d="M330 60 V120 H390" fill="none" stroke="{ac}" stroke-width="7" stroke-linejoin="round"/>
<g stroke="#2b6b3a" stroke-width="8" stroke-linecap="round"><path d="M130 170 L300 170"/><path d="M130 215 L340 215"/><path d="M130 260 L260 260"/><path d="M130 305 L340 305"/><path d="M130 350 L300 350"/><path d="M130 395 L220 395"/></g>
<text x="240" y="520" text-anchor="middle" font-size="30" font-weight="900" fill="{ac}">OpenAPI 명세</text>
<text x="240" y="556" text-anchor="middle" font-size="22" fill="#b2f2bb">문서 한 장 (json / yaml)</text>
<!-- arrow -->
<path d="M420 260 L560 260" stroke="{ac}" stroke-width="12" stroke-linecap="round" marker-end="url(#m)"/>
<!-- browser window -->
<rect x="600" y="60" width="400" height="400" rx="20" fill="#0d2a16" stroke="{ac}" stroke-width="7"/>
<rect x="600" y="60" width="400" height="56" rx="20" fill="#163a22"/>
<circle cx="630" cy="88" r="9" fill="#ff5f57"/><circle cx="658" cy="88" r="9" fill="#febc2e"/><circle cx="686" cy="88" r="9" fill="#28c840"/>
<g font-size="22" font-weight="900">
<rect x="630" y="150" width="340" height="56" rx="10" fill="#2b6b3a"/><text x="650" y="187" fill="#fff">GET</text><text x="730" y="187" fill="#e6fcf5" font-weight="500">/notes</text>
<rect x="630" y="226" width="340" height="56" rx="10" fill="#3f9a4f"/><text x="650" y="263" fill="#fff">POST</text><text x="730" y="263" fill="#e6fcf5" font-weight="500">/notes</text>
<rect x="630" y="302" width="340" height="56" rx="10" fill="#2b6b3a"/><text x="650" y="339" fill="#fff">GET</text><text x="730" y="339" fill="#e6fcf5" font-weight="500">/notes/{{id}}</text>
</g>
<rect x="800" y="390" width="150" height="44" rx="8" fill="none" stroke="#b2f2bb" stroke-width="4"/><text x="875" y="420" text-anchor="middle" font-size="20" font-weight="700" fill="#b2f2bb">Try it out</text>
<text x="800" y="520" text-anchor="middle" font-size="30" font-weight="900" fill="{ac}">Swagger UI</text>
<text x="800" y="556" text-anchor="middle" font-size="22" fill="#b2f2bb">그 문서를 읽어 그린 화면</text>'''
make('th_thu2','/home/claude/out/thu/목_01_썸네일.png','#06180c','#1b5e2f',ac,'Swagger UI vs','OpenAPI, 뭐가 달라?','문서 화면과 명세는 다른 것, 공식 문서와 실제 렌더링으로',svg,fs=96)
