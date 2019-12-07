from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    MAIN_PAGE_URL = "http://selenium1py.pythonanywhere.com/"


class LoginPageLocators():
    LOGIN_URL = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    REGISTER_FORM = (By.ID, "register_form")
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_EMAIL_FIELD = (By.ID, "id_registration-email")
    REGISTER_PASS_FIELD = (By.ID, "id_registration-password1")
    REGISTER_PASS_REPEAT_FIELD = (By.ID, "id_registration-password2")
    REGISTER_BTN = (By.CSS_SELECTOR, "#register_form button")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form .btn-add-to-basket")
    TITLE_IN_PRODUCT_INFO = (By.CSS_SELECTOR, ".product_main h1")
    TITLE_IN_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert-success:nth-child(1) strong")
    PRICE_IN_PRODUCT_INFO = (By.CSS_SELECTOR, ".product_main .price_color")
    PRICE_IN_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-info strong")


class BasketPageLocators():
    BASKET_URL = 'http://selenium1py.pythonanywhere.com/en-gb/basket/'
    HEADER_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn")
    BASKET_TITLE = (By.CSS_SELECTOR, ".page-header h1")
    BASKET_ITEMS_FORM = (By.ID, "basket_formset")
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner > p")
