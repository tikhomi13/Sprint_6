from pages.base_page import BasePage
from locators.yandex_page_locators import YandexPageLocators


class RedirectToYandex(BasePage):

    def close_popup(self):

        self.wait_and_find_element(YandexPageLocators.CLOSE_POPUP).click()

    def dzen_url(self):

        url = self.driver.current_url
        self.find_element_located(YandexPageLocators.LOGO_YA, 10)
        return url
