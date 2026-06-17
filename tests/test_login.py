import pytest
from pages.login_page import LoginPage


class TestLogin:
    """
    Тесты для проверки функциональности логина.
    """
    
    def test_login_with_valid_credentials(self, driver, base_url, test_user):
        """
        Позитивный сценарий: вход с корректными данными.
        Ожидаемый результат: переход на страницу с товарами.
        """
        login_page = LoginPage(driver)
        login_page.open(base_url)
        
        # Выполняем вход
        inventory_page = login_page.login(
            test_user["standard"]["username"],
            test_user["standard"]["password"]
        )
        
        # Проверяем, что перешли на страницу инвентаря
        assert "inventory.html" in driver.current_url, "Не удалось войти в систему"
        assert inventory_page.get_title() == "Products", "Заголовок страницы не соответствует"
        assert inventory_page.get_product_count() > 0, "Нет товаров на странице"
    
    def test_login_with_locked_user(self, driver, base_url, test_user):
        """
        Негативный сценарий: вход с заблокированным пользователем.
        Ожидаемый результат: сообщение об ошибке.
        """
        login_page = LoginPage(driver)
        login_page.open(base_url)
        
        login_page.login_without_redirect(
            test_user["locked"]["username"],
            test_user["locked"]["password"]
        )
        
        error_message = login_page.get_error_message()
        assert error_message is not None, "Сообщение об ошибке не появилось"
        assert "locked out" in error_message, "Сообщение об ошибке не соответствует ожидаемому"
    
    @pytest.mark.parametrize("username,password,expected_error", [
        ("", "secret_sauce", "Username is required"),
        ("standard_user", "", "Password is required"),
        ("invalid_user", "invalid_pass", "Username and password do not match"),
    ])
    def test_login_with_invalid_credentials(self, driver, base_url, username, password, expected_error):
        """
        Негативные сценарии: проверка валидации полей.
        Используем параметризацию для проверки разных случаев.
        """
        login_page = LoginPage(driver)
        login_page.open(base_url)
        
        login_page.login_without_redirect(username, password)
        
        error_message = login_page.get_error_message()
        assert error_message is not None, "Сообщение об ошибке не появилось"
        assert expected_error in error_message, f"Ожидалось '{expected_error}', получено '{error_message}'"
    
    def test_login_page_elements_visible(self, driver, base_url):
        """
        Проверка отображения всех элементов на странице логина.
        """
        login_page = LoginPage(driver)
        login_page.open(base_url)
        
        # Проверяем, что все поля и кнопки видны
        assert login_page.is_element_visible(login_page.USERNAME_INPUT), "Поле Username не видно"
        assert login_page.is_element_visible(login_page.PASSWORD_INPUT), "Поле Password не видно"
        assert login_page.is_element_visible(login_page.LOGIN_BUTTON), "Кнопка Login не видна"
        assert login_page.is_login_page_loaded(), "Страница логина не загружена полностью"
