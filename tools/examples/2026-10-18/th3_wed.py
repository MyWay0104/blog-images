from thumb import make
ac='#f783ac'
# 중심 오브젝트: 브라우저 주소창 하나. 그 아래 컨테이너 하나 안에 /api 와 dist 두 상자. 관계 = 둘이 하나의 주소로 합쳐짐
svg=f'''<defs><filter id="g" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="28"/></filter></defs>
<!-- 주소창 -->
<rect x="140" y="70" width="800" height="110" rx="55" fill="{ac}" opacity=".4" filter="url(#g)"/>
<rect x="140" y="70" width="800" height="110" rx="55" fill="#2a1020" stroke="{ac}" stroke-width="7"/>
<circle cx="215" cy="125" r="18" fill="none" stroke="{ac}" stroke-width="6"/><line x1="228" y1="138" x2="243" y2="153" stroke="{ac}" stroke-width="6" stroke-linecap="round"/>
<text x="280" y="142" font-size="46" font-weight="900" fill="#fff0f6" font-family="DejaVu Sans Mono">localhost:8000</text>
<text x="575" y="240" font-size="28" font-weight="700" fill="{ac}">브라우저가 보는 주소는 하나</text>
<!-- 컨테이너 -->
<rect x="200" y="280" width="680" height="240" rx="26" fill="none" stroke="{ac}" stroke-width="6" stroke-dasharray="22 14"/>
<text x="240" y="328" font-size="26" font-weight="900" fill="{ac}">uvicorn 1개</text>
<rect x="250" y="360" width="270" height="120" rx="18" fill="#3a1526" stroke="#8a4a68" stroke-width="4"/>
<text x="385" y="412" text-anchor="middle" font-size="34" font-weight="900" fill="#fff0f6" font-family="DejaVu Sans Mono">/api</text>
<text x="385" y="452" text-anchor="middle" font-size="24" fill="#e8b4c8">FastAPI → JSON</text>
<rect x="560" y="360" width="270" height="120" rx="18" fill="#3a1526" stroke="#8a4a68" stroke-width="4"/>
<text x="695" y="412" text-anchor="middle" font-size="34" font-weight="900" fill="#fff0f6" font-family="DejaVu Sans Mono">dist/</text>
<text x="695" y="452" text-anchor="middle" font-size="24" fill="#e8b4c8">정적 파일</text>
<!-- 연결선 -->
<path d="M540 180 L540 280" stroke="{ac}" stroke-width="7"/><polygon points="520,270 540,300 560,270" fill="{ac}"/>
<text x="540" y="572" text-anchor="middle" font-size="28" font-weight="700" fill="#e8b4c8">CORS 설정 없음 · 쿠키 문제 없음</text>'''
make('th3_wed','/home/claude/out3/wed/수_01_썸네일.png','#160810','#5a1a3a',ac,'폴더를 나눴더니','CORS가 난다?','FastAPI StaticFiles로 origin 하나로 끝내기',svg,fs=112)
