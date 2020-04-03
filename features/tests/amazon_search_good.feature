# Created by alena at 2/1/20
Feature: Lego search

  Scenario: Find header on goods page
    Given Open Amazon main page
    When Search input fill Lego
    And Click search button
    Then Assert Lego header on page