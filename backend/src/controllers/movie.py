from ..models import Movie, Rating, Comment


class MovieController:
    """
    MovieController class for handling movie-related operations.

    :ivar movie: Instance of the Movie model.
    """

    def __init__(self, movie_id):
        """
        Initialize the MovieController with a movie ID.

        :param movie_id: The ID of the movie.
        :type movie_id: int
        """
        self.movie = Movie.get_by_id(movie_id)

    def get_movie(self):
        """
        Retrieve movie data.

        :return: None if the movie is not found, otherwise a dictionary containing movie data with the following keys:
                    - id (int): Movie ID.
                    - title (str): Movie title.
                    - category (str): Movie category.
                    - country (str): Movie's country.
                    - year (int): Movie's release year.
                    - main_actors (str): Main actors in the movie.
                    - description (str): Movie description.
                    - rating (int): Movie's average rating.
                    - comments (list[dict[str, any]]): Dictionary of user's comments.
        :rtype: dict[str, any] or None
        """
        return None if self.movie is None else self.movie.get_data()

    def rate_movie(self, user_id, user_rating):
        """
        Add a rating for the movie.

        :param user_id: The ID of the user providing the rating.
        :type user_id: int

        :param user_rating: The user's rating of the movie.
        :type user_rating: int

        :return: None if the movie is not found, otherwise an updated dictionary containing movie data:
                    - id (int): Movie ID.
                    - title (str): Movie title.
                    - category (str): Movie category.
                    - country (str): Movie's country.
                    - year (int): Movie's release year.
                    - main_actors (str): Main actors in the movie.
                    - description (str): Movie description.
                    - rating (int): Movie's average rating.
                    - comments (list[dict[str, any]]): Dictionary of user's comments.
        :rtype: dict[str, any] or None
        """
        if not self.movie:
            return None

        new_rating = Rating.create(self.movie.get_id(), user_id, user_rating)
        new_rating.save()

        return self.movie.get_data()

    def comment_movie(self, user_id, user_comment):
        """
        Add a comment for the movie.

        :param user_id: The ID of the user providing the comment.
        :type user_id: int

        :param user_comment: The user's comment for the movie.
        :type user_comment: str

        :return: None if the movie is not found, otherwise an updated dictionary containing movie data:
                    - id (int): Movie ID.
                    - title (str): Movie title.
                    - category (str): Movie category.
                    - country (str): Movie's country.
                    - year (int): Movie's release year.
                    - main_actors (str): Main actors in the movie.
                    - description (str): Movie description.
                    - rating (int): Movie's average rating.
                    - comments (list[dict[str, any]]): Dictionary of user's comments.
        :rtype: dict[str, any] or None
        """
        if not self.movie:
            return None

        new_comment = Comment.create(self.movie.get_id(), user_id, user_comment)
        new_comment.save()

        return self.movie.get_data()
