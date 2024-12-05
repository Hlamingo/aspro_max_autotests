import sys
sys.path.append('..')
from pages.login_page import LoginPage, LoginLocators
import pytest
import time
import allure

@pytest.fixture
def login_page(browser):
    """Фикстура для инициализации страницы входа."""
    return LoginPage(browser)
    
@allure.feature('Авторизация')
class TestLoginPage:
    """Проверка авторизации на сайте"""
    @allure.story('Открытие страницы входа')
    def test_01_open_page(self, login_page):
        """ Проверка успешного открытия страницы входа. """
        with allure.step('Открывает страницу'):
            login_page.open_page()
        title = 'Демоверсия Аспро: Максимум — готовый сайт на 1С-Битрикс'
        with allure.step('Проверяет загрузку страницы'):
            assert login_page.page_title() == title
    
    @allure.story('Открытие окна авторизации')
    def test_02_click_login_button(self, login_page):
        """ Проверка открытия окна авторизации """
        with allure.step('Кликает на кнопку "Войти"'):
            login_page.click_login_button()
        time.sleep(2)
        with allure.step('Проверяет отображение окна авторизации'):
            assert login_page.login_popup_is_displayed()
    
    @allure.story('Ввод логина')
    def test_03_login_enter(self, login_page):
        """ Проверка ввода логина """
        with allure.step('Вводит логин'):
            login_page.login_enter()
        time.sleep(1)
        with allure.step('Проверяет результат ввода логина'):
            assert login_page.checking_login_field() == LoginLocators.EMAIL
    
    @allure.story('Ввод пароля')
    def test_04_password_enter(self, login_page):
        """ Проверка ввода пароля """
        with allure.step('Вводит пароль'):
            login_page.password_enter()
        time.sleep(1)
        with allure.step('Проверяет результат ввода пароля'):
            assert login_page.checking_password_field() == LoginLocators.PASS
    
    @allure.story('Авторизация')
    def test_05_click_submit_button(self, login_page):
        """ Проверка авторизации """
        with allure.step('Кликает на кнопку "Войти"'):
            login_page.click_submit_button()
        with allure.step('Проверяет корректность входа'):
            assert not login_page.login_error()
    
    @allure.story('Проверка результата авторизации')
    def test_06_login_result(self, login_page):
        """ Проверка отображения личного кабинета """
        time.sleep(2)
        with allure.step('Проверяет результат авторизации'):
            assert login_page.login_result() == 'МОЙ КАБИНЕТ'
    
