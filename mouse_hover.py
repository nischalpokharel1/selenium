import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\selenium drivers\chromedriver_win32\chromedriver")
driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element(By.ID,'txtUsername').send_keys("admin")
driver.find_element(By.ID,'txtPassword').send_keys("admin123")

driver.find_element(By.ID,'btnLogin').click()

admin = driver.find_element(By.XPATH,'//*[@id="menu_admin_viewAdminModule"]/b')
user_management = driver.find_element(By.XPATH,'//*[@id="menu_admin_UserManagement"]')
user = driver.find_element(By.XPATH,'//*[@id="menu_admin_viewSystemUsers"]')

action = ActionChains(driver)
action.move_to_element(admin).move_to_element(user_management).move_to_element(user).click().perform()

time.sleep(3)
driver.close()