# News-Crawling
- 뉴스 포털사이트에서 기사 내용을 크롤링합니다.


## 크롤링 수단 결정법 (우선순위별)
- api 제공여부 확인 후 이용
- url(비공식 api) 찾기
- BeautifulSoup 및 Selenium 이용
  - BeautifulSoup : html로만 화면이 구성된 경우
  - Selenium : 사용자가 보는 화면을 표시

  

## 한국일보 기사 크롤링

- 날짜, 제목, 링크, 내용, 단어
- [한국일보](https://www.hankookilbo.com/Search?searchText=)
- 기사 크롤링 후, 해당 기사 내용에서  `konlpy` 이용해 단어 추출

#### 크롤링 과정
- BeautifulSoup 이용

#### 개선점

- 기사 검색시 지정한 날짜와 다른 날짜의 기사가 섞여 있는 경우 있음

- 불용어로 인해 단어 추출해도 기사 내용 추측 불가

  

  

## SBS 단독 뉴스 기사 크롤링

- 날짜, 제목, 링크, 내용
- [SBS 단독보도](https://news.sbs.co.kr/news/newsPlusList.do?themeId=10000000034&plink=TOPWORD&cooper=SBSNEWSEND)
- 크롤링 후 csv로 변환
  - 변환시 링크는 엑셀 함수인 `=HYPERLINK('<링크>', '바로가기')` 형태로 저장

#### 크롤링 과정
- BeautifulSoup 이용

#### 개선점

- 가독성을 높이려면 어떤 식으로 결과물을 처리해야할지 고민 필요

  

  

## MBC 단독 뉴스 기사 크롤링

- 날짜, 제목, 링크, 내용
- [MBC 단독](https://imnews.imbc.com/more/search/?search_kwd=%EB%8B%A8%EB%8F%85#page=0)
- 크롤링 후 csv로 변환
  - 변환시 링크는 엑셀 함수인 `=HYPERLINK('<링크>', '바로가기')` 형태로 저장

#### 크롤링 과정
- 비공식 url 찾아 json 파싱 후 진행
- 페이지 표시 과정
  - 검색 버튼 입력
  - 빈 페이지 표시
  - javascript로 내용 요청
  - 빈 페이지에 추가 후 표시
- `Chrome` > `F12` > `Network` : HTTP 통신 과정을 표시
  - `search_utl.js`에서 기사 내용이 있는 url 가져오기

#### 개선점

- 가독성을 높이려면 어떤 식으로 결과물을 처리해야할지 고민 필요