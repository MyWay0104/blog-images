from lib import *
# 대표 예시: 독서 노트 앱. 노트 문서(ReadingNote) + 표지 이미지. 스토리지 key "covers/2026/book-07.png"
T='[AI활용] MongoDB vs 객체 스토리지(S3·MinIO) 차이: DB에는 주소록, 스토리지에는 물건'
b=''
b+=IMG(1,'목_01_썸네일.png','대표 이미지(썸네일)')
b+=P('대화형 Agent를 멀티턴으로 바꾸면서','회원별 대화 내용을 MongoDB에 저장하게 됐습니다.')
b+=P('그런데 쓰다 보니 이상했습니다.','회원 ID로 대화를 통째로 꺼내 오기만 하니','이게 DB인지 창고(스토리지)인지','구분이 안 되더라고요.')
b+=P('결론부터 말하면','MongoDB는 RDBMS도 스토리지도 아닌 **문서형 DB**이고,','**==DB에는 주소록, 스토리지에는 물건==**을 둡니다.','저는 이걸 정반대로 이해하고 있었습니다.')
b+=BOX('**이 글의 기준**','확인 날짜: 2026-10-18','근거: MongoDB 공식 문서(Documents, Databases and Collections, GridFS), Amazon S3 공식 문서(What is Amazon S3)','MongoDB와 S3·MinIO를 운영해 본 후기가 아니라, 개념을 정리하고 공식 문서로 확인한 글입니다.','예시는 독서 노트 앱으로 통일했습니다.')
b+=HR()
b+=H1('처음에 제가 헷갈렸던 것')
b+=Q('MongoDB는 RDBMS인가 아니면, Storage인가?','이런 구조를 취했을 때, 몽고DB는 스토리지의 성격으로 봐야할 거 같은데, 저장되는 파일의 형식이 RDBMS 친화적인 csv나 table 형식인지, 아니면 단순 자연어의 나열인지, 아니면 어느정도 구조화된 json 파일인지 궁금해.')
b+=P('설명을 듣고 객체 스토리지로 넘어가자 더 막혔습니다.')
b+=Q('스토리지 객체에 대한 개념이 안잡히고 있는데, 실체가 없이 공간만 차지한다는 게 이해가 안돼','어딘가에 분명 저장 되어야 할 텐데 이게 어땋게 가능해?')
b+=Q('그럼 db에 남긴다는 건 실제로 파일이 거기에 있다는 거고 스토리지에 남긴다는 건 경로만 남긴 채로 어딘가 서버에 여러개로 나누어져서 저장된다는거야?')
b+=P('마지막 질문은 **방향이 거꾸로**였습니다.','하나씩 풀어 보겠습니다.')
b+=HR()
b+=H1('1. MongoDB 안에는 JSON 모양의 문서가 들어 있다')
b+=IMG(2,'목_02_MongoDB_문서_BSON.png','MongoDB 공식 문서의 문서(Document)와 BSON 설명','출처: MongoDB 공식 문서 (Documents), 2026-10-18 캡처')
b+=P('MongoDB 문서는 이렇게 적습니다.','"**MongoDB는 데이터 레코드를 BSON 문서로 저장한다.**','**BSON은 JSON 문서의 바이너리 표현이지만**','**JSON보다 더 많은 데이터 유형을 포함한다.**"')
b+=P('그러니까 제 세 가지 후보 중 답은','CSV도, 자연어 나열도 아닌 **구조화된 JSON**이었습니다.','디스크에는 BSON이라는 이진 형식으로 적히고,','꺼내면 다시 JSON(Python에서는 dict)이 됩니다.')
b+=P('필드 값으로는 문서 안에 **다른 문서나 배열**도 넣을 수 있다고 합니다.','그래서 대화 한 건의 메시지 목록을','별도 테이블로 떼지 않고 한 문서 안에 품을 수 있습니다.')
b+=HR()
b+=H1('2. RDBMS, 문서형 DB, 스토리지는 "무엇을 받고 어떻게 찾느냐"가 다르다')
b+=IMG(3,'목_03_세가지_구분.png','RDBMS, 문서형 DB, 객체 스토리지가 받는 것·찾는 방법·내용 이해의 차이 도식')
b+=TABLE(['','RDBMS','문서형 DB (MongoDB)','객체 스토리지 (S3, MinIO)'],[
['받는 것','스키마에 맞는 행','JSON 문서','바이트 덩어리'],
['찾는 방법','SQL로 관계를 조합','필드 조건으로 검색','key 하나로 통째로'],
['내용을','열 단위로 이해','필드 단위로 이해','**해석하지 않음**']])
b+=P('MongoDB가 "스토리지처럼" 느껴졌던 진짜 이유는','**제가 JOIN을 안 했기 때문**이었습니다.','관계를 질문하지 않으니 창고처럼 보였을 뿐,','문서 안의 필드로 검색할 수 있으면 DB입니다.')
b+=IMG(4,'목_04_MongoDB_컬렉션.png','MongoDB 공식 문서의 컬렉션 설명','출처: MongoDB 공식 문서 (Databases and Collections), 2026-10-18 캡처')
b+=P('자리 대응도 공식 문서에 있습니다.','"**MongoDB는 문서를 컬렉션에 저장한다.**','**컬렉션은 관계형 데이터베이스의 테이블과 유사하다.**"')
b+=IMG(5,'목_05_자리_대응.png','RDBMS의 Database·Table·Row와 MongoDB의 Database·Collection·Document 대응 도식')
b+=TABLE(['RDBMS','MongoDB','차이'],[
['Database','Database','같음'],
['Table','Collection','같은 자리'],
['Row','Document','Row는 평평한 열 묶음, Document는 중첩 JSON']])
b+=P('한 가지 주의할 점이 있습니다.','문서는 "**기본적으로 한 컬렉션 안의 문서들이 스키마를 공유하지 않는다.**','**필드와 데이터 유형이 문서마다 다를 수 있다**"고 합니다.')
b+=P('"스키마가 없다"는 건 모양이 없다는 뜻이 아니라','**DB가 강제하지 않는다**는 뜻입니다.','검증 부담이 코드로 옮겨 오니','Pydantic 모델로 모양을 고정해 두는 게 안전합니다.')
b+=HR()
b+=H1('3. 객체 스토리지의 "객체"는 실체가 있다')
b+=IMG(6,'목_06_S3_객체_정의.png','Amazon S3 공식 문서의 object, bucket, key 정의','출처: Amazon S3 공식 문서 (What is Amazon S3?), 2026-10-18 캡처')
b+=P('S3 문서의 정의는 단순합니다.','"**object는 파일과 그 파일을 설명하는 메타데이터다.**','**bucket은 object를 담는 컨테이너다.**','**각 object는 bucket 안에서 유일한 식별자인 key를 가진다.**"')
b+=P('즉 "객체"는 Python의 `object`와 무관하고','**"파일 하나"** 정도로 읽으면 됩니다.','바이트는 분명히 어느 서버의 디스크에 적혀 있습니다.')
b+=IMG(7,'목_07_층_내려가기.png','디스크, 파일 시스템, 객체 스토리지 세 층의 관계 도식')
b+=P('층을 내려가 보면 이렇습니다. (제 이해)')
b+=BOX('**아래에서 위로**','디스크: 실제 바이트가 적히는 곳','파일 시스템: 어느 블록에 적혔는지 기록하고, 폴더 트리로 찾게 해 줌','객체 스토리지: 폴더 트리를 버리고 key 문자열 하나로만 찾음. 여러 서버에 걸쳐 key → 위치 목록을 관리하고 HTTP로 넣고(PUT) 꺼냄(GET)')
b+=P('"스토리지는 내용을 모른다"는 말은','내용이 **없다**가 아니라 **해석하지 않는다**는 뜻입니다.','PDF를 넣으면 PDF로 돌려주지만','몇 페이지인지는 들여다보지 않습니다.')
b+=P('내부에서 복제하거나 조각내는 것은','스토리지의 내부 사정이고,','밖에서는 **key 하나로 통째로** 돌아옵니다.')
b+=HR()
b+=H1('4. 방향 정정: 물건은 스토리지에, 주소록은 DB에')
b+=P('제가 거꾸로 이해했던 부분입니다.')
b+=IMG(8,'목_08_MongoDB_GridFS.png','MongoDB 공식 문서의 GridFS와 16MiB 문서 크기 제한 설명','출처: MongoDB 공식 문서 (GridFS), 2026-10-18 캡처')
b+=P('MongoDB 문서에 따르면','"**BSON 문서 크기 제한은 16MiB**"이고,','그보다 큰 파일은 GridFS라는 별도 방식으로','청크로 나눠 저장합니다.','즉 큰 파일을 문서에 그대로 넣는 건','애초에 DB가 권하는 길이 아닙니다.')
b+=IMG(9,'목_09_주소록_물건.png','독서 노트 JSON은 DB에, 표지 이미지는 스토리지에 두고 key로 연결하는 구조 도식')
b+=P('독서 노트 앱으로 옮기면 이렇습니다.','노트 본문(작은 JSON)은 DB에,','책 표지 스캔 이미지(수 MB)는 객체 스토리지에 둡니다.','DB에는 그 이미지를 가리키는 **key와 상태**만 남깁니다.')
b+=CODE('''# DB에 남기는 것: 주소록 (Pydantic으로 모양을 고정)
class ReadingNote(BaseModel):
    note_id: str
    user_id: str                 # 회원 ID. 문서 안의 필드 + 인덱스
    messages: list[Message]      # [{role, content, ts}, ...] 중첩 JSON
    cover_key: str | None        # 스토리지 key: "covers/2026/book-07.png"
    cover_status: str            # "uploaded" | "pending"
    updated_at: datetime

# 스토리지에서 꺼내는 것: 물건 (key로 bytes를 돌려줌)
data = s3.get_object(Bucket="covers", Key=note.cover_key)["Body"].read()''',[('cover_key','#4dabf7'),('get_object','#4dabf7'),('class','#ffd43b'),('BaseModel','#ffd43b')])
b+=P('`ReadingNote`가 DB의 문서 모양입니다.','`messages`는 중첩 배열로 한 문서 안에 들어갑니다.','`cover_key`는 **실제 이미지가 아니라 그 위치**입니다.','마지막 줄이 그 key로 스토리지에서 바이트를 꺼냅니다.')
b+=P('둘 다 디스크에 적히므로','"실체"의 차이가 아니라 **"역할"의 차이**입니다.')
b+=H2('회원 ID는 컬렉션 이름이 아니라 필드로')
b+=P('여기서부터는 공식 문서가 아니라 **설계 검토에서 나온 제 판단**입니다.')
b+=P('회원마다 컬렉션을 따로 만들면','"최근 일주일 전체 대화량" 같은 질문에','컬렉션을 전부 순회해야 하고','인덱스도 회원 수만큼 생깁니다.','한 컬렉션에 `user_id` 필드 + 인덱스가','같은 접근을 만족하면서 운영이 단순합니다.')
b+=HR()
b+=H1('5. 지금 내 DB에 뭐가 들었는지 확인하는 법')
b+=P('저장 구조를 설명하기 전에','**실제 문서 모양부터 열어 보는 것**이','추측보다 빠릅니다.')
b+=IMG(10,'목_10_확인_방법.png','mongosh로 실제 문서 모양을 확인하는 두 줄과 결과 해석 카드')
b+=CODE('''// mongosh에서
db.getCollectionNames()      // 1. 컬렉션 이름 목록
db.<컬렉션이름>.findOne()     // 2. 문서 하나의 실제 모양''',[('getCollectionNames','#4dabf7'),('findOne','#4dabf7')])
b+=P('첫 줄로 컬렉션 이름을 보고,','둘째 줄로 문서 하나를 그대로 꺼내 봅니다.')
b+=BOX('**결과 해석**','`messages` 배열이 읽히면 → 직접 설계한 JSON 문서. 필드로 검색 가능','`checkpoint: Binary(...)` 같은 이진 값이 보이면 → LangGraph checkpointer(`MongoDBSaver`)가 직렬화해 넣은 것. 메시지 내용으로는 검색이 안 됨 (정확한 필드 구성은 `langgraph-checkpoint-mongodb` 버전마다 달라 확인 필요)')
b+=IMG(11,'목_11_mongosh_findOne_예시.png','mongosh에서 컬렉션 목록과 findOne() 결과를 재구성한 예시. 최상위 필드 이름에 표시','공식 문서의 문서 구조 설명을 바탕으로 재구성한 예시 화면입니다. 값은 독서 노트 앱 예시입니다.')
b+=P('객체 스토리지 쪽은 MinIO를 로컬에 띄워 보면','파일 하나를 올린 뒤 데이터 폴더 안에','원본 바이트와 메타데이터 파일이 실제로 생기는 걸','눈으로 확인할 수 있다고 합니다.','(저는 아직 직접 해보지 않았습니다. 확인 필요)')
b+=HR()
b+=H1('정리')
b+=BOX('**외워 둘 문장 셋**','MongoDB는 문서형 DB. 안에는 구조화된 JSON(BSON)이 들어 있고, 필드로 검색할 수 있으면 DB다.','객체 스토리지의 "객체"는 파일 하나. 실체가 없는 게 아니라 내용을 해석하지 않을 뿐이다.','물건(큰 파일 바이트)은 스토리지에, 주소록(key와 상태)은 DB에. 실체가 아니라 역할의 차이.')
b+=P('새 도구가 나왔을 때 "이게 DB인가 스토리지인가"보다','**"무엇을 받고, 어떻게 찾고, 내용을 이해하는가"**','세 가지를 물으면 자리가 정해집니다.')
b+=HR()
b+=H2('참고자료')
b+=P('[[MongoDB 공식 문서 - Documents|https://www.mongodb.com/docs/manual/core/document/]]','[[MongoDB 공식 문서 - Databases and Collections|https://www.mongodb.com/docs/manual/core/databases-and-collections/]]','[[MongoDB 공식 문서 - GridFS|https://www.mongodb.com/docs/manual/core/gridfs/]]','[[Amazon S3 공식 문서 - What is Amazon S3?|https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html]]','(모두 2026-10-18 확인)')
b+=P('#MongoDB #객체스토리지 #S3 #MinIO #BSON #문서형DB #NoSQL #LangGraph #AI활용')
PAGE(T,b,'/home/claude/out3/thu/2026-10-22_목_MongoDB_vs_객체스토리지_이미지주소포함.html')
