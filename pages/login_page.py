from .base_page import BasePage
from .locators import LoginPageLocators
import time

email = str(time.time()) + "@fakemail.org"

class LoginPage(BasePage):
    def should_go_to_login_page(self):
        assert "login" in self.browser.current_url, f"expected 'login' to be substring of {self.browser.current_url}"
        link = self.browser.find_element(*LoginPageLocators.LOGIN_SUBMIT)
        link.click()
        link = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT)
        link.click()


    def should_be_login_page(self):
        assert "login" in self.browser.current_url, f"expected 'login' to be substring of {self.browser.current_url}"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_SUBMIT), "Login submission link is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_SUBMIT), "Registration is not presented"


    def register_new_user(self):
        input1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        input1.send_keys(email)
        time.sleep(2)
        input2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1)
        input2.send_keys("StrongPassword123_")
        time.sleep(2)
        input3 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
        input3.send_keys("StrongPassword123_")
        time.sleep(2)
        link = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT)
        link.click()




