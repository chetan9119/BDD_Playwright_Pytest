import pytest
from pytest_bdd import scenarios, given, when, then
from pages.base_page import PractoHomePage
import logging

logger = logging.getLogger(__name__)
# Load scenarios from the feature file
scenarios("../features/page.feature")

@pytest.fixture
def practo_home(page):
    """Fixture to initialize the Practo homepage."""
    return PractoHomePage(page)

@given("the Practo homepage is open")
def open_practo_home(practo_home):
    practo_home.open()
    logger.info("Home Page is opened successfully !")

@when("I click the Login button")
def click_login(practo_home):
    practo_home.click_login()
    logger.info("Navigated to Login Page")


@then("I should see the login popup")
def verify_login_popup(practo_home):
    assert practo_home.success, "Login popup not displayed"
    logger.info("Test Passed : Reached to Login Page")
