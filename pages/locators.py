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
    CONSTRUCTOR_DROP_ZONE = (
        By.XPATH,
        "//ul[contains(@class, 'BurgerConstructor_basket__list')]",
    )
    CONSTRUCTOR_INGRIDIENT_LIST = (
        By.XPATH,
        "//div[contains(@class, 'BurgerIngredients_ingredients__menuContainer__Xu3Mo')]",
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
    ORDER_NUMBER = (
        By.XPATH,
        "//div[contains(@class, 'OrderHistory_textBox__3lgbs mb-6')]//p[contains(@class, 'text text_type_digits-default')]",
    )


class OrderFeedPageLocators:
    ORDER_TITLE = (By.XPATH, "//h1[text()='Лента заказов']")
    ORDER_LIST = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list__OLh59')]")
    ORDER_MODAL_OVERLAY = (
        By.XPATH,
        "//div[@class='Modal_modal__P3_V5']//img[contains(@class, 'Modal_modal__loading__3534A') and contains(@alt, 'loading animation')]",
    )
    ORDER_NUMBER_MODAL = (
        By.XPATH,
        "//div[contains(@class, 'Modal_modal__container__Wo2l_')]//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8')]",
    )
    ORDER_CARD = (
        By.XPATH,
        "//li[contains(@class, 'OrderHistory_listItem__2x95r mb-6')]//a",
    )
    ORDER_MODAL = (
        By.XPATH,
        "//div[contains(@class, 'Modal_modal__container__Wo2l_')]",
    )
    TOTAL_COMPLETED_COUNTER = (
        By.XPATH,
        "//p[text()='Выполнено за все время:']/following-sibling::p",
    )
    TODAY_COMPLETED_COUNTER = (
        By.XPATH,
        "//p[text()='Выполнено за сегодня:']/following-sibling::p",
    )
    IN_PROGRESS_SECTION = (
        By.XPATH,
        "//ul[contains(@class, 'OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi')]//li[contains(@class,'text text_type_digits-default mb-2')]",
    )
    ORDER_NUMBER = (
        By.XPATH,
        "//div[contains(@class, 'OrderHistory_textBox__3lgbs mb-6')]//p[contains(@class, 'text text_type_digits-default')]",
    )
    MODAL_CLOSE_BUTTON = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened__3ISw4 Modal_modal__P3_V5')]//button[contains(@class, 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK')]",
    )
