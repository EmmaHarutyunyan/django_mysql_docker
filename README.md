## Django MySQL Docker Project

![Django](https://img.shields.io/static/v1?label=Django&message=5.0&color=092E20&style=plastic&logo=django&logoWidth=40&logoHeight=40)
![MySQL](https://img.shields.io/static/v1?label=MySQL&message=8.0&color=00758F&style=plastic&logo=mysql&logoWidth=40&logoHeight=40)
![Docker](https://img.shields.io/static/v1?label=Docker&message=20.10&color=2496ED&style=plastic&logo=docker&logoWidth=40&logoHeight=40)
 #

Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Docker Setup](#docker-setup)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
## Installation

1 .**Clone the repository:**
```bash
[
git clone https://github.com/your-username/your-repo.git
cd your-repo](https://github.com/EmmaHarutyunyan/django_mysql_docker.git)
```


2. **Create virtual environment and activate:**
```bash


python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```
3. **Install packages:**
```bash
pip install -r requirements.txt
```
4. **Configure databases**:
```bash
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
```
5 .**Migration:**
```bash
python manage.py migrate
python manage.py createsuperuser
```

## Usage

1.**Run project**:
```
python manage.py runserver\
```
2.**Access the application:**
```
Open your browser and navigate to http://127.0.0.1:8000/.
```
3.**Admin Panel**:
```
You can access the admin panel at http://127.0.0.1:8000/admin with the superuser credentials created earlier.
```
## Configuration

1.**Environment Variables**
```
DJANGO_SECRET_KEY: Your Django secret key.
DB_NAME: The name of your database.
DB_USER: The database user.
DB_PASSWORD: The database password.
DB_HOST: The database host.
DB_PORT: The database port.
You can set these variables in a .env file in the root directory.
```
## Docker Setup

1.**Build the Docker images:**
```
docker-compose build
```
2.**Run the containers:**
```
docker-compose up
```
3.**Apply migrations inside the Django container**
```
docker-compose exec web python manage.py migrate
```
4.**Create a superuser inside the Django container:**
```
docker-compose exec web python manage.py createsuperuser
```
5.**Access the application:**
```
Open your browser and navigate to http://127.0.0.1:8000/.
```
## Project Structure
```
.
├── docker-compose.yml
├── Dockerfile
├── .env
├── manage.py
├── requirements.txt
├── myproject
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│ └── ...
└── ...
```
## Contributing

```
   Contributions are welcome! Please follow these steps:
   
   Fork the repository.
   Create a new branch (git checkout -b feature/your-feature).
   Commit your changes (git commit -am 'Add some feature').
   Push to the branch (git push origin feature/your-feature).
   Create a new Pull Request.
```




