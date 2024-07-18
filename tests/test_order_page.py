import allure
import pytest

from pages.order_page import OrderPage
from pages.base_page import BasePage
from pages.main_page import MainPage  # [хм хм]
from pages.yandex_page import RedirectToYandex
from locators.main_page_locators import MainPageLocators
from locators.base_page_locators import BasePageLocators
from data import URLs
from data import Contents


@allure.title('Класс на заполнение анкеты с разным набором данных')
@allure.description('Первый набор данных')
class TestOrderPage:

    data_user = [

        [BasePageLocators.ORDER_BUTTON_1_AT_THE_TOP, Contents.FIRSTNAME, Contents.LASTNAME, Contents.ADDRESS, Contents.PHONE, Contents.ADD_COMMENT],
        [MainPageLocators.ORDER_BUTTON_2_AT_THE_BOTTOM, Contents.FIRSTNAME_2, Contents.LASTNAME_2, Contents.ADDRESS_2, Contents.PHONE_2, Contents.ADD_COMMENT_2]
    ]

    @pytest.mark.parametrize('button,firstname,lastname,address,phone,comment', data_user)
    def test_check_place_an_order(self, driver, button, firstname, lastname, address, phone, comment):

        open_main_page = MainPage(driver)
        open_main_page.open_page(URLs.BASE_URL)
        open_main_page.close_cookie_popup()

        open_main_page.click_order_button(button)
        order_page = OrderPage(driver)

        order_page.open_page(URLs.OPEN_SCOOTER_ORDER_PAGE)
        order_page.fill_for_whom_page(firstname, lastname, address, phone)
        order_page.click_next_to_the_second_page()

        order_page.fill_about_rent_page(comment)
        order_page.order_and_confirm()

        go_to_next_page_ordered_page = order_page.go_to_show_status_page()
        go_to_next_page_ordered_page.get_cancel_button()

        assert go_to_next_page_ordered_page.get_cancel_button().is_displayed()

    @allure.title('Тест перехода на главную страницу со страницы созданного заказа')
    @allure.description('Переход с помощью кнопки Самокат. Для предзаполнения страниц исп. фикстура order_filled')
    @allure.link(URLs.BASE_URL, name='Тестовая ссылка')
    def test_go_to_main_from_order(self, driver, order_filled):

        back_to_main = BasePage(driver)
        back_to_main.click_samokat_button()

        main_screen = MainPage(driver)
        assert main_screen.slogan_on_main_page().is_displayed()
    @allure.title('Тест перехода с сайта Яндекс Самокат на главную Яндекс Дзен')
    def test_go_to_dzen(self, driver):

        main_page = MainPage(driver)
        main_page.open_page(URLs.BASE_URL)
        main_page.click_yandex_button()  # #

        main_page.switch_to_last_browser_tab()

        yandex_page = RedirectToYandex(driver)
        yandex_page.dzen_url()

        yandex_page.close_popup()
        assert yandex_page.dzen_url() == URLs.URL_DZEN
