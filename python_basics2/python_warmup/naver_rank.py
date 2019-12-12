import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.naver.com').text
soup = BeautifulSoup(response, 'html.parser')

tags = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul:nth-child(5) .ah_k')   

with open('tag.txt','w', encoding = 'utf-8') as x:
    x.write('네이버 검색 순위 \n')
    for i, tag in enumerate(tags):
        x.write(f'{i+1},{tag.text} \n')

       