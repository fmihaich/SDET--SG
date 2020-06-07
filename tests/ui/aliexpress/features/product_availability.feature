Feature: Product availability


    Scenario: Check second product of second result page availability
        Given I navigate to Aliexpress home page
        And I search for "iphone" product
        And I click on "gallery" view option
        And I select the result page number "2"
        When I click on the product number "2" of the current result page
        Then I see there are at least "1" available product to buy
