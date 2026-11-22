from thumb import make
ac='#4dabf7'
# 핵심 질문: LangGraph 라우팅에서 바뀌는 것은 그래프인가 부품인가 / 분위기: 비교·선택 / 팔레트: 짙은 남색 + 스카이 / 중심 오브젝트: 세 갈래로 갈라지는 배선 한가운데의 소켓과, 그 위에 떠서 끼워지려는 칩 하나
svg=f'''<defs><filter id="g" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="18"/></filter>
<linearGradient id="c" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#a5d8ff"/><stop offset="1" stop-color="#339af0"/></linearGradient></defs>
<!-- 배선: 왼쪽에서 들어와 세 갈래로 나간다 -->
<line x1="60" y1="330" x2="372" y2="330" stroke="#1c4470" stroke-width="16" stroke-linecap="round"/>
<path d="M708 300 C 820 300, 820 150, 930 150" stroke="#1c4470" stroke-width="16" fill="none" stroke-linecap="round"/>
<line x1="708" y1="330" x2="930" y2="330" stroke="#1c4470" stroke-width="16" stroke-linecap="round"/>
<path d="M708 360 C 820 360, 820 510, 930 510" stroke="#1c4470" stroke-width="16" fill="none" stroke-linecap="round"/>
<circle cx="60" cy="330" r="20" fill="#74c0fc"/>
<rect x="930" y="112" width="96" height="76" rx="18" fill="#0d2137" stroke="#74c0fc" stroke-width="6"/>
<rect x="930" y="292" width="96" height="76" rx="18" fill="#0d2137" stroke="#74c0fc" stroke-width="6"/>
<rect x="930" y="472" width="96" height="76" rx="18" fill="#0d2137" stroke="#74c0fc" stroke-width="6"/>
<!-- 소켓 (부품 자리) -->
<rect x="376" y="196" width="328" height="268" rx="34" fill="#0a1a2e" stroke="#74c0fc" stroke-width="7" stroke-dasharray="20 14"/>
<!-- 칩: 소켓 위에 살짝 떠 있다 -->
<rect x="424" y="166" width="232" height="232" rx="30" fill="{ac}" opacity=".5" filter="url(#g)"/>
<rect x="424" y="166" width="232" height="232" rx="30" fill="url(#c)"/>
<rect x="468" y="210" width="144" height="144" rx="18" fill="#06111f" opacity=".85"/>
<g stroke="#a5d8ff" stroke-width="9" stroke-linecap="round">
<line x1="470" y1="150" x2="470" y2="166"/><line x1="540" y1="150" x2="540" y2="166"/><line x1="610" y1="150" x2="610" y2="166"/>
<line x1="470" y1="398" x2="470" y2="414"/><line x1="540" y1="398" x2="540" y2="414"/><line x1="610" y1="398" x2="610" y2="414"/></g>
<text x="540" y="304" text-anchor="middle" font-size="84" font-weight="900" fill="#fff">?</text>
<!-- 라벨 2개 -->
<text x="540" y="524" text-anchor="middle" font-size="38" font-weight="900" fill="#fff">라우팅 노드</text>
<text x="216" y="290" text-anchor="middle" font-size="32" font-weight="900" fill="#74c0fc">배선</text>'''
make('th_thu4','/home/claude/out/thu/목_01_썸네일.png','#06111f','#12345c',ac,'그래프는 그대로','부품만 바꾼다?','Jev와 LLM structured output을 가르는 기준',svg,fs=112)
