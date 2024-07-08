import allure
from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.base_page import BasePage
#from pages.order_page_2 import OrderPageTwo


class RedirectToYandex(BasePage):

   # CLOSE_POPUP = (By.XPATH, ".//div[8]//span[contains(@class, 'pc94cd50a')]/*")

    # CLOSE_POPUP = (By.XPATH, ".//div[8]//span[contains(@class, 'i8b')]//*[local-name()='svg']")
    CLOSE_POPUP = (By.XPATH, "/html/body/div[8]/div/div[1]/div/div[3]/div/div[1]/div/div/div/div/span")

    LOGO_YA = (By.XPATH, ".//div/header/div[contains(@class, 'desktop-base-header')]/a")



    def close_popup(self):

        close_popup = self.wait_and_find_element(self.CLOSE_POPUP) # спросить как найти svg
        close_popup.click()

    def logo_main(self):

        logo = self.wait_and_find_element(self.LOGO_YA)
        return logo








   # def check_element_yandex(self):

