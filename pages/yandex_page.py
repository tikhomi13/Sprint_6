import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from pages.base_page import BasePage

from locators import Locators


class RedirectToYandex(BasePage):

    def close_popup(self):

        self.wait_and_find_element(Locators.CLOSE_POPUP).click()

    def dzen_url(self):

        url = self.driver.current_url
        self.find_element_located(Locators.LOGO_YA, 10)
        return url
