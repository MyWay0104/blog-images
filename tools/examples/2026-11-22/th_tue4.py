from thumb import make
ac='#9775fa'
# 핵심 질문: 같은 "임베딩"이라는 말이 가리키는 두 가지(토큰 임베딩, RAG 임베딩)는 무엇이 다른가 / 분위기: 비교·선택 / 팔레트: 짙은 남보라 + 바이올렛 / 중심 오브젝트: 한 문장에서 갈라지는 두 결과 — 왼쪽은 토큰마다 하나씩 쌓인 막대 여러 개, 오른쪽은 빛나는 점 하나
svg=f'''<defs><filter id="g" x="-80%" y="-80%" width="260%" height="260%"><feGaussianBlur stdDeviation="20"/></filter>
<linearGradient id="b" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#5f3dc4"/><stop offset="1" stop-color="#b197fc"/></linearGradient></defs>
<!-- 위: 문장 한 줄 -->
<rect x="330" y="20" width="420" height="78" rx="22" fill="#1e1440" stroke="{ac}" stroke-width="6"/>
<text x="540" y="72" text-anchor="middle" font-size="38" font-weight="900" fill="#fff">같은 문장 하나</text>
<path d="M440 100 C 440 150, 300 150, 290 196" stroke="#b197fc" stroke-width="7" fill="none"/>
<path d="M640 100 C 640 150, 790 150, 800 196" stroke="{ac}" stroke-width="7" fill="none"/>
<!-- 왼쪽: 토큰마다 벡터 (막대 5줄) -->
<rect x="70" y="200" width="430" height="290" rx="26" fill="#170f33" stroke="#3d2b7a" stroke-width="6"/>
<rect x="110" y="236" width="350" height="30" rx="10" fill="url(#b)"/>
<rect x="110" y="284" width="350" height="30" rx="10" fill="url(#b)" opacity=".85"/>
<rect x="110" y="332" width="350" height="30" rx="10" fill="url(#b)" opacity=".7"/>
<rect x="110" y="380" width="350" height="30" rx="10" fill="url(#b)" opacity=".55"/>
<rect x="110" y="428" width="350" height="30" rx="10" fill="url(#b)" opacity=".4"/>
<text x="285" y="546" text-anchor="middle" font-size="36" font-weight="900" fill="#d0bfff">토큰마다 1개</text>
<!-- 오른쪽: 문장에 벡터 1개 (점 하나) -->
<rect x="580" y="200" width="430" height="290" rx="26" fill="#170f33" stroke="{ac}" stroke-width="6"/>
<circle cx="795" cy="345" r="74" fill="{ac}" opacity=".45" filter="url(#g)"/>
<circle cx="795" cy="345" r="46" fill="{ac}"/>
<circle cx="795" cy="345" r="18" fill="#fff"/>
<text x="795" y="546" text-anchor="middle" font-size="36" font-weight="900" fill="#fff">문장에 1개</text>'''
make('th_tue4','/home/claude/out/tue/화_01_썸네일.png','#120b24','#3b2a7a',ac,'둘 다 임베딩인데','뭐가 다를까?','토큰 임베딩과 RAG 임베딩을 가르는 기준',svg,fs=104)
