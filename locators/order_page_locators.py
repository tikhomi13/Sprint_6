from selenium.webdriver.common.by import By
import allure

@allure.title('Локаторы для страницы заказа')
class OrderPageLocators:

    WHO_IS_THE_SCOOTER_FOR_CHECK_PAGE = (By.XPATH, ".//div[(text()='Для кого самокат')]")  # Для кого самокат

    FIRSTNAME_FIELD = (By.XPATH, "//div/input[@placeholder='* Имя']")

    LASTNAME_FIELD = (By.XPATH, "//div/input[@placeholder='* Фамилия']")

    ADDRESS_FIELD = (By.XPATH, "//div/input[@placeholder='* Адрес: куда привезти заказ']")

    METRO_LIST = (By.XPATH, ".//input[@class='select-search__input' and @placeholder='* Станция метро']")

    SELECT_METRO = (By.XPATH, "//div[(text()='Волоколамская')]")

    PHONE_FIELD = (By.XPATH, "//div/input[@placeholder='* Телефон: на него позвонит курьер']")

    NEXT_BUTTON = (By.XPATH, ".//div/button[(@class='Button_Button__ra12g Button_Middle__1CSJM') and (text()='Далее')]")

    ABOUT_THE_RENT_CHECK_PAGE = (By.XPATH, ".//div[(text()='Про аренду')]")

    CALENDAR = (By.XPATH, ".//div[@class='react-datepicker__input-container']/input[@placeholder='* Когда привезти самокат']/parent::div")

    CALENDAR_SELECT_DATE = (By.XPATH, ".//div[(@class='react-datepicker')]//div[@aria-label='Choose вторник, 2-е июля 2024 г.']")

    RENT_PERIOD_LIST = (By.XPATH, ".//div[(text()='* Срок аренды')]/parent::div[@class='Dropdown-control']")

    SET_RENT_PERIOD = (By.XPATH, ".//div[(text()='двое суток')]")

    BIKE_COLOR_BLACK = (By.XPATH, ".//div[@class='Order_Checkboxes__3lWSI']/label[(text()='чёрный жемчуг')]")

    COMMENT_FIELD = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")

    CREATE_ORDER_BUTTON = (By.XPATH, ".//div[@class='Order_Buttons__1xGrp']/button[(text()='Заказать')]")

    CONFIRM_BUTTON_YES = (By.XPATH, ".//button[(text()='Да')]")

    ORDER_ADDED = (By.XPATH, ".//div[@class='Order_ModalHeader__3FDaJ' and (text()='Заказ оформлен')]")

    SHOW_STATUS_BUTTON = (By.XPATH, "//div/button[(text()='Посмотреть статус')]")
