import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

#por o user
#por a senha
#clickar no botão login
#add produto ao carrinho
#entrar no carrinho
#verificar se foi adicionado

#login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

#add ao carrinho diretamente da pagina inicial
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

#add ao carrinho clicando no produto, pela página do produto
driver.find_element(By.ID, "item_0_title_link").click()
driver.find_element(By.ID, "add-to-cart").click()

#verificar se foi adicionado ao carrinho
driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
assert driver.find_element(By.XPATH, "//div[@class='inventory_item_name' and contains(text(), 'Sauce Labs Backpack')]").is_displayed()
assert driver.find_element(By.XPATH, "//div[@class='inventory_item_name' and contains(text(), 'Sauce Labs Bike Light')]").is_displayed()