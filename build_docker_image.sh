#!/bin/bash

./oas_setup.sh
SERVICE=dukedoms_player_service_tests
docker build --build-arg service=$SERVICE \
--tag "mhhoban/dukedoms-player-service-tests:latest" .
