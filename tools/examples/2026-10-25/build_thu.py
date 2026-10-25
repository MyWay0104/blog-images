from lib import *
# 대표 예시: Claude Code를 자체 모델 서버(ANTHROPIC_BASE_URL)에 연결해 쓰는 환경. 설정 파일은 %USERPROFILE%\.claude\settings.json
T='[AI활용] Claude Code 외부 통신 끄기: CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC 설정 방법'
SRC='출처: Claude Code 공식 문서, 2026-10-25 캡처'
b=''
b+=IMG(1,'목_01_썸네일.png','대표 이미지(썸네일)')
b+=P('Claude Code를 쓰면서','"AI 코딩 도구는 코드를 외부 LLM 서버로 보낸다"는','말을 들었을 때 저는 이렇게 반박했습니다.')
b+=P('"저는 모델을 자체 서버로 연결해서 쓰니까','밖으로 나갈 일이 없다."')
b+=P('반박은 맞았습니다.','그런데 그게 전부가 아니었습니다.','**==모델 호출 말고도 Claude Code가 밖과 통신하는 경로가 따로 있고,==**','**==그건 모델이 어디 있든 상관없이 일어납니다.==**')
b+=P('공식 문서(Data usage)를 열어 확인한 내용과','그걸 끄는 설정을 정리합니다.')
b+=BOX('**이 글의 기준**','확인 날짜: 2026-10-25','근거: Claude Code 공식 문서 (Data usage, Environment variables, Settings)','**직접 적용한 기록이 아니라 공식 문서 기준 정리**입니다. 아래 설정을 제 환경에 넣고 프록시 로그로 확인하는 일은 아직 하지 않았습니다.','예시 환경: Windows, 모델은 `ANTHROPIC_BASE_URL`로 자체 서버에 연결. 설정 파일은 `%USERPROFILE%\\.claude\\settings.json`','문서 내용은 버전에 따라 바뀝니다. 적용 전에 링크의 최신 문서를 다시 확인하세요.')
b+=HR()
b+=H1('처음에 제가 생각한 것')
b+=Q('(제가 쓰는) 클로드코드는 내부에서만 서빙되는 (자체) 모델을 사용한다.','클로드코드 자체가 외부로 데이터를 보낼일은 없어')
b+=P('이 말에 대한 답은 "그 부분은 맞다, 그러나"였습니다.')
b+=BOX('**당시의 오해**','앞 답변의 "코드를 외부 LLM 서버로 보낸다"는 말은 기본 설정(Anthropic API 직접 연결)을 전제로 한 것이었다. 모델을 자체 서버로 연결했다면 모델 호출을 통한 외부 전송 경로는 없다. 여기까지는 맞았다.','그런데 "모델 호출만 막으면 외부 전송이 전부 막힌다"고 생각한 것이 틀렸다.')
b+=P('"모델이 안에 있다"와','"도구가 밖으로 아무것도 보내지 않는다"는','**다른 문장**이었습니다.')
b+=HR()
b+=H1('1. 모델 호출 외의 통신은 무엇이 있나')
b+=IMG(2,'목_02_공식문서_Telemetry.png','Claude Code 공식 문서의 Telemetry services 절',SRC)
b+=P('공식 문서 Data usage의 Telemetry services 절은','"**Claude Code는 두 종류의 운영 텔레메트리를 보낸다:**','**사용 지표와 오류 보고**"로 시작합니다.')
b+=TABLE(['통신','무엇을 보내나 (공식 문서)','보내지 않는 것'],[
['**사용 지표**(Metrics)','지연 시간, 안정성, 사용 패턴. Anthropic과 제3자 로깅 인프라로','"**코드, 프롬프트, 파일 경로는 절대 포함하지 않는다**"'],
['**오류 보고**(Error reports)','Claude Code 내부의 오류 메시지와 스택 트레이스','비밀값·파일 경로·이메일 등은 떠나기 전에 가림. Pro/Max 로그인 + API 직접 연결일 때만 켜짐'],
['**세션 만족도 설문**','"How is Claude doing?" 평점만','대화 내용은 두 번째 질문에서 "Yes"를 눌러야만 전송'],
['**/feedback, /bug**','대화 기록과 코드 포함','사용자가 직접 실행할 때만'],
['**WebFetch 도메인 안전 검사**','접속하려는 **호스트 이름**을 `api.anthropic.com`에 보내 차단 목록과 대조','전체 URL, 경로, 페이지 내용은 보내지 않음'],
['**설치·업데이트, 플러그인 마켓 자동 등록**','배포 서버, 공식 플러그인 마켓플레이스','—']])
b+=IMG(3,'목_03_통신경로_도식.png','모델 호출, 비모델 통신, 도구가 만드는 통신 세 경로를 나눈 구조 도식')
b+=P('그림으로 놓으면 경로가 세 갈래입니다.','① 모델 호출(자체 서버로 감), ② 비모델 통신(위 표),','③ **AI가 실행하는 도구가 만드는 통신**.')
b+=P('③이 제일 놓치기 쉬웠습니다.','Claude Code가 Bash로 `curl`이나 `npx`를 실행하거나','WebFetch, MCP 서버를 쓰면','그 통신은 **모델이 어디서 서빙되든** 일어납니다.','이건 설정이 아니라 **권한 규칙과 네트워크**로 다룰 일입니다.')
b+=HR()
b+=H1('2. 제공자에 따라 기본값이 다르다')
b+=IMG(4,'목_04_공식문서_제공자별기본값.png','공식 문서의 Default behaviors by API provider 절 도입부',SRC)
b+=P('문서는 이렇게 적습니다.','"**Amazon Bedrock, Google Cloud\'s Agent Platform, Microsoft Foundry,**','**Claude Platform on AWS를 쓸 때는**','**오류 보고, 텔레메트리, 버그 보고가 기본으로 꺼진다.**"')
b+=P('그리고 바로 예외를 답니다.','"**세션 만족도 설문과 WebFetch 도메인 안전 검사는 예외이며**','**제공자와 무관하게 실행된다.**"')
b+=IMG(5,'목_05_공식문서_기본값표.png','공식 문서의 제공자별 기본값 표',SRC)
b+=P('표를 보면 열이 **공식 제3자 제공자**(Vertex, Bedrock, Foundry, AWS)로 나뉩니다.')
b+=BOX('**확인하지 못한 것**','`ANTHROPIC_BASE_URL`로 **자체 서버**를 지정한 경우가 이 표의 어느 열에 해당하는지는 문서에서 확정하지 못했습니다. 표에는 그 경우가 따로 없습니다.','그래서 저는 "기본값이 꺼져 있을 것"이라고 가정하지 않고, 아래처럼 **직접 끄는 설정을 넣는 쪽**으로 정리했습니다. (확인 필요)')
b+=HR()
b+=H1('3. WebFetch 검사는 따로 끈다')
b+=IMG(6,'목_06_공식문서_WebFetch검사.png','공식 문서의 WebFetch domain safety check 절',SRC)
b+=P('WebFetch 도메인 안전 검사 절이 핵심입니다.')
b+=P('"**URL을 가져오기 전에 WebFetch 도구는 요청된 호스트 이름을**','**`api.anthropic.com`에 보내 Anthropic이 관리하는 안전 차단 목록과 대조한다.**','**호스트 이름만 보내며, 전체 URL·경로·페이지 내용은 보내지 않는다.**"')
b+=P('그리고 이 문장.','"**이 검사는 어떤 모델 제공자를 쓰든 실행되며,**','**`CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`의 영향을 받지 않는다.**"')
b+=P('끄려면 설정 파일에 `skipWebFetchPreflight: true`를 넣습니다.','단, 문서는 경고를 붙입니다.','검사를 끄면 차단 목록 없이 아무 URL이나 가져오려 하므로','**WebFetch 권한 규칙으로 허용 도메인을 제한하는 것과 함께** 쓰라고 합니다.')
b+=HR()
b+=H1('4. 끄는 설정 두 가지')
b+=IMG(7,'목_07_공식문서_환경변수항목.png','공식 문서 Environment variables의 CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC 항목',SRC)
b+=H2('CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC')
b+=P('문서 설명을 그대로 옮기면 이렇습니다.','"**`1` 같은 비어 있지 않은 값으로 설정하면 필수가 아닌 네트워크 통신을 끈다:**','**자동 업데이트, 텔레메트리, 오류 보고, `/feedback` 명령,**','**릴리스 노트, PR 상태 배지 확인, 가용성 확인 등.**"')
b+=P('주의할 점 두 가지가 문서에 있습니다.')
b+=BOX('**주의**','"`0`이나 `false`로 설정해도 여전히 꺼진다." 대부분의 on/off 변수와 다르다. 다시 켜려면 변수를 **지워야** 한다.','기능 플래그 가져오기도 꺼지므로 Remote Control 등 일부 기능을 쓸 수 없게 된다.','**공식 플러그인 마켓플레이스 자동 등록은 이 변수로 안 꺼진다.** 아래 변수가 따로 필요하다.')
b+=H2('CLAUDE_CODE_DISABLE_OFFICIAL_MARKETPLACE_AUTOINSTALL')
b+=P('"**`1`로 설정하면 공식 플러그인 마켓플레이스의 자동 등록을 끈다.**"','문서에 따르면 Claude Code는 보통 **첫 대화형 실행 때** 이 변수를 읽고,','그때 설정되어 있으면 등록을 영구히 건너뜁니다.','나중에 변수를 지워도 건너뛴 것이 되돌아오지 않습니다.')
b+=HR()
b+=H1('5. 설정 파일에 넣는 방법')
b+=IMG(8,'목_08_공식문서_env설정.png','공식 문서의 Set variables in settings files 절',SRC)
b+=P('환경변수는 터미널마다 따로 잡지 않아도 됩니다.','문서는 "**`settings.json`의 `env` 키 아래에 변수를 넣으면**','**어떻게 `claude`를 실행했든 적용된다**"고 합니다.')
b+=IMG(9,'목_09_settings_예시.png','settings.json에 env와 skipWebFetchPreflight를 넣은 예시','공식 문서의 형식을 바탕으로 재구성한 예시 화면')
b+=CODE('''{
  "env": {
    "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1",
    "CLAUDE_CODE_DISABLE_OFFICIAL_MARKETPLACE_AUTOINSTALL": "1"
  },
  "skipWebFetchPreflight": true
}''',[('"env"','#22b8cf'),('"skipWebFetchPreflight"','#22b8cf')])
b+=P('`env` 안의 두 줄은 환경변수가 됩니다.','문서대로 값은 **쓴 그대로** 복사되고 셸이 처리하지 않으니','`"1"`처럼 문자열로 적습니다.')
b+=P('`skipWebFetchPreflight`는 환경변수가 아니라 **설정 항목**이라','`env` 바깥에 둡니다.')
b+=P('파일 위치는 문서 기준으로 이렇습니다.')
b+=TABLE(['파일','적용 범위'],[
['`~/.claude/settings.json` (Windows: `%USERPROFILE%\\.claude\\settings.json`)','나, 모든 프로젝트'],
['`.claude/settings.json`','그 프로젝트 (공유)'],
['`.claude/settings.local.json`','그 프로젝트, 나만'],
['관리자가 배포한 managed 설정','조직이 정함']])
b+=P('개별 변수도 있습니다.','지표만 끄려면 `DISABLE_TELEMETRY=1`,','오류 보고만 끄려면 `DISABLE_ERROR_REPORTING=1`,','설문만 끄려면 `CLAUDE_CODE_DISABLE_FEEDBACK_SURVEY=1`.','(각각 Data usage 문서의 Telemetry services 절과 표에 있습니다)')
b+=HR()
b+=H1('6. 적용 순서')
b+=IMG(10,'목_10_적용순서.png','확인, 설정, WebFetch 제한, 로그 확인 네 단계의 적용 순서 카드')
b+=P('제가 다음에 실제로 할 순서입니다. 아직 하지 않았습니다.')
b+=P('**1. 이미 있는 설정부터 봅니다.**','관리자가 배포한 설정이나 `settings.json`의 `env`에','이 변수들이 이미 들어 있을 수 있습니다.')
b+=P('**2. 없으면 넣습니다.**','통신 변수 두 개는 `env`에, `skipWebFetchPreflight`는 설정 항목에.')
b+=P('**3. WebFetch 허용 도메인을 좁힙니다.**','검사를 끈 대가로 차단 목록이 사라지니','권한 규칙으로 갈 수 있는 도메인을 제한합니다.')
b+=P('**4. 실제 통신을 봅니다.**','연습용 저장소에서 세션 하나를 돌리고','프록시 로그에 `api.anthropic.com`이나 통계 도메인이 찍히는지 봅니다.','찍히면 어느 항목이 남았는지 거꾸로 추적합니다.')
b+=P('설정이 "꺼졌다"는 문서의 말이고,','"실제로 안 나간다"는 **로그로 확인할 일**입니다.')
b+=HR()
b+=H1('알게 된 것')
b+=P('**"모델이 안에 있다"와 "도구가 외부로 아무것도 보내지 않는다"는 다른 문장**입니다.','두 번째는 설정을 열어 봐야 말할 수 있습니다.')
b+=P('제 반박이 맞았을 때','"맞다"로 끝나지 않고','"그 부분은 맞다, 그러나 이 통신은 따로 있다"로','범위를 좁혀 준 것이 유용했습니다.','반박이 맞아도 나머지 주장이 자동으로 참은 아니었습니다.')
b+=P('그리고 제품 세부 사항은','기억이 아니라 **공식 문서를 열어** 확인하는 게 맞았습니다.','문서로 확정하지 못한 것(`ANTHROPIC_BASE_URL` 경우)은','"확인 필요"로 남겨 두는 게 정직한 상태입니다.')
b+=HR()
b+=H1('참고자료')
b+=P('[[Claude Code 공식 문서 - Data usage|https://code.claude.com/docs/en/data-usage]]')
b+=P('[[Claude Code 공식 문서 - Environment variables|https://code.claude.com/docs/en/env-vars]]')
b+=P('[[Claude Code 공식 문서 - Settings|https://code.claude.com/docs/en/settings]]')
b+=P('#ClaudeCode #데이터사용 #텔레메트리 #환경변수 #settingsjson #WebFetch #AI코딩도구보안 #AI활용')
import os
PAGE(T,b,os.environ.get('OUT','/home/claude/out/thu/2026-10-29_목_Claude_Code_외부통신_끄기.html'))
print('ok')
