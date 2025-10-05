@REM This starts the flask server, move it to shortcut to make it easier for you
@REM I assume you have already created a venv 
@echo off
cd "YOUR PATH"
CALL .venv\Scripts\activate
start "" http://127.0.0.1:5000/
start flask --app server.py run