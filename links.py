import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\selenium drivers\chromedriver_win32\chromedriver")
driver.get("https://demo.guru99.com/test/newtours/")

links = driver.find_elements(By.TAG_NAME,'a')
print("\n\n\n\n",len(links))
for link in links:
    print(link.text)

# click on specific link
driver.find_element(By.LINK_TEXT,'REGISTER').click()


time.sleep(5)
driver.close()