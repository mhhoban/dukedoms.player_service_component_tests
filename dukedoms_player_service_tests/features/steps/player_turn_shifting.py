from behave import given, then, when
from hamcrest import assert_that, equal_to, is_not, greater_than, has_item

@when('player service receives request to start turn for player with account id "{account_id}"')
def request_player_start_turn(context, account_id):
    """
    send request to start a player's turn
    """

    result, status = context.clients.player_service.gameOperations.start_turn(
        playerId=context.player_ids[account_id]
    ).result()

    assert_that(result.success, equal_to(True))

@when('player service receives request to start buy phase for player with account id "{account_id}"')
def request_player_start_buy(context, account_id):
    """
    send request to start player buy
    """

    result, status = context.clients.player_service.gameOperations.start_buy_phase(
        playerId=context.player_ids[account_id]
    ).result()

    assert_that(result.success, equal_to(True))

@when('player service receives request to end turn player with account id "{account_id}"')
def request_player_start_buy(context, account_id):
    """
    send request to end player turn
    """

    result, status = context.clients.player_service.gameOperations.end_turn(
        playerId=context.player_ids[account_id]
    ).result()

    assert_that(result.success, equal_to(True))
