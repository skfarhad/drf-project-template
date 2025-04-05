#!/bin/bash

set -e

echo "Running database migrations..."
python manage.py migrate

echo "Running unit tests..."
python manage.py test
