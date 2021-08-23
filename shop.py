import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome()
driver.maximize_window()

# Shop: отображение страницы товара
# Открыть http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(10)

# Логин
my_account_tab = driver.find_element_by_link_text("My Account")
my_account_tab.click()
email = "ivan_petrov@mail.ru"
email_field = driver.find_element_by_id("username")
email_field.send_keys(email)
password = "askj28H@l!"
password_field = driver.find_element_by_id("password")
password_field.send_keys(password)
login_btn = driver.find_element_by_name("login")
login_btn.click()

# Нажать на вкладку "Shop"
shop_tab = driver.find_element_by_link_text("Shop")
shop_tab.click()

# Открыть книгу "HTML 5 Forms"
html_5_book = driver.find_element_by_xpath("//*[@id='content']/ul/li[3]/a[1]/h3")
html_5_book.click()

# Добавить тест, что заголовок книги назвается: "HTML5 Forms"
book_title = driver.find_element_by_class_name("product_title")
print("Заголовок книги назвается: " + book_title.text)

driver.quit()
time.sleep(1)

# Shop: количество товаров в категории
# Открыть http://practice.automationtesting.in/
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(10)

# Логин
my_account_tab = driver.find_element_by_link_text("My Account")
my_account_tab.click()
email = "ivan_petrov@mail.ru"
email_field = driver.find_element_by_id("username")
email_field.send_keys(email)
password = "askj28H@l!"
password_field = driver.find_element_by_id("password")
password_field.send_keys(password)
login_btn = driver.find_element_by_name("login")
login_btn.click()

# Нажать на вкладку "Shop"
shop_tab = driver.find_element_by_link_text("Shop")
shop_tab.click()

# Открыть категорию "HTML"
HTML_link = driver.find_element_by_link_text("HTML")
HTML_link.click()

# Добавить тест, что отображается три товара
books = driver.find_elements_by_css_selector("[class = 'products masonry-done'] h3")
print("Отображается " + str(len(books)) + " товара")

driver.quit()
time.sleep(1)

# Shop: сортировка товаров
## Открыть http://practice.automationtesting.in/
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(10)

# Логин
my_account_tab = driver.find_element_by_link_text("My Account")
my_account_tab.click()
email = "ivan_petrov@mail.ru"
email_field = driver.find_element_by_id("username")
email_field.send_keys(email)
password = "askj28H@l!"
password_field = driver.find_element_by_id("password")
password_field.send_keys(password)
login_btn = driver.find_element_by_name("login")
login_btn.click()

# Нажать на вкладку "Shop"
shop_tab = driver.find_element_by_link_text("Shop")
shop_tab.click()

# Проверка, что в селекторе выбран вариант сортировки по умолчанию
default_sorting = driver.find_element_by_css_selector("[value='menu_order']")
assert default_sorting.text == "Default sorting"

# Сортировка товаров от большего к меньшему
order_by = driver.find_element_by_class_name("orderby")
order_by_selector = Select(order_by)
order_by_selector.select_by_value("price-desc")

# Проверка, что в селекторе выбран вариант сортировки от большего к меньшему
high_low_sorting = driver.find_element_by_css_selector("[value='price-desc']")
assert high_low_sorting.text == "Sort by price: high to low"

driver.quit()
time.sleep(1)

# Shop: отображение, скидка товара
## Открыть http://practice.automationtesting.in/
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(10)

# Логин
my_account_tab = driver.find_element_by_link_text("My Account")
my_account_tab.click()
email = "ivan_petrov@mail.ru"
email_field = driver.find_element_by_id("username")
email_field.send_keys(email)
password = "askj28H@l!"
password_field = driver.find_element_by_id("password")
password_field.send_keys(password)
login_btn = driver.find_element_by_name("login")
login_btn.click()

# Нажать на вкладку "Shop"
shop_tab = driver.find_element_by_link_text("Shop")
shop_tab.click()

# Открыть книгу "Android Quick Start Guide"
android_book = driver.find_element_by_xpath("//*[@id='content']/ul/li[1]/a[1]/h3")
android_book.click()

# Проверка, что содержимое старой цены = "₹600.00"
old_price = driver.find_element_by_css_selector("del [class = 'woocommerce-Price-amount amount']")
assert old_price.text == "₹600.00"

# Проверка, что содержимое новой цены = "₹450.00"
new_price = driver.find_element_by_css_selector("ins [class = 'woocommerce-Price-amount amount']")
assert new_price.text == "₹450.00"

# Добавить явное ожидание и нажать на обложку книги
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "[class = 'attachment-shop_single size-shop_single wp-post-image']")))

android_image = driver.find_element_by_css_selector("[class = 'attachment-shop_single size-shop_single wp-post-image']")
android_image.click()

# Добавить явное ожидание и закрыть предпросмотр
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "pp_close")))

close_btn = driver.find_element_by_class_name("pp_close")
close_btn.click()

driver.quit()
time.sleep(1)

# Shop: проверка цены в корзине
## Открыть http://practice.automationtesting.in/
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(10)

# Нажать на вкладку "Shop"
shop_tab = driver.find_element_by_link_text("Shop")
shop_tab.click()

# Добавить в корзину книгу "HTML5 WebApp Development"
add_btn = driver.find_element_by_css_selector("[href='/shop/?add-to-cart=182']")
add_btn.click()
time.sleep(1)

# Проверка, что в возле коризны(вверху справа) количество товаров = "1 Item", а стоимость = "₹180.00"
number_items =  driver.find_element_by_class_name("cartcontents")
assert number_items.text == "1 Item"

cost = driver.find_element_by_css_selector(".wpmenucart-contents .amount")
assert cost.text == "₹180.00"

# Перейти в корзину
number_items.click()

