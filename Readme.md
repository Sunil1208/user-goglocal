
# Django Project with JWT Auth and Middleware

This is a Django project that includes a REST API using Django Rest Framework (DRF), JWT-based authentication, and a custom middleware to intercept incoming requests. The project allows you to create, read, update, and delete users via the Django admin interface and provides API endpoints for user authentication and profile retrieval.

## Features

- User model with custom fields (username, password, first_name, last_name, email)
- Django admin interface for managing users
- JWT-based authentication for API endpoints
- API endpoint for user login (/api/user/login)
- API endpoint for retrieving user profile (/api/user/profile)
- API endpoint for retrieving profiles (/api/users)
- Custom middleware to validate JWT tokens and add user object to requests

## Getting Started

These instructions will help you set up and run the project on your local machine for development and testing purposes.

## Prerequisites

Make sure you have the following software installed:

Python (version 3.6 or higher)
Django (version 4.2.3)
Virtual environment tool (e.g., virtualenv, conda)



## Installation

Clone the repository:

```bash
git clone https://github.com/Sunil1208/user-goglocal
cd goglocal
```

Create and active a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```
    
Install the project dependencies

```bash
pip install -r requirements.txt
```

The project uses a SQLite database by default. You can create and apply the database migrations using the following commands:
```bash
   python manage.py migrate
```

Create a superuser to access the Django admin interface:

```bash
   python manage.py createsuperuser
```

## Usage

To start the development server, run the following command:

```bash
python manage.py runserver
```

You can now access the application at http://127.0.0.1:8000/


Access the Django admin interface at http://localhost:8000/admin and log in with your superuser credentials

### Usability cases
- To create, read, update, and delete users, use the Django admin interface.
- To authenticate a user and obtain a JWT token, make a POST request to `/api/user/login` with the username and password in the request body. The response will contain the JWT token.
- To retrieve a user's profile, make a GET request to `/api/user/profile` with a valid JWT token in the Authorization header. The response will contain the user's first name and last name.
- To retrieve all the user profiles, make a GET request to `/api/users`. The response will contain the list of user details.
## Customization

* If the default User model does not meet the requirements, you can customize it by modifying the UserProfile model in user/models.py.

* You can customize the JWT settings by updating the configurations in the settings.py file of your project.

* Additional customization options are available for serializers, views, and URL configurations. Refer to the Django Rest Framework documentation for more information.
## Postman Collection

To access, test and for the reference of the api's, the following published collection can be used.

https://documenter.getpostman.com/view/10156058/2s9Xy2NrR6#68bad8f1-b3e0-480c-a161-89f3bca72a56

The collection has also been added in the root directory by the name `GoGLOCAL.postman_collection.json`. This can be imported directly into postman and can be used.