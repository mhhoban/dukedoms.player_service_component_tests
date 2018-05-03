from behave import given, then, when
from bravado.exception import HTTPNotFound
from hamcrest import assert_that, equal_to, is_not, greater_than, has_item
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

@given('an empty player service database')
def clear_account_service_db(context):
    """
    drop any existing information from tables for a clean test run.
    """
    engine = create_engine(context.env_urls.player_service_db)
    Session = scoped_session(sessionmaker(bind=engine))
    session = Session()

    session.execute('TRUNCATE TABLE players')
    session.commit()
    session.close()

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

@then('player service returns a welcome packet with new player id')
def assert_welcome_packet_received(context):
    """
    mostly decorative step verifying welcome packet has expected data
    """
    assert_that(context.welcome_packet.player_id, is_not(None))
    assert_that(context.welcome_packet.game_id, equal_to(context.game_id))

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