import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.order_page_2 import OrderPageTwo   # Падало изза этого. Проверить код


@allure.step('Первая часть анкеты, до нажатия Далее')
class OrderPageOne(BasePage):

    WHO_IS_THE_SCOOTER_FOR_CHECK_PAGE = (By.XPATH, ".//div[(text()='Для кого самокат')]")  # Для кого самокат

    FIRSTNAME_FIELD = (By.XPATH, "//div/input[@placeholder='* Имя']")

    LASTNAME_FIELD = (By.XPATH, "//div/input[@placeholder='* Фамилия']")

    ADDRESS_FIELD = (By.XPATH, "//div/input[@placeholder='* Адрес: куда привезти заказ']")

    METRO_LIST = (By.XPATH, ".//input[@class='select-search__input' and @placeholder='* Станция метро']")

    SELECT_METRO = (By.XPATH, "//div[(text()='Волоколамская')]")

    # 1) кликаем на проблемный div: div class="select-search__value"
    # 2) Нажимаем ПКМ - Приостанавливаться на - Изменении поддерева (т е страница останавливается когда меняется DOM)
    # 3) Можем посмотреть что происходит внтури контейнера - появляется нужный див со списком станций
    # 4) Снова кликаем по полю. Видим div class="select-search__select"
    # 5) Это называется остановка на модификации поддерева. Есть еще остановка на изменении атрибутов итд
    # 6) Видео в телеграм. Второй набор данных сделать с Другой станцией

    PHONE_FIELD = (By.XPATH, "//div/input[@placeholder='* Телефон: на него позвонит курьер']")

    NEXT_BUTTON = (By.XPATH, ".//div/button[(@class='Button_Button__ra12g Button_Middle__1CSJM') and (text()='Далее')]")

    @allure.step('Надпись Для кого самокат')
    def get_header_1(self):  #####!!!!

        order_header_1 = self.wait_and_find_element(self.WHO_IS_THE_SCOOTER_FOR_CHECK_PAGE)
        return order_header_1   #.text - чтобы был текст

    @allure.step('Поле Имя')
    def set_firstname(self, name):  # попробовать в тесте, надо добавить аргумент

        self.wait_and_find_element(self.FIRSTNAME_FIELD).send_keys(name)   # return?

    @allure.step('Поле Фамилия')
    def set_lastname(self, lastname):

        self.wait_and_find_element(self.LASTNAME_FIELD).send_keys(lastname)

    @allure.step('Поле Адрес')
    def set_address(self, address):

        self.wait_and_find_element(self.ADDRESS_FIELD).send_keys(address)

    @allure.step('Выбор метро')
    def set_metro(self):

        my_metro = (self.wait_and_find_element(self.METRO_LIST))

        my_metro.click()   # нужна ли звезда?

        my_metro.send_keys('Волоколамск')

        my_station = self.wait_and_find_element(self.SELECT_METRO) # проверить в тесте, может быть ошибка   И здесь
        my_station.click()

    @allure.step('Телефон')
    def set_phone(self, number):

        self.wait_and_find_element(self.PHONE_FIELD).send_keys(number)

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

        next_button = self.wait_and_find_element(self.NEXT_BUTTON)
        next_button.click()

        return OrderPageTwo(self.driver)


# Не забывать про check в названиях методов

