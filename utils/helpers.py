import random
import string


def generate_random_email():
    """Генерирует случайный email для тестов"""
    letters = string.ascii_lowercase
    random_part = ''.join(random.choice(letters) for _ in range(8))
    return f"{random_part}@testmail.com"


def generate_random_string(length=8):
    """Генерирует случайную строку"""
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))


def get_price_as_float(price_text):
    """Извлекает число из строки с ценой"""
    # Пример: "$29.99" -> 29.99
    return float(price_text.replace('$', ''))
