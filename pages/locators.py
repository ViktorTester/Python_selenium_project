from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators ():
    LOGIN_SUBMIT = (By.NAME, "login_submit")
    REGISTRATION_SUBMT = (By.NAME, "registration_submit")