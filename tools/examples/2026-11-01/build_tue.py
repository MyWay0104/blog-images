from lib import *
# 대표 예시: 독서 노트 사이트(reading-notes), 글꼴 Poppins(Google Fonts, OFL), 글꼴 폴더 ./fonts/
T='[AI활용] Google Fonts 직접 호스팅하는 방법: CDN이 막힌 환경에서 @font-face로 글꼴 넣기'
SRC_G='출처: Google Fonts 공식 자료, 2026-11-01 캡처'
SRC_M='출처: MDN Web Docs, 2026-11-01 캡처'
b=''
b+=IMG(1,'화_01_썸네일.png','대표 이미지(썸네일)')
b+=P('웹 페이지에 Google Fonts를 넣는 방법은','`<link>` 한 줄이면 끝입니다.','그런데 **외부로 나가는 연결이 막힌 환경**에서는','그 한 줄이 아무 글꼴도 가져오지 못합니다.')
b+=P('이때 나오는 단어가 **CDN**이고,','해결책이 **직접 호스팅(self-host)**입니다.','CDN이 정확히 뭔지,','글꼴 파일을 내 서버에 두고 `@font-face`로 연결하는 절차를','공식 자료와 실제 실행으로 정리합니다.')
b+=P('결론부터 말하면','**==CSS는 거의 그대로이고, 바뀌는 건 글꼴 파일의 주소(src)뿐==**입니다.')
b+=BOX('**이 글의 기준**','확인 날짜: 2026-11-01','근거: MDN Web Docs (CDN, @font-face), Google Fonts 공식 자료 (Getting started, FAQ, Fonts Knowledge "Self-hosting web fonts"), Google Fonts API가 실제로 돌려준 CSS','직접 호스팅 화면과 요청 기록은 샌드박스에서 Playwright로 실제 실행했습니다. Windows에서 IIS나 Nginx 같은 서버에 올리는 절차는 이 글에서 다루지 않습니다.','예시는 독서 노트 사이트(`reading-notes`)와 Google Fonts의 Poppins 글꼴, 폴더 `./fonts/`로 통일했습니다.')
b+=HR()
b+=H1('1. CDN이 뭔가')
b+=IMG(2,'화_02_MDN_CDN정의.png','MDN의 CDN 정의와 장단점',SRC_M)
b+=P('MDN의 정의는 이렇습니다.','"**CDN(Content Delivery Network)은 여러 지역에 흩어져 있는 서버 집단이다.**','**이 서버들은 데이터의 복제본을 저장해 두고,**','**사용자와 가장 가까운 서버가 요청에 응답하게 한다.**"')
b+=P('즉 CDN은 "남의 서버에 있는 복사본"입니다.','Bootstrap, jQuery 같은 라이브러리 파일을','내 서버가 아니라 CDN에서 받아 쓰는 게 흔한 예입니다.','Google Fonts도 같은 구조입니다.')
b+=P('MDN은 장점과 함께 **단점**도 적습니다.','"**제3자 서비스에 대한 의존이 생긴다.**','**CDN이 다운되거나, 특정 지역에서 차단되거나, 영구 종료되면**','**웹사이트가 오동작한다.**"')
b+=P('제가 겪은 게 바로 "특정 환경에서 차단"이었습니다.')
b+=HR()
b+=H1('2. Google Fonts의 <link> 한 줄이 실제로 하는 일')
b+=P('Google Fonts 문서의 기본 사용법은 이렇습니다.')
b+=CODE('''<link rel="stylesheet"
  href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap">''',[('fonts.googleapis.com','#a9e34b')])
