from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CheckoutPage(BasePage):
    """
    Page Object для страницы оформления заказа.
    """
    
    # Шаг 1: Информация о покупателе
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    ZIP_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    CANCEL_BUTTON = (By.ID, "cancel")
    
    # Шаг 2: Обзор заказа
    ITEM_TOTAL = (By.CLASS_NAME, "summary_subtotal_label")
    TAX = (By.CLASS_NAME, "summary_tax_label")
    TOTAL = (By.CLASS_NAME, "summary_total_label")
    FINISH_BUTTON = (By.ID, "finish")
    
    # Шаг 3: Завершение
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    BACK_HOME_BUTTON = (By.ID, "back-to-products")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def fill_customer_info(self, first_name, last_name, zip_code):
        """Заполняет информацию о покупателе"""
        self.send_keys(self.FIRST_NAME_INPUT, first_name)
        self.send_keys(self.LAST_NAME_INPUT, last_name)
        self.send_keys(self.ZIP_CODE_INPUT, zip_code)
    
    def continue_checkout(self):
        """Нажимает кнопку Continue"""
        self.click(self.CONTINUE_BUTTON)
    
    def cancel_checkout(self):
        """Нажимает кнопку Cancel"""
        self.click(self.CANCEL_BUTTON)
        from pages.cart_page import CartPage
        return CartPage(self.driver)
    
    def get_item_total(self):
        """Возвращает итоговую сумму товаров (текст)"""
        return self.get_text(self.ITEM_TOTAL)
    
    def get_total_with_tax(self):
        """Возвращает итоговую сумму с налогом"""
        return self.get_text(self.TOTAL)
    
    def finish_order(self):
        """Завершает оформление заказа"""
        self.click(self.FINISH_BUTTON)
    
    def get_complete_message(self):
        """Возвращает сообщение об успешном заказе"""
        return self.get_text(self.COMPLETE_HEADER)
    
    def back_home(self):
        """Возвращается на главную"""
        self.click(self.BACK_HOME_BUTTON)
        from pages.inventory_page import InventoryPage
        return InventoryPage(self.driver)
