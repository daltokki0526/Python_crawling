from selenium import webdriver
from selenium.webdriver.support.ui import Select

# driver = webdriver.Chrome('WebDriver.exe 파일 있는 경로 입력')
from webdriver_manager.chrome import ChromeDriverManager #크롬브라우저 연결

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=295873981')
driver.implicitly_wait(time_to_wait=1)
title = driver.find_element_by_class_name('Ere_bo_title').text
title2 = driver.find_element_by_class_name('Ere_sub2_title').text
won = driver.find_element_by_class_name('Ritem').text
element = driver.find_element_by_class_name('Ere_prod_mconts_R').text
driver.quit()100
print(title,"\n",title2,"\n",element,"\n",won,"\n")

