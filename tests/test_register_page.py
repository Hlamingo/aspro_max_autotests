import sys
sys.path.append('..')
from pages.register_page import RegisterPage, RegisterLocators
import time
import pytest

@pytest.fixture
def register_page(browser):
    """ Фикстура для инициализации страницы входа."""
    return RegisterPage(browser)

def test_01_open_register_page(register_page):
    register_page.open_page()
    assert register_page.page_title() == 'Регистрация'
    register_page.click_your_city()
    time.sleep(1)
    
def test_02_register_name_field(register_page):
    """ Проверка ввода ФИО """
    register_page.register_name_field()
    assert register_page.checking_field(
        RegisterLocators.REGISTER_NAME
        ) == 'ТЕСТ'
    
def test_03_register_email_field(register_page):
    """ Проверка ввода email """
    register_page.register_email_field()
    assert register_page.checking_field(
        RegisterLocators.REGISTER_EMAIL
    ) == RegisterLocators.EMAIL
    
def test_04_register_phone_field(register_page):
    """ Проверка ввода Телефона """
    register_page.register_phone_field()
    assert register_page.checking_field(
        RegisterLocators.REGISTER_PERSONAL_PHONE
    ) == RegisterLocators.PHONE
    
def test_05_register_password_field(register_page):
    """ Проверка ввода Пароля """
    register_page.register_password_field()
    assert register_page.checking_field(
        RegisterLocators.REGISTER_PASSWORD
    ) == RegisterLocators.PASS
    
def test_06_confirm_password(register_page):
    """ Проверка ввода подтверждения пароля """
    register_page.register_confirm_password()
    assert register_page.checking_field(
        RegisterLocators.REGISTER_CONFIRM_PASSWORD
    ) == RegisterLocators.PASS
    
def test_07_confirm_licenses_register(register_page):
    """ Проверка установки чекбокса Согласие на обработку ПД """
    register_page.confirm_licenses_register()
    assert register_page.checking_confirm_licenses_register() is True
    
def test_08_click_register_submit_button(register_page):
    """ Проверки результата регистрации """
    register_page.click_register_submit_button()
    assert not register_page.register_error()
    time.sleep(2)
