# Django_OpenAI_Assistants_API
Research Project to Learn OpenAI Assistants API by building a Django web interface; started on 202402


# Setup

cp .env-example .env

set SECRET_KEY equal to OpenAI Key

python3 -m venv venv
source venv/bin/activate

pip install --upgrade pip
python -m pip install django
pip install openai

git clone https://github.com/TweekFawkes/Django_OpenAI_Assistants_API.git

cd chatgpt_clone

python manage.py migrate
python manage.py collectstatic


# Run

source venv/bin/activate

cd chatgpt_clone

python manage.py runserver


# Other Random Notes Below...

- macOS
-- VS Code
--- Docker
---- Dev Containers
---- GitHub Copilot
---- GitHub Copilot Chat
---- GitHub Copilot Labs -> Disabled / EOL
---- Prettier
---- Pylance
---- Python
---- Python Debugger
---- Rainbow CSV
---- WSL

Change to Directory:
cd /Users/bryce/Library/CloudStorage/Dropbox/Code/BackBreaker/TextGenerator/
python3 --version
Python 3.11.5

First Time Only, Create Python Virtual Environment:
python3 -m venv venv
source venv/bin/activate

All other times, Activate Python Virtual Environment:
source venv/bin/activate

Optionally, to exit Python Virtual Environment:
deactivate


### Setup -> One-Time Only ###

pip install --upgrade pip
python -m pip install django
pip install openai


### Creation -> One-Time Only ###

django-admin startproject chatgpt_clone
cd chatgpt_clone

python manage.py startapp chat





