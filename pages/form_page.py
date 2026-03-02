from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    ADD_TO_CART = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    CHECKOUT_BTN = (By.ID, "checkout")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")

    def add_item_and_start_checkout(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART)).click()
        self.wait.until(EC.element_to_be_clickable(self.CART_LINK)).click()
        self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BTN)).click()

    def fill_checkout_details(self, fname, lname, zip_code):
        # We use element_to_be_clickable even for input fields to ensure they are ready
        first_name_input = self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME))
        first_name_input.clear() # Best practice: clear before send_keys
        first_name_input.send_keys(fname)

        last_name_input = self.wait.until(EC.element_to_be_clickable(self.LAST_NAME))
        last_name_input.clear()
        last_name_input.send_keys(lname)

        zip_input = self.wait.until(EC.element_to_be_clickable(self.ZIP_CODE))
        zip_input.clear()
        zip_input.send_keys(zip_code)

        self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BTN)).click()