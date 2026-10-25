from lib import *
# 대표 예시: 도서관 장서 검색 페이지 (검색창 "도서 검색", 버튼 "검색", 링크 "습관의 힘"). 스냅샷 예시의 ref는 e5
T='[AI활용] Playwright MCP 작동 원리: 화면이 아니라 접근성 트리를 읽는다 (DOM과의 차이)'
SRC_PW='출처: Playwright MCP 공식 문서, 2026-10-25 캡처'
SRC_MDN='출처: MDN Web Docs, 2026-10-25 캡처'
b=''
b+=IMG(1,'화_01_썸네일.png','대표 이미지(썸네일)')
b+=P('Claude Code에 Playwright MCP를 붙이면','LLM이 브라우저를 열고','검색창에 글자를 치고 버튼을 누릅니다.')
b+=P('처음엔 당연히','**스크린샷을 보고 클릭하는 줄** 알았습니다.','그런데 공식 문서를 보니','"스크린샷 대신 접근성 스냅샷을 쓴다"고 되어 있었습니다.')
b+=P('접근성 스냅샷이 뭔지,','그게 DOM이랑 뭐가 다른지','DOM 정의부터 다시 물어본 기록입니다.')
b+=P('결론부터 말하면','**==Playwright MCP는 화면을 보지 않고,==**','**==DOM에서 파생된 접근성 트리를 텍스트로 읽습니다.==**')
b+=BOX('**이 글의 기준**','확인 날짜: 2026-10-25','근거: Playwright MCP 공식 문서 (Introduction, Snapshots), microsoft/playwright-mcp 저장소 README, MDN Web Docs (DOM 소개, Accessibility tree)','예시는 도서관 장서 검색 페이지로 통일했습니다. 스냅샷 출력은 샌드박스에서 Playwright를 실제로 실행해 얻은 결과입니다.','도구 이름과 매개변수(`target` 등)는 2026-10-25 기준 공식 문서를 따릅니다. 버전에 따라 달라질 수 있습니다.')
b+=HR()
b+=H1('처음에 제가 헷갈렸던 것')
b+=Q('playwright mcp가 작동하는 원리를 알기쉽게 설명헤줘')
b+=P('"접근성 트리를 읽는다"는 답을 듣고','바로 이렇게 되물었습니다.')
b+=Q('결국 html내에 존재하는 DOM읽는다는건가?','DOM 정의도 같이 설명해줘')
b+=BOX('**당시의 오해**','LLM이 브라우저를 조작한다길래 스크린샷을 보고 클릭하는 줄 알았다.','"접근성 트리"라는 답을 듣고는 결국 HTML 안의 DOM을 읽는 것과 같은 말 아닌가 싶었다.','DOM이 정확히 뭔지도 모호했다.')
b+=P('순서대로 풀어 보겠습니다.','Playwright MCP가 무엇인지 → 스냅샷이 무엇인지 →','DOM이 무엇인지 → 접근성 트리가 무엇인지.')
b+=HR()
b+=H1('1. Playwright MCP는 무엇인가')
b+=IMG(2,'화_02_공식문서_소개와예시.png','Playwright MCP 공식 문서의 소개와 예시',SRC_PW)
b+=P('공식 문서 첫 줄은 이렇습니다.','"**Playwright로 브라우저 자동화 기능을 제공하는**','**MCP(Model Context Protocol) 서버.**','**LLM이 구조화된 접근성 스냅샷으로 웹 페이지와 상호작용하게 한다.**','**비전 모델이 필요 없다.**"')
b+=P('구성은 세 개입니다.','LLM 쪽 클라이언트(Claude Code 등) ↔ MCP 프로토콜 ↔','Playwright MCP 서버(Node.js) ↔ Playwright API ↔ 실제 브라우저.')
b+=P('설정은 MCP 클라이언트에 이 한 덩어리를 넣는 게 전부입니다.')
b+=CODE('''{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    }
  }
}''',[('"playwright"','#51cf66'),('"@playwright/mcp@latest"','#51cf66')])
b+=P('`command`는 실행할 프로그램(`npx`),','`args`는 그 프로그램에 넘길 인수입니다.','`@playwright/mcp@latest`가 서버 패키지 이름이고','`@latest`는 최신 버전을 쓰라는 뜻입니다.')
b+=IMG(3,'화_03_공식문서_KeyFeatures.png','Playwright MCP 공식 문서의 Key Features',SRC_PW)
b+=P('핵심 기능 첫 두 줄이 이 글의 답입니다.')
b+=P('"**Snapshot-based — 픽셀이 아니라 접근성 트리에서 동작한다.**','**요소마다 고유한 ref가 붙어 결정적으로 상호작용한다.**"')
b+=P('"**LLM-friendly — LLM이 자연스럽게 읽는 구조화된 텍스트 출력.**','**DOM 덤프나 스크린샷보다 훨씬 싸다.**"')
b+=P('여기서 "DOM 덤프보다 싸다"는 말이 나옵니다.','즉 **DOM을 통째로 주는 게 아니라는** 뜻입니다.','이게 제 질문의 핵심이었습니다.')
b+=HR()
b+=H1('2. 스냅샷은 어떻게 생겼나')
b+=IMG(4,'화_04_공식문서_스냅샷형식.png','Playwright MCP 공식 문서의 스냅샷 형식 예시',SRC_PW)
b+=P('문서의 예시(할 일 목록 앱)를 보면','스냅샷은 이런 **들여쓰기된 텍스트**입니다.')
b+=CODE('''- heading "todos" [level=1] [ref=e3]
- textbox "What needs to be done?" [ref=e5]
- list [ref=e8]:
  - listitem [ref=e9]:
    - checkbox "Toggle Todo" [ref=e10]
    - text: Buy groceries''',[('[ref=e3]','#51cf66'),('[ref=e5]','#51cf66'),('[ref=e8]','#51cf66'),('[ref=e9]','#51cf66'),('[ref=e10]','#51cf66')])
