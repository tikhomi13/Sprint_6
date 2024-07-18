from selenium.webdriver.common.by import By


class BasePageLocators:

    COOKIE_WINDOW = (By.XPATH, ".//div/button[contains(@class, 'App_CookieButton')]")

    ORDER_BUTTON_1_AT_THE_TOP = (By.XPATH, ".//div[contains(@class, 'Header_Nav')]/button[contains(@class, 'Button_Button') and (text()='Заказать')]")

    SAMOKAT_BUTTON = (By.XPATH, "//div/a[(@class='Header_LogoScooter__3lsAR' and @href='/')]")

    LINK_TO_DZEN = (By.XPATH, "//div/a[(@class='Header_LogoYandex__3TSOI' and @href='//yandex.ru')]")
