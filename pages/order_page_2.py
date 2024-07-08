import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.ordered_page import OrderedPage
#from pages.order_page_1 import OrderPageOne --> circular import ERROR. Не повторять

@allure.step('Вторая часть анкеты заказа, до нажатия "Заказать"')
class OrderPageTwo(BasePage):

    ABOUT_THE_RENT_CHECK_PAGE = (By.XPATH, ".//div[(text()='Про аренду')]")                # Про аренду

    CALENDAR = (By.XPATH, ".//div[@class='react-datepicker__input-container']/input[@placeholder='* Когда привезти самокат']/parent::div")

    CALENDAR_SELECT_DATE = (By.XPATH, ".//div[(@class='react-datepicker')]//div[@aria-label='Choose вторник, 2-е июля 2024 г.']")

    RENT_PERIOD_LIST = (".//div[(text()='* Срок аренды')]/parent::div[@class='Dropdown-control']")

    SELECT_RENT_PERIOD = (By.XPATH, ".//div[(text()='двое суток')]") ###

    BIKE_COLOR_BLACK = (By.XPATH, ".//div[@class='Order_Checkboxes__3lWSI']/label[(text()='чёрный жемчуг')]")  # кликнуть

    COMMENT_FIELD = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']") #click

    ORDER_BUTTON = (By.XPATH, ".//div[@class='Order_Buttons__1xGrp']/button[(text()='Заказать')]")

    CONFIRM_BUTTON_YES = (By.XPATH, ".//button[(text()='Да')]")

    ORDER_ADDED = (By.XPATH, ".//div[@class='Order_ModalHeader__3FDaJ' and (text()='Заказ оформлен')]")  # is displayed

    SHOW_STATUS_BUTTON = (By.XPATH, "//div/button[(text()='Посмотреть статус')]")

    @allure.step("Надпись 'Про аренду' в верхней части анкеты")
    def get_header_2(self):

        order_header_2 = self.wait_and_find_element(self.ABOUT_THE_RENT_CHECK_PAGE)
        return order_header_2

    @allure.step('Выбор даты')
    def set_date(self):

        self.wait_and_find_element(self.CALENDAR).click()     # Добавить аргументы и в шаг тоже
        self.driver.find_element(*self.CALENDAR_SELECT_DATE).click()

    @allure.step('Выбор срока аренды')
    def set_rent_period(self):

        select_list = self.driver.find_element(By.XPATH, ".//div[(text()='* Срок аренды')]/parent::div[@class='Dropdown-control']")

        select_list.click()

        select_period = self.driver.find_element(By.XPATH, ".//div[(text()='двое суток')]")

        select_period.click()
    @allure.step('Выбор черного самоката')

    def set_bike_color_black(self):          # добавить серый ?

        self.wait_and_find_element(self.BIKE_COLOR_BLACK).click()
    @allure.step('Ввод комментария')
    def fill_comment_field(self, comment):

        add_comment = self.wait_and_find_element(self.COMMENT_FIELD)   #.click()
        add_comment.send_keys(comment)

    @allure.step('Шаг, включающий выбор даты, срока аренды, цвета, ввод комментария')
    def fill_about_rent_page(self, comment):

        self.set_date()
        self.set_rent_period()
        self.set_bike_color_black()
        self.fill_comment_field(comment)

    @allure.step("Нажатие 'Да' в окне подтверждения")
    def order_and_confirm(self):

        order_button = self.wait_and_find_element(self.ORDER_BUTTON)
        order_button.click()

        confirm_button = self.wait_and_find_element(self.CONFIRM_BUTTON_YES)
        confirm_button.click()

        return OrderedPage(self.driver)  # возвращаем следующую страницу

    @allure.step('Переход на страницу заказа')
    def go_to_show_status_page(self):
        show_order_status = self.wait_and_find_element(self.SHOW_STATUS_BUTTON)
        show_order_status.click()

        return OrderedPage(self.driver)


    # @allure.step()
    # И здесь шаг. Потом разобраться с метро ъ


    # где дзен - там шаг


