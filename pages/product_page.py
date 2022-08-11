from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math

class ProductPage(BasePage):

    def add_product_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        link.click()
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_right_book(self):
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME)
        item_in_cart_name = self.browser.find_element(*ProductPageLocators.ITEM_IN_CART_NAME)
        assert item_name.text == item_in_cart_name.text, 'incorrect book'

    def should_be_right_price(self):
        item_in_cart_price = self.browser.find_element(*ProductPageLocators.ITEM_IN_CART_PRICE)
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE)
        assert item_in_cart_price.text == item_price.text, 'wrong price'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_dissapear(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should dissapear"



