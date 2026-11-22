from thumb import make
import math
ac='#94d82d'
# 핵심 질문: 글을 쓰지 않는 AI 모델은 무엇을 돌려주나 / 분위기: 구조·원리 / 팔레트: 짙은 녹색 검정 + 라임 / 중심 오브젝트: 아니오(0)에서 예(1)까지 이어진 반원 게이지와 0.91을 가리키는 바늘 하나
cx,cy,r=540,400,290
ang=math.radians(180-0.91*180)             # 0.91 지점의 각도
ex,ey=cx+r*math.cos(ang),cy-r*math.sin(ang)   # 밝은 호가 끝나는 점
nx,ny=cx+(r-70)*math.cos(ang),cy-(r-70)*math.sin(ang)   # 바늘 끝
svg=f'''<defs><filter id="g" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="16"/></filter>
<linearGradient id="a" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#5c940d"/><stop offset="1" stop-color="#c0eb75"/></linearGradient></defs>
<!-- 바탕 호: 아니오(0) ~ 예(1) -->
<path d="M {cx-r} {cy} A {r} {r} 0 0 1 {cx+r} {cy}" stroke="#22330b" stroke-width="58" fill="none" stroke-linecap="round"/>
<!-- 밝은 호: 0.91까지 -->
<path d="M {cx-r} {cy} A {r} {r} 0 0 1 {ex:.1f} {ey:.1f}" stroke="{ac}" stroke-width="58" fill="none" stroke-linecap="round" opacity=".35" filter="url(#g)"/>
<path d="M {cx-r} {cy} A {r} {r} 0 0 1 {ex:.1f} {ey:.1f}" stroke="url(#a)" stroke-width="58" fill="none" stroke-linecap="round"/>
<!-- 바늘 -->
<line x1="{cx}" y1="{cy}" x2="{nx:.1f}" y2="{ny:.1f}" stroke="#f4fce3" stroke-width="14" stroke-linecap="round"/>
<circle cx="{cx}" cy="{cy}" r="44" fill="{ac}" opacity=".4" filter="url(#g)"/>
<circle cx="{cx}" cy="{cy}" r="30" fill="{ac}"/><circle cx="{cx}" cy="{cy}" r="11" fill="#0e1505"/>
<!-- 라벨 3개 -->
<text x="{cx-r}" y="{cy+92}" text-anchor="middle" font-size="40" font-weight="900" fill="#a9e34b">아니오</text>
<text x="{cx+r}" y="{cy+92}" text-anchor="middle" font-size="40" font-weight="900" fill="#fff">예</text>
<text x="{cx}" y="{cy+150}" text-anchor="middle" font-size="104" font-weight="900" fill="#fff" letter-spacing="-2">0.91</text>'''
make('th_wed4','/home/claude/out/wed/수_01_썸네일.png','#0e1505','#2f4a0a',ac,'글은 안 쓰고','확률만 답한다?','Jev와 System One 모델이 답하는 방식',svg,fs=118)
