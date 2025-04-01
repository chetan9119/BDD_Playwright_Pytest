Feature: Login to Practo
  As a user
  I want to navigate to the Practo homepage
  And click the login button

  Scenario: User clicks the login button
    Given the Practo homepage is open
    When I click the Login button
    Then I should see the login popup
