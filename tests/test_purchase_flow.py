import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


class TestPurchaseFlow:
    def test_full_purchase_flow(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()

        inventory = InventoryPage(driver)
        assert inventory.get_page_title() == "Products"
        inventory.add_to_cart("sauce-labs-backpack")
        assert inventory.get_cart_badge_count() == "1"
        inventory.go_to_cart()

        cart = CartPage(driver)
        cart.checkout()
        cart.fill_checkout_info("John", "Doe", "12345")
        cart.continue_checkout()
        cart.finish_checkout()

        success = cart.get_success_message()
        assert "Thank you for your order" in success

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
