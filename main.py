import os
from selenium import webdriver
os.environ['PATH'] += r"C:\New folder"
driver = webdriver.Chrome() 
driver.get("https://stackoverflow.com/questions/61664955/where-to-find-button-id-in-html-inspect")
my_element = driver.find_element_by_link_text('Log in')
my_element.click()
my_element1 = driver.find_element_by_link_text('Accept all cookies')
my_element1.click()