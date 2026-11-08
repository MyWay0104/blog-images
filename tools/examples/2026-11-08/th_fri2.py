from thumb import make
ac='#22b8cf'
# 핵심 질문: npx install X 오타가 왜 위험한가 / 분위기: 경고·확인 / 팔레트: 짙은 청록 배경 + 시안 / 중심 오브젝트: 명령 두 줄 — 위는 오타(install이 패키지 칸에 들어감), 아래는 의도한 명령(도구가 패키지 칸에)
mono="font-family=\"'DejaVu Sans Mono','Noto Sans Mono CJK KR',monospace\""
svg=f'''<defs><filter id="g" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="22"/></filter></defs>
<!-- 오타 명령 -->
<rect x="60" y="40" width="960" height="150" rx="26" fill="#0b2b33" stroke="#15606d" stroke-width="6"/>
<text x="110" y="135" font-size="62" font-weight="700" fill="#e3fafc" {mono}>npx</text>
<rect x="262" y="78" width="300" height="84" rx="16" fill="{ac}"/>
<text x="412" y="137" text-anchor="middle" font-size="58" font-weight="700" fill="#06252b" {mono}>install</text>
<rect x="586" y="78" width="260" height="84" rx="16" fill="#15606d"/>
<text x="716" y="137" text-anchor="middle" font-size="58" font-weight="700" fill="#e3fafc" {mono}>&lt;도구&gt;</text>
<text x="940" y="150" text-anchor="middle" font-size="84" font-weight="900" fill="#15606d">✕</text>
<text x="412" y="238" text-anchor="middle" font-size="30" font-weight="700" fill="#66d9e8">첫 단어 = 패키지 이름 → "install"이라는 다른 패키지</text>
<!-- 의도한 명령 -->
<rect x="60" y="300" width="960" height="150" rx="26" fill="{ac}" opacity=".18" filter="url(#g)"/>
<rect x="60" y="300" width="960" height="150" rx="26" fill="#0b2b33" stroke="{ac}" stroke-width="6"/>
<text x="110" y="395" font-size="62" font-weight="700" fill="#e3fafc" {mono}>npx</text>
<rect x="262" y="338" width="260" height="84" rx="16" fill="{ac}"/>
<text x="392" y="397" text-anchor="middle" font-size="58" font-weight="700" fill="#06252b" {mono}>&lt;도구&gt;</text>
<rect x="546" y="338" width="300" height="84" rx="16" fill="#15606d"/>
<text x="696" y="397" text-anchor="middle" font-size="58" font-weight="700" fill="#e3fafc" {mono}>install</text>
<path d="M905 380 L935 410 L985 345" fill="none" stroke="{ac}" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/>
<text x="392" y="500" text-anchor="middle" font-size="30" font-weight="700" fill="#99e9f2">내가 쓰려던 도구에 install 하위 명령을 넘긴다</text>
<text x="540" y="568" text-anchor="middle" font-size="26" fill="#66d9e8">프록시를 통과했다 ≠ 안전하다 · 설치 전 읽기만 하는 확인 4가지</text>'''
make('th_fri2','/home/claude/out/fri/금_01_썸네일.png','#061a1f','#0b4a56',ac,'npx install 오타가','위험한 이유','첫 단어가 패키지 이름이 된다 · 설치 전 확인 4가지',svg,fs=96)
