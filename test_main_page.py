import time
from .pages.main_page import MainPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    time.sleep(5)
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
    time.sleep(5)


# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     browser.get(link)pytest - v - -tb=line --browser_name=chrome --language=en test_main_page.py
#     login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
#     login_link.click()

#     тест без Page Object