import os

from addict import Dict
from bravado.client import SwaggerClient
from bravado.swagger_model import load_file

def get_environment_variables(env):
    URLS = Dict()
    URLS.local.player_service = 'http://localhost:5004'
    URLS.local.player_service_db = 'postgresql+psycopg2://postgres:daleria@127.0.0.1:5432/player_service'

    URLS.container.player_service = 'http://player-service:5004'
    URLS.container.player_service_db = 'postgresql+psycopg2://postgres:daleria@dukedoms-rdbs:5432/player_service'

    if env == 'local':
        return URLS.local
    else:
        return URLS.container

def before_scenario(context, scenario):

    context.player_ids = {}

    config = {
        'also_return_response': True,
        'validate_responses': True,
        'validate_requests': True,
        'validate_swagger_spec': True,
        'use_models': True,
        'formats': []
    }

    env = context.config.userdata.get('env')
    context.env_urls = get_environment_variables(env)
    context.clients = Dict()
    context.clients.player_service = SwaggerClient.from_spec(
        load_file(
            'specs/dukedoms_player_service_api.yaml',
        ),
        origin_url=context.env_urls.player_service,
        config=config
    )
