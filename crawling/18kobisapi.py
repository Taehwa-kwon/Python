import requests

key = '794306f489b73e2728e234bc266fcd21'
#targetDt= input('년월일로 기입해주십시오')
targetDt = '20200905'
url ='http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key={}&targetDt={}'.format(key,targetDt)

res =requests.get(url).json() #이미 url에서 json 형태니깐 json으로 받고 아니면 import json 하고  json형태로 받으면 바꾸면 된다.
print(type(res))
result = res['boxOfficeResult']
result2 = result['dailyBoxOfficeList']

for item in result2:
    #print(item['rank']+" 위 , 영화명 : "+item['movieNm'] +" 개봉일 : " +item['openDt'] +" 매출액 :  "+ item['salesAmt'] )
    print('{}위 '.format(item['rank'])+'{:*<33}'.format(item['movieNm']) + '개봉일 {} '.format(item['openDt']))





