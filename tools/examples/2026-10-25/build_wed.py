from lib import *
# 대표 예시: 도서관 홈페이지 "신착 도서" 페이지를 순회해 Obsidian 노트로 저장하는 작업. 슬래시 커맨드 이름 /crawl, raw 폴더 raw/
T='[AI활용] Playwright MCP vs Playwright 라이브러리 차이: 크롤링하면 빠지는 것들'
SRC_PW='출처: Playwright 공식 문서, 2026-10-25 캡처'
SRC_GH='출처: microsoft/playwright-mcp 공식 저장소 README, 2026-10-25 캡처'
b=''
b+=IMG(1,'수_01_썸네일.png','대표 이미지(썸네일)')
b+=P('Claude Code에 Playwright MCP를 붙여서','웹 페이지 여러 개를 차례로 돌며','내용을 Obsidian 노트로 저장하고 있었습니다.')
b+=P('그러다 문득 불안해졌습니다.','**중요한 정보가 빠지고 있는 건 아닐까?**')
b+=P('물어보니 답이 예상과 달랐습니다.','MCP와 Python 라이브러리의 차이는','"도구 개수"가 아니라','**==결과를 누가 받느냐==**였습니다.')
b+=P('이 글은 그 차이가 뭔지,','스냅샷에서 실제로 뭐가 빠지는지 직접 확인하고,','그래서 제가 어떤 규칙을 정했는지 적은 기록입니다.')
b+=BOX('**이 글의 기준**','확인 날짜: 2026-10-25','근거: Playwright 공식 문서 (Python 라이브러리 사용법, Page API), Playwright MCP 공식 문서 (Introduction, Snapshots), microsoft/playwright-mcp 저장소 README','"빠지는 것" 목록 중 ①~⑤는 샌드박스에서 Playwright를 실제로 실행해 확인했고, 나머지는 추론으로 표시했습니다.','예시는 도서관 홈페이지의 "신착 도서" 페이지로 통일했습니다. 지난 글(Playwright MCP 작동 원리)의 후속입니다.')
b+=HR()
b+=H1('처음에 제가 헷갈렸던 것')
b+=Q('그럼 웹 크롤링을 할 때 이 플레이라이트가 놓치기 싀운 정보는 어떤거야?')
b+=Q('mcp랑 파이선스크립트에서 직접 라이브러리로 사용할 때랑 다르다는거네?','mcp 플레이라이트에 붙어있는 tool이 라이브러리 전체에 있는 기능을 담지 못해서 그런건가')
b+=Q('그렇구만. 지금 여러가지 정보가 있는 웹을 순차적으로 돌면서','플레이라이트 엠시피로 옵시디언에 정보저장하고 있는데','중요한 정보가 빠질까봐 물어봒어')
b+=BOX('**당시의 오해**','MCP와 라이브러리의 차이는 MCP 쪽에 노출된 tool 개수가 적어서 생기는 거라고 생각했다.','이미 Claude Code에 MCP를 붙여 두었으니, 별도 Python 스크립트를 만드는 것보다 프롬프트로 주의사항을 주는 게 빠르겠다고 판단했다.')
b+=HR()
b+=H1('1. 같은 Playwright, 두 가지 쓰임새')
b+=IMG(2,'수_02_공식문서_라이브러리사용법.png','Playwright Python 공식 문서의 라이브러리 사용 예시',SRC_PW)
b+=P('Playwright는 원래 **라이브러리**입니다.','공식 문서의 최소 예시는 이렇습니다.')
b+=CODE('''from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://playwright.dev")
    print(page.title())
    browser.close()''',[('sync_playwright','#ff6b6b'),('page.goto','#ff6b6b'),('page.title()','#ff6b6b')])
