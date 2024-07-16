import allure
from pages.order_page_2 import OrderPageTwo  #убрать
from pages.ordered_page import OrderedPage
from pages.base_page import BasePage
from pages.main_page import MainPage  # [хм хм]
from pages.yandex_page import RedirectToYandex
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

import time
from data import URLs
from data import Contents


from pages.order_page_1 import OrderPageOne
import time
from data import URLs

class TestOrderedPage:

    @allure.title('Переход на главную страницу со страницы созданного заказа')  # не треба
    @allure.description('Переход на главную с помощью кнопки Самокат. Для заполнения обеих страниц анкеты использована фикстура order_page_2_filled')
    @allure.link(URLs.OPEN_SCOOTER, name='Тестовая ссылка')
    def test_go_to_main_from_order(self, driver, order_page_2_filled):

        back_to_main = BasePage(driver)
        back_to_main.click_samokat_button()

        main_screen = MainPage(driver)
        assert main_screen.slogan_on_main_page().is_displayed()

        # тут еще добавить тест на дзен

    def test_go_to_dzen(self, driver):

        main_page = MainPage(driver)
        main_page.open_page(URLs.OPEN_SCOOTER)
        window_before = driver.window_handles[0]
        main_page.click_yandex_button()

        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)

        yandex_page = RedirectToYandex(driver)
        yandex_page.dzen_url()

        assert yandex_page.dzen_url() == URLs.URL_DZEN

        yandex_page.close_popup()


# +  спросить как убрать вспл окно с куки на сайте самоката
