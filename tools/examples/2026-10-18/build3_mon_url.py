from lib import *
# 대표 예시: 독서 노트 앱. 프론트 폴더 frontend/, 빌드 결과 frontend/dist, API /api/notes/{book_id}
T='[AI활용] Vite+React vs Next.js 차이: "정적 웹인데 SPA"가 말이 되는 이유'
b=''
b+=IMG(1,'월_01_썸네일.png','대표 이미지(썸네일)')
b+=P('Python으로 백엔드를 만들다가','화면이 필요해져서 프론트엔드를 알아보면','이런 문장을 만나게 됩니다.')
b+=P('"정적 파일로 빌드한 SPA를 FastAPI가 서빙한다."')
b+=P('저는 이 문장에서 세 번 멈췄습니다.','정적인데 SPA라니, 서로 모순 아닌가?','Vite와 React는 한 묶음인가, 대체재인가?','그럼 Next.js는 어디에 들어가는 거지?')
b+=P('**==정적/동적과 화면이 바뀌는 것은 다른 축==**이라는 걸','알고 나서야 전부 풀렸는데요.','그 과정을 공식 문서 기준으로 정리해 보겠습니다.')
b+=BOX('**이 글의 기준**','확인 날짜: 2026-10-18','근거: MDN 웹 문서(정적·동적 사이트, SPA 용어집), Vite 공식 가이드, Next.js 공식 문서(CLI, Deploying)','Vite+React와 Next.js를 둘 다 운영해 본 후기가 아니라, 공식 자료로 구조를 비교한 글입니다.','예시는 독서 노트 앱으로 통일했습니다.')
b+=HR()
b+=H1('처음에 제가 헷갈렸던 것')
b+=P('프로젝트 설계 메모에','"복잡해지면 Next.js가 아니라 Vite+React 빌드로 간다"고','적어 두고도 그 뜻을 몰라서 물었습니다.')
b+=Q('정적 SPA가 무슨 뜻이야? 복잡해지면 next.js가 아니라 vite+react 빌드로 넘어간다고 명시해뒀는데, vite와 react는 어떤 기술스택이고 왜 선택한건지?')
b+=P('설명을 듣고도 다시 멈췄습니다.')
b+=Q('잠시만.. 첫 번째 케이스에서 서버가 파일을 만들지 않는다.. 라는 말을 보면, 기존에 동적 웹에서는 그럼 next.js가 일일이 사용자의 피드백에 따라서 html 파일 자체를 계속 바꿔가면서 실행한다는 말이야?','내가 이거 정적/동적 차이를 정확하게 구분이 잘 안되는데 내가 모르는 개념조차 뭔지 잘 모르겠거든. 차근차근 다시 설명해줄래?')
b+=P('당시 제 머릿속은 이랬습니다.')
b+=BOX('**당시의 오해**','"정적"이면 화면이 안 바뀌고, "동적"이면 화면이 바뀌는 것이라고 뭉뚱그려 생각했다.','"동적 웹"이면 서버가 사용자 입력마다 HTML 파일 자체를 고쳐 쓰는 줄 알았다.','Vite, React, Next.js가 서로 대체재인지 한 묶음인지 구분이 안 됐다.')
b+=P('이 오해를 하나씩 풀어 보겠습니다.')
b+=HR()
b+=H1('1. 정적/동적은 "서버가 무엇을 하느냐"의 문제')
b+=P('MDN의 서버 사이드 입문 문서에','정의가 분명하게 적혀 있습니다.')
b+=IMG(2,'월_02_MDN_정적_동적.png','MDN의 정적 사이트와 동적 사이트 설명','출처: MDN Web Docs (Introduction to the server side), 2026-10-18 캡처')
b+=P('정적 사이트는 "**특정 자원을 요청할 때마다**','**서버에서 같은 하드코딩된 내용을 돌려주는 것**"이고,')
b+=P('동적 사이트는 "**응답 내용의 일부가**','**필요할 때 동적으로 생성되는 것**"입니다.')
b+=P('그러니까 기준은 **서버**입니다.','디스크에 있는 `index.html`, `app.js`를','그대로 복사해서 보내면 정적,','요청이 올 때마다 HTML을 새로 조립하면 동적입니다.')
b+=IMG(3,'월_03_정적_동적_도식.png','정적(복사)과 동적(조립)의 차이 도식')
b+=P('제가 "동적이면 HTML 파일 자체를 고쳐 쓰는 건가"라고','물었던 건 반은 맞고 반은 틀렸습니다.','디스크의 파일을 고치는 게 아니라','**응답을 만들 때 메모리에서 조립**해서 보내고,','파일은 그대로 남습니다.')
b+=P('이 정의 어디에도','"화면이 바뀌는가"는 나오지 않습니다.','그게 다음 축입니다.')
b+=HR()
b+=H1('2. SPA는 "브라우저 안에서" 일어나는 일')
b+=IMG(4,'월_04_MDN_SPA.png','MDN 용어집의 SPA 정의','출처: MDN Web Docs (Glossary: SPA), 2026-10-18 캡처')
b+=P('MDN 용어집의 정의는 이렇습니다.')
b+=P('SPA는 "**하나의 웹 문서만 불러온 뒤,**','**다른 내용을 보여줘야 할 때**','**Fetch 같은 JavaScript API로**','**그 문서의 본문을 갱신하는 방식**"입니다.')
b+=P('핵심은 **페이지를 새로 불러오지 않는다**는 것입니다.','HTML 파일은 한 장이고,','화면 전환은 JavaScript가','같은 페이지 안에서 일부를 지우고 다시 그립니다.','데이터는 `/api/...`로 JSON만 받아옵니다.')
b+=P('그러면 "정적 파일 + SPA"는 모순이 아닙니다.')
b+=BOX('**두 축을 나눠서 보기**','축 1 (서버): HTML을 복사해 주느냐(정적) / 조립해 주느냐(동적)','축 2 (브라우저): 화면이 JS로 바뀌느냐(SPA) / 페이지를 새로 불러오느냐','"정적 SPA" = 서버는 파일을 복사만 하고, 브라우저가 JS로 화면을 바꾸는 조합. 가장 흔한 형태다.')
b+=H2('"HTML"이라고 부르는 것이 사실 두 개')
b+=P('제가 진짜 몰랐던 건 용어가 아니라 이것이었습니다.')
b+=IMG(5,'월_05_HTML_두개.png','디스크의 HTML 파일과 브라우저 메모리의 DOM을 구분한 도식')
b+=P('하나는 **디스크에 있는 `index.html` 파일**입니다.','서버가 복사해서 보내는 그것이고,','SPA에서는 한 번 받으면 끝입니다.')
b+=P('다른 하나는 **브라우저 메모리에 펼쳐진 문서(DOM)**입니다.','JavaScript가 지우고 다시 그리는 건 이쪽입니다.','파일은 안 바뀌는데 화면은 바뀌는 이유가 이것입니다.')
b+=P('이 둘을 분리하는 순간 나머지가 풀렸습니다.')
b+=H2('이해한 뒤 제 말로 정리해 본 것')
b+=Q('아.. 오케이 이해했다. 그럼 js랑 ts 같은 언어들은 말 그대로 정해진 스크립트(대본)대로 돌면서 사용자의 입력에 따른 api 반환값을 돌려줄 수 있도록 시나리오를 미리 짜두는거지?')
b+=P('이 정리에는 한 군데 교정이 들어갔습니다.','브라우저의 JS는 Python 스크립트처럼','위에서 아래로 한 번 흐르고 끝나는 "대본"이 아니라','**이벤트에 반응하는 방식**이라는 점입니다.')
b+=CODE('''// 페이지가 열릴 때 한 번 실행된다.
// "검색 버튼이 눌리면 이 함수를 실행하라"고 등록만 해 둔다.
document.getElementById("search").addEventListener("click", async () => {
    const bookId = document.getElementById("book").value;   // 사용자가 입력한 책 ID
    const res = await fetch(`/api/notes/${bookId}`);         // 서버에 JSON 요청
    const data = await res.json();
    render(data);                                            // 화면(DOM)에 그리기
});
// 여기서 스크립트가 "끝나는" 게 아니라 대기 상태로 들어간다.
// 클릭이 올 때마다 위 함수가 실행된다.''',[('addEventListener','#2dd4bf'),('fetch','#2dd4bf'),('async','#ffd43b'),('await','#ffd43b'),('const','#74c0fc')])
b+=P('첫 줄에서 버튼에 함수를 **등록**합니다.','`fetch`로 `/api/notes/책ID`에 JSON을 요청하고,','받은 데이터를 `render`로 화면에 그립니다.','페이지(HTML 파일)는 그대로인데','화면만 바뀌는 것이 이 코드입니다.')
b+=HR()
b+=H1('3. Vite와 React는 한 묶음, Next.js는 다른 층')
b+=P('이제 세 이름을 제자리에 놓을 수 있습니다.')
b+=TABLE(['이름','공식 소개 (요지)','하는 일'],[
['React','"웹과 네이티브 사용자 인터페이스를 위한 라이브러리". 컴포넌트라는 조각으로 UI를 만든다.','**화면을 그리는 라이브러리**. 브라우저에서 DOM을 바꾸는 쪽'],
['Vite','"빌드 도구". 네이티브 ES 모듈 기반 개발 서버 + 코드를 번들하는 빌드 명령','**개발 서버 + 빌드 도구**. React 코드를 브라우저가 읽는 파일로 만든다'],
['Next.js','React 기반 풀스택 프레임워크. `next dev`, `next build`, `next start` 명령 제공','**프레임워크**. 라우팅·서버 렌더링까지 포함하고 Node.js 서버로 실행']])
b+=P('즉 **Vite+React는 한 묶음**입니다.','React가 화면을 그리고, Vite가 그 코드를 빌드합니다.','Next.js는 React 위에 서버까지 얹은 **다른 층의 선택지**입니다.')
b+=H2('Vite 빌드의 결과물은 폴더 하나')
b+=IMG(6,'월_06_Vite_build_dist.png','Vite 공식 가이드의 빌드와 미리보기 설명','출처: Vite 공식 문서 (Deploying a Static Site), 2026-10-18 캡처')
b+=P('Vite 가이드는 이렇게 적습니다.','`npm run build`를 실행하면','"**기본적으로 빌드 결과물은 `dist`에 놓이고,**','**이 `dist` 폴더를 원하는 어느 플랫폼에나 배포할 수 있다**".')
b+=P('그리고 `npm run preview`는','"`dist`의 파일을 서빙하는 **로컬 정적 웹 서버**를 띄운다"고 합니다.')
b+=P('그러니까 Vite+React의 결과물은','**HTML, JS, CSS 파일이 든 폴더**입니다.','누가 서빙하든 상관없습니다.','Python 백엔드가 그대로 내줘도 됩니다.')
b+=CODE('''frontend/src/*.jsx  ──(npm run build)──▶  frontend/dist/
                                           ├ index.html
                                           └ assets/*.js, *.css
                                        └── 이게 "정적 파일". 서버는 복사만 한다''',[('npm run build','#2dd4bf'),('frontend/dist/','#ffd43b')])
