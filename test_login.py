from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://example.com/login")

# Valid credentials test
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
username.send_keys("admin")
password.send_keys("admin123")
password.send_keys(Keys.RETURN)
time.sleep(2)

# TODO: Add assertions for success login

driver.quit()
