@player_service

Feature: Game Service

Scenario: Player Service Receives Request To Create New Player
  When player service receives new player request
  | account_id | game_id |
  | 1337       | 13387   |
  Then it returns a welcome packet with new player id
  When player service is queried for that id's player info
  Then it returns player info with
  | account_id | game_id | game_status |
  | 1337       | 13387   | pending     |
