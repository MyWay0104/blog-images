from thumb import make
ac='#fab005'
# 핵심 질문: 어떤 환경변수에 NEXT_PUBLIC_을 붙이고 어떤 값은 절대 붙이면 안 되나 / 분위기: 의문·빈틈(보안 경계) / 팔레트: 짙은 갈색 검정 + 앰버 / 중심 오브젝트: 서버 금고에서 브라우저로 나가는 문, 접두사 붙은 값만 문을 통과
mono="font-family=\"'DejaVu Sans Mono','Noto Sans Mono CJK KR',monospace\""
svg=f'''<defs><filter id="g" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="24"/></filter>
<linearGradient id="p" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3a2b0a"/><stop offset="1" stop-color="#241a05"/></linearGradient></defs>
<!-- 서버 금고 -->
<rect x="60" y="60" width="440" height="430" rx="26" fill="url(#p)" stroke="#6b5012" stroke-width="6"/>
<text x="100" y="118" font-size="30" font-weight="700" fill="#ffd43b">서버</text>
<rect x="100" y="150" width="360" height="60" rx="12" fill="#1c1403" stroke="#6b5012" stroke-width="4"/>
<text x="120" y="190" font-size="26" fill="#bfa65a" {mono}>NOTION_TOKEN</text>
<rect x="100" y="230" width="360" height="60" rx="12" fill="#1c1403" stroke="#6b5012" stroke-width="4"/>
<text x="120" y="270" font-size="26" fill="#bfa65a" {mono}>REVALIDATE_SECRET</text>
<rect x="100" y="330" width="360" height="60" rx="12" fill="#1c1403" stroke="{ac}" stroke-width="5"/>
<text x="120" y="370" font-size="24" font-weight="700" fill="{ac}" {mono}>NEXT_PUBLIC_SITE_URL</text>
<!-- 문(경계) -->
<rect x="520" y="40" width="14" height="470" rx="7" fill="{ac}" opacity=".9"/>
<rect x="500" y="40" width="54" height="470" rx="20" fill="{ac}" opacity=".35" filter="url(#g)"/>
<!-- 브라우저 -->
<rect x="590" y="60" width="430" height="430" rx="26" fill="none" stroke="{ac}" stroke-width="6"/>
<text x="630" y="118" font-size="30" font-weight="700" fill="#fff">브라우저</text>
<rect x="630" y="330" width="350" height="60" rx="12" fill="{ac}"/>
<text x="650" y="370" font-size="24" font-weight="700" fill="#1c1403" {mono}>"https://…"</text>
<path d="M466 360 H 622" stroke="{ac}" stroke-width="10" stroke-linecap="round"/>
<path d="M600 338 L 628 360 L 600 382" fill="none" stroke="{ac}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>
<text x="805" y="200" text-anchor="middle" font-size="26" fill="#8a7a3a">토큰은 여기 없다</text>
<text x="805" y="240" text-anchor="middle" font-size="22" fill="#8a7a3a">(번들에 실리지 않음)</text>
<text x="540" y="565" text-anchor="middle" font-size="26" fill="#ffe066">접두사가 붙은 값만 빌드 때 번들에 박혀 문을 넘는다</text>'''
make('th_tue3','/home/claude/out/tue/화_01_썸네일.png','#1c1403','#4a3608',ac,'NEXT_PUBLIC_을','어디에 붙여야 할까','브라우저에 노출되는 값과 서버에만 두는 값의 경계',svg,fs=92)
