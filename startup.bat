cls

IF not exist "%CD%\venv\" py -3 -m venv venv
call venv\Scripts\activate

python -m pip install -U pip

python -m pip install -U discord.py[voice]

python -m pip install -U requests

python -m pip install -U BeautifulSoup4

python BotMain.py