import pytest
from locators.main_page_locators import MainPageLocators
import allure
from pages.main_page import MainPage
from data import URLs
from data import QuestionsAnswers


class TestMainPage:

    data = [

        [MainPageLocators.QUESTION_1, MainPageLocators.ANSWER_1, QuestionsAnswers.ANSWER_1_FOR_ASSERT],
        [MainPageLocators.QUESTION_2, MainPageLocators.ANSWER_2, QuestionsAnswers.ANSWER_2_FOR_ASSERT],
        [MainPageLocators.QUESTION_3, MainPageLocators.ANSWER_3, QuestionsAnswers.ANSWER_3_FOR_ASSERT],
        [MainPageLocators.QUESTION_4, MainPageLocators.ANSWER_4, QuestionsAnswers.ANSWER_4_FOR_ASSERT],
        [MainPageLocators.QUESTION_5, MainPageLocators.ANSWER_5, QuestionsAnswers.ANSWER_5_FOR_ASSERT],
        [MainPageLocators.QUESTION_6, MainPageLocators.ANSWER_6, QuestionsAnswers.ANSWER_6_FOR_ASSERT],
        [MainPageLocators.QUESTION_7, MainPageLocators.ANSWER_7, QuestionsAnswers.ANSWER_7_FOR_ASSERT],
        [MainPageLocators.QUESTION_8, MainPageLocators.ANSWER_8, QuestionsAnswers.ANSWER_8_FOR_ASSERT]
    ]

    @allure.description("Параметризованный тест для проверки ответов на восемь вопросов, расположеннных внизу гл. стр")
    @pytest.mark.parametrize('question,answer,text', data)
    def test_check_questions(self, driver, question, answer, text):
        open_main_page = MainPage(driver)
        open_main_page.open_page(URLs.BASE_URL)
        open_main_page.scroll_to_questions()

        text_to_be_displayed = open_main_page.select_questions(question, answer)
        assert text_to_be_displayed == text
