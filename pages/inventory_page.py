from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class InventoryPage(BasePage):
    """
    Page Object для главной страницы (инвентарь).
    """
    
    # Локаторы
    PAGE_TITLE = (By.CLASS_NAME, "title")
    CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    PRODUCT_ITEMS = (By.CLASS_NAME, "inventory_item")
    
    # Шаблон для добавления конкретного товара (используем CSS)
    ADD_TO_CART_BUTTON_TEMPLATE = "[data-test='add-to-cart-{product_name}']"
    REMOVE_BUTTON_TEMPLATE = "[data-test='remove-{product_name}']"
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def get_title(self):
        """Возвращает заголовок страницы"""
        return self.get_text(self.PAGE_TITLE)
    
    def get_product_count(self):
        """Возвращает количество товаров на странице"""
        return len(self.driver.find_elements(*self.PRODUCT_ITEMS))
    
    def add_product_to_cart(self, product_name):
        """
        Добавляет товар в корзину по названию.
        product_name: например, "sauce-labs-backpack"
        """
        locator = (By.CSS_SELECTOR, self.ADD_TO_CART_BUTTON_TEMPLATE.format(product_name=product_name))
        self.click(locator)
    
    def remove_product_from_cart(self, product_name):
        """Удаляет товар из корзины"""
        locator = (By.CSS_SELECTOR, self.REMOVE_BUTTON_TEMPLATE.format(product_name=product_name))
        self.click(locator)
    
    def open_cart(self):
        """Открывает корзину"""
        self.click(self.CART_BUTTON)
        from pages.cart_page import CartPage
        return CartPage(self.driver)
    
    def get_cart_count(self):
        """Возвращает количество товаров в корзине"""
        if self.is_element_visible(self.CART_BADGE, timeout=2):
            return int(self.get_text(self.CART_BADGE))
        return 0
