from thumb import make
ac='#ff922b'
# 핵심 질문: 터미널에 (.venv) 표시가 없으면 가상환경을 안 쓰는 건가 / 분위기: 디버깅·추적 / 팔레트: 짙은 갈색 검정 + 오렌지 / 중심 오브젝트: 표시 칸이 비어 있는 터미널 창에서 .venv 폴더의 python.exe로 곧장 이어지는 선
mono="font-family=\"'DejaVu Sans Mono','Noto Sans Mono CJK KR',monospace\""
svg=f'''<defs><filter id="g" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="18"/></filter>
<linearGradient id="f" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7a4514"/><stop offset="1" stop-color="#3d2510"/></linearGradient>
<marker id="m" markerUnits="userSpaceOnUse" markerWidth="34" markerHeight="34" refX="28" refY="17" orient="auto"><path d="M0,0 L34,17 L0,34 z" fill="{ac}"/></marker></defs>
<!-- 터미널 창: (.venv) 자리가 비어 있다 -->
<rect x="70" y="30" width="520" height="270" rx="24" fill="#2b1a0a" stroke="#5f3811" stroke-width="6"/>
<rect x="70" y="30" width="520" height="56" rx="24" fill="#3d2510"/><rect x="70" y="62" width="520" height="24" fill="#3d2510"/>
<circle cx="108" cy="58" r="10" fill="#5f3811"/><circle cx="140" cy="58" r="10" fill="#5f3811"/><circle cx="172" cy="58" r="10" fill="#5f3811"/>
<rect x="104" y="124" width="170" height="60" rx="14" fill="none" stroke="#ffa94d" stroke-width="5" stroke-dasharray="14 10"/>
<text x="294" y="168" font-size="40" font-weight="700" fill="#ffd8a8" {mono}>PS &gt;</text>
<rect x="424" y="130" width="22" height="48" fill="#ffd8a8"/>
<text x="104" y="246" font-size="30" font-weight="700" fill="#ffa94d">(.venv) 표시 없음</text>
<!-- .venv 폴더 -->
<path d="M610 270 H770 L800 306 H1016 Q1030 306 1030 320 V540 Q1030 556 1014 556 H626 Q610 556 610 540 Z" fill="url(#f)" stroke="{ac}" stroke-width="6"/>
<text x="640" y="358" font-size="40" font-weight="900" fill="#fff" {mono}>.venv</text>
<rect x="660" y="414" width="330" height="92" rx="22" fill="{ac}" opacity=".4" filter="url(#g)"/>
<rect x="660" y="414" width="330" height="92" rx="22" fill="{ac}"/>
<text x="825" y="474" text-anchor="middle" font-size="38" font-weight="900" fill="#1a0f05" {mono}>python.exe</text>
<!-- 실행 줄에서 python.exe로 곧장 -->
<path d="M350 304 C 350 460, 480 460, 648 460" stroke="{ac}" stroke-width="18" fill="none" opacity=".3" filter="url(#g)"/>
<path d="M350 304 C 350 460, 480 460, 648 460" stroke="{ac}" stroke-width="9" fill="none" marker-end="url(#m)"/>'''
make('th_mon4','/home/claude/out/mon/월_01_썸네일.png','#1a0f05','#4a2a0c',ac,'(.venv)가 없는데','venv로 실행된다?','VS Code가 가상환경을 쓰는 방식과 확인 방법',svg,fs=96)
