# Awwards
This is a repository for an app that allows users to post projects they have completed and other users are able to see the projects and rate them out of ten

#### By **[PETER KINYANJUI]**

## Description
This is a simple web apllication. A user can create an account and sign into it.
The site supports uploading projects and other users can see the projects posted by various users and rate them 

## Set Up and Installations

### Prerequisites
1. Django
2. Python3.6
3. [Postgres](https://www.postgresql.org/download/)
4. [python virtualenv](https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b)

### Clone the Repo
Run the following command on the terminal:
* git clone https://github.com/KIKIKILOKJ/Awwards.git 
* cd awwards

### Activate virtual environment
Activate virtual environment using python3.6 as default handler
bash
* virtualenv -p /usr/bin/python3.6 venv 
* source venv/bin/activate

### Install dependancies
Install dependancies that will create an environment for the app to run
pip3 install -r requirements.txt

### Create the Database
bash
psql
CREATE DATABASE awards;

### .env file
Create .env file and paste paste the following filling where appropriate:
python
* SECRET_KEY = '<Secret_key>'
* DBNAME = 'awards'
* USER = '<Username>'
* PASSWORD = '<password>'
* DEBUG = True


### Run initial Migration
bash
 * python3.6 manage.py makemigrations AWWARDS
 * python3.6 manage.py migrate

### Run the app
bash
* python3.6 manage.py runserver
* Open terminal on localhost:8000
* Testing the Application
To run the tests for the class files:
   * $ python3.6 manage.py test

## Technologies used
   - Python 3.6
   - HTML
   - Bootstrap 4
   - JavaScript
   - Heroku
   - Postgresql

## BDD
| Behavior           | Input                 | Outcome                            |
| -------------------|-----------------------| -----------------------------------|
| Create account       | add credentials to register | credentials are saved to database         |
|Login| add registered credentials to login page   |    user is logged in   |
|View Projects       |Go to index to view  | All projects are shown|
|Post new project     | Add details of post  | project is added         |
|View profile       | Click on profile  | image is added         |

## Support and contact details
Contact me on petermax2004@gmail.com for any comments, reviews or advice.

### License
[MIT](LICENSE)
Copyright (c) 2019 **PETER KINYANJUI**
