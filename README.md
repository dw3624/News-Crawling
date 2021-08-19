# News-Crawling
- 뉴스 포털사이트에서 기사 내용을 크롤링합니다.

  

## 한국일보 기사 크롤링

- 날짜, 제목, 링크, 내용, 단어
- [한국일보](https://www.hankookilbo.com/Search?searchText=)
- 기사 크롤링 후, 해당 기사 내용에서  `konlpy` 이용해 단어 추출

#### 개선점

- 기사 검색시 지정한 날짜와 다른 날짜의 기사가 섞여 있는 경우 있음

- 불용어로 인해 단어 추출해도 기사 내용 추측 불가

  

  

## SBS 단독 뉴스 기사 크롤링

- 날짜, 제목, 링크, 내용
- [SBS 단독보도](https://news.sbs.co.kr/news/newsPlusList.do?themeId=10000000034&plink=TOPWORD&cooper=SBSNEWSEND)
- 크롤링 후 csv로 변환
  - 변환시 링크는 엑셀 함수인 `=HYPERLINK('<링크>', '바로가기')` 형태로 저장

#### 개선점

- 가독성을 높이려면 어떤 식으로 결과물을 처리해야할지 고민 필요
