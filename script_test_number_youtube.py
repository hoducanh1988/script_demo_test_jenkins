import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.youtube.com/")
search_box = driver.find_element("xpath", "/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input")
search_box.send_keys('visual studio')
search_box.submit()

time.sleep(3)

driver.quit()

print("success")
