import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from helpers.data import URL
from helpers.helpers import JS_DRAG_AND_DROP
from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):

    @allure.step("Нажать кнопку 'Аккаунт'")
    def click_account(self):
        self.click(MainPageLocators.ACCOUNT_BUTTON)

    @allure.step("Нажимаем на кнопку 'Констурктор'")
    def click_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Нажимаем на кнопку 'Заказы'")
    def click_order_feed(self):
        self.click(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Нажимаем на кнопку 'Ингридиента'")
    def click_ingredient(self):
        self.click(MainPageLocators.INGREDIENT_BUN)

    @allure.step("Получаем количество ингридиентов")
    def get_ingredient_counter(self):
        return self.get_text(MainPageLocators.INGREDIENT_COUNTER)

    @allure.step("Закрываем модальное окно")
    def close_modal(self):
        self.click(MainPageLocators.MODAL_CLOSE_BUTTON)

    @allure.step("Модальное окно показано")
    def is_modal_displayed(self):
        return self.is_element_present(MainPageLocators.MODAL_IS_OPEN)

    @allure.step("Модальное окно закрыто")
    def is_modal_closed(self):
        return self.is_element_present(MainPageLocators.MODAL_IS_CLOSED)

    @allure.step("Нажимаем Создать заказ")
    def click_create_order(self):
        self.click(MainPageLocators.CREATE_ORDER_BUTTON)

    @allure.step("Модальное окно заказа")
    def get_order_modal(self):
        return self.get_text(MainPageLocators.ORDER_MODAL)

    @allure.step("Переносим модальное ингридиент в зону конструктора")
    def drag_ingredient_to_constructor(self):
        """Перетаскивает ингредиент в блок сборки (drag & drop)."""
        source = self.visibility_element(MainPageLocators.INGREDIENT_BUN)
        target = self.visibility_element(MainPageLocators.CONSTRUCTOR_DROP_ZONE)
        self.execute_script(JS_DRAG_AND_DROP, source, target)

    @allure.step("Возвращает текущее значение счётчика булки (0, если не добавлена).")
    def get_bun_counter(self) -> int:
        """Возвращает текущее значение счётчика булки (0, если не добавлена)."""
        elements = self.find_elements(*MainPageLocators.INGREDIENT_COUNTER)
        if not elements:
            return 0
        return len(elements)

    @allure.step("Получаем количество элементов в конструкторе")
    def wait_bun_counter(self, expected_value: int, timeout: int = 10):
        """Ждёт, пока счётчик булки не станет равным expected_value."""
        return self.get_bun_counter() == expected_value

    def constructor_page_is_open(self):
        return (
            self.is_element_present(MainPageLocators.CONSTRUCTOR_INGRIDIENT_LIST)
            and self.get_current_url() == URL.MAIN_PAGE_URL
        )
