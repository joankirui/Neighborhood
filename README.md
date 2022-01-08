## Neighborhood
![Awards!](static/images/main.png)
## Author
[Joan Kirui](https://github.com/joankirui)

## Description

This is a neighborhood app where a user must signup first, be able to join a hood owned by the hood admin, and once you join a hood, one can see businesses and posts in only that hood they belong to.


## Live Link
<!-- To view site [click here](https://jkawards.herokuapp.com/) -->

## User Story
* Sign in with the application to start using.
* Set up a profile about me and a general location and my neighborhood name.
* Find a list of different businesses in my neighborhood.
* Find Contact Information for the health department and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood
* Change My neighborhood when I decide to move out.
* Only view details of a single neighborhood.

## Setup and Installation
    To get the project ...

### Cloning the repository:
    https://github.com/joankirui/Neighborhood.git

### Navigate into the folder and install requirements
    cd Neighborhood pip install -r requirements.txt

### Install and activate Virtual
    - python3.6 -m venv virtual 
    - source virtual/bin/activate  

# Setup Database 
* SetUp your database User,Password,Host then make migrate
   - python manage.py makemigrations neighbor

* Now Migrate 
   - python manage.py migrate 

* Run the application
   - python3.6 manage.py runserver

* Testing the application
   - python manage.py test

* Open the application on your browser 
   - 127.0.0.1:8000.

## Technology used
    python3.6
    Django 3.2.9
    Heroku

## Known Bugs
* There are no known bugs currently but pull requests are allowed incase you spot a bug

## Contact Information
    If you have any question or contributions, please email me at [joankirui99@gmail.com]

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Copyright © 2021  [JOAN KIRUI](https://github.com/joankirui)

