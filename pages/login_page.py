from pages.base_page import BasePage
from pages.locators import LoginPageLocators
import time



class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_url = self.browser.current_url
        assert "login" in login_url, "Login url is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Registration form is not presented"

    def register_new_user(self):
        email = str(time.time()) + "@testmail.org"
        password = "Qq1234567890"

        email_form = self.browser.find_element(*LoginPageLocators.REG_FORM_EMAIL)
        assert email_form, "Email form is not presented"
        email_form.send_keys(email)

        password_form = self.browser.find_element(*LoginPageLocators.REG_FORM_PASS)
        assert password_form, "Password form is not presented"
        password_form.send_keys(password)

        confirm_password = self.browser.find_element(*LoginPageLocators.REG_FORM_PASS_CONFIRM)
        assert confirm_password, "Password form is not presented"
        confirm_password.send_keys(password)

        register_button = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        assert register_button, "Register button is not presented"
        register_button.click()