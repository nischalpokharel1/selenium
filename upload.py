import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\selenium drivers\chromedriver_win32\chromedriver")
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

driver.switch_to.frame(0)

driver.find_element(By.ID,'RESULT_FileUpload-10').send_keys("C:/New folder (2)/sample.png")
time.sleep(2)
driver.close()
