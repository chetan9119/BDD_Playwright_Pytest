from playwright.sync_api import Page

class PractoHomePage:
    def __init__(self, page: Page):
        self.page = page
        self.login_button = page.locator("text=Login")  # Locating the 'Login' button by text
        self.success = page.locator("a#loginLink")
    
    def open(self):
        """Navigates to the Practo homepage."""
        self.page.goto("https://www.practo.com/")
    
    def click_login(self):
        """Clicks the Login button."""
        self.login_button.click()
        self.page.wait_for_timeout(3000)
