@echo off

call venv\Scripts\activate

REM Verifica o requerimentos da aplicação se está de acordo
REM pip install -r .\requirements.txt

REM Verifica as migrações do banco de dados
REM python manage.py migrate

REM Executa as migrações do banco de dados
REM python manage.py makemigrations

REM Inicializa o servidor Django
python manage.py runserver 172.16.114.199:8000

REM Mantém a janela do prompt aberta após o comando ser executado
pause