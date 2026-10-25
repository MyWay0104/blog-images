from lib import *
# 대표 예시: 내 저장소 = YOUR-USERNAME/reading-notes (독서 노트 앱), 남의 저장소 = octocat/Spoon-Knife (GitHub 공식 연습용 저장소)
T='[AI활용] git fork vs clone 차이: 내 저장소를 다른 PC로 가져올 때 fork가 필요 없는 이유'
SRC='출처: GitHub Docs, 2026-10-25 캡처'
b=''
b+=IMG(1,'월_01_썸네일.png','대표 이미지(썸네일)')
b+=P('오픈소스 도구 하나를 써 보려고','저장소 주소를 받았는데요.','열어 보니 원본이 아니라','누군가 **fork**한 저장소였습니다.')
b+=P('그때 처음으로 궁금해졌습니다.','fork가 정확히 뭐지?','내가 늘 쓰던 `git clone`이랑 뭐가 다르지?')
b+=P('결론부터 말하면','**==fork는 서버 안에서 복사, clone은 서버에서 내 PC로 복사==**입니다.','"어디서 어디로"가 다릅니다.')
b+=P('이 한 줄이 잡히기 전까지','제가 뭘 잘못 생각했는지부터 적어 보겠습니다.')
b+=BOX('**이 글의 기준**','확인 날짜: 2026-10-25','근거: GitHub Docs (About forks, Fork a repository, Syncing a fork, Cloning a repository), Git 공식 문서 (git-clone)','환경: Windows, Git과 GitHub 계정이 있는 상태','예시는 내 저장소 `reading-notes`(독서 노트 앱)와 GitHub 공식 연습용 저장소 `octocat/Spoon-Knife`로 통일했습니다.')
b+=HR()
b+=H1('처음에 제가 헷갈렸던 것')
b+=Q('이거 근데 원본 git이 있고 forked git이 있는데 무슨 차이야?','forked하면 마지막 git 상태로 가져와서','내가 내 마음대로 git 수정하면서 추가 개발 할 수 있다는 뜻인가?')
b+=P('그리고 이해했다고 생각하고','바로 이렇게 적용했습니다.')
b+=Q('아, 그러면 다른 PC에서 github에 올린 내 개인과제 당겨갈 때','git clone이 아니라 fork를 해야겠다.')
b+=P('이 두 번째 문장이 틀렸습니다.','당시 제 머릿속은 이랬습니다.')
b+=BOX('**당시의 오해**','fork는 "마지막 커밋 상태만" 가져오는 것이라고 생각했다.','fork와 clone을 같은 종류의 동작(코드를 가져오는 것)으로 여겼다.','그래서 "내 것을 가져올 때도 fork"라고 잘못 적용했다.')
b+=P('하나씩 공식 문서로 풀어 보겠습니다.')
b+=HR()
b+=H1('1. fork는 GitHub 서버 안에서 일어나는 복사다')
b+=IMG(2,'월_02_공식문서_fork정의.png','GitHub Docs의 fork 정의',SRC)
b+=P('GitHub 문서의 정의는 이렇습니다.','"**fork는 다른 저장소(upstream 저장소)의 복사본으로 시작하는 저장소다.**','**자기만의 설정과 권한을 갖지만 upstream 저장소와 연결은 유지된다.**"')
b+=P('핵심은 두 가지입니다.')
b+=P('첫째, fork는 **저장소 하나가 새로 생기는 것**입니다.','브랜치가 아닙니다.','문서도 "브랜치는 한 저장소의 일부이고,','fork는 자기 설정과 협업 공간을 가진 별도 저장소"라고 구분합니다.')
b+=P('둘째, 이 복사는 **GitHub 서버 안에서** 일어납니다.','남의 계정에 있던 저장소가','내 계정 아래에 하나 더 생기는 것입니다.','내 PC에는 아직 아무것도 오지 않았습니다.')
b+=IMG(3,'월_03_fork_clone_방향.png','fork는 원격에서 원격으로, clone은 원격에서 로컬로 복사하는 방향 도식')
b+=P('그래서 "마지막 상태만 가져온다"는 제 생각은 틀렸습니다.','fork는 저장소를 통째로 복사하므로','**커밋 이력도 같이 복사됩니다.**')
b+=P('fork 대화 상자에 "기본 브랜치만 복사" 선택지가 있는데,','이건 브랜치 수를 줄이는 옵션이지','이력을 잘라 내는 옵션이 아닙니다.')
b+=HR()
b+=H1('2. clone은 서버에서 내 PC로 내려받는 것이다')
b+=P('반대로 `git clone`은 Git 자체의 명령입니다.','Git 공식 문서는 이렇게 적습니다.')
b+=P('"**저장소를 새로 만든 디렉터리에 복제하고,**','**복제한 저장소의 각 브랜치에 대해**','**원격 추적 브랜치를 만든다.**"')
b+=P('GitHub 문서(Cloning a repository)는 더 쉽게 말합니다.','"저장소를 복제하면 GitHub.com에서 내 컴퓨터로 저장소를 복사한다.','그 시점의 모든 저장소 데이터,','**모든 파일과 폴더의 모든 버전**을 내려받는다."')
b+=P('즉 clone도 이력을 통째로 가져옵니다.','다만 도착지가 **내 PC**입니다.')
b+=IMG(4,'월_04_공식문서_fork후clone.png','GitHub Docs: fork를 만든 뒤에도 파일은 아직 내 컴퓨터에 없다는 설명',SRC)
b+=P('이 문장이 저한테는 제일 결정적이었습니다.','"**이제 Spoon-Knife 저장소의 fork가 생겼지만,**','**그 저장소의 파일은 아직 당신 컴퓨터에 없다.**"')
b+=P('fork를 했든 안 했든,','작업하려면 결국 clone을 합니다.','**fork는 clone을 대신하는 게 아니라 clone 앞에 붙는 단계**였습니다.')
b+=P('실제로 clone이 이력을 통째로 가져오는지','연습용 저장소로 확인해 봤습니다.')
b+=IMG(5,'월_05_터미널_clone과_log.png','git clone 뒤 git log로 커밋 이력이 함께 내려온 것을 확인한 터미널 화면','샌드박스에서 실제로 실행한 결과 (octocat/Spoon-Knife)')
b+=P('clone 직후 `git log --oneline`을 치면','원본의 커밋이 그대로 보입니다.','"마지막 상태만"이 아니라 **이력 전체**입니다.')
b+=HR()
b+=H1('3. 그러면 fork는 언제 필요한가')
b+=P('GitHub 문서의 한 줄이 답입니다.','"**fork하면 upstream 저장소에 영향을 주지 않고**','**프로젝트에 변경을 제안할 수 있다.**"')
b+=P('즉 fork의 목적은','**원본에 쓰기 권한이 없을 때**','내 마음대로 push할 곳을 확보하는 것입니다.')
b+=TABLE(['상황','필요한 것','이유'],[
['남의 저장소를 고쳐서 쓰고 싶다','fork → clone','원본에 push 권한이 없으니 내 계정에 복사본이 있어야 push할 수 있다'],
['남의 저장소를 그냥 쓰기만 한다','clone','읽기만 하면 되니 내 계정에 복사본이 필요 없다'],
['**내 저장소**를 다른 PC로 가져온다','clone','이미 내 소유라 push 권한이 있다. fork할 이유가 없다']])
b+=P('세 번째 줄이 제 질문의 답이었습니다.','`reading-notes`는 제 저장소이고','저는 이미 push 권한이 있습니다.','다른 PC에서는 **clone만 하면 끝**입니다.')
b+=CODE('''git clone https://github.com/YOUR-USERNAME/reading-notes.git
cd reading-notes
git remote -v''',[('git clone','#9775fa'),('git remote -v','#9775fa')])
b+=P('`git clone` 뒤에 내 저장소 주소를 붙입니다.','`cd`로 받아진 폴더에 들어갑니다.','`git remote -v`로 `origin`이 내 저장소를 가리키는지 확인합니다.')
b+=P('이게 전부입니다.','여기서 작업하고 `git push`하면','GitHub의 내 저장소에 그대로 올라갑니다.')
b+=HR()
b+=H1('4. fork를 했다면 upstream을 등록해 둔다')
b+=P('반대로 `Spoon-Knife`처럼 남의 저장소를','fork해서 고쳐 쓰는 경우에는','저장소가 **세 개**가 됩니다.')
b+=IMG(6,'월_06_세_저장소_관계.png','upstream(원본), origin(내 fork), 내 PC(clone) 세 저장소의 관계와 명령 흐름 도식')
b+=TABLE(['이름','어디에','무엇'],[
['`upstream`','GitHub, 남의 계정','원본 저장소 (octocat/Spoon-Knife)'],
['`origin`','GitHub, 내 계정','내 fork (YOUR-USERNAME/Spoon-Knife)'],
['로컬','내 PC','origin을 clone한 작업 폴더']])
b+=P('fork를 clone하면 `origin`은 **내 fork**를 가리킵니다.','원본은 자동으로 등록되지 않습니다.','그래서 문서는 `upstream`이라는 이름으로','원본을 직접 추가하라고 합니다.')
b+=IMG(7,'월_07_공식문서_upstream추가.png','GitHub Docs: git remote add upstream 명령과 git remote -v 결과',SRC)
b+=CODE('''git clone https://github.com/YOUR-USERNAME/Spoon-Knife.git
cd Spoon-Knife
git remote add upstream https://github.com/octocat/Spoon-Knife.git
git remote -v''',[('git remote add upstream','#9775fa')])
b+=P('`git remote add upstream`은','"upstream이라는 이름으로 이 주소를 기억해 둬라"는 뜻입니다.','그 뒤 `git remote -v`를 치면','`origin` 두 줄과 `upstream` 두 줄이 같이 보입니다.')
b+=H2('원본이 업데이트되면')
b+=P('fork는 만든 순간부터 **원본과 따로 갑니다.**','원본에 새 커밋이 생겨도','내 fork에는 자동으로 오지 않습니다.')
b+=P('받아오는 방법은 두 가지입니다.')
b+=IMG(8,'월_08_공식문서_Syncfork.png','GitHub Docs: 웹 화면의 Sync fork 메뉴',SRC)
b+=P('하나는 GitHub 웹 화면의 **Sync fork** 메뉴입니다.','fork 저장소 페이지에서 파일 목록 위에 있습니다.')
b+=P('다른 하나는 명령어입니다.')
b+=CODE('''git fetch upstream
git checkout main
git merge upstream/main''',[('git fetch upstream','#9775fa'),('git merge upstream/main','#9775fa')])
b+=P('`git fetch upstream`은 원본의 브랜치와 커밋을 가져오기만 합니다.','`git checkout main`으로 내 기본 브랜치로 옮깁니다.','`git merge upstream/main`으로 원본의 변경을 내 브랜치에 합칩니다.')
b+=P('문서는 이 과정이','"로컬 변경을 잃지 않고 fork의 기본 브랜치를 동기화한다"고 하면서,','**로컬만 바뀌므로 GitHub의 fork를 갱신하려면 push해야 한다**고 덧붙입니다.')
b+=P('제가 fork에 손을 많이 댈수록','이 merge에서 충돌이 날 가능성이 커집니다.','그래서 "고쳐 쓸 게 설정값 몇 개뿐이라면','fork보다 설정으로 해결하는 게 싸다"는 생각이 들었습니다.','이 부분은 제 판단입니다.')
b+=HR()
b+=H1('5. fork와 clone, 한 장으로 정리')
b+=IMG(9,'월_09_요약카드.png','fork와 clone의 차이와 선택 기준 요약 카드')
b+=TABLE(['','fork','clone'],[
['어디서 어디로','GitHub 서버 → GitHub 서버 (남의 계정 → 내 계정)','GitHub 서버 → 내 PC'],
['무엇이 생기나','내 계정에 새 저장소','내 PC에 작업 폴더'],
['이력','통째로 복사','통째로 복사'],
['누구 기능','GitHub의 기능','Git의 명령'],
['필요한 때','원본에 push 권한이 없을 때','코드를 PC에서 다루려는 모든 때']])
b+=P('fork와 clone은 "어디서 어디로"가 다릅니다.','**==fork는 서버 안, clone은 서버에서 내 PC==**.','이 한 줄이 잡히니까','"내 것을 가져올 때 fork"가 왜 틀렸는지 바로 보였습니다.')
b+=HR()
b+=H1('알게 된 것')
b+=P('남의 저장소 주소를 받으면','이제는 **원본인지 fork인지부터** 봅니다.','문서에 따르면 fork 저장소 페이지에는','이름 아래에 upstream 저장소가 표시됩니다.')
b+=P('fork라면 원본과 차이가 있는지 확인하고,','차이가 없으면 **원본 기준**으로 씁니다.','제가 받았던 주소도 그랬습니다.')
b+=P('그리고 fork는 GitHub 안에서만 동작하는 기능입니다.','GitHub가 아닌 다른 Git 서버로 저장소를 옮길 때는','fork가 아니라 clone한 뒤','그 서버 주소를 remote로 추가해 push합니다.','이 부분은 제가 직접 해보지는 않았습니다. (확인 필요)')
b+=P('Python으로 비유하면','`pip install`로 받아 쓰는 게 clone 쪽에 가깝고,','저장소를 fork해 고친 뒤','그 fork에서 설치하는 게 fork 기반 사용입니다.','대가로 원본의 버전업을 직접 따라가야 합니다.')
b+=HR()
b+=H1('참고자료')
b+=P('[[GitHub Docs - About forks|https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-forks]]')
b+=P('[[GitHub Docs - Fork a repository|https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo]]')
b+=P('[[GitHub Docs - Syncing a fork|https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork]]')
b+=P('[[GitHub Docs - Cloning a repository|https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository]]')
b+=P('[[Git 공식 문서 - git-clone|https://git-scm.com/docs/git-clone]]')
b+=P('#git #github #fork #clone #upstream #AI활용 #개발입문 #버전관리')
import os
PAGE(T,b,os.environ.get('OUT','/home/claude/out/mon/2026-10-26_월_git_fork_vs_clone.html'))
print('ok')
