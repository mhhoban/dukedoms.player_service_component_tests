from behave import given, then, when
from hamcrest import assert_that, equal_to, is_not, greater_than, has_item

@when('player service is queried with player id for account "{account_id}"')
def query_player_id(context, account_id):
    """
    send a request to player service for player info
    """
    result, status = context.clients.player_service.playerInfo.get_player_info(
        playerId=int(context.player_ids[account_id])
    ).result()
    assert_that(status.status_code, equal_to(200))
    context.retrieved_player_info = result


@then('it returns player info with')
def assert_player_info_accuracy(context):
    """
    check that the data returned by query_player_id is as expected
    """
    game_status = context.table.rows[0]['game_status']
    turn_phase = context.table.rows[0]['turn_phase']
    account_id = context.table.rows[0]['account_id']
    game_id = context.table.rows[0]['game_id']


    assert_that(context.retrieved_player_info.player_id, equal_to(int(context.player_ids[account_id])))
    assert_that(context.retrieved_player_info.game_id, equal_to(int(game_id)))
    assert_that(context.retrieved_player_info.game_status, equal_to(game_status))
    assert_that(context.retrieved_player_info.account_id, equal_to(int(account_id)))

@then('the request is successful')
def generic_pass(context):
    pass
