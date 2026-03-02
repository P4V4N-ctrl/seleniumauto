from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        # Task 3: Use Explicit Waits instead of static sleeps
        self.wait = WebDriverWait(driver, 10)
        
    # Locators (Task 4: POM implementation)
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    INVENTORY_CONTAINER = (By.ID, "inventory_container") # Used to verify success

    def login(self, username, password):
        """
        Performs the login flow and waits for the dashboard to confirm success.
        """
        # 1. Wait for fields and enter credentials
        self.wait.until(EC.visibility_of_element_located(self.USERNAME_FIELD)).send_keys(username)
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD_FIELD)).send_keys(password)
        
        # 2. Click the login button
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()
        
        # 3. CRITICAL: Wait for the URL to contain 'inventory' 
        # This prevents the "jumping back to login" issue by ensuring the session is loaded.
        self.wait.until(EC.url_contains("inventory"))
        
        # 4. Task 2 & 3 Verification: Ensure a dashboard element is present
        self.wait.until(EC.presence_of_element_located(self.INVENTORY_CONTAINER))

    def is_logged_in(self):
        """
        Helper method to check if the session is still active.
        """
        return "inventory" in self.driver.current_url