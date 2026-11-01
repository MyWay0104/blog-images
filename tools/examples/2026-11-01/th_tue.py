from thumb import make
ac='#a9e34b'
# 핵심 질문: 외부 연결이 막혔을 때 글꼴을 어떻게 넣나 / 분위기: 설치·따라하기 / 팔레트: 짙은 올리브 배경 + 라임 / 중심 오브젝트: 글자 "Aa" 카드 하나가 구름(CDN)에서 오는 길은 끊겨 있고, 내 서버 폴더에서 오는 길은 연결됨
svg=f'''<defs><filter id="g" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="26"/></filter></defs>
<!-- 구름(CDN) -->
<g fill="#2a3a12" stroke="#4a6a22" stroke-width="5">
<ellipse cx="230" cy="150" rx="150" ry="70"/><circle cx="170" cy="120" r="55"/><circle cx="260" cy="100" r="70"/><circle cx="330" cy="140" r="50"/>
</g>
<text x="235" y="165" text-anchor="middle" font-size="32" font-weight="700" fill="#8aa36a">CDN</text>
<!-- 끊긴 선 -->
<path d="M380 180 L520 290" stroke="#6a7a4a" stroke-width="10" stroke-dasharray="22 16" stroke-linecap="round"/>
<g stroke="#ff8787" stroke-width="12" stroke-linecap="round"><path d="M430 200 L480 260"/><path d="M480 200 L430 260"/></g>
<!-- 내 서버 폴더 -->
<path d="M90 400 L90 560 L370 560 L370 430 L230 430 L205 400 Z" fill="#1e2a0c" stroke="{ac}" stroke-width="6" stroke-linejoin="round"/>
<text x="230" y="510" text-anchor="middle" font-size="30" font-weight="700" fill="{ac}" font-family="DejaVu Sans Mono">./fonts/</text>
<!-- 연결선 -->
<path d="M375 480 C 460 480, 480 360, 560 345" stroke="{ac}" stroke-width="12" fill="none" stroke-linecap="round"/>
<polygon points="545,322 600,340 552,372" fill="{ac}"/>
<!-- Aa 카드 -->
<rect x="620" y="150" width="380" height="380" rx="34" fill="{ac}" opacity=".3" filter="url(#g)"/>
<rect x="620" y="150" width="380" height="380" rx="34" fill="#1e2a0c" stroke="{ac}" stroke-width="7"/>
<text x="810" y="400" text-anchor="middle" font-size="230" font-weight="900" fill="{ac}" font-family="Poppins">Aa</text>
<text x="810" y="490" text-anchor="middle" font-size="30" font-weight="700" fill="#dcebc0">@font-face</text>'''
make('th_tue','/home/claude/out/tue/화_01_썸네일.png','#121a05','#3a5a14',ac,'CDN이 막혔는데','글꼴은 어떻게?','Google Fonts를 내 서버에서 @font-face로 직접 호스팅',svg,fs=112)
