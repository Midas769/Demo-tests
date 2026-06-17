from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    """
    Page Object для страницы авторизации.
    """
    
    # Локаторы (способ найти элемент на странице)
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    BOT_IMAGE = (By.CLASS_NAME, "bot_column")  # Декоративный элемент для проверки загрузки страницы
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def login(self, username, password):
        """
        Выполняет вход в систему.
        Возвращает объект InventoryPage после успешного входа.
        """
        from pages.inventory_page import InventoryPage  # Импорт здесь, чтобы избежать циклической зависимости
        
        self.send_keys(self.USERNAME_INPUT, username)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        
        # Возвращаем страницу с товарами
        return InventoryPage(self.driver)
    
    def login_without_redirect(self, username, password):
        """
        Выполняет вход, но НЕ возвращает следующую страницу.
        Используется для негативных сценариев.
        """
        self.send_keys(self.USERNAME_INPUT, username)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
    
    def get_error_message(self):
        """Возвращает текст ошибки, если она есть"""
        if self.is_element_visible(self.ERROR_MESSAGE):
            return self.get_text(self.ERROR_MESSAGE)
        return None
    
    def is_login_page_loaded(self):
        """Проверяет, загрузилась ли страница логина"""
        return self.is_element_visible(self.BOT_IMAGE, timeout=5)
    
    def clear_fields(self):
        """Очищает поля ввода"""
        self.driver.find_element(*self.USERNAME_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
