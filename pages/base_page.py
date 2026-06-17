from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import logging

logger = logging.getLogger(__name__)


class BasePage:
    """
    Базовый класс для всех Page Objects.
    Содержит общие методы для работы с элементами.
    """
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=0.5)
    
    def open(self, url):
        """Открывает URL в браузере"""
        logger.info(f"Открываем страницу: {url}")
        self.driver.get(url)
    
    def click(self, locator):
        """Ожидает элемент и кликает по нему"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        logger.info(f"Клик по элементу: {locator}")
    
    def send_keys(self, locator, text):
        """Ожидает элемент и вводит текст"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)
        logger.info(f"Ввод текста в элемент: {locator}")
    
    def get_text(self, locator):
        """Возвращает текст элемента"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text
    
    def is_element_visible(self, locator, timeout=10):
        """Проверяет, виден ли элемент на странице"""
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
    
    def is_element_present(self, locator, timeout=5):
        """Проверяет, присутствует ли элемент в DOM"""
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False
    
    def get_current_url(self):
        """Возвращает текущий URL"""
        return self.driver.current_url
    
    def take_screenshot(self, name="screenshot"):
        """Делает скриншот страницы"""
        screenshot_path = f"{name}.png"
        self.driver.save_screenshot(screenshot_path)
        logger.info(f"Скриншот сохранен: {screenshot_path}")
        return screenshot_path
