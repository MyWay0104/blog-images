from lib import *
# 대표 예시: 독서 노트 앱. 백엔드 FastAPI(8000), 프론트 Vite+React(개발 5173), 빌드 결과 frontend/dist, API /api/notes
T='[AI활용] FastAPI StaticFiles로 프론트까지 한 포트에서 서빙하기: 폴더를 나눴다고 CORS가 나는 게 아니다'
b=''
b+=IMG(1,'수_01_썸네일.png','대표 이미지(썸네일)')
b+=P('백엔드는 FastAPI, 화면은 Vite+React로','독서 노트 앱을 설계하다가','이런 문장을 받았습니다.')
b+=P('"FastAPI가 정적 파일을 함께 서빙해서','컨테이너 1개, 동일 origin.','CORS 설정과 로그인 쿠키 문제가','처음부터 사라진다."')
b+=P('저는 이 문장의 뜻을 몰라서','저장소를 `frontend/`, `backend/`로 나누면','그 자체로 CORS가 나는 줄 알았는데요.')
b+=P('**==CORS는 폴더 개수가 아니라==**','**==브라우저가 보는 주소(origin) 개수로 결정==**된다는 걸','알고 나니 배포 구조가 한 번에 납득됐습니다.')
b+=BOX('**이 글의 기준**','확인 날짜: 2026-10-18','근거: FastAPI 공식 문서(CORS, Static Files), Starlette 공식 문서(Routing), Vite 공식 문서(server.proxy), Python 공식 문서(asyncio)','이 구성을 제가 실제로 배포해 본 후기가 아니라, 설계 중에 개념을 정리하고 공식 문서로 확인한 글입니다. 실제 배포 환경의 제약은 따로 확인이 필요합니다.','예시는 독서 노트 앱으로 통일했습니다. 백엔드 8000번, Vite 개발 서버 5173번')
b+=HR()
b+=H1('처음에 제가 헷갈렸던 것')
b+=Q('일단 배포 구조: FastAPI가 정적 파일을 함께 서빙(StaticFiles 마운트)해서 컨테이너 1개, 동일 origin. CORS 설정과 로그인 쿠키 공유 문제가 처음부터 사라집니다.','위 말이 어떤 걸 의미하는 건지 알려줘.')
b+=Q('루트폴더 자체를 frontend\\ , backend\\로 구성한 뒤에 바로 배포하면 CORS 문제가 발생한다는 말이니?','내가 FastAPI를 넣으려는 이유 - 첫 번째, 백과 프론트의 분리로 운영/유지/보수 난이도 낮춤 + 두 번째, 비동기 방식으로 agent 동작 시간 단축인데 이게 무슨 상관이 있는건지 상세하게 알려줘.')
b+=BOX('**당시의 오해**','저장소를 `frontend/`, `backend/` 폴더로 나누면 그 자체로 CORS 문제가 생기는 줄 알았다.','"분리"는 배포 단위(컨테이너)의 분리라고 생각해서, 같은 컨테이너에 올리면 분리의 이점이 사라지는 게 아닌가 싶었다.','"비동기로 agent가 빨라진다"는 말을 들었지만 왜 빨라지는지, 분리와 무슨 상관인지 연결이 안 됐다.')
b+=HR()
b+=H1('1. CORS는 주소(origin)가 몇 개인가의 문제')
b+=IMG(2,'수_02_FastAPI_CORS_origin.png','FastAPI 공식 문서의 origin 정의와 예시','출처: FastAPI 공식 문서 (CORS), 2026-10-18 캡처')
b+=P('FastAPI 문서의 정의는 이렇습니다.','origin은 "**프로토콜(http, https), 도메인, 포트의 조합**"이고,','`http://localhost`, `https://localhost`, `http://localhost:8080`은','"**전부 localhost지만 프로토콜이나 포트가 달라서 다른 origin**"입니다.')
b+=P('그리고 문서의 Steps 절에 따르면','브라우저가 `localhost:8080`에서 받은 화면이','`localhost:80`의 백엔드를 부르려 하면,','백엔드가 "허용 origin 목록"에','`http://localhost:8080`을 넣어 둬야 통과합니다.')
b+=IMG(3,'수_03_origin_개수.png','브라우저가 보는 주소가 둘일 때와 하나일 때의 차이 도식')
b+=P('즉 CORS가 생기는 조건은 하나입니다.')
b+=BOX('**CORS 발생 조건**','브라우저가 HTML을 받은 주소와, 그 HTML 안의 JavaScript가 API를 호출하는 주소가 다르면 생긴다.','폴더가 몇 개인지, 저장소가 몇 개인지는 상관없다.')
b+=P('같은 컨테이너라도','프론트 서버(3000번)와 uvicorn(8000번)이','**프로세스 2개로 따로 뜨면** origin이 둘이라 생깁니다.')
b+=P('반대로 uvicorn 하나가 API와 정적 파일을','**둘 다 내주면** origin이 하나라 생길 수가 없습니다.','쿠키도 마찬가지입니다.','쿠키는 발급된 호스트에만 자동으로 붙으니','주소가 하나면 로그인 쿠키 문제도 같이 사라집니다.')
b+=HR()
b+=H1('2. uvicorn 하나로 끝내는 구조')
b+=IMG(4,'수_04_단일_컨테이너.png','uvicorn 하나가 /api와 frontend/dist를 함께 서빙하는 구조 도식')
b+=P('월요일 글에서 본 것처럼','Vite+React의 빌드 결과물은','`frontend/dist/` 폴더 하나입니다.','이 폴더를 FastAPI가 내주면 됩니다.')
b+=IMG(5,'수_05_FastAPI_StaticFiles.png','FastAPI 공식 문서의 StaticFiles 마운트 설명','출처: FastAPI 공식 문서 (Static Files), 2026-10-18 캡처')
b+=P('FastAPI 문서는 `app.mount(...)`를','"**마운트란 특정 경로에 완전히 독립된 애플리케이션을 붙이는 것이고,**','**그 아래 모든 하위 경로를 그 앱이 처리한다**"고 설명합니다.')
b+=CODE('''from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# /api/... 경로는 로직 (라우터들). 먼저 등록한다.
app.include_router(notes_router, prefix="/api")

# 나머지 경로는 frontend/dist 폴더의 정적 파일을 그대로 내준다.
# html=True: 폴더 요청("/")에 index.html을 돌려준다.
app.mount("/", StaticFiles(directory="frontend/dist", html=True), name="static")''',[('include_router','#f783ac'),('app.mount','#f783ac'),('StaticFiles','#ffd43b'),('html=True','#ffd43b')])
b+=P('첫 블록은 FastAPI와 `StaticFiles`를 불러옵니다.','`include_router` 줄이 `/api/...` 경로의 로직을 등록합니다.','마지막 줄이 `/` 아래 **모든 경로**를','`frontend/dist` 폴더로 보냅니다.')
b+=P('`html=True`는 Starlette 문서에 따르면','"**HTML 모드로 실행. 폴더에 `index.html`이 있으면 자동으로 불러온다**"는 옵션입니다.','그래서 `/`를 열면 `index.html`이 나옵니다.')
b+=IMG(6,'수_06_등록_순서.png','라우터를 먼저 등록하고 StaticFiles를 나중에 마운트해야 하는 이유 도식')
b+=P('**순서가 중요합니다.**','Starlette 라우팅 문서는','"**들어온 경로는 각 Route에 순서대로 대조된다**"고 하고,','"더 구체적인 경로를 일반적인 경로보다 앞에 두라"고 합니다.')
b+=P('`/`에 마운트한 정적 파일은 가장 일반적인 경로라서','먼저 등록하면 `/api/...`까지 가로챕니다.','그래서 **라우터 먼저, 마운트 나중**입니다.','(FastAPI의 `mount`도 같은 순서 규칙을 따른다는 것은','Starlette 문서에서 따라온 제 추론입니다. 확인 필요)')
b+=H2('개발할 때는 주소가 둘로 갈린다')
b+=P('빌드하기 전, 집에서 개발할 때는','Vite 개발 서버(5173번)와 uvicorn(8000번)이','따로 뜹니다.','이때는 origin이 둘이라 CORS가 생깁니다.')
b+=IMG(7,'수_07_Vite_proxy.png','Vite 공식 문서의 server.proxy 설명과 예시','출처: Vite 공식 문서 (Server Options - server.proxy), 2026-10-18 캡처')
b+=P('Vite 문서의 `server.proxy`는','"**요청 경로가 그 키로 시작하면 지정한 대상으로 프록시한다**"는 옵션입니다.','문서 예시는 `\'/foo\': \'http://localhost:4567\'`이고,','`localhost:5173/foo`가 `localhost:4567/foo`로 넘어갑니다.')
b+=CODE('''// frontend/vite.config.js — 개발 중에만 쓰는 설정
export default {
  server: {
    proxy: { "/api": "http://localhost:8000" }  // /api/* 는 FastAPI로 전달
  }
}''',[('proxy','#f783ac'),('"/api"','#ffd43b')])
b+=P('브라우저는 5173번만 봅니다.','`/api/notes` 요청은 Vite가 뒤에서 8000번으로 넘깁니다.','그래서 개발 중에도 CORS 설정 없이 돌아갑니다.','배포할 때는 이 설정이 필요 없습니다.','uvicorn 하나가 다 내주니까요.')
b+=HR()
b+=H1('3. "분리"는 컨테이너가 아니라 책임의 분리')
b+=P('여기서부터는 공식 문서가 아니라','설계하면서 **제가 정리한 판단**입니다.')
b+=P('제가 원한 "백과 프론트의 분리"는','배포 단위를 나누는 게 아니었습니다.','**백엔드는 "입력을 주면 JSON을 돌려준다"는 계약만 책임지고**','**화면을 모른다**는 것이었습니다.')
b+=P('이 분리는 컨테이너가 하나여도 그대로 성립합니다.','프론트를 바꿔도 백엔드는 안 바뀌고,','같은 API를 테스트 스크립트나 다른 도구도 부를 수 있고,','화면 없이 API만으로 정확도를 잴 수 있습니다.')
b+=TABLE(['"분리"의 두 가지 뜻','무엇을 나누나','컨테이너 1개에서'],[
['배포 단위 분리','프론트 서버와 백엔드 서버를 따로 띄움','사라짐 (안 나눔)'],
['책임 분리','백엔드는 JSON 계약만, 화면은 프론트만','**그대로 성립**']])
b+=HR()
b+=H1('4. 비동기는 "기다리는 시간을 겹치는 것"')
b+=P('두 번째 질문, "비동기로 agent가 빨라진다"는 말의 뜻입니다.')
b+=P('독서 노트 앱에서 추천을 만들려면','독서 기록, 책 정보, 메모, 리뷰','네 군데서 데이터를 가져온다고 해 보겠습니다.','순서대로 하면 네 번 기다리고,','동시에 시작하면 **가장 느린 하나만큼만** 기다립니다.')
b+=P('Python 문서의 `asyncio.gather`는','"**awaitable 객체들을 동시에(concurrently) 실행한다**"는 함수입니다.')
b+=CODE('''import asyncio

async def collect_context(member_id: str, book_id: str):
    # 네 조회를 동시에 시작하고 전부 끝날 때까지 기다린다
    history, book, notes, reviews = await asyncio.gather(
        fetch_reading_history(member_id),
        fetch_book_info(book_id),
        fetch_notes(book_id),
        fetch_reviews(book_id),
    )
    return history, book, notes, reviews''',[('asyncio.gather','#f783ac'),('async def','#74c0fc'),('await','#74c0fc')])
