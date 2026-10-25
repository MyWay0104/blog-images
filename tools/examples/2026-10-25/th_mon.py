from thumb import make
ac='#9775fa'
# 핵심 질문: fork와 clone은 뭐가 다른가 / 분위기: 비교·선택 / 팔레트: 짙은 보라 배경 + 라벤더 보라 / 중심 오브젝트: 저장소 상자 하나에서 두 갈래(옆 상자=fork, 아래 노트북=clone)
svg=f'''<defs><filter id="g" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="28"/></filter>
<linearGradient id="lg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{ac}" stop-opacity=".9"/><stop offset="1" stop-color="{ac}" stop-opacity=".35"/></linearGradient></defs>
<!-- 서버 구역 -->
<rect x="70" y="40" width="940" height="250" rx="34" fill="none" stroke="#4b3a86" stroke-width="5" stroke-dasharray="22 14"/>
<text x="110" y="92" font-size="30" font-weight="700" fill="#9a8bd0">GitHub 서버</text>
<!-- 원본 저장소 -->
<rect x="130" y="110" width="300" height="150" rx="24" fill="#1c1238" stroke="#6f5bb5" stroke-width="5"/>
<circle cx="180" cy="150" r="12" fill="#6f5bb5"/><rect x="205" y="140" width="180" height="20" rx="10" fill="#6f5bb5"/>
<rect x="160" y="190" width="240" height="18" rx="9" fill="#4b3a86"/><rect x="160" y="222" width="160" height="18" rx="9" fill="#4b3a86"/>
<!-- fork 화살표 -->
<path d="M450 185 L600 185" stroke="{ac}" stroke-width="12" stroke-linecap="round"/><polygon points="596,160 650,185 596,210" fill="{ac}"/>
<text x="470" y="160" font-size="40" font-weight="900" fill="{ac}">fork</text>
<!-- 내 fork 저장소 -->
<rect x="660" y="110" width="300" height="150" rx="24" fill="{ac}" opacity=".35" filter="url(#g)"/>
<rect x="660" y="110" width="300" height="150" rx="24" fill="#1c1238" stroke="{ac}" stroke-width="6"/>
<circle cx="710" cy="150" r="12" fill="{ac}"/><rect x="735" y="140" width="180" height="20" rx="10" fill="{ac}"/>
<rect x="690" y="190" width="240" height="18" rx="9" fill="#6f5bb5"/><rect x="690" y="222" width="160" height="18" rx="9" fill="#6f5bb5"/>
<!-- clone 화살표 -->
<path d="M810 300 L810 400" stroke="{ac}" stroke-width="12" stroke-linecap="round"/><polygon points="785,396 810,450 835,396" fill="{ac}"/>
<text x="840" y="370" font-size="40" font-weight="900" fill="{ac}">clone</text>
<!-- 노트북 -->
<rect x="640" y="440" width="340" height="110" rx="18" fill="url(#lg)" filter="url(#g)" opacity=".7"/>
<rect x="660" y="455" width="300" height="95" rx="14" fill="#1c1238" stroke="{ac}" stroke-width="6"/>
<rect x="600" y="550" width="420" height="22" rx="8" fill="{ac}"/>
<text x="810" y="520" text-anchor="middle" font-size="34" font-weight="700" fill="#f3f0ff">내 PC</text>'''
make('th_mon','/home/claude/out/mon/월_01_썸네일.png','#0f0a1e','#3a2a6e',ac,'fork랑 clone','뭐가 다르지?','서버 안의 복사 vs 내 PC로의 복사',svg,fs=118)
