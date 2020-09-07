import os
import sys
import urllib.request
import json

client_id = "vDF3LlFWh1oyATg95OcS"
client_secret = "W8EuA4XtI6"

for i in range(1,1001,100):
    encText = urllib.parse.quote("파이썬")

    url = "https://openapi.naver.com/v1/search/blog.json?display=100&start="+str(i)+"&query=" + encText 
    #url = "https://openapi.naver.com/v1/search/blog.json?query=" + encText + "&display="'100' # json 결과    naverDevlopers -> serviceAPI-> API호출예제를 복사했지만 API기본정보에서 blog.xlm로 바꿔준다.
    #url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        
        print(type(response_body)) #현재 byte형태임 <class 'bytes'>
        #print(response_body.decode('utf-8')) #결과는 {} 형태인 딕셔너리 형태
        
        data = json.loads(response_body)
        print(data)
        print(type(data))

        items = data['items']

        for item in  items:
            print(item['title'])
            print(item['link'])

        title = item['title']    
        link  = item['link']

        list = {title,link}
        print(list)





    else:
        print("Error Code:" + rescode)

