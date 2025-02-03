@echo off

call venv\Scripts\activate

REM Inicializa o servidor Django
python manage.py runserver

REM Mantém a janela do prompt aberta após o comando ser executado
pause