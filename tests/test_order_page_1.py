import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

#from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.order_page_1 import OrderPageOne
from pages.order_page_2 import OrderPageTwo
import time
from data import URLs
from data import Contents


@allure.title('Класс на заполнение первой страницы анкеты')
@allure.description('Первый набор данных')  # как реализовать второй? Нужна ли здесь параметризация?
class TestOrderPageOne:

    def test_fill_for_whom_page(self, driver):

        order_page_1 = OrderPageOne(driver)
        order_page_1.open_page(URLs.OPEN_SCOOTER_ORDER_PAGE)
        order_page_1.fill_for_whom_page(Contents.FIRSTNAME, Contents.LASTNAME, Contents.ADDRESS, Contents.PHONE)

        go_to_next_page = order_page_1.click_next_to_the_second_page()
        go_to_next_page.get_header_2()                                     # подхватываем элемент, расположенный на новой странице
        assert go_to_next_page.get_header_2().is_displayed()

# второй набор?



    #def test_set_firstname(self, driver):

     #   open_order_1_page = OrderPageOne(driver)
     #   open_order_1_page.open_page(URLs.OPEN_SCOOTER_ORDER_PAGE)
     #   OrderPageOne(driver).set_firstname(Contents.FIRSTNAME)


# Проверить весь флоу



