import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
#from pages.order_page_2 import OrderPageTwo   # Падало изза этого. Проверить код
from pages.ordered_page import OrderedPage


from pages.ordered_page import OrderedPage

from locators import Locators


@allure.step('Первая часть анкеты, до нажатия Далее')
class OrderPage(BasePage):



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

        return OrderPage(self.driver)

    # бывший order_page_2

    @allure.step("Надпись 'Про аренду' в верхней части анкеты")
    def get_header_2(self):

        order_header_2 = self.wait_and_find_element(Locators.ABOUT_THE_RENT_CHECK_PAGE)
        return order_header_2

    @allure.step('Выбор даты')
    def set_date(self):

        self.wait_and_find_element(Locators.CALENDAR).click()     # Добавить аргументы и в шаг тоже
        self.driver.find_element(*Locators.CALENDAR_SELECT_DATE).click()

    @allure.step('Выбор срока аренды')
    def set_rent_period(self):

        select_list = self.driver.find_element(By.XPATH, ".//div[(text()='* Срок аренды')]/parent::div[@class='Dropdown-control']") # ВЫНЕСТИ

        select_list.click()

        select_period = self.driver.find_element(By.XPATH, ".//div[(text()='двое суток')]") # ВЫНЕСТИ

        select_period.click()
    @allure.step('Выбор черного самоката')

    def set_bike_color_black(self):          # добавить серый ?

        self.wait_and_find_element(Locators.BIKE_COLOR_BLACK).click()
    @allure.step('Ввод комментария')
    def fill_comment_field(self, comment):

        add_comment = self.wait_and_find_element(Locators.COMMENT_FIELD)   #.click()
        add_comment.send_keys(comment)

    @allure.step('Шаг, включающий выбор даты, срока аренды, цвета, ввод комментария')
    def fill_about_rent_page(self, comment):

        self.set_date()
        self.set_rent_period()
        self.set_bike_color_black()
        self.fill_comment_field(comment)

    @allure.step("Нажатие 'Да' в окне подтверждения")
    def order_and_confirm(self):

        order_button = self.find_element_located(Locators.CREATE_ORDER_BUTTON)
        order_button.click()

        confirm_button = self.find_element_located(Locators.CONFIRM_BUTTON_YES)
        confirm_button.click()

        return OrderedPage(self.driver)  # возвращаем следующую страницу

    @allure.step('Переход на страницу заказа')
    def go_to_show_status_page(self):

        show_order_status = self.find_element_located(Locators.SHOW_STATUS_BUTTON)
        show_order_status.click()

        return OrderedPage(self.driver)








# Не забывать про check в названиях методов

