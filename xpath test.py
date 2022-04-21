from selenium import webdriver

# driver = webdriver.Chrome('WebDriver.exe 파일 있는 경로 입력')
from webdriver_manager.chrome import ChromeDriverManager #크롬브라우저 연결

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=289083771')
driver.implicitly_wait(time_to_wait=1)
element = driver.find_element_by_xpath('/html/body/div[5]/div[9]/div[6]/div[3]/div[1]/text()[1]').text
driver.quit()
print(element)