b+=P('`<link>`로 **CSS 파일 하나**를 불러옵니다.','주소의 `family=` 뒤가 글꼴 이름과 굵기입니다.')
b+=P('그 주소가 돌려주는 CSS를 직접 열어 봤습니다.')
b+=IMG(3,'화_03_API응답_fontface.png','Google Fonts API가 돌려준 CSS: @font-face와 fonts.gstatic.com 주소','출처: fonts.googleapis.com 응답을 PC 브라우저로 직접 열어 캡처 (Noto Sans KR 요청), 2026-11-01')
b+=P('안에 든 건 **`@font-face` 규칙의 묶음**이고,','각 규칙의 `src`는 **`fonts.gstatic.com`**의 `.woff2` 파일을 가리킵니다.')
b+=IMG(4,'화_04_CDN_vs_직접호스팅.png','CDN 경로와 직접 호스팅 경로에서 글꼴 파일이 오는 길을 비교한 도식')
b+=P('그러니까 `<link>` 한 줄 뒤에는 **두 번의 외부 요청**이 숨어 있습니다.','① `fonts.googleapis.com`에서 CSS를 받고,','② 그 CSS가 가리키는 `fonts.gstatic.com`에서 글꼴 파일을 받습니다.','둘 중 하나라도 막히면 글꼴이 안 옵니다.')
b+=P('Google Fonts FAQ도 이 구조를 그대로 설명합니다.','"**브라우저는 Google Fonts Web API에 HTTP 요청을 보내고,**','**API는 CSS를, 이어서 CSS에 적힌 글꼴 파일을 사용자에게 보낸다.**"','이 요청에는 방문자의 IP 주소, 요청 URL, 브라우저 정보(user agent)와 referer가 포함된다고 적혀 있습니다.')
b+=HR()
b+=H1('3. 직접 호스팅해도 되나')
b+=IMG(5,'화_05_FAQ_selfhost.png','Google Fonts FAQ: 사용자 데이터를 Google에 보내지 않고 글꼴을 넣을 수 있는가',SRC_G)
b+=P('FAQ에 바로 그 질문이 있습니다.','"**Google 서버에서 글꼴을 받는 대신, 개발자는 글꼴을 내려받아**','**자기 서버에 올려서 직접 호스팅할 수 있다.**','**웹사이트 운영자의 서버에서 글꼴이 로드되면**','**Google은 그 사이트 방문과 관련한 어떤 데이터도 받지 않는다.**"')
b+=P('라이선스도 FAQ에 있습니다.','"**모든 Google Fonts는 오픈 소스이고 비용이 없다.**"','"**상업적으로 쓸 수 있고, 상업적으로 판매되는 제품 안에 포함할 수도 있다.**','**가장 흔한 라이선스는 SIL Open Font License다.**"')
b+=P('글꼴 파일은 fonts.google.com에서 내려받거나,','FAQ가 안내하는 대로 GitHub `google/fonts` 저장소에서 받을 수 있습니다.','"**설치하거나 직접 호스팅할 글꼴 파일을 내려받을 수 있다**"고 적혀 있습니다.')
b+=BOX('**FAQ가 적어 둔 직접 호스팅의 단점**','① 파일 크기가 커진다. API는 글꼴을 조각내어 필요한 부분만 주지만, 직접 호스팅은 파일 전체를 받는다.','② 브라우저별 최적화를 못 받는다. API는 브라우저에 맞는 형식과 수정본을 자동으로 골라 준다.','③ 업데이트를 직접 해야 한다. API는 글꼴이 갱신되면 자동으로 반영한다.','막힌 환경에서는 어차피 선택지가 없지만, 열린 환경이라면 이 세 가지를 알고 고르는 게 맞습니다.')
b+=HR()
b+=H1('4. @font-face가 하는 일')
b+=IMG(6,'화_06_MDN_fontface문법.png','MDN의 @font-face 정의와 문법 예시',SRC_M)
b+=P('MDN의 정의입니다.','"**`@font-face` CSS at-rule은 글자를 표시할 사용자 지정 글꼴을 지정한다.**','**글꼴은 원격 서버에서 로드할 수도, 사용자 컴퓨터에 설치된 로컬 글꼴을 쓸 수도 있다.**"')
b+=P('필수 항목은 두 개입니다.')
b+=TABLE(['항목','뜻 (MDN)'],[
['`font-family`','"글꼴 속성의 값으로 쓸 이름을 지정한다. 규칙이 유효하려면 반드시 있어야 한다"'],
['`src`','"글꼴 파일에 대한 참조를 지정한다. 형식과 기술에 대한 힌트를 포함한다. 반드시 있어야 한다"'],
['`font-weight`','"이 글꼴 파일이 담당하는 굵기. `100 400`처럼 범위도 가능"'],
['`font-display`','"글꼴을 내려받는 동안과 받은 뒤에 어떻게 표시할지 정한다"']])
b+=P('`src`에는 `local()`과 `url()`을 같이 쓸 수 있습니다.','MDN: "**사용자 기기에 설치된 글꼴이 있으면 그것을 쓰고,**','**없으면 `url()`로 지정한 글꼴 파일을 내려받아 쓴다.**"')
b+=IMG(7,'화_07_지식문서_selfhost_차이.png','Google Fonts Knowledge: 직접 호스팅과 서비스 이용의 유일한 차이는 src 경로',SRC_G)
b+=P('Google의 Fonts Knowledge 글은 차이를 한 줄로 정리합니다.','"**유일한 실제 차이는 글꼴 파일 경로(src)가**','**절대 URL(https://fonts.gstatic.com/...)이 아니라**','**상대 URL(../fonts/FONT_FILE_NAME.woff2)이 된다는 것이다.**"')
b+=P('즉 2번에서 본 API 응답의 `@font-face`를','**내 CSS에 옮겨 적고 `src`만 내 폴더로 바꾸면** 됩니다.')
b+=HR()
b+=H1('5. 직접 해 보기')
b+=P('독서 노트 사이트에 Poppins를 직접 호스팅해 봤습니다.','폴더 구조는 이렇습니다.')
b+=CODE('''reading-notes/
  index.html
  fonts/
    Poppins-Regular.ttf
    Poppins-Bold.ttf''',[('fonts/','#a9e34b')])
