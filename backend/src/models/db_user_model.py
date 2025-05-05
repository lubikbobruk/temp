from flask_jwt_extended import create_access_token

from ..exts import db
from ..recsys import RecMechanism


class User(db.Model):
    """
    User Model represents a user in the system.

    :ivar id: User's unique identifier.
    :type id: int

    :ivar name: User's first name.
    :type name: str

    :ivar surname: User's last name.
    :type surname: str

    :ivar email: User's email. It should be unique among all users.
    :type email: str

    :ivar password: User's password.
    :type password: str

    :ivar ratings: A list with movie ratings.
    :type ratings: list[rating]
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    surname = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.Text(), nullable=False)
    ratings = db.relationship("Rating", backref="user", lazy=True)

    def __repr__(self):
        """
        String representation of the User instance.

        :return: String representing the user.
        :rtype: user
        """
        return f"<User-{self.id}>"

    def save(self):
        """
        Save the current instance of User to the database.
        """
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """
        Delete the current instance of User from the database.
        """
        db.session.delete(self)
        db.session.commit()

    def get_id(self):
        """
        Get the unique identifier of the user.

        :return: User's ID.
        :rtype: int
        """
        return self.id

    def get_data(self):
        """
        Get the user's data.

        :return: Dictionary with user's data. A dictionary containing user data with the following keys:
                    - id (int): User's ID.
                    - name (str): User's name.
                    - surname (str): User's surname.
                    - email (str): User's email address.
                    - ratings (list[dict[str, any]]): List of rating objects, the keys are movie ids (movie_id)
                      and movie ratings (movie_rating).
        :rtype: dict[str, any]
        """
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "email": self.email,
            "ratings": self._get_ratings()
        }

    def get_login_data(self):
        """
        Get the user's login data.

        :return: Dictionary with user's login data. A dictionary containing user data with the following keys:
                    - id (int): User's ID.
                    - name (str): User's name.
                    - surname (str): User's surname.
                    - email (str): User's email address.
                    - ratings (list[dict[str, any]]): List of rating objects, the keys are movie ids (movie_id)
                      and movie ratings (movie_rating).
                    - access_token (str): User's JWT access token.
        :rtype: dict[str, any]
        """
        login_data = self.get_data()
        login_data["access_token"] = create_access_token(identity=self.email)

        return login_data

    def get_recommendations(self):
        """
        Get movie recommendations for the user based on their preferences and the Spearman's correlation coefficients.

        This method utilizes a recommendation mechanism to calculate movie recommendations for the user.
        It first creates an instance of the RecMechanism class, passing in self (the current user)
        and all users in the system.
        The RecMechanism class calculates the Spearman's correlation coefficients between the current user
        and other users, and updates the correlations attribute of the current user.

        :return: A list of movie recommendations for the user. Each recommendation is represented as a dictionary
                 with the following keys:
                    - id (int): Movie ID.
                    - similar_user_id (int): ID of a user with similar preferences who rated the movie highly.
                    - similar_user_rating (float): The movie rating of the similar correlated user.
                    - similar_user_correlation (float): Spearman's correlation coefficient between the current user
                                                        and another user.
        :rtype: list[dict[str, any]]
        """
        rec_mechanism = RecMechanism(self, User.get_all())

        return rec_mechanism.get_recommendations()

    def get_predicted_movie_rating_by_movie_id(self, movie_id):
        """
        This method retrieves a predicted movie rating for a specified movie ID. The prediction is based on
        a recommendation mechanism that leverages ratings from all users.

        Here's how it works: a RecMechanism object is initialized with the current user and the list of all users.
        The RecMechanism's get_predicted_rating_for_movie() method is called with the specified movie ID.

        The RecMechanism's get_predicted_rating_for_movie() method calculates the predicted rating based on
        a specific recommendation algorithm (e.g., collaborative filtering, matrix factorization, etc.).

        :param movie_id: The ID of the movie for which the predicted rating is to be retrieved.
        :type movie_id: int

        :return: The predicted rating for the specified movie in dict with following keys:
                    - user_id (int): The user's ID.
                    - user_predicted_rating (float): The prediction value.
        :rtype: dict[str, any]
        """
        rec_mechanism = RecMechanism(self, User.get_all())
        prediction = {"user_id": self.get_id(),
                      "user_predicted_rating": rec_mechanism.get_predicted_rating_for_movie(movie_id)}

        return prediction

    def get_ratings(self):
        """
        Get the user's ratings.

        :return: User's ratings. The keys are movie IDs and the values are rating float values.
        :rtype: dict[int, float]
        """
        return {rating.get_movie_id(): rating.get_movie_rating() for rating in self.ratings}

    def get_mean_rating(self):
        """
        Calculates and returns the mean rating that the user has given to all rated movies.

        :return: The mean rating.
        :rtype: float
        """
        return 0 if len(self.ratings) == 0 else \
            sum(rating.get_movie_rating() for rating in self.ratings) / len(self.ratings)

    def get_neighbor(self, neighbor_id):
        """
        Get the neighboring user.

        :param neighbor_id: ID of the neighboring user.
        :type neighbor_id: int

        :return: User instance.
        :rtype: user
        """
        return User.get_by_id(neighbor_id)

    def validate_password(self, password):
        """
        Validate the user's password.

        :param password: Input password.
        :type password: str

        :return: Boolean indicating if the password is valid.
        :rtype: bool
        """
        return self.password == password

    def _get_ratings(self):
        """
        Get the user's ratings in a formatted way.

        :return: List of dictionaries with movie IDs and ratings. Each rating object contains following keys:
                    - movie_id (int): ID of the rated movie.
                    - movie_rating (float): Rating of the movie.
        :rtype: list[dict[str, any]]
        """
        return [{"movie_id": rating.get_movie_id(), "movie_rating": rating.get_movie_rating()}
                for rating in self.ratings]

    @staticmethod
    def get_by_id(user_id):
        """
        Returns a User instance associated with the provided user ID.

        :param user_id: The unique identifier associated with a user.
        :type user_id: int

        :return: Instance of the User model associated with the provided ID. If no user is found with the provided ID,
                 the method returns None.
        :type: user or None
        """
        return User.query.get(user_id)

    @staticmethod
    def get_by_email(user_email):
        """
        Returns a User instance associated with the provided email address.

        :param user_email: Email address of the user.
        :type user_email: str

        :return: Instance of the User model associated with the provided email. If no user is found with the provided
                 email, the method returns None.
        :type: user or None
        """
        return User.query.filter_by(email=user_email).first()

    @staticmethod
    def get_all():
        """
        Returns a list of all User instances in the database.

        :return: List of all User model instances.
        :type: list[user]
        """
        return User.query.all()
