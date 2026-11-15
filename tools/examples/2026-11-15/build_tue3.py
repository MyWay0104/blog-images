from lib import *
# 대표 예시: Notion을 글 저장소로 쓰는 Next.js 16 블로그(notion-blog). 환경변수 5개: NOTION_TOKEN, NOTION_DATA_SOURCE_ID, NEXT_PUBLIC_SITE_URL, REVALIDATE_SECRET, NODE_ENV
T='[AI활용] Next.js 환경변수 NEXT_PUBLIC_ 차이: 브라우저에 노출되는 값과 서버에만 두는 값'
SN='출처: Next.js 공식 문서(nextjs.org, 2026-08-25 갱신 표시), 2026-11-15 캡처'
SV='출처: Vercel 공식 문서(vercel.com), 2026-11-15 캡처'
SX='제 프로젝트의 변수 이름과 공식 문서의 설명을 바탕으로 재구성한 예시 화면 (값은 자리 표시이며 실제 파일이 아닙니다)'
b=''
b+=IMG(1,'화_01_썸네일.png','대표 이미지(썸네일)')
b+=P('Notion을 글 저장소로 쓰는 Next.js 16 블로그를 배포하기 전에','환경변수를 한 줄씩 다시 봤습니다.','Notion 토큰, 데이터 소스 ID, 사이트 주소, 캐시 갱신 비밀번호.','이 중 어떤 것에 `NEXT_PUBLIC_`을 붙여야 하는지가 문제였습니다.')
b+=Q('환경변수는 값 저장소이자 보안 경계다.','공개 가능한 URL과 공개하면 안 되는 토큰·시크릿을 구분한다.','NEXT_PUBLIC_은 브라우저에 전달될 수 있다는 의미다.')
b+=P('결론부터 적으면,','**==`NEXT_PUBLIC_`은 "이 값을 빌드 때 브라우저용 JS에 박아 넣어도 된다"는 선언입니다.==**','사이트 주소처럼 어차피 공개된 값에만 붙이고,','토큰·비밀번호는 접두사 없이 서버에만 둡니다.')
b+=BOX('**이 글의 기준**','확인 날짜: 2026-11-15 (프로젝트 기록은 2026-08)','근거: 제 프로젝트 학습 기록(환경변수 5개의 역할과 운영 원칙) + Next.js 공식 문서 "How to use environment variables in Next.js"(2026-08-25 갱신 표시), Vercel 공식 문서 "Config and Secret environment variables"','`.env` 화면은 변수 이름만 실제이고 값은 자리 표시로 바꾼 재구성 화면입니다. 실제 토큰 값은 어디에도 적지 않았습니다.','예시 이름은 `notion-blog`로 통일했습니다.')
b+=HR()
b+=H1('1. 환경변수가 사는 두 세계')
b+=IMG(2,'화_02_도식_두환경.png','서버(Node.js)에서는 process.env 전부가 읽히고, next build 때 NEXT_PUBLIC_ 값만 JS 번들에 인라인되어 브라우저로 가는 구조를 그린 도식')
b+=P('Next.js 앱은 코드가 **두 곳**에서 돌아갑니다.','서버(Node.js)와, 방문자의 브라우저입니다.','서버 쪽 코드(Route Handler, Server Component, Server Action)는 `process.env`의 값을 전부 읽을 수 있습니다.')
b+=P('브라우저는 다릅니다. 방문자가 개발자 도구를 열면 **JS 파일을 그대로 볼 수 있는 곳**입니다.','그래서 Next.js는 기본적으로 환경변수를 브라우저에 보내지 않습니다.')
b+=IMG(3,'화_03_공식문서_환경변수_개요.png','Next.js 공식 문서 환경변수 가이드의 첫 부분: .env로 환경변수를 읽고, NEXT_PUBLIC_ 접두사로 브라우저용 번들에 포함한다는 안내와 .gitignore 경고',SN)
b+=P('공식 문서는 두 가지 기능으로 시작합니다.','"**`.env`를 사용해 환경변수를 불러온다**",','"**`NEXT_PUBLIC_` 접두사를 붙여 브라우저용으로 환경변수를 번들에 포함한다**".','그리고 바로 경고가 붙습니다. "`create-next-app` 기본 템플릿은 모든 `.env` 파일을 `.gitignore`에 넣는다. 이 파일들을 저장소에 커밋할 일은 거의 없다."')
b+=HR()
b+=H1('2. NEXT_PUBLIC_이 실제로 하는 일: 빌드 때 값을 박는다')
b+=IMG(4,'화_04_공식문서_브라우저번들.png','Next.js 공식 문서 "Bundling Environment Variables for the Browser": 접두사 없는 변수는 Node.js 환경에서만 쓸 수 있고, NEXT_PUBLIC_ 값은 빌드 시점에 번들에 인라인된다는 설명과 빌드 뒤 값이 굳는다는 Note',SN)
b+=P('이 절이 핵심이었습니다.','"**`NEXT_PUBLIC_`이 아닌 환경변수는 Node.js 환경에서만 쓸 수 있다. 브라우저에서는 접근할 수 없다**(클라이언트는 다른 환경에서 돌기 때문)."')
b+=P('"**브라우저에서 값을 쓸 수 있게 하려면, Next.js는 빌드 시점에 값을 JS 번들에 "인라인"할 수 있다.','`process.env.[variable]`에 대한 모든 참조를 하드코딩된 값으로 바꾸는 것이다.**"','즉 접두사는 권한 설정이 아니라, **빌드할 때 코드 안의 변수 자리를 값 문자열로 치환하라**는 표시입니다.')
b+=P('그래서 문서의 Note가 중요합니다.','"**빌드가 끝난 뒤에는 앱이 이 환경변수들의 변경에 더 이상 반응하지 않는다.**"','하나의 Docker 이미지를 여러 환경에 배포하면 `NEXT_PUBLIC_` 값은 전부 **빌드 때 평가된 값으로 얼어붙는다**고 적혀 있습니다.')
b+=IMG(5,'화_05_env파일_재구성.png','notion-blog의 .env.local 구성(값은 자리 표시)과, 빌드 뒤 브라우저 JS에서 NEXT_PUBLIC_SITE_URL은 문자열로 박히고 NOTION_TOKEN은 undefined가 되는 모습',SX)
b+=P('제 프로젝트에 대입하면 위와 같습니다.','`NEXT_PUBLIC_SITE_URL`은 빌드 뒤 번들 안에서 주소 문자열이 되고,','`NOTION_TOKEN`은 번들에 들어가지 않아 브라우저에서는 `undefined`입니다.')
b+=IMG(6,'화_06_공식문서_인라인예시.png','Next.js 공식 문서의 인라인 예시: process.env.NEXT_PUBLIC_ANALYTICS_ID가 빌드 때 값으로 바뀌는 코드와, 변수로 돌려 읽는 동적 조회는 인라인되지 않는다는 예시',SN)
b+=P('한 가지 함정도 문서에 있습니다.','"**동적 조회는 인라인되지 않는다.**"','`const varName = "NEXT_PUBLIC_..."; process.env[varName]`처럼 변수로 돌려 읽거나,','`const env = process.env; env.NEXT_PUBLIC_...`처럼 한 번 담아서 읽으면 치환이 안 됩니다.','빌드 도구가 **글자 그대로 `process.env.NEXT_PUBLIC_이름`**을 찾아 바꾸기 때문입니다.')
b+=HR()
b+=H1('3. 제 프로젝트의 변수 5개를 나눠 보면')
b+=IMG(7,'화_07_프로젝트변수_카드.png','notion-blog 환경변수 5개(NOTION_TOKEN, NOTION_DATA_SOURCE_ID, NEXT_PUBLIC_SITE_URL, REVALIDATE_SECRET, NODE_ENV)의 역할과 어디에 두는지 정리한 표')
b+=P('**`NOTION_TOKEN`** — Notion Integration 인증. 글을 읽고 쓰는 권한이라 서버에만 둡니다.','**`NOTION_DATA_SOURCE_ID`** — 글이 들어 있는 Data Source의 위치 식별자. 비밀번호는 아니지만 브라우저에 보낼 이유가 없어 접두사 없이 둡니다.')
b+=P('**`NEXT_PUBLIC_SITE_URL`** — sitemap, canonical, OG 이미지 주소를 만들 때 쓰는 사이트 절대 주소.','어차피 주소창에 보이는 값이라 접두사를 붙여도 됩니다.')
b+=Q('NEXT_PUBLIC_SITE_URL에는 유료 도메인이 없어도 된다. Vercel이 제공하는 안정된 주소를 쓴다.','끝에 /를 붙이지 않는다. 비워 두면 sitemap, canonical URL, Open Graph 이미지 주소 등이 잘못 만들어질 수 있다.')
b+=P('**`REVALIDATE_SECRET`** — 외부에서 캐시 갱신 API를 부를 때 "진짜 관리자인가"를 확인하는 비밀번호.','기록에 이렇게 적어 두었습니다.')
b+=Q('NEXT_PUBLIC_ 접두사를 붙이면 브라우저에 노출될 수 있으므로 절대 붙이지 않는다.')
b+=P('**`NODE_ENV`** — 직접 적지 않습니다. 이 부분은 아래에서 공식 문서로 확인합니다.')
b+=IMG(8,'화_08_도식_결정기준.png','"이 값이 브라우저에 보여도 되는가"라는 질문으로 NEXT_PUBLIC_을 붙일지, 접두사 없이 서버에만 둘지 가르는 결정 흐름')
b+=P('정리하면 새 변수를 추가할 때 묻는 질문은 하나였습니다.','**이 값이 브라우저에 보여도 되는가?**','되면 `NEXT_PUBLIC_`, 아니면 접두사 없이 서버에만 둡니다.','헷갈리면 "아니오" 쪽에 둡니다. 서버에만 있던 값을 나중에 공개하기는 쉽지만, 한 번 번들에 실린 값은 되돌릴 수 없기 때문입니다.')
b+=HR()
b+=H1('4. 배포 서비스 쪽: Vercel의 Config와 Secret')
b+=IMG(9,'화_09_Vercel_Secret.png','Vercel 공식 문서 "Config and Secret environment variables": Config는 저장 뒤에도 읽을 수 있고, Secret은 저장 뒤 쓰기 전용이며 비밀번호·API 키·토큰에 쓴다는 설명',SV)
b+=P('환경변수를 Vercel에 등록할 때는 **타입**을 고릅니다.','"**Config 값은 저장 뒤에도 접근 권한이 있는 멤버가 읽을 수 있다.** 공개 접두사 같은 민감하지 않은 설정에 쓴다."','"**Secret 값은 저장 뒤 쓰기 전용이다.** 비밀번호, API 키, 토큰에 쓴다."')
b+=P('그래서 `NOTION_TOKEN`과 `REVALIDATE_SECRET`은 Secret으로,','`NEXT_PUBLIC_SITE_URL`은 Config로 두는 것이 문서의 분류와 맞습니다.','문서에는 "Secret 값이 32자 이상이고 빌드 로그에 나타나면 `[REDACTED]`로 바꾼다"는 설명도 있습니다.')
b+=P('주의할 점: Vercel의 Secret은 "대시보드에서 값을 숨긴다"는 뜻이지,','코드에서 `NEXT_PUBLIC_`을 붙인 값을 브라우저에서 숨겨 주지는 않습니다.','**접두사 판단은 코드 쪽에서, 보관 방식은 배포 서비스 쪽에서** 각각 해야 합니다. (이 문장은 두 문서를 읽고 제가 정리한 것입니다.)')
b+=HR()
b+=H1('5. 런타임에 읽는 길과 NODE_ENV')
b+=IMG(10,'화_10_공식문서_런타임.png','Next.js 공식 문서 "Runtime Environment Variables": 기본적으로 환경변수는 서버에서만 쓸 수 있고, connection()을 쓰는 동적 렌더링에서는 서버가 런타임에 값을 읽는다는 설명과 예시 코드',SN)
b+=P('"**기본적으로 환경변수는 서버에서만 쓸 수 있다.**"','문서는 서버에서 동적 렌더링을 할 때 `process.env.MY_VALUE`를 **런타임에** 읽는 예시를 보여 줍니다.','그래서 "하나의 Docker 이미지를 여러 환경에 승격시키며 값만 바꾸는" 운영이 가능하다고 설명합니다.','브라우저에 값이 필요하다면 빌드 때 박거나, 직접 API를 만들어 넘겨 주라는 것이 문서의 선택지입니다.')
b+=IMG(11,'화_11_공식문서_로드순서.png','Next.js 공식 문서 "Environment Variable Load Order": process.env → .env.$(NODE_ENV).local → .env.local → .env.$(NODE_ENV) → .env 순서와, NODE_ENV가 없으면 next dev는 development, 그 외는 production으로 자동 지정된다는 Good to know',SN)
b+=P('`NODE_ENV`를 직접 적지 않은 이유도 문서에 있습니다.','"**`NODE_ENV`가 지정되지 않았으면 Next.js는 `next dev`를 실행할 때 자동으로 `development`를, 그 외 모든 명령에서는 `production`을 지정한다.**"','허용되는 값은 `production`, `development`, `test` 세 가지뿐입니다.')
b+=Q('.env에 직접 넣었다면 production으로 바꾸기보다 수동 설정을 제거하는 편이 안전하다.')
b+=P('읽는 순서도 적어 둘 만합니다.','`process.env` → `.env.$(NODE_ENV).local` → `.env.local` → `.env.$(NODE_ENV)` → `.env` 순서로 찾고,','**먼저 찾으면 멈춥니다.** 같은 이름을 두 파일에 두면 앞쪽이 이깁니다.')
b+=CODE('''# 문서 기준 — 어디에 두고 무엇을 올리나
.env                 # 공통 기본값. 저장소에 올려도 되는 값만
.env.local           # 내 PC 전용 비밀값. .gitignore 대상
.env.development     # next dev 때만
.env.production      # next build / start 때만
# NODE_ENV 는 적지 않는다. next dev → development, 그 외 → production''',[('.env.local','#ffd43b'),('NODE_ENV','#ff8787')])
b+=HR()
b+=H1('6. 정리')
b+=IMG(12,'화_12_정리카드.png','기본은 서버 전용, 빌드 때 값이 박힌다, 읽는 순서와 NODE_ENV, Vercel의 Secret 타입 — 공식 문서로 확인한 네 가지 카드')
b+=TABLE(['내가 처음 생각한 것','공식 문서로 확인한 것'],[
['NEXT_PUBLIC_은 "읽기 권한"을 주는 설정','빌드 때 코드 안의 process.env.이름을 값 문자열로 치환하라는 표시다. 빌드 뒤에는 값이 굳는다'],
['접두사 없는 값도 브라우저에서 읽을 수 있다','기본적으로 환경변수는 서버에서만 쓸 수 있다. 브라우저 번들에는 들어가지 않는다'],
['process.env를 변수에 담아 써도 된다','동적 조회(process.env[이름], env.이름)는 인라인되지 않는다. 글자 그대로 써야 한다'],
['NODE_ENV는 내가 설정해야 한다','지정하지 않으면 next dev는 development, 그 외는 production으로 자동 지정된다'],
['Vercel에 Secret으로 두면 안전하다','Secret은 저장 뒤 값을 숨기는 타입이다. NEXT_PUBLIC_을 붙인 값이 브라우저로 가는 것과는 별개다']])
b+=BOX('**확인된 것과 확인되지 않은 것**','확인됨(공식 문서): 접두사 없는 변수는 Node.js 환경 전용, NEXT_PUBLIC_은 빌드 시점 인라인, 빌드 뒤 값 고정, 동적 조회 미인라인, 런타임 읽기(connection), 로드 순서 5단계, NODE_ENV 자동 지정과 허용 값 3가지(Next.js), Config/Secret 구분과 빌드 로그 REDACTED(Vercel)','확인됨(제 기록): 변수 5개의 역할과 운영 원칙, NEXT_PUBLIC_SITE_URL 끝에 / 없이 두는 이유, NODE_ENV 수동 설정 제거','확인 필요: 빌드된 번들 파일을 열어 실제로 값이 박힌 모습은 이번에 직접 확인하지 못했습니다(샌드박스에서 Next.js 설치 불가). 위 .env 화면은 재구성입니다.')
b+=HR()
b+=H1('알게 된 것')
b+=P('**NEXT_PUBLIC_은 권한이 아니라 치환 표시였습니다.**','빌드 때 코드 안의 자리를 값으로 바꿔 브라우저용 JS에 실어 보냅니다.','그래서 붙이는 순간 그 값은 공개된 것으로 봐야 했습니다.')
b+=P('**판단은 "브라우저에 보여도 되는가" 하나로 충분했습니다.**','사이트 주소는 예, 토큰과 비밀번호는 아니오.','헷갈리면 아니오 쪽에 두고, 필요해지면 그때 공개하는 편이 안전합니다.')
b+=P('**코드 쪽 판단과 배포 서비스 쪽 보관은 따로 해야 했습니다.**','접두사는 코드에서, Secret 타입은 Vercel에서.','하나를 했다고 다른 하나가 해결되지는 않습니다.')
b+=HR()
b+=H1('참고자료')
b+=P('[[Next.js 공식 문서 - How to use environment variables in Next.js|https://nextjs.org/docs/app/guides/environment-variables]]')
b+=P('[[Vercel 공식 문서 - Config and Secret environment variables|https://vercel.com/docs/environment-variables/sensitive-environment-variables]]')
b+=P('[[Vercel 공식 문서 - Environment variables|https://vercel.com/docs/environment-variables]]')
b+=P('#Nextjs #환경변수 #NEXT_PUBLIC #Vercel #env #보안 #웹개발입문 #AI활용 #개발입문')
import os
PAGE(T,b,os.environ.get('OUT','/home/claude/out/tue/2026-11-17_화_Nextjs_환경변수_NEXT_PUBLIC.html'))
print('ok')
