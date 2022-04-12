from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\selenium drivers\chromedriver_win32\chromedriver")
driver.get("https://test.fenced.ai/")
driver.maximize_window()

# driver.save_screenshot("C:\fenced\a.png")
driver.get_screenshot_as_file("C:/fenced/b.png") #this is working
time.sleep(3)
driver.close()