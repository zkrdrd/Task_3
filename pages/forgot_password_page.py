import allure

from helpers.data import Credential
from pages.base_page import BasePage
from pages.locators import ForgotPasswordPageLocators


class ForgotPasswordPage(BasePage):
    @allure.step("Вводим адрес электронной почты")
    def enter_email_and_recover(self):
        self.email_input()
        self.click(ForgotPasswordPageLocators.RECOVERY_BUTTON)

    @allure.step("Нажимаем посмотреть пароль")
    def click_show_password(self):
        self.click(ForgotPasswordPageLocators.SHOW_PASSWORD_BUTTON)

    @allure.step("Проверяем поле ввода пароля")
    def is_password_field_active(self):
        return self.is_element_present(ForgotPasswordPageLocators.PASSWORD_ACTIVE_FIELD)

    @allure.step("Поле 'Введите код из письма' отображается")
    def is_input_code_field_active(self):
        return self.is_element_present(ForgotPasswordPageLocators.CODE_FROM_MAIL)

    @allure.step("Отображается страница востановление пароля")
    def password_recovery_page_is_displayed(self):
        return self.is_element_present(
            ForgotPasswordPageLocators.RCOVERY_TEXT
        ) and self.is_element_present(ForgotPasswordPageLocators.RECOVERY_BUTTON)
