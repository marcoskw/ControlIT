@echo off
setlocal

rem Defina as variáveis
set "SOURCE=C:\licenca"
set "DESTINATION=D:\BACKUPS\LICENCA"
set "EXCLUDE=venv"

rem Obtenha a data de hoje no formato YYYYMMDD
for /f "delims=" %%i in ('powershell -command "Get-Date -Format 'yyyyMMdd'"') do set "DATE=%%i"

rem Crie a pasta de backup se não existir
if not exist "%DESTINATION%" (
    mkdir "%DESTINATION%"
)

rem Crie uma cópia dos arquivos, excluindo a pasta venv
robocopy "%SOURCE%" "%TEMP%\projeto_backup" /E /XD "%SOURCE%\%EXCLUDE%"

rem Compacte os arquivos em um zip
powershell -command "Compress-Archive -Path '%TEMP%\projeto_backup\*' -DestinationPath '%DESTINATION%\backup_%DATE%.zip'"

rem Limpe a pasta temporária
rmdir /S /Q "%TEMP%\projeto_backup"

echo Backup concluído com sucesso! O arquivo está em: %DESTINATION%\backup_%DATE%.zip
pause