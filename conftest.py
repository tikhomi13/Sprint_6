import pytest
from selenium import webdriver
from pages.order_page import OrderPage
from pages.main_page import MainPage
from data import URLs
from data import Contents
from locators.base_page_locators import BasePageLocators
import allure


@allure.title('Фикстура для открытия / завершения сеанса браузера и вкл. полноэкоранного режима')
@pytest.fixture(scope='function')
def driver():

    firefox_driver = webdriver.Firefox()
    firefox_driver.maximize_window()

    yield firefox_driver
    firefox_driver.quit()

@allure.title('Фикстура для предзаполнения формы заказа самоката')
@pytest.fixture()
def order_filled(driver):

    main_page = MainPage(driver)
    main_page.open_page(URLs.BASE_URL)
    main_page.close_cookie_popup()
    main_page.click_order_button(BasePageLocators.ORDER_BUTTON_1_AT_THE_TOP)

    order_page_1 = OrderPage(driver)
    order_page_1.fill_for_whom_page(Contents.FIRSTNAME, Contents.LASTNAME, Contents.ADDRESS, Contents.PHONE)

    go_to_next_page = order_page_1.click_next_to_the_second_page()
    go_to_next_page.get_header_2()

    order_page_2 = OrderPage(driver)
    order_page_2.fill_about_rent_page(Contents.ADD_COMMENT)
    order_page_2.order_and_confirm()

    go_to_next_page_ordered_page = order_page_2.go_to_show_status_page()
    go_to_next_page_ordered_page.get_cancel_button()

    yield driver
