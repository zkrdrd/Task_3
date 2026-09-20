from time import sleep

import allure

from pages.base_page import BasePage
from pages.locators import BaseLocators, LoginPageLocators


class LoginPage(BasePage):
    @allure.step("Нажимаем кнопку забыли пароль")
    def click_forgot_password(self):
        self.click(LoginPageLocators.FORGOT_PASSWORD_LINK)

    @allure.step("Авторизуемся")
    def login(self):
        self.email_input()
        self.password_input()
        self.click(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Открылась страница авторизации")
    def login_page_is_display(self):
        return (
            self.is_element_present(LoginPageLocators.PAGE_TITLE)
            and self.is_element_present(BaseLocators.EMAIL_INPUT)
            and self.is_element_present(BaseLocators.PASSWORD_INPUT)
            and self.is_element_present(LoginPageLocators.LOGIN_BUTTON)
        )
