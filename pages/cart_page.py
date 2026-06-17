from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    """
    Page Object для страницы корзины.
    """
    
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    REMOVE_BUTTON_TEMPLATE = "[data-test='remove-{product_name}']"
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def get_cart_items_count(self):
        """Возвращает количество товаров в корзине"""
        return len(self.driver.find_elements(*self.CART_ITEMS))
    
    def remove_item(self, product_name):
        """Удаляет товар из корзины"""
        locator = (By.CSS_SELECTOR, self.REMOVE_BUTTON_TEMPLATE.format(product_name=product_name))
        self.click(locator)
    
    def proceed_to_checkout(self):
        """Переходит к оформлению заказа"""
        self.click(self.CHECKOUT_BUTTON)
        from pages.checkout_page import CheckoutPage
        return CheckoutPage(self.driver)
    
    def continue_shopping(self):
        """Возвращается к покупкам"""
        self.click(self.CONTINUE_SHOPPING_BUTTON)
        from pages.inventory_page import InventoryPage
        return InventoryPage(self.driver)
    
    def get_item_names(self):
        """Возвращает список названий товаров в корзине"""
        items = self.driver.find_elements(*self.ITEM_NAME)
        return [item.text for item in items]
