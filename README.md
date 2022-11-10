# Store APIs  module.
This Project is e-commerce API.

This API has been made for a simple small scale e-commerce businesses.
<br/>

# Basic functionality
1. Login and Registration.
2. Add new Products and show it in admin (product fields are: name, price). 
3. List all products ordered by price.
4. Search for products by name
5. Add products to cart.
6. Get user cart.
7. Create order with products in the cart.
8. Get user orders.

<br/>

# Getting started

## Installation

make a new folder for the project and open this folder in the Terminal/Windows (PowerShell) and run this command

``` bash
git clone https://github.com/omar-bendary/Store-Task-Bit68.git
```

# Pre-requisites and Local Development
# Using Docker and Docker compose

The first step is to sign up for
a free account on [DockerHub](https://hub.docker.com/signup)  and then install the Docker desktop app on your local machine:
* [Docker for Mac](https://docs.docker.com/desktop/install/mac-install/)
* [Docker for Windows](https://docs.docker.com/desktop/install/windows-install/)
Once Docker is done installing we can confirm the correct version is running by typing the
command docker --version in the command line shell
```shell
$ docker --version
Docker version 20.10.14, build a224086
```
### Running our container
1- Open the project Code folder in Terminal/Windows (PowerShell).

2- Run this command .
```bash
docker-compose up -d --build
```

### To Stop the currently running container
Control+c (press the “Control” and “c” button at
the same time) and additionally type docker-compose down.
```shell
docker-compose down
```
### Now let’s confirm everything is working
```bash
docker-compose exec web python manage.py  makemigrations 
```
```bash
docker-compose exec web python manage.py  migrate 
```
> Now create the admin user
```bash
 docker-compose exec web python manage.py createsuperuser 
```
The application is run on http://127.0.0.1:8000/

###  Set up your RDBMS , open your setting.py
```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "db",  # set in docker-compose.yml
        "PORT": 5432,  # default postgres port
    }
}
```
<br/>

# Using virtual environment approach.
## To create a virtual environment 

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install packages.

1- Open the project Code folder in Terminal/Windows (PowerShell).

2- Run this command .
```bash
# Windows
> python -m venv .venv
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# macOS
% python3 -m venv .venv
```

### To activate a new virtual environment called .venv:

```bash
# Windows
> .venv\Scripts\Activate.ps1
(.venv) >

# macOS
% source .venv/bin/activate
(.venv) %
```

### To deactivate and leave a virtual environment type deactivate.

```bash
# Windows
(.venv) > deactivate
>

# macOS
(.venv) % deactivate
%
```

### install requirements.txt


Run `pip install requirements.txt`. All required packages are included in the requirements file.

> make sure to activate the virtual environment first
```bash
pip install -r requirements.txt
```

**You might see a WARNING message about updating pip after running these commands. It’s always good to be on the latest version of software and to remove the annoying WARNING message each time you use pip. You can either copy and paste the recommended command or run `python -m pip install --upgrade pip` to be on the latest version.**

```bash
(.venv) > python -m pip install --upgrade pip
```

## Now let’s confirm everything is working by running Django’s internal web server via the runserver command

```bash
(.venv) > python manage.py  makemigrations 
```
```bash
(.venv) > python manage.py  migrate 
```
> Now create the admin user
```bash
(.venv) > python manage.py createsuperuser 
```
Run the surver
```bash
# Windows
(.venv) > python manage.py runserver

# macOS
(.venv) % python3 manage.py runserver
```

## Set up your RDBMS , open your setting.py
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DB_NAME',
        'USER': 'DB_USER',
        'PASSWORD': 'DB_PASSWORD',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}
```

The application is run on http://127.0.0.1:8000/ by default in the backend configuration.

**Open http://127.0.0.1:8000/ your web browser**

<br/>


# API Reference

## Getting Started
Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, http://127.0.0.1:8000/, which is in the backend configuration.

<br/>

## Endpoints
### GET /auth/users/
* General:
  * Create a new user.
  * Returns user information if it was created successfully.
* Sample: `curl http://127.0.0.1:8000/auth/users/ -X POST -H "Content-Type: application/json" -d '{"username": "testuser","email": "test@gmail.com","password": "MyPassword", "first_name": "test","last_name": "user"}'`

```json
{
    "id": 2,
    "username": "testuser",
    "email": "test@gmail.com",
    "first_name": "test",
    "last_name": "user"
}
```
<br/>

### POST /auth/jwt/create/
* General:
  * Login a user to the system by creating access and refresh tokens.
  * Returns user access and refresh tokens (to use it for logging-in) if it was created successfully.
* `curl http://127.0.0.1:8000/auth/jwt/create/ -X POST -H "Content-Type: application/json" -d '{"username": "testuser", "password": "MyPassword"}'`

```json
{
  {
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2NzY5NTY4NiwianRpIjoiZDI0MzkzNmM0MGFkNDcxMmEyNGI5N2M5YjIxNWI1ZjciLCJ1c2VyX2lkIjoxfQ.J_YiVMoPBuRK0qHSoLoOy8FrnPM0FFydztEu3qQ_Wy8",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY3Njk1Njg2LCJqdGkiOiI5NTY4MGEyNjkyZDg0ZmJhOTlhNzU1NDhkZjQ5ZDc1NyIsInVzZXJfaWQiOjF9.AsdT7UfJTtXlkgKk3Xmhghz3Arz3yytU024wB25w-Nw"
}
}
```

>To keep your user logged-in , use an extention like [Moheader](https://modheader.com/)

- - - -
<br/>

### GET /store/products/
* General:
  * Returns a list of all stored products (Order by price) that you added in the admin panel  with your admin user
link - Created at - Last scraped at - Last scraped by )
* Sample: `curl http://127.0.0.1:8000/store/products/`

```json
[
    {
        "id": 1,
        "name": "Toy",
        "price": "10.00"
    },
    {
        "id": 2,
        "name": "Bed",
        "price": "1200.00"
    }
]
```
<br/>

### GET /store/products/?search={product_name}
* General:
  * Returns a list of all products searched by product name
* Sample: `curl http://127.0.0.1:8000/store/products/?search=toy`
```json
[
    {
        "id": 1,
        "name": "Toy",
        "price": "10.00"
    }
]
```

### POST /store/carts/
* General:
  * Create a cart for a user.
  * Returns cart_created=True and the cart_id
  * Note :<mark>User must be authenticated</mark>.
* `curl http://127.0.0.1:8000/store/carts/ -X POST -H 'Accept: application/json' -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY4MTY3ODYxLCJqdGkiOiI1NGVjY2I5Zjc2MjY0OGQ5YmU2ZjQwNjBkNDY2Y2ExZCIsInVzZXJfaWQiOjJ9.5K-I471R8DuXtkLRHFFG03LEsQuqevZStflyJhv0Exo"`

```json
{
    "cart_created": true,
    "cart_id": "8305e67d-4f30-4c38-b347-39776676d4cf"
}        
      
```
* Case1:
  * If a cart already exits it.Returns cart_already_exists= True and the cart_id
  * Note :<mark>User must be authenticated</mark>.
* `curl http://127.0.0.1:8000/store/carts/ -X POST -H 'Accept: application/json' -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY4MTY3ODYxLCJqdGkiOiI1NGVjY2I5Zjc2MjY0OGQ5YmU2ZjQwNjBkNDY2Y2ExZCIsInVzZXJfaWQiOjJ9.5K-I471R8DuXtkLRHFFG03LEsQuqevZStflyJhv0Exo"`
```json
{
    "cart_already_exists": true,
    "cart_id": "8305e67d-4f30-4c38-b347-39776676d4cf"
}   
```
        
* Case2:
  * If the user is not authenticated (anonymous user).Returns detail=Authentication credentials were not provided.
* `curl http://127.0.0.1:8000/store/carts/ -X POST `

```json
{
    "detail": "Authentication credentials were not provided."
}
      
```
<br/>

### GET /store/carts/{cart_id}/
* General:
  * Return cart_id and a list of items
  * Return list of items in the cart. each item is a dictionary of item details.
  * Return total price of the cart.
  * Note :<mark>User must be authenticated</mark>.
* Sample: `curl http://127.0.0.1:8000/store/carts/8305e67d-4f30-4c38-b347-39776676d4cf/`

```json
{
    "id": "8305e67d-4f30-4c38-b347-39776676d4cf",
    "items": [
        {
            "id": 2,
            "product": {
                "id": 1,
                "name": "Toy",
                "price": "10.00"
            },
            "quantity": 12,
            "total_price": 120.0
        },
        {
            "id": 3,
            "product": {
                "id": 2,
                "name": "Bed",
                "price": "1200.00"
            },
            "quantity": 10,
            "total_price": 12000.0
        }
    ],
    "total_price": 12120.0
}
```

### DELETE /store/carts/{cart_id}/
* General:
  * Deletes the cart with given ID if it exists.
  * Note :<mark>User must be authenticated</mark>.
* `curl -X DELETE http://127.0.0.1:8000/store/carts/8305e67d-4f30-4c38-b347-39776676d4cf/`

<br/>

### GET /store/carts/{cart_id}/items/
* General:
  * Return list of items in the cart with given ID if it exists.
  * Each item is a dictionary of item details.
  * Note :<mark>User must be authenticated</mark>.
* Sample: `curl http://127.0.0.1:8000/store/carts/f41bb933-fb99-4e29-869d-15baf87ae23c/items/`

```json
[
    {
        "id": 6,
        "product": {
            "id": 1,
            "name": "Toy",
            "price": "10.00"
        },
        "quantity": 15,
        "total_price": 150.0
    },
    {
        "id": 7,
        "product": {
            "id": 2,
            "name": "Bed",
            "price": "1200.00"
        },
        "quantity": 20,
        "total_price": 24000.0
    }
]
```

### POST /store/carts/{cart_id}/items/
* General:
  * Creates a cart_item and adds it to the cart with given ID if it exists.
  * Returns a dictionary of the created item id, product_id and quantity.
  * If the item already exits in the cart it updates the quantity by adding the new quantity to the existing quantity. 
  * Note :<mark>User must be authenticated</mark>.
* `curl http://127.0.0.1:8000/store/carts/f41bb933-fb99-4e29-869d-15baf87ae23c/items/ -X POST -H "Content-Type: application/json" -d '{"product_id" : 3, "quantity": 1}'`

```json
{
    "id": 8,
    "product_id": 3,
    "quantity": 1
}
```
### PATCH /store/carts/{cart_id}/items/{cart_item_id}/
* General:
  * Updates the quantity for cart_item with given ID if it exists.
  * Returns a dictionary of the new quantity.
  * Note :<mark>User must be authenticated</mark>.
* `curl http://127.0.0.1:8000/store/carts/f41bb933-fb99-4e29-869d-15baf87ae23c/items/6/ -X PATCH -H "Content-Type: application/json" -d '{"quantity": 1}'`

```json
{

"quantity": 20

}
```
### GET /store/orders/
* General:
  * Returns a list of user orders.
  * If the user is an Admin it.Returns list of all users orders.
  * Each list item is a dictionary of order details.
  * Note :<mark>User must be authenticated</mark>.
* Sample: `curl http://127.0.0.1:8000/store/orders/`

```json
[
    {
        "id": 2,
        "placed_at": "November 10, 2022 - (02:43) PM",
        "user": 2,
        "items": [
            {
                "product": 1,
                "quantity": 20,
                "unit_price": "10.00"
            },
            {
                "product": 2,
                "quantity": 20,
                "unit_price": "1200.00"
            },
            {
                "product": 3,
                "quantity": 2,
                "unit_price": "30000.00"
            }
        ]
    }
]
```
### POST /store/orders/
* General:
  * Creates an order for the user.
  * Returns a dictionary of order details.
  * Removes all the items of cart and the cart becomes empty. 
  * If the cart is already empty.Return "The cart is empty.".
  * Note :<mark>User must be authenticated</mark>.
* `curl http://127.0.0.1:8000/store/orders/ -X POST`

```json
{
    "id": 3,
    "placed_at": "November 10, 2022 - (03:04) PM",
    "user": 2,
    "items": [
        {
            "product": 1,
            "quantity": 22,
            "unit_price": "10.00"
        }
    ]
}
```

### GET /store/orders/{order_id}
* General:
  * Returns a dictionary of order details for order with given ID if it exists.
  * Note :<mark>User must be authenticated</mark>.
* Sample: `curl http://127.0.0.1:8000/store/orders/3/`

```json
{
    "id": 3,
    "placed_at": "November 10, 2022 - (03:04) PM",
    "user": 2,
    "items": [
        {
            "product": 1,
            "quantity": 22,
            "unit_price": "10.00"
        }
    ]
}
```

### DELETE /store/orders/{order_id}
* General:
  * Deletes an order with given ID if it exists.
  * Note :<mark>User must be authenticated and Admin user</mark>.
* `curl -X DELETE http://127.0.0.1:8000/store/orders/3/`

# Deployment N/A

<br/>

# Authors
Omar Bendary