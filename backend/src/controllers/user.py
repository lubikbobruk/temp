from ..models import User, Movie


class UserController:
    """
    UserController class for handling user-related operations.

    :ivar user: Instance of the User model.
    """
    def __init__(self, user_id):
        """
        Initialize the UserController with a user ID.

        :param user_id: The ID of the user.
        :type user_id: int
        """
        self.user = User.get_by_id(user_id)

    def get_data(self):
        """
        Retrieve user data.

        :return: None if the user is not found, otherwise a dictionary containing user data with the following keys:
                    - id (int): User ID.
                    - name (str): User's name.
                    - surname (str): User's surname.
                    - email (str): User's email.
                    - ratings (list[dict[str, any]]): Dictionary of user's movie ratings.
        :rtype: dict[str, any] or None
        """
        return None if not self.user else self.user.get_data()

    def get_recommendations(self):
        """
        Retrieve movie recommendations for the user.

        :return: None if the user is not found, otherwise a list of dictionaries, where each dictionary contains:
                    - id (int): Movie ID.
                    - title (str): Movie title.
                    - category (str): Movie category.
                    - similar_user_id (int): ID of the similar user who has rated the movie.
                    - similar_user_correlation (float): Spearman's correlation coefficient between the user
                                                        and the similar user.
        :rtype: list[dict[str, any]] or None
        """
        if not self.user:
            return None

        raw_recommendations = self.user.get_recommendations()
        full_recommendations = Movie.format_recommendations(raw_recommendations)

        return full_recommendations

    def get_predicted_movie_rating(self, movie_id):
        """
        This method retrieves a predicted movie rating for a specified movie ID. If the movie doesn't exist,
        it returns None.

        The method checks if the specified movie exists in the database. If the movie doesn't exist, it returns None.
        If the movie exists, the method calls get_predicted_movie_rating_by_movie_id() method of the User object
        with the specified movie ID.

        The User object's get_predicted_movie_rating_by_movie_id() method calculates the predicted rating based on
        a recommendation algorithm that leverages ratings from all users.

        :param movie_id: The ID of the movie for which the predicted rating is to be retrieved.
        :type movie_id: int

        :return: None if the movie doesn't exist or if the user doesn't exist,
                 otherwise the predicted rating for the specified movie with the following keys:
                    - user_id (int): The user's ID.
                    - user_predicted_rating (float): The prediction rating.
        :rtype: dict[str, any] or None
        """
        return None if not self.user or not Movie.get_by_id(movie_id) else \
            self.user.get_predicted_movie_rating_by_movie_id(movie_id)
