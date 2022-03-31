import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\selenium drivers\chromedriver_win32\chromedriver")
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html  ")
driver.maximize_window()

sourcelement = driver.find_element(By.ID,'box7')
targetelement = driver.find_element(By.ID,'box107')


action = ActionChains(driver)
action.drag_and_drop(sourcelement,targetelement).perform()

time.sleep(5)
driver.close()