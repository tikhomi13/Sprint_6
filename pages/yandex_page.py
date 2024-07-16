import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from pages.base_page import BasePage


class RedirectToYandex(BasePage):

    # CLOSE_POPUP = (By.XPATH, ".//div[8]//span[contains(@class, 'i8b')]//*[local-name()='svg']") устарело (?)

    CLOSE_POPUP = (By.XPATH, ".//div[8]//span[contains(@class, 'b99')]//*[local-name()='svg']")


    LOGO_YA = (By.XPATH, ".//div/header/div[contains(@class, 'desktop-base-header')]/a")

    DZEN_URL = 'https://dzen.ru/?yredirect=true'


    def close_popup(self):

        close_popup = self.wait_and_find_element(self.CLOSE_POPUP) #

        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.CLOSE_POPUP))
        close_popup.click()

    def logo_main(self):

        logo = self.wait_and_find_element(self.LOGO_YA)
        return logo

    def dzen_url(self):

       # self.driver.set_script_timeout(4)
        url = self.driver.current_url

        self.wait_and_find_element(self.LOGO_YA)
        return url



