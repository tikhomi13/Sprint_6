import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.yandex_page import RedirectToYandex


#from pages.order_page_1 import OrderPageOne
#from pages.order_page_2 import OrderPageTwo
#from pages.main_page import MainPage   # CIRCULAR ERROR! ! !

@allure.step('Класс Страница заказа (после подтверждения анкеты')
class OrderedPage(BasePage):

    CANCEL_ORDER_BUTTON_IS_CLICKABLE = (By.XPATH, "//div/button[(text()='Отменить заказ')]")

    # LINK_TO_DZEN = (By.XPATH, "//div/a[(@class='Header_LogoYandex__3TSOI' and @href='//yandex.ru')]")

    @allure.step("Элемент 'Отменить заказ' на странице заказа")
    def get_cancel_button(self):

        cancel_button = self.wait_and_find_element(self.CANCEL_ORDER_BUTTON_IS_CLICKABLE)
        return cancel_button

