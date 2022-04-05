#Откройте http://practice.automationtesting.in/
#Нажмите на вкладку "My Account
#В разделе " Register", введите email для регистрации
#В разделе " Register", введите пароль для регистрации
#составьте такой пароль, чтобы отобразилось " или " иначе регистрация не выполнится
#почту и пароль сохраните, потребуюутся в дальнейшем
#Нажмите на кнопку "Registr"
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_id("menu-item-50").click()
driver.find_element_by_id("reg_email").send_keys("Nai@mail.ru")
time.sleep(10)
driver.find_element_by_id("reg_password").send_keys("Nicebook!!!!!!??&&")
time.sleep(10)
driver.find_element_by_xpath("//input[@name='register']").click()
time.sleep(5)
driver.quit()


#Откройте http://practice.automationtesting.in/
#Нажмите на вкладку "My Account"
#В разделе " Login", введите email для логина
#В разделе " Login", введите пароль для логина
#Нажмите на кнопку "Login"
#Добавьте проверку, что на странице есть элемент "Logout"

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_id("menu-item-50").click()
time.sleep(10)
driver.find_element_by_id("username").send_keys("Nai@mail.ru")
time.sleep(10)
driver.find_element_by_id("password").send_keys("Nicebook!!!!!!??&&")
time.sleep(10)
driver.find_element_by_xpath("//input[@type='submit']").click()
close_btn_text = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.XPATH, "//a[@href='http://practice.automationtesting.in/my-account/customer-logout/']"), "Logout"))
time.sleep(5)
driver.quit()


