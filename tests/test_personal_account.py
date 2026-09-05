import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


@allure.feature("Личный кабинет")
class TestPersonalAccount:

    @allure.title("Переход по клику на 'Личный кабинет'")
    def test_go_to_personal_account(self, driver):
        MainPage(driver).click_account()
        assert LoginPage(driver).login_page_is_display()

    @allure.title("Авторизуемся и переход в раздел 'История заказов'")
    def test_go_to_order_history(self, driver):
        main_page = MainPage(driver)
        main_page.click_account()
        LoginPage(driver).login()
        main_page.constructor_page_is_open()
        main_page.click_account()
        profile_page = ProfilePage(driver)
        profile_page.click_order_history()
        assert profile_page.is_order_history_item_present()

    @allure.title("Выход из аккаунта")
    def test_logout(self, driver):
        main_page = MainPage(driver)
        main_page.click_account()
        login_page = LoginPage(driver)
        login_page.login()
        main_page.constructor_page_is_open()
        main_page.click_account()
        ProfilePage(driver).click_logout()
        assert login_page.login_page_is_display()
