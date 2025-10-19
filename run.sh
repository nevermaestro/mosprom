#!/bin/sh
cd app && . .env/bin/activate && .env/bin/flask --app app run --host=0.0.0.0 --debug