b+=P('줄마다 세 가지가 있습니다.','**역할**(heading, textbox, checkbox),','**이름**("What needs to be done?"),','그리고 **ref 번호**(e5).')
b+=P('LLM은 이 텍스트를 읽고','"e5가 입력창이구나"를 알아낸 다음','**번호로 지목해서** 도구를 부릅니다.')
b+=CODE('''browser_type  { target: "e5", text: "headphones" }
browser_click { target: "e10" }''',[('target: "e5"','#51cf66'),('target: "e10"','#51cf66')])
b+=P('`browser_type`은 입력, `browser_click`은 클릭입니다.','`target`에 ref 번호를 넣습니다.','좌표를 추측할 필요가 없습니다.')
b+=P('문서의 ref 규칙도 적어 둡니다.')
b+=TABLE(['항목','공식 문서 설명'],[
['형식','`e` + 숫자. iframe 안이면 앞에 프레임 id (`e1`, `e15`, `f2e7`)'],
['범위','**스냅샷 하나 안에서만** 고유'],
['수명','**페이지가 바뀔 때까지** 유효'],
['부여 대상','상호작용 요소만이 아니라 접근성 트리가 노출하는 **모든 노드**']])
b+=P('그래서 페이지가 바뀌면 ref도 새로 받아야 합니다.','오래된 ref를 쓰면 문서대로','"Ref … not found in the current page snapshot. Try capturing new snapshot."','오류가 납니다.')
b+=HR()
b+=H1('3. 그러면 DOM이 뭔가')
b+=P('여기서 제가 되물은 지점입니다.','"결국 HTML 안에 있는 DOM을 읽는다는 건가?"','DOM이 뭔지부터 정확히 잡아야 했습니다.')
b+=IMG(5,'화_05_MDN_DOM정의.png','MDN의 DOM 정의',SRC_MDN)
b+=P('MDN의 정의는 이렇습니다.','"**DOM은 문서의 구조(예: 웹 페이지를 나타내는 HTML)를**','**메모리에 표현해서 웹 페이지와 스크립트를 연결한다.**"')
b+=P('"**DOM은 문서를 논리적 트리로 나타낸다.**','**트리의 가지 끝마다 노드가 있고, 노드는 객체를 담는다.**"')
b+=P('그리고 다른 절에 이 문장이 있습니다.','"**브라우저가 HTML 문서를 파싱하면 DOM 트리를 만들고,**','**그것을 써서 문서를 표시한다.**"')
b+=P('정리하면 이렇습니다.')
b+=BOX('**HTML과 DOM의 관계**','HTML = 서버가 보내 준 **글자 그대로의 파일**','DOM = 브라우저가 그 파일을 읽어 **메모리에 만든 트리 구조의 객체**','JavaScript의 `document.getElementById(...)`가 만지는 것이 DOM이다.')
b+=P('"HTML 안에 DOM이 있다"는 제 표현은','정확하지 않았습니다.','DOM은 HTML **안에** 있는 게 아니라','HTML을 **읽어서 만든 것**입니다.')
b+=HR()
b+=H1('4. 접근성 트리는 DOM에서 파생된 요약본이다')
b+=IMG(6,'화_06_MDN_접근성트리.png','MDN의 접근성 트리 정의',SRC_MDN)
b+=P('MDN의 접근성 트리 설명이','제 질문에 정확히 답합니다.')
b+=P('"**브라우저는 마크업을 DOM 트리라는 내부 표현으로 바꾼다.**','**DOM 트리에는 마크업의 모든 요소·속성·텍스트 노드를 나타내는 객체가 있다.**','**브라우저는 그 다음 DOM 트리를 바탕으로 접근성 트리를 만든다.**"')
b+=P('원래 용도는 스크린 리더 같은 보조 기술입니다.','접근성 트리의 객체는 네 가지를 가집니다.')
b+=TABLE(['속성','뜻 (MDN)','도서관 검색 페이지라면'],[
['name','이것을 뭐라고 부르나','"도서 검색"'],
['description','이름 외에 더 설명할 것','(없음)'],
['role','어떤 종류인가','textbox'],
['state','상태가 있나 (checked, expanded 등)','(없음)']])
b+=IMG(7,'화_07_HTML_DOM_접근성트리_스냅샷.png','HTML → DOM → 접근성 트리 → 스냅샷으로 이어지는 네 단계 도식')
b+=P('네 단계로 놓으면 이렇게 됩니다.','**HTML**(파일) → **DOM**(브라우저 메모리의 트리 전체) →','**접근성 트리**(의미만 남긴 파생본) → **스냅샷**(그것을 텍스트 + ref로).')
b+=P('앞의 셋은 브라우저가 만들고,','마지막 하나를 Playwright MCP가 만들어 LLM에 줍니다.')
b+=HR()
b+=H1('5. 직접 확인해 보기')
b+=P('말로만 들으면 감이 안 와서','도서관 검색 페이지를 하나 만들고','Playwright로 접근성 스냅샷을 직접 찍어 봤습니다.')
b+=CODE('''<div class="box">
  <label for="q">도서 검색</label>
  <input id="q" type="text">
  <button type="submit">검색</button>
</div>''',[('class="box"','#ffa94d'),('id="q"','#ffa94d')])
b+=P('이런 HTML에서 Playwright의 `aria_snapshot()`을 부르면','아래처럼 나옵니다.')
b+=IMG(8,'화_08_실제실행_HTML과_스냅샷.png','같은 페이지의 HTML과 Playwright 접근성 스냅샷을 나란히 둔 화면','샌드박스에서 Playwright(Python)로 실제 실행한 결과. MCP 스냅샷의 ref 번호는 이 출력에 없다')
b+=CODE('''- heading "도서관 장서 검색" [level=1]
- text: 도서 검색
- textbox "도서 검색"
- button "검색"''',[('textbox','#51cf66'),('button','#51cf66'),('heading','#51cf66')])
b+=P('`div`도 `class="box"`도 `id="q"`도 사라졌습니다.','`<input type="text">`는 **`textbox`라는 역할**로,','`<label>`의 글자는 **입력창의 이름**으로 붙었습니다.')
b+=P('DOM 요소는 17개였는데','스냅샷에 남은 줄은 열 줄 남짓입니다.','**레이아웃용 요소와 속성은 빠지고 의미만 남는다**는 게','눈으로 확인됐습니다.')
b+=BOX('**주의**','이 출력은 Playwright 라이브러리의 `aria_snapshot()` 결과입니다. Playwright MCP의 스냅샷은 여기에 `[ref=e5]` 같은 번호가 붙은 형태로, 세부 형식이 완전히 같은지는 확인하지 못했습니다. (확인 필요)','링크의 `/url` 줄이 MCP 스냅샷에도 나오는지도 확인하지 못했습니다. 공식 문서의 예시에는 링크에 주소가 보이지 않습니다.')
b+=HR()
b+=H1('6. 그래서 "DOM을 읽는다"는 반쯤 맞다')
b+=IMG(9,'화_09_반쯤맞다_카드.png','"DOM을 읽는다"는 말의 맞는 부분과 틀린 부분 비교 카드')
b+=P('제 되물음에 대한 답은 이렇습니다.')
b+=P('**맞는 부분**: 출발점은 DOM입니다.','화면 픽셀이 아니라 브라우저가 만든 트리에서 나옵니다.')
b+=P('**틀린 부분**: DOM 자체를 읽는 게 아닙니다.','DOM에서 **의미만 남긴 파생본**(접근성 트리)을 읽습니다.','그래서 "DOM 덤프보다 훨씬 싸다"는 문서 표현이 나옵니다.')
b+=Q('HTML → DOM(전체 구조) → 접근성 트리(의미 요약) → MCP 스냅샷(+ref).','그러니 "DOM을 읽는다"는 반쯤 맞다. 직접이 아니라 파생본을 읽는다.')
b+=HR()
b+=H1('7. 왜 스크린샷 대신 스냅샷인가')
b+=IMG(10,'화_10_공식문서_스냅샷vs스크린샷.png','Playwright MCP 공식 문서의 스냅샷과 스크린샷 비교표',SRC_PW)
b+=P('공식 문서에 비교표가 있습니다.')
b+=TABLE(['','스냅샷','스크린샷'],[
['토큰 비용','낮음 — 텍스트만','높음 — 이미지 토큰'],
['정밀도','정확 — ref가 특정 요소를 가리킴','근사 — 좌표 추측 필요'],
['속도','즉시 — 텍스트 파싱','느림 — 비전 모델 추론'],
['재현성','결정적 — 같은 구조면 같은 동작','가변 — 레이아웃이 바뀌면 좌표가 깨짐'],
['비전 모델','불필요','필요']])
b+=P('제가 제일 와닿은 건 **토큰**이었습니다.','스냅샷은 텍스트라 싸고,','비전 모델이 없는 로컬 모델로도 돌릴 수 있습니다.')
b+=P('화면이 꼭 필요한 경우(캔버스, 차트)는','문서에서 "스냅샷과 스크린샷을 같이 찍어라"고 하고,','좌표 기반 조작은 **Vision Mode**라는 별도 모드로 둡니다.','Vision Mode 문서는 이번에 열리지 않아 내용은 확인하지 못했습니다.')
b+=HR()
b+=H1('알게 된 것')
b+=P('접근성 트리를 쓰는 이유는 결국 **토큰과 재현성**입니다.','사람이 조작에 필요한 것만 남긴 구조라','LLM이 조작하기에도 딱 맞습니다.')
b+=P('뒤집어 말하면','**조작에는 충분하지만 데이터 수집에는 부족할 수 있습니다.**','class, id, 속성값, 보이지 않는 요소가','스냅샷에 없기 때문입니다.','이 깨달음이 다음 글(크롤링에서 빠지는 것들)로 이어집니다.')
b+=P('그리고 용어를 정확히 잡는 게 중요했습니다.','"HTML 안의 DOM"이 아니라','"HTML을 읽어 만든 DOM, 그 DOM에서 파생된 접근성 트리".','이 순서가 잡히니 MCP가 뭘 보는지가 분명해졌습니다.')
b+=HR()
b+=H1('참고자료')
b+=P('[[Playwright MCP - Introduction|https://playwright.dev/mcp/introduction]]')
b+=P('[[Playwright MCP - Snapshots|https://playwright.dev/mcp/snapshots]]')
b+=P('[[microsoft/playwright-mcp 저장소 README|https://github.com/microsoft/playwright-mcp]]')
b+=P('[[MDN - Document Object Model 소개|https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction]]')
b+=P('[[MDN - Accessibility tree|https://developer.mozilla.org/en-US/docs/Glossary/Accessibility_tree]]')
b+=P('#PlaywrightMCP #Playwright #MCP #접근성트리 #DOM #ClaudeCode #브라우저자동화 #AI활용')
import os
PAGE(T,b,os.environ.get('OUT','/home/claude/out/tue/2026-10-27_화_Playwright_MCP_작동원리.html'))
print('ok')
