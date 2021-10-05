# 모듈 import
import requests
import pandas as pd
import json


# 변수 할당
# https://imnews.imbc.com/more/search/?search_kwd=단독#page=0
kwd = '단독'
page = 0
page_size = 1000
base_url = f'https://searchapi.imnews.imbc.com/search?callback=search_202110052313&query={kwd}&page={page}&pagesize={page_size}&sorttype=date'\
     + '&startdate=20201005&enddate=20211005'\
          + '&news_type=NE'


# json 파일 파싱
# search_202110052340({ ... }) 형태로 나오므로 slicing
res = requests.get(base_url)
result = res.text[20:-1]
data = json.loads(result)
articles = data['result']['rows']

# 결과 들어갈 빈 리스트 생성
result_title = []
result_descs = []
result_dates = []
result_links = []


for article in articles:
    if '[단독]' in article['fields']['artsubject']\
         or '[단독]' in article['fields']['adf_bcont']\
             or '단독 인터뷰' in article['fields']['adf_bcont']:
        # print(article['fields']['artsubject'])

        link = 'https://imnews.imbc.com' + article['fields']['linkurl']
        result_title.append(article['fields']['artsubject'])
        result_descs.append(article['fields']['adf_bcont'])
        result_dates.append(article['fields']['operday'][:-6])
        result_links.append(link)

    
# dataframe화
news_list = pd.DataFrame({
    'date': result_dates,
    'title': result_title,
    'links': result_links,
    'description': result_descs
})

# csv로 저장
news_list.to_csv('./data/mbc단독뉴스.csv', encoding='utf-8-sig')