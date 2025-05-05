from flask import request
from flask_restx import Resource, Namespace
from flask_jwt_extended import jwt_required

from controllers.movies import MoviesController, MovieController
from models.serialization_models import (
    create_book_model        as create_movie_model,
    create_book_preview_model as create_preview_model,
    create_rating_model,
    create_comment_model,
)

movies_namespace = Namespace("movies", description="Books related operations.")

movie_model   = create_movie_model(movies_namespace)
preview_model = create_preview_model(movies_namespace)
rating_model  = create_rating_model(movies_namespace)
comment_model = create_comment_model(movies_namespace)


@movies_namespace.route('')
class MoviesRouter(Resource):
    @movies_namespace.marshal_list_with(preview_model)
    @jwt_required()
    def get(self):
        """
        GET /movies
        Return a list of all books (id, title, author).
        """
        ctrl = MoviesController()
        return ctrl.get_books(), 200


@movies_namespace.route('/sort')
class MoviesSortRouter(Resource):
    @movies_namespace.response(400, "Invalid query parameters")
    @movies_namespace.marshal_list_with(preview_model)
    @jwt_required()
    def get(self):
        """
        GET /movies/sort?year=latest&title=abc
        Return sorted books by query parameters.
        """
        ctrl = MoviesController()
        params = request.args.to_dict()
        if not ctrl.validate_sort_parameters(params):
            return {"message": "Invalid query parameters."}, 400
        return ctrl.get_books_sorted(params), 200


@movies_namespace.route('/<int:id>')
class MovieRouter(Resource):
    @movies_namespace.response(404, "Book not found")
    @movies_namespace.marshal_with(movie_model)
    @jwt_required()
    def get(self, id):
        """
        GET /movies/<id>
        Return full details for a single book.
        """
        ctrl = MovieController(id)
        book = ctrl.get_book()
        if book is None:
            return {"message": "Book not found"}, 404
        return book, 200


@movies_namespace.route('/<int:id>/rate')
class MovieRateRouter(Resource):
    @movies_namespace.expect(rating_model)
    @movies_namespace.response(404, "Book not found")
    @movies_namespace.marshal_with(movie_model)
    @jwt_required()
    def put(self, id):
        """
        PUT /movies/<id>/rate
        Body: { "user_id": X, "book_rating": 4.2 }
        Add or update a rating for this book.
        """
        ctrl = MovieController(id)
        data = request.get_json()
        updated = ctrl.rate_book(data.get("user_id"), data.get("book_rating"))
        if updated is None:
            return {"message": "Book not found"}, 404
        return updated, 200


@movies_namespace.route('/<int:id>/comment')
class MovieCommentRouter(Resource):
    @movies_namespace.expect(comment_model)
    @movies_namespace.response(404, "Book not found")
    @movies_namespace.marshal_with(movie_model)
    @jwt_required()
    def put(self, id):
        """
        PUT /movies/<id>/comment
        Body: { "user_id": X, "user_comment": "Great read!" }
        Add or update a comment for this book.
        """
        ctrl = MovieController(id)
        data = request.get_json()
        updated = ctrl.comment_book(data.get("user_id"), data.get("user_comment"))
        if updated is None:
            return {"message": "Book not found"}, 404
        return updated, 200
