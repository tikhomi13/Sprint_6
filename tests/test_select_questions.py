import pytest
from selenium import webdriver
from data import URLs
from data import QuestionsAnswers

from pages.main_page import MainPage

from locators import Locators

class TestMainPage:

    @pytest.mark.parametrize('question,answer,text', [

        [Locators.QUESTION_1, Locators.ANSWER_1, QuestionsAnswers.ANSWER_ONE_TEXT],
        [Locators.QUESTION_2, Locators.ANSWER_2, QuestionsAnswers.ANSWER_TWO_TEXT],
        [Locators.QUESTION_3, Locators.ANSWER_3, QuestionsAnswers.ANSWER_THREE_TEXT],
        [Locators.QUESTION_4, Locators.ANSWER_4, QuestionsAnswers.ANSWER_FOUR_TEXT],
        [Locators.QUESTION_5, Locators.ANSWER_5, QuestionsAnswers.ANSWER_FIVE_TEXT],
        [Locators.QUESTION_6, Locators.ANSWER_6, QuestionsAnswers.ANSWER_SIX_TEXT],
        [Locators.QUESTION_7, Locators.ANSWER_7, QuestionsAnswers.ANSWER_SEVEN_TEXT],
        [Locators.QUESTION_8, Locators.ANSWER_8, QuestionsAnswers.ANSWER_EIGHT_TEXT]
        ]
    )

    def test_choosing_questions(self, driver, question, answer, text):

        open_main_page = MainPage(driver)
        open_main_page.open_page(URLs.OPEN_SCOOTER)
        open_main_page.scroll_to_questions()

        expected_text = open_main_page.select_questions(question, answer)
        assert expected_text == text