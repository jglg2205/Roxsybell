#!/usr/bin/env bash
set -o errexit

pip install -r joyeria/requirements.txt

python joyeria/manage.py collectstatic --no-input
python joyeria/manage.py migrate