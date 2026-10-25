# Weekly Blog 원고 빌더

네이버 블로그 [AI활용] 글을 만드는 스크립트 모음. 새 세션에서는 이 저장소를 받아 `tools/`를 작업 폴더로 복사해 쓴다.
규칙(글 형식, 이미지 규칙, 썸네일 규칙)은 프로젝트 문서 `Weekly Blog 운영 지침.md`가 기준이고, 여기 코드는 그 규칙을 구현한 것이다. 규칙이 바뀌면 코드도 같이 고친다.

## 파일

| 파일 | 역할 |
|---|---|
| `lib.py` | 원고 HTML 생성 도우미. 모든 서식을 인라인 `style`로 넣는다(네이버 붙여넣기용). `P` 문단, `H1`/`H2` 소제목, `Q` 인용, `BOX` 회색 상자, `CODE` 코드 상자, `TABLE` 표, `IMG` 이미지, `PAGE` 파일 출력 |
| `shot.py` | HTML을 PNG로 렌더링. `python3 shot.py in.html out.png 1080` (높이 생략 시 `#card` 요소만 찍음), `python3 shot.py in.html out.png 1080 1080` (고정 크기) |
| `thumb.py` | 1080×1080 썸네일 틀. 상단 45% 글자, 하단 55% SVG 그림. `make(name, out, bg, bg2, ac, l1, l2, sub, svg, fs)` |
| `dia.css` | 도식 공통 CSS. 폭 1080px, `:root{--bg;--fg;--ac}`를 각 도식에서 지정 |
| `examples/<실행일>/` | 그 주에 실제로 쓴 빌드 스크립트, 썸네일 스크립트, 도식 HTML. 새 글을 만들 때 복사해서 고친다 |

## 환경

- Python 3 + Playwright(Chromium). 샌드박스에는 미리 설치되어 있다. `python3 -c "import playwright"`로 확인
- 글꼴: 도식·썸네일은 Noto Sans CJK KR(Black 포함), 코드는 DejaVu Sans Mono. `fc-list | grep -i "noto sans cjk"`로 확인
- PIL(Pillow): 캡처 자르기와 미리보기 합치기에 쓴다

## 글 1건 만드는 순서

1. `examples/`에서 비슷한 글의 `build3_요일.py`를 복사해 원고를 쓴다. 대표 예시 이름을 파일 첫 줄 주석에 적는다.
2. 공식 문서 캡처는 PC 브라우저로 찍어 PIL로 잘라 `요일_NN_내용.png`로 저장한다.
3. 도식은 `dia.css`를 쓰는 HTML로 그리고 `shot.py`로 렌더링한다. 썸네일은 `th3_요일.py`를 복사해 만든다.
4. 이미지 번호는 원고에 나오는 순서와 같게 맞춘다. 이미지를 모두 만든 뒤 `grep -o '\[이미지 [0-9]*: [^|]*' 원고.html`로 순서를 확인한다.
5. 이미지를 이 저장소에 올린다: 폴더 `<게시일>_<요일>` (예 `2026-10-19_mon`), 파일 `<요일>_<번호>.png` (예 `mon_01.png`). 한글 파일명은 주소에 쓰지 않는다.
6. 커밋·푸시 뒤 1~2분 기다린다(Pages 반영).
7. 주소 참조 버전을 만든다:
   ```
   IMG_URL_BASE=https://myway0104.github.io/blog-images/2026-10-19_mon python3 build3_mon_url.py
   ```
   `build3_요일_url.py`는 출력 파일명만 `_이미지주소포함.html`로 바꾼 사본이다.
8. 원고 HTML(주소 참조 버전)과 썸네일 PNG를 대화에 전달한다. 썸네일은 대표 이미지로 따로 올려야 하므로 반드시 파일로 준다.

## lib.py 모드

| 환경변수 | 동작 |
|---|---|
| (없음) | `[이미지 N: 파일명 | 설명]` 회색 상자. 사용자가 이미지를 직접 올리는 예전 방식 |
| `IMG_URL_BASE=<폴더 주소>` | `<img src="<폴더 주소>/<요일>_<번호>.png">`. 기본 방식 |
| `EMBED_DIR=<폴더>` | base64로 본문에 내장. 네이버가 거부하므로 쓰지 않는다(2026-10-18 확인) |

글꼴은 `lib.py`의 `FF` 상수로 모든 글자 요소에 `나눔스퀘어`를 지정한다(네이버에서 적용 확인, 2026-10-18).

## 네이버 붙여넣기에서 확인된 것 (2026-10-18)

- 인라인 `style` 서식(굵게, 형광펜, 표, 회색 상자, 코드 상자)과 `<img src="https://...">` 외부 이미지는 붙여넣기로 들어간다.
- base64 `data:` 이미지는 PNG·JPEG·WebP·GIF 모두 "허용되지 않는 형식의 이미지"로 거부된다.
- 발행 후에도 이미지 주소는 이 저장소 주소 그대로다. 파일을 지우거나 옮기면 글이 깨진다.
- `raw.githubusercontent.com`은 비인증 요청 속도 제한 대상이라 쓰지 않는다. Pages 주소(`myway0104.github.io/blog-images/...`)를 쓴다.

## 2026-10-25 추가

| 파일 | 역할 |
|---|---|
| `crop.py` | PC 브라우저 캡처(jpg)를 잘라 PNG로 저장. `python3 crop.py <원본> <출력> <top> <bottom> [left right]`. 오른쪽 스크롤바 15px는 기본으로 잘라 낸다 |
| `term.css` | 터미널·코드 화면 재구성용 공통 CSS (`#card` 1080px, `.bar` 제목줄, `.body` 본문, 색 클래스 `.p .c .g .y .v`) |
| `pushday.sh` | 하루치 이미지를 `<게시일>_<요일>/<요일>_<번호>.png`로 복사해 커밋·푸시하고, `IMG_URL_BASE`를 넣어 `_이미지주소포함.html`을 만든다. `bash pushday.sh 월 mon 2026-10-26 build_mon.py` |

- 이번 주 빌드 스크립트는 `build_<요일>.py` 하나로 두고, 출력 파일명은 환경변수 `OUT`으로 바꾼다(`_url.py` 사본을 만들지 않는다).
- 실제 실행 가능한 명령(git, Playwright `aria_snapshot()`, `page.evaluate`)은 샌드박스에서 돌려 그 출력을 `term.css`로 그렸다. 원고의 출처 줄에 "실제 실행" 또는 "재구성"을 구분해 적는다.
