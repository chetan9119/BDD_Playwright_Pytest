import pytest
from playwright.sync_api import sync_playwright
import pytest_html


@pytest.fixture(scope="session")
def browser():
    """Launch the Playwright browser instance."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # Set headless=True for CI/CD
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    """Create a new page instance for each test."""
    page = browser.new_page()
    yield page
    page.close()
    

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Take screenshot on test failure"""
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            screenshot_path = f"reports/screenshots/{item.name}.png"
            page.screenshot(path=screenshot_path)
            with open(screenshot_path, "rb") as f:
                report.extra = getattr(report, "extra", [])
                report.extra.append(pytest_html.extras.png(f.read(), "Screenshot"))
