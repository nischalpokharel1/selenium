import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\selenium drivers\chromedriver_win32\chromedriver")

driver.get("https://stackoverflow.com/")
print(driver.title)

driver.find_element_by_xpath('/html/body/header/div/ol[2]/li[2]/a[1]').click()

email = driver.find_element_by_name('email')
pwd = driver.find_element_by_name('password')

email = email.send_keys("pokharelnischal567@gmail.com")
pwd = pwd.send_keys("hello")

driver.find_element_by_xpath('/html/body/div[4]/div/button[1]').click()

driver.find_element_by_name('submit-button').click()
print(email.is_enabled())

time.sleep(5)
driver.close()