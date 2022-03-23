from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\selenium drivers\chromedriver_win32\chromedriver")

driver.get("https://support.google.com/mail/answer/56256?hl=en")
print(driver.title)

driver.get("https://about.facebook.com/")
print(driver.title)

driver.back()
print(driver.title)

driver.forward()
print(driver.title)

time.sleep(5)

driver.close()
