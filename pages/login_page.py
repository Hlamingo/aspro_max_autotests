import sys
sys.path.append('..')
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import os

class LoginLocators:
    """ Локаторы для главной страницы """
    LOG_IN = (By.CLASS_NAME, 'auth_wr_inner')
    AUTH_FORM_POPUP = (By.ID, 'wrap_ajax_auth')
    USER_LOGIN_FIELD = (By.ID, 'USER_LOGIN_POPUP')
    USER_PASSWORD_FIELD = (By.ID, 'USER_PASSWORD_POPUP')
    SUBMIT_BUTTON = (By.NAME, 'Login1')
    LOGIN_ERROR = (By.CLASS_NAME, 'alert.alert-danger.compact')
    AUTH_RESULT = (By.XPATH, '//span[text()="Мой кабинет"]')
    # Данные для авторизации
    EMAIL = os.getenv('ASPRO_LOGIN')
    PASS = os.getenv('ASPRO_PASS')
    
class LoginPage(BasePage):
    """ Страница авторизации """
    def __init__(self, driver):
        super().__init__(driver)
        
    def page_title(self):
        """Извлекает название страницы и возварщает текст"""
        return self.driver.title
        
    def click_login_button(self):
        """Находит кнопку 'Войти' и кликает её"""
        button = self.find_elements(LoginLocators.LOG_IN)
        if button[1].is_displayed() and button[1].is_enabled():
            button[1].click()
        else:
            raise Exception('Кнопка "Войти" недоступна')
        
    def login_popup_is_displayed(self):
        """ Взвращает результат отображения окна авторизации """
        login_popup = self.find_element(LoginLocators.AUTH_FORM_POPUP)
        return login_popup.is_displayed()
    
    def login_enter(self):
        """ Вводит лоин """
        self.find_element(LoginLocators.USER_LOGIN_FIELD).send_keys(
                LoginLocators.EMAIL
            )
        
    def checking_login_field(self):
        """ Возвращает значения в поле 'Логин' """
        login_field = self.find_element(LoginLocators.USER_LOGIN_FIELD)
        return self.get_attribute(login_field)
        
    def password_enter(self):
        """ Вводит пароль """
        self.find_element(LoginLocators.USER_PASSWORD_FIELD).send_keys(
                LoginLocators.PASS
            )
    
    def checking_password_field(self):
        """ Возвращает значения в поле 'Пароль' """
        password_field = self.find_element(
            LoginLocators.USER_PASSWORD_FIELD
        )
        return self.get_attribute(password_field)
        
    def click_submit_button(self):
        """ Кликает кнопку 'Войти' """
        return self.find_element(LoginLocators.SUBMIT_BUTTON).click()
        
    def login_error(self):
        """ Возвращает False в случае ошибки """
        try:
            return self.find_element(LoginLocators.LOGIN_ERROR).text
        except TimeoutException:
            return False
    
    def login_result(self):
        """ Возвращает заголовок страницы после успешной авторизации """
        my_cabinet = self.find_elements(LoginLocators.AUTH_RESULT)
        return my_cabinet[1].text
