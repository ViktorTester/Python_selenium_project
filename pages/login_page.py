from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_go_to_login_page(self):
        assert "login" in self.browser.current_url, f"expected 'login' to be substring of {self.browser.current_url}"

        link = self.browser.find_element(*LoginPageLocators.SUBMIT_LINK)
        link.click()

        link = self.browser.find_element(*LoginPageLocators.REGISTRATION_LINK)
        link.click()

    # return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_page(self):
        assert "login" in self.browser.current_url, f"expected 'login' to be substring of {self.browser.current_url}"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.SUBMIT_LINK), "Login submission link is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.SUBMIT_LINK), "Registration is not presented"
