# Guia de Inicialização do Projeto

Siga os passos abaixo para configurar e rodar o projeto:

1. **Clonar o repositório:**
    ```bash
    git clone https://github.com/marcoskw/licenca.git .
    ```

2. **Criar o Ambiente Virtual:**
    ```bash
    python -m venv venv
    ```

3. **Ativar o Ambiente Virtual:**
    - **Windows:**
      ```bash
      .\venv\Scripts\activate
      ```
    - **Linux:**
      ```bash
      source ./venv/bin/activate
      ```

4. **Instalar as dependências do projeto:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Atualizar o pip:**
    ```bash
    python -m pip install --upgrade pip
    ```

6. **Fazer as migrações para o banco de dados:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

7. **Criar o superusuário:**
    ```bash
    python manage.py createsuperuser
    ```

8. **Rodar o projeto:**
    ```bash
    python manage.py runserver
    ```
