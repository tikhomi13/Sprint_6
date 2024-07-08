# Файл для тестового кода

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

base_url = 'https://qa-mesto.praktikum-services.ru/'

# инициализируем драйвер браузера

firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument('--window-size=1920,1080')
driver = webdriver.Firefox(options=firefox_options)

time.sleep(5)

driver.quit()



def test_check_email_placeholder():
    driver = webdriver.Firefox()
    driver.get(base_url)

    email = driver.find_element(By.ID, "email")

    assert email.get_attribute("placeholder") == 'Email'

    driver.quit()

def test_check_password_placeholder():
    driver = webdriver.Firefox()
    driver.get(base_url)

    password = driver.find_element(By.ID, "password")

    assert password.get_attribute("placeholder") == 'Пароль'

    driver.quit()
