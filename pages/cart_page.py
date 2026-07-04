from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def checkout(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "checkout")))
        self.driver.execute_script("document.getElementById('checkout').click()")
        self.wait.until(EC.presence_of_element_located((By.ID, "first-name")))

    def fill_checkout_info(self, first_name, last_name, zip_code):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(zip_code)

    def continue_checkout(self):
        self.driver.execute_script("document.getElementById('continue').click()")
        self.wait.until(EC.presence_of_element_located((By.ID, "finish")))

    def finish_checkout(self):
        self.driver.execute_script("document.getElementById('finish').click()")
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "complete-header")))

    def get_success_message(self):
        return self.driver.find_element(By.CLASS_NAME, "complete-header").text
