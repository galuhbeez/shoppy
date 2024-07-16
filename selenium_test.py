from selenium import webdriver
from selenium.webdriver.common.keys import Keys

service = webdriver.ChromeService(executable_path = './chromedriver')
driver = webdriver.Chrome(service=service)
driver.get("https://www.python.org")
print(driver.title)

search_box = driver.find_element("name", "q")
search_box.clear()
search_box.send_keys("getting started with python")
search_box.submit()
print(driver.current_url)