# Scenario_2:
# User is taken to the search results page

# Steps:
# 1. Open https://www.bestbuy.com/ page
# 2. Insert dry vacuum in search field
# 3. Click search button or click enter button
# 4. Expect to see the search results page. Check that title is relevant to search text

Feature: Search feature


  Scenario: User is taken to the search results page
    Given Open Best Buy main page
    When Search for dry vacuum
    Then Search result for "dry vacuum" is shown