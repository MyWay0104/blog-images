from thumb import make
ac='#ffd43b'
# 핵심 질문: 문장을 넣으면 다음 단어는 어떻게 정해지나 / 분위기: 설치·따라하기 / 팔레트: 짙은 올리브 검정 + 옐로 / 중심 오브젝트: 층층이 쌓인 블록과, 그 층을 건너뛰어 위로 올라가는 화살표 하나
slabs=''
ys=[452,378,304,230,156]
ops=[.35,.5,.65,.8,1]
for y,o in zip(ys,ops):
    slabs+=f'<rect x="250" y="{y}" width="470" height="54" rx="16" fill="url(#s)" opacity="{o}"/>'
svg=f'''<defs><filter id="g" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="16"/></filter>
<linearGradient id="s" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8a6d0b"/><stop offset="1" stop-color="#ffe066"/></linearGradient>
<marker id="m" markerUnits="userSpaceOnUse" markerWidth="44" markerHeight="44" refX="34" refY="22" orient="auto"><path d="M0,0 L44,22 L0,44 z" fill="{ac}"/></marker></defs>
<!-- 층을 지나 올라가는 가운데 길 -->
<line x1="485" y1="560" x2="485" y2="96" stroke="#5c4d0c" stroke-width="10" stroke-linecap="round"/>
{slabs}
<!-- 층을 건너뛰는 길 -->
<path d="M 730 480 C 890 480, 890 110, 740 104" stroke="{ac}" stroke-width="22" fill="none" opacity=".35" filter="url(#g)"/>
<path d="M 730 480 C 890 480, 890 110, 740 104" stroke="{ac}" stroke-width="11" fill="none" stroke-dasharray="26 16" stroke-linecap="round" marker-end="url(#m)"/>
<!-- 꼭대기: 다음 단어 -->
<circle cx="485" cy="84" r="46" fill="{ac}" opacity=".4" filter="url(#g)"/>
<circle cx="485" cy="84" r="30" fill="{ac}"/><circle cx="485" cy="84" r="11" fill="#14120a"/>
<!-- 라벨 3개 -->
<text x="130" y="330" text-anchor="middle" font-size="44" font-weight="900" fill="#ffe066">12층</text>
<text x="966" y="304" text-anchor="middle" font-size="34" font-weight="900" fill="#fff">건너뛰는 길</text>
'''
make('th_fri4','/home/claude/out/fri/금_01_썸네일.png','#14120a','#4a3f0a',ac,'문장을 넣으면','다음 단어는?','Transformer Explainer로 GPT-2 속 들여다보기',svg,fs=124)
