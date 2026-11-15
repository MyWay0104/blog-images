# 2026-11-15 실행 (게시 11-16 ~ 11-20) 스크립트 보관

- `build_*3.py` : 요일별 원고 빌드 (lib.py 사용). `IMG_URL_BASE`를 주면 이미지 주소가 GitHub Pages 주소로 들어간다.
- `th_*3.py` + `thumb.py` : 1080×1080 썸네일 (요일마다 강조색 계열이 다름: 월 crimson, 화 amber, 수 indigo, 목 pink, 금 teal)
- `f_*.html`(월) `g_*.html`(화) `h_*.html`(수) `i_*.html`(목) `j_*.html`(금) : 본문 도식 원본. `python3 shot.py <html> <png> 1080`으로 렌더
- `check.sh` : 이미지 번호 순서·파일 존재·`**` 잔존·금지어 점검. 금지어 목록은 저장소에 두지 않고 `FORBID` 환경변수나 로컬 `forbid.txt`로 준다
- `pushday.sh` : 요일 이미지를 `<날짜>_<요일>/<요일>_NN.png`로 복사·커밋·푸시하고 `_이미지주소포함.html`을 빌드
- `api-sdk-lab/` : 수요일 글의 로컬 시험 서버(`fake_openai_server.py`)와 requests 직접 호출 예제(`01_api_direct.py`)
- `reading-notes-eval/rule_judge.py` : 목요일 글의 pydantic 규칙 판정기
