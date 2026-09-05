from time import sleep

import allure
from selenium.webdriver.common.by import By

from helpers.data import URL
from pages.locators import MainPageLocators
from pages.login_page import LoginPage
from pages.main_page import MainPage


@allure.feature("Основной функционал")
class TestMainFunctionality:

    @allure.title("Переход по клику на 'Лента заказов'")
    def test_click_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_feed()
        assert "/feed" in driver.current_url

    @allure.title("Переход по клику на 'Конструктор'")
    def test_click_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.click_constructor()
        assert driver.current_url == URL.MAIN_PAGE_URL

    @allure.title("Открытие всплывающего окна с деталями ингредиента")
    def test_ingredient_modal_open(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient()
        assert main_page.is_modal_displayed()

    @allure.title("Закрытие всплывающего окна кликом по крестику")
    def test_ingredient_modal_close(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient()
        main_page.close_modal()
        assert main_page.is_modal_closed()

    @allure.title(
        "При добавлении ингредиента в заказ увеличивается каунтер данного ингредиента"
    )
    def test_ingredient_counter_increase(self, driver):
        main_page = MainPage(driver)
        initial_counter = main_page.get_bun_counter()
        main_page.drag_ingredient_to_constructor(MainPageLocators.INGREDIENT_BUN)
        main_page.wait_bun_counter(initial_counter + 2)
        updated_counter = main_page.get_bun_counter()
        assert (
            updated_counter == initial_counter + 2
        ), f"Ожидали счётчик {initial_counter + 2}, получили {updated_counter}"

    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_create_order_as_logged_user(self, driver):
        # логинимся
        main_page = MainPage(driver)
        main_page.click_account()
        login_page = LoginPage(driver)
        login_page.login()
        sleep(0.2)
        main_page.drag_ingredient_to_constructor(MainPageLocators.INGREDIENT_BUN)
        main_page.click_create_order()
        assert main_page.get_order_modal()