b+=P('`gather` 안의 네 호출이 동시에 시작됩니다.','효과는 **I/O 대기가 긴 작업이 여러 개일 때만** 납니다.','CPU 계산 구간에서는 겹칠 대기 시간이 없습니다.')
b+=H2('함정: async def만 붙이면 비동기가 아니다')
b+=IMG(8,'수_08_Python_to_thread.png','Python 공식 문서의 asyncio.to_thread 설명과 예시','출처: Python 공식 문서 (asyncio - Coroutines and Tasks), 2026-10-18 캡처')
b+=P('Python 문서는 `asyncio.to_thread`를','"**함수를 별도 스레드에서 비동기로 실행한다**"고 하고,','"**그대로 부르면 이벤트 루프를 막을 I/O 작업**에 쓰라"고 합니다.')
b+=P('문서의 예시 설명이 핵심입니다.','"코루틴 안에서 `blocking_io()`를 직접 부르면','**그 시간 동안 이벤트 루프가 막힌다**".')
b+=IMG(9,'수_09_동기_호출_함정.png','async def 안에서 동기 함수를 그대로 부를 때와 to_thread로 감쌀 때의 시간 흐름 비교 도식')
b+=P('`requests`나 동기 DB 라이브러리를','`async def` 안에서 그냥 호출하면','그 호출이 끝날 때까지 **서버 전체가 멈춥니다**.','`gather`로 네 개를 묶어도 하나씩 차례로 돕니다.')
b+=CODE('''async def fetch_notes(book_id: str):
    sql = NOTES_SQL.format(book_id=book_id)
    # 동기 DB 라이브러리를 별도 스레드에서 실행하고 결과만 await
    # 이 줄이 있어야 gather가 실제로 겹친다. 빼면 서버 전체가 멈춘다.
    return await asyncio.to_thread(db.execute_sql, sql)''',[('asyncio.to_thread','#f783ac'),('await','#74c0fc')])
