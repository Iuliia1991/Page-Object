from pages.locators import BasketPageLocators
from pages.base_page import BasePage


class BasketPage(BasePage):
    def basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_IS_NOT_EMPTY), \
            "Basket is not empty!"

    def basket_empty_text_present(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_TEXT), \
            "Basket empty text is not presented!"