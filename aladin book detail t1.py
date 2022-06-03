#안쓰는 함수 빼놓자

from selenium import webdriver #셀레리움 크롤러
from webdriver_manager.chrome import ChromeDriverManager #크롬브라우저 연결
import urllib
from bs4 import BeautifulSoup #뷰티플스프 크롤러
import requests
import csv #결과물 파일출력
import urllib.request
import pyperclip #싸이트 방어 피하기
import time #시간제어
from selenium.webdriver.common.keys import Keys #버튼 컨트롤
from selenium.webdriver.common.by import By

url = "https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=289083771"
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get(url)
head = {'User-Agent' : "Magic Browser"}
request = urllib.request.Request(url, headers = head) 
response = urllib.request.urlopen(request)     
bsObject = BeautifulSoup(driver.page_source, 'html.parser')
title = bsObject.find("a", {"class":"Ere_bo_title"}).getText()
mans = bsObject.find("li", {"class":"Ere_sub2_title"}).getText()
basic = bsObject.find("div", {"class":"conts_info_list1"}).getText()
bunru = bsObject.find("ul", {"id":"ulCategory"}).getText()
print(title, mans, basic, bunru)

print([e.text for e in driver.find_elements(By.XPATH, '//*[@id="Ere_prod_allwrap"]/div[9]/div[6]')])