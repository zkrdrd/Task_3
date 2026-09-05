import allure

from pages.base_page import BasePage
from pages.locators import OrderFeedPageLocators


class OrderFeedPage(BasePage):

    @allure.step("Выбираем первый заказ")
    def click_first_order(self):
        self.click(OrderFeedPageLocators.ORDER_CARD)

    @allure.step("Модально окно поазано")
    def is_order_modal_displayed(self):
        return self.is_element_present(OrderFeedPageLocators.ORDER_MODAL)

    @allure.step("Номер зааказ из модального окна")
    def get_order_number_from_modal(self):
        return self.get_text(OrderFeedPageLocators.ORDER_NUMBER_MODAL)

    @allure.step("Всего завершено заказов")
    def get_total_completed(self):
        return self.get_text(OrderFeedPageLocators.TOTAL_COMPLETED_COUNTER)

    @allure.step("Сегондя завершено заказов")
    def get_today_completed(self):
        return self.get_text(OrderFeedPageLocators.TODAY_COMPLETED_COUNTER)

    @allure.step("Заказ в процессе")
    def order_number_in_progress(self, number):
        return self.wait_text(OrderFeedPageLocators.IN_PROGRESS_SECTION, number)

    @allure.step("Модальное окно прогрузилось")
    def order_modal_loaded(self):
        self.is_element_present(OrderFeedPageLocators.ORDER_MODAL_OVERLAY)

    @allure.step("Получение номера заказа из списка заказов")
    def get_order_number(self):
        return self.get_text(OrderFeedPageLocators.ORDER_NUMBER)

    @allure.step("Страница заказов открыта")
    def order_page_is_open(self):
        return (
            self.is_element_present(OrderFeedPageLocators.ORDER_TITLE)
            and self.is_element_present(OrderFeedPageLocators.ORDER_LIST)
            and "/feed" in self.get_current_url(),
        )
