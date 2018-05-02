@player_service

Feature: Game Service
Background: Clear Player Service DB
  Given an empty player service db

Scenario: Player Service Receives Request To Create New Player
  When player service receives new player request
    | account_id | game_id |
    | 1337       | 13387   |
  Then it returns a welcome packet with new player id
  When player service is queried for that player's info
  Then it returns player info with
    | account_id | game_id | game_status |
    | 1337       | 13387   | pending     |

Scenario: Player Service Receives Activate Player Request
  Given a pending player with info
    | account_id | game_id |
    | 1337       | 13387   |
  When player service receives request to activate the pending player with turn phase "Action"
  Then the request is successful
  When player service is queried for that player's info
  Then it returns player info with
    | account_id | game_id | game_status | turn_phase |
    | 1337       | 13387   | active      | action     |



@wip
Scenario: Player Service Receives Phase Change Request

@wip
Scenario: Player Service Receives Play Card Request
