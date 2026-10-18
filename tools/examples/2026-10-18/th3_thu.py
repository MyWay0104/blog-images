from thumb import make
ac='#4dabf7'
# 중심 오브젝트: 왼쪽 주소록 카드(DB, key 한 줄), 오른쪽 상자(스토리지, 물건). 관계 = 카드의 key가 상자를 가리킴
svg=f'''<defs><filter id="g" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="28"/></filter>
<linearGradient id="bx" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{ac}"/><stop offset="1" stop-color="#1e3a5c"/></linearGradient></defs>
<!-- 주소록 카드 -->
<rect x="90" y="110" width="400" height="300" rx="20" fill="#0f2036" stroke="{ac}" stroke-width="6"/>
<rect x="90" y="110" width="400" height="58" rx="20" fill="#1e3a5c"/>
<text x="120" y="150" font-size="28" font-weight="900" fill="#eaf4ff">MongoDB · 주소록</text>
<rect x="125" y="200" width="200" height="16" rx="8" fill="#2d5680"/><rect x="125" y="240" width="260" height="16" rx="8" fill="#2d5680"/>
<rect x="125" y="290" width="330" height="60" rx="12" fill="#07111f" stroke="{ac}" stroke-width="3"/>
<text x="140" y="330" font-size="24" font-weight="700" fill="{ac}" font-family="DejaVu Sans Mono">cover_key: "covers/…"</text>
<text x="290" y="465" text-anchor="middle" font-size="28" font-weight="700" fill="#9cc7ee">위치와 상태만 적는다</text>
<!-- 화살표 -->
<path d="M460 320 C 560 320, 600 300, 680 300" fill="none" stroke="{ac}" stroke-width="9" stroke-linecap="round"/><polygon points="675,275 725,300 675,325" fill="{ac}"/>
<!-- 상자 (스토리지) -->
<rect x="740" y="200" width="250" height="210" rx="18" fill="{ac}" opacity=".35" filter="url(#g)"/>
<polygon points="740,250 865,200 990,250 990,410 865,460 740,410" fill="url(#bx)"/>
<polygon points="740,250 865,300 990,250 865,200" fill="#9cc7ee"/>
<line x1="865" y1="300" x2="865" y2="460" stroke="#0f2036" stroke-width="4"/>
<text x="865" y="520" text-anchor="middle" font-size="28" font-weight="700" fill="{ac}">스토리지 · 물건(bytes)</text>'''
make('th3_thu','/home/claude/out3/thu/목_01_썸네일.png','#050d18','#163a66',ac,'MongoDB는','스토리지가 아니다','DB에는 주소록, 객체 스토리지에는 물건',svg,fs=112)
