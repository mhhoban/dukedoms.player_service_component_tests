@player_service

Feature: Game Service
Background: Clear Player Service DB
  Given an empty player service database
  And an active player with account id "13387"

@wip
Scenario: Player Service Receives Start Turn Request
  Given player with account id "13387" in phase "inactive"
  When player service receives request to start turn for player with account id "13387"
  Then the request is successful
  
@wip
Scenario: Player Service Receives Start Buy Request
  Given player with account id "13387" in phase "action"
  When player service receives request to start buy phase for player with account id "13387"
  Then the request is successful

@wip
Scenario: Player Service Receives Start Buy Request
  Given player with account id "13387" in phase "buy"
  When player service receives request to end turn player with account id "13387"
  Then the request is successful
