import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.24h.com.vn/")
the_thao = driver.find_element("xpath", "/html/body/div[2]/header/nav/div/div/ul/li[6]/a/span[2]")
the_thao.click()
bong_da = driver.find_element("xpath", "/html/body/div[2]/header/nav/div/div/ul/li[1]/a/span[2]")
bong_da.click()

time.sleep(3)

driver.quit()

print("success")
