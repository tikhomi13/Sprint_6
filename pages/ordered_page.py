import allure
from pages.base_page import BasePage
from locators.ordered_page_locators import OrderedPageLocators


@allure.step('Класс Страница созданного заказа (после подтверждения анкеты')
class OrderedPage(BasePage):

    @allure.step("Элемент 'Отменить заказ' на странице активного заказа")
    def get_cancel_button(self):

        cancel_button = self.find_element_located(OrderedPageLocators.CANCEL_ORDER_BUTTON_IS_CLICKABLE)
        return cancel_button
