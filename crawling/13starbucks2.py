from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('./crawling/chromedriver.exe')
driver.get('https://www.starbucks.co.kr/store/store_map.do')
driver.implicitly_wait(20)

loca = driver.find_element(By.CLASS_NAME,'loca_search')
loca.click()
driver.implicitly_wait(10)

sido = driver.find_element(By.CLASS_NAME,'sido_arae_box')
li = sido.find_elements_by_tag_name('li')
li[5].click()

sido = driver.find_element(By.CLASS_NAME,'gugun_arae_box')
li = sido.find_elements_by_tag_name('li')
li[4].click()

source = driver.page_source
soup = BeautifulSoup(source,'html.parser')
storelist = soup.find('ul',class_ ='quickSearchResultBox')
storelist_li = storelist.find_all('li')

for li in storelist_li:
    print(li.find('strong').text)
    print(li.find('p').text)

driver.close()