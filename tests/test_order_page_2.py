import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.order_page_1 import OrderPageOne
from pages.order_page_2 import OrderPageTwo  #убрать
from pages.ordered_page import OrderedPage

import time
from data import URLs
from data import Contents

@allure.title('Заполнение второй страницы анкеты')
@allure.description('Первая страница анкеты заполнена с помощью фикстуры order_page_1_filled')  # как реализовать второй? Нужна ли здесь параметризация?
class TestOrderPageTwo:

    def test_when_to_deliver_scooter(self, driver, order_page_1_filled):

        order_page_2 = OrderPageTwo(driver)
        order_page_2.fill_about_rent_page(Contents.ADD_COMMENT)
        order_page_2.order_and_confirm()

        go_to_next_page_ordered_page = order_page_2.go_to_show_status_page()
        go_to_next_page_ordered_page.get_cancel_button()

        assert go_to_next_page_ordered_page.get_cancel_button().is_displayed()




