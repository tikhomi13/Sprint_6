import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

#from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By

from locators import Locators

# from pages.main_page import MainPage circular err


class BasePage:

   # ORDER_BUTTON_1_AT_THE_TOP = (By.XPATH, ".//div/button[@class='Button_Button__ra12g' and (text()='Заказать')]")

    # SAMOKAT_BUTTON = (By.XPATH, "//div/a[(@class='Header_LogoScooter__3lsAR' and @href='/')]")

    # - YANDEX_DZEN_BUTTON = (By.XPATH, ".//a/img[@alt='Yandex']")
    # + LINK_TO_DZEN = (By.XPATH, "//div/a[(@class='Header_LogoYandex__3TSOI' and @href='//yandex.ru')]")



    def __init__(self, driver): # тесты делаем отдельно. То есть для страницы Об аренде у нас класс страница и тесты на каждое поле
        self.driver = driver     # переделать структуру, два окна это одна страница

    @allure.step('Метод поиска и ожидания элемента')
    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)




    @allure.step('Метод для открытия страниц')
    def open_page(self, url):
        self.driver.get(url)

    @allure.step("Кнопка Самокат в хедере слева")
    def click_samokat_button(self):
        samokat_button = self.wait_and_find_element(Locators.SAMOKAT_BUTTON)
        samokat_button.click()

        #return MainPage(self.driver) ##########




# ввод в поле - называть input ....
