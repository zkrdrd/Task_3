import re
import time

import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.profile_page import ProfilePage


@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("Открытие всплывающего окна с деталями заказа")
    def test_order_modal_open(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_feed()
        order_feed = OrderFeedPage(driver)
        order_feed.click_first_order()
        assert order_feed.is_order_modal_displayed()

    @allure.title(
        "Заказы пользователя из 'Истории заказов' отображаются в 'Ленте заказов'"
    )
    def test_user_orders_in_feed(self, driver):  # делать заказ и переходить смотреть
        main_page = MainPage(driver)
        main_page.click_account()
        login_page = LoginPage(driver)
        login_page.login()
        main_page.drag_ingredient_to_constructor()
        main_page.click_create_order()
        order_page = OrderFeedPage(driver)
        order_page.is_order_modal_displayed()
        main_page.close_modal()
        main_page.click_order_feed()
        main_page.click_account()
        profile_page = ProfilePage(driver)
        profile_page.click_order_history()
        profile_order_number = profile_page.get_order_number()
        main_page.click_order_feed()
        order_feed_number = order_page.get_order_number()
        assert profile_order_number[0] == order_feed_number[0]

    @allure.title(
        "При создании нового заказа счётчики 'Выполнено за сегодня' и 'Выполнено за всё время' увеличивается"
    )
    def test_today_total_completed_counter_increase(self, driver):
        main_page = MainPage(driver)
        main_page.click_account()
        login_page = LoginPage(driver)
        login_page.login()
        main_page.constructor_page_is_open()
        main_page.click_order_feed()
        order_page = OrderFeedPage(driver)
        today_before = order_page.get_today_completed()
        total_before = order_page.get_total_completed()
        main_page.click_constructor()
        main_page.drag_ingredient_to_constructor()
        main_page.click_create_order()
        main_page.close_modal()
        main_page.click_order_feed()
        today_after = order_page.get_today_completed()
        total_after = order_page.get_total_completed()
        assert today_after == str(int(today_before) + 1) and total_after == str(
            int(total_before) + 1
        )

    @allure.title("После оформления заказа его номер появляется в разделе 'В работе'")
    def test_order_appears_in_progress(self, driver):
        main_page = MainPage(driver)
        main_page.click_account()
        login_page = LoginPage(driver)
        login_page.login()
        main_page.drag_ingredient_to_constructor()
        main_page.click_create_order()
        order_page = OrderFeedPage(driver)
        order_page.is_order_modal_displayed()
        order_page.order_modal_loaded()
        order_number = order_page.get_order_number_from_modal()
        main_page.close_modal()
        main_page.click_order_feed()
        order_page.order_page_is_open()
        assert order_page.order_number_in_progress(order_number)
