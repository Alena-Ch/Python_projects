
#  Scenario_3:
#Verify that Registration flow works as expected

#Steps:
#1.	Open https://www.bestbuy.com/ page
#2.	Click account button
#3.	Best Buy: click "Create account"
#4.	Fill all fields with fake data
#5.	Click submit
#6.	Expected registration will be complete successfully

Feature: Registration


  Scenario: Verify that Registration flow works as expected
    Given Open Best Buy main page
    When Click account button
    And Click "Create account"
    And Enter Jon in First name field
    And Enter Smith in Last name field
    And Enter simptelen@gmail.com in Email address field
    And Enter abcd111&&& in Passwords field
    And Enter abcd111&&& in Confirm Password field
    And Enter (917)478-1111 in Phone Number field
    And Click submit
    Then User can see message Hi, Jon