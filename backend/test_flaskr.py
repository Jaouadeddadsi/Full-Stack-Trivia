import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


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

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    def test_get_questions(self):
        res = self.client().get("/questions?page=1")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["questions"])
        self.assertEqual(len(data["questions"]), 10)
        self.assertTrue(data["total_questions"])
        self.assertTrue(data["current_categories"])
        self.assertEqual(len(data["current_categories"]), 4)
        self.assertTrue(data["categories"])
        self.assertEqual(len(data["categories"]), 6)

    def test_get_questions_page_not_found(self):
        pass
    '''
    Delete question
    '''

    def test_delete_question(self):
        res = self.client().delete("/questions/26")
        data = json.loads(res.data)

        self.assertEqual(data["success"], True)
        self.assertEqual(data["deleted"], 26)

    def test_delete_question_not_found(arg):
        pass

    '''
    Post question
    '''

    def test_create_question(self):
        res = self.client().post('/questions',
                                 json={"question": "Q1", "answer": "A1",
                                       "difficulty": 2, "category": 1})
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
