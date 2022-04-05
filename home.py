#Откройте http://practice.automationtesting.in/
#Проскролльте страницу вниз на 6 00 пикселей
#Нажмите на название книги "Selenium Ruby" или на кнопку "READ
#Нажмите на вкладку "REVIEWS"
#Поставьте 5 звёзд
#Заполните поле "Review" сообщением : "Nice book!"
#Заполните поле "Name"
#Заполните "Email"
#Нажмите на кнопку "Submit"

from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0, 1000);")
driver.find_element_by_xpath("//a[@rel='nofollow']").click()
driver.find_element_by_xpath("//a[@href='#tab-reviews']").click()
driver.find_element_by_css_selector(".stars .star-5").click()
driver.find_element_by_id("comment").send_keys("Nice book!")
driver.find_element_by_id("author").send_keys("Nail")
driver.find_element_by_id("email").send_keys("Nail@mail.ru")
driver.find_element_by_id("submit").click()
time.sleep(5)
driver.quit()


