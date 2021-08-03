# 모듈 import
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

# 변수 할당
sbs_url = 'https://news.sbs.co.kr'
base_url = 'https://news.sbs.co.kr/news/newsPlusList.do?'
pages = 'pageIdx='
theme = '&themeId=10000000034'

# 결과 들어갈 빈 리스트 생성
result_title = []
result_descs = []
result_dates = []
result_links = []

# page50까지 반복
for page_num in range(1,51):
    print(f'now on page {page_num}...')
    url = base_url + pages + str(page_num) + theme

    res = requests.get(url)
    data = bs(res.text, 'html.parser')

    title = data.select('a.news > p.desc > strong.sub')
    descs = data.select('a.news > p.desc > span.read')
    dates = data.select('a.news > p.desc > span.date')
    links = data.find_all('a', class_='news')

    for i in range(len(title)):
        result_title.append(title[i].text)
        result_descs.append(descs[i].text)
        result_dates.append(dates[i].text[2:-6])

        temp = sbs_url + str(links[i]['href'])
        result_links.append(f'=HYPERLINK("{temp}","링크")')

# dataframe화
news_list = pd.DataFrame({
    'date': result_dates,
    'title': result_title,
    'links': result_links,
    'description': result_descs
})

# csv로 저장
news_list.to_csv('./data/sbs단독뉴스.csv', encoding='utf-8-sig')