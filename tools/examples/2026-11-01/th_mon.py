from thumb import make
ac='#339af0'
# 핵심 질문: 실행은 성공인데 왜 결과가 비었나 / 분위기: 디버깅·추적 / 팔레트: 짙은 남색 배경 + 파랑 / 중심 오브젝트: 달력(예약) 위에 체크 표시가 있는데, 그 옆 문서는 비어 있음 — "성공"과 "빈 문서"의 대비
svg=f'''<defs><filter id="g" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="26"/></filter></defs>
<!-- 달력 -->
<rect x="90" y="70" width="400" height="430" rx="26" fill="#0b2238" stroke="#1d4a73" stroke-width="6"/>
<rect x="90" y="70" width="400" height="80" rx="26" fill="#1d4a73"/>
<text x="290" y="125" text-anchor="middle" font-size="34" font-weight="700" fill="#eaf4ff">매주 토요일 23:00</text>
<g fill="#1d4a73"><rect x="130" y="190" width="60" height="50" rx="10"/><rect x="210" y="190" width="60" height="50" rx="10"/><rect x="290" y="190" width="60" height="50" rx="10"/><rect x="370" y="190" width="60" height="50" rx="10"/>
<rect x="130" y="260" width="60" height="50" rx="10"/><rect x="210" y="260" width="60" height="50" rx="10"/><rect x="290" y="260" width="60" height="50" rx="10"/><rect x="370" y="260" width="60" height="50" rx="10"/></g>
<circle cx="400" cy="420" r="52" fill="{ac}" opacity=".35" filter="url(#g)"/>
<circle cx="400" cy="420" r="46" fill="{ac}"/>
<path d="M375 420 L393 438 L428 400" stroke="#04101c" stroke-width="10" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
<text x="180" y="432" font-size="30" font-weight="700" fill="{ac}">실행 성공</text>
<!-- 화살표 -->
<path d="M520 285 L600 285" stroke="{ac}" stroke-width="12" stroke-linecap="round"/><polygon points="596,258 650,285 596,312" fill="{ac}"/>
<!-- 빈 문서 -->
<path d="M690 70 L930 70 L1000 140 L1000 520 L690 520 Z" fill="#0b2238" stroke="{ac}" stroke-width="6" stroke-linejoin="round"/>
<path d="M930 70 L930 140 L1000 140" fill="none" stroke="{ac}" stroke-width="6" stroke-linejoin="round"/>
<text x="845" y="300" text-anchor="middle" font-size="72" font-weight="900" fill="{ac}">0건</text>
<text x="845" y="360" text-anchor="middle" font-size="28" fill="#9ccdf5">검토한 대화</text>
<text x="845" y="470" text-anchor="middle" font-size="28" font-weight="700" fill="#ff8787">대화 검색 도구 없음</text>'''
make('th_mon','/home/claude/out/mon/월_01_썸네일.png','#04101c','#123a5c',ac,'실행은 성공인데','파일은 비어 있다?','Claude 예약작업이 대화 이력을 못 읽는 이유',svg,fs=108)
