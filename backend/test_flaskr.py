import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres:///{}".format(self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    '''
    Questions
    '''

    def test_get_questions(self):
        res = self.client().get("/questions?page=1")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["questions"])
        self.assertEqual(len(data["questions"]), 10)
        self.assertTrue(data["total_questions"])
        self.assertTrue(data["categories"])
        self.assertEqual(len(data["categories"]), 6)

    def test_get_questions_page_not_found(self):
        res = self.client().get("/questions?page=1000")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "not found")
    '''
    Delete question
    '''

    def test_delete_question(self):
        question = Question(question="Q", answer="A",
                            category=1, difficulty=1)
        question.insert()
        res = self.client().delete(f'/questions/{question.id}')
        data = json.loads(res.data)

        self.assertEqual(data["success"], True)
        self.assertEqual(data["deleted"], question.id)

    def test_delete_question_not_found(self):
        res = self.client().delete("/questions/1000")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "not found")

    '''
    Add question
    '''

    def test_create_question(self):
        res = self.client().post('/questions',
                                 json={"question": "Q2", "answer": "A2",
                                       "difficulty": 2, "category": 1})
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)
        self.assertTrue(data["created"])

    '''
    Search Question
    '''

    def test_search_question(self):
        res = self.client().post('/questions',
                                 json={'searchTerm': 'title'})
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])
        self.assertTrue(data["total_questions"])

    '''
    Questions by category
    '''

    def test_question_by_cat(self):
        res = self.client().get('/categories/1/questions')
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])
        self.assertTrue(data['total_questions'])
    '''
    quiz
    '''

    def test_quizzes(self):
        res = self.client().post('/quizzes',
                                 json={'previous_questions': [],
                                       'quiz_category': {'id': 4, 'type': 'History'}
                                       }
                                 )
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)
        self.assertTrue(data['question'])

    def test_not_allowed(self):
        res = self.client().get('/quizzes')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 405)
        self.assertEqual(data['message'], 'method not allowed')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
