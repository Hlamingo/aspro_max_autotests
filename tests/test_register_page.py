import sys
sys.path.append('..')
from pages.register_page import RegisterPage
import time

def test_register_page(browser):
    register_page = RegisterPage(browser)
    register_page.open_page()
    register_page.click_your_city()
    register_page.register_name_field()
    register_page.register_email_field()
    register_page.register_phone_field()
    register_page.register_password_field()
    register_page.register_confirm_password()
    register_page.confirm_licenses_register()
    register_page.click_register_submit_button()
    assert not register_page.register_error()
    time.sleep(10)
