from thumb import make
ac='#f06595'
# 핵심 질문: 평가 항목을 규칙(코드)에 맡길지 LLM 판정에 맡길지 어떻게 가르나 / 분위기: 비교·선택 / 팔레트: 짙은 와인 + 핑크 / 중심 오브젝트: 저울 — 한쪽은 자(규칙), 한쪽은 말풍선(LLM 판정), 받침에 질문
mono="font-family=\"'DejaVu Sans Mono','Noto Sans Mono CJK KR',monospace\""
svg=f'''<defs><filter id="g" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="22"/></filter>
<linearGradient id="p" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#4a1630"/><stop offset="1" stop-color="#2a0c1b"/></linearGradient></defs>
<g transform="translate(0,-55)">
<!-- 저울 기둥 -->
<rect x="530" y="150" width="20" height="300" rx="10" fill="#6b2140"/>
<path d="M400 450 H680 L650 490 H430 Z" fill="#6b2140"/>
<rect x="150" y="140" width="780" height="18" rx="9" fill="{ac}"/>
<circle cx="540" cy="149" r="22" fill="{ac}"/>
<!-- 왼쪽 접시: 규칙 -->
<path d="M190 158 L170 300" stroke="#ff8fab" stroke-width="5"/><path d="M190 158 L330 300" stroke="#ff8fab" stroke-width="5"/>
<rect x="110" y="300" width="300" height="110" rx="22" fill="url(#p)" stroke="{ac}" stroke-width="5"/>
<text x="260" y="346" text-anchor="middle" font-size="30" font-weight="700" fill="#fff">규칙 (코드)</text>
<text x="260" y="390" text-anchor="middle" font-size="24" fill="#ffb3c6" {mono}>1 &lt;= x &lt;= 100</text>
<!-- 오른쪽 접시: LLM 판정 -->
<path d="M890 158 L750 300" stroke="#ff8fab" stroke-width="5"/><path d="M890 158 L1010 300" stroke="#ff8fab" stroke-width="5"/>
<rect x="670" y="300" width="340" height="110" rx="22" fill="url(#p)" stroke="#ff8fab" stroke-width="5"/>
<text x="840" y="346" text-anchor="middle" font-size="30" font-weight="700" fill="#fff">LLM 판정기</text>
<text x="840" y="390" text-anchor="middle" font-size="24" fill="#ffb3c6">"도움이 되는가?" 채점 기준</text>
<!-- 받침 질문 -->
<rect x="250" y="500" width="580" height="60" rx="18" fill="{ac}" opacity=".35" filter="url(#g)"/>
<rect x="250" y="500" width="580" height="60" rx="18" fill="{ac}"/>
<text x="540" y="541" text-anchor="middle" font-size="28" font-weight="700" fill="#1f0812">코드로 판정할 수 있는가?</text>
</g>'''
make('th_thu3','/home/claude/out/thu/목_01_썸네일.png','#1f0812','#4a1630',ac,'LLM-as-a-Judge','언제 써야 할까','규칙 기반 평가와 LLM 판정을 가르는 기준 하나',svg,fs=92)
