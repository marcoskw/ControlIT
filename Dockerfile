# Use uma imagem base do Python
FROM python:3.9

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos de requisitos e instala as dependências
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copia o restante dos arquivos do projeto
COPY . /app/

# Expõe a porta que o Django usará
EXPOSE 8000

# Define o comando para iniciar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
