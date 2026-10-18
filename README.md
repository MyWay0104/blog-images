# blog-images

네이버 블로그 [AI활용] 글의 본문 이미지 저장소. 폴더는 게시일_요일, 파일은 요일_번호.png (원고의 이미지 번호와 같다).

주의: 글에서 이 주소를 그대로 참조하면 파일을 지우거나 옮길 때 글의 이미지가 깨진다.

## 폴더

- `YYYY-MM-DD_요일/`: 글 1건의 이미지. 파일은 `요일_번호.png`
- `tools/`: 원고·도식·썸네일을 만드는 스크립트와 그 주의 예시. 사용법은 `tools/README.md`
- 이미지 주소는 GitHub Pages 주소를 쓴다: `https://myway0104.github.io/blog-images/<폴더>/<파일>`
- `.nojekyll`: Pages가 Jekyll 처리를 건너뛰고 파일을 그대로 내보내게 한다
