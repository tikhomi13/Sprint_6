from selenium.webdriver.common.by import By


class OrderedPageLocators:

    CANCEL_ORDER_BUTTON_IS_CLICKABLE = (By.XPATH, "//div/button[(text()='Отменить заказ')]")