b+=P('`sync_playwright()`로 Playwright를 시작하고,','`chromium.launch()`로 브라우저를 띄우고,','`new_page()`로 탭을 하나 열고,','`goto()`로 주소에 가서 `title()`로 제목을 받습니다.')
b+=P('여기서 중요한 건 마지막 줄입니다.','`page.title()`의 결과가 **제 Python 변수**로 옵니다.','`page.content()`를 부르면','문서대로 "**doctype을 포함한 페이지의 전체 HTML**"이 옵니다.')
b+=P('반면 **Playwright MCP**는','이 라이브러리를 LLM이 쓸 수 있게 감싼 서버입니다.','LLM이 `browser_click` 같은 도구를 부르면','서버가 브라우저를 움직이고 결과를 돌려줍니다.')
b+=HR()
b+=H1('2. 차이는 도구 개수가 아니라 결과가 가는 곳')
b+=IMG(3,'수_03_결과가_가는_곳.png','라이브러리와 MCP에서 같은 click의 결과가 각각 어디로 가는지 비교한 도식')
b+=P('제 첫 가설은 "MCP 도구가 적어서"였습니다.','부분적으로는 맞습니다.','라이브러리의 API 수백 개를 전부 노출하지는 않으니까요.')
b+=IMG(4,'수_04_공식문서_KeyFeatures.png','Playwright MCP 공식 문서의 Key Features: 70개 이상의 도구',SRC_PW)
b+=P('그런데 공식 문서를 보니','"**Full automation — 탐색, 폼, 네트워크 모킹, 스토리지, 트레이싱, 비디오 등을 다루는 70개 이상의 도구**"라고 되어 있습니다.','도구가 적어서 생기는 문제가 아니었습니다.')
b+=P('진짜 차이는 **결과가 가는 곳**입니다.')
b+=TABLE(['','라이브러리','MCP'],[
['누가 부르나','내 Python 코드','LLM'],
['결과가 어디로','**내 코드의 변수** (원본 그대로)','**LLM의 컨텍스트** (접근성 스냅샷)'],
['저장은 누가','코드가 파일·DB에 저장','LLM이 읽고 요약해서 저장'],
['다음 동작은','코드에 적힌 대로 (결정론)','LLM이 판단 (비결정론)'],
['맞는 용도','크롤링, 배치, 파이프라인','탐색, 테스트, 에이전트 조작']])
b+=P('MCP에서 LLM이 받는 것은','지난 글에서 본 **접근성 스냅샷**입니다.','DOM에서 의미만 남긴 요약본이죠.')
b+=P('**==압축이 들어가는 순간 크롤링용 정보가 빠집니다.==**','그리고 빠진 것은 LLM도 모르니까','"다 저장했다"고 보고하게 됩니다.')
b+=HR()
b+=H1('3. 실제로 뭐가 빠지는지 확인해 봤다')
b+=P('말로만 하면 불안해서','도서관 "신착 도서" 페이지를 하나 만들고','Playwright로 접근성 스냅샷을 찍어 HTML과 비교했습니다.')
b+=IMG(5,'수_05_실제실행_빠진것.png','신착 도서 페이지의 HTML과 접근성 스냅샷을 나란히 두고 빠진 부분을 표시한 화면','샌드박스에서 Playwright(Python)의 aria_snapshot()으로 실제 실행한 결과')
b+=P('결과는 이랬습니다.')
b+=TABLE(['HTML에 있던 것','스냅샷에서는'],[
['`data-book-id="1001"`, `data-isbn="…"`','**없음.** 글자가 아닌 속성값은 사라짐'],
['`class="badge-green"` (초록 배지)','**없음.** "대출 가능" 글자만 남고 색은 모름'],
['`<details>` 안의 접힌 안내문','**없음.** 제목 "도서관 이용 안내"만 남음'],
['`display:none`인 탭 내용','**없음.** 화면에 없으면 트리에도 없음'],
['`<button><img src="star.png">`','`button` 아래 `img`만. **무슨 버튼인지 모름**'],
['`<a href="/book/1001">`','링크 이름과 `/url`은 남음']])
b+=IMG(6,'수_06_빠지기쉬운것_카드.png','접근성 스냅샷에서 빠지기 쉬운 것 6가지 요약 카드')
b+=P('정리하면 **글자는 남고 나머지는 빠집니다.**','속성값, 접힌 내용, 숨겨진 요소, 시각 정보, 아이콘 버튼의 의미.','화면 밖의 행(무한 스크롤, 가상화 목록)은','DOM에도 없으니 당연히 없을 것이라고 봅니다. (추론)')
b+=BOX('**주의**','이 실험은 Playwright 라이브러리의 `aria_snapshot()`으로 했습니다. Playwright MCP가 돌려주는 스냅샷은 여기에 `[ref=…]`가 붙은 형태이며, 링크 주소(`/url`)가 MCP 스냅샷에도 포함되는지는 확인하지 못했습니다. 공식 문서의 스냅샷 예시에는 링크에 주소가 보이지 않습니다. (확인 필요)','iframe과 Shadow DOM이 어디까지 담기는지, 긴 페이지에서 스냅샷이 잘리는 상한이 있는지도 확인하지 못했습니다.')
b+=HR()
b+=H1('4. MCP 안에서도 원본을 꺼낼 수는 있다')
b+=P('그러면 MCP를 쓰면 원본을 아예 못 보느냐 하면','그건 아닙니다.','저장소 README에 두 도구가 있습니다.')
b+=IMG(7,'수_07_저장소README_browser_evaluate.png','playwright-mcp README의 browser_evaluate 도구 설명',SRC_GH)
b+=P('`browser_evaluate`는','"**페이지나 요소에서 JavaScript 식을 평가한다**"는 도구입니다.','`function`에 `() => { ... }` 형태의 함수를 넣고,','`filename`을 주면 **결과를 파일로 저장**합니다.')
b+=IMG(8,'수_08_저장소README_run_code_unsafe.png','playwright-mcp README의 browser_run_code_unsafe 도구 설명',SRC_GH)
b+=P('`browser_run_code_unsafe`는','"**Playwright 코드 조각을 실행한다**"는 도구로,','`page` 객체를 받는 함수를 넘기면 라이브러리 API 전체를 쓸 수 있습니다.')
b+=P('다만 이름에 **unsafe**가 붙어 있고,','README는 "Playwright 서버 프로세스에서 임의의 JavaScript를 실행하며','**RCE(원격 코드 실행)와 동등하다**"고 경고합니다.','제가 대화할 때는 이 도구가 `browser_run_code`라는 이름이었는데,','2026-10-25 기준 README에는 `_unsafe`가 붙어 있습니다.')
b+=P('이 도구들로 라이브러리에서 하던 걸 그대로 해 봤습니다.','(아래는 Python 라이브러리로 실행한 결과이고,','MCP의 `browser_evaluate`도 같은 JavaScript를 받습니다.)')
b+=IMG(9,'수_09_터미널_evaluate.png','evaluate로 innerText와 data 속성값을 직접 꺼낸 터미널 화면','샌드박스에서 Playwright(Python)로 실제 실행한 결과')
b+=CODE('''document.body.innerText
[...document.querySelectorAll('tr[data-book-id]')]
    .map(r => r.dataset.bookId + ' ' + r.dataset.isbn)''',[('innerText','#ff6b6b'),('dataset.bookId','#ff6b6b'),('dataset.isbn','#ff6b6b')])
