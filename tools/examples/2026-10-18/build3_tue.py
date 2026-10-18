from lib import *
# 대표 예시: 독서 노트 앱. Streamlit은 app.py, FastAPI는 main.py, Next.js는 app/page.tsx. 포트 3000
T='[AI활용] npm run dev vs build 차이: Streamlit만 쓰던 사람이 Next.js에서 헷갈린 것'
b=''
b+=IMG(1,'화_01_썸네일.png','대표 이미지(썸네일)')
b+=P('Streamlit으로 화면을 만들 때는','`uv run streamlit run app.py` 한 줄이면','브라우저가 열리고 끝이었습니다.')
b+=P('Next.js 프로젝트를 받아서','`npm run build`를 쳤더니','아무것도 안 뜨길래 한참 헤맸는데요.')
b+=P('알고 보니 **==build는 "실행"이 아니라 "변환"==**이었고,','`streamlit run`의 짝은 `npm run dev`였습니다.')
b+=P('왜 그런지 공식 문서 기준으로 정리해 보겠습니다.')
b+=BOX('**이 글의 기준**','확인 날짜: 2026-10-18','근거: npm 공식 문서(npm run-script), Next.js 공식 문서(CLI, Project Structure, Deploying), Streamlit 공식 문서(streamlit run), uv 공식 문서(Running commands)','환경: Windows, Node.js와 npm이 설치된 상태. Next.js App Router 기준','예시는 독서 노트 앱으로 통일했습니다.')
b+=HR()
b+=H1('처음에 제가 헷갈렸던 것')
b+=Q('streamilt에서는 uv run streamlit run ~~.py 로 실행을 했었는데, next.js + React 구조에서는 npm run build 같은 걸로 진행을 했었거든.','나는 next.js 기반 프로젝트가 \'진입점\'이 없다는 게 너무 어색했다.','next run ~.py 처럼 실행하면 localhost가 뜨면서 웹이 구동되는 줄 알았는데, npm run build 처럼 왜 스트림릿이랑 차이가 나는지 궁금해.')
b+=P('당시 제 머릿속은 이랬습니다.')
b+=BOX('**당시의 오해**','`npm run build`가 `streamlit run`처럼 "실행하면 localhost가 뜨는" 명령이라고 생각했다.','Streamlit의 `app.py`, FastAPI의 `main.py`처럼 "여기서 시작한다"는 파일이 Next.js에는 없다고 느꼈다.','`uv run`과 `npm run`이 이름이 비슷해서 같은 종류의 명령이라고 여겼다.')
b+=P('세 가지를 하나씩 풀어 보겠습니다.')
b+=HR()
b+=H1('1. npm run은 "별칭 실행", uv run은 "환경 안에서 실행"')
b+=P('이름이 비슷해서 같은 명령인 줄 알았는데','하는 일이 다릅니다.')
b+=IMG(2,'화_02_npm_run_script.png','npm 공식 문서의 npm run-script 설명','출처: npm 공식 문서 (npm-run-script), 2026-10-18 캡처')
b+=P('npm 문서는 이렇게 적습니다.','"**패키지의 `scripts` 객체에 적힌 임의의 명령을 실행한다.**','**명령을 안 주면 사용 가능한 스크립트 목록을 보여준다.**"')
b+=P('즉 `npm run dev`는','`package.json`의 `scripts` 안에서','`dev`라는 이름을 찾아 그 줄을 실행하는 것입니다.','`dev`가 무엇을 하는지는 **그 줄에 적힌 내용**이 정합니다.')
b+=CODE('''// package.json — Next.js 공식 문서(Deploying)에 나온 기본 모양
{
  "scripts": {
    "dev":   "next dev",
    "build": "next build",
    "start": "next start"
  }
}''',[('"dev"','#ff922b'),('"build"','#ff922b'),('"start"','#ff922b')])
b+=P('그러니까 `npm run dev`는 사실 `next dev`이고,','`npm run build`는 `next build`입니다.','진짜 질문은 "**`next dev`와 `next build`가 뭐가 다른가**"였습니다.')
b+=P('반면 uv 문서의 `uv run`은','"**프로젝트 환경 안에서 명령을 실행**"하고,','"실행 전에 프로젝트 환경이 최신인지 보장한다"고 합니다.','가상환경을 활성화하는 수고를 대신해 주는 것이지,','별칭을 찾아 주는 게 아닙니다.')
b+=TABLE(['명령','하는 일 (공식 문서)','비유'],[
['`uv run X`','프로젝트 가상환경 안에서 X를 실행','"이 방 안에서 X를 해라"'],
['`npm run X`','`package.json`의 `scripts.X`에 적힌 줄을 실행','"X라는 메모를 펴서 그대로 해라"']])
b+=HR()
b+=H1('2. dev는 실행, build는 변환, start는 운영 실행')
b+=IMG(3,'화_03_Nextjs_CLI_명령.png','Next.js 공식 문서의 CLI 명령 표','출처: Next.js 공식 문서 (next CLI), 2026-10-18 캡처')
b+=P('Next.js CLI 문서의 설명은 이렇습니다.')
b+=TABLE(['명령','공식 문서 설명 (요지)','무엇이 뜨나'],[
['`next dev`','개발 모드로 Next.js를 시작. 저장하면 바로 반영(Hot Module Reloading), 오류 표시','**개발 서버가 뜸** (기본 3000번 포트)'],
['`next build`','"애플리케이션의 최적화된 프로덕션 빌드를 만든다. 각 라우트 정보를 표시한다"','**아무것도 안 뜸.** 결과물 폴더(`.next/`)만 생김'],
['`next start`','"프로덕션 모드로 Next.js를 시작. 먼저 `next build`로 컴파일되어 있어야 한다"','**운영 서버가 뜸** (기본 3000번 포트)']])
b+=P('제가 `npm run build`를 치고 기다린 건','"변환만 하는 명령"을 "실행 명령"으로 착각한 것이었습니다.')
b+=P('Streamlit 쪽과 비교하면 이렇습니다.')
b+=IMG(4,'화_04_Streamlit_run.png','Streamlit 공식 문서의 streamlit run 설명','출처: Streamlit 공식 문서 (streamlit run), 2026-10-18 캡처')
b+=P('Streamlit 문서는 `streamlit run`을','"**이 명령은 Streamlit 앱을 시작한다**"고 한 줄로 설명합니다.','빌드 단계에 해당하는 명령은 문서에 따로 없습니다.')
b+=IMG(5,'화_05_실행_변환_도식.png','dev(실행), build(변환), start(운영 실행) 세 명령의 역할 도식')
b+=P('정리하면 세 명령은 이렇게 갈립니다.')
b+=BOX('**세 명령의 역할**','`npm run dev` = 실행. 코드를 고치면서 보는 개발 서버. `streamlit run`의 짝.','`npm run build` = 변환. 브라우저가 읽을 파일로 바꿔 `.next/`에 저장. 화면은 안 뜸.','`npm run start` = 운영 실행. 변환된 결과물로 서버를 띄움. 코드를 고쳐도 반영 안 됨 (다시 build 필요).')
b+=P('문서에는 작은 주의도 있습니다.','개발 빌드는 `.next/dev`에 저장되어','`next dev`와 `next build`를 **동시에 돌려도 충돌하지 않는다**고 합니다.')
b+=H2('왜 Streamlit에는 빌드가 없을까')
b+=P('여기서부터는 공식 문서로 확인한 것이 아니라','**제가 이해한 설명**입니다.')
b+=P('브라우저가 읽을 수 있는 건 HTML, CSS, JavaScript뿐입니다.','Next.js에서 제가 쓰는 코드(TypeScript, JSX)는','**브라우저로 가는 코드**라서 한 번 변환이 필요합니다.','그 변환이 `build`입니다.')
b+=P('Streamlit에서 제가 쓰는 `app.py`는','**서버에서 Python으로 그대로 실행**되고,','브라우저 쪽 화면은 패키지 안에','이미 변환된 상태로 들어 있다고 이해했습니다.','(Streamlit 소스나 문서로 확인하지는 않았습니다. 확인 필요)')
b+=HR()
b+=H1('3. 진입점은 사라진 게 아니라 폴더 규칙으로 옮겨 갔다')
b+=P('"`app.py` 같은 시작 파일이 없다"는 느낌의 정체입니다.')
b+=IMG(6,'화_06_Nextjs_폴더_주소.png','Next.js 공식 문서의 폴더 경로와 URL 대응표','출처: Next.js 공식 문서 (Project structure - Nested routes), 2026-10-18 캡처')
b+=P('Next.js 프로젝트 구조 문서는 이렇게 적습니다.','"**폴더가 URL 구간을 정의한다.**','**`page` 또는 `route` 파일이 있을 때 그 경로가 공개된다.**"')
b+=P('그리고 표에 따르면','`app/layout.tsx`는 "모든 경로를 감싸는 루트 레이아웃",','`app/page.tsx`는 주소 `/`의 공개 경로입니다.')
b+=P('즉 진입점이 없는 게 아니라','**`app/page.tsx`가 첫 화면**이고,','**`app/layout.tsx`가 공통 뼈대**입니다.','다만 "이 파일을 실행하라"고 제가 지정하는 게 아니라','**정해진 이름과 위치에 두면 프레임워크가 찾아 갑니다.**')
b+=IMG(7,'화_07_진입점_비교.png','파일 하나로 지정하는 진입점과 폴더 규칙으로 정해지는 진입점의 비교 도식')
b+=TABLE(['도구','진입점을 정하는 방식','독서 노트 앱이라면'],[
['Streamlit','실행할 파일을 명령에 적는다','`streamlit run app.py`'],
['FastAPI','`모듈:객체`를 명령에 적는다','`uvicorn main:app --reload`'],
['Next.js','정해진 위치의 파일을 프레임워크가 찾는다','`app/page.tsx` → 주소 `/`, `app/notes/page.tsx` → 주소 `/notes`']])
b+=P('FastAPI도 사실 비슷한 구조였습니다.','`uvicorn`이 `main.py`의 `app` 객체를 찾아 실행하니까요.','Next.js는 그 **`app` 객체를 만드는 일까지**','프레임워크가 가져간 것이라고 이해했습니다. (제 이해)')
b+=HR()
b+=H1('4. 세 도구의 명령 대응표')
b+=IMG(8,'화_08_명령_대응표.png','Streamlit, FastAPI, Next.js의 개발 실행·빌드·운영 실행 명령 대응 카드')
b+=TABLE(['하는 일','Streamlit','FastAPI','Next.js'],[
['개발 중 실행','`uv run streamlit run app.py`','`uv run uvicorn main:app --reload`','`npm run dev`'],
['배포용 결과물 생성','없음','없음','`npm run build`'],
['운영 실행','`streamlit run app.py`','`uvicorn main:app`','`npm run start`']])
b+=P('표를 보면 Python 쪽 두 도구에는','"배포용 결과물 생성" 칸이 비어 있습니다.','**이 칸이 비어 있어서 "빌드"라는 단계가 낯설었던 것**입니다.')
b+=HR()
b+=H1('5. 직접 확인하는 순서')
b+=P('명령 세 개를 순서대로 치면서','무엇이 뜨고 무엇이 안 뜨는지 확인해 보면 정리가 됩니다.')
b+=IMG(9,'화_09_확인_순서.png','npm run dev → build → start 순서로 확인하는 흐름도')
b+=CODE('''npm run dev     # 1. 개발 서버. 브라우저에서 http://localhost:3000 확인
npm run build   # 2. 변환. 터미널에 라우트 목록이 찍히고 .next/ 폴더가 생김. 화면은 안 뜸
npm run start   # 3. 운영 서버. 다시 http://localhost:3000''',[('npm run dev','#ff922b'),('npm run build','#ff922b'),('npm run start','#ff922b')])
b+=P('1번에서 `app/page.tsx`의 글자를 바꿔 저장하면','브라우저가 바로 바뀌는지 봅니다.','2번은 끝나도 아무것도 안 뜨는 게 정상입니다.','3번에서는 글자를 바꿔도 반영되지 않습니다.')
b+=IMG(10,'화_10_npm_run_dev_예시.png','npm run dev 직후 터미널 화면을 재구성한 예시. Local 주소 줄에 표시','실제 캡처가 아니라 공식 문서의 설명을 바탕으로 재구성한 예시 화면입니다. 버전에 따라 문구가 다를 수 있습니다.')
b+=IMG(11,'화_11_npm_run_build_예시.png','npm run build 직후 터미널 화면을 재구성한 예시. 라우트 목록과 .next 폴더','실제 캡처가 아니라 공식 문서(next build의 라우트 출력 예시)를 바탕으로 재구성한 예시 화면입니다.')
b+=P('문제가 생겼을 때도 이 순서가 유용합니다.','`dev`는 되는데 `build`가 실패하면','첫 실패 지점은 빌드입니다.','`build`는 되는데 `start`에서 안 보이면','빌드 결과물이나 포트 쪽을 봅니다.')
b+=BOX('**주의할 점**','`npm run`으로 CLI 옵션을 넘길 때는 `npm run dev -- -p 4000`처럼 `--`를 넣어야 npm이 옵션을 `next`에 전달합니다. (Next.js CLI 문서의 안내)','`next start`는 `next build` 없이 실행하면 안 됩니다. 문서에 "먼저 컴파일되어 있어야 한다"고 적혀 있습니다.','포트는 `-p` 옵션이나 `PORT` 환경변수로 바꿉니다. `PORT`는 `.env`에 넣어도 적용되지 않는다고 문서에 적혀 있습니다.')
b+=HR()
b+=H1('정리')
b+=BOX('**외워 둘 문장 둘**','`npm run build`는 실행이 아니라 변환이다. `streamlit run`의 짝은 `npm run dev`다.','진입점은 사라진 게 아니라 "파일 하나"에서 "폴더 규칙"으로 옮겨 갔다. `app/page.tsx`가 첫 화면이다.')
b+=P('"빌드"라는 단계가 낯설었던 뿌리는','**브라우저는 HTML, CSS, JS만 읽는다**는 사실이었습니다.','그 외의 소스는 반드시 한 번 변환돼야 하고,','Python 쪽에서는 그 변환을 체감할 일이 없었던 것입니다.')
b+=HR()
b+=H2('참고자료')
b+=P('[[npm 공식 문서 - npm run-script|https://docs.npmjs.com/cli/v10/commands/npm-run-script]]','[[Next.js 공식 문서 - next CLI|https://nextjs.org/docs/app/api-reference/cli/next]]','[[Next.js 공식 문서 - Project structure|https://nextjs.org/docs/app/getting-started/project-structure]]','[[Next.js 공식 문서 - Deploying (package.json scripts)|https://nextjs.org/docs/app/getting-started/deploying]]','[[Streamlit 공식 문서 - streamlit run|https://docs.streamlit.io/develop/api-reference/cli/run]]','[[uv 공식 문서 - Running commands in projects|https://docs.astral.sh/uv/concepts/projects/run/]]','(모두 2026-10-18 확인)')
b+=P('#Nextjs #npmrundev #npmrunbuild #Streamlit #packagejson #진입점 #프론트엔드입문 #AI활용')
PAGE(T,b,'/home/claude/out3/tue/2026-10-20_화_npm_run_dev_vs_build.html')
