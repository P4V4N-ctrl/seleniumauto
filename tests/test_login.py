import pytest
from pages.login_page import LoginPage

def test_login_positive(driver, setup_config):
    login_page = LoginPage(driver)
    
    # 1. Check if we are already logged in
    # If we are already on the inventory page, we can skip the login steps
    if "inventory" not in driver.current_url:
        driver.get(setup_config['base_url']) # Task 2: Navigate to login [cite: 18]
        
        # Task 2: Enter credentials from config.json and click login [cite: 19, 20]
        login_page.login(setup_config['username'], setup_config['password'])
    
    # 2. Task 3: Implement proper assertions [cite: 29]
    # This verifies successful login by checking the URL or dashboard element [cite: 21]
    assert "inventory" in driver.current_url, "Login failed: Dashboard not reached"