from flask_restx import Resource, Namespace
from flask_jwt_extended import jwt_required

from ..models import create_user_model, create_recommendation_model, create_prediction_model
from ..controllers import UserController


user_namespace = Namespace("user", description="User related operations.")

user_model = create_user_model(user_namespace)
recommendation_model = create_recommendation_model(user_namespace)
prediction_model = create_prediction_model(user_namespace)


@user_namespace.route("/<int:id>")
class UserRouter(Resource):
    """
    A resource representing an individual user. Provides access to user data through the GET method.
    """

    @user_namespace.response(404, "User not found")
    @user_namespace.marshal_with(user_model)
    @jwt_required()
    def get(self, id):
        """
        Retrieve user data by ID.

        :param id: The ID of the user.
        :type id: int

        :return: A dictionary containing user data with the following keys:
                    - id (int): User ID.
                    - name (str): User's name.
                    - surname (str): User's surname.
                    - email (str): User's email.
                    - ratings (list[dict[str, any]]): Dictionary of user's movie ratings.
        :rtype: dict[str, any]
        """
        user_controller = UserController(id)

        user_response = user_controller.get_data()

        if user_response is None:
            return {"message": "User not found"}, 404

        return user_response, 200


@user_namespace.route("/<int:id>/recommendations")
class UserRecsRouter(Resource):
    """
    A resource representing movie recommendations for a user. Provides access to user-specific recommendations
    through the GET method.
    """

    @user_namespace.response(404, "User not found")
    @user_namespace.marshal_list_with(recommendation_model)
    @jwt_required()
    def get(self, id):
        """
        Retrieve movie recommendations for a user by ID.

        :param id: The ID of the user.
        :type id: int

        :return: A list of dictionaries, where each dictionary contains:
                    - id (int): Movie ID.
                    - title (str): Movie title.
                    - category (str): Movie category.
                    - similar_user_id (int): ID of the similar user who has rated the movie.
                    - similar_user_rating (float): The rating of the movie of the similar user.
                    - similar_user_correlation (float): Spearman's correlation coefficient between the user
                                                        and the similar user.
        :rtype: list[dict[str, any]]
        """
        user_controller = UserController(id)

        recs_response = user_controller.get_recommendations()

        if recs_response is None:
            return {"message": "User not found"}, 404

        return recs_response, 200


@user_namespace.route("/<int:id>/prediction/<int:movie_id>")
class UserPredictionRouter(Resource):
    """
    A resource representing a predicted movie rating for a user. Provides access to predicted movie ratings
    through the GET method.
    """

    @user_namespace.response(404, "User or movie not found")
    @user_namespace.marshal_with(prediction_model)
    @jwt_required()
    def get(self, id, movie_id):
        """
        Retrieve a predicted movie rating for a user by user's ID and movie's ID.

        :param id: The ID of the user.
        :type id: int

        :param movie_id: The ID of the movie.
        :type movie_id: int

        :return: A dictionary, containing:
                    - user_id (int): The user's ID.
                    - user_predicted_rating (float): Predicted movie rating for the user.
        :rtype: dict[str, any]
        """
        user_controller = UserController(id)

        prediction_response = user_controller.get_predicted_movie_rating(movie_id)

        if prediction_response is None:
            return {"message": "User or movie not found"}, 404

        return prediction_response, 200
