from thumb import make
ac='#22b8cf'
# 핵심 질문: 모델 호출만 막으면 외부 전송이 끝인가 / 분위기: 디버깅·추적 / 팔레트: 짙은 청록 배경 + 시안 / 중심 오브젝트: 노트북에서 나가는 선 여러 가닥 — 굵은 하나는 안쪽 서버로, 가는 선들은 밖으로 새어 나감
svg=f'''<defs><filter id="g" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="26"/></filter></defs>
<!-- 울타리(내부 영역) -->
<rect x="60" y="40" width="600" height="520" rx="30" fill="none" stroke="#175a68" stroke-width="5" stroke-dasharray="22 14"/>
<text x="100" y="92" font-size="30" font-weight="700" fill="#5fc6d6">내부</text>
<!-- 노트북 -->
<rect x="120" y="230" width="260" height="160" rx="18" fill="#0a2a33" stroke="{ac}" stroke-width="6"/>
<rect x="90" y="392" width="320" height="22" rx="8" fill="{ac}"/>
<text x="250" y="320" text-anchor="middle" font-size="30" font-weight="700" fill="#e6fbff">Claude Code</text>
<!-- 내부 서버 -->
<rect x="440" y="130" width="190" height="110" rx="18" fill="#0a2a33" stroke="#5fc6d6" stroke-width="5"/>
<text x="535" y="178" text-anchor="middle" font-size="26" font-weight="700" fill="#e6fbff">자체 모델</text>
<text x="535" y="212" text-anchor="middle" font-size="22" fill="#9fe3ee">서버</text>
<path d="M385 290 C 420 290, 420 185, 435 185" stroke="#5fc6d6" stroke-width="14" fill="none" stroke-linecap="round"/>
<!-- 밖으로 새는 선들 -->
<g stroke="{ac}" stroke-width="7" fill="none" stroke-linecap="round" opacity=".95">
<path d="M385 310 C 560 310, 600 300, 760 300"/>
<path d="M385 330 C 560 340, 600 380, 760 380"/>
<path d="M385 350 C 560 370, 600 460, 760 460"/>
</g>
<g fill="{ac}"><polygon points="755,284 800,300 755,316"/><polygon points="755,364 800,380 755,396"/><polygon points="755,444 800,460 755,476"/></g>
<rect x="690" y="270" width="330" height="220" rx="24" fill="{ac}" opacity=".25" filter="url(#g)"/>
<g font-size="27" font-weight="700" fill="#e6fbff">
<text x="815" y="310">지표 · 설문</text>
<text x="815" y="390">WebFetch 검사</text>
<text x="815" y="470">도구 통신</text>
</g>
<text x="760" y="92" font-size="30" font-weight="700" fill="{ac}">외부</text>'''
make('th_thu','/home/claude/out/thu/목_01_썸네일.png','#041a1f','#0f4a56',ac,'모델은 내부인데','통신은 나간다?','Claude Code의 비모델 통신과 끄는 설정',svg,fs=112)
