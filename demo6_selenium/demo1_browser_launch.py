import time

from selenium import webdriver

d = webdriver.Chrome()

d.get("https://google.com")

d.maximize_window()

time.sleep(10)
print(d.title)
