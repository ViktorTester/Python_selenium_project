from .pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    time.sleep(1)
    page.add_product_to_basket()
    time.sleep(1)
    page.should_be_right_book()
    time.sleep(1)
    page.should_be_right_price()


# pytest -s test_product_page.py


