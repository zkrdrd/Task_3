import allure

from pages.base_page import BasePage
from pages.locators import ProfilePageLocators


class ProfilePage(BasePage):
    @allure.step("Нажимаем на профиль")
    def click_profile(self):
        self.click(ProfilePageLocators.PROFILE_LINK)

    @allure.step("Нажимаем история закпазов")
    def click_order_history(self):
        self.click(ProfilePageLocators.ORDER_HISTORY_LINK)

    @allure.step("Наживаем выйти")
    def click_logout(self):
        self.click(ProfilePageLocators.LOGOUT_BUTTON)

    @allure.step("История заказов показана")
    def is_order_history_item_present(self):
        return self.is_element_present(ProfilePageLocators.ORDER_HISTORY_ITEM)

    @allure.step("Получение номера заказа из истории заказов")
    def get_order_number(self):
        return self.get_text(ProfilePageLocators.ORDER_NUMBER)