b+=P('`to_thread`에 동기 함수와 인자를 넘기면','별도 스레드에서 돌고 결과만 `await`로 받습니다.','이 한 줄을 빼면','"비동기로 짰는데 왜 느리지"가 됩니다.')
b+=P('(위 코드는 설계안이고,','제 환경에서 시간을 재 본 것은 아닙니다. 확인 필요)')
b+=HR()
b+=H1('정리')
b+=IMG(10,'수_10_요약_카드.png','CORS, 분리, 비동기 세 가지의 핵심 문장 요약 카드')
b+=BOX('**외워 둘 문장 셋**','CORS는 폴더 구조가 아니라 브라우저가 보는 주소(origin)의 개수 문제다. 배포 전에 "주소창에 뭐가 보일까"를 먼저 그린다.','"분리"는 배포 단위 분리와 책임 분리를 구분한다. 내가 원한 건 후자였고, 후자는 컨테이너 개수와 무관하다.','비동기의 어려움은 `async`를 붙이는 게 아니라, 내가 쓰는 라이브러리가 동기인지 아는 것이다.')
b+=P('결정을 닫기 직전에','"이 문장이 무슨 뜻인지"를 확인하고 넘어간 덕분에','단일 컨테이너 구성이 왜 그렇게 되는지 납득할 수 있었습니다.')
b+=HR()
b+=H2('참고자료')
b+=P('[[FastAPI 공식 문서 - CORS|https://fastapi.tiangolo.com/tutorial/cors/]]','[[FastAPI 공식 문서 - Static Files|https://fastapi.tiangolo.com/tutorial/static-files/]]','[[Starlette 공식 문서 - StaticFiles (html 옵션)|https://www.starlette.io/staticfiles/]]','[[Starlette 공식 문서 - Routing (순서 규칙)|https://www.starlette.io/routing/]]','[[Vite 공식 문서 - server.proxy|https://vite.dev/config/server-options.html#server-proxy]]','[[Python 공식 문서 - asyncio.gather, asyncio.to_thread|https://docs.python.org/3/library/asyncio-task.html]]','(모두 2026-10-18 확인)')
b+=P('#FastAPI #StaticFiles #CORS #origin #Vite #proxy #asyncio #to_thread #비동기 #AI활용')
PAGE(T,b,'/home/claude/out3/wed/2026-10-21_수_FastAPI_StaticFiles_CORS.html')
