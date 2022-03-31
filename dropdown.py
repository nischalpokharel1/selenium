import time
from zoneinfo import available_timezones
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="C:\selenium drivers\chromedriver_win32\chromedriver")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

element = driver.find_element(By.ID,'RESULT_RadioButton-9')
dropdown = Select(element)

# dropdown.select_by_visible_text('Morning') #selecting by visible text

# dropdown.select_by_index(3) #selecting by index
dropdown.select_by_value('Radio-1') #selecting by value
# count no of options 
print('available no of options: ',len(dropdown.options))

# capture all the available options
all_values = dropdown.options
for values in all_values:
    print(values.text)

time.sleep(5)
driver.close()