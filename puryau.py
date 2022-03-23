import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\selenium drivers\chromedriver_win32\chromedriver")

driver.get("https://puryau.com/")

driver.find_element_by_link_text("Place Order").click()


email = driver.find_element_by_id("email")
password = driver.find_element_by_id("password")

email = email.send_keys("rajanlama79@gmail.com")
password = password.send_keys("123456")

# driver.find_element_by_link_text("Log In").click()
driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div/div[2]/form/div[3]/div/button").click()

pickup = driver.find_element_by_id("origin-input")

pickup = pickup.send_keys("K")

list = driver.find_element_by_xpath("/html/body/div[5]")

# drop = driver.find_element_by_id("destination-input")
#
# drop = drop.send_keys("lalitpur")
#
# reciver_name = driver.find_element_by_id("destination-name")
# reciver_phone = driver.find_element_by_id("destination-phone")
#
# reciver_name = reciver_name.send_keys("Nischal Pokarel")
# reciver_phone = reciver_phone.send_keys("9860815351")
#
# time.sleep(10)
# driver.close()

