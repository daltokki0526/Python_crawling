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

print("▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣")
print("달토끼 알라딘 도서페이지 크롤러 V1.0")
start_page = int(input("●●PageNumber=1 페이지번호 시작 넣어주세요 (ex:1)>"))
end_page = int(input("●●PageNumber=99 페이지번호 끝 넣어주세요 (ex:999)>"))

##########로그인 시퀸스 시작
url_login = "https://www.aladin.co.kr/login/wlogin.aspx?returnurl=%2faccount%2fwmaininfo.aspx%3fpType%3dMyAccount%26start%3dwe"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url_login)
time.sleep(1)
# id, pw 입력
driver.find_element_by_name('Email').send_keys('shilpir@naver.com')
driver.find_element_by_name('Password').send_keys('licrury1004!!')
time.sleep(1)
# 로그인 버튼을 클릭합니다
driver.find_element_by_xpath('//*[@id="LoginForm"]/div[2]/a/div').click()
#바로 하면 페이지 이동이 안될 수 있다.
time.sleep(1)
##########로그인 시퀸스 끝

f = open('aladincrowling.csv','w',encoding='utf-8-sig',newline='')
csvWriter = csv.writer(f)

while start_page < end_page + 1:
    ## 만화 발간일 순서대로 나오는 페이지
    url = "https://www.aladin.co.kr/shop/wbrowse.aspx?BrowseTarget=List&ViewRowsCount=25&ViewType=Detail&PublishMonth=0&SortOrder=5&page={}&Stockstatus=1&PublishDay=84&CID=2551&SearchOption=&CustReviewRankStart=&CustReviewRankEnd=&CustReviewCountStart=&CustReviewCountEnd=&PriceFilterMin=&PriceFilterMax=#".format(start_page)

    start_page = start_page + 1

    driver.implicitly_wait(30)
    driver.get(url)
    head = {'User-Agent' : "Magic Browser"}
    request = urllib.request.Request(url, headers = head) 
    response = urllib.request.urlopen(request)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    book_page_urls = []
        
    for link in soup.find_all("a", {"class":"bo3"}):
        path = link.get('href')
        book_page_urls.append(path)

    for index, book_page_url in enumerate(book_page_urls):
        driver.get(book_page_url)
        bsObject = BeautifulSoup(driver.page_source, 'html.parser')

        title = bsObject.find("a", {"class":"Ere_bo_title"}).getText()
        mans = bsObject.find("li", {"class":"Ere_sub2_title"}).getText()
        basic = bsObject.find("div", {"class":"conts_info_list1"}).getText()
        bunru = bsObject.find("ul", {"id":"ulCategory"}).getText()
        try:
            mookcha = bsObject.find("div", {"id":"div_TOC_Short"}).getText()
        except:
            mookcha = "목차없음"
        csvWriter.writerow([start_page-1, index+1, title, mans, basic, bunru, mookcha])   

    if start_page == end_page + 1:
        print("▣▣▣▣▣▣크롤완료!!.▣▣▣▣▣▣▣▣▣▣")

f.close()

print("▣▣ 크롤링이 종료되었습니다. 콘솔창을 끄셔도 됩니다 !! ▣▣")


