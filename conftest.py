import pytest
import json
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

@pytest.fixture(scope="session")
def setup_config():
    with open('config/config.json') as f:
        return json.load(f)

# CHANGE: scope is now "session" so it opens once for all tests
@pytest.fixture(scope="session") 
def driver(setup_config):
    options = webdriver.ChromeOptions()
    
    # Keeps the browser open after the script ends
    options.add_experimental_option("detach", True)
    
    # options.add_argument("--headless") # Uncomment for bonus points Task 6
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    
    yield driver
    
    # In a real production environment, we would use driver.quit()
    # For your debugging, we leave it commented out
    # driver.quit() 

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        # Get the driver from the session-scoped fixture
        driver = item.funcargs.get("driver")
        if driver:
            if not os.path.exists("screenshots"):
                os.makedirs("screenshots")
            file_name = f"screenshots/{item.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            driver.save_screenshot(file_name)