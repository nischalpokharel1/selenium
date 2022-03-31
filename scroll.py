import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\selenium drivers\chromedriver_win32\chromedriver")
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window() #maximize the window

# scroll down by pixel
# driver.execute_script("window.scrollBy(0,1000);") #scroll down

# scroll till item is found 
# it is not working
# flag = driver.find_element(By.XPATH,'//*[@id="content"]/div[2]/div[2]/table[2]/tbody/tr[23]/td[1]/img')
# driver.execute_script("argument[0].scrollIntoView();",flag)

# scroll till end of page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")

time.sleep(2)
driver.close()


