from flask import request
from flask_restx import Resource, Namespace
from flask_jwt_extended import jwt_required

from ..models import create_movie_model, create_preview_model, create_rating_model, create_comment_model
from ..controllers import MoviesController, MovieController


movies_namespace = Namespace("movies", description="Movies related operations.")

movie_model = create_movie_model(movies_namespace)
preview_model = create_preview_model(movies_namespace)
rating_model = create_rating_model(movies_namespace)
comment_model = create_comment_model(movies_namespace)


@movies_namespace.route('')
class MoviesRouter(Resource):
    """
    A class representing the movies route, responsible for handling operations related to retrieving all movies.
    """

    @movies_namespace.marshal_list_with(preview_model)
    @jwt_required()
    def get(self):
        """
        Gets data of all movies.

        :return: A list of dictionaries containing the following keys for each movie:
                    - id (int): Movie ID.
                    - title (str): Movie title.
                    - category (str): Movie category.
        :rtype: list[dict[str, any]]
        """
        movies_controller = MoviesController()

        movies_response = movies_controller.get_movies()

        return movies_response, 200


@movies_namespace.route("/sort")
class MoviesSortRouter(Resource):
    """
    A class representing the movies sort route, responsible for handling operations related to sorting movies.
    """

    @movies_namespace.response(400, "Invalid QUERY parameters")
    @movies_namespace.marshal_list_with(preview_model)
    @jwt_required()
    def get(self):
        """
        Gets all movies sorted by QUERY parameters.

        :return: A list of dictionaries containing the following keys for each sorted movie:
                    - id (int): Movie ID.
                    - title (str): Movie title.
                    - category (str): Movie category.
        :rtype: list[dict[str, any]]
        """
        movies_controller = MoviesController()

        sort_params = request.args.to_dict()

        if not movies_controller.validate_sort_parameters(sort_params):
            return {"message": "Invalid QUERY parameters."}, 400

        movies_sorted_response = movies_controller.get_movies_sorted(sort_params)

        return movies_sorted_response, 200


@movies_namespace.route("/movie/<int:id>")
class MovieRouter(Resource):
    """
    A class representing the movie route, responsible for handling operations related to a single movie.
    """

    @movies_namespace.response(404, "Movie not found")
    @movies_namespace.marshal_with(movie_model)
    @jwt_required()
    def get(self, id):
        """
        Gets a movie by its ID.

        :param id: The ID of the movie.
        :type id: int

        :return: A dictionary containing the following keys:
                    - id (int): Movie ID.
                    - title (str): Movie title.
                    - category (str): Movie category.
                    - country (str): Movie's country.
                    - year (int): Movie's release year.
                    - main_actors (str): Main actors in the movie.
                    - description (str): Movie description.
                    - rating (int): Movie's average rating.
                    - comments (list[dict[str, any]]): Dictionary of user's comments.
        :rtype: dict[str, any]
        """
        movie_controller = MovieController(id)

        movie_response = movie_controller.get_movie()

        if movie_response is None:
            return {"message": "Movie not found"}, 404

        return movie_response, 200


@movies_namespace.route("/movie/<int:id>/rate")
class MovieRateRouter(Resource):
    """
    A class representing the movie rate route, responsible for handling operations related to rating a movie.
    """

    @movies_namespace.expect(rating_model)
    @movies_namespace.response(404, "Movie not found")
    @movies_namespace.marshal_with(movie_model)
    @jwt_required()
    def put(self, id):
        """
        Adds a new rating for the movie by its ID.

        :param id: The ID of the movie.
        :type id: int

        :return: A dictionary containing the following keys:
                    - id (int): Movie ID.
                    - title (str): Movie title.
                    - category (str): Movie category.
                    - country (str): Movie's country.
                    - year (int): Movie's release year.
                    - main_actors (str): Main actors in the movie.
                    - description (str): Movie description.
                    - rating (int): Movie's average rating.
                    - comments (list[dict[str, any]]): Dictionary of user's comments.
        :rtype: dict[str, any]
        """
        movie_controller = MovieController(id)

        rate_data = request.get_json()

        movie_rate_response = movie_controller.rate_movie(rate_data.get("user_id"), rate_data.get("user_rating"))

        if movie_rate_response is None:
            return {"message": "Movie not found"}, 404

        return movie_rate_response, 200


@movies_namespace.route("/movie/<int:id>/comment")
class MovieCommentRouter(Resource):
    """
    A class representing the movie comment route, responsible for handling operations related to commenting on a movie.
    """

    @movies_namespace.expect(comment_model)
    @movies_namespace.response(404, "Movie not found")
    @movies_namespace.marshal_with(movie_model)
    @jwt_required()
    def put(self, id):
        """
        Adds a new comment for the movie by its ID.

        :param id: The ID of the movie.
        :type id: int

        :return: A dictionary containing the following keys:
                    - id (int): Movie ID.
                    - title (str): Movie title.
                    - category (str): Movie category.
                    - country (str): Movie's country.
                    - year (int): Movie's release year.
                    - main_actors (str): Main actors in the movie.
                    - description (str): Movie description.
                    - rating (int): Movie's average rating.
                    - comments (list[dict[str, any]]): Dictionary of user's comments.
        :rtype: dict[str, any]
        """
        movie_controller = MovieController(id)

        comment_data = request.get_json()

        movie_comment_response = movie_controller.comment_movie(comment_data.get("user_id"),
                                                                comment_data.get("user_comment"))

        if movie_comment_response is None:
            return {"message": "Movie not found"}, 404

        return movie_comment_response, 200
