import allure
from pages.order_page_2 import OrderPageTwo  #убрать
from pages.ordered_page import OrderedPage
from pages.base_page import BasePage
from pages.main_page import MainPage  # [хм хм]
from pages.yandex_page import RedirectToYandex
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

import time
from data import URLs
from data import Contents


from pages.order_page_1 import OrderPageOne
import time
from data import URLs

class TestOrderedPage:

    @allure.title('Переход на главную страницу со страницы созданного заказа')
    @allure.description('Переход на главную с помощью кнопки Самокат. Для заполнения обеих страниц анкеты использована фикстура order_page_2_filled')
    @allure.link(URLs.OPEN_SCOOTER, name='Тестовая ссылка')
    def test_go_to_main_from_order(self, driver, order_page_2_filled):

        back_to_main = BasePage(driver)
        back_to_main.click_samokat_button()

        main_screen = MainPage(driver)
        assert main_screen.slogan_on_main_page().is_displayed()

        # тут еще добавить тест на дзен

    def test_go_to_dzen(self):

        #driver.get('https://dzen.ru/')
        #time.sleep(4)

        firefox_driver = webdriver.Firefox()
        firefox_driver.maximize_window()

        yield firefox_driver
        firefox_driver.quit()

        main_page = MainPage    # (driver)
        main_page.open_page(URLs.OPEN_SCOOTER)
        main_page.click_yandex_button()

        assert WebDriverWait(firefox_driver, 4).until(expected_conditions.url_changes('https://dzen.ru/?yredirect=true'))


        #assert yandex.



        time.sleep(4)

        driver.find_element(By.XPATH, "//*[@id='LayoutContentMicroRoot']/div/div/div/div[1]/div[1]/div/article/div[2]/ul/li[2]/a/div[2]/span").click()



        #driver.find_element(By.XPATH, "/html/body/div[8]/div/div[1]/div/div[3]/div/div[1]/div/div/div/div/span").click()

        #element = driver.find_element(By.XPATH, "//*[@id='LayoutContentMicroRoot']/div/div/div/div[1]/div[1]/div/article/div[2]/ul/li[2]/a/div[2]/span")
        #time.sleep(2)

        #main_page = MainPage(driver)
        #main_page.open_page(URLs.OPEN_SCOOTER)

        #main_page.click_yandex_button()
        #time.sleep(4)

        #element = driver.find_element(By.XPATH, "//*[@id='LayoutContentMicroRoot']/div/div/div/div[1]/div[1]/div/article/div[2]/ul/li[2]/a/div[2]/span")
        #time.sleep(2)

        #element.click()


       # dzen = RedirectToYandex(driver)
       # dzen.close_popup() #метод

       # to_dzen.close_popup() #метод
        time.sleep(4)

        #to_dzen.close_popup()




        #time.sleep(4)

       # assert to_dzen.logo_main().is_displayed()





