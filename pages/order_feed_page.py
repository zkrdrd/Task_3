from pages.base_page import BasePage
from pages.locators import OrderFeedPageLocators
import allure


class OrderFeedPage(BasePage):
    @allure.step("Выпираем первый заказ")
    def click_first_order(self):
        self.click(OrderFeedPageLocators.ORDER_CARD)

    @allure.step("Модально окно поазано")
    def is_order_modal_displayed(self):
        return self.is_element_present(OrderFeedPageLocators.ORDER_MODAL)

    @allure.step("Номер зааказ из модального окна")
    def get_order_number_from_modal(self):
        return self.get_text(OrderFeedPageLocators.ORDER_NUMBER_IN_MODAL)

    @allure.step("Всего завершено заказов")
    def get_total_completed(self):
        return self.get_text(OrderFeedPageLocators.TOTAL_COMPLETED_COUNTER)

    @allure.step("Сегондя завершено заказов")
    def get_today_completed(self):
        return self.get_text(OrderFeedPageLocators.TODAY_COMPLETED_COUNTER)

    @allure.step("Заказы в процессе")
    def get_in_progress_orders(self):
        elements = self.driver.find_elements(*OrderFeedPageLocators.IN_PROGRESS_SECTION)
        return [el.text for el in elements]
