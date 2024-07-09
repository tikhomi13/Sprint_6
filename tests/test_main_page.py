import time

import allure
from pages.main_page import MainPage
from pages.base_page import BasePage
from data import URLs
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

        assert open_main_page.select_question_1() == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'


    def test_select_question_2(self, driver):

        open_main_page = MainPage(driver)
        open_main_page.open_page(URLs.OPEN_SCOOTER)

        open_main_page.scroll_to_questions()
        open_main_page.select_question_2()

        assert open_main_page.select_question_2().text == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'


    def test_select_question_3(self, driver):

        open_main_page = MainPage(driver)
        open_main_page.open_page(URLs.OPEN_SCOOTER)

        open_main_page.scroll_to_questions()
        open_main_page.select_question_3()

        assert open_main_page.select_question_3().text == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'


    def test_select_question_4(self, driver):
        open_main_page = MainPage(driver)
        open_main_page.open_page(URLs.OPEN_SCOOTER)

        open_main_page.scroll_to_questions()
        open_main_page.select_question_4()

        assert open_main_page.select_question_4().text == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    def test_select_question_5(self, driver):
        open_main_page = MainPage(driver)
        open_main_page.open_page(URLs.OPEN_SCOOTER)

        open_main_page.scroll_to_questions()
        open_main_page.select_question_5()

        assert open_main_page.select_question_5().text == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

    def test_select_question_6(self, driver):
        open_main_page = MainPage(driver)
        open_main_page.open_page(URLs.OPEN_SCOOTER)

        open_main_page.scroll_to_questions()
        open_main_page.select_question_6()

        assert open_main_page.select_question_6().text == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

    def test_select_question_7(self, driver):
        open_main_page = MainPage(driver)
        open_main_page.open_page(URLs.OPEN_SCOOTER)

        open_main_page.scroll_to_questions()
        open_main_page.select_question_7()

        assert open_main_page.select_question_7().text == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    def test_select_question_8(self, driver):
        open_main_page = MainPage(driver)
        open_main_page.open_page(URLs.OPEN_SCOOTER)

        open_main_page.scroll_to_questions()
        open_main_page.select_question_8()

        assert open_main_page.select_question_8().text == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'


        # не совсем понял, как здесь применить параметризацию
