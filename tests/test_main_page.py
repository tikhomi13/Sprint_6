import time

import pytest

from locators import Locators

import allure
from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.order_page_1 import OrderPageOne
from data import URLs
from data import QuestionsAnswers
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestMainPage:

    @allure.title('Параметризованный тест на клик по двум кнопкам "Заказать"')
    @allure.description('Одна расположена в хедере справа, вторая - в нижней части главной страницы')
    @pytest.mark.parametrize('button', [Locators.ORDER_BUTTON_1_AT_THE_TOP, Locators.ORDER_BUTTON_2_AT_THE_BOTTOM])
    def test_use_order_buttons(self, driver, button):

        open_main_page = MainPage(driver)
        open_main_page.open_page(URLs.BASE_URL)
        open_main_page.click_order_button(button)

        go_to_order_page = OrderPageOne(driver)

        assert go_to_order_page.get_header_1().is_displayed()










    class TestMainPage:
        data = [

            [Locators.QUESTION_1, Locators.ANSWER_1, QuestionsAnswers.ANSWER_1_FOR_ASSERT],
            [Locators.QUESTION_2, Locators.ANSWER_2, QuestionsAnswers.ANSWER_2_FOR_ASSERT],
            [Locators.QUESTION_3, Locators.ANSWER_3, QuestionsAnswers.ANSWER_3_FOR_ASSERT],
            [Locators.QUESTION_4, Locators.ANSWER_4, QuestionsAnswers.ANSWER_4_FOR_ASSERT],
            [Locators.QUESTION_5, Locators.ANSWER_5, QuestionsAnswers.ANSWER_5_FOR_ASSERT],
            [Locators.QUESTION_6, Locators.ANSWER_6, QuestionsAnswers.ANSWER_6_FOR_ASSERT],
            [Locators.QUESTION_7, Locators.ANSWER_7, QuestionsAnswers.ANSWER_7_FOR_ASSERT],
            [Locators.QUESTION_8, Locators.ANSWER_8, QuestionsAnswers.ANSWER_8_FOR_ASSERT]
        ]

        @pytest.mark.parametrize('question,answer,text', data)  # добавляем data
        def test_choosing_questions(self, driver, question, answer, text):
            open_main_page = MainPage(driver)
            open_main_page.open_page(URLs.BASE_URL)
            open_main_page.scroll_to_questions()

            text_to_be_displayed = open_main_page.select_questions(question, answer)
            assert text_to_be_displayed == text




