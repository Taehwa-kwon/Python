id='i_kebi'
pw='!sora146969'

from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('./crawling/chromedriver.exe')
driver.get('https://nid.naver.com/nidlogin.login')
driver.implicitly_wait(5)

#driver.find_element_by_name('id').send_keys(id)
#driver.find_element_by_name('pw').send_keys(pw)

driver.execute_script("document.getElementsByName('id')[0].value=\'"+id+"\'")
driver.execute_script("document.getElementsByName('pw')[0].value=\'"+pw+"\'")
driver.implicitly_wait(3)

driver.find_element_by_class_name('btn_global').click()
driver.implicitly_wait(3)
driver.find_element_by_xpath('//*[@id="new.dontsave"]').click()

driver.get('https://order.pay.naver.com/home')
source = driver.page_source
soup = BeautifulSoup(source,'html.parser')
point = soup.select_one('dl.my_npoint strong')
print('포인트는 ',point.text)