from lib import *
# 대표 예시: Notion을 글 저장소로 쓰는 Next.js 16 블로그(notion-blog) — 'use cache'를 켠 뒤 새 글을 즉시 반영하려면 revalidateTag와 updateTag 중 무엇을 어디서 부르나
T="[AI활용] Next.js 16 revalidateTag vs updateTag 차이: 'use cache' 뒤 새 글이 늦게 보이는 이유"
SN1='출처: Next.js 공식 문서 "use cache"(nextjs.org/docs/app/api-reference/directives/use-cache), 2026-11-15 캡처'
SN2='출처: Next.js 공식 문서 "Revalidating"(nextjs.org/docs/app/getting-started/revalidating), 2026-11-15 캡처'
SN3='출처: Next.js 공식 문서 "revalidateTag"(nextjs.org/docs/app/api-reference/functions/revalidateTag), 2026-11-15 캡처'
SR='공식 문서의 예시 형식에 제 프로젝트 구조를 맞춰 다시 쓴 코드 화면 (재구성, 실제 실행 화면 아님)'
b=''
b+=IMG(1,'금_01_썸네일.png','대표 이미지(썸네일)')
b+=P('Notion을 글 저장소로 쓰는 Next.js 16 블로그를 만들면서 캐시를 넣기로 했을 때,','장점 세 개 옆에 단점을 하나 적어 뒀습니다.','"새 글이나 수정 내용이 캐시가 갱신될 때까지 늦게 보일 수 있다."')
b+=P('그 단점을 메우는 함수가 둘입니다. `revalidateTag`와 `updateTag`.','이름이 비슷해서 "둘 중 아무거나 부르면 새 글이 보이겠지"라고 생각하기 쉬운데, 공식 문서를 다시 읽어 보니 **다음 요청이 받는 것**이 다릅니다.')
b+=P('결론부터 적으면,','**==revalidateTag(tag, \'max\')는 "오래됐다"고 표시만 하고, 다음 요청에는 옛 결과를 주면서 뒤에서 새로 만듭니다. updateTag(tag)는 그 자리에서 만료시켜 쓴 사람이 바로 새 글을 봅니다 — 단, Server Action 안에서만.==**','그러니 고르는 기준은 "어느 게 더 좋은가"가 아니라 **무효화 신호가 어디서 오는가**입니다.')
b+=BOX('**이 글의 기준**','확인 날짜: 2026-11-15','근거: Next.js 공식 문서 "use cache"(2026-11-06 갱신), "Revalidating"(2026-06-25 갱신), "revalidateTag"(2026-08-25 갱신), "updateTag"(2026-08-18 갱신), 그리고 2026년 8월에 제 프로젝트를 설계하며 남긴 기록','기준 버전: Next.js 16의 Cache Components(`cacheComponents: true`) 방식입니다. 이전 방식(`unstable_cache`, fetch 옵션)은 다루지 않습니다.','코드 화면은 공식 문서의 예시 형식에 제 프로젝트 구조를 맞춰 **다시 쓴 것**이고, 이번 글을 쓰면서 Next.js 프로젝트를 실제로 돌려 확인하지는 않았습니다. 돌려 보지 않은 부분은 "확인 필요"로 적었습니다.')
b+=HR()
b+=H1('1. 캐시가 끼면 새 글이 늦게 보인다')
b+=IMG(2,'금_02_도식_캐시흐름.png','방문자 → Next.js 서버 → use cache 저장소(태그 posts) → Notion API로 이어지는 읽기 흐름과, 새 글 저장이 revalidateTag 또는 updateTag로 저장소의 posts 태그를 겨냥하는 구조를 그린 도식')
b+=P('예시는 Notion을 글 저장소로 쓰는 블로그입니다.','글 목록 페이지가 열릴 때마다 Notion API를 부르면 느리고 호출량도 늘어서, 한 번 읽은 결과를 캐시에 두고 다시 씁니다.')
b+=P('설계 기록에 적어 둔 장점은 셋이었습니다. "페이지가 빠르다", "Notion API 호출량이 줄어든다", "Notion이 잠시 장애여도 기존 글을 제공할 수 있다."','단점은 하나. "**새 글이나 수정 내용이 캐시가 갱신될 때까지 늦게 보일 수 있다.**"')
b+=P('그래서 캐시는 "넣을까 말까"가 아니라 "**누가, 언제, 어떻게 만료시키나**"를 같이 정해야 하는 물건입니다.','이 글은 그 "어떻게"의 두 함수를 비교합니다.')
b+=HR()
b+=H1("2. 'use cache'는 선언이다")
b+=IMG(3,'금_03_공식문서_use_cache.png','Next.js 공식 문서 use cache의 Usage: next.config.ts에 cacheComponents: true를 켜고, 함수·컴포넌트·파일 수준에 use cache를 적는다. 캐시되는 함수와 컴포넌트는 async여야 한다',SN1)
b+=P('공식 문서의 첫 문장이 범위를 정합니다. "**`use cache`는 Cache Components 기능이다. 켜려면 `next.config.ts`에 `cacheComponents` 옵션을 넣어라.**"','그다음 "**함수, 컴포넌트, 파일 수준에 `use cache`를 적는다. 캐시되는 함수와 컴포넌트는 async여야 한다.**"')
b+=P('즉 `\'use cache\'`는 무엇을 하는 호출이 아니라 "이 결과는 캐시 대상"이라는 **선언**입니다.','선언만 하고 아무 설정도 안 하면 기본 프로필이 적용됩니다. 문서에 따르면 default 프로필은 stale 5분, revalidate 15분, expire 없음입니다.')
b+=P('제 프로젝트에서는 처음에 `unstable_cache`를 쓸 생각이었습니다. 실제 확인 결과 Next.js 16 Cache Components에서는 `use cache`를 쓰는 것으로 정리됐고, 기록에는 이렇게 남아 있습니다.','"`unstable_cache`를 유지하면 당장의 구조 변경은 적지만 나중에 `use cache`로 다시 옮겨야 한다. 이 프로젝트는 장기적으로 맞는 Next.js 16 방식을 선택해 `use cache`, `Suspense`, `generateStaticParams` 도입 시점을 앞당겼다."')
b+=HR()
b+=H1('3. cacheLife는 시간, cacheTag는 이름표')
b+=IMG(4,'금_04_공식문서_cacheLife.png','Next.js 공식 문서 Revalidating의 cacheLife 프로필 표: default(5m/15m/never), seconds, minutes, hours, days, weeks, max(5m/30d/1y)와 stale·revalidate·expire를 숫자로 넘기는 객체 예시',SN2)
b+=P('무효화 함수로 가기 전에 두 보조 함수를 갈라 둡니다. 둘은 **서로 다른 축**입니다.')
b+=P('**`cacheLife(프로필)`은 시간**입니다. 캐시를 얼마나 오래 쓸지 정합니다.','표의 `max` 프로필은 stale 5분, revalidate 30일, expire 1년. "시간으로는 거의 안 바뀐다"는 선언에 가깝습니다.','**`cacheTag(이름)`은 이름표**입니다. 나중에 "이 묶음만 골라서" 무효화하려고 붙입니다.')
b+=P('같은 문서의 "무엇을 캐시해야 하나" 절이 제 경우를 거의 그대로 적어 놓았습니다.','"**시간 기반 갱신이 필요 없는 콘텐츠, 예를 들어 CMS에서 오는 데이터는 `cacheTag`와 `max` 같은 긴 `cacheLife`를 써서 정적 셸에 두어라. 콘텐츠 소스가 바뀔 때 웹훅 같은 알림으로 `revalidateTag`를 부르도록 구성하라.**"','Notion이 제 CMS이니, 글 목록은 `cacheLife(\'max\')` + `cacheTag(\'posts\')`가 됩니다.')
b+=HR()
b+=H1('4. revalidateTag vs updateTag — 다음 요청이 받는 것')
b+=IMG(5,'금_05_공식문서_revalidateTag.png','Next.js 공식 문서 Revalidating의 revalidateTag 절: stale-while-revalidate 의미로 태그별 캐시를 무효화하며, 옛 콘텐츠를 즉시 주고 새 콘텐츠는 뒤에서 읽는다. Server Action이나 Route Handler에서 부른다. 두 번째 인자는 옛 콘텐츠를 얼마나 오래 줄 수 있는지이며 max가 가장 긴 창',SN2)
b+=P('`revalidateTag`의 정의는 이렇습니다.','"**`revalidateTag`는 stale-while-revalidate 의미로 태그별 캐시 항목을 무효화한다 — 옛 콘텐츠를 즉시 주고, 그동안 새 콘텐츠를 뒤에서 읽는다. 업데이트가 조금 늦어도 되는 콘텐츠, 예를 들어 블로그 글이나 상품 목록에 알맞다.**"','부르는 자리는 "**Server Action 또는 Route Handler**".')
b+=P('두 번째 인자의 뜻도 적혀 있습니다. "**두 번째 인자는 새 콘텐츠를 뒤에서 만드는 동안 옛 콘텐츠를 얼마나 오래 줄 수 있는지 정한다. 그 시간이 지나면 이후 요청은 새 콘텐츠가 준비될 때까지 막힌다. `\'max\'`가 가장 긴 창을 준다.**"')
b+=IMG(6,'금_06_공식문서_updateTag.png','Next.js 공식 문서 Revalidating의 updateTag 절: read-your-own-writes 상황을 위해 캐시를 즉시 만료시키며 Server Action에서만 쓸 수 있다. createPost 예시와 updateTag/revalidateTag의 Where·Behavior·Use case 비교표',SN2)
b+=P('`updateTag`는 반대쪽입니다.','"**`updateTag`는 read-your-own-writes 상황을 위해 캐시된 데이터를 즉시 만료시킨다 — 사용자가 옛 콘텐츠 대신 자기 변경을 바로 본다. `revalidateTag`와 달리 Server Action 안에서만 쓸 수 있다.**"')
b+=P('문서의 비교표를 옮기면 이렇습니다.')
b+=TABLE(['','updateTag','revalidateTag'],[
['어디서 (Where)','Server Action에서만','Server Action과 Route Handler'],
['동작 (Behavior)','캐시를 즉시 만료','stale-while-revalidate (옛것을 주면서 뒤에서 갱신)'],
['쓰임 (Use case)','read-your-own-writes — 쓴 사람이 자기 변경을 본다','뒤에서 새로고침 — 조금 늦어도 괜찮을 때']])
b+=P('문서 예시가 두 함수의 성격을 잘 보여 줍니다.','`updateTag` 예시는 `createPost` — 글을 만들고 `updateTag(\'posts\')`를 부른 뒤 **방금 만든 글 페이지로 redirect**합니다. 쓴 사람이 바로 자기 글을 봐야 하니 즉시 만료가 필요합니다.','`revalidateTag` 예시는 `updateUser` — 데이터를 바꾸고 `revalidateTag(\'user\', \'max\')`. 주석에 "권장: stale-while-revalidate"라고 적혀 있습니다.')
b+=HR()
b+=H1('5. 제 프로젝트에 놓으면 — 읽기 한 곳, 무효화 두 곳')
b+=IMG(7,'금_07_코드_재구성.png','notion-blog 프로젝트 구조에 맞춰 다시 쓴 코드: lib/notion.ts의 getPosts에 use cache·cacheLife(max)·cacheTag(posts), app/admin/actions.ts의 Server Action에서 updateTag(posts), app/api/revalidate/route.ts의 Route Handler에서 x-revalidate-secret 헤더를 REVALIDATE_SECRET과 비교한 뒤 revalidateTag(posts, max)',SR)
b+=P('공식 문서의 예시 형식에 제 프로젝트 구조를 맞춰 다시 쓰면 위와 같습니다. 파일이 셋입니다.')
b+=CODE('''// lib/notion.ts — 읽기: 결과를 캐시 대상으로 선언하고, 수명과 이름표를 붙인다
import { cacheLife, cacheTag } from 'next/cache'

export async function getPosts() {
  'use cache'            // 이 함수의 결과를 캐시한다 (async 필수)
  cacheLife('max')       // 시간으로는 거의 안 바뀐다고 선언 (CMS 글)
  cacheTag('posts')      // 나중에 이 이름표로 골라서 무효화
  return notion.queryPublishedPosts()
}''',[("'use cache'",'#ffd43b'),('cacheLife','#8ce99a'),('cacheTag','#8ce99a')])
b+=P('**읽기는 한 곳**입니다. `getPosts`에 `\'use cache\'`를 선언하고, `cacheLife(\'max\')`로 "시간으로는 안 바뀐다", `cacheTag(\'posts\')`로 "posts라는 이름표"를 붙입니다.','`cacheLife`와 `cacheTag`는 `\'use cache\'` 범위 안에서 부릅니다.')
b+=P('**무효화는 두 곳**입니다.','① 관리자 화면의 Server Action(`app/admin/actions.ts`)에서 저장 직후 `updateTag(\'posts\')`. 저장한 사람이 바로 자기 글을 봐야 하니 즉시 만료.','② 외부 자동화가 "발행 끝났다"고 알려 오는 Route Handler(`app/api/revalidate/route.ts`)에서 `revalidateTag(\'posts\', \'max\')`. 여기서는 `updateTag`를 쓸 수 없습니다. `updateTag` 참조 문서의 예시는 Route Handler에서 부르면 "**updateTag can only be called from within a Server Action**" 오류가 난다고 적고, "Route Handler, Client Component, 그 밖의 어떤 문맥에서도 쓸 수 없다"고 못 박습니다.')
b+=P('②에 `REVALIDATE_SECRET`이 등장합니다. 설계할 때 이 값의 역할을 한참 오해했고, 바로잡은 문장을 기록에 그대로 남겼습니다.','"**`REVALIDATE_SECRET`은 새 글을 임시로 담는 공간이 아니다. 외부에서 `/api/revalidate`를 호출할 때 \'이 요청이 진짜 관리자나 자동화 시스템에서 왔는가?\'를 확인하는 비밀번호다.**"')
b+=P('그래서 Route Handler의 첫 줄이 비밀번호 대조입니다. 헤더의 값이 서버 환경변수와 다르면 401로 거부하고, 같을 때만 `revalidateTag`를 부릅니다.','기록의 운영 원칙도 같이 옮깁니다. "Vercel 환경변수에 한 번 등록한다", "`NEXT_PUBLIC_` 접두사를 붙이면 브라우저에 노출될 수 있으므로 절대 붙이지 않는다", "관리자 페이지에서 매번 사람이 입력하게 만들 필요는 없다", 그리고 "**관리자 페이지의 Server Action이 서버 내부에서 직접 `updateTag()`를 호출하면 외부 비밀값 입력 자체가 필요 없을 수 있다.**"')
b+=P('마지막 문장이 ①과 ②의 관계입니다. 같은 서버 안에서 부르는 ①은 비밀번호가 필요 없고, 바깥에서 두드리는 ②만 문지기가 필요합니다.')
b+=HR()
b+=H1('6. "불렀는데 왜 아직 옛 글이지?" — 갱신은 요청이 촉발한다')
b+=IMG(8,'금_08_공식문서_갱신동작.png','Next.js 공식 문서 revalidateTag의 Revalidation Behavior: revalidateTag는 태그 데이터를 stale로 표시하고, 다음 요청이 갱신을 시작하며 그동안 옛 콘텐츠를 준다. profile=max(권장), 다른 프로필·객체, {expire: 0}, 두 번째 인자 없음(deprecated)의 네 경우와 "갱신은 revalidateTag 호출이 아니라 요청이 촉발한다"는 Good to know',SN3)
b+=P('`revalidateTag` 참조 문서의 "Revalidation Behavior" 절이 오해를 풀어 줍니다.','"**`revalidateTag`를 부르면 그 태그의 데이터가 stale로 표시된다. 그 데이터에 대한 다음 요청이 갱신을 시작하고, 갱신이 도는 동안 옛 콘텐츠를 받는다.**"')
b+=P('두 번째 인자의 네 경우도 정리돼 있습니다.','**`profile="max"` (권장)**: 1년짜리 창. 갱신이 도는 동안 요청은 항상 옛 콘텐츠를 받는다.','**다른 프로필이나 객체**: 다른 창을 원할 때.','**`{ expire: 0 }`**: "**옛 콘텐츠를 절대 주지 않으므로 다음 요청은 막히는 갱신(캐시 미스)이 된다. 호출자가 데이터를 즉시 없애야 하는데 `updateTag`를 쓸 수 없을 때 쓴다.**"','**두 번째 인자 없음 (deprecated)**: `{ expire: 0 }`처럼 동작한다. Server Action이면 `updateTag`로, 아니면 `profile="max"`로 옮겨라.')
b+=P('그리고 Good to know 한 줄.','"**갱신은 `revalidateTag` 호출이 아니라 요청이 촉발한다. 그래서 그 태그를 쓰는 페이지들은 한꺼번에가 아니라 방문될 때 각각 갱신된다.**"','"불렀는데 왜 아직 옛 글이지?"가 버그가 아니라 설계대로일 수 있다는 뜻입니다. `\'max\'`로 불렀다면 다음 방문자는 옛 목록을 받고, 그 다음 방문자부터 새 목록을 봅니다.')
b+=IMG(9,'금_09_공식문서_RouteHandler.png','Next.js 공식 문서 revalidateTag의 Route Handler 예시: GET 요청의 tag 쿼리를 읽어 revalidateTag(tag, max)를 부른다. 웹훅처럼 Server Action 바깥에서 올 때 updateTag는 쓸 수 없으니 즉시 만료가 필요하면 revalidateTag(tag, { expire: 0 })',SN3)
b+=P('Route Handler 예시 아래에 제 ②번 상황이 그대로 적혀 있습니다.','"**무효화가 Server Action 바깥에서 올 때, 예를 들어 웹훅이나 다른 서비스가 Route Handler를 부를 때는 `updateTag`를 쓸 수 없다. 데이터를 즉시 만료시키려면 `{ expire: 0 }`을 넘겨라.**"','그러니 ②에서도 "옛 목록을 잠깐 보여 줘도 되나"에 따라 `\'max\'`와 `{ expire: 0 }` 중 하나를 고르게 됩니다.')
b+=IMG(10,'금_10_도식_시간표.png','새 글 저장 직후 들어온 요청이 무엇을 보는지 세 호출로 나눈 시간표: updateTag는 다음 요청이 새로 읽는 동안 기다린 뒤 새 글을 보고, revalidateTag(max)는 다음 요청이 옛 결과를 받으며 뒤에서 갱신한 뒤 그 다음 요청부터 새 글, revalidateTag({expire: 0})는 다음 요청이 기다린 뒤 새 글')
b+=P('공식 문서의 설명을 시간순으로 옮기면 위와 같습니다.','`updateTag`와 `{ expire: 0 }`은 다음 요청이 **기다렸다가 새 글**을 보고, `\'max\'`는 다음 요청이 **옛것을 즉시** 받고 그 다음 요청부터 새 글을 봅니다.','(이 시간표는 문서의 설명을 옮긴 것이고, 제 프로젝트에서 요청 간격을 재 보지는 않았습니다. 확인 필요.)')
b+=HR()
b+=H1('7. 신호가 오는 곳이 함수를 정한다')
b+=IMG(11,'금_11_결정카드.png','무효화 신호가 어디서 오는지로 함수를 고르는 결정 카드: ① 관리자 화면의 Server Action → updateTag, ② 웹훅·외부 자동화의 Route Handler → revalidateTag(max 또는 expire 0), ③ 신호 없음 → cacheLife 프로필. REVALIDATE_SECRET은 ②의 문지기')
b+=TABLE(['무효화 신호가 오는 곳','부르는 함수','이유'],[
['같은 서버 안의 Server Action (관리자 화면 저장)','`updateTag(\'posts\')`','쓴 사람이 바로 자기 글을 봐야 한다. Server Action에서만 가능'],
['바깥에서 Route Handler로 (웹훅·외부 자동화)','`revalidateTag(\'posts\', \'max\')`','옛 목록을 잠깐 더 보여 줘도 되면. 호출자는 REVALIDATE_SECRET을 들고 온다'],
['바깥에서 오는데 즉시 비워야 할 때','`revalidateTag(\'posts\', { expire: 0 })`','Route Handler에서는 updateTag를 쓸 수 없으므로'],
['아무도 알려 주지 않을 때','`cacheLife(\'hours\')` 같은 프로필','신호가 없으면 프로필의 revalidate 주기가 유일한 갱신 수단']])
b+=P('표의 첫 열이 질문입니다. 함수 이름을 외우는 대신 "**이 무효화 신호는 어디서 오나**"를 먼저 적으면 둘째 열은 따라옵니다.','그리고 네 번째 줄 — 아무 신호도 없는 경우 — 를 잊으면 `cacheLife(\'max\')`를 선언한 글 목록은 누가 만료시켜 줄 때까지 그대로입니다.')
b+=HR()
b+=H1('8. 정리')
b+=IMG(12,'금_12_정리카드.png','선언(use cache), 수명(cacheLife), 이름표(cacheTag), 무효화(revalidateTag vs updateTag), 갱신은 요청이 촉발한다 — 공식 문서 네 쪽을 한 장으로 모은 카드')
b+=TABLE(['내가 처음 생각한 것','공식 문서로 정리한 것'],[
['revalidateTag와 updateTag는 이름만 다른 같은 기능','revalidateTag는 stale 표시 후 옛것을 주며 뒤에서 갱신, updateTag는 즉시 만료. 다음 요청이 받는 것이 다르다'],
['어디서든 편한 쪽을 부르면 된다','updateTag는 Server Action에서만. Route Handler·웹훅에서는 revalidateTag뿐이고, 즉시 비우려면 { expire: 0 }'],
['revalidateTag를 부르면 그 자리에서 새로 만든다','갱신은 요청이 촉발한다. 태그를 쓰는 페이지는 방문될 때 각각 갱신된다'],
['REVALIDATE_SECRET은 새 글을 임시로 담는 공간','외부 호출이 진짜인지 확인하는 비밀번호. 서버 안에서 updateTag를 부르면 외부 비밀값이 필요 없을 수 있다'],
['인자 하나짜리 revalidateTag(tag)면 충분','deprecated. { expire: 0 }처럼 동작하므로 \'max\' 프로필이나 updateTag로 옮긴다']])
b+=BOX('**확인된 것과 확인되지 않은 것**','확인됨(공식 문서): `use cache`는 `cacheComponents: true`가 필요하고 캐시되는 함수는 async여야 한다는 것, cacheLife 프로필 표(default 5m/15m/never, max 5m/30d/1y), revalidateTag의 stale-while-revalidate 정의와 호출 위치(Server Action·Route Handler), updateTag의 즉시 만료와 Server Action 한정, 두 번째 인자의 네 경우와 "갱신은 요청이 촉발한다", 인자 하나짜리 호출의 deprecated, CMS 데이터에는 cacheTag + 긴 cacheLife + 웹훅으로 revalidateTag를 권한다는 것','확인됨(제 기록): 캐시의 장단점, unstable_cache 대신 use cache를 고른 결정, REVALIDATE_SECRET의 역할과 운영 원칙','확인 필요: 이번 글의 코드 화면은 재구성이며 실제로 빌드·실행하지 않았습니다. updateTag 직후 다음 요청이 실제로 얼마나 기다리는지, \'max\'로 불렀을 때 뒤의 갱신이 끝나는 데 걸리는 시간은 제 프로젝트에서 재 보지 않았습니다. 문서는 serverless 환경에서 메모리 캐시가 갱신 사이에 유지되지 않을 수 있다고도 적는데, 이 부분도 확인하지 못했습니다.')
b+=HR()
b+=H1('알게 된 것')
b+=P('**두 함수의 차이는 "무엇을 무효화하나"가 아니라 "다음 요청이 무엇을 받나"였습니다.**','같은 posts 태그를 겨냥해도, revalidateTag는 옛것을 주며 뒤에서 갱신하고 updateTag는 기다렸다가 새것을 줍니다.','그래서 신호가 오는 곳 — 같은 서버 안의 Server Action인지, 바깥의 Route Handler인지 — 가 함수를 정합니다.')
b+=P('**REVALIDATE_SECRET은 데이터가 아니라 문지기였습니다.**','설계 초반에 "새 글을 담아 두는 값"쯤으로 생각했던 걸 기록으로 바로잡아 두길 잘했습니다.','바깥에서 두드리는 문에만 자물쇠가 필요하고, 안에서 부르는 updateTag에는 필요 없습니다.')
b+=HR()
b+=H1('참고자료')
b+=P('[[Next.js 공식 문서 - use cache|https://nextjs.org/docs/app/api-reference/directives/use-cache]]')
b+=P('[[Next.js 공식 문서 - Revalidating (cacheLife, cacheTag, revalidateTag, updateTag)|https://nextjs.org/docs/app/getting-started/revalidating]]')
b+=P('[[Next.js 공식 문서 - revalidateTag|https://nextjs.org/docs/app/api-reference/functions/revalidateTag]]')
b+=P('[[Next.js 공식 문서 - updateTag|https://nextjs.org/docs/app/api-reference/functions/updateTag]]')
b+=P('#Nextjs #Nextjs16 #usecache #revalidateTag #updateTag #cacheTag #cacheLife #캐시무효화 #Notion블로그 #AI활용 #개발입문')
import os
PAGE(T,b,os.environ.get('OUT','/home/claude/out/fri/2026-11-20_금_Nextjs_revalidateTag_vs_updateTag.html'))
print('ok')
