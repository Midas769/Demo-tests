# Данные для тестов
VALID_USERS = {
    "standard_user": {"username": "standard_user", "password": "secret_sauce"},
    "problem_user": {"username": "problem_user", "password": "secret_sauce"},
    "performance_glitch_user": {"username": "performance_glitch_user", "password": "secret_sauce"},
}

LOCKED_USER = {"username": "locked_out_user", "password": "secret_sauce"}

PRODUCTS = {
    "backpack": "sauce-labs-backpack",
    "bike_light": "sauce-labs-bike-light",
    "bolt_tshirt": "sauce-labs-bolt-t-shirt",
    "fleece_jacket": "sauce-labs-fleece-jacket",
    "onesie": "sauce-labs-onesie",
    "tshirt_red": "test.allthethings()-t-shirt-(red)",
}

CUSTOMER_INFO = {
    "valid": {"first_name": "John", "last_name": "Doe", "zip": "12345"},
    "invalid": {"first_name": "", "last_name": "", "zip": ""},
}
