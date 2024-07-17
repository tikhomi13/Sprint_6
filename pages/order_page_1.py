import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.order_page_2 import OrderPageTwo   # Падало изза этого. Проверить код

from locators import Locators


@allure.step('Первая часть анкеты, до нажатия Далее')
class OrderPageOne(BasePage):



    @allure.step('Надпись Для кого самокат')
    def get_header_1(self):  #####!!!!

        order_header_1 = self.wait_and_find_element(Locators.WHO_IS_THE_SCOOTER_FOR_CHECK_PAGE)
        return order_header_1   #.text - чтобы был текст

    @allure.step('Поле Имя')
    def set_firstname(self, name):  # попробовать в тесте, надо добавить аргумент

        self.wait_and_find_element(Locators.FIRSTNAME_FIELD).send_keys(name)   # return?

    @allure.step('Поле Фамилия')
    def set_lastname(self, lastname):

        self.wait_and_find_element(Locators.LASTNAME_FIELD).send_keys(lastname)

    @allure.step('Поле Адрес')
    def set_address(self, address):

        self.wait_and_find_element(Locators.ADDRESS_FIELD).send_keys(address)

    @allure.step('Выбор метро')
    def set_metro(self):

        my_metro = (self.wait_and_find_element(Locators.METRO_LIST))

        my_metro.click()   # нужна ли звезда?

        my_metro.send_keys('Волоколамск')

        my_station = self.wait_and_find_element(Locators.SELECT_METRO) # проверить в тесте, может быть ошибка   И здесь
        my_station.click()

    @allure.step('Телефон')
    def set_phone(self, number):

        self.wait_and_find_element(Locators.PHONE_FIELD).send_keys(number)

# там же не сказано проверять отдельно?

    @allure.step('Шаг, заполняющий поля Имя Фамилия Адрес Телефон')
    def fill_for_whom_page(self, name, lastname, address, number): # шаг, проверить сначала методы по отдельности

        self.set_firstname(name)
        self.set_lastname(lastname)
        self.set_address(address)
        self.set_metro()
        self.set_phone(number)

    @allure.step('Метод перехода на вторую часть анкеты - OrderPageTwo')
    def click_next_to_the_second_page(self):

        next_button = self.wait_and_find_element(Locators.NEXT_BUTTON)
        next_button.click()

        return OrderPageTwo(self.driver)







# Не забывать про check в названиях методов

