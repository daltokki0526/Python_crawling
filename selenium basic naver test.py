from selenium import webdriver #셀레리움 크롤러
from webdriver_manager.chrome import ChromeDriverManager #크롬브라우저 연결
from selenium.webdriver.common.keys import Keys #버튼 컨트롤
from selenium.webdriver.common.by import By

url = "http://www.naver.com"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)

driver.find_element(By.ID, 'query').send_keys("이현세", Keys.ENTER)

variable = driver.current_url #새주소로 갱신
driver.get(variable)


print([e.text for e in driver.find_elements(By.XPATH, '//*[@id="main_pack"]/section[1]/div[1]/div[1]/div')])
print([e.text for e in driver.find_elements(By.XPATH, '//*[@id="main_pack"]/section[1]/div[2]/div[1]/div/div[2]/dl/div[1]/dd')])
print([e.text for e in driver.find_elements(By.XPATH, '//*[@id="main_pack"]/section[1]/div[2]/div[1]/div/div[2]/dl/div[3]/dt')])


