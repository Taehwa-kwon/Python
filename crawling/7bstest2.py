import requests
import urllib.request 
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/marketindex/exchangeList.nhn'

res = requests.get(url)
print(res)
##print(res.text)  #HTML을 모두 가져온다.

# 0. !! 먼저 url을 오픈해주고 / urllib는 URL을 다루는 라이브러리 , 즉 인터넷주소에 활용하는 라이브러리
res=urllib.request.urlopen(url)
print(requests.get(url))

# 1. BeautifulSoap객체로 만들어준다.
soup = BeautifulSoup(res,'html.parser')


# 2. 이걸 찾는 방법은 해당 URL에서 F12 눌러서 Elements 에서 밑에 경로를 볼 수 있다.
name = soup.select('td.tit')
exchange = soup.select('td.sale')

currency = []
price = []


#===========================================================#
for re in exchange:
    ##print(re.string) 
    print(re.text)
    
    price.append(re.text)

print('================================')
print(  str.strip(name[0].string) + exchange[0].string ) ##미국 , 환율 
print('================================')

#===========================================================#
item = soup.select(".tit") 
item_text = []

for i in item:
    k = i.text.strip()
    item_text.append(k)
##print(item_text) ##모든 나라 가져오기


#===========================================================#
res = requests.get(url).text
result2 = soup.select('td.tit>a') 


for re in result2:
    ##print(re.string.strip()) 
    ##print(re.string.strip().split(" ")) 
    currency.append(re.string.strip())

resultzip = list(zip(currency,price)) ##zip을 통해서 합친다. 근데 zip해놓고 출력이 안되니깐 list로 
##print(currency)    
##print(price)

##print(resultzip)

for c,p in resultzip:
    ##print('통화명 : ' ,c , ' 현재 환율 : ' ,p)
    print("통화명 : {}  |  가격 : {}".format(c,p) )
