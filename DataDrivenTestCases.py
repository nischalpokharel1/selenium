import xlutils
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\selenium drivers\chromedriver_win32\chromedriver")
# driver.get('https://demo.guru99.com/test/newtours/')
driver.get("https://puryau.com/UserSignin/")

driver.maximize_window()

path = "C://New1/login1.xlsx"

rows = xlutils.getRowCount(path,'Sheet1')

for r in range(2,rows+1):
    username = xlutils.readData(path,'Sheet1',r,1)
    password = xlutils.readData(path,'Sheet1',r,2)

    # driver.find_element(By.NAME,'userName').send_keys(username)
    # driver.find_element(By.NAME,'password').send_keys(password)
    driver.find_element_by_id("email").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)

    # driver.find_element(By.NAME,'submit').click()
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div/div[2]/form/div[3]/div/button").click()



    # if driver.title == "Login: Mercury Tours":
    if driver.title == "Puryau - On Demand Delivery । All Nepal Home Delivery Cargo & Courier":
        print("Test Passed")
        xlutils.writeData(path,'Sheet1',r,3,'Pass')
        driver.find_element_by_xpath('//*[@id="topnav"]/div[1]/div/div[1]/ul[2]/li[4]/a/img').click()
        logout = driver.find_element_by_xpath('//*[@id="topnav"]/div[1]/div/div[1]/ul[2]/li[4]/div/a[3]')
        action = ActionChains(driver)
        action.move_to_element(logout).click().perform()
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div/div/div/div/a[1]').click() 

    else:
        print("Test Failed")
        xlutils.writeData(path,'Sheet1',r,3,'Fail')

    
time.sleep(3)
driver.close()
    # driver.find_element_by_link_text('Home').click()