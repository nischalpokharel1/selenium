import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\selenium drivers\chromedriver_win32\chromedriver")
driver.get("file:///C:/Users/pokha/OneDrive/Desktop/selinieum/table_sample.html")

# row=print(len(driver.find_element_by_xpath('/html/body/table/tbody/tr'))) #find no of rows
# column =print(len(driver.find_element(By.XPATH,'/html/body/table/tbody/tr[1]/th'))) #find no of columns

# print(row,column)

table=driver.find_element_by_xpath("/html/body/table")
for tr in table.find_elements_by_tag_name("tr"):
    print(tr.text.split(),"22222222222")

for td in table.find_elements_by_tag_name("td"):
    print(td.text,"3333333333")

for th in table.find_elements_by_tag_name("th"):
    print(th.text,"4444444444")

time.sleep(2)
driver.close()