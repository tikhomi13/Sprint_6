from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from data import URLs
from data import QuestionsAnswers


class Locators:

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


    CLOSE_POPUP = (By.XPATH, ".//div[8]//span[contains(@class, 'cd475')]//*[local-name()='svg']")



# Перенести переключение окон в BasePage










