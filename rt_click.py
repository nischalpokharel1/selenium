import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\selenium drivers\chromedriver_win32\chromedriver")
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()

button = driver.find_element_by_xpath('/html/body/div/section/div/div/div/p/span')

action = ActionChains(driver)
action.context_click(button).perform()

time.sleep(5)
driver.close()