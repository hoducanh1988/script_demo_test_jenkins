import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.google.com")
search_box = driver.find_element("name", "q")
search_box.send_keys('selenium')
search_box.submit()

time.sleep(3)

driver.quit()
