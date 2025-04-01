from playwright.sync_api import Page

class PractoLoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("input[name='username']")  # Verify exact selector
        self.password_input = page.locator("input[name='password']")
        self.submit_button = page.locator("button:has-text('Login')")
        self.error_message_1 = page.locator('span#usernameErrorBlock')
        self.error_message_2 = page.locator('span#passwordErrorBlock')

    def fill_credentials(self, username, password):
        """Fills in the login form."""
        self.username_input.type(username)
        self.password_input.type(password)
        
    def open(self):
        """Navigates to the Practo homepage."""
        self.page.goto("https://accounts.practo.com/login?next=%2Fcheckid_request&intent=fabric")

        
    def logout(self):
        self.page.locator('span.icon-ic_down_cheveron').nth(4).click()
        self.page.get_by_role('link', name="Logout").click()
        self.page.wait_for_timeout(2000)

    def submit(self):
        """Clicks the login button."""
        self.submit_button.wait_for()
        self.submit_button.click()

    def is_profile_name_loaded(self) -> bool:
        """Checks if dashboard is loaded after login."""
        return self.page.locator('span.user_info_top')

    def is_error_displayed(self) -> bool:
        """Checks if an error message is displayed."""
        return self.error_message_1 or self.error_message_1
