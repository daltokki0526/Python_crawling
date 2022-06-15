from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager #크롬브라우저 연결

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('http://www.kyobobook.co.kr/product/detailViewKor.laf?mallGb=KOR&ejkGb=KOR&linkClass=4717&barcode=9791168940420')
driver.implicitly_wait(time_to_wait=1)
mookcha = driver.find_element(By.XPATH, ('//*[@id="container"]/div[5]/div[1]/div[3]/div[5]')).text #목차
isbn = driver.find_element(By.XPATH, ('//*[@id="container"]/div[5]/div[1]/div[3]/table/tbody/tr[1]/td/span[1]')).text #isbn
page = driver.find_element(By.XPATH, ('//*[@id="container"]/div[5]/div[1]/div[3]/table/tbody/tr[2]/td')).text #page
size = driver.find_element(By.XPATH, ('//*[@id="container"]/div[5]/div[1]/div[3]/table/tbody/tr[3]/td')).text #size
onesu = driver.find_element(By.XPATH, ('//*[@id="container"]/div[5]/div[1]/div[3]/table/tbody/tr[4]/td/a')).text #원서
bunya = driver.find_element(By.XPATH, ('//*[@id="container"]/div[5]/div[1]/div[3]/ul/li')).text #장르
basicinfo = driver.find_element(By.XPATH, ('//*[@id="container"]/div[2]/form/div[1]/div[2]')).text #기본정보
cash = driver.find_element(By.XPATH, ('//*[@id="container"]/div[2]/form/div[3]/div[1]/ul/li[1]/span[2]/strong')).text #가격
story = driver.find_element(By.XPATH, ('//*[@id="container"]/div[5]/div[1]/div[3]/div[3]')).text #줄거리

driver.quit()

print(isbn, page, size, onesu, mookcha, bunya, basicinfo, cash, story)
