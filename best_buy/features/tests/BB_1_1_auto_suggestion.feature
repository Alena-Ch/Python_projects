#Scenario_1:
#Verify that Auto-suggestion works

#Steps:
#1.	Open https://www.bestbuy.com/ page
#2.	Insert group of keywords in search field (use data separation)
#a.	Photo printer
#b.	Music player
#c.	TV
#d.	Wifi router
#3.	Wait a couple of seconds
#4.	Expected to see some suggestions. Count them

Feature: Auto-suggestion feature (for Best Buy multiple search functionality)


  Scenario Outline: Verify that Auto-suggestion works
  Examples:
  |search_word       |expected_search_result |
  |photo printer     |"photo printer"        |
  |music player      |"music player"         |
  |tv                |"tv"                   |
  |wifi router       |"wifi router"          |

  Given Open Best Buy main page
  When Search for <search_word>
    And Print <search_word> number
  Then Suggestions for <expected_search_result> are shown


