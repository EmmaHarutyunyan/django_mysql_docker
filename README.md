Django MySQL Docker Project
A Django project set up with MySQL and Docker for efficient development and deployment.

Django MySQL Docker

Table of Contents
Installation
Usage
Configuration
Docker Setup
Project Structure
Contributing
License
Installation
Clone the repository:

git clone https://github.com/your-username/your-repo.git
cd your-repo
Create virtual envoirement and activate:

python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
Install packages:

pip install -r requirements.txt
Configure databases:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your-database-name',
        'USER': 'your-database-user',
        'PASSWORD': 'your-database-password',
        'HOST': 'your-database-host',
        'PORT': 'your-database-port',
    }
}
Migration:

python manage.py migrate
python manage.py createsuperuser
Usage
Run project:

python manage.py runserver
Access the application:

Open your browser and navigate to http://127.0.0.1:8000/.
Admin Panel:

You can access the admin panel at http://127.0.0.1:8000/admin with the superuser credentials created earlier.
Configuration
Environment Variables
DJANGO_SECRET_KEY: Your Django secret key.
DB_NAME: The name of your database.
DB_USER: The database user.
DB_PASSWORD: The database password.
DB_HOST: The database host.
DB_PORT: The database port.
You can set these variables in a .env file in the root directory.
Docker Setup
Build the Docker images:
docker-compose build
Run the containers:
docker-compose up
Apply migrations inside the Django container:
docker-compose exec web python manage.py migrate
Create a superuser inside the Django container:
docker-compose exec web python manage.py createsuperuser
Access the application:
Open your browser and navigate to http://127.0.0.1:8000/.
Project Structure
      .
      ├── docker-compose.yml
      ├── Dockerfile
      ├── .env
      ├── manage.py
      ├── requirements.txt
      ├── myproject
      │   ├── __init__.py
      │   ├── settings.py
      │   ├── urls.py
      │   ├── wsgi.py
      │   └── ...
      └── ...
Contributing
   Contributions are welcome! Please follow these steps:
   
   Fork the repository.
   Create a new branch (git checkout -b feature/your-feature).
   Commit your changes (git commit -am 'Add some feature').
   Push to the branch (git push origin feature/your-feature).
   Create a new Pull Request.
