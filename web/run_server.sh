#!/bin/bash

echo 'creating regex'

python data/wacky_regex.py > data.json

echo 'running server...'
export FLASK_APP=app.py
flask run --host=0.0.0.0 -p 1234
