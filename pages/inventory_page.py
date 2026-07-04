from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def add_to_cart(self, item_name):
        btn = self.driver.find_element(By.CSS_SELECTOR, f"button[data-test='add-to-cart-{item_name}']")
        self.driver.execute_script("arguments[0].click();", btn)

    def get_cart_badge_count(self):
        return self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart_contents_container")))

    def get_page_title(self):
        return self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title"))).text
