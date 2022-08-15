from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_SUBMIT = (By.NAME, "login_submit")
    REGISTRATION_SUBMIT = (By.NAME, "registration_submit")
    REGISTRATION_EMAIL = (By.NAME, "registration-email")
    REGISTRATION_PASSWORD1 = (By.NAME, "registration-password1")
    REGISTRATION_PASSWORD2 = (By.NAME, "registration-password2")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class ProductPageLocators():
    ADD_TO_BASKET = (By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/form/button")
    ITEM_NAME = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/h1")
    ITEM_IN_CART_NAME = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    ITEM_IN_CART_PRICE = (By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")
    ITEM_PRICE = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/p[1]")
    SUCCESS_MESSAGE = (By.XPATH, "//*[@id='messages']/div[1]/div")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CHECK_THE_BASKET = (By.XPATH, "//*[@id='default']/header/div[1]/div/div[2]/span/a")
    #(By.XPATH, ("//a[text()='Посмотреть корзину']")) при смене языка, поиск не сработает.
    CART_IS_EMPY_MSG = (By.XPATH, "//*[@id='content_inner']/p")
    CART_IS_EMPTY = (By.CLASS_NAME, "thumbnail")

