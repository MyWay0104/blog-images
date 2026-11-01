from thumb import make
ac='#20c997'
# 핵심 질문: 관측 도구의 네 단위가 어떻게 포개지나 / 분위기: 개념 구분 / 팔레트: 짙은 청록 배경 + 민트 / 중심 오브젝트: 포개진 네 겹 상자(Project > Session > Trace > Span), 맨 안쪽 Span만 빛남
svg=f'''<defs><filter id="g" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="22"/></filter></defs>
<rect x="60" y="30" width="960" height="530" rx="36" fill="#07251f" stroke="#2f6b5e" stroke-width="6"/>
<text x="100" y="86" font-size="34" font-weight="900" fill="#96f2d7">Project</text>
<rect x="140" y="120" width="800" height="400" rx="30" fill="#0a332b" stroke="#3f8f7c" stroke-width="6"/>
<text x="180" y="174" font-size="34" font-weight="900" fill="#b2f2e0">Session</text>
<rect x="220" y="206" width="640" height="270" rx="26" fill="#0e4237" stroke="{ac}" stroke-width="6"/>
<text x="260" y="258" font-size="34" font-weight="900" fill="#e6fcf5">Trace</text>
<rect x="300" y="290" width="480" height="140" rx="22" fill="{ac}" opacity=".35" filter="url(#g)"/>
<rect x="300" y="290" width="480" height="140" rx="22" fill="{ac}"/>
<text x="540" y="378" text-anchor="middle" font-size="64" font-weight="900" fill="#031a14">Span</text>'''
make('th_thu','/home/claude/out/thu/목_01_썸네일.png','#041a16','#0f5a48',ac,'Trace, Span, Session','뭐가 어디에 들어가나','LLM 관측 도구가 기록을 묶는 네 단위, 공식 문서로 정리',svg,fs=96)
