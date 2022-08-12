from selenium.webdriver.common.by import By


# class MainPageLocators():
#     LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_SUBMIT = (By.NAME, "login_submit")
    REGISTRATION_SUBMT = (By.NAME, "registration_submit")

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