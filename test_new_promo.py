import pytest
from .pages.product_page import ProductPage



@pytest.mark.parametrize('links', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail(reason="wont fix it right now")), "8", "9"])
def test_guest_can_add_product_to_basket(browser, links):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{links}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_be_right_book()
    page.should_be_right_price()



