
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
from time import sleep

url = "https://www.google.com/"
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get(url)
head = {'User-Agent' : "Magic Browser"}
request = urllib.request.Request(url, headers = head) 
response = urllib.request.urlopen(request)     
bsObject = BeautifulSoup(driver.page_source, 'html.parser')


search_box = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')

search_box.send_keys('greeksharifa.github.io')
search_box.send_keys(Keys.RETURN)

elements = driver.find_elements_by_xpath('//*[@id="rso"]/div[*]/div/div[1]/a/h3/span')

for element in elements:
    print(element.text)
    print(element.text, file=open('gorio.txt', 'w', encoding='utf-8'))

sleep(3)
driver.close()