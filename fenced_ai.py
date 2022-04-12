import xlutils
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\selenium drivers\chromedriver_win32\chromedriver")
driver.get("https://test.fenced.ai/login")

driver.maximize_window()

path = "C://fenced/fenced.xlsx"

rows = xlutils.getRowCount(path,'Sheet1')

for r in range(2,rows+1):
    username = xlutils.readData(path,'Sheet1',r,1)
    password = xlutils.readData(path,'Sheet1',r,2)

    driver.find_element_by_id("email").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    time.sleep(5)

    driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/form/div[2]/div[3]/button").click()
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/div/div/div/ul/li[2]/ul/li[1]/a/span').click()
    driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div[2]/div/div/a/div').click()




    # if driver.title == "fenced.ai":
    #     print("Test Passed")
    #     xlutils.writeData(path,'Sheet1',r,3,'Pass')
    #     driver.find_element_by_xpath('//*[@id="topnav"]/div[1]/div/div[1]/ul[2]/li[4]/a/img').click()
    #     logout = driver.find_element_by_xpath('//*[@id="topnav"]/div[1]/div/div[1]/ul[2]/li[4]/div/a[3]')
    #     action = ActionChains(driver)
    #     action.move_to_element(logout).click().perform()
    #     driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div/div/div/div/a[1]').click() 

    # else:
    #     print("Test Failed")
    #     xlutils.writeData(path,'Sheet1',r,3,'Fail')

    
# time.sleep(3)
# driver.close()
    # driver.find_element_by_link_text('Home').click()