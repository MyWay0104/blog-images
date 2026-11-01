from thumb import make
ac='#fab005'
# 핵심 질문: 프로젝트 지침과 지식 파일에 각각 무엇을 넣나 / 분위기: 구조·원리 / 팔레트: 짙은 갈색 배경 + 골드 / 중심 오브젝트: 작은 메모 카드(지침) 하나가 두꺼운 문서 묶음(지식)을 가리키는 모양
svg=f'''<defs><filter id="g" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="24"/></filter></defs>
<!-- 지침 카드 (작게) -->
<rect x="90" y="190" width="300" height="200" rx="24" fill="{ac}" opacity=".3" filter="url(#g)"/>
<rect x="90" y="190" width="300" height="200" rx="24" fill="#2a1f00" stroke="{ac}" stroke-width="7"/>
<text x="240" y="265" text-anchor="middle" font-size="40" font-weight="900" fill="#fff">지침</text>
<g stroke="#6b5200" stroke-width="8" stroke-linecap="round"><path d="M140 310 L340 310"/><path d="M140 345 L280 345"/></g>
<text x="240" y="440" text-anchor="middle" font-size="26" fill="#d4b24c">짧게 · 어떻게</text>
<!-- 화살표 -->
<path d="M400 290 L520 290" stroke="{ac}" stroke-width="12" stroke-linecap="round"/><polygon points="515,266 565,290 515,314" fill="{ac}"/>
<!-- 문서 묶음 (크게) -->
<rect x="640" y="90" width="330" height="430" rx="22" fill="#3d2e00" stroke="#6b5200" stroke-width="6" transform="rotate(-6 805 305)"/>
<rect x="615" y="100" width="330" height="430" rx="22" fill="#2a1f00" stroke="#8a6b00" stroke-width="6" transform="rotate(-2 780 315)"/>
<rect x="590" y="110" width="330" height="430" rx="22" fill="#2a1f00" stroke="{ac}" stroke-width="7"/>
<text x="755" y="190" text-anchor="middle" font-size="40" font-weight="900" fill="#fff">문서</text>
<g stroke="#8a6b00" stroke-width="8" stroke-linecap="round">
<path d="M640 240 L870 240"/><path d="M640 280 L850 280"/><path d="M640 320 L870 320"/><path d="M640 360 L800 360"/><path d="M640 400 L870 400"/><path d="M640 440 L830 440"/>
</g>
<text x="755" y="505" text-anchor="middle" font-size="26" fill="#d4b24c">길게 · 무엇을</text>'''
make('th_fri','/home/claude/out/fri/금_01_썸네일.png','#1a1200','#5a4200',ac,'Claude 프로젝트 지침과','지식 파일, 뭐가 다를까','지침은 짧게, 규칙은 문서로. 지원 문서와 실제 구성으로 정리',svg,fs=92)
