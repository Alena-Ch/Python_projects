#  Scenario_7:
#User is able to add multiple items to the Shopping Cart

#Steps:
#1.	Open https://www.bestbuy.com/ page
#2.	Insert smart watch in search field
#3.	On search results page choose something and click it
#4.	Add product to shopping cart
#5.	Return to product search page
#6.	On search results page choose another product and click it
#7.	Add product to shopping cart
#8.	Expected products would be in cart
#9.	Close all pop-ups

Feature: Shopping Cart feature


  Scenario: User is able to add multiple items to the Shopping Cart
    Given Open Best Buy main page
    When Search for smart watch
    And Choose product and click it
    And Add product to shopping cart
    And Return to product search page
    Then Verify cart contains 1 product
