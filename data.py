# Здесь тестовые данные

from selenium.webdriver.common.by import By

class URLs:

    OPEN_SCOOTER = "https://qa-scooter.praktikum-services.ru/"

    OPEN_SCOOTER_ORDER_PAGE = "https://qa-scooter.praktikum-services.ru/order"

    # сюда вставляемые значения

class Contents:

    FIRSTNAME = 'Платон'

    LASTNAME = 'Тихомиров'

    ADDRESS = 'Красногорск'

    PHONE = '+79060837008'

    ADD_COMMENT = 'Комментарий_Курьеруъ Comment_111'  # send keys






    SHOW_ORDER_STATUS_BUTTON = (By.XPATH, ".//button[(text()='Посмотреть статус')]")

    CANCEL_ORDER = (By.XPATH, ".//button[(text()='Отменить заказ')]")