b+=P('CSS는 이렇게 적었습니다.')
b+=CODE('''@font-face {
  font-family: "Poppins";
  src: url("./fonts/Poppins-Regular.ttf") format("truetype");
  font-weight: 400;
  font-display: swap;
}
@font-face {
  font-family: "Poppins";
  src: url("./fonts/Poppins-Bold.ttf") format("truetype");
  font-weight: 700;
  font-display: swap;
}
body { font-family: "Poppins", "Noto Sans CJK KR", sans-serif; }''',[('./fonts/Poppins-Regular.ttf','#a9e34b'),('./fonts/Poppins-Bold.ttf','#a9e34b'),('font-display: swap','#ffd43b')])
b+=P('첫 번째 `@font-face`는 **굵기 400**에 Regular 파일을,','두 번째는 **굵기 700**에 Bold 파일을 붙입니다.','같은 `font-family` 이름을 쓰고 `font-weight`로 가릅니다.')
b+=P('`src`의 `url()`은 CSS 파일 기준 **상대 경로**이고,','`format("truetype")`은 `.ttf` 파일이라는 힌트입니다.','(Google Fonts API는 `.woff2`를 주지만, 저는 내려받은 `.ttf`를 그대로 썼습니다)')
b+=P('`font-display: swap`은 글꼴을 받는 동안','대체 글꼴로 먼저 보여 주고 받은 뒤 바꾸라는 뜻입니다.','API 응답에도 같은 값이 들어 있었습니다.')
b+=P('마지막 줄의 `font-family`는 **우선순위 목록**입니다.','Poppins → 한글은 Noto Sans CJK KR → 둘 다 없으면 sans-serif.','Google Fonts 문서도 "목록 끝에 `serif`나 `sans-serif` 같은','일반 글꼴 이름을 붙여라"라고 합니다.')
b+=IMG(8,'화_08_실제실행_fontface비교.png','@font-face를 적용한 제목과 적용하지 않은 제목을 나란히 렌더링한 화면','샌드박스에서 Playwright로 실제 렌더링한 결과')
b+=P('위가 `./fonts/`에서 받은 Poppins,','아래가 적용하지 않은 시스템 글꼴입니다.','외부로 나가는 연결 없이 글꼴이 바뀌었습니다.')
b+=HR()
b+=H1('6. 정말 밖으로 안 나갔는지 확인')
b+=P('"안 나갔다"는 느낌이 아니라 기록으로 확인했습니다.','페이지를 열 때 브라우저가 보낸 요청을 Playwright로 기록했습니다.')
b+=IMG(9,'화_09_터미널_요청기록.png','페이지를 열 때 브라우저가 요청한 파일 목록: 문서 1개와 글꼴 파일 2개','샌드박스에서 Playwright로 실제 기록한 요청 목록')
b+=P('요청은 세 개뿐입니다.','`index.html`, 그리고 `./fonts/`의 글꼴 파일 두 개.','`fonts.googleapis.com`이나 `fonts.gstatic.com`으로 나간 요청은 **없습니다.**')
b+=P('실제 사이트에서는 브라우저 개발자 도구의 **Network 탭**에서','Font 유형으로 걸러 보면 같은 것을 확인할 수 있습니다.')
b+=HR()
b+=H1('7. 절차 정리')
b+=IMG(10,'화_10_직접호스팅_5단계.png','직접 호스팅 5단계 요약 카드')
b+=TABLE(['단계','할 일','확인'],[
['1','Google Fonts 또는 GitHub `google/fonts`에서 글꼴 파일 내려받기','라이선스(OFL 등) 확인'],
['2','프로젝트의 `fonts/` 폴더에 넣기','CSS 기준 상대 경로 메모'],
['3','CSS에 `@font-face` 선언 (이름, `src`, 굵기, `font-display`)','굵기마다 규칙 하나'],
['4','`font-family: "이름", sans-serif;`로 사용','맨 뒤에 일반 글꼴 이름'],
['5','Network 탭에서 글꼴 요청이 내 서버로 가는지 확인','googleapis·gstatic 요청 없음']])
b+=P('API 응답에서 봤듯이 Google Fonts는','글꼴을 **유니코드 범위별로 여러 조각**으로 나눠 줍니다.','직접 호스팅할 때 파일 하나로 두면 그만큼 커집니다.','필요한 글자만 담도록 줄이는 방법(서브셋)은','이 글에서 다루지 않았습니다. (확인 필요)')
b+=HR()
b+=H1('알게 된 것')
b+=P('**CDN은 "남의 서버에 있는 복사본"**입니다.','편하지만, MDN이 적어 둔 대로','그 서버가 막히면 내 사이트도 같이 멈춥니다.')
b+=P('Google Fonts의 `<link>` 한 줄은','실제로는 **CSS 한 번, 글꼴 파일 한 번**, 두 번의 외부 요청이었습니다.','그걸 알고 나니 직접 호스팅이 뭘 바꾸는 건지 분명해졌습니다.','**`src`의 주소 하나**입니다.')
b+=HR()
b+=H1('참고자료')
b+=P('[[MDN - CDN (Glossary)|https://developer.mozilla.org/en-US/docs/Glossary/CDN]]')
b+=P('[[MDN - @font-face|https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face]]')
b+=P('[[Google Fonts - Getting started with the Google Fonts API|https://developers.google.com/fonts/docs/getting_started]]')
b+=P('[[Google Fonts - FAQ|https://fonts.google.com/faq]]')
b+=P('[[Google Fonts Knowledge - Self-hosting web fonts|https://fonts.google.com/knowledge/using_type/self_hosting_web_fonts]]')
b+=P('#GoogleFonts #fontface #CDN #웹폰트 #직접호스팅 #selfhost #CSS #AI활용 #웹개발입문')
import os
PAGE(T,b,os.environ.get('OUT','/home/claude/out/tue/2026-11-03_화_Google_Fonts_직접호스팅.html'))
print('ok')
