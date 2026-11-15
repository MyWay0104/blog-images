from thumb import make
ac='#20c997'
# 핵심 질문: 'use cache'를 켠 뒤 새 글이 늦게 보일 때 revalidateTag와 updateTag 중 무엇을 어디서 부르나 / 분위기: 비교·원리 / 팔레트: 짙은 청록 검정 + 민트 틸 / 중심 오브젝트: posts 태그가 붙은 캐시 저장소에 두 신호(표시만·즉시 만료)가 꽂히는 그림
mono="font-family=\"'DejaVu Sans Mono','Noto Sans Mono CJK KR',monospace\""
svg=f'''<defs><filter id="g" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="22"/></filter>
<marker id="m1" markerUnits="userSpaceOnUse" markerWidth="30" markerHeight="30" refX="26" refY="15" orient="auto"><path d="M0,0 L30,15 L0,30 z" fill="#63e6be"/></marker>
<marker id="m2" markerUnits="userSpaceOnUse" markerWidth="30" markerHeight="30" refX="26" refY="15" orient="auto"><path d="M0,0 L30,15 L0,30 z" fill="{ac}"/></marker></defs>
<!-- 캐시 저장소 -->
<rect x="90" y="50" width="400" height="420" rx="30" fill="#0c3328" stroke="#1b5e4a" stroke-width="6"/>
<text x="290" y="112" text-anchor="middle" font-size="30" font-weight="700" fill="#fff">use cache 저장소</text>
<rect x="180" y="142" width="220" height="58" rx="29" fill="{ac}"/>
<text x="290" y="183" text-anchor="middle" font-size="30" font-weight="700" fill="#06201a" {mono}>posts</text>
<rect x="140" y="240" width="300" height="26" rx="13" fill="#1b5e4a"/>
<rect x="140" y="288" width="230" height="26" rx="13" fill="#1b5e4a"/>
<rect x="140" y="336" width="270" height="26" rx="13" fill="#1b5e4a"/>
<rect x="140" y="384" width="190" height="26" rx="13" fill="#1b5e4a"/>
<text x="290" y="446" text-anchor="middle" font-size="24" fill="#63e6be">저장해 둔 옛 목록</text>
<!-- 신호 1: revalidateTag -->
<rect x="640" y="70" width="380" height="124" rx="24" fill="#0c3328" stroke="#63e6be" stroke-width="6"/>
<text x="830" y="122" text-anchor="middle" font-size="31" font-weight="700" fill="#fff" {mono}>revalidateTag</text>
<text x="830" y="168" text-anchor="middle" font-size="24" fill="#96f2d7">오래됐다고 표시만 한다</text>
<path d="M636 132 L500 132" stroke="#63e6be" stroke-width="8" stroke-dasharray="18 14" marker-end="url(#m1)"/>
<!-- 신호 2: updateTag -->
<rect x="640" y="286" width="380" height="124" rx="24" fill="{ac}" opacity=".35" filter="url(#g)"/>
<rect x="640" y="286" width="380" height="124" rx="24" fill="{ac}"/>
<text x="830" y="338" text-anchor="middle" font-size="31" font-weight="700" fill="#06201a" {mono}>updateTag</text>
<text x="830" y="384" text-anchor="middle" font-size="24" font-weight="700" fill="#06201a">그 자리에서 즉시 만료</text>
<path d="M636 348 L500 348" stroke="{ac}" stroke-width="8" marker-end="url(#m2)"/>
<!-- 바닥 설명 -->
<text x="555" y="530" text-anchor="middle" font-size="25" fill="#96f2d7">둘 다 같은 posts 태그를 겨냥한다 — 차이는 다음 요청이 받는 것</text>'''
make('th_fri3','/home/claude/out/fri/금_01_썸네일.png','#06201a','#0f4a3a',ac,'revalidateTag','vs updateTag',"'use cache' 뒤 새 글이 늦게 보이는 이유",svg,fs=92)
