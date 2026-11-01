from thumb import make
ac='#e64980'
# 핵심 질문: 여러 모델 앞에 두는 두 도구가 뭐가 다른가 / 분위기: 개념 구분 / 팔레트: 짙은 자주 배경 + 마젠타 / 중심 오브젝트: 왼쪽 "내 앱" 상자 안에 LangChain 칩, 가운데 앱 밖에 선 LiteLLM 게이트웨이 상자, 오른쪽 모델 제공사 원 세 개
svg=f'''<defs><filter id="g" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="26"/></filter></defs>
<!-- 내 앱 상자 -->
<rect x="70" y="120" width="330" height="360" rx="30" fill="#2b0d1c" stroke="#7a3a58" stroke-width="6" stroke-dasharray="20 14"/>
<text x="235" y="180" text-anchor="middle" font-size="30" font-weight="700" fill="#f3b5cc">내 앱 (안)</text>
<rect x="110" y="230" width="250" height="110" rx="22" fill="{ac}" opacity=".25" filter="url(#g)"/>
<rect x="110" y="230" width="250" height="110" rx="22" fill="#3a1226" stroke="{ac}" stroke-width="6"/>
<text x="235" y="300" text-anchor="middle" font-size="40" font-weight="900" fill="#fff">LangChain</text>
<text x="235" y="420" text-anchor="middle" font-size="24" fill="#c98ba8">라이브러리</text>
<!-- 화살표 -->
<path d="M405 300 L470 300" stroke="{ac}" stroke-width="12" stroke-linecap="round"/><polygon points="465,278 510,300 465,322" fill="{ac}"/>
<!-- 게이트웨이 -->
<rect x="520" y="200" width="280" height="200" rx="26" fill="{ac}" opacity=".25" filter="url(#g)"/>
<rect x="520" y="200" width="280" height="200" rx="26" fill="#3a1226" stroke="{ac}" stroke-width="7"/>
<text x="660" y="280" text-anchor="middle" font-size="40" font-weight="900" fill="#fff">LiteLLM</text>
<text x="660" y="330" text-anchor="middle" font-size="26" fill="#f3b5cc">게이트웨이 (밖)</text>
<text x="660" y="440" text-anchor="middle" font-size="24" fill="#c98ba8">별도 서버</text>
<!-- 제공사 원 -->
<g stroke="{ac}" stroke-width="6" fill="#2b0d1c">
<path d="M805 260 L880 180" stroke="#7a3a58" stroke-width="8" fill="none"/><path d="M805 300 L880 300" stroke="#7a3a58" stroke-width="8"/><path d="M805 340 L880 420" stroke="#7a3a58" stroke-width="8" fill="none"/>
<circle cx="940" cy="180" r="52"/><circle cx="940" cy="300" r="52"/><circle cx="940" cy="420" r="52"/>
</g>
<text x="940" y="192" text-anchor="middle" font-size="30" font-weight="900" fill="{ac}">A</text>
<text x="940" y="312" text-anchor="middle" font-size="30" font-weight="900" fill="{ac}">B</text>
<text x="940" y="432" text-anchor="middle" font-size="30" font-weight="900" fill="{ac}">C</text>'''
make('th_wed','/home/claude/out/wed/수_01_썸네일.png','#1c0612','#5a1a3a',ac,'LiteLLM vs LangChain','뭐가 다를까?','둘 다 여러 모델 앞의 중계 계층, 서 있는 자리가 다르다',svg,fs=92)
