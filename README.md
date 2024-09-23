Thrift App - Django Application

Overview

Thrift App is a simple hypothetical store management system that allows you to manage customer data and track orders. The application includes the following key features:

1.A customer and order management system with a REST API.

2.OpenID Connect (OIDC) authentication and authorization via Auth0.

3.SMS notifications sent to customers when an order is created, using the Africa's Talking SMS gateway.

Features

1.Customers and Orders Database

.  Customers: Contains basic details such as customer name and a unique code.

.  Orders: Stores details such as the item name, order amount, and the time the order was placed.

2.REST API

.  Customers API: Endpoints for creating, retrieving, updating, and deleting customers.

.  Orders API: Endpoints for managing orders, including the ability to create and view orders.

.  The API follows REST principles, allowing CRUD operations for both customers and orders.

3.Authentication & Authorization

. OpenID Connect (OIDC) via Auth0 for secure authentication.

. Users must log in through Auth0 to access the API endpoints, ensuring only authenticated users can create and manage customers and orders.

4.SMS Notifications

.  When a new order is placed, an SMS notification is sent to the customer using the Africa's Talking SMS gateway.

.  This feature enhances user engagement by keeping customers informed of their orders in real-time.

Project Setup

Prerequisites:

. Python 3.x

. Django 4.x

. Auth0 Account for OpenID Connect

. Africa's Talking account for SMS integration

. If you don't have an AuthO account,please Sign up here:https://auth0.com/

Installation

1.Clone the repository

git clone https://github.com/your-repo/thrift-app.git

cd thrift-app

2.Setup virtual environment

python -m venv env
source env/bin/activate  

3.Install dependencies

pip install -r requirements.txt

4.Set up environment variables

Create a .env file at the root of your project and configure the following environment variables:

SECRET_KEY=<your-django-secret-key>

AUTH0_DOMAIN=<your-auth0-domain>

AUTH0_CLIENT_ID=<your-auth0-client-id>

AUTH0_CLIENT_SECRET=<your-auth0-client-secret>

AFRICASTALKING_USERNAME=<your-africastalking-username>

AFRICASTALKING_API_KEY=<your-africastalking-api-key>

5.Run migrations

python manage.py migrate

6.Run the server

python manage.py runserver

Usage

Api Endpoints

1.Customer API
. GET /api/customers/ - List all customers

. POST /api/customers/ - Add a new customer

. GET /api/customers/{id}/ - Retrieve a specific customer

. PUT /api/customers/{id}/ - Update a customer

. DELETE /api/customers/{id}/ - Delete a customer

2.Order API
. GET /api/orders/ - List all orders

. POST /api/orders/ - Add a new order

. GET /api/orders/{id}/ - Retrieve a specific order

. PUT /api/orders/{id}/ - Update an order

. DELETE /api/orders/{id}/ - Delete an order

Authentication

. Users must log in using their Auth0 credentials to access the API.

. Token-based authentication is required for all API requests.

SMS Notification

. Upon adding a new order, the system automatically sends an SMS to the customer using Africa's Talking API.

Technologies Used

. Django: Backend framework for building the API.

. Django REST Framework: For RESTful API design.

. Auth0: OIDC authentication for secure user login.

. Africa's Talking: SMS gateway integration for sending SMS notifications.