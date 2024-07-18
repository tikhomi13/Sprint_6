import allure
from pages.base_page import BasePage
from pages.ordered_page import OrderedPage
from locators.order_page_locators import OrderPageLocators


@allure.step('Первая часть анкеты, до нажатия Далее')
class OrderPage(BasePage):

    @allure.step('Надпись Для кого самокат')
    def get_header_1(self):

        order_header_1 = self.wait_and_find_element(OrderPageLocators.WHO_IS_THE_SCOOTER_FOR_CHECK_PAGE)
        return order_header_1
        #  .text - чтобы был текст

    @allure.step('Поле Имя')
    def set_firstname(self, name):

        self.wait_and_find_element(OrderPageLocators.FIRSTNAME_FIELD).send_keys(name)

    @allure.step('Поле Фамилия')
    def set_lastname(self, lastname):

        self.wait_and_find_element(OrderPageLocators.LASTNAME_FIELD).send_keys(lastname)

    @allure.step('Поле Адрес')
    def set_address(self, address):

        self.wait_and_find_element(OrderPageLocators.ADDRESS_FIELD).send_keys(address)

    @allure.step('Выбор метро')
    def set_metro(self):

        my_metro = (self.wait_and_find_element(OrderPageLocators.METRO_LIST))
        my_metro.click()
        my_metro.send_keys('Волоколамск')

        my_station = self.wait_and_find_element(OrderPageLocators.SELECT_METRO)
        my_station.click()

    @allure.step('Телефон')
    def set_phone(self, number):

        self.wait_and_find_element(OrderPageLocators.PHONE_FIELD).send_keys(number)

    @allure.step('Шаг, заполняющий поля Имя Фамилия Адрес Телефон')
    def fill_for_whom_page(self, name, lastname, address, number):

        self.set_firstname(name)
        self.set_lastname(lastname)
        self.set_address(address)
        self.set_metro()
        self.set_phone(number)

    @allure.step('Метод перехода на вторую часть анкеты - OrderPageTwo')
    def click_next_to_the_second_page(self):

        next_button = self.wait_and_find_element(OrderPageLocators.NEXT_BUTTON)
        next_button.click()

        return OrderPage(self.driver)

    @allure.step("Надпись 'Про аренду' в верхней части анкеты")
    def get_header_2(self):

        order_header_2 = self.wait_and_find_element(OrderPageLocators.ABOUT_THE_RENT_CHECK_PAGE)
        return order_header_2

    @allure.step('Выбор даты')
    def set_date(self):

        self.wait_and_find_element(OrderPageLocators.CALENDAR).click()
        self.driver.find_element(*OrderPageLocators.CALENDAR_SELECT_DATE).click()

    @allure.step('Выбор срока аренды')
    def set_rent_period(self):

        select_list = self.find_element_located(OrderPageLocators.RENT_PERIOD_LIST, 9)
        select_list.click()

        select_period = self.find_element_located(OrderPageLocators.SET_RENT_PERIOD)
        select_period.click()

    @allure.step('Выбор черного самоката')
    def set_bike_color_black(self):

        self.wait_and_find_element(OrderPageLocators.BIKE_COLOR_BLACK).click()

    @allure.step('Ввод комментария')
    def fill_comment_field(self, comment):

        add_comment = self.wait_and_find_element(OrderPageLocators.COMMENT_FIELD)
        add_comment.send_keys(comment)

    @allure.step('Шаг, включающий выбор даты, срока аренды, цвета, ввод комментария')
    def fill_about_rent_page(self, comment):

        self.set_date()
        self.set_rent_period()
        self.set_bike_color_black()
        self.fill_comment_field(comment)

    @allure.step("Нажатие 'Да' в окне подтверждения")
    def order_and_confirm(self):

        order_button = self.find_element_located(OrderPageLocators.CREATE_ORDER_BUTTON)
        order_button.click()

        confirm_button = self.find_element_located(OrderPageLocators.CONFIRM_BUTTON_YES)
        confirm_button.click()

        return OrderedPage(self.driver)  # возвращаем следующую страницу

    @allure.step('Переход на страницу заказа')
    def go_to_show_status_page(self):

        show_order_status = self.find_element_located(OrderPageLocators.SHOW_STATUS_BUTTON)
        show_order_status.click()

        return OrderedPage(self.driver)
