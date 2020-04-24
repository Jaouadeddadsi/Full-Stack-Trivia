import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10


def paginate_questions(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    questions = [question.format() for question in selection]
    current_questions = questions[start:end]

    return current_questions


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    cors = CORS(app, resources={r"/*": {"origins": "*"}})

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type, Authorization, true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PATCH,POST,DELETE,OPTIONS')
        return response

    @app.route('/categories')
    def get_categories():
        try:
            categories = {}
            for cat in Category.query.order_by(Category.id).all():
                categories[cat.id] = cat.type

            return jsonify({
                "success": True,
                "categories": categories
            })
        except:
            abort(422)

    @app.route('/questions')
    def get_questions():
        page_exist = True
        try:
            selection = Question.query.order_by(Question.id).all()
            current_questions = paginate_questions(request, selection)

            if len(current_questions) == 0:
                page_exist = False
                raise Exception('page not found')
            current_category = list(set([q["category"]
                                         for q in current_questions]))
            categories = {}
            for cat in Category.query.all():
                categories[cat.id] = cat.type.lower()
            return jsonify({
                "success": True,
                "questions": current_questions,
                "total_questions": len(selection),
                "current_category": current_category,
                "categories": categories
            })
        except:
            if not page_exist:
                abort(404)
            abort(422)

    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_question(question_id):
        question_found = True
        try:
            question = Question.query.filter(
                Question.id == question_id).one_or_none()
            if question is None:
                question_found = False
                raise Exception("Question Not found")
            question.delete()
            return jsonify({
                "success": True,
                "deleted": question_id
            })
        except:
            if not question_found:
                abort(404)
            abort(422)

    @app.route("/questions", methods=['POST'])
    def add_question():
        search_found = True
        body = request.get_json()
        question = body.get('question', None)
        answer = body.get('answer', None)
        difficulty = body.get('difficulty', None)
        category = body.get('category', None)
        searchTerm = body.get('searchTerm', None)

        try:
            if searchTerm:
                selection = Question.query.filter(
                    Question.question.like(f'%{searchTerm}%')).all()
                if len(selection) == 0:
                    search_found = False
                    raise Exception("not found")
                search_questions = [question.format()
                                    for question in selection]
                categories = [question['category'] for question in
                              search_questions]
                current_category = list(set(categories))

                return jsonify({
                    "success": True,
                    "questions": search_questions,
                    "total_questions": len(search_questions),
                    "current_category": current_category
                })

            new_question = Question(
                question=question, answer=answer, category=category,
                difficulty=difficulty)
            new_question.insert()
            return jsonify({
                "success": True,
                "created": new_question.id
            })
        except:
            if not search_found:
                abort(404)
            abort(422)

    @app.route('/categories/<int:category>/questions')
    def get_question_by_cat(category):
        try:
            selection = Question.query.filter(
                Question.category == category).all()
            questions = [question.format() for question in selection]
            current_category = Category.query.get(category).type
            return jsonify({
                "success": True,
                "questions": questions,
                "total_questions": len(selection),
                "current_category":  current_category
            })
        except:
            abort(422)

    @app.route('/quizzes', methods=['POST'])
    def get_quiz_questions():
        body = request.get_json()
        previous_questions = body.get('previous_questions', [])
        quiz_category = body.get('quiz_category', {})
        try:
            selection = Question.query.filter(
                Question.category == quiz_category['id']).all()
            questions = list(filter(
                lambda x: x.id not in previous_questions, selection))
            question = random.choice(questions)

            return jsonify({
                "success": True,
                "question": question.format()
            })

        except:
            abort(422)

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "not found"
        }), 404

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(405)
    def not_allowed(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "method not allowed"
        }), 405

    return app
