# Scenario_5:
# Shopping cart - empty state

# Steps:
# 1. Open https://www.bestbuy.com/ page
# 2. Click cart button
# 3. Expected cart page will have empty in the title

Feature: Shopping cart feature


  Scenario: Shopping cart - empty state
    Given Open Best Buy main page
    When Click cart icon
    Then User sees message Your cart is empty