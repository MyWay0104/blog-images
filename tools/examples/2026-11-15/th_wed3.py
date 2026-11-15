from thumb import make
ac='#5c7cfa'
# 핵심 질문: API 직접 호출·SDK·LangChain은 뭐가 다르고 뭐가 같은가 / 분위기: 구조·원리 / 팔레트: 남색 검정 + 인디고 / 중심 오브젝트: 세 층의 계단이 한 지점(같은 주소)으로 모이는 깔때기
mono="font-family=\"'DejaVu Sans Mono','Noto Sans Mono CJK KR',monospace\""
svg=f'''<defs><filter id="g" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="24"/></filter>
<linearGradient id="p" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1c2556"/><stop offset="1" stop-color="#101538"/></linearGradient></defs>
<!-- 세 층 -->
<rect x="80" y="40" width="920" height="90" rx="20" fill="url(#p)" stroke="#2b3670" stroke-width="5"/>
<text x="120" y="98" font-size="36" font-weight="700" fill="#dbe4ff">LangChain</text>
<text x="960" y="98" text-anchor="end" font-size="30" fill="#91a7ff" {mono}>llm.invoke(prompt)</text>
<rect x="150" y="160" width="780" height="90" rx="20" fill="url(#p)" stroke="#2b3670" stroke-width="5"/>
<text x="190" y="218" font-size="36" font-weight="700" fill="#dbe4ff">SDK</text>
<text x="890" y="218" text-anchor="end" font-size="30" fill="#91a7ff" {mono}>client.chat.completions</text>
<rect x="220" y="280" width="640" height="90" rx="20" fill="url(#p)" stroke="#2b3670" stroke-width="5"/>
<text x="260" y="338" font-size="36" font-weight="700" fill="#dbe4ff">requests</text>
<text x="820" y="338" text-anchor="end" font-size="30" fill="#91a7ff" {mono}>requests.post(url)</text>
<!-- 수렴 -->
<path d="M540 380 L540 432" stroke="{ac}" stroke-width="10" stroke-linecap="round"/>
<path d="M505 402 L540 437 L575 402" fill="none" stroke="{ac}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>
<rect x="190" y="452" width="700" height="78" rx="20" fill="{ac}" opacity=".3" filter="url(#g)"/>
<rect x="190" y="452" width="700" height="78" rx="20" fill="{ac}"/>
<text x="540" y="503" text-anchor="middle" font-size="30" font-weight="700" fill="#0b0f2a" {mono}>POST /v1/chat/completions</text>
<text x="540" y="572" text-anchor="middle" font-size="26" fill="#91a7ff">편해지는 만큼 안 보이게 된다 — 목적지는 하나</text>'''
make('th_wed3','/home/claude/out/wed/수_01_썸네일.png','#0b0f2a','#1c2a6e',ac,'API·SDK·LangChain','셋 다 같은 주소다','직접 호출과 SDK, LangChain의 차이는 숨기는 양이다',svg,fs=92)
