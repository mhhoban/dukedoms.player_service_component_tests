from behave import given, then, when
from hamcrest import assert_that, equal_to, is_not, greater_than, has_item

@given('a pending player with info')
@when('player service receives new player request')
def new_player_request(context):
    """
    send a request to player service to create new pending player
    """
    account_id = int(context.table.rows[0]['account_id'])
    context.game_id = int(context.table.rows[0]['game_id'])

    result, status = context.clients.player_service.newPlayer.create_new_player(
        newPlayerRequest={
            'accountId': account_id,
            'gameId': context.game_id
        }
    ).result()
    assert_that(status.status_code, equal_to(200))
    context.welcome_packet = result
    context.player_ids[str(account_id)] = context.welcome_packet.player_id

@given('a player with state')
def new_player_with_state(context):
    """
    create a new player with a pre-defined state
    """
    new_player_request(context)
    activate_pending_player(context, context.table.rows[0]['turn_phase'])


@then('player service returns a welcome packet with player id for account "{account_id}"')
def assert_welcome_packet_received(context, account_id):
    """
    mostly decorative step verifying welcome packet has expected data
    """
    assert_that(context.welcome_packet.player_id, is_not(None))
    assert_that(context.welcome_packet.game_id, equal_to(context.game_id))

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
