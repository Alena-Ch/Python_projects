#  Scenario_8:
#Shopping cart - Change quantity

#Steps:
#1.	Repeat step User is able to add an item to the Shopping Cart
#2.	Click cart button
#3.	Change quantity from 1 to 2
#4.	Expected items in cart will be 2

Feature: Shopping cart feature


  Scenario: Shopping cart - Change quantity
    Given Open Best Buy main page
    When Search for smart watch
    And Choose product and click it
    And Add product to shopping cart
    And Change quantity from 1 to 2
    Then Verify cart contains 2 product