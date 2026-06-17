import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


@pytest.fixture(scope="function")  # scope="function" — новый драйвер для каждого теста
def driver(request):
    """
    Фикстура для создания и закрытия WebDriver.
    Поддерживает Chrome и Firefox (можно выбрать через параметры).
    """
    browser = request.config.getoption("--browser", default="chrome").lower()
    
    logger.info(f"Запуск браузера: {browser}")
    
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Убрать эту строку, чтобы видеть браузер
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        # Запускаем драйвер через webdriver-manager
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )
    
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        # options.add_argument("--headless")
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options
        )
    
    else:
        raise ValueError(f"Браузер '{browser}' не поддерживается")
    
    driver.maximize_window()
    driver.implicitly_wait(10)  # Ожидание элементов до 10 секунд
    
    logger.info("Драйвер создан")
    
    yield driver  # Передаем драйвер в тест
    
    # После завершения теста:
    logger.info("Закрытие драйвера")
    driver.quit()


@pytest.fixture(scope="session")
def base_url():
    """Базовый URL для тестирования"""
    return "https://www.saucedemo.com/"


@pytest.fixture
def test_user():
    """Тестовые данные пользователя"""
    return {
        "standard": {"username": "standard_user", "password": "secret_sauce"},
        "locked": {"username": "locked_out_user", "password": "secret_sauce"},
        "problem": {"username": "problem_user", "password": "secret_sauce"},
        "performance": {"username": "performance_glitch_user", "password": "secret_sauce"},
    }


# ========== Параметры командной строки ==========

def pytest_addoption(parser):
    """Добавляем параметр --browser для выбора браузера"""
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Выбор браузера: chrome или firefox"
    )


@pytest.fixture
def browser_name(request):
    """Возвращает имя браузера для использования в тестах"""
    return request.config.getoption("--browser")
