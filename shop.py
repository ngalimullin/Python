#Откройте http://practice.automationtesting.in/
#Залогиньтесь
#Нажмите на вкладку "Shop"
#Откройте книгу "HTML 5 Forms"
#Добавьте тест, что заголовок книги назвается :"HTML5 Forms"
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
driver.find_element_by_id("menu-item-40").click()
driver.find_element_by_xpath("//img[@title='Mastering HTML5 Forms']").click()
h1text = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div h1"), "HTML5 Forms"))
time.sleep(5)
driver.quit()

#Откройте http://practice.automationtesting.in/
#Залогиньтесь
#Нажмите на вкладку "Shop"
#Откройте категорию "HTML"
#Добавьте тест, что отображается три товара
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
driver.find_element_by_id("menu-item-40").click()
driver.find_element_by_xpath("//a[@href='http://practice.automationtesting.in/product-category/html/']").click()
element = driver.find_element_by_css_selector("#woocommerce_product_categories-2 > ul > li.cat-item.cat-item-19.current-cat > span")
element_get_text = element.text
assert element_get_text == "(3)"
print(element_get_text)
time.sleep(5)
driver.quit()

#Откройте http://practice.automationtesting.in/
#Залогиньтесь
#Нажмите на вкладку "Shop"
#Добавьте тест, что в селекторе выбран вариант сортировки по умолчанию
#Отсортируйте товары по цене от большей к меньшей
#Снова объявите переменную с локатором основного селектора сортировки # т.к после сортировки страница обновится
#Добавьте тест, что в селекторе выбран вариант сортировки по цене от большей к меньшей
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_id("menu-item-50").click()
driver.find_element_by_id("username").send_keys("Nai@mail.ru")
driver.find_element_by_id("password").send_keys("Nicebook!!!!!!??&&")
driver.find_element_by_id("menu-item-40").click()
element = driver.find_element_by_css_selector("[value='menu_order']")
test_defalt = element.get_attribute("selected")
assert test_defalt == 'true'
element2 = driver.find_element_by_class_name("orderby")
select = Select(element2)
select.select_by_index("5")
element = driver.find_element_by_css_selector("[value='price-desc']")
test_defalt = element.get_attribute("selected")
assert test_defalt == 'true'
time.sleep(5)
driver.quit()

#Откройте http://practice.automationtesting.in/
#Залогиньтесь
#Нажмите на вкладку "
#Откройте книгу "Android Quick Start
#Добавьте тест, что содержимое старой цены = 600.00 используйте assert
#Добавьте тест, что содержимое новой цены = 450 .00 используйте assert
#Добавьте явное ожидание и нажмите на обложку книги
#Подберите такой селектор и тайминги, чтобы открылось окно предпросмотра картинки (не вся картинка на всю страницу)
#Добавьте явное ожидание и закройте предпросмотр нажав на крестик (кнопка вверху справа)
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_id("menu-item-50").click()
driver.find_element_by_id("username").send_keys("Nai@mail.ru")
time.sleep(2)
driver.find_element_by_id("password").send_keys("Nicebook!!!!!!??&&")
time.sleep(2)
driver.find_element_by_css_selector("[name='login']").click()
driver.find_element_by_id("menu-item-40").click()
driver.find_element_by_css_selector("[href='http://practice.automationtesting.in/product/android-quick-start-guide/']").click()
element = driver.find_element_by_css_selector("div p del span")
test_600 = element.text
assert test_600 == '₹600.00'
element2 = driver.find_element_by_css_selector("ins span")
test_450 = element2.text
assert test_450 == '₹450.00'
img_clic = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='images']"))).click()
time.sleep(10)
driver.find_element_by_css_selector("[class='pp_close']").click()
driver.quit()

