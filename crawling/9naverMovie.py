import urllib.request
import requests
from bs4 import BeautifulSoup

for i in range(1,11):
    url = "https://movie.naver.com/movie/point/af/list.nhn?page=%s"%(i)
    res = requests.get(url).text

    

    soup =BeautifulSoup(res,'html.parser')
    title = soup.select('td.title>a.movie')
    #title = soup.select('td.title>a.movie.color_b')
    content = soup.select('td.title')
    id = soup.select('td.num .author')
    date = soup.select('tr td.num ')[1] #아직 이거는 못함..
    

    
    for i,t in enumerate(title):
        #print(i,'title : ',t.text)
        pass


    for i,c in enumerate(content):
        #print(c)
        #print(i,'content : ', c.text.strip().split('\n')[4])
        pass
        

    for i,c in enumerate(id):
        #print(i,'작성자 : ', c.text)
        pass
        

    for i,c in enumerate(date):
        print(i , " 공백 " , date.text.split('****')[1])
        #print(c.split('\n')[1])
        #print(i,'날짜 : ', c.text.split('\n'))
        
   
        
    