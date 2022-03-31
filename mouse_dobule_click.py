import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\selenium drivers\chromedriver_win32\chromedriver")
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

button = driver.find_element_by_xpath('//*[@id="HTML10"]/div[1]/button')

action = ActionChains(driver)
action.double_click(button).perform()

time.sleep(5)
driver.close()