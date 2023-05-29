from pages.locators import ProductPageLocators
from pages.base_page import BasePage


class ProductPage(BasePage):
    def add_to_cart(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def return_book_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        return book_name.text

    def return_book_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        return book_price.text

    def name_should_be_right(self, book_name):
        book_cart_name = self.browser.find_element(*ProductPageLocators.BOOK_CART_NAME)
        assert book_cart_name.text == book_name, "The book name is not right"

    def price_should_be_right(self, book_price):
        book_cart_price = self.browser.find_element(*ProductPageLocators.BOOK_CART_PRICE)
        assert book_cart_price.text == book_price, "The book price is not right"
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, not disappeared"


