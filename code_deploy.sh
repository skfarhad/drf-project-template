#!/usr/bin/env bash

git pull
./manage.py migrate
./manage.py test
./prod/stop_server.sh
./prod/run_server.sh