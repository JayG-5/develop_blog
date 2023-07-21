# django Blog

#### django와 템플릿을 이용하여 요구 기능이 구현된 블로그 제작

---

### 📅프로젝트 기간

#### 2023. 07. 17 ~ 2023. 07. 20

#### Python, django, SQLite3, HTML5, CSS

# 📜요구사항

구현 : ✔

미구현 : ❌

주절주절... : 💬

- 메인페이지 ✔
  - 페이지 제목 ✔
  - 입장하기 버튼 ✔
- 유저 ✔
  - 회원가입 ✔
  - 로그인 ✔
  - 프로필 ✔
    - 닉네임 ✔
    - 수정 ✔
- 게시글
  - 목록 ✔
  - 작성 ✔
    - 권한 : 로그인 ✔
    - 사진업로드 ✔
    - 조회수 ❌
  - 상세 ✔
  - 수정 ✔
    - 권한 : 로그인, 본인 ✔
    - 수정 된 내용을 볼 수 있어야함 ❌
  - 삭제 ✔
    - 권한 : 로그인, 본인 ✔
    - 존재하지 않는 게시글입니다 페이지 ✔
  - 검색 ✔
    - 주제나 태그에 따라 ✔
    - 시간순 정렬 ✔
- 댓글 💬
  - 권한 : 로그인 ✔
  - 대댓글 ✔
    - 권한 : 로그인 ✔
- 정적파일(collectstatic) ✔
- 번역 ❌
- AWS Lightsail 배포 ❌

## 💬주 절 주 절 ...

댓글을 굳이 만들어야하나... 라는 생각을 하다가 '**thread**'앱을 떠올리게됬다.

댓글 -> 답글로 개념만 바꾸면 된다.

댓글모델을 따로 만들 필요없이 Post가 다른 Post를 부모Post로 참조하면 간단하게 구현할 수 있다

그래서..

## 💃모델

![db.jpg](./readme/db.jpg)

## 🛠부가적인 기능들

뭘 적어야 좋을지 몰라 기능소개를 해야겠다는 생각이 든다.

### 🤖MD Parser & 이미지 업로더

글 작성할때 Toast Editor를 사용했는데, 에디터 자체가 이미지업로드를 지원한다.

막아버릴수도 없고, 주렁주렁 base64 텍스트가 스크롤을 농락하는걸 두고볼수도 없다.

글 작성/수정이 완료됬을때, 글의 내용을 정규표현식으로 base64이미지를 파싱해서 이미지 업로더에 던지면 ~~인코딩 디코딩 뭐어쩌구저쩌구 해서~~ 업로드 후 imgurl로 return 해준다.

### 🎲랜덤 닉네임

챗선생께 부사100개 동사100개 동물이름100개(~~동물이름에 뭐 이것저것 섞어놨던데~~)를 달라고했다

### 🚧권한확인 데코레이터

상단 요구사항에 보면 로그인, 본인 등과 같은 권한에 관련된 내용이 존재하는데, 어떻게 구현을 할까 고민하다... 앞서 배웠던 **데코레이터**가 생각이 났다.

어떻게 만들지 고민하다 데코레이터에 파라미터를 넣어서 쓰도록 제작했다

```python
    @user_has_permission(['login','own','not_me'])
```

이상하긴 한데 어쨌든

- **login** : 로그인유저
- **own** : 글 주인
- **not_me** : 내가 아님
  - 팔로우 때문에 만들었다.

## 📡Urls

```

/                                    - index

accouts/reg/'                        - 회원가입
accouts/login/'                      - 로그인
accouts/logout/'                     - 로그아웃

blog/write/"                         - 게시글 작성
blog/detail/<int:pk>/",              - 게시글 상세
blog/detail/<int:pk>/like/"          - 게시글 좋아요
blog/detail/<int:pk>/hashtag/"       - 게시글 해시태그 설정
blog/update/<int:pk>/"               - 게시글 수정
blog/delete/<int:pk>/"               - 게시글 삭제
blog/@<str:nickname>/"               - 유저
blog/@<str:nickname>/edit/"          - 프로필 수정
blog/@<str:nickname>/follow/"        - 유저 팔로우
```

## 💻메인

### 메인페이지

![](./readme/0_메인.png)

### 입장하기

![](./readme/1_블로그.png)

### 로그인

![](./readme/2_로그인.png)

### 최초 로그인 상태

![](./readme/3_최초로그인.png)

### 프로필 제출

![](./readme/4_프로필작성후.png)

### 글쓰기

![](./readme/6_글쓰기.png)

### 글쓰기 완료

![](./readme/7_작성직후.png)

### 해시태그

![](./readme/8_해시태그.png)
좋아요도 눌러주고

### 해시태그 삭제

![](./readme/8-1_해시태그삭제.png)

### 수정으로 가면

![](./readme/9_수정으로가면.png)

### 답글 작성

![](./readme/10_답글.png)

### 답글

![](./readme/11_답글.png)

### 블로그 메인

![](./readme/12_작성후.png)

### 일반 검색

![](./readme/13_검색.png)

### #을 붙이면 해시태그 검색

![](./readme/14_해시검색.png)

### 댓글 검색

![](./readme/15_댓글검색.png)

### 유저명

![](./readme/16_유저검색.png)

### @를 붙여서 유저 풀네임 검색

![](./readme/17_유저검색.png)

### 프로필로 감

![](./readme/18_유저검색직후.png)

# 📝회고

- 아는건 별로 없는데, 원하는 기능은 많다보니 놓친게 많이 보여 아쉬움
- 소셜로그인을 넣을 생각으로 구현을 했었는데, 비용이나 기술문제로 뒤늦게 일반 로그인으로 변경
- Toast editor에서 이미지를 처리할때, hooks속성을 이용하면 파싱을 안하고 처리 할 수 있다고 하는데. 너무 뒤늦게 알아버렸다. ~~공부를 안했다는거지...~~
