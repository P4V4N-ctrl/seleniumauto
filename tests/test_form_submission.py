import pytest
from faker import Faker
from pages.login_page import LoginPage
from pages.form_page import FormPage

def test_checkout_form_submission(driver, setup_config):
    fake = Faker()
    login_page = LoginPage(driver)
    form_page = FormPage(driver)
    
    # Login if needed
    if "inventory" not in driver.current_url:
        driver.get(setup_config['base_url'])
        login_page.login(setup_config['username'], setup_config['password'])
    
    # This matches your STEP 2 & 3
    form_page.add_item_and_start_checkout()
    form_page.fill_checkout_details(fake.first_name(), fake.last_name(), fake.postcode())
    
    # This matches your STEP 4 (Validation)
    # Check that we reached the final overview or success page
    assert "checkout-step-two" in driver.current_url or "checkout-complete" in driver.current_url