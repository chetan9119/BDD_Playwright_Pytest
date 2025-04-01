Feature: Login to Practo
  As a user
  I want to log in to my account
  So that I can access my profile
  and logout

  Scenario: Valid Login
    Given the Practo homepage is open
    When I click the Login button
    And I enter valid credentials
    Then I should be redirected to the dashboard

  Scenario: Invalid Login
    Given the Practo homepage is open
    When I click the Login button
    And I enter invalid credentials
    Then I should see an error message
