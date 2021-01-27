# Scenario_9:
# User is able to write a review

# Steps:
# 1. Open https://www.bestbuy.com/ page
# 2. Insert Wifi router in search field
# 3. On search results page choose something and click it
# 4. Click "write review" button
# 5. Expected product has "write review" button

Feature: Review feature


  Scenario: User is able to write a review
    Given Open Best Buy main page
    When Search for wifi router
    And Click on router
    And Click on "Reviews" button
    Then User can see Write a Review button


