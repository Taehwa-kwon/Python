import requests
#해당하는 서버에 요청을 하고 값을 받아오는것 (requests)

api = 'https://search.naver.com/search.naver?'
values= {
    'sm':'top_hty',
    'fbm':'0',
    'ie':'utf8',
    'query':'%ED%83%9C%ED%92%8D'
}

r = requests.get(api,params=values)  #장점은 여기부분


print(r)  #요청 완료 ! 메세지 출력됌
print(r.text) # 전체 HTML을 가져온다.
print(r.url) #주소값을 가져오고

print(r.json)