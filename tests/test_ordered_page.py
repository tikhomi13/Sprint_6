import allure
from pages.base_page import BasePage
from pages.main_page import MainPage  # [хм хм]
from pages.yandex_page import RedirectToYandex

from data import URLs

class TestOrderedPage:

    @allure.title('Переход на главную страницу со страницы созданного заказа')  # не треба
    @allure.description('Переход на главную с помощью кнопки Самокат. Для заполнения обеих страниц анкеты использована фикстура order_page_2_filled')
    @allure.link(URLs.BASE_URL, name='Тестовая ссылка')
    def test_go_to_main_from_order(self, driver, order_page_2_filled):

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

