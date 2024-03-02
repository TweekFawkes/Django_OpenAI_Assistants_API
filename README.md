# Django_OpenAI_Assistants_API

Research Project to Learn OpenAI Assistants API by building a Django web interface; Started on 202402.

## Setup Instructions

### Clone Repo

```bash
git clone https://github.com/TweekFawkes/Django_OpenAI_Assistants_API.git
cd chatgpt_clone
```

### Configure OpenAI Secret Key

```bash
cp .env-example .env
# Set SECRET_KEY equal to your OpenAI Key in the .env file
```

### Ensure We Are Using Python3

```bash
...% python --version       
Python 3.11.7

...% python3 --version
Python 3.11.7
```

### Create Python Virtual Environment (macOS)

```bash
python3 -m venv venv
source venv/bin/activate

(venv)...%
```

### Install Python Pip & Dependencies

```bash
pip install --upgrade pip
python -m pip install django
pip install openai
pip install python-dotenv
```

### Django Setup

```bash
python manage.py migrate
```

## Operating Instructions

### Activate Python Virtual Environment

If not in the python virtual environment, then activate the virtual environment

```bash
source venv/bin/activate

(venv)...%
```

### Running the Web Application

Start the server:

```bash
cd chatgpt_clone
python manage.py runserver
```

### Stopping the Web Application

Stop the server:

```bash
CTRL+C
```

### Optionally, to exit Python Virtual Environment (macOS):

```bash
(venv)...% deactivate

...%
```

# Other Random Notes Below...

## VS Code Extensions

```
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
```

# References
- https://commons.wikimedia.org/wiki/File:Loading_icon.gif
