from lib import *
# 대표 예시: Notion을 글 저장소로 쓰는 Next.js 16 블로그(notion-blog). 부품: components/ui/pagination.tsx(shadcn, Base UI 기반), components/common/post-pagination.tsx(수정 지점)
T='[AI활용] Next.js hydration mismatch 오류 해결: tabIndex가 서버와 브라우저에서 달랐던 이유'
SN='출처: Next.js 공식 문서(nextjs.org), 2026-11-15 캡처'
SR='출처: React 공식 문서(react.dev, v19.3 표시), 2026-11-15 캡처'
SB='출처: Base UI 공식 문서(base-ui.com), 2026-11-15 캡처'
SS='출처: shadcn/ui 공식 문서 체인지로그(ui.shadcn.com), 2026-11-15 캡처'
SM='출처: MDN Web Docs(developer.mozilla.org), 2026-11-15 캡처'
SX='공식 문서의 오류 문구와 제 기록(서버 0, 브라우저 -1)을 바탕으로 재구성한 예시 화면 (실제 콘솔 원문이 아닙니다)'
b=''
b+=IMG(1,'월_01_썸네일.png','대표 이미지(썸네일)')
b+=P('Notion을 글 저장소로 쓰는 Next.js 16 블로그를 만들다가','개발 서버 콘솔에 하이드레이션 경고가 떴습니다.','화면은 멀쩡해 보였는데, 페이지 번호 링크의 `tabIndex`가','**서버에서는 `"0"`, 브라우저에서는 `"-1"`**로 달랐습니다.')
b+=P('처음엔 "속성 하나 맞춰 주면 끝"이라고 생각했습니다.','그런데 정리하고 보니 그건 증상을 덮는 쪽이었습니다.')
b+=Q('하이드레이션은 단순히 "동적 HTML이라서"가 아니라,','서버에서 먼저 만든 React HTML에 브라우저의 React 동작을 연결할 때 발생한다.')
b+=P('결론부터 적으면,','**==서버와 브라우저가 속성을 다르게 합치는 경로(버튼 안에 링크를 끼우는 `render`) 자체를 쓰지 않도록 바꿨습니다.==**','공용 부품은 손대지 않고, 그 부품을 쓰는 쪽에서 고쳤습니다.')
b+=BOX('**이 글의 기준**','확인 날짜: 2026-11-15 (프로젝트 기록은 2026-08)','근거: 제 프로젝트 학습 기록(Next.js 16, React 19, shadcn/ui Base UI 기반) + Next.js 공식 문서(react-hydration-error), React 공식 문서(hydrateRoot), Base UI 공식 문서(Button), shadcn/ui 체인지로그, MDN(tabindex)','기록에 남은 것은 "서버 0 / 브라우저 -1"이라는 값의 차이와 수정 내용입니다. 콘솔 메시지 원문은 남기지 못해, 아래 콘솔 화면은 공식 문서의 문구로 재구성했습니다.','예시 이름은 `notion-blog`로 통일했습니다. 코드 조각도 기록의 구조를 바탕으로 다시 쓴 것입니다.')
b+=HR()
b+=H1('1. 하이드레이션이 정확히 뭘 하는 단계인가')
b+=IMG(2,'월_02_도식_하이드레이션.png','서버가 HTML을 만들어 보내고, 브라우저에서 React가 같은 트리를 다시 계산해 맞물리는 과정과 불일치가 생기는 지점을 그린 도식')
b+=P('Next.js는 서버에서 React 트리를 **완성된 HTML**로 만들어 보냅니다.','브라우저는 그 HTML을 먼저 그립니다. 이때는 아직 클릭이 안 됩니다.')
b+=P('그다음 JS가 도착하면 React가 **같은 트리를 브라우저에서 다시 계산**하면서','서버가 만든 HTML에 이벤트 핸들러를 붙입니다. 이게 하이드레이션입니다.','제 기록의 비유로는 "가구가 다 놓인 모델하우스에 전기와 수도를 연결하는 일"입니다.')
b+=IMG(3,'월_03_공식문서_Nextjs_원인.png','Next.js 공식 문서 "Text content does not match server-rendered HTML": 왜 이 오류가 나는지와 흔한 원인 목록',SN)
b+=P('Next.js 문서는 이렇게 적습니다.','"**서버에서 미리 렌더링된 React 트리와, 브라우저의 첫 렌더링(하이드레이션)에서 렌더링된 React 트리 사이에 차이가 있었다.**"','흔한 원인으로 잘못된 태그 중첩, `typeof window` 분기, `window`·`localStorage` 같은 브라우저 전용 API,','`Date()`, 브라우저 확장 프로그램, CSS-in-JS 설정, HTML을 고치는 CDN을 듭니다.')
b+=IMG(4,'월_04_공식문서_React_주의.png','React 공식 문서 hydrateRoot의 Caveats: 렌더링 결과가 서버와 동일해야 하며 불일치는 버그로 보고 고쳐야 한다, 속성 차이가 보정된다는 보장은 없다',SR)
b+=P('React 문서의 두 문장이 이 글의 방향을 정했습니다.','"**`hydrateRoot()`는 렌더링된 내용이 서버 렌더링 결과와 동일하기를 기대한다. 불일치는 버그로 취급하고 고쳐야 한다.**"','"**개발 모드에서는 불일치를 경고하지만, 속성 차이가 보정된다는 보장은 없다.**"')
b+=P('즉 경고가 떠도 React가 알아서 고쳐 주지 않을 수 있습니다.','제 기록에 적힌 "일부 속성이 서버 값 그대로 남을 수 있다"가 바로 이 문장입니다.')
b+=HR()
b+=H1('2. 제 경우: 페이지 번호 하나가 거치던 네 단계')
b+=IMG(5,'월_05_도식_문제경로.png','PaginationLink → Base UI Button → render={<a>} → 속성 병합으로 이어지는 경로와, 그 끝에서 서버 tabIndex 0 / 브라우저 -1로 갈라진 결과')
b+=P('문제가 난 곳은 글 목록 아래의 페이지네이션이었습니다.','shadcn의 `PaginationLink`는 안에서 **Base UI의 Button**을 쓰고,','그 버튼에 `render={<a>}`로 링크 태그를 끼워 넣어 "버튼처럼 보이는 링크"를 만듭니다.')
b+=P('이 과정에서 버튼의 속성과 링크의 속성이 **합쳐져** 최종 태그가 됩니다.','그 병합 결과가 서버와 브라우저에서 달랐습니다.','기록에 남은 값은 `tabIndex` 서버 `"0"`, 브라우저 `"-1"`입니다.')
b+=IMG(6,'월_06_콘솔경고_재구성.png','개발 서버 콘솔의 하이드레이션 경고 예시: React의 오류 문구와 PostPagination 아래 a 태그의 tabIndex 차이',SX)
b+=P('React가 내는 경고 문구는 공식 오류 페이지(#418)에 있습니다.','"**서버가 렌더링한 HTML이 클라이언트와 일치하지 않아 하이드레이션에 실패했다.','그 결과 이 트리는 클라이언트에서 다시 생성된다.**"','위 화면의 트리 부분은 제 기록의 값으로 다시 그린 것입니다.')
b+=IMG(7,'월_07_MDN_tabindex.png','MDN tabindex 문서: 음수 값은 순차 키보드 탐색에서 제외되고, 0은 문서 순서대로 Tab에 포함된다는 설명',SM)
b+=P('왜 이 차이가 "콘솔 잡음"이 아닌지는 MDN이 설명해 줍니다.','"**음수 값은 그 요소가 순차 키보드 탐색으로 도달할 수 없다는 뜻**"이고,','"**`tabindex="0"`은 순차 키보드 탐색에서 포커스 가능해야 한다는 뜻**"입니다.')
b+=Q('첫 페이지의 비활성 "이전" 항목은 눌러도 이동할 곳이 없다.','그런데 서버의 tabIndex="0"이 남으면 키보드 사용자는 작동하지 않는 항목에서 한 번 멈추게 된다.','이는 단순 콘솔 잡음이 아니라 접근성 버그다.')
b+=P('화면에는 아무 이상이 없어 보였지만,','Tab 키로 움직이는 사람에게는 **눌러도 아무 일 없는 가짜 링크**가 하나 끼어 있던 겁니다.')
b+=HR()
b+=H1('3. 공식 문서가 알려 주는 세 가지 해결과, 왜 안 썼나')
b+=IMG(8,'월_08_공식문서_Nextjs_해결.png','Next.js 공식 문서의 Solution 3: suppressHydrationWarning은 한 단계만 적용되는 비상구이며, React는 불일치 텍스트를 고치려 하지 않는다는 안내',SN)
b+=P('Next.js 문서는 해결책을 세 가지로 정리합니다.')
b+=TABLE(['문서의 해결책','무엇을 하나','제 경우에 맞았나'],[
['`useEffect`로 클라이언트에서만 렌더','첫 렌더는 서버와 같게 두고, 하이드레이션 뒤 한 번 더 그린다 (두 번 렌더)','아니오. 페이지 번호는 서버와 브라우저가 같아야 하는 값이다'],
['`dynamic(..., { ssr: false })`','그 컴포넌트는 서버에서 아예 렌더하지 않는다','아니오. 글 목록 아래 링크를 서버 HTML에서 빼면 SSR의 이점을 버린다'],
['`suppressHydrationWarning`','경고만 끈다. "한 단계만 적용되고 비상구용"','아니오. 값이 다른 원인이 남는다. 문서도 "불일치 텍스트를 고쳐 주지 않는다"고 적는다']])
b+=P('셋 다 **"서버와 브라우저가 다를 수밖에 없는 값"**(시각, 랜덤, 브라우저 설정)을 위한 길입니다.','페이지 번호 링크는 그런 값이 아니었습니다. 같은 코드가 같은 결과를 내야 하는 자리였습니다.')
b+=HR()
b+=H1('4. 속성을 맞추지 않고 경로를 없앴다')
b+=IMG(9,'월_09_BaseUI_링크규칙.png','Base UI 공식 문서 Button의 "Rendering links as buttons": 링크는 자체 의미가 있으므로 render로 버튼처럼 만들지 말고, 버튼처럼 보이게 하려면 a 요소에 직접 CSS를 입히라는 안내',SB)
b+=P('Base UI 문서를 읽으니 답이 먼저 적혀 있었습니다.','"**링크(`<a>`)는 자체 의미를 가지므로 `render` prop을 통해 버튼으로 렌더링해서는 안 된다.**"','"**링크가 시각적으로 버튼처럼 보여야 한다면, Button 컴포넌트 대신 `<a>` 요소에 직접 CSS를 입혀라.**"')
b+=IMG(10,'월_10_BaseUI_API.png','Base UI Button API: nativeButton(기본값 true, render로 교체한 요소가 네이티브 button인지), render(컴포넌트의 HTML 요소를 다른 태그나 컴포넌트로 교체)',SB)
b+=P('`render`는 "컴포넌트의 HTML 요소를 다른 태그로 바꾸거나 다른 컴포넌트와 합성"하는 옵션이고,','`nativeButton`은 "render로 바꾼 요소가 네이티브 `<button>`인지"를 알려 주는 옵션(기본값 `true`)입니다.','링크를 끼우려면 `nativeButton={false}`까지 써야 했으니, 애초에 버튼 규칙에 맞지 않는 사용이었습니다.')
b+=IMG(11,'월_11_도식_전후비교.png','수정 전(버튼 안에 링크를 끼우는 render 병합)과 수정 후(Link에 buttonVariants 스타일만, 비활성은 span aria-disabled)의 코드 경로 비교')
b+=P('그래서 바꾼 구조는 이렇습니다.','이동 가능한 항목은 **Next.js `Link`에 `buttonVariants`로 스타일만** 입혔습니다.','이동 불가능한 이전·다음은 **`<span aria-disabled="true">`**로 두었습니다.')
b+=CODE('''// components/common/post-pagination.tsx (구조만 옮겨 적음)
// 이동 가능: 링크는 링크로 두고, 버튼 모양은 클래스로만
<Link href="/posts?page=2" className={buttonVariants({ variant: "ghost" })}>
  다음
</Link>

// 이동 불가: 애초에 포커스 대상이 아닌 span
<span aria-disabled="true" className={...}>이전</span>''',[('Link','#8ce99a'),('span','#ffd43b'),('buttonVariants','#74c0fc')])
b+=P('`span`은 특별한 클릭 기능이 없는 묶음 요소라서 **Tab 포커스 대상이 되지 않습니다.**','병합 경로를 쓰지 않으니 서버와 브라우저가 다르게 계산할 자리 자체가 없어졌습니다.')
b+=Q('이 해결은 components/ui/pagination.tsx를 고치지 않고','components/common/post-pagination.tsx에서 문제 경로만 우회했다.','공용 원본의 영향 범위를 넓히지 않은 좋은 사례다.')
b+=P('`components/ui/`는 shadcn CLI가 관리하는 기초 부품 영역이라 손대지 않기로 정해 둔 상태였습니다.','거기엔 디자인뿐 아니라 포커스·키보드·ARIA·열림 상태가 들어 있어서,','잘못 고치면 여러 화면의 접근성과 하이드레이션이 같이 깨질 수 있기 때문입니다.')
b+=IMG(12,'월_12_shadcn_BaseUI기본.png','shadcn/ui 체인지로그 "July 2026 - Base UI as the Default": 새 프로젝트는 Base UI가 기본이고 Radix도 계속 지원된다는 안내',SS)
b+=P('참고로 인터넷의 shadcn 예제 대부분은 **Radix 기반**이라 `asChild`를 씁니다.','shadcn/ui는 2026년 7월부터 **Base UI를 기본**으로 바꿨고(Radix도 계속 지원),','마이그레이션 안내에는 "**`asChild`는 이제 `render`**"라고 적혀 있습니다.','겉모습이 같은 컴포넌트라도 속성을 합치는 방식이 다르니, 예제를 붙이기 전에 어느 기반인지 확인해야 했습니다.')
b+=HR()
b+=H1('5. 정리: 경고를 끄기 전에 확인한 세 가지')
b+=IMG(13,'월_13_정리카드.png','어디서 갈라졌나, 끄는 방법이 맞나, 경로를 없앨 수 있나 — 하이드레이션 경고를 만났을 때 확인한 세 가지 카드')
b+=TABLE(['내가 처음 생각한 것','기록과 공식 문서로 정리한 것'],[
['속성 하나 맞춰 주면 끝','불일치는 버그로 취급하고 원인을 고쳐야 한다. 속성 차이가 보정된다는 보장이 없다 (React)'],
['화면이 멀쩡하면 괜찮다','tabIndex 0이 남으면 키보드 사용자가 가짜 링크에서 멈춘다. 접근성 버그다 (MDN)'],
['Vercel과 localhost에서 스타일이 달라지는 문제','같은 불일치가 두 환경 모두에서 생긴다. 개발 환경은 오류 화면이 더 눈에 띌 뿐이다 (기록)'],
['suppressHydrationWarning으로 끄자','한 단계만 적용되는 비상구다. 서버와 다를 수밖에 없는 값(시각 등)에만 쓴다 (Next.js)'],
['버튼 안에 링크를 끼우면 된다','링크는 자체 의미가 있으니 render로 버튼화하지 말고 a에 CSS를 입혀라 (Base UI)']])
b+=BOX('**확인된 것과 확인되지 않은 것**','확인됨(공식 문서): 하이드레이션 정의와 흔한 원인(Next.js), 불일치는 버그이며 속성 보정은 보장 없음(React), 세 가지 해결책과 suppressHydrationWarning의 한계(Next.js), tabindex 0/-1의 뜻(MDN), 링크를 render로 버튼화하지 말라는 규칙과 nativeButton 기본값(Base UI), Base UI 기본 전환과 asChild→render(shadcn/ui)','확인됨(제 기록): 서버 0 / 브라우저 -1 값 차이, Button→render→병합 경로, Link+buttonVariants와 span aria-disabled로 바꾼 수정, components/common에서만 고친 점','확인 필요: 당시 콘솔 메시지 원문(기록 없음, 위 화면은 재구성). 속성 병합 결과가 서버·브라우저에서 왜 달라졌는지의 내부 원인은 Base UI 쪽을 더 파 보지 않아 적지 않았습니다.')
b+=HR()
b+=H1('알게 된 것')
b+=P('**하이드레이션 경고는 "두 React 트리가 다르다"는 신호였습니다.**','서버가 만든 HTML과 브라우저가 계산한 결과가 어긋났다는 뜻이고,','React는 그걸 알아서 맞춰 주지 않을 수 있습니다.')
b+=P('**증상을 덮는 것과 원인 경로를 지우는 것은 다른 수정이었습니다.**','`suppressHydrationWarning`도, `useEffect` 두 번 렌더도 자리가 따로 있습니다.','페이지 번호처럼 "같아야 하는 값"이 달라졌다면 경로를 봐야 했습니다.')
b+=P('**고치는 위치도 선택이었습니다.**','공용 부품(`components/ui`)은 두고, 그걸 쓰는 쪽(`components/common`)에서 경로를 바꿨습니다.','콘솔이 조용해진 것보다 Tab 이동이 맞게 된 것을 확인 기준으로 삼았습니다.')
b+=HR()
b+=H1('참고자료')
b+=P('[[Next.js 공식 문서 - Text content does not match server-rendered HTML|https://nextjs.org/docs/messages/react-hydration-error]]')
b+=P('[[React 공식 문서 - hydrateRoot|https://react.dev/reference/react-dom/client/hydrateRoot]]')
b+=P('[[React 공식 문서 - Minified React error #418|https://react.dev/errors/418]]')
b+=P('[[Base UI 공식 문서 - Button|https://base-ui.com/react/components/button]]')
b+=P('[[shadcn/ui 체인지로그 - July 2026, Base UI as the Default|https://ui.shadcn.com/docs/changelog/2026-07-base-ui-default]]')
b+=P('[[MDN - tabindex|https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/tabindex]]')
b+=P('#Nextjs #hydration #하이드레이션 #React #shadcn #BaseUI #tabIndex #웹접근성 #AI활용 #개발입문')
import os
PAGE(T,b,os.environ.get('OUT','/home/claude/out/mon/2026-11-16_월_Nextjs_hydration_mismatch.html'))
print('ok')
