from thumb import make
ac='#2dd4bf'
# 중심 오브젝트: 종이 문서 한 장(디스크 파일)은 그대로, 오른쪽 화면(DOM)은 빛나며 바뀌는 모습. 관계 = 복사 1회 → 화면 갱신 반복
svg=f'''<defs><filter id="g" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="28"/></filter>
<linearGradient id="scr" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{ac}" stop-opacity=".55"/><stop offset="1" stop-color="{ac}" stop-opacity=".12"/></linearGradient></defs>
<!-- 왼쪽: 디스크의 파일 (변하지 않음) -->
<rect x="120" y="110" width="250" height="330" rx="16" fill="#102830" stroke="#2a6a78" stroke-width="5"/>
<polygon points="300,110 370,180 300,180" fill="#1d4650"/>
<rect x="160" y="210" width="150" height="14" rx="7" fill="#2a6a78"/><rect x="160" y="250" width="110" height="14" rx="7" fill="#2a6a78"/><rect x="160" y="290" width="170" height="14" rx="7" fill="#2a6a78"/><rect x="160" y="330" width="90" height="14" rx="7" fill="#2a6a78"/>
<text x="245" y="490" text-anchor="middle" font-size="30" font-weight="700" fill="#9fd9d0">index.html · 그대로</text>
<!-- 가운데 화살표: 한 번 복사 -->
<path d="M400 275 L600 275" stroke="{ac}" stroke-width="10" stroke-linecap="round"/><polygon points="600,250 650,275 600,300" fill="{ac}"/>
<text x="520" y="245" text-anchor="middle" font-size="26" font-weight="700" fill="{ac}">한 번 복사</text>
<!-- 오른쪽: 브라우저 화면 (빛나며 바뀜) -->
<rect x="690" y="90" width="290" height="370" rx="22" fill="{ac}" opacity=".35" filter="url(#g)"/>
<rect x="690" y="90" width="290" height="370" rx="22" fill="#0b1a1f" stroke="{ac}" stroke-width="6"/>
<rect x="690" y="90" width="290" height="60" rx="22" fill="#163a44"/><circle cx="725" cy="120" r="8" fill="{ac}"/><circle cx="752" cy="120" r="8" fill="#2a6a78"/><circle cx="779" cy="120" r="8" fill="#2a6a78"/>
<rect x="720" y="180" width="230" height="70" rx="12" fill="url(#scr)"/>
<rect x="720" y="270" width="230" height="70" rx="12" fill="url(#scr)" opacity=".7"/>
<rect x="720" y="360" width="150" height="70" rx="12" fill="url(#scr)" opacity=".45"/>
<text x="940" y="135" text-anchor="middle" font-size="40" font-weight="900" fill="{ac}">↻</text>
<text x="835" y="520" text-anchor="middle" font-size="30" font-weight="700" fill="{ac}">화면(DOM) · 계속 바뀜</text>'''
make('th3_mon','/home/claude/out3/mon/월_01_썸네일.png','#06161b','#124a4a',ac,'정적 웹인데','SPA라고?','Vite+React vs Next.js, HTML이 두 개라는 것',svg,fs=118)
