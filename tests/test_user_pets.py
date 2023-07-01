import pytest
from selenium.webdriver.common.by import By
from settings import valid_email, valid_password

# Задаем количество питомцев из статистики профиля
num_of_pets: int = 51

def test_user_pets():
    """Проверка, что количество питомцев соответствует статистике из профиля"""
    pytest.driver.implicitly_wait(5)

    # Получаем всех питомцев
    pets = pytest.driver.find_elements(By.CSS_SELECTOR, '#all_my_pets > table > tbody > tr')

    # Проверяем что все питомцы на месте
    assert len(pets) == num_of_pets


def test_pets_photo():
    """Проверка, что хотя бы у половины питомцев в профиле есть фото"""

    pytest.driver.implicitly_wait(5)

    # Получаем все фото питомцев
    images = pytest.driver.find_elements(By.CSS_SELECTOR, '#all_my_pets > table > tbody > tr > th > img')

    # Считаем колличество карточек без фото
    pets_without_photo = 0
    for i in range(len(images)):
        if images[i].get_attribute('src') == '':
            pets_without_photo += 1
    # Проверяем что хотя бы у половины питомцев есть фото
    assert pets_without_photo <= num_of_pets // 2


def test_pets_params():
    """Проверка, что у всех питомцев есть имя, порода и возраст"""

    pytest.driver.implicitly_wait(5)

    # Получаем все имена питомцев
    names = pytest.driver.find_elements(By.CSS_SELECTOR, '#all_my_pets > table > tbody > tr > td:nth-child(2)')
    # Получаем все породы питомцев
    breeds = pytest.driver.find_elements(By.CSS_SELECTOR, '#all_my_pets > table > tbody > tr > td:nth-child(3)')
    # Получаем возраста всех питомцев
    ages = pytest.driver.find_elements(By.CSS_SELECTOR, '#all_my_pets > table > tbody > tr > td:nth-child(4)')

    for i in range(len(names)):
        # Проверяем что у всех питомцев есть имя, порода и возраст
        assert names[i].text != ''
        assert breeds[i].text != ''
        assert ages[i].text != ''


def test_pets_names():
    """Проверка, что имена питомцев не повторяются"""

    pytest.driver.implicitly_wait(5)

    # Получаем все имена питомцев
    names = pytest.driver.find_elements(By.CSS_SELECTOR, '#all_my_pets > table > tbody > tr > td:nth-child(2)')

    # Сверяем имена
    for i in range(len(names)):
        for j in range(len(names)):
            assert names[i] != names[j]


def test_pets_repeats():
    """Проверка, что в списке нет повторяющихся питомцев"""

    pytest.driver.implicitly_wait(5)

    # Получаем все имена питомцев
    names = pytest.driver.find_elements(By.CSS_SELECTOR, '#all_my_pets > table > tbody > tr > td:nth-child(2)')
    # Получаем все породы питомцев
    breeds = pytest.driver.find_elements(By.CSS_SELECTOR, '#all_my_pets > table > tbody > tr > td:nth-child(3)')
    # Получаем возраста всех питомцев
    ages = pytest.driver.find_elements(By.CSS_SELECTOR, '#all_my_pets > table > tbody > tr > td:nth-child(4)')

    for i in range(len(names)):
        for j in range(len(names)):
            assert names[i] != names[j] and breeds[i] != breeds[j] and ages[i] != ages[j]
