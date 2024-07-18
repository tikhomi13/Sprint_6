from pages.base_page import BasePage
from locators.yandex_page_locators import YandexPageLocators
import allure


class RedirectToYandex(BasePage):

    @allure.title("Метод для закрытия всплывающего окна с рекламой браузера на главной Дзена")

    def close_popup(self):

        self.wait_and_find_element(YandexPageLocators.CLOSE_POPUP).click()
    @allure.title("Метод возвращает URL яндекс дзена после редиректа на сайт")
    def dzen_url(self):

        url = self.driver.current_url
        self.find_element_located(YandexPageLocators.LOGO_YA, 10)
        return url
