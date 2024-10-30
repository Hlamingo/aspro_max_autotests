import sys
sys.path.append('..')
from pages.login_page import LoginPage, LoginLocators
import pytest
import time

@pytest.fixture
def login_page(browser):
    """Фикстура для инициализации страницы входа."""
    return LoginPage(browser)
    
def test_open_page(login_page):
    """ Проверка успешного открытия страницы входа. """
    login_page.open_page()
    # title - это название страницы 
    title = 'Демоверсия Аспро: Максимум — готовый сайт на 1С-Битрикс'
    assert login_page.page_title() == title

def test_click_login_button(login_page):
    """ Проверка открытия окна авторизации """
    login_page.click_login_button()
    time.sleep(2)
    assert login_page.login_popup_is_displayed()
    
def test_login_enter(login_page):
    """ Проверка ввода логина """
    login_page.login_enter()
    time.sleep(1)
    assert login_page.checking_login_field() == LoginLocators.EMAIL
    
def test_password_enter(login_page):
    """ Проверка ввода пароля """
    login_page.password_enter()
    time.sleep(1)
    assert login_page.checking_password_field() == LoginLocators.PASS
    
def test_click_submit_button(login_page):
    """ Проверка авторизации """
    login_page.click_submit_button()
    assert not login_page.login_error()
    
def test_login_result(login_page):
    """ Проверка отображения личного кабинета """
    time.sleep(2)
    assert login_page.login_result() == 'МОЙ КАБИНЕТ'
