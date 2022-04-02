from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\selenium drivers\chromedriver_win32\chromedriver")
driver.get("https://www.facebook.com/")
driver.maximize_window()

# capture all cookies created by browser
cookies = driver.get_cookies()
print(len(cookies))
print(cookies,"\n\n\n")

#add new cookie in browser
cookie = {'name': 'Nischal', 'value': 'Pokharel'}
driver.add_cookie(cookie)
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

# delete cookie
driver.delete_cookie('Nischal') #we can delete all cookies by delete_all_cookies() method
cookies = driver.get_cookies()
print(len(cookies))

time.sleep(3)
driver.close()