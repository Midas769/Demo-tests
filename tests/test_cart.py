import pytest
from pages.login_page import LoginPage


class TestCart:
    """
    Тесты для проверки функциональности корзины.
    """
    
    @pytest.fixture(autouse=True)
    def setup(self, driver, base_url, test_user):
        """Выполняем вход перед каждым тестом"""
        login_page = LoginPage(driver)
        login_page.open(base_url)
        self.inventory_page = login_page.login(
            test_user["standard"]["username"],
            test_user["standard"]["password"]
        )
    
    def test_add_single_product_to_cart(self, driver):
        """Добавление одного товара в корзину"""
        # Добавляем товар
        self.inventory_page.add_product_to_cart("sauce-labs-backpack")
        
        # Проверяем, что количество в корзине = 1
        assert self.inventory_page.get_cart_count() == 1, "Количество товаров в корзине не равно 1"
    
    def test_add_multiple_products_to_cart(self, driver):
        """Добавление нескольких товаров в корзину"""
        products = ["sauce-labs-backpack", "sauce-labs-bike-light", "sauce-labs-bolt-t-shirt"]
        
        for product in products:
            self.inventory_page.add_product_to_cart(product)
        
        # Проверяем количество
        assert self.inventory_page.get_cart_count() == len(products), "Количество товаров не совпадает"
    
    def test_remove_product_from_cart(self, driver):
        """Удаление товара из корзины"""
        # Добавляем товар
        self.inventory_page.add_product_to_cart("sauce-labs-backpack")
        assert self.inventory_page.get_cart_count() == 1
        
        # Удаляем товар
        self.inventory_page.remove_product_from_cart("sauce-labs-backpack")
        assert self.inventory_page.get_cart_count() == 0, "Корзина не очистилась"
    
    def test_cart_page_shows_correct_items(self, driver):
        """Проверка, что в корзине отображаются правильные товары"""
        product_name = "sauce-labs-backpack"
        self.inventory_page.add_product_to_cart(product_name)
        
        # Открываем корзину
        cart_page = self.inventory_page.open_cart()
        
        # Проверяем, что товар есть в корзине
        item_names = cart_page.get_item_names()
        assert "Sauce Labs Backpack" in item_names, "Товар не найден в корзине"
        assert cart_page.get_cart_items_count() == 1, "Неверное количество товаров в корзине"
