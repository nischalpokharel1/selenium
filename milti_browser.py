import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path="C:\selenium drivers\chromedriver_win32\chromedriver")
driver.get("https://gmail.google.com/inbox/")
print(driver.current_url) #print link of the page
driver.find_element_by_xpath("/html/body/header/span/a[1]/span[1]").click()
time.sleep(5)
driver.close()