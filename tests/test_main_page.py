import allure
from pages.main_page import MainPage
from pages.base_page import BasePage
from data import URLs

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

