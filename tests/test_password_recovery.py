import allure

from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


@allure.feature("Восстановление пароля")
class TestPasswordRecovery:

    @allure.title(
        "Переход на страницу восстановления пароля по кнопке 'Восстановить пароль'"
    )
    def test_navigate_to_forgot_password(self, driver):
        MainPage(driver).click_account()
        LoginPage(driver).click_forgot_password()
        assert ForgotPasswordPage(driver).password_recovery_page_is_displayed()

    @allure.title("Ввод почты и клик по кнопке 'Восстановить'")
    def test_recovery_with_email(self, driver):
        MainPage(driver).click_account()
        LoginPage(driver).click_forgot_password()
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.enter_email_and_recover()
        assert forgot_page.is_input_code_field_active()

    @allure.title("Клик по кнопке показать/скрыть пароль делает поле активным")
    def test_show_password_activates_field(self, driver):
        MainPage(driver).click_account()
        LoginPage(driver).click_forgot_password()
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.enter_email_and_recover()
        forgot_page.click_show_password()
        assert forgot_page.is_password_field_active()
