from selenium.webdriver.common.by import By
from pages.product_page import ProductPage
from pages.base_page import BasePage
import time
import pytest


@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
                                  pytest.param(7, marks=pytest.mark.xfail),
                                  8, 9])

def test_guest_can_add_to_cart(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()
    page.return_book_name()
    page.return_book_price()
    page.add_to_cart()
    time.sleep(1)
    page.solve_quiz_and_get_code()
    time.sleep(3)
    cart_page = ProductPage(browser, browser.current_url)
    cart_page.name_should_be_right(page.return_book_name())
    cart_page.price_should_be_right(page.return_book_price())

