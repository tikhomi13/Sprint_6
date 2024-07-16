import time

import allure
from pages.main_page import MainPage
from pages.base_page import BasePage
from data import URLs
from data import QuestionsAnswers
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestMainPage:

    @allure.title('Открыть форму заказа с помощью верхней кнопки "Заказать"')
    @allure.description('Форма заполняется открывается нажатием на кнопку заказа в хедере справа')
    def test_use_order_button_1(self, driver):                        # потом перенести открытие сайта в фикстуру
        open_main_page = MainPage(driver)                             # Автотест - образец
        open_main_page.open_page(URLs.OPEN_SCOOTER)                   # Открываем страницу через метод в Base_page

        go_to_order_page = open_main_page.click_order_button_one()    # Кликаем по кнопке # Заказать и используем метод перехода из main_page
        assert go_to_order_page.get_header_1().is_displayed()         # click_order_button_one() c ретерном следующей страницы (анкеты). Здесь переход
                                                                      # Проверяем отображение надписи на новой странице
    @allure.title('Открыть форму заказа с помощью нижней кнопки "Заказать"')
    @allure.description('Форма заполняется открывается нажатием на кнопку заказа, расположенную внизу на главной странице')
    def test_use_order_button_2(self, driver):

        open_main_page = MainPage(driver)
        open_main_page.open_page(URLs.OPEN_SCOOTER)

        go_to_order_page = open_main_page.click_order_button_two()   # возвращаем новую страницу
        assert go_to_order_page.get_header_1().is_displayed()        # как закрыть всплывающее окно с куки?


    def test_select_question_1(self, driver):
        open_main_page = MainPage(driver)
        open_main_page.open_page(URLs.OPEN_SCOOTER)  # Открыли стр

        open_main_page.scroll_to_questions()  # Прокрутили
        open_main_page.select_question_1()  # Выбрали вопрос


        assert open_main_page.select_question_1() == QuestionsAnswers.ANSWER_ONE_TEXT


    def test_select_question_2(self, driver):

        open_main_page = MainPage(driver)
        open_main_page.open_page(URLs.OPEN_SCOOTER)

        open_main_page.scroll_to_questions()
        open_main_page.select_question_2()

        assert open_main_page.select_question_2().text == QuestionsAnswers.ANSWER_TWO_TEXT


    def test_select_question_3(self, driver):

        open_main_page = MainPage(driver)
        open_main_page.open_page(URLs.OPEN_SCOOTER)

        open_main_page.scroll_to_questions()
        open_main_page.select_question_3()

        assert open_main_page.select_question_3().text == QuestionsAnswers.ANSWER_THREE_TEXT


    def test_select_question_4(self, driver):
        open_main_page = MainPage(driver)
        open_main_page.open_page(URLs.OPEN_SCOOTER)

        open_main_page.scroll_to_questions()
        open_main_page.select_question_4()

        assert open_main_page.select_question_4().text == QuestionsAnswers.ANSWER_FOUR_TEXT

    def test_select_question_5(self, driver):
        open_main_page = MainPage(driver)
        open_main_page.open_page(URLs.OPEN_SCOOTER)

        open_main_page.scroll_to_questions()
        open_main_page.select_question_5()

        assert open_main_page.select_question_5().text == QuestionsAnswers.ANSWER_FIVE_TEXT

    def test_select_question_6(self, driver):
        open_main_page = MainPage(driver)
        open_main_page.open_page(URLs.OPEN_SCOOTER)

        open_main_page.scroll_to_questions()
        open_main_page.select_question_6()

        assert open_main_page.select_question_6().text == QuestionsAnswers.ANSWER_SIX_TEXT

    def test_select_question_7(self, driver):
        open_main_page = MainPage(driver)
        open_main_page.open_page(URLs.OPEN_SCOOTER)

        open_main_page.scroll_to_questions()
        open_main_page.select_question_7()

        assert open_main_page.select_question_7().text == QuestionsAnswers.ANSWER_SEVEN_TEXT

    def test_select_question_8(self, driver):
        open_main_page = MainPage(driver)
        open_main_page.open_page(URLs.OPEN_SCOOTER)

        open_main_page.scroll_to_questions()
        open_main_page.select_question_8()

        assert open_main_page.select_question_8().text == QuestionsAnswers.ANSWER_EIGHT_TEXT


        # не совсем понял, как здесь применить параметризацию
