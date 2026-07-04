import pytest
from pages.login_page import LoginPage


class TestLogin:
    def test_successful_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()
        assert login_page.is_inventory_displayed()

    def test_failed_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.enter_username("invalid_user")
        login_page.enter_password("wrong_password")
        login_page.click_login()
        error = login_page.get_error_message()
        assert "Username and password do not match" in error

    def test_empty_username(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.enter_password("secret_sauce")
        login_page.click_login()
        error = login_page.get_error_message()
        assert "Username is required" in error
