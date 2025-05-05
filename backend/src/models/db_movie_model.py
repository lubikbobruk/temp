from sqlalchemy import text

from ..exts import db

# Valid parameters for sorting.
QUERY_SORT_PARAMS = {
    "abc": "asc", "zyx": "desc",

    "lowest": "asc", "highest": "desc",

    "oldest": "asc", "latest": "desc"
}


class Movie(db.Model):
    """
    The Movie class is a database model that represents a movie with various properties and methods.

    :ivar id: Unique identifier for each movie.
    :type id: int

    :ivar title: Title of the movie.
    :type title: str

    :ivar category: Category of the movie.
    :type category: str

    :ivar country: Country where the movie was produced.
    :type country: str

    :ivar year: Year when the movie was released.
    :type year: int

    :ivar main_actors: Main actors in the movie.
    :type main_actors: str

    :ivar description: Description of the movie.
    :type description: str

    :ivar ratings: A list of Rating objects associated with the movie.
                   Each Rating object represents a user's rating for the movie.
    :type ratings: list[rating]

    :ivar comments: A list of Comment objects associated with the movie.
                    Each Comment object represents a user's comment on the movie.
    :type comments: list[comment]
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), nullable=False)
    category = db.Column(db.String(30), nullable=False)
    country = db.Column(db.String(30), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    main_actors = db.Column(db.Text(), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    ratings = db.relationship("Rating", backref="movie", lazy=True)
    comments = db.relationship("Comment", backref="movie", lazy=True)

    def __repr__(self):
        """
        Returns a string representation of the Movie instance.

        :return: String, representation of the movie instance.
        :rtype: movie
        """
        return f"<Movie-{self.id}>"

    def save(self):
        """
        Adds and commits the current Movie instance to the database.
        """
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """
        Deletes and commits the current Movie instance from the database.
        """
        db.session.delete(self)
        db.session.commit()

    def get_id(self):
        """
        Get the unique identifier of the movie.

        :return: Movie's ID.
        :rtype: int
        """
        return self.id

    def get_data(self):
        """
        Returns a dictionary of movie data including the calculated average rating and a list of comments.

        :return: Dictionary, movie data. A dictionary containing movie data with the following keys:
                    - id (int): Movie ID.
                    - title (str): Movie title.
                    - category (str): Movie category.
                    - year (int): Movie filming year.
                    - main_actors (str): Main starring actors.
                    - description (str): Movie description.
                    - rating (float): Movie average calculated rating.
                    - comments (list[dict[str, any]]): Movie comments list with dicts.
        :rtype: dict[str, any]
        """
        return {
            "id": self.id,
            "title": self.title,
            "category": self.category,
            "country": self.country,
            "year": self.year,
            "main_actors": self.main_actors,
            "description": self.description,
            "rating": self._get_rating(),
            "comments": self._get_comments()
        }

    def get_preview_data(self):
        """
        Returns a dictionary of preview movie data including id, title, and category.

        :return: Dictionary, preview movie data. A dictionary containing movie data with the following keys:
                    - id (int): Movie ID.
                    - title (str): Movie title.
                    - category (str): Movie category.
        :rtype: dict[str, any]
        """
        return {"id": self.id, "title": self.title, "category": self.category}

    def _get_rating(self):
        """
        Returns the average rating of the movie.

        :return: Float, average rating of the movie.
        :rtype: float
        """
        return sum([rating.get_movie_rating() for rating in self.ratings]) / len(self.ratings) if self.ratings else 0

    def _get_comments(self):
        """
        Returns a list of dictionaries where each dictionary contains a user_id and a user_comment.

        :return: List of dictionaries, containing user_id and user_comment.
        :rtype: list[dict[str, any]]
        """
        return [{"user_id": comment.get_user_id(), "user_comment": comment.get_user_comment()}
                for comment in self.comments]

    @staticmethod
    def get_by_id(movie_id):
        """
        Retrieves a movie instance by its id.

        :param movie_id: Integer, unique identifier of the movie.
        :type movie_id: int

        :return: Movie instance or None if not found.
        :rtype: movie or None
        """
        return Movie.query.get(movie_id)

    @staticmethod
    def get_all():
        """
        Retrieves all movies and returns their preview data.

        :return: List of dictionaries, preview data of all movies.
        :rtype: list[dict[str, any]]
        """
        movies = Movie.query.all()
        return [movie.get_preview_data() for movie in movies]

    @staticmethod
    def validate_sort_parameters(sort_params):
        """
        Validates the sort parameters by checking if the keys and values are allowed.

        :param sort_params: Dictionary, sort parameters provided by the user.
        :type sort_params: dict

        :return: Boolean, True if the sort parameters are valid, False otherwise.
        :rtype: bool
        """
        for key, value in sort_params.items():
            if key not in ["title", "rating", "year", "country"] or value not in QUERY_SORT_PARAMS.keys():
                return False
        return True

    @staticmethod
    def sort_all(sort_params):
        """
        Sorts all movies based on the provided sort parameters and returns their preview data.

        :param sort_params: Dictionary, validated sort parameters provided by the user.
        :type sort_params: dict

        :return: List of dictionaries, sorted preview data of all movies.
        :rtype: list[dict[str, any]]
        """
        query = ", ".join(f"{key} {QUERY_SORT_PARAMS[value]}" for key, value in sort_params.items())
        movies_sorted = Movie.query.order_by(text(query)).all()
        return [movie.get_preview_data() for movie in movies_sorted]

    @staticmethod
    def format_recommendations(recommendations):
        """
        Format the raw movie recommendations by retrieving additional movie details.

        :param recommendations: The list of raw movie recommendations.
        :type recommendations: list[dict[str, any]]

        :return: The formatted movie recommendations with additional movie details.
        :rtype: list[dict[str, any]]
        """
        for rec in recommendations:
            movie = Movie.get_by_id(rec["id"])
            rec.update({"title": movie.title, "category": movie.category})

        return recommendations
