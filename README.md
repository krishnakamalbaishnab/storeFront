# StoreFront - E-Commerce Platform
StoreFront is a Django-based e-commerce web application. This project allows users to browse and purchase products, and includes features such as user authentication, product listings, and more.

## Features
- User authentication (login, registration).
- Product browsing and searching.
- Add to cart and purchase functionality.
- Product tags and likes for enhanced user experience.
- Admin panel for managing products and users.
  
### Project Structure
- storefront: Core settings and configurations of the Django project.
- store: App responsible for managing products, categories, and orders.
- tags: App for managing product tags.
- likes: App to allow users to like and rate products.
- playground: App used for experimenting with Django features.
  
## Installation
- Prerequisites  : Python 3.8 or higher & MySQL installed and running.
  
### Steps : Clone the repository:

```bash
git clone https://github.com/yourusername/storefront.git
```
- Navigate to the project directory:

```bash

cd storefront
```
- Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Alternatively, if you're using Pipenv:

```bash
pipenv install
```
- Set up MySQL:
Create a new MySQL database:
SQL

```bash
CREATE DATABASE storefront_db;
```
- Update the database configuration in storefront/settings.py:

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'storefront_db',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
Run the initial migrations and create a superuser:

```bash

python manage.py migrate
python manage.py createsuperuser
```
- Run the development server:

```bash
python manage.py runserver
```

- Visit the site at http://127.0.0.1:8000

### Database
The project uses MySQL. Could you make sure that the database credentials in storefront/settings.py are configured correctly?

### Contributing
Feel free to contribute by submitting a pull request. Make sure to follow the existing coding standards and write tests for any new features.

## License
This project is licensed under an open license. Feel free to use, modify, and distribute the code as you see fit. Please give credit to the original author, Krishna Kamal Baishnab, when using the content in any public or private project

