from base64 import encode
from selenium import webdriver
PATH = "C:\Users\aitor\Downloads\chromedriver_win32"
driver = webdriver.Chrome(PATH)
driver.get("https://google.com")
driver.quit()