import urllib.request
import requests
from bs4 import BeautifulSoup

url = 'https://news.naver.com/main/home.nhn'

res = urllib.request.urlopen(url)
soup = BeautifulSoup(res,'html.parser')

result = soup.select('ul.section_list_ranking li span.rank em')
result1 = soup.select('ul.section_list_ranking li a ')

print(len(result1)) #총 6개 카테고리 10개씩 

for i in result:
    print('글 순위 : ' , i.text) # 글순위 제목 링크가 한번에 붙어야 하는데...


for i in result1:
    
    #print('제목 : ', i.attrs['title'])
    #print('링크 : ', i.attrs['href'])
    url_content = 'https://news.naver.com'+i.attrs['href']

    content_res = requests.get(url_content).text
    content_soup = BeautifulSoup(content_res,'html.parser')
    content = content_soup.select_one('#articleBodyContents')
    #print(content.text)

