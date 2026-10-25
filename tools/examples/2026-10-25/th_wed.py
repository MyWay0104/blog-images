from thumb import make
ac='#ff6b6b'
# 핵심 질문: 같은 Playwright인데 왜 MCP로 크롤링하면 빠지나 / 분위기: 의문·빈틈 / 팔레트: 짙은 적갈색 배경 + 코랄 / 중심 오브젝트: 깔때기(요약) 위로 들어간 문서가 아래로는 일부만 나오고 옆으로 조각이 새는 모습
svg=f'''<defs><filter id="g" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="26"/></filter></defs>
<!-- 위: 원본 문서 -->
<rect x="330" y="40" width="420" height="150" rx="18" fill="#2a1010" stroke="#7a3030" stroke-width="5"/>
<rect x="360" y="70" width="300" height="16" rx="8" fill="#7a3030"/><rect x="360" y="100" width="360" height="16" rx="8" fill="#7a3030"/><rect x="360" y="130" width="240" height="16" rx="8" fill="#7a3030"/><rect x="360" y="160" width="330" height="16" rx="8" fill="#7a3030"/>
<text x="540" y="235" text-anchor="middle" font-size="30" font-weight="700" fill="#ffb3b3">원본 페이지</text>
<!-- 깔때기 -->
<path d="M250 260 L830 260 L600 420 L600 470 L480 470 L480 420 Z" fill="{ac}" opacity=".35" filter="url(#g)"/>
<path d="M250 260 L830 260 L600 420 L600 470 L480 470 L480 420 Z" fill="#2a1010" stroke="{ac}" stroke-width="7" stroke-linejoin="round"/>
<text x="540" y="350" text-anchor="middle" font-size="44" font-weight="900" fill="{ac}">요약</text>
<!-- 새는 조각들 -->
<g fill="#ffb3b3" opacity=".9">
<rect x="150" y="330" width="70" height="16" rx="8" transform="rotate(-20 185 338)"/>
<rect x="110" y="400" width="54" height="16" rx="8" transform="rotate(-35 137 408)"/>
<rect x="860" y="330" width="70" height="16" rx="8" transform="rotate(20 895 338)"/>
<rect x="900" y="400" width="54" height="16" rx="8" transform="rotate(35 927 408)"/>
</g>
<text x="120" y="470" font-size="26" font-weight="700" fill="#ffb3b3">data-* 속성</text>
<text x="820" y="470" font-size="26" font-weight="700" fill="#ffb3b3">접힌 내용</text>
<!-- 아래: 요약본 -->
<rect x="420" y="490" width="240" height="90" rx="14" fill="#2a1010" stroke="{ac}" stroke-width="5"/>
<rect x="445" y="515" width="150" height="14" rx="7" fill="{ac}"/><rect x="445" y="545" width="100" height="14" rx="7" fill="{ac}" opacity=".6"/>
<text x="700" y="545" font-size="28" font-weight="700" fill="{ac}">LLM이 받는 것</text>'''
make('th_wed','/home/claude/out/wed/수_01_썸네일.png','#1a0808','#5a1c1c',ac,'MCP로 크롤링','뭐가 빠질까?','Playwright MCP vs 라이브러리, 결과를 누가 받느냐',svg,fs=112)
