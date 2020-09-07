import urllib.request  #urllib모듈은 URL을 다루는 라이브러리이다.
import urllib.parse
#해당하는 서버에 요청을 하고 값을 받아오는것 (urllib)


#url="https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=%ED%83%9C%ED%92%8D"
api = 'https://search.naver.com/search.naver?'

values= {
    'sm':'top_hty',
    'fbm':'0',
    'ie':'utf8',
    'query':'%ED%83%9C%ED%92%8D'

}

params = urllib.parse.urlencode(values)  #urllib는 parse도 해야하고 POST방식인 경우 다르게 해야한다.그래서 request방식이 더 선호됨
print(params)

url = api + params
data = urllib.request.urlopen(url).read()
print(data.decode('utf-8'))