from selenium.webdriver.common.by import By
import allure

@allure.title('Локатор для страницы созданного заказа')
class OrderedPageLocators:

    CANCEL_ORDER_BUTTON_IS_CLICKABLE = (By.XPATH, "//div/button[(text()='Отменить заказ')]")
