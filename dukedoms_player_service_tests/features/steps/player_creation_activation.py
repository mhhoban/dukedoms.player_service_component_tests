from behave import given, then, when
from hamcrest import assert_that, equal_to, is_not, greater_than, has_item

@given('a pending player with info')
@when('player service receives new player request')
def new_player_request(context):
    """
    send a request to player service to create new pending player
    """
    context.account_id = int(context.table.rows[0]['account_id'])
    context.game_id = int(context.table.rows[0]['game_id'])

    result, status = context.clients.player_service.newPlayer.create_new_player(
        newPlayerRequest={
            'accountId': context.account_id,
            'gameId': context.game_id
        }
    ).result()
    assert_that(status.status_code, equal_to(200))
    context.welcome_packet = result

@then('player service returns a welcome packet with player id for account "{account_id}"')
def assert_welcome_packet_received(context, account_id):
    """
    mostly decorative step verifying welcome packet has expected data
    """
    assert_that(context.welcome_packet.player_id, is_not(None))
    assert_that(context.welcome_packet.game_id, equal_to(context.game_id))

    context.player_ids[account_id] = context.welcome_packet.player_id
