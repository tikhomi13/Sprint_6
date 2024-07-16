import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from pages.base_page import BasePage

from locators import Locators


class RedirectToYandex(BasePage):

    def close_popup(self):

        close_popup = self.wait_and_find_element(Locators.CLOSE_POPUP) #

        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(Locators.CLOSE_POPUP))
        close_popup.click()

    def logo_main(self):

        logo = self.wait_and_find_element(Locators.LOGO_YA)
        return logo

    def dzen_url(self):

       # self.driver.set_script_timeout(4)
        url = self.driver.current_url

        self.wait_and_find_element(Locators.LOGO_YA)
        return url
