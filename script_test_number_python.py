import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.python.org/")
about = driver.find_element("xpath", "/html/body/div/header/div/nav/ul/li[1]/a")
about.click()

time.sleep(3)

driver.quit()

print("success")
