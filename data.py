# Здесь тестовые данные

from selenium.webdriver.common.by import By

class URLs:

    OPEN_SCOOTER = "https://qa-scooter.praktikum-services.ru/"

    OPEN_SCOOTER_ORDER_PAGE = "https://qa-scooter.praktikum-services.ru/order"

    URL_DZEN = 'https://dzen.ru/?yredirect=true'

    # сюда вставляемые значения

class Contents:

    FIRSTNAME = 'Платон'

    LASTNAME = 'Тихомиров'

    ADDRESS = 'Красногорск'

    PHONE = '+79060837008'

    ADD_COMMENT = 'Комментарий_Курьеруъ Comment_111'  # send keys

    SHOW_ORDER_STATUS_BUTTON = (By.XPATH, ".//button[(text()='Посмотреть статус')]")

    CANCEL_ORDER = (By.XPATH, ".//button[(text()='Отменить заказ')]")

class QuestionsAnswers:

    ANSWER_ONE_TEXT = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    ANSWER_TWO_TEXT = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    ANSWER_THREE_TEXT = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

    ANSWER_FOUR_TEXT = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    ANSWER_FIVE_TEXT = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

    ANSWER_SIX_TEXT = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

    ANSWER_SEVEN_TEXT = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    ANSWER_EIGHT_TEXT = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

















