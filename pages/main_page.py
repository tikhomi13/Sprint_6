import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.yandex_page import RedirectToYandex
from locators.main_page_locators import MainPageLocators
from locators.base_page_locators import BasePageLocators


@allure.step('Главная страница')
class MainPage(BasePage):

    @allure.step('Метод выбора кнопок "Заказать" для параметризованного теста')
    def click_order_button(self, button):

        if button == MainPageLocators.ORDER_BUTTON_2_AT_THE_BOTTOM:

            element_to_scroll = self.find_element_located(MainPageLocators.RENT_TIME_IS_FINISHING, 8)
            self.driver.execute_script("arguments[0]. scrollIntoView();", element_to_scroll)

            order_button = self.find_element_located(button)
            order_button.click()

        else:

            order_button = self.find_element_located(button)
            order_button.click()

    @allure.step('Метод скролла до видимости кнопки Заказать, расположенной на главной странице')
    def scroll_to_questions(self):

        element_to_scroll = self.driver.find_element(*MainPageLocators.IMPORTANT_QUESTIONS)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(element_to_scroll))

        self.driver.execute_script("arguments[0]. scrollIntoView();", element_to_scroll)

    @allure.step('Метод выбора вопросов для параметризованного теста')
    def select_questions(self, question, answer):          # метод для параметризации

        question_select = self.wait_and_find_element(question)
        question_select.click()

        answer_select = self.wait_and_find_element(answer)
        return answer_select.text

    @allure.step('Уникальный элемент главной страницы - надпись Самокат на пару дней')
    def slogan_on_main_page(self):

        return self.wait_and_find_element(MainPageLocators.MAIN_PAGE_SLOGAN)

    @allure.step("Кнопка редиректа в dzen в хедере слева")
    def click_yandex_button(self):

        yandex_button = self.find_element_located(BasePageLocators.LINK_TO_DZEN)
        yandex_button.click()

        return RedirectToYandex(self.driver)

    def close_cookie_popup(self):

        cookie_accept = self.find_element_located(BasePageLocators.COOKIE_WINDOW)
        cookie_accept.click()
