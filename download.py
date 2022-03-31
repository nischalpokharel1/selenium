from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\selenium drivers\chromedriver_win32\chromedriver")

driver.get('http://demo.automationtesting.in/FileDownload.html')
driver.maximize_window()

driver.find_element(By.ID,'pdfbox').send_keys("hello all")
driver.find_element(By.ID,'createPdf').click()
driver.find_element(By.XPATH,'//*[@id="pdf-link-to-download"]').click()
time.sleep(2)
driver.close()
 