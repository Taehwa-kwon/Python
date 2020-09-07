from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome('./crawling/chromedriver.exe')
url ='https://www.starbucks.co.kr/store/store_map.do'
driver.get(url)
time.sleep(20)
source = driver.page_source
soup = BeautifulSoup(source,'html.parser')
result = soup.select('.quickResultLstCon')
print(result)
