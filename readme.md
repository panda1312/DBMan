# SQL Manager Web App

A lightweight, containerized web application for managing a SQL (PostgreSQL) database, built with Flask and SQLAlchemy. Designed for easy development and production deployment using Docker and Gunicorn.

---

## 🚀 Features

- 📦 Containerized with Docker
- 🐍 Built with Flask
- 🛢️ PostgreSQL database integration
- 🔥 Hot reload during development
- 🚀 Gunicorn for production-ready performance
- 🌐 Clean, minimal UI
- 🛠️ Easy to deploy anywhere

---

## 📂 Project Structure

```plaintext
sql-manager/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── templates/
│   │   └── index.html
│   └── static/
│       └── style.css
├── run.py
├── docker/
│   └── web/
│       └── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
├── .gitignore
└── README.md
