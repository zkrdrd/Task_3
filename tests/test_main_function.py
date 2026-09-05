import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


@allure.feature("Основной функционал")
class TestMainFunctionality:

    @allure.title("Переход по клику на 'Лента заказов'")
    def test_click_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_feed()
        assert OrderFeedPage(driver).order_page_is_open()

    @allure.title("Переход по клику на 'Конструктор'")
    def test_click_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_feed()
        main_page.click_constructor()
        assert main_page.constructor_page_is_open()

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
        main_page.drag_ingredient_to_constructor()
        main_page.wait_bun_counter(initial_counter + 2)
        updated_counter = main_page.get_bun_counter()
        assert (
            updated_counter == initial_counter + 2
        ), f"Ожидали счётчик {initial_counter + 2}, получили {updated_counter}"

    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_create_order_as_logged_user(self, driver):
        main_page = MainPage(driver)
        main_page.click_account()
        login_page = LoginPage(driver)
        login_page.login()
        main_page.drag_ingredient_to_constructor()
        main_page.click_create_order()
        assert main_page.get_order_modal()
