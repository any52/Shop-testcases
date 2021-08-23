from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

# Открыть http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(10)

# Проскроллить страницу вниз на 600 пикселей
driver.execute_script("window.scrollBy(0, 600);")

# Нажать на название книги "Selenium Ruby"
selenium_ruby_btn = driver.find_element_by_xpath("//*[@id='text-22-sub_row_1-0-2-0-0']/div/ul/li/a[1]/h3")
selenium_ruby_btn.click()

# Нажать на вкладку "REVIEWS"
review_tab = driver.find_element_by_css_selector(".reviews_tab > a")
review_tab.click()

# Поставить 5 звёзд
first_star_btn = driver.find_element_by_class_name("star-1")
first_star_btn.click()

second_star_btn = driver.find_element_by_class_name("star-2")
second_star_btn.click()

third_star_btn = driver.find_element_by_class_name("star-3")
third_star_btn.click()

# Заполнить поле "Review" сообщением: "Nice book!"
review_field = driver.find_element_by_name("comment")
review_field.send_keys("Nice book!")

# Заполнить поле "Name"
name = driver.find_element_by_id("author")
name.send_keys("Ivan Petrov")

# Заполнить "Email"
email = driver.find_element_by_id("email")
email.send_keys("ivan_petrov@mail.ru")

# Нажать на кнопку "SUBMIT"
submit_btn = driver.find_element_by_id("submit")
submit_btn.click()

driver.quit()