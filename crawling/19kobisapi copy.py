import requests,time,datetime

movieDate_str = time.strftime('%Y%m%d' , time.localtime(time.time())) #날짜형태를 문자로(str) 바꾸는 함수    #time.time 은 현재 시간. 
print(movieDate_str)
print(type(movieDate_str))

movieDate_time = datetime.datetime.strptime(movieDate_str,'%Y%m%d').date() #strptime은 다시 time형태로 바꿔준다.    #date가 없으면 시간도 나오니깐 date 를 붙여서 시간을 빼준다.
print(movieDate_time)
print(type(movieDate_time))

movieDate_tmp = movieDate_time - datetime.timedelta(weeks=2) #weeks   오늘날짜 - 하루 


key = '794306f489b73e2728e234bc266fcd21'
targetDt = time.strftime('%Y%m%d' , time.localtime(time.time()))
print(targetDt)

for i in range(0,30):
    movieDate_time = datetime.datetime.strptime(targetDt,'%Y%m%d').date()
    movieDate_tmp = movieDate_time - datetime.timedelta(weeks=2)
    targetDt = movieDate_time.strftime('%Y%m%d')

    url ='http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key={}&targetDt={}'.format(key,targetDt)
    print(url)


    res =requests.get(url).json() #이미 url에서 json 형태니깐 json으로 받고 아니면 import json 하고  json형태로 받으면 바꾸면 된다.
    #print(type(res))
    #print(res)
    result = res['boxOfficeResult']
    result2 = result['dailyBoxOfficeList']

    for item in result2: 
        #print('{}위 '.format(item['rank'])+'{:*<33}'.format(item['movieNm']) + '개봉일 {} '.format(item['openDt']))
        print()





