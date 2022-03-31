import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\selenium drivers\chromedriver_win32\chromedriver")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
#how to find how many input boxes in web page

input_boxes = driver.find_elements(By.CLASS_NAME,'text_field')
print(len(input_boxes))


status = driver.find_element(By.ID,'RESULT_TextField-1').is_displayed()
print("True or False",status)

status = driver.find_element(By.ID,'RESULT_TextField-1').is_enabled()
print("True or False",status)


#how to provide value into textbox
driver.find_element(By.ID,'RESULT_TextField-1').send_keys('Nischal')
driver.find_element(By.ID,'RESULT_TextField-2').send_keys('Pokharel')
driver.find_element(By.ID,'RESULT_TextField-3').send_keys('9860815351')

#radio buttons and checkboxes

# a = driver.find_element(By.ID,'RESULT_RadioButton-7_0').is_selected()
# print(a)
# driver.find_element(By.ID,"RESULT_CheckBox-8_0").click()
# driver.find_element(By.ID,"RESULT_RadioButton-7_0").click()
# a = driver.find_element(By.ID,'RESULT_RadioButton-7_1').is_selected()
# print(a)

driver.find_element(By.ID,'RESULT_CheckBox-8_0').click() #sunday , here the box should be selected according to tutorial i follwo which is not happening in my case

time.sleep(5)
driver.close()



