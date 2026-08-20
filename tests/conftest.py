import pytest
import random

# создали функцию для генерации логина
def generate_random_email():
    cohort_id = random.randint(100, 999)
    return f"beepbeep_{cohort_id}@ya.ru"

# создали функцию для генерации валидного пароля
def generate_random_password():
    return str(random.randint(100000, 999999))

# создали фикстуру для генерации данных
@pytest.fixture
def user_data():
    return {
        "email": generate_random_email(),
        "password": generate_random_password()
    }

# создали фикстуру для зарегистрированного пользователя
@pytest.fixture
def existing_user():
    return {
        "email": "beepbeep111@ya.ru",
        "password": "123456"
    }