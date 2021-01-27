# Scenario_1:
# Verify that Auto-suggestion works

# Steps:
# 1. Open https://www.bestbuy.com/ page
# 2. Insert group of keywords in search field (use data separation)
#    a. Photo printer
#    b.	Music player
#    c.	TV
#    d.	Wifi router
# 3. Wait a couple of seconds
# 4. Expected to see some suggestions. Count them

Feature: Auto-suggestion feature


  Scenario: Verify that Auto-suggestion works
    Given Open Best Buy main page
    When Search for photo printer
    When Wait for product suggestions
    And Count suggestions
    Then Suggestions for "photo printer" are shown
