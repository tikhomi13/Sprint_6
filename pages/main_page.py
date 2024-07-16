import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

import data
from pages.base_page import BasePage
from pages.order_page_1 import OrderPageOne
from pages.yandex_page import RedirectToYandex
from locators import Locators

from data import URLs
from data import QuestionsAnswers
import time

@allure.step('Главная страница')
class MainPage(BasePage):

    @allure.step('Метод клика по кнопке Заказать, расположенной в хедере')
    def click_order_button_one(self): #### вот тут !!!!!!!!!!! правильный вариант - перенести выше

        order_button_1 = self.wait_and_find_element(Locators.ORDER_BUTTON_1_AT_THE_TOP)   # problem Была изза звезды
        order_button_1.click()

        return OrderPageOne(self.driver)   # Выполняется переход на другую стр

    @allure.step('Метод клика по кнопке Заказать, расположенной на главной странице ниже')
    def click_order_button_two(self):

        element_to_scroll = self.wait_and_find_element(Locators.RENT_TIME_IS_FINISHING)
        self.driver.execute_script("arguments[0]. scrollIntoView();", element_to_scroll)

        order_button_2 = self.driver.find_element(*Locators.ORDER_BUTTON_2_AT_THE_BOTTOM)
        order_button_2.click()

        return OrderPageOne(self.driver)

    @allure.step('Метод скролла до видимости кнопки Заказать, расположенной на главной странице')
    def scroll_to_questions(self):

        element_to_scroll = self.driver.find_element(*Locators.IMPORTANT_QUESTIONS)
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(element_to_scroll))

        self.driver.execute_script("arguments[0]. scrollIntoView();", element_to_scroll)


    def select_questions(self, question):

        question_select = self.wait_and_find_element(question)
        question_select.click()

        return question_select.text   ####



    def choose_answer(self, answer):

        answer_select = self.wait_and_find_element(answer)
        return answer_select.text





    @allure.step('Далее селекты вопросов внизу страницы')
    def select_question_1(self):

        question_1_select = self.wait_and_find_element(Locators.QUESTION_1)
        question_1_select.click()

        answer_text = Locators.ANSWER_1
        return self.driver.find_element(*answer_text).text

    def select_question_2(self):

        question_2_select = self.wait_and_find_element(Locators.QUESTION_2)
        question_2_select.click()

        answer_text = Locators.ANSWER_2
        return self.driver.find_element(*answer_text)

    def select_question_3(self):

        question_3_select = self.wait_and_find_element(Locators.QUESTION_3)
        question_3_select.click()

        answer_text = Locators.ANSWER_3
        return self.driver.find_element(*answer_text)

    def select_question_4(self):

        question_4_select = self.wait_and_find_element(Locators.QUESTION_4)
        question_4_select.click()

        answer_text = Locators.ANSWER_4
        return self.driver.find_element(*answer_text)

    def select_question_5(self):

        question_5_select = self.wait_and_find_element(Locators.QUESTION_5)
        question_5_select.click()

        answer_text = Locators.ANSWER_5
        return self.driver.find_element(*answer_text)

    def select_question_6(self):

        question_6_select = self.wait_and_find_element(Locators.QUESTION_6)
        question_6_select.click()

        answer_text = Locators.ANSWER_6
        return self.driver.find_element(*answer_text)

    def select_question_7(self):

        question_7_select = self.wait_and_find_element(Locators.QUESTION_7)
        question_7_select.click()

        answer_text = Locators.ANSWER_7
        return self.driver.find_element(*answer_text)

    def select_question_8(self):

        question_8_select = self.wait_and_find_element(Locators.QUESTION_8)
        question_8_select.click()

        answer_text = Locators.ANSWER_8
        return self.driver.find_element(*answer_text)


    @allure.step('Уникальный элемент главной страницы - надпись Самокат на пару дней')
    def slogan_on_main_page(self):

        return self.wait_and_find_element(Locators.MAIN_PAGE_SLOGAN)

    #LINK_TO_DZEN = (By.XPATH, "//div/a[(@class='Header_LogoYandex__3TSOI' and @href='//yandex.ru')]")


    @allure.step("Кнопка редиректа в dzen в хедере слева")
    def click_yandex_button(self):

        yandex_button = self.wait_and_find_element(Locators.LINK_TO_DZEN)
        yandex_button.click()

       # self.driver.set_script_timeout(4)

        return RedirectToYandex(self.driver)