b+=H2('Next.js는 서버가 딸려 온다')
b+=IMG(7,'월_07_Nextjs_배포옵션.png','Next.js 공식 문서의 배포 옵션 표','출처: Next.js 공식 문서 (Deploying), 2026-10-18 캡처')
b+=P('Next.js 공식 문서의 배포 옵션은','**Node.js 서버, Docker 컨테이너, 정적 내보내기, 어댑터** 네 가지입니다.','기능 지원은 Node.js 서버와 Docker가 "All",','정적 내보내기는 "Limited"입니다.')
b+=P('Node.js 서버 항목에는','`npm run build`로 빌드하고 `npm run start`로','"**Node.js 서버를 시작한다**"고 적혀 있습니다.','즉 기본 형태는 **서버 프로세스가 따로 뜨는 것**입니다.')
b+=IMG(8,'월_08_Nextjs_static_export.png','Next.js 정적 내보내기의 제한 설명','출처: Next.js 공식 문서 (Deploying - Static export), 2026-10-18 캡처')
b+=P('정적 내보내기도 됩니다.','"HTML/CSS/JS 정적 자산을 서빙할 수 있는','어느 웹 서버에나 배포할 수 있다"고 하면서도,','"**서버가 필요한 Next.js 기능은 지원하지 않는다**"고 적혀 있습니다.')
b+=P('정리하면 Next.js는','**서버 기능을 쓰려고 고르는 도구**이고,','서버 기능을 안 쓰면 정적 파일만 남습니다.')
b+=HR()
b+=H1('4. 그래서 FastAPI가 있으면 Vite+React')
b+=IMG(9,'월_09_구조_비교.png','Vite+React와 Next.js를 FastAPI 백엔드와 함께 놓았을 때의 프로세스 구조 비교')
b+=P('여기서부터는 공식 문서가 아니라 **제 판단**입니다.')
b+=P('독서 노트 앱의 백엔드가 이미 FastAPI라면,','화면 쪽에 필요한 건 **정적 파일 폴더 하나**입니다.','Vite+React의 `dist`를 FastAPI가 서빙하면','프로세스는 하나로 끝납니다.')
b+=P('Next.js를 고르면 Node.js 서버가 하나 더 뜹니다.','그 서버가 해 주는 일(서버 렌더링, API 라우트, 데이터 가져오기)은','FastAPI가 이미 하고 있는 일과 겹칩니다.')
b+=P('즉 선택 기준은 "어느 쪽이 더 널리 쓰이는가"가 아니라','**==서버 쪽 일을 누가 이미 하고 있는가==**입니다.')
b+=IMG(10,'월_10_선택기준_요약.png','상황별 선택 기준 요약 카드')
b+=TABLE(['상황','고르는 쪽','이유'],[
['백엔드가 이미 FastAPI(또는 다른 Python 서버)','Vite+React','결과물이 정적 폴더라 그 서버가 그대로 서빙. 프로세스 1개'],
['서버 렌더링, 파일 기반 라우팅, Node.js 서버를 직접 쓸 계획','Next.js','그 기능들이 프레임워크에 들어 있음. Node.js 서버 필요'],
['화면이 한두 장이고 상태가 단순','순수 HTML + JS','React도 과할 수 있음 (제 판단)']])
b+=P('개발할 때는 Vite 개발 서버(기본 5173번 포트)와','FastAPI(8000번)가 따로 뜨므로','주소가 둘로 갈립니다.','이때 생기는 CORS 문제는','이번 주 수요일 글에서 따로 다루겠습니다.')
b+=HR()
b+=H1('정리')
b+=BOX('**외워 둘 문장 하나**','정적/동적은 서버가 HTML을 복사하느냐 조립하느냐의 문제이고, 브라우저 안에서 화면이 바뀌는 것은 별개의 층이다.')
b+=P('"HTML"은 디스크의 파일과 브라우저의 DOM, **두 개**입니다.','SPA는 파일은 그대로 두고 DOM만 바꿉니다.','Vite+React는 그 파일 묶음을 만들고,','Next.js는 거기에 서버를 얹습니다.')
b+=P('한 번 설명을 듣고 "알겠다"고 넘어가지 않고','**내가 모르는 개념이 뭔지 모르겠다**고 되물은 게','이번에 가장 잘한 일이었습니다.','그 질문이 "HTML이 두 개"라는 설명을 끌어냈습니다.')
b+=HR()
b+=H2('참고자료')
b+=P('[[MDN - Introduction to the server side (Static sites / Dynamic sites)|https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/First_steps/Introduction]]','[[MDN Glossary - SPA|https://developer.mozilla.org/en-US/docs/Glossary/SPA]]','[[Vite - Getting Started|https://vite.dev/guide/]]','[[Vite - Deploying a Static Site|https://vite.dev/guide/static-deploy.html]]','[[Vite - Server Options (server.port 기본값 5173)|https://vite.dev/config/server-options.html]]','[[React 공식 사이트|https://react.dev/]]','[[Next.js - CLI (next dev / build / start)|https://nextjs.org/docs/app/api-reference/cli/next]]','[[Next.js - Deploying|https://nextjs.org/docs/app/getting-started/deploying]]','(모두 2026-10-18 확인)')
b+=P('#Vite #React #Nextjs #SPA #정적웹 #동적웹 #FastAPI #프론트엔드입문 #AI활용')
PAGE(T,b,'/home/claude/out3/mon/2026-10-19_월_Vite_React_vs_Nextjs_이미지주소포함.html')
