import random

# создали функцию для генерации логина
def generate_random_email():
    cohort_id = random.randint(100, 999)
    return f"beepbeep_{cohort_id}@ya.ru"

# создали функцию для генерации валидного пароля
def generate_random_password():
    return str(random.randint(100000, 999999))