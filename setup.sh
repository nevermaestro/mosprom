#!/bin/sh
cd app && python3 -m venv .env && . .env/bin/activate && pip install -r requirements.txt