b+=P('첫 줄은 **화면의 글자 전체**를 그대로 꺼냅니다.','둘째 줄은 `data-book-id`가 있는 행을 모두 찾아','`bookId`와 `isbn` 값을 뽑습니다.','스냅샷에는 없던 `1001 9780000000001`이 나옵니다.')
b+=P('그런데 한 가지가 남습니다.','이 결과도 여전히 **LLM 컨텍스트로 돌아갑니다.**','코드를 LLM이 즉석에서 짜니 세션마다 다를 수 있고,','결과를 파일로 남기지 않으면 결국 요약본만 남습니다.')
b+=HR()
b+=H1('5. 그래서 정한 규칙: raw를 같이 남긴다')
b+=P('스크립트로 갈지 프롬프트로 갈지 고민하다가','이렇게 물었습니다.')
b+=Q('파이썬 스크립트 생성보다는 mcp달아준 클로드코드에게','주의사항을 프롬프트로 전달하는건 어때??')
b+=P('받은 답의 요지는 이랬습니다.','프롬프트는 누락 확률을 **낮추는** 수단이지 **막는** 수단이 아니다.','페이지가 많아질수록 뒤로 갈수록 펼치기·스크롤 단계를 건너뛰기 쉽고,','세션마다 결과가 달라진다. (이 부분은 Claude의 판단입니다)')
b+=P('그래도 단기 해법으로는 프롬프트를 택했습니다.','대신 **원본(raw)을 반드시 같이 남기는** 규칙을 넣었습니다.')
b+=IMG(10,'수_10_raw규칙_흐름.png','페이지 1개를 노트로 저장할 때의 /crawl 규칙 5단계 흐름')
b+=P('규칙은 일회성 메시지가 아니라','`.claude/commands/crawl.md` 같은 **슬래시 커맨드**로 둡니다.','매 페이지 같은 규칙이 적용되고 다른 환경으로 옮기기도 쉽습니다.')
b+=CODE('''# /crawl — 페이지 1개를 노트로 저장하는 규칙
1. 스냅샷을 찍기 전에 탭·아코디언·"더보기"를 모두 열고
   끝까지 스크롤한 뒤 로딩을 기다린다.
2. browser_evaluate로 아래를 실행해 raw/<페이지제목>.txt 로 저장한다.
   - document.body.innerText
   - [...document.querySelectorAll('a[href]')].map(a => a.href)
3. 노트는 스냅샷이 아니라 2번의 raw 파일을 읽고 작성한다.
4. 저장 후 raw의 표 행 수·링크 수와 노트를 대조한다.
   불일치가 있으면 노트 하단에 "요약하며 뺀 항목"으로 적는다.
5. raw에 없는 값은 "미확인"으로 적는다. 추측으로 채우지 않는다.''',[('browser_evaluate','#ff6b6b'),('raw/<페이지제목>.txt','#ff6b6b')])
b+=P('2번이 핵심입니다.','**요약되기 전의 원본을 파일로 확보**해 두면','나중에 다시 크롤링하지 않고 재가공할 수 있고,','4번처럼 "빠졌는지"를 숫자로 대조할 수 있습니다.')
b+=BOX('**아직 하지 않은 것**','이 뼈대는 대화에서 합의한 규칙을 옮긴 것이고, 실제 슬래시 커맨드 파일은 아직 만들지 않았습니다.','이미 저장한 노트 3~5개를 실제 페이지와 나란히 비교하는 일이 다음 할 일입니다. 표가 긴 페이지, 탭·아코디언 페이지, 링크가 많은 페이지부터 봅니다.','수백 페이지 이상이거나 주기적으로 반복한다면 결국 라이브러리 스크립트가 싸고 정확할 것입니다. 프롬프트로 돌리며 페이지 유형이 파악되면 그때 옮길 생각입니다.')
b+=HR()
b+=H1('알게 된 것')
b+=P('**MCP는 LLM이 브라우저를 손으로 조작하게 해 주는 인터페이스**고,','**라이브러리는 내 프로그램이 브라우저를 부품으로 쓰는 것**입니다.','같은 `click`이라도 결과를 누가 받느냐가 다릅니다.')
b+=P('지금 방식은 "LLM이 요약한 것"만 남는 구조라','**빠져도 빠진 줄 모릅니다.**','그래서 수집은 원본 보존부터, 해석만 LLM에게.')
b+=P('다음부터는 크롤링을 시작하기 전에','**raw 보존 규칙부터** 정하기로 했습니다.')
b+=HR()
b+=H1('참고자료')
b+=P('[[Playwright Python - Getting started (Library)|https://playwright.dev/python/docs/library]]')
b+=P('[[Playwright Python - Page API (content, evaluate)|https://playwright.dev/python/docs/api/class-page]]')
b+=P('[[Playwright MCP - Introduction|https://playwright.dev/mcp/introduction]]')
b+=P('[[Playwright MCP - Snapshots|https://playwright.dev/mcp/snapshots]]')
b+=P('[[microsoft/playwright-mcp 저장소 README (도구 목록)|https://github.com/microsoft/playwright-mcp]]')
b+=P('#PlaywrightMCP #Playwright #웹크롤링 #MCP #ClaudeCode #슬래시커맨드 #Obsidian #AI활용')
import os
PAGE(T,b,os.environ.get('OUT','/home/claude/out/wed/2026-10-28_수_Playwright_MCP_vs_라이브러리.html'))
print('ok')
