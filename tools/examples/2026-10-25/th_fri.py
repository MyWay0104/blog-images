from thumb import make
ac='#ff922b'
# 핵심 질문: 코드 분석을 한 문장으로 시키면 왜 안 되나 / 분위기: 구조·원리 / 팔레트: 짙은 갈색 배경 + 주황 / 중심 오브젝트: 돋보기 하나가 코드 파일 더미 위에 놓이고, 옆에 일시정지(⏸) 표시 — 읽기만 함
svg=f'''<defs><filter id="g" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="26"/></filter></defs>
<!-- 파일 더미 -->
<rect x="140" y="120" width="420" height="420" rx="22" fill="#2a1a0a" stroke="#5a3a1a" stroke-width="5" transform="rotate(-6 350 330)"/>
<rect x="160" y="100" width="420" height="420" rx="22" fill="#2a1a0a" stroke="#6b4420" stroke-width="5" transform="rotate(3 370 310)"/>
<rect x="180" y="80" width="420" height="420" rx="22" fill="#2a1a0a" stroke="#8a5a2a" stroke-width="5"/>
<g fill="#6b4420"><rect x="220" y="130" width="200" height="16" rx="8"/><rect x="220" y="170" width="300" height="16" rx="8"/><rect x="250" y="210" width="260" height="16" rx="8"/><rect x="250" y="250" width="180" height="16" rx="8"/><rect x="220" y="290" width="320" height="16" rx="8"/><rect x="250" y="330" width="220" height="16" rx="8"/><rect x="220" y="370" width="280" height="16" rx="8"/><rect x="250" y="410" width="160" height="16" rx="8"/></g>
<!-- 돋보기 -->
<circle cx="640" cy="330" r="150" fill="{ac}" opacity=".3" filter="url(#g)"/>
<circle cx="640" cy="330" r="140" fill="#1c0d02" stroke="{ac}" stroke-width="14"/>
<path d="M745 435 L880 570" stroke="{ac}" stroke-width="36" stroke-linecap="round"/>
<g fill="{ac}"><rect x="560" y="290" width="170" height="16" rx="8"/><rect x="560" y="330" width="120" height="16" rx="8"/><rect x="560" y="370" width="150" height="16" rx="8"/></g>
<text x="640" y="262" text-anchor="middle" font-size="22" font-weight="700" fill="#ffd8b0" font-family="DejaVu Sans Mono">main.py:ask()</text>
<!-- 일시정지 배지 -->
<rect x="60" y="520" width="330" height="60" rx="14" fill="#2a1a0a" stroke="{ac}" stroke-width="4"/>
<text x="225" y="562" text-anchor="middle" font-size="30" font-weight="900" fill="{ac}" font-family="DejaVu Sans Mono">plan mode on</text>'''
make('th_fri','/home/claude/out/fri/금_01_썸네일.png','#1c0d02','#5a3010',ac,'남의 코드 분석','뭐라고 시키지?','Plan 모드 + 쪼개기·근거 강제·모르는 것 목록',svg,fs=112)
