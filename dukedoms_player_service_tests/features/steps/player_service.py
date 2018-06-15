from behave import given, then, when
from hamcrest import assert_that, equal_to, is_not, greater_than, has_item

@when('player service is queried for that player\'s info')
def query_player_id(context):
    """
    send a request to player service for player info
    """
    result, status = context.clients.player_service.playerInfo.get_player_info(
        playerId=context.welcome_packet.player_id
    ).result()
    assert_that(status.status_code, equal_to(200))
    context.retrieved_player_info = result


@then('it returns player info with')
def assert_player_info_accuracy(context):
    """
    check that the data returned by query_player_id is as expected
    """
    game_status = context.table.rows[0]['game_status']

    assert_that(context.retrieved_player_info.player_id, equal_to(context.welcome_packet.player_id))
    assert_that(context.retrieved_player_info.game_id, equal_to(context.game_id))
    assert_that(context.retrieved_player_info.game_status, equal_to(game_status))
    assert_that(context.retrieved_player_info.account_id, equal_to(context.account_id))

@when('player service receives request to activate the pending player with turn phase "{phase}"')
def activate_pending_player(context, phase):
    """
    send request to activate a pending player with a given turn phase
    """
    result, status = context.clients.player_service.gameOperations.activate_player(
        activatePlayerRequest = {
            'playerId': context.welcome_packet.player_id,
            'startingPhase': phase
        }
    ).result()

    assert_that(status.status_code, equal_to(200))

@then('the request is successful')
def generic_pass(context):
    pass
