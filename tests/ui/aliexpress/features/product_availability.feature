Feature: Product availability

    Background:
        Given I navigate to Aliexpress home page

    @EXERCISE
    Scenario: Check second product of second result page availability
        Given I search for "iphone" product
        And I click on "list" view option
        And I select the result page number "2"
        When I click on the product number "2" of the current result page
        Then I see the selected product details
        And I see there are at least "1" available product to buy

    @EXTRA
    Scenario: Check third product of first result page availability with gallery view
        Given I search for "iphone 8" product
        And I click on "gallery" view option
        When I click on the product number "3" of the current result page
        Then I see the selected product details
        And I see there are at least "1" available product to buy