#Откройте http://practice.automationtesting.in/ в этом тесте логиниться не нужно
#Нажмите на вкладку "Shop"
#Добавьте в корзину книгу "HTML5 WebApp см. комментарии в самом низу
#Добавьте тест , что возле коризны(вверху справа) количество товаров = 1 Item"Item", а стоимость = 180.00 "
#Используйте для проверки assert
#Перейдите в корзину
#Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость
#Используя явное ожидание, проверьте что в Total отобразилась стоимость
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.find_element_by_id("menu-item-40").click()
driver.find_element_by_css_selector("[href='/shop/?add-to-cart=182']").click()
time.sleep(5)
element = driver.find_element_by_css_selector("[title='View your shopping cart']")
test_Item180 = element.text
assert test_Item180 == "1 Item₹180.00"
driver.find_element_by_class_name("wpmenucart-icon-shopping-cart-0").click()
test_subtotal = WebDriverWait(driver, 20).until(
     EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[data-title='Subtotal']"), "180"))
test_thank = WebDriverWait(driver, 20).until(
     EC.text_to_be_present_in_element((By.TAG_NAME, "strong"), "189"))
time.sleep(3)
driver.quit()

#Откройте http://practice.automationtesting.in/ в этом тесте логиниться не нужно
#Нажмите на вкладку "Shop"
#Добавьте в корзину книги "HTML5 WebApp и "JS Data Structures and"
#Перед добавлением первой книги, проскролльте вниз на 300 пикселей
#После добавления 1 й книги добавьте sleep
#Перейдите в корзину
#Удалите первую книгу
#Перед удалением добавьте sleep
#Нажмите на Undo
#В Quantity увеличьте количесто товара до 3 шт для "JS Data Structures and"
#Предварительно очистите поле с помощью локатор_поля .clear()
#Нажмите на кнопку "UPDATE BASKET"
#Добавьте тест, что value элемента quantity для "JS Data Structures and равно 3 используйте assert
#Нажмите на кнопку "APPLY"
#Перед нажатимем добавьте sleep
#Добавьте тест, что возникло сообщение : "Please enter a coupon code"

from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_id("menu-item-40").click()
driver.execute_script("window.scrollBy(0, 300);")
driver.find_element_by_css_selector("[href='/shop/?add-to-cart=182']").click()
driver.find_element_by_css_selector("[data-product_id='180']").click()
driver.find_element_by_css_selector("[title='View your shopping cart']").click()
driver.find_element_by_css_selector("[data-product_id='182']").click()
driver.find_element_by_link_text("Undo?").click()
driver.find_element_by_css_selector("[name='cart[045117b0e0a11a242b9765e79cbf113f][qty]']").clear()
driver.find_element_by_css_selector("[name='cart[045117b0e0a11a242b9765e79cbf113f][qty]']").send_keys("3")
driver.find_element_by_css_selector("[name='update_cart']").click()
time.sleep(3)
element = driver.find_element_by_css_selector("[name='cart[045117b0e0a11a242b9765e79cbf113f][qty]']")
test_input = element.get_attribute("value")
assert test_input == "3"
time.sleep(3)
driver.find_element_by_css_selector("[value='Apply Coupon']").click()
time.sleep(3)
element = driver.find_element_by_class_name("woocommerce-error")
test_error = element.text
assert test_error == "Please enter a coupon code."
time.sleep(3)
driver.quit()

#Откройте http://practice.automationtesting.in/ в этом тесте логиниться не нужно
#Нажмите на вкладку " и проскролльте на 300 пикселей вниз
#Добавьте в корзину книгу "HTML5 WebApp
#Перейдите в корзину
#Нажмите "PROCEED TO"
#Перед нажатием, добавьте явное ожидание
#Заполните все обязательные поля
#Выберите способ оплаты "Check"
#Нажмите PLACE ORDER
#Используя явное ожидание, проверьте что отображается надпись "Thank you. Your order has been"
#Используя явное ожидание, проверьте что в Payment Method отображается текст "Check"
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.find_element_by_id("menu-item-40").click()
driver.execute_script("window.scrollBy(0, 300);")
driver.find_element_by_css_selector("[href='/shop/?add-to-cart=182']").click()
time.sleep(2)
driver.find_element_by_css_selector("[title='View your shopping cart']").click()
proceed_btn = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[href='http://practice.automationtesting.in/checkout/']"))).click()
name_input = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='billing_first_name']"))).send_keys("Ivan")
driver.find_element_by_css_selector("[name='billing_last_name']").send_keys("Ivanov")
driver.find_element_by_css_selector("[name='billing_email']").send_keys("mail@mail.ru")
driver.find_element_by_css_selector("[name='billing_phone']").send_keys("8123589623")
driver.find_element_by_id("s2id_billing_country").click()
driver.find_element_by_id("s2id_autogen1_search").send_keys("Russia")
driver.find_element_by_id("select2-results-1").click()
driver.find_element_by_id("billing_address_1").send_keys("Russia")
driver.find_element_by_id("billing_city").send_keys("Samara")
driver.find_element_by_id("billing_state").send_keys("Samarskaya")
driver.find_element_by_id("billing_postcode").send_keys("123456")
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(5)
driver.find_element_by_id("payment_method_cheque").click()
driver.find_element_by_id("place_order").click()
test_thank = WebDriverWait(driver, 20).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"),"Thank you. Your order has been received."))
test_Check = WebDriverWait(driver, 20).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tfoot tr:nth-child(3)"),"Check Payments"))
time.sleep(3)
driver.quit()