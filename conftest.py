import pytest
from selenium import webdriver
from pages.base_page import BasePage
from pages.ordered_page import OrderedPage
from pages.order_page_2 import OrderPageTwo
from pages.order_page_1 import OrderPageOne
from pages.main_page import MainPage
from data import URLs
from data import Contents
from locators import Locators

@pytest.fixture(scope='function')
def driver():                     # фикстура, задающая настройки Fierefox

    firefox_driver = webdriver.Firefox()
    firefox_driver.maximize_window()

    yield firefox_driver
    firefox_driver.quit()


@pytest.fixture()
def order_page_1_filled(driver):    # фикстура, заполняющая анкету "Для кого самокат"

    main_page = MainPage(driver)
    main_page.open_page(URLs.BASE_URL)
    main_page.close_cookie_popup()
    # main_page.click_order_button_one()
    main_page.click_order_button(Locators.ORDER_BUTTON_1_AT_THE_TOP)

    order_page_1 = OrderPageOne(driver)
    order_page_1.fill_for_whom_page(Contents.FIRSTNAME, Contents.LASTNAME, Contents.ADDRESS, Contents.PHONE)

    go_to_next_page = order_page_1.click_next_to_the_second_page()
    go_to_next_page.get_header_2()

    yield driver

@pytest.fixture()
def order_page_2_filled(driver, order_page_1_filled):    # фикстура, заполняющая анкету "Про аренду"

    order_page_2 = OrderPageTwo(driver)
    order_page_2.fill_about_rent_page(Contents.ADD_COMMENT)
    order_page_2.order_and_confirm()

    go_to_next_page_ordered_page = order_page_2.go_to_show_status_page()
    go_to_next_page_ordered_page.get_cancel_button()

    yield driver
