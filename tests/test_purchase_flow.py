import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


class TestPurchaseFlow:
    def test_add_item_and_view_cart(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()

        inventory = InventoryPage(driver)
        assert inventory.get_page_title() == "Products"
        inventory.add_to_cart("sauce-labs-backpack")
        assert inventory.get_cart_badge_count() == "1"

    def test_checkout_page_loads(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()

        inventory = InventoryPage(driver)
        inventory.add_to_cart("sauce-labs-backpack")
        inventory.go_to_cart()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "checkout")))
        driver.execute_script("document.getElementById('checkout').click()")
        first_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "first-name")))
        assert first_name.is_displayed()

    def test_add_multiple_items(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()

        inventory = InventoryPage(driver)
        inventory.add_to_cart("sauce-labs-backpack")
        inventory.add_to_cart("sauce-labs-bike-light")
        assert inventory.get_cart_badge_count() == "2"
