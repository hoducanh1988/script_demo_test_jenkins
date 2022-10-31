import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://vnexpress.net/")
dash_board = driver.find_element("xpath", "/html/body/header/div/a/span")
dash_board.click()
khoa_hoc = driver.find_element("xpath", "/html/body/section[2]/section/div/div[2]/div/div[1]/div/div/ul[7]/li[1]/a")
khoa_hoc.click()

time.sleep(3)

driver.quit()

print("success")
