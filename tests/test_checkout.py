import pytest
from pages.login_page import LoginPage


class TestCheckout:
    """
    Тесты для проверки оформления заказа.
    """
    
    @pytest.fixture(autouse=True)
    def setup(self, driver, base_url, test_user):
        """Выполняем вход и добавляем товар перед каждым тестом"""
        login_page = LoginPage(driver)
        login_page.open(base_url)
        self.inventory_page = login_page.login(
            test_user["standard"]["username"],
            test_user["standard"]["password"]
        )
        # Добавляем товар в корзину
        self.inventory_page.add_product_to_cart("sauce-labs-backpack")
        self.cart_page = self.inventory_page.open_cart()
    
    def test_complete_checkout_flow(self, driver):
        """Полный сценарий оформления заказа"""
        # Переходим к оформлению
        checkout_page = self.cart_page.proceed_to_checkout()
        
        # Заполняем информацию
        checkout_page.fill_customer_info("John", "Doe", "12345")
        checkout_page.continue_checkout()
        
        # Проверяем, что на шаге обзора
        assert "checkout-step-two" in driver.current_url, "Не перешли на шаг обзора"
        
        # Проверяем расчеты
        item_total = checkout_page.get_item_total()
        assert "29.99" in item_total or "32.97" in item_total, "Некорректная итоговая сумма"
        
        # Завершаем заказ
        checkout_page.finish_order()
        
        # Проверяем успешное завершение
        complete_message = checkout_page.get_complete_message()
        assert "Thank you for your order" in complete_message, "Заказ не был оформлен"
    
    def test_checkout_with_empty_fields(self, driver):
        """Оформление с пустыми полями"""
        checkout_page = self.cart_page.proceed_to_checkout()
        
        # Не заполняем поля, сразу нажимаем Continue
        checkout_page.continue_checkout()
        
        # Проверяем, что остались на той же странице (валидация)
        assert "checkout-step-one" in driver.current_url, "Сработала валидация пустых полей"
    
    def test_cancel_checkout(self, driver):
        """Отмена оформления заказа"""
        checkout_page = self.cart_page.proceed_to_checkout()
        
        # Нажимаем Cancel
        cart_page = checkout_page.cancel_checkout()
        
        # Проверяем, что вернулись в корзину
        assert "cart" in driver.current_url, "Не вернулись в корзину"
        assert cart_page.get_cart_items_count() == 1, "Товар пропал из корзины"
