import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import json

base_url = 'https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EB%8B%A8%EB%8F%85&sort=1&photo=0&field=0&pd=5&ds=2021.05.10&de=2022.05.10&mynews=1&office_type=1&office_section_code=1&news_office_checked=1019&nso=so:dd,p:1y,a:all&start='
page = 1
articles = 'start'

dates = []
titles = []
links = []
while articles:
    print(f'현재 페이지: {page}')
    # url 주소 생성
    url = base_url + str(page)
    
    # 기사 데이터 선택
    res = requests.get(url)
    result = res.text
    data = bs(res.text, 'html.parser')
    articles = data.select('div.news_area')
    
    # 현재 페이지 기사 표시
    for article in articles:
        article_date = article.select('span.info')[0].text
        article_title = article.select('a.news_tit')[0].text
        article_link = article.select('a.news_tit')[0]['href']
        
        if '[단독]' in article_title:            
            print(article_date, article_title)
            
            dates.append(article_date)
            titles.append(article_title)
            links.append(article_link)
    
    # 페이지 갱신
    page += 10

df = pd.DataFrame({
    'date': dates,
    'title': titles,
    'href': links,
})

no_dup_df = df.drop_duplicates(subset=['title'])
no_dup_df.reset_index(drop=True, inplace=True)
no_dup_df.to_csv('./data/mbn단독뉴스.csv', encoding='utf-8-sig')
