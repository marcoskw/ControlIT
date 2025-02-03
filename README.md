# Django Equipment Management System

The Django Equipment Management System is a comprehensive web application for managing company assets, employees, and IT infrastructure.

This project provides a robust platform for businesses to track and manage their equipment, software licenses, and employee information. It offers features for registering companies, departments, operators, and various types of equipment, with a focus on computer hardware and software management.

The system includes functionality for:

- Company and department management
- Employee (operator) tracking
- Equipment inventory, including computers and software
- Incident logging for both operators and equipment
- Software license management
- Computer inspection scheduling and reporting
- Wiki-style knowledge base

Built with Django, this application leverages the power of Python to deliver a scalable and maintainable solution for equipment management needs.

## Repository Structure

```
.
├── atualiza
│   └── licenca
│       ├── core
│       ├── empresa
│       ├── equipamentos
│       ├── ocorrencias
│       ├── parametros
│       ├── usuarios
│       └── wiki
├── core
├── empresa
├── equipamentos
├── ocorrencias
├── parametros
├── usuarios
└── wiki
```

Key Files:
- `manage.py`: Django's command-line utility for administrative tasks
- `requirements.txt`: List of Python package dependencies
- `Dockerfile`: Configuration for Docker containerization
- `docker-compose.yml`: Docker Compose configuration for easy deployment

Important integration points:
- `core/settings.py`: Django project settings
- `core/urls.py`: Main URL configuration
- `*/models.py`: Database models for each application
- `*/views.py`: View functions for handling requests
- `*/admin.py`: Admin interface configurations

## Usage Instructions

### Installation

Prerequisites:
- Python 3.9 or higher
- pip (Python package manager)
- Docker (optional, for containerized deployment)

Step-by-step installation:

1. Clone the repository:
   ```
   git clone <repository_url>
   cd django-equipment-management
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

### Getting Started

1. Access the admin interface at `http://localhost:8000/admin/` and log in with your superuser credentials.

2. Start by creating a company in the "Empresas" section.

3. Add departments (setores) and operators (operadores) associated with the company.

4. Navigate to the equipment management section to add various types of equipment, focusing on computers and their associated software.

5. Use the incident logging system to track issues with operators or equipment.

6. Utilize the wiki feature to create and manage knowledge base articles.

### Configuration Options

- `core/settings.py`: Adjust database settings, static file handling, and other Django configurations.
- `parametros/models.py`: Modify `ParametrosEmpresa` to adjust company-specific settings.

### Common Use Cases

1. Registering a new computer:
   ```python
   from equipamentos.models import Computador, Marca, SistemaOperacional
   from empresa.models import Operador, Setor

   new_computer = Computador.objects.create(
       nome_rede="PC001",
       status="ATV",
       modelo="ThinkPad X1",
       serial_number="ABC123",
       operador=Operador.objects.get(nome_operador="John Doe"),
       setor=Setor.objects.get(nome_setor="IT"),
       marca=Marca.objects.get(nome_marca="Lenovo"),
       sistema_operacional=SistemaOperacional.objects.get(nome_sistema_operacional="Windows 10"),
       processador="Intel i7",
       memoria="16GB",
       armazenamento="512GB",
       tipo_armazenamento="SSD"
   )
   ```

2. Logging an equipment incident:
   ```python
   from ocorrencias.models import OcorrenciaComputador
   from django.contrib.auth.models import User

   OcorrenciaComputador.objects.create(
       data=timezone.now(),
       usuario=User.objects.get(username="admin"),
       tipo_ocorrencia="INATIVAR COMPUTADOR",
       computador=Computador.objects.get(nome_rede="PC001"),
       observacoes="Computer no longer in use"
   )
   ```

### Integration Patterns

- Use Django's ORM for database operations across all applications.
- Leverage Django's built-in authentication system for user management.
- Utilize Django's admin interface for easy data management and configuration.

### Testing & Quality

To run tests:
```
python manage.py test
```

### Troubleshooting

1. Database migration issues:
   - Problem: `django.db.utils.OperationalError: no such table`
   - Solution: 
     ```
     python manage.py makemigrations
     python manage.py migrate
     ```
   - If issues persist, check `INSTALLED_APPS` in `settings.py` and ensure all apps are listed.

2. Static files not loading:
   - Problem: CSS and JavaScript files not being served
   - Solution: 
     - Ensure `DEBUG = True` in `settings.py` for development
     - Run `python manage.py collectstatic`
     - Check `STATIC_URL` and `STATIC_ROOT` in `settings.py`

3. Permission denied errors:
   - Problem: Unable to write to log files or media directory
   - Solution:
     - Check file permissions: `ls -l /path/to/directory`
     - Adjust permissions: `chmod 755 /path/to/directory`
     - Ensure the web server process has write access

For more detailed debugging:
- Enable Django's debug logging in `settings.py`:
  ```python
  LOGGING = {
      'version': 1,
      'disable_existing_loggers': False,
      'handlers': {
          'console': {
              'class': 'logging.StreamHandler',
          },
      },
      'root': {
          'handlers': ['console'],
          'level': 'DEBUG',
      },
  }
  ```
- Check the console output or log files (typically in `/var/log/django/` on Linux systems) for detailed error messages.

Performance optimization:
- Monitor database query performance using Django Debug Toolbar
- Use `select_related()` and `prefetch_related()` to optimize database queries
- Implement caching for frequently accessed data using Django's caching framework

## Data Flow

The Django Equipment Management System processes requests through the following flow:

1. User sends a request to a specific URL (e.g., `/equipamentos/listar/`)
2. Django's URL dispatcher (`urls.py`) routes the request to the appropriate view function
3. The view function in `views.py` processes the request, interacting with models as needed
4. Models (`models.py`) interact with the database to retrieve or modify data
5. The view prepares the data and renders a template (`templates/*.html`)
6. The rendered HTML is sent back to the user's browser

```
[User] -> [URL Dispatcher] -> [View] <-> [Model] <-> [Database]
                                 |
                                 v
                            [Template]
                                 |
                                 v
                              [User]
```

Note: For API requests, the flow is similar, but instead of rendering templates, views return JSON responses.

## Deployment

Prerequisites:
- Docker
- Docker Compose

Deployment steps:

1. Build the Docker image:
   ```
   docker-compose build
   ```

2. Start the containers:
   ```
   docker-compose up -d
   ```

3. Apply migrations:
   ```
   docker-compose exec web python manage.py migrate
   ```

4. Create a superuser:
   ```
   docker-compose exec web python manage.py createsuperuser
   ```

5. Collect static files:
   ```
   docker-compose exec web python manage.py collectstatic
   ```

The application should now be accessible at `http://localhost:8000`.

For production deployments, ensure you set `DEBUG = False` in `settings.py` and configure a production-ready web server like Nginx to serve static files and proxy requests to Gunicorn.

## Infrastructure

The project uses Docker for containerization, defined in the following files:

- Dockerfile:
  - Base image: python:3.9
  - Installs project dependencies
  - Sets up the working directory
  - Exposes port 8000
  - Runs the Django development server

- docker-compose.yml:
  - Defines a web service that builds from the Dockerfile
  - Maps port 8000 to the host
  - Mounts the current directory to /app in the container

Database:
- The project uses SQLite by default, as defined in `core/settings.py`
- For production, consider using a more robust database like PostgreSQL

Static files:
- Served by Django's development server in debug mode
- For production, use a dedicated web server like Nginx to serve static files