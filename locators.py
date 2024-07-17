from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from data import URLs
from data import QuestionsAnswers

import time


class Locators:

    # main_page

    QUESTION_1 = (By.ID, "accordion__heading-0")

    QUESTION_2 = (By.ID, "accordion__heading-1")

    QUESTION_3 = (By.ID, "accordion__heading-2")

    QUESTION_4 = (By.ID, "accordion__heading-3")

    QUESTION_5 = (By.ID, "accordion__heading-4")

    QUESTION_6 = (By.ID, "accordion__heading-5")

    QUESTION_7 = (By.ID, "accordion__heading-6")

    QUESTION_8 = (By.ID, "accordion__heading-7")

    ANSWER_1 = (By.XPATH, f'.//p[(text()="{QuestionsAnswers.ANSWER_ONE_TEXT}")]')

    ANSWER_2 = (By.XPATH, f'.//p[(text()="{QuestionsAnswers.ANSWER_TWO_TEXT}")]')

    ANSWER_3 = (By.XPATH, f'.//p[(text()="{QuestionsAnswers.ANSWER_THREE_TEXT}")]')

    ANSWER_4 = (By.XPATH, f'.//p[(text()="{QuestionsAnswers.ANSWER_FOUR_TEXT}")]')

    ANSWER_5 = (By.XPATH, f'.//p[(text()="{QuestionsAnswers.ANSWER_FIVE_TEXT}")]')

    ANSWER_6 = (By.XPATH, f'.//p[(text()="{QuestionsAnswers.ANSWER_SIX_TEXT}")]')

    ANSWER_7 = (By.XPATH, f'.//p[(text()="{QuestionsAnswers.ANSWER_SEVEN_TEXT}")]')

    ANSWER_8 = (By.ID, "accordion__panel-7")

    IMPORTANT_QUESTIONS = (By.XPATH, ".//div[@class='Home_SubHeader__zwi_E' and (text()='Вопросы о важном')]")

    RENT_TIME_IS_FINISHING = (By.XPATH, ".//div[(text()='Когда аренда заканчивается')]")

    MAIN_PAGE_SLOGAN = (By.XPATH, ".//div[@class='Home_Header__iJKdX']")

    LINK_TO_DZEN = (By.XPATH, "//div/a[(@class='Header_LogoYandex__3TSOI' and @href='//yandex.ru')]")

    SAMOKAT_BUTTON = (By.XPATH, "//div/a[(@class='Header_LogoScooter__3lsAR' and @href='/')]")

    ORDER_BUTTON_1_AT_THE_TOP = (By.XPATH, ".//div[contains(@class, 'Header_Nav')]/button[contains(@class, 'Button_Button') and (text()='Заказать')]")

    ORDER_BUTTON_2_AT_THE_BOTTOM = (By.XPATH, ".//div[contains(@class, 'Home_FinishButton')]/button[contains(@class, 'Button_Button') and (text()='Заказать')]")

    LOGO_YA = (By.XPATH, ".//div/header/div[contains(@class, 'desktop-base-header')]/a")

    COOKIE_WINDOW = (By.XPATH, ".//div/button[contains(@class, 'App_CookieButton')]")




    # order_page_ 1

    WHO_IS_THE_SCOOTER_FOR_CHECK_PAGE = (By.XPATH, ".//div[(text()='Для кого самокат')]")  # Для кого самокат

    FIRSTNAME_FIELD = (By.XPATH, "//div/input[@placeholder='* Имя']")

    LASTNAME_FIELD = (By.XPATH, "//div/input[@placeholder='* Фамилия']")

    ADDRESS_FIELD = (By.XPATH, "//div/input[@placeholder='* Адрес: куда привезти заказ']")

    METRO_LIST = (By.XPATH, ".//input[@class='select-search__input' and @placeholder='* Станция метро']")

    SELECT_METRO = (By.XPATH, "//div[(text()='Волоколамская')]")

    PHONE_FIELD = (By.XPATH, "//div/input[@placeholder='* Телефон: на него позвонит курьер']")

    NEXT_BUTTON = (By.XPATH, ".//div/button[(@class='Button_Button__ra12g Button_Middle__1CSJM') and (text()='Далее')]")

    # order_page_2

    ABOUT_THE_RENT_CHECK_PAGE = (By.XPATH, ".//div[(text()='Про аренду')]")                # Про аренду

    CALENDAR = (By.XPATH, ".//div[@class='react-datepicker__input-container']/input[@placeholder='* Когда привезти самокат']/parent::div")

    CALENDAR_SELECT_DATE = (By.XPATH, ".//div[(@class='react-datepicker')]//div[@aria-label='Choose вторник, 2-е июля 2024 г.']")

    RENT_PERIOD_LIST = (".//div[(text()='* Срок аренды')]/parent::div[@class='Dropdown-control']")

    SELECT_RENT_PERIOD = (By.XPATH, ".//div[(text()='двое суток')]") ###

    BIKE_COLOR_BLACK = (By.XPATH, ".//div[@class='Order_Checkboxes__3lWSI']/label[(text()='чёрный жемчуг')]")  # кликнуть

    COMMENT_FIELD = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']") #click

    CREATE_ORDER_BUTTON = (By.XPATH, ".//div[@class='Order_Buttons__1xGrp']/button[(text()='Заказать')]")

    CONFIRM_BUTTON_YES = (By.XPATH, ".//button[(text()='Да')]")

    ORDER_ADDED = (By.XPATH, ".//div[@class='Order_ModalHeader__3FDaJ' and (text()='Заказ оформлен')]")  # is displayed

    SHOW_STATUS_BUTTON = (By.XPATH, "//div/button[(text()='Посмотреть статус')]")


    # yandex_page

    CLOSE_POPUP = (By.XPATH, ".//div[3]/div/div[1]/div/div/div/div/span")  # меняющийся локатор, проверить











    # ordered_page

    CANCEL_ORDER_BUTTON_IS_CLICKABLE = (By.XPATH, "//div/button[(text()='Отменить заказ')]")














