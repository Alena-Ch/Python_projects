
#  Scenario_4:
#Verify that Sign-In with existing account works

#Steps:
#1.	Open https://www.bestbuy.com/ page
#2.	Click account button
#3.	Fill data from prev step
#4.	Click submit
#5.	Expected login will be complete successfully

Feature: Sign-In feature


  Scenario: Verify that Sign-In with existing account works
    Given Open Best Buy main page
    When Click account button
    And Click on Sign In button
    And Enter simptelen@gmail.com in Email address field
    And Enter abcd111&&& in Passwords field
    And Click Sign In
    Then User can see message Hi, Jon
