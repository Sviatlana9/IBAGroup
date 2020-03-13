from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("C:/webdrivers/chromedriver.exe")
driver.get("https://www.tut.by/")
print(driver.title)
assert "TUT" in driver.title
elem = driver.find_element_by_name ("q")
elem.clear()
elem.send_keys("TUT")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
time.sleep(15)
driver.close()