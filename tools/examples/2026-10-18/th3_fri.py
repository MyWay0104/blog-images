from thumb import make
ac='#ffd43b'
# 중심 오브젝트: 왼쪽에 흐릿한 토글 스위치(X), 오른쪽에 빛나는 프롬프트 한 줄. 관계 = 스위치가 아니라 문장
svg=f'''<defs><filter id="g" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="26"/></filter></defs>
<!-- 토글 스위치 (아님) -->
<rect x="110" y="150" width="260" height="120" rx="60" fill="#241e0e" stroke="#4a3d1a" stroke-width="6"/>
<circle cx="300" cy="210" r="44" fill="#4a3d1a"/>
<text x="240" y="330" text-anchor="middle" font-size="28" font-weight="700" fill="#8a7a4a">켜고 끄는 스위치?</text>
<line x1="120" y1="140" x2="360" y2="285" stroke="#b03a2e" stroke-width="12" stroke-linecap="round"/>
<line x1="360" y1="140" x2="120" y2="285" stroke="#b03a2e" stroke-width="12" stroke-linecap="round"/>
<!-- 화살표 -->
<text x="440" y="222" text-anchor="middle" font-size="44" font-weight="900" fill="{ac}">→</text>
<!-- 프롬프트 한 줄 -->
<rect x="500" y="110" width="500" height="200" rx="22" fill="{ac}" opacity=".3" filter="url(#g)"/>
<rect x="500" y="110" width="500" height="200" rx="22" fill="#14110a" stroke="{ac}" stroke-width="6"/>
<text x="530" y="170" font-size="26" fill="#d9c98a" font-family="DejaVu Sans Mono">&gt; 실패하는 pytest 3개를</text>
<text x="530" y="215" font-size="26" fill="#d9c98a" font-family="DejaVu Sans Mono">  고쳐줘</text>
<rect x="600" y="235" width="195" height="52" rx="10" fill="{ac}"/>
<text x="697" y="272" text-anchor="middle" font-size="30" font-weight="900" fill="#14110a" font-family="DejaVu Sans Mono">ultrathink</text>
<text x="750" y="370" text-anchor="middle" font-size="30" font-weight="700" fill="{ac}">프롬프트에 붙는 한 줄</text>
<!-- 아래: 측정 -->
<rect x="110" y="430" width="890" height="110" rx="18" fill="#241e0e" stroke="#4a3d1a" stroke-width="4"/>
<text x="555" y="476" text-anchor="middle" font-size="26" fill="#d9c98a" font-family="DejaVu Sans Mono">{{"thinking": null, "thinking_chars": 0, ...}}</text>
<text x="555" y="518" text-anchor="middle" font-size="24" font-weight="700" fill="#8a7a4a">"켜졌는가"가 아니라 로그로 확인한다</text>'''
make('th3_fri','/home/claude/out3/fri/금_01_썸네일.png','#0f0c05','#4a3a0e',ac,'ultrathink는','스위치가 아니다','오픈 모델을 Claude Code에 붙였을 때 추론 깊이 확인',svg,fs=106)
