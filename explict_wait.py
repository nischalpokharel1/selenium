import time

from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\selenium drivers\chromedriver_win32\chromedriver")

driver.maximize_window()
driver.get("https://www.expedia.com/")

driver.find_element_by_link_text("Flights").click()

driver.find_element_by_class_name("uitk-field-label").click()
time.sleep(4)
driver.find_element_by_xpath("//*[@id=wizard-flight-tab-roundtrip]/div[2]/div[1]/div/div[2]/div/div/div/div[1]/button").send_keys("Nepal")
time.sleep(4)

driver.find_element_by_link_text("Search").click()