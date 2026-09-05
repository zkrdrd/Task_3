from selenium.webdriver.common.by import By


class BaseLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")


class MainPageLocators:
    ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]/parent::a")
    MODAL_IS_OPEN = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened__3ISw4 Modal_modal__P3_V5')]//h2[text()='Детали ингредиента']",
    )
    MODAL_CLOSE_BUTTON = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened__3ISw4 Modal_modal__P3_V5')]//button[contains(@class, 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK')]",
    )
    MODAL_IS_CLOSED = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal__P3_V5')]//h2[text()='Детали ингредиента']",
    )
    # ---
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']/parent::a")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']/parent::a")
    INGREDIENT_BUN = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")
    INGREDIENT_DETAILS_MODAL = (
        By.XPATH,
        "//div[contains(@class, 'Modal_modal__container')]",
    )

    INGREDIENT_COUNTER = (
        By.XPATH,
        "//ul[@class='BurgerConstructor_basket__list__l9dp_']//img[contains(@alt, 'Флюоресцентная булка R2-D3 (верх)') or contains(@alt, 'Флюоресцентная булка R2-D3 (низ)')]",
    )
    CREATE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_MODAL = (
        By.XPATH,
        "//div[contains(@class, 'Modal_modal__contentBox__sCy8X pt-30 pb-30')]//p[contains(text(), 'идентификатор заказа')]",
    )

    # Карточка ингредиента-соуса (для второго добавления)
    INGREDIENT_SAUCE = (By.XPATH, "//img[@alt='Соус Spicy-X']")

    # Зона конструктора (куда перетаскиваем — блок сборки бургера)
    CONSTRUCTOR_DROP_ZONE = (
        By.XPATH,
        "//ul[contains(@class, 'BurgerConstructor_basket__list')]",
    )


class LoginPageLocators:
    PAGE_TITLE = (By.XPATH, "//h2[text()='Вход']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")


class ForgotPasswordPageLocators:
    RCOVERY_TEXT = (By.XPATH, "//h2[contains(text(),'Восстановление пароля')]")
    CODE_FROM_MAIL = (By.XPATH, "//label[contains(text(), 'Введите код из письма')]")

    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    RECOVERY_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    SHOW_PASSWORD_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'input__icon input__icon-action')]",
    )
    PASSWORD_ACTIVE_FIELD = (
        By.XPATH,
        "//div[contains(@class, 'input_status_active')]",
    )


class ProfilePageLocators:
    PROFILE_LINK = (By.XPATH, "//a[@href='/account/profile']")
    ORDER_HISTORY_LINK = (By.XPATH, "//a[@href='/account/order-history']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    ORDER_HISTORY_ITEM = (
        By.XPATH,
        "//div[contains(@class, 'OrderHistory_orderHistory__qy1VB')]",
    )


class OrderFeedPageLocators:
    ORDER_CARD = (By.XPATH, "//div[contains(@class, 'OrderHistory_orderCard')]")
    ORDER_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__container')]")
    ORDER_NUMBER_IN_MODAL = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title')]")
    TOTAL_COMPLETED_COUNTER = (
        By.XPATH,
        "//p[text()='Выполнено за всё время:']/following-sibling::p",
    )
    TODAY_COMPLETED_COUNTER = (
        By.XPATH,
        "//p[text()='Выполнено за сегодня:']/following-sibling::p",
    )
    IN_PROGRESS_SECTION = (
        By.XPATH,
        "//div[contains(@class, 'OrderFeed_orderBoard')]//li[contains(@class, 'text_type_digits-default')]",
    )
