# Keychain Collector App
## Project Description
Keychain collector is a web application built with Django, designed for keychain lovers. It allows users to manage their keychains by documenting important details for each keychain such as acquisition date and location, material, theme, story and images. These details help preserving the memories associated with each one.

## Features
- **User Authentication**: Secure sign up and login
- **Keychain Management**: 
    - View all keychains associated with the user account.
    - Easily add new keychain.
    - Update the details of existing keychain.
    - Remove existing keychain.
    - Upload images for each keychain.

## Technologies 
* Visual Studio Code
* Python
* Django
* PostgreSQL

## Installation
### 1- Clone repository
```bash
git clone https://github.com/Reema1r/Keychain-Collector.git
```
### 2- Navigate to folder
```bash
cd Keychain-Collector
```
### 3- Create and activate virtual environment
```bash
pipenv shell
```
### 4- Install dependencies
```bash
pipenv install django djangorestframework psycopg2-binary
```
### 5- Apply migrations
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```
### 6- Create supperuser
```bash
python manage.py createsuperuser
```
### 7- Start the server
```bash
python manage.py runserver
```