import sys
sys.path.append('..')
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://max-demo.ru/'
        
    def open_page(self):
        """ Открывает страницу по URL. """
        return self.driver.get(self.base_url)
        
    def find_element(self, locator, time=10):
        """ Ищет элементы на странице и возвращает его """
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator)
            )
        
    def find_elements(self, locator, time=10):
        """ Ищет элементы на странице и возвращает список элементов """
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator)
            )
            
    def get_attribute(self, element):
        """ Получает введенное значение из поля"""
        return element.get_attribute('value')
    
    def scroll_into_view (self, element):
        """ Прокручивает страницу до элемента """
        return self.driver.execute_script(
            "arguments[0].scrollIntoView();", element
            )
    
    def scroll_to(self):
        """ Прокручивает вниз до конца страницы """
        return self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
            )
    
    def checkbox_click(self, checkbox):
        """ Кликает на чекбокс """
        return self.driver.execute_script(
            "arguments[0].click();", checkbox
            )
