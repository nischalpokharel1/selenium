import unittest

from selenium import webdriver

class SearchEngineTest(unittest.TestCase):
    def testGoogle(self):
        self.driver = webdriver.Chrome(executable_path="C:\selenium drivers\chromedriver_win32\chromedriver")
        self.driver.get("https://www.google.com/")
        print("Title of the page is: " + self.driver.title)
        self.driver.close()


    def testBing(self):
        self.driver = webdriver.Chrome(executable_path="C:\selenium drivers\chromedriver_win32\chromedriver")
        self.driver.get("https://www.bing.com/")
        print("Title of the page is: " + self.driver.title)
        self.driver.close()

    def testFencedAi(self):
        self.driver = webdriver.Chrome(executable_path="C:\selenium drivers\chromedriver_win32\chromedriver")
        self.driver.get("https://fenced.ai/")
        print("Title of the page is: " + self.driver.title)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()