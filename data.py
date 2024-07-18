# Здесь тестовые данные

# from selenium.webdriver.common.by import By

class URLs:

    BASE_URL = "https://qa-scooter.praktikum-services.ru/"

    OPEN_SCOOTER_ORDER_PAGE = "https://qa-scooter.praktikum-services.ru/order"

    URL_DZEN = 'https://dzen.ru/?yredirect=true'

class Contents:

    FIRSTNAME = 'Платон'

    LASTNAME = 'Тихомиров'

    ADDRESS = 'Красногорск'

    PHONE = '+79060837008'

    ADD_COMMENT = 'Комментарий_Курьеруъ Comment_111'  # send keys

    FIRSTNAME_2 = 'Константин'

    LASTNAME_2 = 'Швец'

    ADDRESS_2 = 'Балашиха'

    PHONE_2 = '+79295062814'

    ADD_COMMENT_2 = ' '

class QuestionsAnswers:

    ANSWER_ONE_TEXT = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    ANSWER_TWO_TEXT = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    ANSWER_THREE_TEXT = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

    ANSWER_FOUR_TEXT = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    ANSWER_FIVE_TEXT = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

    ANSWER_SIX_TEXT = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

    ANSWER_SEVEN_TEXT = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    ANSWER_EIGHT_TEXT = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

    # Здесь тот же текст, но для assert'a в параметризованном тесте, так как текст выше задейстстован в локаторах параметризованного теста
    # Как результат - в случае несоответствия ОР и ФР выводится не assertion error, а timeout exception, так как перед сравнением ОР и ФР метод ищет
    # элемент с тем же самым текстом (см ANSWER_1, ANSWER_2) Итд.
    # Единственный найденный способ вынести хардкод из самого теста - написать здесь копии переменных, которые нигде не задействованы
    # Если есть еще какой-то вариант, избегающий дублирование переменных в этом файле - исправлю

    ANSWER_1_FOR_ASSERT = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    ANSWER_2_FOR_ASSERT = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    ANSWER_3_FOR_ASSERT = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

    ANSWER_4_FOR_ASSERT = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    ANSWER_5_FOR_ASSERT = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

    ANSWER_6_FOR_ASSERT = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

    ANSWER_7_FOR_ASSERT = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    ANSWER_8_FOR_ASSERT = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
