import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

# Registration_login: регистрация аккаунта
# Открыть http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(10)

# Нажать на вкладку "My Account Menu"
my_account_tab = driver.find_element_by_link_text("My Account")
my_account_tab.click()

#В разделе "Register", ввести email для регистрации
email = "ivan_petrov@mail.ru"
email_field = driver.find_element_by_id("reg_email")
email_field.send_keys(email)

# В разделе "Register", ввести пароль для регистрации
password = "askj28H@l!"
password_field = driver.find_element_by_id("reg_password")
password_field.send_keys(password)

# Нажать на кнопку "Register"
register_btn = driver.find_element_by_name("register")
register_btn.click()

driver.quit()
time.sleep(1)

# Registration_login: логин в систему
# Открыть http://practice.automationtesting.in/
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(10)

# Нажать на вкладку "My Account Menu"
my_account_tab = driver.find_element_by_link_text("My Account")
my_account_tab.click()

# В разделе "Login", ввести email для логина
email_field = driver.find_element_by_id("username")
email_field.send_keys(email)

# В разделе "Login", ввести пароль для логина
password_field = driver.find_element_by_id("password")
password_field.send_keys(password)

# Нажать на кнопку "Login"
login_btn = driver.find_element_by_name("login")
login_btn.click()

# Проверка, что на странице есть элемент "Logout"
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id='page-36']/div/div[1]/nav/ul/li[6]/a")))

driver.quit()