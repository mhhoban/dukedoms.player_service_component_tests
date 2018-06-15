@player_service

Feature: Game Service
Background: Clear Player Service DB
  Given an empty player service database

Scenario: Player Service Receives Start Turn Request
  Given a player with state:
    | game_id | account_id | turn_phase |
    | 13387   | 1337       | inactive   |
  When player service receives request to start turn for player with account id "1337"
  Then the request is successful

Scenario: Player Service Receives Start Buy Request
  Given a player with state:
    | game_id | account_id | turn_phase |
    | 13387   | 1337       | action   |
  When player service receives request to start buy phase for player with account id "1337"
  Then the request is successful

@foo
Scenario: Player Service Receives Start Buy Request
  Given a player with state:
    | game_id | account_id | turn_phase |
    | 13387   | 1337       | buy   |
  When player service receives request to end turn player with account id "1337"
  Then the request is successful
