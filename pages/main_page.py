import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from pages.base_page import BasePage
from pages.order_page import OrderPage
from pages.yandex_page import RedirectToYandex
from locators import Locators


@allure.step('Главная страница')
class MainPage(BasePage):

    @allure.step('Метод выбора кнопок "Заказать" для параметризованного теста')
    def click_order_button(self, button):

        if button == Locators.ORDER_BUTTON_2_AT_THE_BOTTOM:

            element_to_scroll = self.wait_and_find_element(Locators.RENT_TIME_IS_FINISHING)
            self.driver.execute_script("arguments[0]. scrollIntoView();", element_to_scroll)

            order_button = self.wait_and_find_element(button)
            order_button.click()

        else:

            order_button = self.wait_and_find_element(button)
            order_button.click()


    @allure.step('Метод скролла до видимости кнопки Заказать, расположенной на главной странице')
    def scroll_to_questions(self):

        element_to_scroll = self.driver.find_element(*Locators.IMPORTANT_QUESTIONS)
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(element_to_scroll))

        self.driver.execute_script("arguments[0]. scrollIntoView();", element_to_scroll)

    @allure.step('Метод выбора вопросов для параметризованного теста')
    def select_questions(self, question, answer):          # метод для параметризации

        question_select = self.wait_and_find_element(question)
        question_select.click()

        answer_select = self.wait_and_find_element(answer)
        return answer_select.text

    @allure.step('Уникальный элемент главной страницы - надпись Самокат на пару дней')
    def slogan_on_main_page(self):

        return self.wait_and_find_element(Locators.MAIN_PAGE_SLOGAN)


    @allure.step("Кнопка редиректа в dzen в хедере слева")
    def click_yandex_button(self):

        yandex_button = self.find_element_located(Locators.LINK_TO_DZEN)
        yandex_button.click()

        return RedirectToYandex(self.driver)

    def close_cookie_popup(self):

        cookie_accept = self.find_element_located(Locators.COOKIE_WINDOW)
        cookie_accept.click()
