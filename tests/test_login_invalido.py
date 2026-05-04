from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.saucedemo.com/")


driver.find_element(By.ID, "user-name").send_keys("user_invalido")
driver.find_element(By.ID, "password").send_keys("senha_invalida")
driver.find_element(By.ID, "login-button").click()
assert len(driver.find_elements(By.XPATH, "//span[@class='title']")) == 0