import allure
from pages.order_page_1 import OrderPageOne
from data import URLs
from data import Contents


@allure.title('Класс на заполнение первой страницы анкеты')
@allure.description('Первый набор данных')  # как реализовать второй? Нужна ли здесь параметризация?
class TestOrderPageOne:

    def test_fill_for_whom_page(self, driver):

        order_page_1 = OrderPageOne(driver)
        order_page_1.open_page(URLs.OPEN_SCOOTER_ORDER_PAGE)
        order_page_1.fill_for_whom_page(Contents.FIRSTNAME, Contents.LASTNAME, Contents.ADDRESS, Contents.PHONE)

        go_to_next_page = order_page_1.click_next_to_the_second_page()
        go_to_next_page.get_header_2()                                     # подхватываем элемент, расположенный на новой странице
        assert go_to_next_page.get_header_2().is_displayed()

# второй набор?


# Проверить весь флоу



