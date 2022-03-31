import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\selenium drivers\chromedriver_win32\chromedriver")
driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element_by_xpath('//*[@id="HTML9"]/div[1]/button').click()
time.sleep(3)
driver.switch_to.alert.accept()

time.sleep(5)
driver.close()