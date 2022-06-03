from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager #크롬브라우저 연결
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = "https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=289083771"
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get(url)
print("### partial_link_text")
print([e.text for e in browser.find_elements_by_partial_link_text("도굴왕")])
