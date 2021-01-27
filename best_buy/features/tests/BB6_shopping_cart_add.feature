#  Scenario_6:
# User is able to add an item to the Shopping Cart

# Steps:
# 1. Open https://www.bestbuy.com/  page
# 2. Insert smart watch in search field
# 3. On search results page choose something and click it
# 4. Add product to shopping cart
# 5. Expected product would be in cart
# 6. Close all pop-ups

Feature: Shopping Cart feature


  Scenario: User is able to add an item to the Shopping Cart
    Given Open Best Buy main page
    When Search for smart watch
    And Choose product and click it
    And Add product to shopping cart
    Then Verify cart contains 1 product
