from .base_page import BasePage
from .locators import BasePageLocators

class BasketPage(BasePage):
    def should_be_empty_cart_msg(self):
        assert self.is_element_present(*BasePageLocators.CART_IS_EMPY_MSG), "Cart is not empty msg is not present"

    def should_be_empty_cart(self):
        assert self.is_not_element_present(*BasePageLocators.CART_IS_EMPTY), "Cart is not empty"