# Full Stack Trivia

This project is a part of Fullstack Nanodegree with [Udacity](https://www.udacity.com/). It is a trivia full-stack web application. Users can:

     1. Display questions - both all questions and by category. Questions show the question, category, and difficulty rating by default and can show/hide the answer.
    2. Delete questions.
    3. Add questions.
    4. Search for questions based on a text query string.
    5. Play the quiz game, randomizing either all questions or within a specific category.

The frontend use [Reactjs](https://reactjs.org/) and the backend use [Flask](https://flask.palletsprojects.com/en/1.1.x/)

![app img](app.png)

All backend code follows [PEP8 style guidelines](https://www.python.org/dev/peps/pep-0008/).

# Getting started

## Pre-requisites and Local Development

Developers using this project should already have Python3, pipenv, pip and node installed on their local machines

## Backend

### PIP Dependencies

From the backend folder run `pip install`. All required packages are included in the `Pipfile` file.

#### Key Dependencies

- [Flask](https://flask.palletsprojects.com/en/1.1.x/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.
- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.
- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

### Database Setup

With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:

```shell
	psql trivia < trivia.psql
```

### Running the server

To run the application run the following commands:

```shell
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

These commands put the application in development and directs our application to use the `__init__.py` file in our flaskr folder. Working in development mode shows an interactive debugger in the console and restarts the server whenever changes are made. If running locally on Windows, look for the commands in the [Flask documentation](https://flask.palletsprojects.com/en/1.1.x/tutorial/factory/).

The application is run on http://127.0.0.1:5000/ by default and is a proxy in the frontend configuration.

## Frontend

From the frontend folder, run the following commands to start the client:

```shell
npm install // only once to install dependencies
npm start
```

By default, the frontend will run on `localhost:3000`.

## Tests

In order to run tests navigate to the backend folder and run the following commands:

```shell
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```

The first time you run the tests, omit the dropdb command.

All tests are kept `test_flaskr.py` file and should be maintained as updates are made to app functionality.

# API Reference
