from lib import *
# 대표 예시: 독서 노트 앱(reading-notes)에 외부 npm CLI 도구 하나를 처음 붙이는 상황. 도구 이름은 <도구>로 일반화한다 (실제 설치 기록 없음 → 공식 문서 기준 정리)
T='[AI활용] npx install 오타가 위험한 이유: npm 패키지 설치 전 확인 4가지'
SN='출처: npm 공식 문서(docs.npmjs.com), 2026-11-08 캡처'
SJ='출처: npm 공식 레지스트리 사이트(npmjs.com), 2026-11-08 캡처'
SG='출처: GitHub 공식 블로그(github.blog), 2026-11-08 캡처'
SR='출처: npm 레지스트리 메타데이터(registry.npmjs.org/install/latest)와 npmjs.com 표기를 발췌해 정리, 2026-11-08'
SX='공식 문서의 명령 형식을 바탕으로 재구성한 예시 화면 (실제 실행 결과가 아닙니다)'
b=''
b+=IMG(1,'금_01_썸네일.png','대표 이미지(썸네일)')
b+=P('독서 노트 앱에 외부 npm 도구를 하나 붙이려고 했습니다.','설치 명령은 `npx install <도구>`라고 알고 있었습니다.')
b+=P('그런데 치기 전에 이런 질문이 걸렸습니다.')
b+=Q('npx install <도구>를 했을 때 프록시를 통해 정상적으로 설치가 된다면,','보안으로부터 완전히 안전하다고 할 수 있는가?','(도구 이름과 환경 표현은 바꿨습니다)')
b+=P('결론부터 적으면, 두 가지가 다 틀려 있었습니다.','**==프록시를 통과했다는 것은 "그 경로가 허용됐다"는 뜻이지, 코드가 안전하다는 뜻이 아닙니다.==**','그리고 `npx install <도구>`는 애초에 **그 도구를 설치하는 명령이 아니었습니다.**')
b+=P('npm 공식 문서 네 곳(npm exec, scripts, config, npm view)과','GitHub 공식 블로그를 읽고 정리했습니다.')
b+=BOX('**이 글의 기준**','확인 날짜: 2026-11-08','근거: npm 공식 문서(npm exec · scripts · config · npm view, CLI v12 문서), npm 레지스트리(npmjs.com, registry.npmjs.org), GitHub 공식 블로그(Our plan for a more secure npm supply chain, 2025-09)','이 글은 실제로 설치해 본 기록이 아니라 **공식 문서 기준으로 정리한 글**입니다. 명령 예시 화면은 문서의 형식을 바탕으로 재구성했고, 실제 실행 결과가 아닙니다.','프록시가 실제로 어떤 검사를 하는지는 환경마다 달라 확인하지 못했습니다. 그 부분은 추론이라고 표시했습니다.','예시는 독서 노트 앱(`reading-notes`)에 외부 CLI 도구 `<도구>`를 붙이는 상황으로 통일했습니다.')
b+=HR()
b+=H1('먼저 그림 하나')
b+=IMG(2,'금_02_도식_첫단어.png','npx install <도구>와 npx <도구> install에서 npx가 첫 단어를 패키지 이름으로, 나머지를 인자로 읽는 방식을 비교한 도식')
b+=P('npx는 **첫 단어를 패키지 이름**으로 읽습니다.','`npx install <도구>`에서 패키지는 `install`이고, `<도구>`는 그 패키지에 넘기는 인자입니다.','제가 쓰려던 도구는 명령 어디에도 "패키지"로 들어가 있지 않았습니다.')
b+=P('단어 순서 하나가 "무엇을 받아서 무엇을 실행할지"를 통째로 바꿉니다.','이게 왜 위험한지를 공식 문서로 따라가 보겠습니다.')
b+=HR()
b+=H1('1. npx install <도구>는 무엇을 하는 명령인가')
b+=IMG(3,'금_03_공식문서_npmexec_개요.png','npm exec 공식 문서의 Synopsis와 Description: 명령 형식과 "요청한 패키지가 로컬에 없으면 설치 여부를 묻는다"는 문단',SN)
b+=P('npm exec 문서의 명령 형식은 이렇습니다.','"**`npm exec -- <pkg>[@<version>] [args...]`**"','첫 자리가 패키지(`<pkg>`), 그 뒤가 인자(`args`)입니다.','npx도 같은 규칙으로 동작한다고 같은 문서가 설명합니다.')
b+=P('그 아래 문단이 이 글의 출발점입니다.','"**요청한 패키지가 로컬 프로젝트 의존성에 없으면 프롬프트가 출력된다.','`--yes`나 `--no`로 이 프롬프트를 억제할 수 있다.','표준 입력이 TTY가 아니거나 CI 환경이 감지되면 `--yes`로 간주한다.','요청한 패키지는 npm 캐시 폴더에 설치되고, 그 폴더가 실행 프로세스의 PATH에 추가된다.**"')
b+=P('즉 터미널에서 직접 치면 "설치할까요?" 하고 한 번 묻지만,','스크립트나 CI처럼 **사람이 없는 자리에서는 묻지 않고 설치**합니다.')
b+=IMG(4,'금_04_공식문서_npmexec_실행파일규칙.png','npm exec 공식 문서: 첫 번째 위치 인자에서 실행 파일을 결정하는 규칙과, npx에서 옵션은 위치 인자 앞에 와야 한다는 예시',SN)
b+=P('어느 패키지를 받을지는 이렇게 정합니다.','"**`--package` 옵션이 없으면, npm은 첫 번째 위치 인자로 주어진 패키지 지정자에서 실행 파일 이름을 알아내려 한다.**"','패키지의 `bin` 항목이 하나면 그것을 쓰고,','하나로 정해지지 않으면(bin이 없거나 이름이 안 맞으면) "**npm exec은 에러로 종료한다.**"')
b+=P('예시도 문서에 있습니다.','`npx foo@latest bar --package=@npmcli/foo`를 치면','npm은 **`foo` 패키지**를 찾아 `foo bar --package=@npmcli/foo`를 실행합니다.','"npx로 실행할 때는 모든 플래그와 옵션이 **위치 인자보다 앞에** 와야 한다"는 규칙 때문입니다.')
b+=P('이 규칙을 제 명령에 대면,','`npx install <도구>`에서 npm이 찾는 패키지는 **`install`**입니다.')
b+=IMG(5,'금_05_npmjs_install패키지.png','npmjs.com의 install 패키지 페이지: 0.13.0, 7년 전 게시, 0 Dependencies, 2081 Dependents, 64 Versions, "Minimal JavaScript module loader"',SJ)
b+=P('그리고 `install`이라는 이름의 패키지는 **실제로 있습니다.**','설명은 "Minimal JavaScript module loader", 버전 0.13.0,','마지막 게시는 7년 전, 이 패키지에 의존하는 패키지가 2,081개입니다.','제가 쓰려던 도구와는 아무 관계가 없는 패키지입니다.')
b+=IMG(6,'금_06_install패키지_메타데이터.png','레지스트리 메타데이터에서 발췌한 install@0.13.0의 bin·scripts 항목과, 공식 문서 기준으로 npx install <도구>가 어떻게 진행될지 정리한 카드',SR)
b+=P('레지스트리 메타데이터를 보면 이 패키지에는 `bin` 항목이 없고,','설치 때 자동으로 도는 스크립트(preinstall·install·postinstall)도 없습니다.','그래서 공식 문서 기준으로는 "실행 파일을 정할 수 없다"는 **에러로 끝날** 가능성이 큽니다.','(에러 전에 캐시 설치까지 진행되는지는 문서만으로 알 수 없어 확인 필요로 남깁니다. 직접 실행해 보지는 않았습니다.)')
b+=P('여기서 안심하면 안 되는 이유가 있습니다.','**이번엔 오타가 가리킨 이름의 주인이 무해한 패키지였을 뿐**입니다.','오타가 가리킨 이름에 `bin`이 있는 패키지가 있었다면','설치 프롬프트 → 캐시에 설치 → 그 실행 파일 실행까지 그대로 갑니다.','CI나 스크립트 안이라면 프롬프트조차 없습니다.')
b+=CODE('''# 오타: "install"이라는 이름의 패키지를 찾는다
npx install <도구>

# 의도한 명령: <도구> 패키지에 install 하위 명령을 넘긴다
npx <도구> install

# 버전을 적으면 그 버전만 받는다 (옵션은 패키지 이름 앞에)
npx <도구>@<검토한 버전> install''',[('npx install <도구>','#ff8787'),('npx <도구> install','#8ce99a'),('<검토한 버전>','#ffd43b')])
b+=P('정확한 명령 형태는 **도구의 README**에서 확인하는 것이 먼저입니다.','첫 단어가 그 도구의 패키지 이름인지만 봐도 이 오타는 걸러집니다.')
b+=HR()
b+=H1('2. 프록시를 통과했다 ≠ 안전하다')
b+=Q('프록시가 통과시킨 것이면','보안 검토를 통과한 것과 같다고 생각했다.')
b+=P('질문의 두 번째 절반입니다.','당시에는 "프록시가 허용했다 = 검토가 끝났다"로 읽고 있었습니다.')
b+=IMG(7,'금_07_도식_경로와실행.png','네트워크 경로(레지스트리 → 프록시 → 다운로드)와 내 PC 안의 실행(설치 스크립트 → 실행 파일 → 그 뒤의 일)을 두 층으로 나눈 도식')
b+=P('두 층을 섞고 있었던 겁니다.','프록시는 **네트워크 경로**에 있는 장치입니다.','"이 주소로 나가는 연결을 허용할지"를 정하고 기록합니다.','어떤 검사를 더 하는지는 환경마다 달라서 여기서는 단정하지 않겠습니다 (추론, 확인 필요).')
b+=P('분명한 것은 그 다음 층입니다.','받아온 패키지가 **내 PC 안에서 무엇을 하는지**는','경로가 허용됐는지와는 다른 문제입니다.','설치 스크립트가 돌고, npx가 실행 파일을 돌리고, 그 프로그램이 파일과 네트워크를 만집니다.')
b+=IMG(8,'금_08_GitHub블로그_ShaiHulud.png','GitHub 공식 블로그 "Our plan for a more secure npm supply chain"의 Shai-Hulud 설명 문단과 GitHub의 대응 조치',SG)
b+=P('"신뢰받는 패키지"가 경로를 정상 통과한 사례가 공식 기록에 있습니다.','GitHub 공식 블로그(2025년 9월)입니다.','"**2025년 9월 14일, 우리는 Shai-Hulud 공격을 통보받았다.','탈취된 메인테이너 계정을 통해 인기 JavaScript 패키지에','악성 post-install 스크립트를 주입하는 방식으로','npm 생태계에 침투한 자기 복제 웜이다.**"','GitHub은 "**500개 이상의 손상된 패키지를 즉시 제거**"했다고 적었습니다.')
b+=P('이 사례에서 패키지 이름도, 받아오는 주소도 평소와 같았습니다.','달라진 것은 **설치할 때 자동으로 도는 스크립트**였습니다.','경로를 보는 장치가 걸러 줄 수 있는 층이 아닙니다.')
b+=IMG(9,'금_09_공식문서_scripts_순서.png','npm scripts 공식 문서의 Life Cycle Operation Order 중 npm install 항목: preinstall → install → postinstall 순서',SN)
b+=P('그 스크립트가 무엇인지는 npm scripts 문서에 있습니다.','`npm install` 때 **preinstall → install → postinstall** 순서로 실행되고,','"**이것들은 `<pkg-name>`의 scripts에서 실행된다**"고 적혀 있습니다.','패키지를 만든 사람이 `package.json`에 적어 둔 명령이, 설치하는 순간 **내 PC에서** 도는 겁니다.')
b+=P('같은 문서의 Best Practices에는 이런 문장도 있습니다.','"**`install`을 쓰지 마라. 컴파일에는 `.gyp` 파일을, 그 밖에는 `prepare`를 써라.','`preinstall`이나 `install` 스크립트를 명시적으로 둘 일은 거의 없어야 한다.**"','그러니 설치 스크립트가 **있다는 것 자체가** 한 번 읽어 볼 이유가 됩니다.')
b+=Q('"완전히 안전한" 상태는 없다.','위험이 어디에 있는지 알고, 줄이고, 감시하는 것이 할 수 있는 전부다.')
b+=P('질문에 대한 답은 "아니오"였고, 더 정확히는 질문이 잘못돼 있었습니다.','"안전한가"가 아니라 "**위험이 어느 층에 있고, 그 층을 누가 보는가**"를 물었어야 했습니다.')
b+=HR()
b+=H1('3. 설치 전 확인 4가지')
b+=P('그래서 외부 npm 도구를 처음 쓰기 전에 치는 명령을 정했습니다.','넷 다 **설치하기 전에, 읽기만 하는** 확인입니다.')
b+=IMG(10,'금_10_확인명령_재구성.png','독서 노트 앱에 외부 도구를 붙이기 전에 치는 확인 명령: 명령 형태, npm view로 이름·버전·scripts·bin 보기, 버전 고정 실행',SX)
b+=P('**① 명령 형태.** 첫 단어가 정말 그 도구의 패키지 이름인지 README에서 확인합니다.','`npx install <도구>`가 아니라 `npx <도구> install`입니다. 옵션은 패키지 이름 앞에 씁니다.')
b+=P('**② 이름과 버전.** `npm view <도구> name description version`으로','그 이름의 패키지가 무엇인지, 몇 버전인지 봅니다.','설명이 내가 아는 도구와 다르면 거기서 멈춥니다.')
b+=P('**③ 설치 스크립트.** `npm view <도구> scripts`에','`preinstall` · `install` · `postinstall`이 있으면 내용을 읽습니다.','`npm view <도구> bin`으로 npx가 실행할 파일 이름도 봅니다.')
b+=P('**④ 버전 고정.** 검토한 버전을 `npx <도구>@<버전>`처럼 적습니다.','버전을 안 적으면 실행할 때마다 그때의 latest를 받습니다.')
b+=IMG(11,'금_11_공식문서_npmview.png','npm view 공식 문서의 Synopsis와 Description: 패키지 지정자 뒤에 필드 이름을 적어 특정 항목만 보는 예시',SN)
b+=P('②와 ③의 근거입니다.','npm view 문서: "**`npm view [<package-spec>] [<field>[.subfield]...]`**",','"**이 명령은 패키지에 대한 데이터를 보여 주고 stdout에 출력한다.**"','`npm view ronn@0.3.5 dependencies`처럼 **패키지 뒤에 필드 이름**을 적으면 그 항목만 나옵니다.','`scripts`, `bin`, `versions`도 같은 방식입니다. 설치는 일어나지 않습니다.')
b+=IMG(12,'금_12_공식문서_ignorescripts.png','npm config 공식 문서의 ignore-scripts 항목: 기본값 false, 참이면 package.json의 스크립트를 실행하지 않음',SN)
b+=P('③에서 스크립트가 있는 패키지를 그래도 시험해 봐야 한다면 `--ignore-scripts`가 있습니다.','config 문서: "**참이면 npm은 package.json 파일에 지정된 스크립트를 실행하지 않는다.**"','다만 이 옵션은 **설치 스크립트만** 막습니다. npx가 돌리는 실행 파일 자체는 그대로 돕니다.','npx와 조합한 동작을 직접 시험해 보지는 못했습니다 (확인 필요).')
b+=P('④의 근거는 npm exec 형식의 `<pkg>[@<version>]`입니다.','프로젝트 의존성으로 저장할 때도 비슷합니다.','config 문서의 `save-prefix` 기본값은 `"^"`라서 `1.2.3`을 설치하면 `^1.2.3`으로 저장되고, 이것은 **minor 업그레이드를 허용**합니다.','정확한 버전으로 적으려면 `save-exact`를 켭니다. "**의존성이 npm 기본 semver 범위 연산자 대신 정확한 버전으로 package.json에 저장된다.**"')
b+=IMG(13,'금_13_확인4가지.png','명령 형태, 이름과 버전, 설치 스크립트, 버전 고정 — 설치 전 확인 4가지를 정리한 카드')
b+=TABLE(['내가 알고 있던 것','공식 문서 기준'],[
['`npx install <도구>`가 설치 명령이다','첫 단어가 패키지 이름이다. `install`이라는 다른 패키지를 찾는다. 올바른 형태는 `npx <도구> install`'],
['npx는 설치하기 전에 항상 물어본다','로컬에 없으면 묻지만, TTY가 아니거나 CI면 `--yes`로 간주한다'],
['프록시를 통과했으면 안전하다','프록시는 경로의 허용 여부를 정한다. 설치 스크립트와 실행 파일은 내 PC 안에서 돈다 (다른 층)'],
['설치는 파일을 받는 것이다','`npm install`은 패키지의 preinstall → install → postinstall 스크립트를 실행한다'],
['버전은 안 적어도 된다','버전이 없으면 매번 latest. 프로젝트 저장 기본값 `^`는 minor 업그레이드를 허용한다']])
b+=BOX('**정리: 확인된 것과 확인되지 않은 것**','확인됨(문서): npx는 첫 위치 인자를 패키지 지정자로 읽고, 로컬에 없으면 프롬프트(비대화형이면 자동 yes) 뒤 npm 캐시에 설치한다. bin이 하나로 정해지지 않으면 에러로 종료한다. npm install은 패키지의 preinstall·install·postinstall을 실행한다. ignore-scripts는 package.json 스크립트 실행을 막는다. save-prefix 기본값은 ^이다.','확인됨(레지스트리): `install`이라는 패키지가 존재하고(0.13.0), bin과 설치 스크립트가 없다.','확인됨(공식 블로그): 2025-09 Shai-Hulud는 악성 post-install 스크립트를 주입하는 방식이었고 500개 이상의 패키지가 제거됐다.','확인 필요: `npx install <도구>`를 실제로 쳤을 때 에러 전에 캐시 설치까지 진행되는지. `npx --ignore-scripts`의 실제 동작. 프록시가 실제로 수행하는 검사 범위(환경마다 다름).')
b+=HR()
b+=H1('알게 된 것')
b+=P('**명령의 첫 단어가 곧 "받아올 패키지"였습니다.**','`npx install <도구>`는 도구를 설치하는 명령이 아니라','`install`이라는 남의 패키지를 찾는 명령이었습니다.','이번엔 그 이름의 주인이 무해했을 뿐입니다.')
b+=P('**"통과했다"와 "안전하다"는 다른 층의 말이었습니다.**','프록시는 경로를 보고, 설치 스크립트와 실행 파일은 내 PC 안에서 돕니다.','2025년 9월 사고도 경로가 아니라 스크립트 층에서 났습니다.')
b+=P('그래서 지금은 외부 도구를 붙이기 전에','`npm view`로 **이름 · 버전 · scripts · bin**을 읽고, 버전을 적어서 실행하는 것을 순서로 정했습니다.','설치 전에 읽기만 하는 네 줄이 프록시가 대신해 주지 않는 부분입니다.')
b+=HR()
b+=H1('참고자료')
b+=P('[[npm 공식 문서 - npm exec (npx vs npm exec 포함)|https://docs.npmjs.com/cli/v12/commands/npm-exec/]]')
b+=P('[[npm 공식 문서 - scripts (Life Cycle Operation Order, Best Practices)|https://docs.npmjs.com/cli/v12/using-npm/scripts/]]')
b+=P('[[npm 공식 문서 - config (ignore-scripts, save-exact, save-prefix)|https://docs.npmjs.com/cli/v12/using-npm/config/]]')
b+=P('[[npm 공식 문서 - npm view|https://docs.npmjs.com/cli/v12/commands/npm-view/]]')
b+=P('[[npm 레지스트리 - install 패키지|https://www.npmjs.com/package/install]]')
b+=P('[[GitHub 공식 블로그 - Our plan for a more secure npm supply chain (2025-09)|https://github.blog/security/supply-chain-security/our-plan-for-a-more-secure-npm-supply-chain/]]')
b+=P('#npm #npx #공급망보안 #postinstall #버전고정 #npmview #AI코딩도구 #AI활용 #개발입문')
import os
PAGE(T,b,os.environ.get('OUT','/home/claude/out/fri/2026-11-13_금_npx_install_오타_설치전확인.html'))
print('ok')