# Используя явное ожидание, проверить что в Total отобразилась стоимость
total_cost = WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".product-price [class = 'woocommerce-Price-amount amount']"), "₹180.00"))


# Используя явное ожидание, проверить что в Subtotal отобразилась стоимость
subtotal_cost = WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal [class='woocommerce-Price-amount amount']"), "₹180.00"))

driver.quit()
time.sleep(1)

# Shop: работа в корзине
## Открыть http://practice.automationtesting.in/
path_to_extension = r'C:\Users\Anna\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\4.34.0_0'
chrome_options = Options()
chrome_options.add_argument('load-extension=' + path_to_extension)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.create_options()
time.sleep(10)
driver.maximize_window()
# Неявное ожидание поиска элементов
driver.implicitly_wait(10)
first_browser_tab = driver.window_handles[0]
driver.switch_to.window(first_browser_tab)
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(20)

# Нажать на вкладку "Shop"
shop_tab = driver.find_element_by_link_text("Shop")
shop_tab.click()

# Добавить в корзину книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm"
driver.execute_script("window.scrollBy(0, 300);")

add_HTML5_book_btn = driver.find_element_by_css_selector("[href='/shop/?add-to-cart=182']")
add_HTML5_book_btn.click()
time.sleep(1)

add_js_data_book_btn = driver.find_element_by_css_selector("[href='/shop/?add-to-cart=180']")
add_js_data_book_btn.click()
time.sleep(1)

# Перейти в корзину
number_items = driver.find_element_by_class_name("cartcontents")
number_items.click()

# Удалить первую книгу
time.sleep(1)
remove_btns_for_all_books = driver.find_elements_by_css_selector("[title = 'Remove this item']")
remove_btns_for_all_books[0].click()

# Нажать на Undo (отмена удаления)
undo_link = driver.find_element_by_link_text("Undo?")
undo_link.click()
time.sleep(1)

# В Quantity увеличить количесто товара до 3 шт для "JS Data Structures and Algorithm“
quantities_for_js_data_book = driver.find_element_by_xpath("//*[@id='page-34']/div/div[1]/form/table/tbody/tr[1]/td[5]/div/input")
quantities_for_js_data_book.clear()
quantities_for_js_data_book.send_keys("3")

# Нажмите на кнопку "UPDATE BASKET"
update_basket_btn = driver.find_element_by_name("update_cart")
update_basket_btn.click()

# Добавить тест, что value элемента quantity для "JS Data Structures and Algorithm" равно 3
value_quantity = quantities_for_js_data_book.get_attribute("value")
assert value_quantity == "3"

# Нажать на кнопку "APPLY COUPON"
time.sleep(3)
apply_coupon_btn = driver.find_element_by_name("apply_coupon")
apply_coupon_btn.click()

# Добавить тест, что возникло сообщение: "Please enter a coupon code."
WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-error"), "Please enter a coupon code."))

driver.quit()
time.sleep(1)

# Shop: покупка товара
## Открыть http://practice.automationtesting.in/
path_to_extension = r'C:\Users\Anna\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\4.34.0_0'
chrome_options = Options()
chrome_options.add_argument('load-extension=' + path_to_extension)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.create_options()
time.sleep(10)
driver.maximize_window()
# Неявное ожидание поиска элементов
driver.implicitly_wait(10)
first_browser_tab = driver.window_handles[0]
driver.switch_to.window(first_browser_tab)
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(20)

# Нажать на вкладку "Shop"
shop_tab = driver.find_element_by_link_text("Shop")
shop_tab.click()

# Добавить в корзину книги "HTML5 WebApp Development"
driver.execute_script("window.scrollBy(0, 300);")

add_HTML5_book_btn = driver.find_element_by_css_selector("[href='/shop/?add-to-cart=182']")
add_HTML5_book_btn.click()
time.sleep(1)

# Перейти в корзину
number_items = driver.find_element_by_class_name("cartcontents")
number_items.click()

# Нажать на "PROCEED TO CHECKOUT"
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "[class = 'checkout-button button alt wc-forward']")))
proceed_to_checkout_btn = driver.find_element_by_css_selector("[class = 'checkout-button button alt wc-forward']")
proceed_to_checkout_btn.click()

# Заполнить все обязательные поля
WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#billing_first_name_field label"), "First Name "))
first_name = driver.find_element_by_id("billing_first_name").send_keys("Ivan")
last_name = driver.find_element_by_id("billing_last_name").send_keys("Petrov")
email = driver.find_element_by_id("billing_email").send_keys("ivan_petrov@mail.ru")
phone = driver.find_element_by_id("billing_phone").send_keys("9305843210")
country = driver.find_element_by_id("billing_country")
country_selector = Select(country).select_by_value("RU")
address = driver.find_element_by_name("billing_address_1").send_keys("Sovetskaya")
city = driver.find_element_by_name("billing_city").send_keys("Saint-Petersburg")
state = driver.find_element_by_name("billing_state").send_keys("Saint-Petersburg")
post_code = driver.find_element_by_name("billing_postcode").send_keys("190000")

# Выбрать способ оплаты "Check Payments"
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(2)
check_payments_btn = driver.find_element_by_id("payment_method_cheque")
check_payments_btn.click()

# Нажать PLACE ORDER
place_order_btn = driver.find_element_by_id("place_order")
place_order_btn.click()

# Используя явное ожидание, проверить что отображается надпись "Thank you. Your order has been received."
WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[class = 'woocommerce-thankyou-order-received']"), "Thank you. Your order has been received."))

# Используя явное ожидание, проверить что в Payment Method отображается текст "Check Payments"
WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.XPATH, "//*[@id='page-35']/div/div[1]/table/tfoot/tr[3]/td"), "Check Payments"))

driver.quit()

