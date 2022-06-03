from selenium import webdriver

driver = webdriver.Chrome("chromedriver")
driver.get("http://www.naver.com")

print("### tag_name")
print([e.text for e in driver.find_elements_by_tag_name('a')[:100] if 'text' in dir(e)])
print("### xpath")
print([e.text for e in driver.find_elements_by_xpath('//*[@id="NM_set_home_btn"]')])
print([e.text for e in driver.find_elements_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div[2]/a[1]')])

print("### id")
print([e.text for e in driver.find_elements_by_id("NM_set_home_btn")])
print("### class_name")
print([e.text for e in driver.find_elements_by_class_name("link_set")])
print("### link_text")
print([e.text for e in driver.find_elements_by_link_text("네이버를 시작페이지로")])
print("### partial_link_text")
print([e.text for e in driver.find_elements_by_partial_link_text("네이버")])
print("### css_selector")
print([e.text for e in driver.find_elements_by_css_selector("#NM_set_home_btn")])

print("### custom attribute")
print([e.text for e in driver.find_elements_by_css_selector("[data-clk='top.mkhome']")])
print([e.text for e in driver.find_elements_by_xpath("//*[@data-clk='top.mkhome']")])