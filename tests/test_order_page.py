import time

import allure
from pages.order_page import OrderPage
from pages.base_page import BasePage
from pages.main_page import MainPage  # [хм хм]
from data import Contents

from pages.yandex_page import RedirectToYandex

from data import URLs


@allure.title('Класс на заполнение анкеты')
@allure.description('Первый набор данных')  # как реализовать второй? Нужна ли здесь параметризация?
class TestOrderPage:

    def test_fill_for_whom_page(self, driver):

        order_page_1 = OrderPage(driver)
        order_page_1.open_page(URLs.OPEN_SCOOTER_ORDER_PAGE)
        order_page_1.fill_for_whom_page(Contents.FIRSTNAME, Contents.LASTNAME, Contents.ADDRESS, Contents.PHONE)

        go_to_next_page = order_page_1.click_next_to_the_second_page()
        go_to_next_page.get_header_2()                                     # подхватываем элемент, расположенный на новой странице
        assert go_to_next_page.get_header_2().is_displayed()


    def test_when_to_deliver_scooter(self, driver, order_page_1_filled):

        order_page_2 = OrderPage(driver)
        order_page_2.fill_about_rent_page(Contents.ADD_COMMENT)
        order_page_2.order_and_confirm()

        go_to_next_page_ordered_page = order_page_2.go_to_show_status_page()
        go_to_next_page_ordered_page.get_cancel_button()

        assert go_to_next_page_ordered_page.get_cancel_button().is_displayed()




    @allure.title('Переход на главную страницу со страницы созданного заказа')  # не треба
    @allure.description('Переход на главную с помощью кнопки Самокат. Для заполнения обеих страниц анкеты использована фикстура order_page_2_filled')
    @allure.link(URLs.BASE_URL, name='Тестовая ссылка')
    def test_go_to_main_from_order(self, driver, order_page_2_filled):

        back_to_main = BasePage(driver)
        back_to_main.click_samokat_button()

        main_screen = MainPage(driver)
        assert main_screen.slogan_on_main_page().is_displayed()


# второй набор?


# Проверяем весь флоу

    def test_place_an_order(self, driver):

        order_page = OrderPage(driver)
        order_page.open_page(URLs.OPEN_SCOOTER_ORDER_PAGE)
        order_page.fill_for_whom_page(Contents.FIRSTNAME, Contents.LASTNAME, Contents.ADDRESS, Contents.PHONE)

        order_page.click_next_to_the_second_page()
        order_page.fill_about_rent_page(Contents.ADD_COMMENT)
        order_page.order_and_confirm()

        go_to_next_page_ordered_page = order_page.go_to_show_status_page() # подхват
        go_to_next_page_ordered_page.get_cancel_button()
        time.sleep(5)

        assert go_to_next_page_ordered_page.get_cancel_button().is_displayed()




    @allure.title('Переход на главную страницу со страницы созданного заказа')  # не треба
    @allure.description('Переход на главную с помощью кнопки Самокат. Для заполнения обеих страниц анкеты использована фикстура order_page_2_filled') # поправить имя
    @allure.link(URLs.BASE_URL, name='Тестовая ссылка')
    def test_go_to_main_from_order(self, driver, order_page_2_filled): # объединить фикстуру

        back_to_main = BasePage(driver)
        back_to_main.click_samokat_button()

        main_screen = MainPage(driver)
        assert main_screen.slogan_on_main_page().is_displayed()


    def test_go_to_dzen(self, driver):

        main_page = MainPage(driver)
        main_page.open_page(URLs.BASE_URL)
        main_page.click_yandex_button() ##

        main_page.switch_to_last_browser_tab()

        yandex_page = RedirectToYandex(driver)
        yandex_page.dzen_url()

        yandex_page.close_popup()
        assert yandex_page.dzen_url() == URLs.URL_DZEN




