## 🔧 What This App Uses

This application uses Docker as a containerization tool and PostgreSQL as the database in local development.
In production, it uses the Heroku PostgreSQL database provided by Heroku.
The app can be deployed to Heroku, making it a fully functional production website that anyone can access.

## 📝 General Description of the To-Do App

This is a To-Do application where users can:

- Create tasks
- Add descriptions to tasks
- Edit their own tasks
- Delete their own tasks

Users can:

- Register (Sign Up)
- Log in / Log out
- Change their username or password (after logging in)
- Verify their email address
- Reset their password using the "Forgot Password?" feature
- Switch the language between English and Georgian

## 🏗 Project Structure

The project contains two main Django apps:

1 note – Handles creating, editing, and deleting tasks.
2 api – Provides REST API functionality using Django REST Framework (DRF).

## 🛠 Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- Docker & Docker Compose
- Heroku (Production)
- JWT Authentication
