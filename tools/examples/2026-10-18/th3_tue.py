from thumb import make
ac='#ff922b'
# 중심 오브젝트: 터미널 창 하나. build 줄 뒤에는 폴더(.next/)만, dev 줄 뒤에는 빛나는 화면. 관계 = 갈림
svg=f'''<defs><filter id="g" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="26"/></filter></defs>
<!-- 터미널 창 -->
<rect x="90" y="80" width="560" height="400" rx="22" fill="#2a1a0a" stroke="#6b4420" stroke-width="5"/>
<rect x="90" y="80" width="560" height="56" rx="22" fill="#3a2410"/><circle cx="125" cy="108" r="9" fill="{ac}"/><circle cx="155" cy="108" r="9" fill="#6b4420"/><circle cx="185" cy="108" r="9" fill="#6b4420"/>
<text x="130" y="210" font-size="40" font-weight="700" fill="#e3c3a0" font-family="DejaVu Sans Mono">$ npm run build</text>
<text x="130" y="265" font-size="30" fill="#8a6a4a" font-family="DejaVu Sans Mono">… (아무것도 안 뜸)</text>
<text x="130" y="360" font-size="40" font-weight="700" fill="{ac}" font-family="DejaVu Sans Mono">$ npm run dev</text>
<text x="130" y="415" font-size="30" fill="{ac}" font-family="DejaVu Sans Mono">▸ http://localhost:3000</text>
<!-- build → 폴더 -->
<path d="M650 230 L760 230" stroke="#8a6a4a" stroke-width="8" stroke-linecap="round"/><polygon points="760,210 800,230 760,250" fill="#8a6a4a"/>
<rect x="820" y="170" width="190" height="130" rx="16" fill="none" stroke="#8a6a4a" stroke-width="6" stroke-dasharray="18 12"/>
<text x="915" y="247" text-anchor="middle" font-size="34" font-weight="900" fill="#d9a46b" font-family="DejaVu Sans Mono">.next/</text>
<!-- dev → 화면 -->
<path d="M650 390 L760 390" stroke="{ac}" stroke-width="8" stroke-linecap="round"/><polygon points="760,370 800,390 760,410" fill="{ac}"/>
<rect x="820" y="330" width="190" height="130" rx="16" fill="{ac}" opacity=".45" filter="url(#g)"/>
<rect x="820" y="330" width="190" height="130" rx="16" fill="#3a2410" stroke="{ac}" stroke-width="6"/>
<rect x="845" y="360" width="140" height="14" rx="7" fill="{ac}"/><rect x="845" y="390" width="100" height="14" rx="7" fill="{ac}" opacity=".7"/><rect x="845" y="420" width="120" height="14" rx="7" fill="{ac}" opacity=".45"/>
<text x="915" y="520" text-anchor="middle" font-size="28" font-weight="700" fill="{ac}">화면이 뜬다</text>
<text x="915" y="140" text-anchor="middle" font-size="28" font-weight="700" fill="#d9a46b">폴더만 생긴다</text>'''
make('th3_tue','/home/claude/out3/tue/화_01_썸네일.png','#160d04','#5a3010',ac,'npm run build','왜 안 뜨지?','Streamlit 사용자가 Next.js에서 헷갈린 dev와 build',svg,fs=112)
