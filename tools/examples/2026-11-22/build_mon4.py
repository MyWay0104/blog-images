from lib import *
# 대표 예시: 실습 폴더 api-sdk-lab, 가상환경 .venv, 실행 파일 01_api_direct.py (VS Code에서 Ctrl+F5로 실행)
T='[AI활용] VS Code 가상환경 활성화 안 됨? (.venv) 표시가 없어도 venv로 실행되는 이유와 확인 방법'
SP='출처: Python 공식 문서 "venv — Creation of virtual environments"(docs.python.org/3/library/venv.html), 2026-11-22 캡처'
SV='출처: VS Code 공식 문서 "Python environments in VS Code"(code.visualstudio.com/docs/python/environments), 2026-11-22 캡처'
SR='제 기록에 남아 있던 실행 줄을 바탕으로 다시 그린 터미널 화면 (재구성, 실제 캡처 아님)'
SX='샌드박스(리눅스, Python 3.13.17, uv 0.11.32)에서 실제로 실행한 출력을 옮긴 화면'
b=''
b+=IMG(1,'월_01_썸네일.png','대표 이미지(썸네일)')
b+=P('VS Code에서 파이썬 파일을 Ctrl+F5로 실행했는데,','터미널 프롬프트 앞에 `(.venv)`가 안 붙어 있었습니다.','"가상환경이 안 잡힌 건가? 그럼 지금 어느 파이썬으로 돌고 있는 거지?"')
b+=P('결론부터 적으면,','**==(.venv) 표시가 없어도 가상환경의 파이썬으로 실행될 수 있습니다. 활성화(activate)는 편의 기능이고, 실제로 무엇이 실행됐는지는 파이썬의 경로가 정합니다.==**','그래서 표시를 믿지 말고 **`sys.executable`을 한 번 찍어 보는 것**이 가장 빠른 확인입니다.')
b+=BOX('**이 글의 기준**','확인 날짜: 2026-11-22','제 기록: 2026년 8월, Windows의 VS Code(PowerShell 터미널)에서 uv로 만든 실습 폴더를 Ctrl+F5로 실행했을 때 남긴 메모. 당시 VS Code와 확장의 버전은 기록에 없습니다(확인 필요).','근거: Python 공식 문서 venv(3.15.2 문서), VS Code 공식 문서 "Python environments in VS Code"(문서 표기 02/04/2026), uv 공식 문서','실행 화면: 이번 글을 쓰면서 샌드박스(리눅스)에서 같은 상황을 다시 만들어 실제로 실행했습니다. 그래서 경로가 `.venv/bin/python`으로 나옵니다. Windows에서는 `.venv\\Scripts\\python.exe`입니다.','VS Code 터미널 화면 한 장은 기록을 바탕으로 다시 그린 것입니다.')
b+=HR()
b+=H1('1. 처음에 헷갈렸던 것')
b+=P('실습 폴더 이름은 `api-sdk-lab`, 가상환경은 그 안의 `.venv`, 실행한 파일은 `01_api_direct.py`입니다.','Ctrl+F5(디버깅 없이 실행)를 눌렀더니 터미널에 이런 줄이 찍혔습니다.')
b+=IMG(2,'월_02_터미널_실행줄.png','VS Code의 PowerShell 터미널: 프롬프트에 (.venv) 표시 없이 .venv\\Scripts\\python.exe를 전체 경로로 지정해 01_api_direct.py를 실행한 줄, 그리고 echo $env:VIRTUAL_ENV의 결과가 비어 있는 모습',SR)
b+=P('프롬프트는 `PS C:\\...\\api-sdk-lab>` 그대로이고, `(.venv)`가 없습니다.','`$env:VIRTUAL_ENV`를 찍어 봐도 비어 있었습니다.','그때 남긴 질문이 이것입니다.')
b+=Q('Ctrl+F5 실행 시 .venv가 activate 안 된 상태로 보이는데, 이게 맞나?')
b+=P('그런데 답은 이미 그 실행 줄 안에 있었습니다.','맨 앞을 다시 보면 `python`이 아니라 **`.venv\\Scripts\\python.exe`의 전체 경로**가 적혀 있습니다.')
b+=HR()
b+=H1('2. venv를 쓰는 길은 두 개다')
b+=IMG(3,'월_03_도식_두가지길.png','가상환경을 쓰는 두 가지 길: ① activate 스크립트를 돌려 PATH 앞에 .venv\\Scripts를 끼우고 VIRTUAL_ENV와 (.venv) 표시가 생긴 뒤 python 실행 ② 활성화 없이 .venv\\Scripts\\python.exe를 전체 경로로 직접 실행. 둘 다 같은 인터프리터와 같은 패키지를 쓴다')
b+=P('저는 "가상환경을 쓴다 = 활성화한다"라고 한 덩어리로 알고 있었습니다.','공식 문서를 읽어 보니 둘은 다른 일이었습니다.')
b+=P('**활성화(activate)가 하는 일**은 Python 문서에 이렇게 적혀 있습니다.','"**가상환경은 그 실행 디렉터리(POSIX는 `bin`, Windows는 `Scripts`)의 스크립트로 \'활성화\'할 수 있다. 이 스크립트는 그 디렉터리를 `PATH` 앞에 붙인다. 그래서 python을 실행하면 그 환경의 파이썬 인터프리터가 불린다.**"')
b+=P('즉 활성화는 "그냥 `python`이라고만 쳐도 venv의 파이썬이 잡히게" **길을 바꿔 주는 편의 기능**입니다.','프롬프트의 `(.venv)`와 `VIRTUAL_ENV`는 그때 같이 생기는 표시입니다.')
b+=IMG(4,'월_04_공식문서_Python_venv.png','Python 공식 문서 venv의 How venvs work: 가상환경을 굳이 활성화할 필요는 없고 그 환경의 파이썬 인터프리터 전체 경로를 지정하면 된다. 활성화하면 VIRTUAL_ENV가 설정되지만, 활성화가 필수가 아니므로 VIRTUAL_ENV로 가상환경 사용 여부를 판단할 수 없다',SP)
b+=P('그리고 바로 다음 문단이 제 질문의 답이었습니다.','"**가상환경을 굳이 활성화할 필요는 없다. 파이썬을 부를 때 그 환경의 파이썬 인터프리터 전체 경로를 지정하면 되기 때문이다.**"')
b+=P('한 문단 더.','"**가상환경이 활성화되면 `VIRTUAL_ENV` 환경변수에 그 환경의 경로가 들어간다. 하지만 가상환경을 쓰는 데 명시적인 활성화가 필요하지 않으므로, `VIRTUAL_ENV`로는 가상환경을 쓰고 있는지 판단할 수 없다.**"')
b+=P('제 터미널의 실행 줄은 정확히 이 두 번째 길이었습니다.','활성화 스크립트는 돌리지 않았고, venv 안의 `python.exe`를 전체 경로로 불렀습니다.','그러니 **표시는 없는데 실행은 venv로 된 것**이 맞습니다.')
b+=HR()
b+=H1('3. 직접 돌려서 확인해 봤습니다')
b+=P('말로만 넘어가기 찜찜해서, 같은 구조의 폴더를 만들고 실제로 실행해 봤습니다.','`01_api_direct.py` 맨 위에 "지금 나를 돌리는 파이썬이 누구인지" 찍는 다섯 줄을 넣었습니다.')
b+=CODE('''import os
import sys

print("실행한 파이썬 :", sys.executable)
print("sys.prefix    :", sys.prefix)
print("base_prefix   :", sys.base_prefix)
print("venv 안인가   :", sys.prefix != sys.base_prefix)
print("VIRTUAL_ENV   :", os.environ.get("VIRTUAL_ENV"))''',[('import','#74c0fc'),('sys.executable','#ffd43b'),('sys.prefix != sys.base_prefix','#ffd43b'),('os.environ.get','#8ce99a')])
b+=P('한 줄씩 보면 이렇습니다.','`sys.executable`은 **지금 이 코드를 실행하고 있는 파이썬 파일의 경로**입니다.','`sys.prefix`는 지금 파이썬이 쓰는 환경의 위치, `sys.base_prefix`는 그 환경을 만든 원래 파이썬의 위치입니다.','둘이 다르면 가상환경 안입니다. Python 문서가 "**`sys.prefix != sys.base_prefix`만 확인하면 충분하다**"고 적은 판별식입니다.','`os.environ.get("VIRTUAL_ENV")`는 표시용 환경변수가 채워져 있는지 봅니다.')
b+=IMG(5,'월_05_실행결과_시스템_vs_경로지정.png','실제 실행 결과: ① python3 01_api_direct.py는 /usr/local/bin/python3로 돌고 venv 안인가 False ② .venv/bin/python 01_api_direct.py는 /work/api-sdk-lab/.venv/bin/python으로 돌고 venv 안인가 True인데 VIRTUAL_ENV는 None',SX)
b+=P('①은 가상환경과 상관없는 시스템 파이썬입니다. `venv 안인가: False`.','②가 제 VS Code 상황입니다. **활성화하지 않고 venv의 python을 경로로 직접 불렀더니** `venv 안인가: True`인데 `VIRTUAL_ENV`는 `None`입니다.','표시는 비어 있고, 실행은 venv로 됐습니다.')
b+=IMG(6,'월_06_실행결과_activate_vs_uvrun.png','실제 실행 결과: ③ source .venv/bin/activate 후에는 프롬프트에 (.venv)가 붙고 VIRTUAL_ENV가 채워진다 ④ 활성화하지 않은 터미널에서 uv run python 01_api_direct.py를 실행해도 venv 파이썬으로 돌고 VIRTUAL_ENV가 채워진다',SX)
b+=P('③은 활성화한 경우입니다. 프롬프트에 `(.venv)`가 붙고 `VIRTUAL_ENV`도 채워집니다.','④는 `uv run`입니다. 프롬프트는 그대로인데, 실행된 파이썬은 venv이고 `VIRTUAL_ENV`도 채워져 있었습니다.','(uv가 실행하는 프로그램에 이 값을 넣어 주는 것으로 보입니다. uv 문서에서 이 동작을 설명한 문장은 찾지 못했습니다. 확인 필요)')
b+=IMG(7,'월_07_결과표.png','네 가지 실행 방법의 결과 표: 프롬프트의 (.venv) 표시, VIRTUAL_ENV, 실제로 돈 파이썬. ② 경로 직접 지정은 표시 두 칸이 ①과 똑같이 비어 있지만 실제 파이썬은 ③과 같은 venv')
b+=P('표로 놓으면 한눈에 보입니다.','**②는 표시 두 칸이 ①과 똑같이 비어 있는데, 실제로 돈 파이썬은 ③과 같습니다.**','표시만 봐서는 "시스템 파이썬으로 돈 것"과 "venv로 돈 것"을 구별할 수 없다는 뜻입니다.')
b+=HR()
b+=H1('4. 그럼 VS Code는 어떤 파이썬을 쓰나')
b+=IMG(8,'월_08_공식문서_VSCode_인터프리터.png','VS Code 공식 문서 Python environments의 Select an environment: 상태 표시줄이나 Python: Select Interpreter로 환경을 고르며, 선택된 환경이 코드 실행·디버깅·IntelliSense에 쓰인다. 기본적으로 디버거는 선택된 환경을 쓰고, 다른 인터프리터를 쓰려면 launch.json의 python 속성을 지정한다. Select Interpreter 목록에 .venv가 Workspace로 표시된 예시',SV)
b+=P('VS Code 공식 문서의 설명은 한 문장입니다.','"**선택된 환경이 코드 실행, 디버깅, IntelliSense 같은 언어 기능에 쓰인다.**"')
b+=P('바로 아래 Tip에는 이렇게 적혀 있습니다.','"**기본적으로 디버거는 선택된 환경을 쓴다. 디버깅에 다른 인터프리터를 쓰려면 `launch.json` 디버그 설정의 `python` 속성을 지정하라.**"')
b+=P('그러니 VS Code에서 중요한 것은 "터미널이 활성화됐는가"가 아니라 **"어떤 인터프리터가 선택돼 있는가"**입니다.','선택은 창 오른쪽 아래 상태 표시줄의 파이썬 버전을 누르거나, 명령 팔레트에서 `Python: Select Interpreter`를 실행해서 합니다.','캡처의 목록 맨 아래 줄 `.venv ... .\\.venv\\Scripts\\python.exe  Workspace`가 프로젝트 폴더의 가상환경입니다.')
b+=H2('터미널 자동 활성화는 별도 설정')
b+=IMG(9,'월_09_공식문서_VSCode_터미널설정.png','VS Code 공식 문서의 Terminal settings: 터미널을 열면 확장이 선택된 파이썬 환경을 자동으로 활성화한다. python-envs.terminal.autoActivationType의 기본값은 command',SV)
b+=P('같은 문서에 터미널 이야기도 따로 있습니다.','"**VS Code에서 터미널을 열면, 확장이 선택된 파이썬 환경을 자동으로 활성화해서 `python`, `pip` 같은 명령이 올바른 인터프리터를 쓰게 한다.**"')
b+=P('방식은 `python-envs.terminal.autoActivationType` 설정으로 정합니다.')
b+=TABLE(['값','동작 (공식 문서)'],[
['`command` (기본값)','터미널이 열린 뒤 활성화 명령을 눈에 보이게 실행한다'],
['`shellStartup`','셸 시작 스크립트로 활성화한다. 터미널이 열리는 즉시 환경이 활성 상태다'],
['`off`','자동 활성화를 하지 않는다']])
b+=P('즉 "직접 연 터미널"은 자동으로 활성화해 주는 기능이 따로 있고,','"실행 버튼이 돌리는 파이썬"은 선택된 인터프리터를 쓰는 것이 기본입니다.','제 기록의 터미널은 실행 줄이 `python.exe` 전체 경로였고 `(.venv)` 표시는 없었습니다.','(실행 버튼이 띄운 터미널에 자동 활성화가 어떻게 적용되는지는 VS Code와 확장 버전, 설정에 따라 다를 수 있습니다. 제 환경의 당시 버전은 기록에 없어 확인 필요)')
b+=HR()
b+=H1('5. 불안할 때 확인하는 순서')
b+=IMG(10,'월_10_확인순서.png','확인 순서 3단계: ① VS Code 상태 표시줄에서 선택된 인터프리터가 .venv인지 ② 파일 맨 위에 import sys와 print(sys.executable) ③ print(sys.prefix != sys.base_prefix)가 True인지. 프롬프트의 (.venv)와 VIRTUAL_ENV는 판별 기준으로 쓰지 않는다')
b+=P('**1. 상태 표시줄을 본다.**','오른쪽 아래에 선택된 인터프리터가 `.venv`로 나오는지 확인합니다.')
b+=P('**2. 파일 맨 위에 두 줄을 넣고 실행한다.**')
b+=CODE('''import sys
print(sys.executable)''',[('import','#74c0fc'),('sys.executable','#ffd43b')])
b+=P('출력된 경로에 `.venv`가 들어 있으면 그 가상환경의 파이썬으로 돈 것입니다.','Windows라면 `...\\api-sdk-lab\\.venv\\Scripts\\python.exe` 형태입니다.')
b+=P('**3. 더 확실하게는 판별식 한 줄.**')
b+=CODE('print(sys.prefix != sys.base_prefix)',[('sys.prefix != sys.base_prefix','#ffd43b')])
b+=P('`True`면 가상환경 안입니다.','기록에 "다음에 해볼 것"으로 적어 둔 것도 이것이었습니다. "`sys.executable`을 각 파일에 잠깐 찍어보며 어떤 인터프리터로 돌고 있는지 습관적으로 확인하기."')
b+=HR()
b+=H1('6. 반대 방향의 함정도 있습니다')
b+=P('"표시가 없어도 괜찮다"로 끝내면 반만 맞습니다.','위의 ①처럼, **활성화하지 않은 터미널에서 그냥 `python 01_api_direct.py`를 치면 시스템 파이썬이 잡힐 수 있습니다.**','그러면 `.venv`에 설치한 패키지를 못 찾습니다.')
b+=TABLE(['실행 방법','어느 파이썬이 도나'],[
['VS Code 실행 버튼, Ctrl+F5, F5','선택된 인터프리터 (공식 문서)'],
['활성화된 터미널에서 `python 파일.py`','그 가상환경의 파이썬'],
['활성화 안 된 터미널에서 `python 파일.py`','PATH에서 먼저 잡히는 파이썬 (시스템 파이썬일 수 있음)'],
['`uv run python 파일.py`','프로젝트의 `.venv` (활성화 여부와 무관)']])
b+=P('uv 문서는 `uv run`을 이렇게 설명합니다.','"**`run`을 쓰면 uv는 주어진 명령을 실행하기 전에 프로젝트 환경이 최신 상태인지 확인한다.**"','그리고 "**`uv run` 없이 프로젝트의 스크립트와 명령을 실행하려면 가상환경이 활성화되어 있어야 한다**"고도 적습니다.')
b+=P('그래서 터미널에서 직접 실행할 때는 `uv run python 01_api_direct.py`가 가장 헷갈릴 일이 적습니다.','활성화했는지 기억할 필요가 없기 때문입니다.')
b+=HR()
b+=H1('7. 정리')
b+=IMG(11,'월_11_정리카드.png','정리 카드: 활성화는 PATH 앞에 끼워 넣는 편의 기능, 활성화는 필수가 아니다, VS Code는 선택된 환경으로 실행·디버깅한다, 판별은 sys.prefix != sys.base_prefix로 한다')
b+=TABLE(['내가 처음 생각한 것','확인한 것'],[
['`(.venv)` 표시가 없으면 가상환경이 안 잡힌 것','표시는 활성화 스크립트를 돌렸을 때 생긴다. 전체 경로로 실행하면 표시 없이도 venv로 돈다'],
['가상환경을 쓰려면 반드시 activate 해야 한다','Python 문서: 굳이 활성화할 필요는 없다. 인터프리터 전체 경로를 지정하면 된다'],
['`VIRTUAL_ENV`가 비어 있으면 venv가 아니다','Python 문서: `VIRTUAL_ENV`로는 판단할 수 없다. 실제 실행에서도 비어 있는데 venv였다'],
['VS Code는 터미널을 활성화해서 실행한다','VS Code 문서: 선택된 환경이 실행·디버깅에 쓰인다. 터미널 자동 활성화는 별도 설정이다'],
['표시가 없어도 항상 괜찮다','활성화 안 된 터미널에서 그냥 `python`을 치면 시스템 파이썬이 잡힐 수 있다']])
b+=BOX('**확인된 것과 확인되지 않은 것**','확인됨(공식 문서): 활성화는 PATH 앞에 실행 폴더를 붙이는 일이라는 것, 활성화 없이 전체 경로로 실행할 수 있다는 것, `VIRTUAL_ENV`로는 판단할 수 없고 `sys.prefix != sys.base_prefix`로 판별한다는 것, VS Code에서 선택된 환경이 실행·디버깅에 쓰인다는 것, 터미널 자동 활성화 설정의 세 값','확인됨(실제 실행): 샌드박스 리눅스에서 네 가지 실행 방법의 출력','확인 필요: 제 Windows VS Code에서 같은 다섯 줄을 다시 찍어 본 것은 아닙니다. 당시 화면은 기록의 실행 줄을 바탕으로 다시 그렸습니다. 실행 버튼이 띄운 터미널에 자동 활성화가 적용되는 조건, uv run이 `VIRTUAL_ENV`를 채우는 동작의 문서 근거는 확인하지 못했습니다.')
b+=HR()
b+=H1('알게 된 것')
b+=P('**"활성화됐는가"와 "어느 파이썬으로 도는가"는 다른 질문이었습니다.**','저는 화면의 표시로 두 번째 질문에 답하려고 했는데, 표시는 첫 번째 질문의 답일 뿐이었습니다.')
b+=P('**확인은 표시가 아니라 경로로 합니다.**','`print(sys.executable)` 한 줄이면 끝나는 일을, 프롬프트만 보면서 불안해하고 있었습니다.')
b+=HR()
b+=H1('참고자료')
b+=P('[[Python 공식 문서 - venv (How venvs work)|https://docs.python.org/3/library/venv.html#how-venvs-work]]')
b+=P('[[VS Code 공식 문서 - Python environments in VS Code|https://code.visualstudio.com/docs/python/environments]]')
b+=P('[[VS Code 공식 문서 - Python debugging in VS Code|https://code.visualstudio.com/docs/python/debugging]]')
b+=P('[[uv 공식 문서 - Running commands|https://docs.astral.sh/uv/concepts/projects/run/]]')
b+=P('[[uv 공식 문서 - Working on projects|https://docs.astral.sh/uv/guides/projects/]]')
b+=P('#VSCode #파이썬가상환경 #venv #가상환경활성화 #uv #sysexecutable #파이썬 #AI활용 #개발입문')
import os
PAGE(T,b,os.environ.get('OUT','/home/claude/out/mon/2026-11-23_월_VSCode_venv_표시와_실제.html'))
print('ok')
