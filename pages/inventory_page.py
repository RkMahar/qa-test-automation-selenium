from selenium.webdriver.common.by import By


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, item_name):
        self.driver.find_element(By.CSS_SELECTOR, f"button[data-test='add-to-cart-{item_name}']").click()

    def get_cart_badge_count(self):
        return self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    def get_page_title(self):
        return self.driver.find_element(By.CLASS_NAME, "title").text
