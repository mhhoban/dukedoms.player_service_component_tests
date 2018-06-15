Feature: Player Actions
Tests for players playing and buying cards
  Background:
    Given active player with account id "13387"

  @wip
  Scenario: Player Purchases Card
    Given player with account id "13387" in "buy" phase
    When player service receives request for card purchase:
      | account id | card id |
      | 13387      | 11      |
    Then player has card id "11" at top of discard pile

    @wip
    Scenario: Player Plays Card
    Given player with account id "13387" in "action" phase
    When player service receives request to play card:
      | account id | card slot id |
    
