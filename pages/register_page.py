import sys
sys.path.append('..')
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
import os

class RegisterLocators:
    
    YOUR_CITY = (By.CSS_SELECTOR, '[data-id="3213"]')
    REGISTER_NAME = (By.ID, 'input_NAME')
    REGISTER_EMAIL = (By.ID, 'input_EMAIL')
    REGISTER_PERSONAL_PHONE = (By.ID, 'input_PERSONAL_PHONE')
    REGISTER_PASSWORD = (By.ID, 'input_PASSWORD')
    REGISTER_CONFIRM_PASSWORD = (By.ID, 'input_CONFIRM_PASSWORD')
    CHECKBOX_LICENSES_REGISTER = (By.ID, 'licenses_register')
    SUBMIT_BUTTON = (By.NAME, 'register_submit_button1')
    REGISTER_ERROR = (By.CLASS_NAME, 'errortext')
    # Данные для регистрации
    EMAIL = os.getenv('ASPRO_LOGIN')
    PASS = os.getenv('ASPRO_PASS')
    PHONE = os.getenv('ASPRO_PHONE')
    
class RegisterPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = 'https://max-demo.ru/auth/registration/?register=yes&backurl=/'

    def click_your_city(self):
        """ Закрывает попап Ваш город ... ? """
        try:
            your_city_popup = self.find_elements(RegisterLocators.YOUR_CITY)
            if your_city_popup:
                return your_city_popup[1].click()
            else:
                pass
        except TimeoutException:
            pass

    def register_name_field(self):
        """ Вводит ФИО """
        return self.find_element(
            RegisterLocators.REGISTER_NAME).send_keys(
            'ТЕСТ'
            )
        
    def register_email_field(self):
        """ Вводит email """
        return self.find_element(
            RegisterLocators.REGISTER_EMAIL).send_keys(
                RegisterLocators.EMAIL
            )
    # ~ 'qa.test.2025@mail.ru'
    def register_phone_field(self):
        """ Вводит номер телефона """
        return self.find_element(
            RegisterLocators.REGISTER_PERSONAL_PHONE).send_keys(
                RegisterLocators.PHONE
            )
    
    def register_password_field(self):
        """ Вводит пароль """
        return self.find_element(
            RegisterLocators.REGISTER_PASSWORD).send_keys(
                RegisterLocators.PASS
            )
    
    def register_confirm_password(self):
        """ Подтверждает пароль """
        return self.find_element(
            RegisterLocators.REGISTER_CONFIRM_PASSWORD).send_keys(
                RegisterLocators.PASS
            )
    
    def confirm_licenses_register(self):
        """ Кликает на чекбокс согласия обработки персональных дан. """
        checkbox = self.find_element(
            RegisterLocators.CHECKBOX_LICENSES_REGISTER
        )
        return self.checkbox_click(checkbox)
        
    def click_register_submit_button (self):
        """ Кликает на кнопку Зарегистрироваться """
        submit = self.find_element(RegisterLocators.SUBMIT_BUTTON)
        self.scroll_into_view(submit)
        time.sleep(2)
        return submit.click()
        
    def register_error (self):
        """ Извлекает текст ошибки ругистрации"""
        try:
            return self.find_element(
                RegisterLocators.REGISTER_ERROR
                ).text
        except TimeoutException:
            return False
        
