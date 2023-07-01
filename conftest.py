from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from settings import valid_email, valid_password


@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.add_argument('--window-size 800,600')


@pytest.fixture(autouse=True)
def browser():
    service = Service('/chromedriver/')
    pytest.driver = webdriver.Chrome(service=service)
    pytest.driver.get('http://petfriends.skillfactory.ru/login')
    pytest.driver.find_element(By.ID, 'email').send_keys(valid_email)
    pytest.driver.find_element(By.ID, 'pass').send_keys(valid_password)
    submit_button = WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, \
                                                                               'button[type="submit"]')))
    submit_button.click()
    navbar = WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, \
                                                                                     '.navbar-toggler-icon')))
    navbar.click()
    my_pets_page = WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,\
                                                                                    'a.nav-link[href="/my_pets"]')))
    my_pets_page.click()

    yield

    pytest.driver.quit()
