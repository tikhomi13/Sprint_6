from selenium.webdriver.common.by import By
import allure

@allure.title('Локаторы для главной страницы Яндекс Дзен')
class YandexPageLocators:

    CLOSE_POPUP = (By.XPATH, ".//div[3]/div/div[1]/div/div/div/div/span")

    LOGO_YA = (By.XPATH, ".//div/header/div[contains(@class, 'desktop-base-header')]/a")
