import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from pages.base_page import PractoHomePage
from pages.login_page import PractoLoginPage
import logging
import os
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)
scenarios("../features/login.feature")

@pytest.fixture
def practo_home(page):
    """Fixture to initialize the Practo homepage."""
    logger.info("Opening the browser")
    return PractoHomePage(page)

@pytest.fixture
def practo_login(page):
    """Fixture to initialize the Practo login page."""
    return PractoLoginPage(page)

@given("the Practo homepage is open")
def open_practo_home(practo_home):
    logger.info("Navigated to Home Page")
    practo_home.open()

@when("I click the Login button")
def click_login(practo_home):
    logger.info("Clicking login button")
    practo_home.click_login()

@when("I enter valid credentials")
def enter_valid_credentials(practo_login):
    """This step now correctly captures username/password from the feature file."""
    logger.info("Entering Valid Username and Password")
    email = os.getenv("VALID_USER")
    password = os.getenv("VALID_PASSWORD")
    practo_login.fill_credentials(str({email}), str({password}))
    logger.info("Logging in ...")
    practo_login.submit()
    logger.info("Test Passed : Logged in Successfully !")
    practo_login.page.wait_for_timeout(2000)


@when("I enter invalid credentials")
def enter_invalid_credentials(practo_login):
    """Same fix applied for invalid credentials."""
    logger.info("Entering Invalid Username and Password !")
    email = os.getenv("INVALID_USER")
    password = os.getenv("INVALID_PASSWORD")
    practo_login.fill_credentials(str({email}), str({password}))
    logger.info("Logging in ...")
    practo_login.submit()
    logger.info("Test Passed : Invalid Credentials !")
    practo_login.page.wait_for_timeout(2000)

@then("I should be redirected to the dashboard")
def verify_dashboard(practo_login):
    assert practo_login.is_profile_name_loaded(), "Dashboard did not load"
    logger.info("Test Passed : Profile Section is available")
    practo_login.page.wait_for_timeout(500)
    logger.info("Logged Out")

@then("I should see an error message")
def verify_error_message(practo_login):
    assert practo_login.is_error_displayed(), "Error message not displayed"
    logger.info("Test Passed : Unable to login")