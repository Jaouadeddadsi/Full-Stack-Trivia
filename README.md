# Full Stack Trivia

This project is a part of Fullstack Nanodegree with [Udacity](https://www.udacity.com/). It is a trivia full-stack web application. Users can:

- Display questions - both all questions and by category. Questions show the question, category, and difficulty rating by default and can show/hide the answer.
- Delete questions.
- Add questions.
- Search for questions based on a text query string.
- Play the quiz game, randomizing either all questions or within a specific category.

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

## Getting Started

- Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, http://127.0.0.1:5000/, which is set as a proxy in the frontend configuration.
- Authentication: This version of the application does not require authentication or API keys.

## Error Handling

Errors are returned as JSON objects in the following format:

```python
{
	"success": False,
	"error": 400,
	"message": "bad request"
}

```

The API will return three error types when requests fail:

- 400: Bad Request.
- 404: Not Fount.
- 422: Unprocessable.
- 405: Method Not Allowed.

## Endpoint Library

### GET /categories

- General:

      	- Returns success value, and an object of categories, object keys represent categories ids and values represent categories names

- Sample: curl http://127.0.0.1:5000/categories

```python
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "success": true
}

```

### GET /questions

- General:

  - Returns a list of questions objects, categories, current_category, success value, and total number of questions.
  - Results are paginated in groups of 10. Include a request argument to choose page number, starting from 1.

- Sample: `curl http://127.0.0.1:5000/questions?page=2`

```python
{
  "categories": {
    "1": "science",
    "2": "art",
    "3": "geography",
    "4": "history",
    "5": "entertainment",
    "6": "sports"
  },
  "current_category": null,
  "questions": [
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    },
    {
      "answer": "Escher",
      "category": 2,
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    },
    {
      "answer": "Mona Lisa",
      "category": 2,
      "difficulty": 3,
      "id": 17,
      "question": "La Giaconda is better known as what?"
    },
    {
      "answer": "One",
      "category": 2,
      "difficulty": 4,
      "id": 18,
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    },
    {
      "answer": "Jackson Pollock",
      "category": 2,
      "difficulty": 2,
      "id": 19,
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    },
    {
      "answer": "The Liver",
      "category": 1,
      "difficulty": 4,
      "id": 20,
      "question": "What is the heaviest organ in the human body?"
    },
    {
      "answer": "Alexander Fleming",
      "category": 1,
      "difficulty": 3,
      "id": 21,
      "question": "Who discovered penicillin?"
    },
    {
      "answer": "Blood",
      "category": 1,
      "difficulty": 4,
      "id": 22,
      "question": "Hematology is a branch of medicine involving the study of what?"
    },
    {
      "answer": "Scarab",
      "category": 4,
      "difficulty": 4,
      "id": 23,
      "question": "Which dung beetle was worshipped by the ancient Egyptians?"
    },
    {
      "answer": "Neil Gaiman",
      "category": 1,
      "difficulty": 5,
      "id": 25,
      "question": "Neverwhere"
    }
  ],
  "success": true,
  "total_questions": 22
}

```

### DELETE /questions/{question_id}

- General:

  - Deletes the question of the given ID if it exists. Returns the id of the deleted question and success value.

- Sample: `curl -X DELETE http://127.0.0.1:5000/questions/25`

```python
{
  "deleted": 25,
  "success": true
}

```

### POST /questions

- General:

  - Creates a new question using the submitted question, answer, difficulty and rating. Returns the id of the created question and success value.
  - Search questions using the submitted searchTerm. Returns searched questions objects, total of searched questions, current category and success value.

- Sample: - `curl -X POST http://127.0.0.1:5000/questions -H "Content-Type: application/json" -d '{"question": "who created linux", "answer": "Linus Torvalds", "difficulty": 5, "category": 1}'`

```python
{
	"created": 34,
    "success": true
}
```

- Search: `curl -X POST http://127.0.0.1:5000/questions -H "Content-Type: application/json" -d '{"searchTerm": "title"}'`

```python
{

	"current_category": null,
    "questions": [
      	  {
      	  "answer": "Maya Angelou",
      	  "category": 4,
      	  "difficulty": 2,
      	  "id": 5,
      	  "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
      	  },
      	  {
      	  "answer": "Edward Scissorhands",
      	  "category": 5,
      	  "difficulty": 3,
      	  "id": 6,
      	  "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
      	  }
    ],
		  "success": true,
		  "total_questions": 2
}

```

### GET /categories/{category_id}/questions

- General:

  - Returns a list of questions objects of the same category (category_id)), success value, total number of questions and current category type.

- Sample: `curl http://127.0.0.1:5000/categories/1/questions`

```python
{
  "current_category": "Science",
  "questions": [
    {
      "answer": "The Liver",
      "category": 1,
      "difficulty": 4,
      "id": 20,
      "question": "What is the heaviest organ in the human body?"
    },
    {
      "answer": "Alexander Fleming",
      "category": 1,
      "difficulty": 3,
      "id": 21,
      "question": "Who discovered penicillin?"
    },
    {
      "answer": "Blood",
      "category": 1,
      "difficulty": 4,
      "id": 22,
      "question": "Hematology is a branch of medicine involving the study of what?"
    },
    {
      "answer": "a",
      "category": 1,
      "difficulty": 1,
      "id": 33,
      "question": "q"
    },
    {
      "answer": "Linus Torvalds",
      "category": 1,
      "difficulty": 5,
      "id": 34,
      "question": "who created linux"
    }
  ],
  "success": true,
  "total_questions": 5
}
```

### POST /quizzes

- General: - Returns success value and a random question object from the submitted category and doesn't belong to the previous questions list.

- Sample: `curl -X POST http://127.0.0.1:5000/quizzes -H "Content-Type: application/json" -d '{"previous_questions": [], "quiz_category": {"id": 4, "type": "History"}}'`

```python
{
  "question": {
    "answer": "Maya Angelou",
    "category": 4,
    "difficulty": 2,
    "id": 5,
    "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
  },
  "success": true
}
```

# Author

    Jaouad Eddadsi

# Acknowledgments

Many thanks to Udacity for this amazing project
