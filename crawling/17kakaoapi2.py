import requests
api_key = '05d732ff79fcab76b4c978070267e116'

#경로 위도 추출 !!!!!!!!!
query = input('검색할 주소 입력 : ')# 전북 삼성동 100
url = 'https://dapi.kakao.com/v2/local/search/address.json?query={}'.format(query)
headers={'Authorization':'KakaoAK {}'.format(api_key)}

res = requests.get(url,headers=headers) #url에서 결과값은 json임 
#print(res.text)
#print(type(res.json())) #json형태니깐 dictional형태로 출력된다.   dictional = key : value       || list = [0,0,0,0]
data_json = res.json()

#print(data_json)

data = data_json['documents'] #dictionaly니깐 키워드로 뽑아내고
for item in data:
    a=(item['address']['address_name'])
    b=(item['address']['x'])
    c=(item['address']['y'])


x= b
y= c
radius=20000  #2km
query= input('대형마트를 입력하시오 : ')
category_group_code='MT1'
url2 = 'https://dapi.kakao.com/v2/local/search/keyword.json?x={}&y={}&radius={}&query={}&category_group_code={}'.format(x,y,radius,query,category_group_code)
headers2={'Authorization':'KakaoAK {}'.format(api_key)}

res= requests.get(url2,headers=headers2)
data_json = res.json()

print(data_json)

print(data_json['documents'][0]['address_name'])

