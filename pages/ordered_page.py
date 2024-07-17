import allure
from pages.base_page import BasePage
from locators import Locators
from data import Contents
from selenium.webdriver.common.by import By



@allure.step('Класс Страница заказа (после подтверждения анкеты')
class OrderedPage(BasePage):

    @allure.step("Элемент 'Отменить заказ' на странице заказа")
    def get_cancel_button(self):

        cancel_button = self.find_element_located(Locators.CANCEL_ORDER_BUTTON_IS_CLICKABLE)
        return cancel_button
