import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators
#from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By

from locators import Locators

# from pages.main_page import MainPage circular err


class BasePage:



    def __init__(self, driver): # тесты делаем отдельно. То есть для страницы Об аренде у нас класс страница и тесты на каждое поле
        self.driver = driver     # переделать структуру, два окна это одна страница

    @allure.step('Метод поиска и ожидания элемента')
    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Метод поиска и ожидания элемента с возможностью выставления времени ожидания')
    def find_element_located(self, locator, time=8):    # изменить время в одном из тестов

        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f'Not found {locator}')

    @allure.step('Метод поиска и ожидания нескольких элементов с возможностью выставления времени ожидания')
    def find_elementS_located(self, locator, time=10):

        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator), message=f'Not found {locator}')

    # ПРОДОЛЖИТЬ ТУТ. ПРИМЕНИТЬ ЭТИ МЕТОДЫ В ТЕСТАХ (заменить сарый и проверить работоспособность)

    # Затем перекроить страницы и написать параметризованный тест на два набора данных





    @allure.step('Метод для открытия страниц')
    def open_page(self, url):
        self.driver.get(url)

    @allure.step("Кнопка Самокат в хедере слева")
    def click_samokat_button(self):
        samokat_button = self.wait_and_find_element(Locators.SAMOKAT_BUTTON)
        samokat_button.click()

        #return MainPage(self.driver) ##########


    def switch_to_last_browser_tab(self):

        window_before = self.driver.window_handles
        windows_after = self.driver.switch_to.window(window_before[-1])
        return windows_after

# ввод в поле - называть input ....
