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

# 입력 텍스트 받기
print("▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣")
print("달토끼 YES24 도서페이지 크롤러 V1.0")
print("▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣")
print("●●시작하기전에 이미지가 저장을 위해 크롤러 실행파일과 같은곳에 img 폴더 생성해주세요 !!")
print("●●yes24의 성인인증은 크롤하기 전에 먼저 완료해주세요")
print("▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣")
print("●●크롤링 진행시 크롬웹브라우저가 자동 동작하니 건들지 말아주세요 !!")
print("●●아이디와 암호는 그리고 카테고리번호 페이지 번호는 정확하게 넣어주셔야합니다. !!")
print("●●카테고리 번호는 예를들어 메뉴에서 국내도서>만화/라이트노벨>!!액션!! 즉 액션 단계에 주소창에서 가장 마지막의 숫자입니다.")
print("●●페이지수는 예를들어 액션을 선택했을때 나오는 페이지 1,2,3,4.. 의 번호입니다. 1페이지만 뽑고싶으시면 시작과 끝 페이지가 모두 1 입니다.")
print("●●페이지 끝번호 까지 입력하고 엔터 치시면 크롤링이 시작됩니다. 차분히 기다려주세요.")
print("●●텍스트 데이터는 yes24crowling.csv 파일에 이미지는 img 폴더에 들어갑니다.")
print("●●다음 오류는 크롤관 무관합니다 시스템에 부착된 장치가 작동하지 않습니다. 결과물에 지장없는 에러입니다.")
print("▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣▣")
idgogo = input("●●예스24 아이디 적어주세요>")
pwgogo = input("●●예스24 암호 적어주세요>")
taget = input("●●Category/Display/001001008009 예스24의 카테고리 번호를 넣어주세요 (ex:001001008009)>")
start_page = int(input("●●PageNumber=1 페이지번호 시작 넣어주세요 (ex:1)>"))
end_page = int(input("●●PageNumber=99 페이지번호 끝 넣어주세요 (ex:99)>"))

##########로그인 시퀸스 시작

url_login = "https://www.yes24.com/Templates/FTLogin.aspx"

driver = webdriver.Chrome(ChromeDriverManager().install())  #크롬브라우져 켜기
driver.get(url_login)
time.sleep(1)

# id, pw 입력할 곳을 찾기
tag_id = driver.find_element_by_name('SMemberID')
tag_pw = driver.find_element_by_name('SMemberPassword')
tag_id.clear()
tag_pw.clear()
time.sleep(1)

# id 입력
tag_id.click()
pyperclip.copy(idgogo)
tag_id.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

# pw 입력
tag_pw.click()
pyperclip.copy(pwgogo)
tag_pw.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

# 로그인 버튼을 클릭합니다
login_btn = driver.find_element_by_id('btnLogin')
login_btn.click()

#바로 하면 페이지 이동이 안될 수 있다.
time.sleep(1)

##########로그인 시퀸스 끝

f = open('yes24crowling.csv','w',encoding='utf-8-sig',newline='')
csvWriter = csv.writer(f)

while start_page < end_page + 1:

    url = "http://www.yes24.com/24/Category/Display/{}?PageNumber={}".format(taget, start_page)

    start_page = start_page + 1

    #driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(30)
    driver.get(url)

    head = {'User-Agent' : "Magic Browser"}

    request = urllib.request.Request(url, headers = head) 

    response = urllib.request.urlopen(request)

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    book_page_urls = []
    
    for link in soup.find_all("a", {"class":"bgYUI ico_nWin"}):
        path = "http://www.yes24.com"+link.get('href')
        book_page_urls.append(path)

    for index, book_page_url in enumerate(book_page_urls):
        driver.get(book_page_url)
        bsObject = BeautifulSoup(driver.page_source, 'html.parser')

        title = bsObject.find("h2", {"class":"gd_name"}).getText()
        try: # 원서 내용 없는 책 때문에 에러처리
            orgin_title = bsObject.find("span", {"class":"gd_orgin"}).getText()
        except:
            orgin_title = "원서 없음"
        price = bsObject.find("em", {"class":"yes_m"}).getText()
        prices = bsObject.find("span", {"class":"nor_price"}).getText()
        author = bsObject.find("span", {"class":"gd_auth"}).getText()
        pub = bsObject.find("span", {"class":"gd_pub"}).getText()
        bsize = bsObject.find("tbody", {"class":"b_size"}).getText()
        yesalertli = bsObject.find("dl", {"class":"yesAlertDl"})
        yesalertli2 = yesalertli.find("ul", {"class":"yesAlertLi"}).getText()
        try: #줄거리 업는책 때문에 에러처리
            infotext = bsObject.find("div", {"class":"infoWrap_txtInner"})
            infotext2 = infotext.find("textarea", {"class":"txtContentText"}).getText()
        except:
            infotext2 = "줄거리 없음"
        imgurl = bsObject.find("em", {"class":"imgBdr"})
        imgurl2 = imgurl.find("img")
        imgurl3 = imgurl2.get("src")
        
        # 책 상세정보 bsize 에서 isbn 추출
        isbn13a=bsize.find("ISBN13")+1
        isbn13b=bsize[isbn13a+6:isbn13a+19]
        
        csvWriter.writerow([start_page-1, index+1, title.strip(), isbn13b, orgin_title.strip(), price.strip(), prices.strip(), 
        author.strip(), pub.strip(), bsize.strip().replace("\n","▣"), infotext2.strip(), yesalertli2.strip().replace("\n","▣"), imgurl3])   

        urllib.request.urlretrieve(imgurl3, "./img/"+ isbn13b + ".jpg")
    
    if start_page == end_page + 1:
        print("▣▣▣▣▣▣크롤완료!!.▣▣▣▣▣▣▣▣▣▣")

f.close() # csv 파일생성 끝내기

driver.close() # 크롬브라우져 창 닫기

print("▣▣ 크롤링이 종료되었습니다. 콘솔창을 끄셔도 됩니다 !!! ▣▣")





