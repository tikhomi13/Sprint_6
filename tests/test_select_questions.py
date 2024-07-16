import pytest
from selenium import webdriver
from data import URLs
from data import QuestionsAnswers

from pages.main_page import MainPage

from locators import Locators

class TestMainPage:

    @pytest.mark.parametrize('question,answer', [

        [Locators.QUESTION_1, Locators.ANSWER_1],
        [Locators.QUESTION_2, Locators.ANSWER_2],
        [Locators.QUESTION_3, Locators.ANSWER_3],
        [Locators.QUESTION_4, Locators.ANSWER_4],
        [Locators.QUESTION_5, Locators.ANSWER_5],
        [Locators.QUESTION_6, Locators.ANSWER_6],
        [Locators.QUESTION_7, Locators.ANSWER_7],
        [Locators.QUESTION_8, Locators.ANSWER_8]
        ]
    )

    def test_choosing_questions(self, driver, question, answer):

        open_main_page = MainPage(driver)
        open_main_page.open_page(URLs.OPEN_SCOOTER)
        open_main_page.scroll_to_questions()

        open_main_page.select_questions(question)

        #open_main_page.question

        assert open_main_page.select_questions(question).text == open_main_page.choose_answer(answer)

