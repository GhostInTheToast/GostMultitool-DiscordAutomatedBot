@ECHO OFF

IF not exist "%CD%\venv\" py -3 -m venv venv
call venv\Scripts\activate

pip install -U pip >nul

python -m discord
IF %ERRORLEVEL% NEQ 0 pip install -r requirements.txt

python BotMain.py