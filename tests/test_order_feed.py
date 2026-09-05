import time

import allure
from selenium.webdriver.common.by import By

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
    def test_user_orders_in_feed(self, driver):
        login_page = LoginPage(driver)
        login_page.login()
        # переходим в историю заказов
        driver.get("https://stellarburgers.nomoreparties.site/account/order-history")
        # получаем номер последнего заказа
        profile_page = ProfilePage(driver)
        history_items = driver.find_elements(
            By.XPATH, "//div[contains(@class, 'OrderHistory_listItem')]"
        )
        assert len(history_items) > 0, "Нет заказов в истории"
        # извлекаем номер заказа (предположим, что он в атрибуте или тексте)
        order_number = (
            history_items[0]
            .find_element(
                By.XPATH, ".//p[contains(@class, 'text_type_digits-default')]"
            )
            .text
        )
        # переходим в ленту заказов
        driver.get("https://stellarburgers.nomoreparties.site/feed")
        order_feed = OrderFeedPage(driver)
        # ищем этот номер заказа в ленте
        assert order_feed.is_element_present(
            (By.XPATH, f"//p[text()='{order_number}']")
        )

    @allure.title(
        "При создании нового заказа счётчик 'Выполнено за всё время' увеличивается"
    )
    def test_total_completed_counter_increase(self, driver, credentials):
        # логинимся и создаём заказ
        login_page = LoginPage(driver)
        login_page.login(credentials["email"], credentials["password"])
        # запоминаем текущее значение
        driver.get("https://stellarburgers.nomoreparties.site/feed")
        order_feed = OrderFeedPage(driver)
        total_before = int(order_feed.get_total_completed())
        # возвращаемся на главную и создаём заказ
        driver.get("https://stellarburgers.nomoreparties.site/")
        main_page = MainPage(driver)
        main_page.click_ingredient()
        driver.execute_script(
            "arguments[0].click();",
            driver.find_element(By.XPATH, "//button[text()='Добавить']"),
        )
        main_page.click_create_order()
        main_page.close_modal()
        # снова идём в ленту и проверяем счётчик
        driver.get("https://stellarburgers.nomoreparties.site/feed")
        total_after = int(order_feed.get_total_completed())
        assert total_after == total_before + 1

    @allure.title(
        "При создании нового заказа счётчик 'Выполнено за сегодня' увеличивается"
    )
    def test_today_completed_counter_increase(self, driver, credentials):
        # аналогично предыдущему, но используем сегодняшний счётчик
        login_page = LoginPage(driver)
        login_page.login(credentials["email"], credentials["password"])
        driver.get("https://stellarburgers.nomoreparties.site/feed")
        order_feed = OrderFeedPage(driver)
        today_before = int(order_feed.get_today_completed())
        driver.get("https://stellarburgers.nomoreparties.site/")
        main_page = MainPage(driver)
        main_page.click_ingredient()
        driver.execute_script(
            "arguments[0].click();",
            driver.find_element(By.XPATH, "//button[text()='Добавить']"),
        )
        main_page.click_create_order()
        main_page.close_modal()
        driver.get("https://stellarburgers.nomoreparties.site/feed")
        today_after = int(order_feed.get_today_completed())
        assert today_after == today_before + 1

    @allure.title("После оформления заказа его номер появляется в разделе 'В работе'")
    def test_order_appears_in_progress(self, driver, credentials):
        login_page = LoginPage(driver)
        login_page.login(credentials["email"], credentials["password"])
        main_page = MainPage(driver)
        main_page.click_ingredient()
        driver.execute_script(
            "arguments[0].click();",
            driver.find_element(By.XPATH, "//button[text()='Добавить']"),
        )
        main_page.click_create_order()
        order_number = main_page.get_order_number_from_modal()
        main_page.close_modal()
        driver.get("https://stellarburgers.nomoreparties.site/feed")
        order_feed = OrderFeedPage(driver)
        # ждём появления номера в разделе "В работе" (может занять несколько секунд)
        time.sleep(2)
        in_progress_numbers = order_feed.get_in_progress_orders()
        assert order_number in in_progress_numbers
