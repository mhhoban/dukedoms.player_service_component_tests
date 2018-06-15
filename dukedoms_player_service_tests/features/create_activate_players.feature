Feature: Player Service Create and Activate Players

  Background: Clear Player Service DB
    Given an empty player service database

  Scenario: Player Service Receives Request To Create New Player
    When player service receives new player request
      | account_id | game_id |
      | 1337       | 13387   |
    Then player service returns a welcome packet with player id for account "1337"
    When player service is queried with player id for account "1337"
    Then it returns player info with
      | account_id | game_id | game_status | turn_phase |
      | 1337       | 13387   | pending     | pending    |

  Scenario: Player Service Receives Activate Player Request
    Given a pending player with info
      | account_id | game_id |
      | 1337       | 13387   |
    When player service receives request to activate the pending player with turn phase "Action"
    Then the request is successful
    When player service is queried with player id for account "1337"
    Then it returns player info with
      | account_id | game_id | game_status | turn_phase |
      | 1337       | 13387   | active      | action     |
