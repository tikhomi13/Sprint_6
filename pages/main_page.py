import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.order_page_1 import OrderPageOne
from pages.yandex_page import RedirectToYandex
import time

@allure.step('Главная страница')
class MainPage(BasePage):
    # Здесь - page object. Локаторы, методы

    #ORDER_BUTTON_1_AT_THE_TOP = (By.XPATH, ".//div/button[@class='Button_Button__ra12g' and (text()='Заказать')]") # перенос в BasePage

    ORDER_BUTTON_2_AT_THE_BOTTOM = (By.XPATH, ".//div/button[@class='Button_Button__ra12g Button_Middle__1CSJM' and (text()='Заказать')]")

    IMPORTANT_QUESTIONS = (By.XPATH, ".//div[@class='Home_SubHeader__zwi_E' and (text()='Вопросы о важном')]")

    RENT_TIME_IS_FINISHING = (By.XPATH, ".//div[(text()='Когда аренда заканчивается')]")

    MAIN_PAGE_SLOGAN = (By.XPATH, ".//div[@class='Home_Header__iJKdX']")



    QUESTION_1_TO_SELECT = (By.XPATH, ".//div[@class='accordion']//div[@id='accordion__heading-0']")

    QUESTION_1_SELECTED = (By.XPATH, ".//p[contains(text(), '400 рублей')]")

    QUESTION_2_TO_SELECT = (By.XPATH, ".//div[@class='accordion']//div[@id='accordion__heading-1']")

    QUESTION_2_SELECTED = (By.XPATH, ".//p[contains(text(), 'один заказ — один самокат')]")

    QUESTION_3_TO_SELECT = (By.XPATH, ".//div[@class='accordion']//div[@id='accordion__heading-2']")

    QUESTION_3_SELECTED = (By.XPATH, ".//p[contains(text(), '9 мая')]")

    QUESTION_4_TO_SELECT = (By.XPATH, ".//div[@class='accordion']//div[@id='accordion__heading-3']")

    QUESTION_4_SELECTED = (By.XPATH, ".//p[contains(text(), 'с завтрашнего дня')]")

    QUESTION_5_TO_SELECT = (By.XPATH, ".//div[@class='accordion']//div[@id='accordion__heading-4']")

    QUESTION_5_SELECTED = (By.XPATH, ".//p[contains(text(), 'номеру 1010')]")

    QUESTION_6_TO_SELECT = (By.XPATH, ".//div[@class='accordion']//div[@id='accordion__heading-5']")

    QUESTION_6_SELECTED = (By.XPATH, ".//p[contains(text(), 'Зарядка не понадобится')]")

    QUESTION_7_TO_SELECT = (By.XPATH, ".//div[@class='accordion']//div[@id='accordion__heading-6']")

    QUESTION_7_SELECTED = (By.XPATH, ".//p[contains(text(), 'Штрафа не будет')]")

    QUESTION_8_TO_SELECT = (By.XPATH, ".//div[@class='accordion']//div[@id='accordion__heading-7']")

    QUESTION_8_SELECTED = (By.XPATH, ".//p[contains(text(), 'Всем самокатов')]")

    @allure.step('Метод клика по кнопке Заказать, расположенной в хедере')
    def click_order_button_one(self): #### вот тут !!!!!!!!!!! правильный вариант - перенести выше

        order_button_1 = self.wait_and_find_element(self.ORDER_BUTTON_1_AT_THE_TOP)   # problem Была изза звезды
        order_button_1.click()

        return OrderPageOne(self.driver)   # Выполняется переход на другую стр

    @allure.step('Метод клика по кнопке Заказать, расположенной на главной странице ниже')
    def click_order_button_two(self):

        element_to_scroll = self.wait_and_find_element(self.RENT_TIME_IS_FINISHING)
        self.driver.execute_script("arguments[0]. scrollIntoView();", element_to_scroll)

        order_button_2 = self.driver.find_element(*self.ORDER_BUTTON_2_AT_THE_BOTTOM)
        order_button_2.click()

        return OrderPageOne(self.driver)

    @allure.step('Метод скролла до видимости кнопки Заказать, расположенной на главной странице')
    def scroll_to_page_bottom(self):

        element_to_scroll = self.driver.find_element(self.IMPORTANT_QUESTIONS)
        self.driver.execute_script("arguments[0]. scrollIntoView();", element_to_scroll)

    @allure.step('Далее селекты вопросов внизу страницы')
    def select_question_1(self):

        question_1_select = self.driver.find_element(*self.QUESTION_1_TO_SELECT)
        question_1_select.click()

    def select_question_2(self):

        question_2_select = self.wait_and_find_element(self.QUESTION_2_TO_SELECT)
        question_2_select.click()

    def select_question_3(self):

        question_3_select = self.wait_and_find_element(self.QUESTION_3_TO_SELECT)
        question_3_select.click()

    def select_question_4(self):

        question_4_select = self.wait_and_find_element(self.QUESTION_4_TO_SELECT)
        question_4_select.click()

    def select_question_5(self):

        question_5_select = self.wait_and_find_element(self.QUESTION_5_TO_SELECT)
        question_5_select.click()

    def select_question_6(self):

        question_6_select = self.wait_and_find_element(self.QUESTION_6_TO_SELECT)
        question_6_select.click()

    def select_question_7(self):

        question_7_select = self.wait_and_find_element(self.QUESTION_7_TO_SELECT)
        question_7_select.click()

    def select_question_8(self):

        question_8_select = self.wait_and_find_element(self.QUESTION_8_TO_SELECT)
        question_8_select.click()

    @allure.step('Уникальный элемент главной страницы - надпись Самокат на пару дней')
    def slogan_on_main_page(self):

        return self.wait_and_find_element(self.MAIN_PAGE_SLOGAN)

    LINK_TO_DZEN = (By.XPATH, "//div/a[(@class='Header_LogoYandex__3TSOI' and @href='//yandex.ru')]")


    @allure.step("Кнопка редиректа в dzen в хедере слева")
    def click_yandex_button(self):

        yandex_button = self.wait_and_find_element(self.LINK_TO_DZEN)
        yandex_button.click()

        return RedirectToYandex(self.driver)

    #CLOSE_POPUP = (By.XPATH, ".//div[8]//span[contains(@class, 'pc94cd50a')]")

    #def close_popup(self):

      #  close_popup = self.wait_and_find_element(self.CLOSE_POPUP) # спросить как найти svg
      #  close_popup.click()







