# Django_OpenAI_Assistants_API
Research Project to Learn OpenAI Assistants API by building a Django web interface; started on 202402

# Setup: Clone Repo
git clone https://github.com/TweekFawkes/Django_OpenAI_Assistants_API.git
cd chatgpt_clone

# Setup: Configure OpenAPI Secrect Key
cp .env-example .env
set SECRET_KEY equal to OpenAI Key

# Setup: Create Python Virutal Env (macOS)
python3 -m venv venv
source venv/bin/activate

# Setup: Install Python Pip & Dependencies
pip install --upgrade pip
python -m pip install django
pip install openai
pip install python-dotenv

# Setup: ...
python manage.py migrate

# Run: Python Virutal Env (macOS)
source venv/bin/activate

# Run: ...
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





python manage.py collectstatic




# Refs
- https://commons.wikimedia.org/wiki/File:Loading_icon.gif
