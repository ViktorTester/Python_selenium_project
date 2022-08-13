from .pages.product_page import ProductPage
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
import pytest

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_be_right_book()
    page.should_be_right_price()

@pytest.mark.parametrize('link', [pytest.param("coders-at-work_207/?promo=newYear2019", marks=pytest.mark.xfail(reason="wont fix it right now"))])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/{link}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.parametrize('link', [pytest.param("coders-at-work_207/?promo=newYear2019", marks=pytest.mark.xfail(reason="wont fix it right now"))])
def test_message_disappeared_after_adding_product_to_basket(browser,link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/{link}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_dissapear()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket()
    page = BasketPage(browser, link)
    page.should_be_empty_cart_msg()
    page.should_be_empty_cart()




