import requests
from bs4 import BeautifulSoup

url = 'https://www.starbucks.co.kr/store/store_map.do'
res = requests.get(url).text
soup = BeautifulSoup(res,'html.parser')
result = soup.select('.quickResultLstCon')
print(result)
