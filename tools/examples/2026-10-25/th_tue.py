from thumb import make
ac='#51cf66'
# 핵심 질문: LLM은 브라우저를 어떻게 보는가 / 분위기: 구조·원리 / 팔레트: 짙은 녹색 배경 + 연두 / 중심 오브젝트: 브라우저 창 하나가 오른쪽의 텍스트 트리로 변환되는 모습 (화면→트리)
svg=f'''<defs><filter id="g" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="26"/></filter></defs>
<!-- 브라우저 창 -->
<rect x="70" y="60" width="430" height="470" rx="24" fill="#0d2a17" stroke="#1f5a33" stroke-width="5"/>
<rect x="70" y="60" width="430" height="54" rx="24" fill="#13331f"/><circle cx="104" cy="87" r="9" fill="#1f5a33"/><circle cx="134" cy="87" r="9" fill="#1f5a33"/><circle cx="164" cy="87" r="9" fill="#1f5a33"/>
<rect x="110" y="150" width="240" height="30" rx="8" fill="#2a6b3f"/>
<rect x="110" y="215" width="300" height="56" rx="12" fill="#0a1f11" stroke="#2a6b3f" stroke-width="4"/><rect x="420" y="215" width="60" height="56" rx="12" fill="#2a6b3f"/>
<rect x="110" y="310" width="350" height="20" rx="8" fill="#1f5a33"/><rect x="110" y="350" width="280" height="20" rx="8" fill="#1f5a33"/><rect x="110" y="390" width="320" height="20" rx="8" fill="#1f5a33"/>
<rect x="110" y="450" width="200" height="20" rx="8" fill="#1f5a33"/>
<text x="285" y="575" text-anchor="middle" font-size="30" font-weight="700" fill="#8fd9a0">화면 (픽셀)</text>
<!-- 변환 화살표 -->
<path d="M520 295 L600 295" stroke="{ac}" stroke-width="12" stroke-linecap="round"/><polygon points="596,268 650,295 596,322" fill="{ac}"/>
<!-- 텍스트 트리 -->
<rect x="670" y="60" width="350" height="470" rx="24" fill="{ac}" opacity=".25" filter="url(#g)"/>
<rect x="670" y="60" width="350" height="470" rx="24" fill="#0d2a17" stroke="{ac}" stroke-width="6"/>
<g font-family="DejaVu Sans Mono" font-size="27" fill="#eafbef">
<text x="700" y="140">- heading</text>
<text x="700" y="200">- <tspan fill="{ac}" font-weight="700">textbox</tspan></text>
<text x="730" y="245" font-size="23" fill="#8fd9a0">"도서 검색"</text>
<text x="730" y="290" font-size="23" fill="{ac}">[ref=e5]</text>
<text x="700" y="355">- button</text>
<text x="700" y="415">- list:</text>
<text x="730" y="470">- link</text>
</g>
<text x="845" y="575" text-anchor="middle" font-size="30" font-weight="700" fill="{ac}">접근성 트리 (텍스트)</text>'''
make('th_tue','/home/claude/out/tue/화_01_썸네일.png','#061a0d','#17502a',ac,'LLM은 화면을','보지 않는다','Playwright MCP가 읽는 건 DOM의 요약본, 접근성 트리',svg,fs=112)
